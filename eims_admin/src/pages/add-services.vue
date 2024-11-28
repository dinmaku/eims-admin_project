    <template>
        <div class="bg-gray-200 w-full h-full">
        <div class="w-full h-[65px] bg-gray-100 mt-2 flex items-center justify-between px-5 shadow-lg">
        <h1 class="font-amaticBold font-extraLight text-3xl">
        Add Services
    </h1>
    </div>
    
    <div class="flex flex-row items-center m-5 space-x-5">
        <div class="flex justify-start w-52 h-20 bg-white rounded-lg shadow-lg px-2 items-center border-l-2 border-green-400 space-x-5">
            <img class="w-auto h-12" src="/img/box.png" alt="Vendor Image">
            <h2 class="font-amaticRegular text-4xl font-bold mb-0"> {{ totalPackages }} <span class = "text-sm antialiased text-gray-600">packages</span></h2>
        </div>
        <div class="flex justify-start w-52 h-20 bg-white rounded-lg shadow-lg px-2 items-center border-l-2 border-blue-400 space-x-5">
            <img class="w-auto h-12" src="/img/discount.png" alt="Vendor Image">
            <h2 class="font-amaticRegular text-4xl font-bold mb-0"> <span class = "text-sm antialiased text-gray-600">discounts</span></h2>
        </div>
    </div>
    
    <div class="flex flex-row justify-between items-center m-5 my-5">
    <div class = "flex">
    <button :class="[ 
        'flex justify-center items-center w-32 h-10 m-2 font-raleway font-semibold rounded-lg shadow-lg transition-transform duration-300 transform hover:scale-105', 
        { 'bg-white text-teal-800': showTable === 'packages', 'bg-gray-800 text-white': showTable !== 'packages' } 
    ]" @click="showTable = 'vendors'">
        Package Deals
    </button>
    
    <button :class="[ 
        'flex justify-center items-center w-28 h-10 m-2 font-raleway font-semibold rounded-lg shadow-lg transition-transform duration-300 transform hover:scale-105', 
        { 'bg-white text-teal-800': showTable === 'staffs', 'bg-gray-800 text-white': showTable !== 'staffs' } 
    ]" @click="showTable = 'staffs'">
        Discounts
    </button>
    </div>
    <button class = "mr-2 w-36 h-10 bg-[#9B111E] font-semibold text-gray-100 font-quicksand rounded-full shadow-lg 
    transition-transform duration-300 transform hover:scale-105" @click="addPackagesBtn">
    + Add Services
    </button>
    </div>
    
    <div v-if="showTable === 'packages'" class="relative shadow-md sm:rounded-xl w-full max-w-[1170px] h-auto ml-5 mt-2 font-amaticBold mb-10">
    <div class="overflow-x-auto">
        <table class="w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400 mb-4">
            <thead class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
                <tr>
                    <th scope="col" class="px-4 py-3">#</th>
                    <th scope="col" class="px-4 py-3">Package Name</th>
                    <th scope="col" class="px-4 py-3">Package Type</th>
                    <th scope="col" class="px-4 py-3">Venue</th>
                    <th scope="col" class="px-4 py-3">Price</th>
                    <th scope="col" class="px-4 py-3">Capacity</th>
                    <th scope="col" class="px-4 py-3">Action</th>
                </tr>
            </thead>
            <tbody>
                <tr
                    v-for="(packageItem, index) in paginatedPackages"
                    :key="packageItem.no"
                    class="border-b dark:border-gray-700 odd:bg-white odd:dark:bg-gray-900 even:bg-gray-50 even:dark:bg-gray-800">
                    <th scope="row" class="px-4 py-3 font-medium text-gray-900 whitespace-nowrap dark:text-white">{{ packageItem.dummyIndex}}</th>
                    <td class="px-4 py-3">{{ packageItem.package_name }}</td>
                    <td class="px-4 py-3">{{ packageItem.package_type }}</td>
                    <td class="px-4 py-3">{{ packageItem.venue }}</td>
                    <td class="px-4 py-3">{{ packageItem.price}}</td>
                    <td class="px-4 py-3">{{ packageItem.capacity }}</td>
                    <td class="px-4 py-3">
                        <button
                            class="h-8 w-20 bg-[#9B111E] font-amaticBold text-sm rounded-md text-white hover:bg-[#B73A45]"
                            @click="editPackageBtn(index)">
                            View
                        </button>
                    </td>
                </tr>
            </tbody>
        </table>
    
        <!-- Pagination Controls -->
        <div class="flex justify-center space-x-2 mt-4 mb-6">
            <button 
                @click="prevPackagesPage" 
                :disabled="currentPackagesPage === 1" 
                class="px-3 py-1 bg-[#9B111E] text-white rounded-md hover:bg-[#B73A45] disabled:opacity-50 text-md">
                Previous
            </button>
            <button 
                v-for="page in totalPackagesPages" 
                :key="page" 
                @click="changePackagesPage(page)" 
                :class="{'bg-[#9B111E]': currentPackagesPage === page, 'bg-gray-300': currentPackagesPage !== page}" 
                class="px-3 py-1 text-white rounded-md hover:bg-[#B73A45] text-xs">
                {{ page }}
            </button>
            <button 
                @click="nextPackagesPage" 
                :disabled="currentPackagesPage === totalPackagesPages" 
                class="px-3 py-1 bg-[#9B111E] text-white rounded-md hover:bg-[#B73A45] disabled:opacity-50 text-xs">
                Next
            </button>
        </div>
    </div>
</div>

    
    <!-- Add Packages Form -->
    <form v-if="addPackagesForm" @submit.prevent="addPackages" class="flex justify-center items-center fixed inset-0 bg-gray-800 bg-opacity-50 overflow-y-auto">
    <div class="bg-white w-[500px] p-5 rounded-lg shadow-lg overflow-y-auto">
        <div class="flex justify-between items-center m-3">
        <h1 class="font-semibold text-xl font-raleway text-gray-800">Add Package</h1>
        <button class="mt-2 bg-red-500 text-white px-3 py-1 rounded transform-transition duration-300 transform hover:scale-105" @click="closePackagesForm">
            Close
        </button>
        </div>
        <div class="border border-gray-500 mt-5 items-center"></div>
        <div class="m-5">
        <span>{{ errorMessage }}</span>

    
        
        <div class="mt-5">
            <input type="text" class="mt-2 ml-2 p-2 w-full h-10 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:border-blue-700" v-model="package_name" placeholder="Package Name" required>
        </div>

        <div class="mt-5">
        <select class="flex mt-4 ml-2 p-2 w-full h-10 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:border-blue-700" v-model="package_type">
          <option value="" class="text-gray-700" disabled selected>Select a Type of Package</option>
          <option value="Wedding">Wedding</option>
          <option value="Birthday">Birthday</option>
          <option value="Debut">Debut</option>
        </select>
      </div>

        <div class="mt-5">
            <input type="text" class="mt-2 ml-2 p-2 w-full h-10 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:border-blue-700" v-model="venue" placeholder="Venue" required>
        </div>
    

        <div class="mt-5 flex flex-row">
            <div class="flex items-center space-x-2">
            <input type="number" class="mt-2 ml-2 p-2 w-full h-10 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:border-blue-700" v-model="capacity" placeholder="Capacity" required>
            </div>
            <div class="flex items-center space-x-2">
            <input type="number" class="mt-2 ml-2 p-2 w-full h-10 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:border-blue-700" v-model="package_price" placeholder="Price" required>
            </div>
        </div>
       
    

        <div class="mt-5">
            <textarea
                class="mt-2 ml-2 p-2 w-full h-24 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:border-blue-700 align-top resize-none"
                v-model="description"
                placeholder="Description"
                required
            ></textarea>
        </div>
    
  
       
    
        <!-- Confirm Button -->
        <div class="flex justify-center items-center mt-10">
            <button type="submit" class="w-20 h-10 bg-blue-500 text-gray-100 font-semibold rounded-lg shadow-md transform-transition duration-300 transform hover:scale-105">
            Confirm
            </button>
        </div>
        </div>
    </div>
  </form>

  <!--Edit Packages Form-->
  <form v-if="editPackagesForm" @submit.prevent="confirmEditPackage" class="flex justify-center items-center fixed inset-0 bg-gray-800 bg-opacity-50 overflow-y-auto">
    <div class="bg-white w-[500px] p-5 rounded-lg shadow-lg overflow-y-auto">
      <div class="flex justify-between items-center m-3">
        <h1 class="font-semibold text-xl font-raleway text-gray-800">Edit Package</h1>
        <button class="mt-2 bg-red-500 text-white px-3 py-1 rounded transform-transition duration-300 transform hover:scale-105" @click="closeEditPackagesBtn">
          Close
        </button>
      </div>
      <div class="border border-gray-500 mt-5 items-center"></div>
      <div class="m-5">
        <span>{{ errorMessage }}</span>

        <div class="mt-5">
          <input type="text" class="mt-2 ml-2 p-2 w-full h-10 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:border-blue-700" v-model="selectedPackage.package_name" placeholder="Package Name" required>
        </div>

        <div class="mt-5">
          <select class="flex mt-4 ml-2 p-2 w-full h-10 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:border-blue-700" v-model="selectedPackage.package_type">
            <option value="" class="text-gray-700" disabled selected>Select a Type of Package</option>
            <option value="Wedding">Wedding</option>
            <option value="Birthday">Birthday</option>
            <option value="Debut">Debut</option>
          </select>
        </div>

        <div class="mt-5">
          <input type="text" class="mt-2 ml-2 p-2 w-full h-10 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:border-blue-700" v-model="selectedPackage.venue" placeholder="Venue" required>
        </div>

        <div class="mt-5 flex flex-row">
          <div class="flex items-center space-x-2">
            <input type="number" class="mt-2 ml-2 p-2 w-full h-10 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:border-blue-700" v-model="selectedPackage.capacity" placeholder="Capacity" required>
          </div>
          <div class="flex items-center space-x-2">
            <input type="number" class="mt-2 ml-2 p-2 w-full h-10 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:border-blue-700" v-model="selectedPackage.price" placeholder="Price" required>
          </div>
        </div>

        <div class="mt-5">
          <textarea
            class="mt-2 ml-2 p-2 w-full h-24 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:border-blue-700 align-top resize-none"
            v-model="selectedPackage.description"
            placeholder="Description"
            required
          ></textarea>
        </div>

        <!-- Confirm Button -->
        <div class="flex justify-center items-center mt-10 space-x-3">
          <button @click.prevent="deletePackage(selectedPackage.packageId)" class = "w-20 h-10 bg-yellow-500 text-gray-100 font-semibold rounded-lg shadow-md  transform-transition duration-300 transform hover:scale-105">
            Delete
            </button>
          <button type="submit" class="w-20 h-10 bg-blue-500 text-gray-100 font-semibold rounded-lg shadow-md transform-transition duration-300 transform hover:scale-105">
            Confirm
          </button>
        </div>
      </div>
    </div>
  </form>
    

    
    
    </div>
    </template>

    <script>
import axios from 'axios';

axios.defaults.withCredentials = true;

export default {
  name: 'AddServices',
  data() {
    return {
      showTable: 'packages',
      currentPackagesPage: 1,
      rowsPerPackagesPage: 5,
      errorMessage: '',


      addPackagesForm: false,
      addPackagesDetails: false,
      addStaffDetails: false,
      selectedOption: '',

      editPackagesForm: false,
      selectedPackages: null, 
      editPackagesForm: false,

      editStaffForm: false,
      selectedStaff: null, 
      editStaffForm: false,

      //add package inputs
      package_name: '',
      package_type: '',
      venue: '',
      capacity: '',
      package_price: '',
      description: '',
      

      selectedPackage: null,
   


      staffs: [],
      packages: [],
  
      


      
    };
  },
  computed: {
    totalPackagesPages() {
        return Math.ceil(this.packages.length / this.rowsPerPackagesPage);
    },
    paginatedPackages() {
        if (!this.packages || this.packages.length === 0) {
            return []; // Ensure it's an empty array if packages is not available
        }
        const start = (this.currentPackagesPage - 1) * this.rowsPerPackagesPage;
        const end = start + this.rowsPerPackagesPage;
        return this.packages.slice(start, end);
    },
    totalPackages() {
        return this.packages.length;
    },
    startIndex() {
        return (this.currentPackagesPage - 1) * this.rowsPerPackagesPage + 1;
    },
},

  methods: {
    async addPackages() {
            try {
                // Validate required fields
                const fields = [
                    this.package_name, this.package_type, this.venue, this.capacity, this.package_price, this.description
                ];

                if (fields.some(field => !field)) {
                    this.errorMessage = 'All fields are required!';
                    return;
                }

                // Prepare the data payload
                const requestData = {
                    package_name: this.package_name,
                    package_type: this.package_type,
                    venue: this.venue,
                    price: this.package_price, // Assuming 'package_price' is the price field
                    capacity: this.capacity,
                    description: this.description,
                };

                // Send the request to the backend
                const response = await axios.post('http://127.0.0.1:5000/create-package', requestData, {
                    headers: {
                        'Content-Type': 'application/json',
                        'Authorization': `Bearer ${localStorage.getItem('access_token')}`
                    }
                });

                // Check for successful response
                if (response.status === 201) {
                    alert('Package created successfully!');
                    this.resetPackageForm(); // Reset the form after success
                }
            } catch (error) {
                // Handle error feedback
                this.errorMessage = error.response?.data?.message || 'An error occurred. Please try again.';
            }
        },



      resetPackageForm() {
        this.package_name = '';
        this.package_type = '';
        this.venue = '';
        this.capacity =  '';
        this.package_price =  '';
        this.description =  '';
      },

      async fetchPackages() {
            try {
                const token = localStorage.getItem('access_token');
                if (!token) {
                    alert('You are not logged in. Please log in to view event packages.');
                    return;
                }

                const response = await axios.get('http://127.0.0.1:5000/created-packages', {
                    headers: {
                        'Content-Type': 'application/json',
                        'Authorization': `Bearer ${token}`,
                    },
                    withCredentials: true,
                });

               // Populate packages array with data from API
                this.packages = response.data.map((pkg, index) => ({
                packageId: pkg.package_id,   // API returns package_id, so map to packageId
                package_name: pkg.package_name,
                package_type: pkg.package_type,
                venue: pkg.venue,
                price: pkg.price,
                capacity: pkg.capacity,
                description: pkg.description,
                dummyIndex: index + 1  // Dummy index, independent of package_id
            }));

            } catch (error) {
                console.error('Error fetching event packages:', error.response?.data || error.message);
            }
        },



        async confirmEditPackage() {
              try {
                  const token = localStorage.getItem('access_token');

                  if (!this.selectedPackage || !this.selectedPackage.packageId) {
                      alert("Package ID is missing or invalid.");
                      return;
                  }

                  const response = await axios.put(
                      `http://127.0.0.1:5000/created-package/${this.selectedPackage.packageId}`,
                      {
                          package_name: this.selectedPackage.package_name,
                          package_type: this.selectedPackage.package_type,
                          venue: this.selectedPackage.venue,
                          price: this.selectedPackage.price,
                          capacity: this.selectedPackage.capacity,
                          description: this.selectedPackage.description,
                      },
                      {
                          headers: {
                              Authorization: `Bearer ${token}`,
                          },
                      }
                  );

                  if (response.status === 200) {
                      alert('Package updated successfully!');

                      // Update the package in the list
                      const index = this.packages.findIndex(
                          (packageItem) => packageItem.packageId === this.selectedPackage.packageId
                      );
                      if (index !== -1) {
                          this.packages[index] = { ...this.selectedPackage };
                      }

                      this.closeEditPackagesBtn();
                  } else {
                      alert('Failed to update package.');
                  }
              } catch (error) {
                  console.error('Error updating package:', error);
                  if (error.response) {
                      alert(`Error updating package: ${error.response.data.message}`);
                  } else {
                      alert('Error updating package. Please try again.');
                  }
              }
          },


          async deletePackage(packageId) {
              try {
                  if (!confirm('Are you sure you want to delete this package? This action cannot be undone.')) {
                      return;
                  }

                  const token = localStorage.getItem('access_token');
                  if (!token) {
                      alert('You are not logged in. Please log in to delete packages.');
                      return;
                  }

                  const response = await axios.delete(`http://127.0.0.1:5000/created-package/${packageId}`, {
                      headers: {
                          Authorization: `Bearer ${token}`,
                      },
                  });

                  if (response.status === 200) {
                      alert('Package deleted successfully!');
                      // Remove the deleted package from the packages array
                      this.packages = this.packages.filter(packageItem => packageItem.packageId !== packageId);
                  } else {
                      alert('Failed to delete package.');
                  }
              } catch (error) {
                  console.error('Error deleting package:', error);
                  if (error.response) {
                      alert(`Error deleting package: ${error.response.data.message}`);
                  } else {
                      alert('Error deleting package. Please try again.');
                  }
              }
          },

      





    changePackagesPage(page) {
        this.currentPackagesPage = page;
    },
    prevPackagesPage() {
        if (this.currentPackagesPage > 1) {
            this.currentPackagesPage--;
        }
    },
    nextPackagesPage() {
        if (this.currentPackagesPage < this.totalPackagesPages) {
            this.currentPackagesPage++;
        }
    },

    prevStaffsPage() {
      if (this.currentStaffsPage > 1) {
        this.currentStaffsPage--;
      }
    },
    nextStaffsPage() {
      if (this.currentStaffsPage < this.totalStaffsPages) {
        this.currentStaffsPage++;
      }
    },
    changeStaffsPage(page) {
      this.currentStaffsPage = page;
    },

    addPackagesBtn() {
      this.addPackagesForm = true;
    },
    closePackagesForm() {
      this.addPackagesForm = false;
    },


    editVendorBtn(){
      this.editVendorForm = true;
    },

    closeEditVendorBtn() {
      this.editVendorForm = false;
    },

    editVendorBtn(index) {
        this.selectedVendor = this.paginatedPackages[index]; 
        this.editVendorForm = true; // Show the edit form
    },
    closeEditUserBtn() {
        this.editUserForm = false; 
        this.selectedVendor = null; 
    },

    editStaffBtn(){
      this.editStaffForm = true;
    },

    closeStaffVendorBtn() {
      this.editStaffForm = false;
    },

    editPackageBtn(index) {
          console.log("Selected Package from paginatedPackages: ", JSON.parse(JSON.stringify(this.paginatedPackages[index])));
          this.selectedPackage = this.paginatedPackages[index]; 
          this.editPackagesForm = true;
      },
    closeEditPackagesBtn() {
        this.editPackagesForm = false;
        this.selectedPackage = null; 
    },
    
  },
  mounted() {
    if (this.showTable === 'packages') {
        this.fetchPackages(); // Fetch staff data on component mount
    } else if (this.showTable === 'vendors') {
        this.fetchVendors(); // Fetch vendor data on component mount
    }
},
watch: {
    showTable(newTable) {
        if (newTable === 'packages') {
            this.fetchPackages();
        } else if (newTable === 'vendors') {
            this.fetchVendors();
        }
    },
},
};
    </script>

    <style scoped>
    </style>