<template>
    <div class="bg-gray-200 w-full h-full overflow-y-auto">
        <div class="w-full h-[65px] bg-gray-100 mt-2 flex items-center justify-between px-5 shadow-lg">
        <h1 class="font-amaticBold font-extraLight text-3xl">
            Add Outfit Packages
        </h1>
        </div>
    
        <div class="flex flex-row items-center m-5 space-x-5">
        <div class="flex justify-start w-52 h-20 bg-white rounded-lg shadow-lg px-2 items-center border-l-2 border-green-400 space-x-5">
            <img class="w-auto h-12" src="/img/wardrobes.png" alt="Vendor Image">
            <h2 class="font-amaticRegular text-4xl font-bold mb-0"> {{ totalOutfitPackages }} <span class = "text-sm antialiased text-gray-600">packages</span></h2>
        </div>
    </div>
    
                <div class="flex flex-row justify-between items-center m-5 my-5">
                <div class = "flex">
                <button :class="[ 
                    'flex justify-center items-center w-28 h-10 m-2 font-raleway font-semibold rounded-lg shadow-lg transition-transform duration-300 transform hover:scale-105', 
                    { 'bg-white text-teal-800': showTable === 'GownPackages', 'bg-gray-800 text-white': showTable !== 'GownPackages' } 
                ]" @click="showTable = 'GownPackages'">
                    Venues
                </button>
                </div>
                <button class = "mr-2 w-44 h-10 bg-blue-600 font-semibold text-gray-100 font-quicksand rounded-full shadow-lg 
                transition-transform duration-300 transform hover:scale-105" @click="addOutfitsPackageBtn">
                + Add Outfit Package
                </button>
                </div>
    
            <!-- Gown Packages Table -->
                <div v-if="showTable === 'GownPackages'" class="relative shadow-md sm:rounded-xl w-[1170px] h-[200] ml-5 mt-2 font-amaticBold mb-10">
                    <div class="overflow-x-auto">
                        <table class="w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400 mb-4 max-h-30">
                            <thead class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
                                <tr>
                                    <th scope="col" class="px-2 py-3">#</th>
                                    <th scope="col" class="px-2 py-3">Package Name</th>
                                    <th scope="col" class="px-2 py-3">Description</th>
                                    <th scope="col" class="px-2 py-3">Price</th>
                                    <th scope="col" class="px-2 py-3">Action</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr
                                    v-for="(gownPackage, index) in paginatedGownPackages"
                                    :key="gownPackage.gown_package_id"
                                    class="border-b dark:border-gray-700 odd:bg-white odd:dark:bg-gray-900 even:bg-gray-50 even:dark:bg-gray-800">
                                    <th scope="row" class="px-2 py-3 font-medium text-gray-900 whitespace-nowrap dark:text-white">{{ gownPackage.dummyIndex }}</th>
                                    <td class="px-1 py-3 hidden sm:table-cell">{{ gownPackage.gown_package_name }}</td>
                                    <td class="px-1 py-3 hidden sm:table-cell">{{ gownPackage.description }}</td>
                                    <td class="px-1 py-3 hidden sm:table-cell">{{ gownPackage.gown_package_price }}</td>
                                    <td class="px-1 py-3 hidden sm:table-cell">
                                        <button
                                            class="h-8 w-12 bg-blue-900 font-amaticBold font-medium text-sm rounded-md text-white hover:bg-blue-600"
                                            @click="editGownPackageBtn(index)">
                                            Edit
                                        </button>
                                    </td>
                                </tr>
                            </tbody>
                        </table>

                        <!-- Pagination Controls -->
                        <div class="flex justify-center space-x-2 mt-4 mb-6">
                            <button @click="prevGownPackagePage" :disabled="currentGownPackagePage === 1"
                                class="px-3 py-1 bg-blue-900 text-white rounded-md hover:bg-blue-600 disabled:opacity-50 text-md">Previous</button>
                            <button v-for="page in totalGownPackagePages" :key="page" @click="changeGownPackagePage(page)"
                                :class="{'bg-blue-900': currentGownPackagePage === page, 'bg-gray-300': currentGownPackagePage !== page}"
                                class="px-3 py-1 text-white rounded-md hover:bg-blue-600 text-xs">
                                {{ page }}
                            </button>
                            <button @click="nextGownPackagePage" :disabled="currentGownPackagePage === totalGownPackagePages"
                                class="px-3 py-1 bg-blue-900 text-white rounded-md hover:bg-blue-600 disabled:opacity-50 text-xs">Next</button>
                        </div>
                    </div>
                </div>

    
           <!-- Add Gown Package Form -->
      
 <!-- Add Gown Package Form -->
 <form @submit.prevent="addGownPackage" v-if="addOutfitsPackageForm" class="flex justify-center items-center fixed inset-0 bg-gray-800 bg-opacity-50 overflow-y-auto">
      <div class="bg-white w-[500px] p-5 rounded-lg shadow-lg overflow-y-auto">
        <div class="flex justify-between items-center m-3">
          <h1 class="font-semibold text-xl font-raleway text-gray-800">Add Gown Package</h1>
          <button @click="closeAddGownPackageForm" class="mt-2 bg-red-500 text-white px-3 py-1 rounded transform transition duration-300 transform hover:scale-105">
            Close
          </button>
        </div>

        <div class="border border-gray-500 mt-5 items-center"></div>
        <div class="m-5">
          <span>{{ errorMessage }}</span>

          <!-- Gown Package Name -->
          <div class="mt-5">
            <input type="text" class="mt-2 ml-2 p-2 w-full h-10 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:border-blue-700" v-model="newGownPackage.gown_package_name" placeholder="Gown Package Name" required>
          </div>

          <!-- Description -->
          <div class="mt-5">
            <input type="text" class="mt-2 ml-2 p-2 w-full h-10 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:border-blue-700" v-model="newGownPackage.description" placeholder="Description">
          </div>

         <!-- Gowns -->
          <h2 class="font-semibold text-lg font-raleway text-gray-800 mt-8 mb-4">Gowns</h2>
          <div class="mb-4 p-4 border border-gray-300 rounded-lg">
            <label class="block text-sm font-medium text-gray-700 mb-2">Select Gowns</label>
            <select @change="addGownOutfits" multiple class="mt-2 p-2 w-full h-40 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:ring-2 focus:ring-blue-500" size="5">
              <option v-for="outfit in gowns" :key="outfit.outfit_id" :value="outfit.outfit_id">
                {{ outfit.outfit_name }} - {{ outfit.rent_price }} php
              </option>
            </select>
          </div>

          <!-- Tuxedos -->
          <h2 class="font-semibold text-lg font-raleway text-gray-800 mt-8 mb-4">Tuxedos</h2>
          <div class="mb-4 p-4 border border-gray-300 rounded-lg">
            <label class="block text-sm font-medium text-gray-700 mb-2">Select Tuxedos</label>
            <select @change="addTuxedoOutfits" multiple class="mt-2 p-2 w-full h-40 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:ring-2 focus:ring-blue-500" size="5">
              <option v-for="outfit in tuxedos" :key="outfit.outfit_id" :value="outfit.outfit_id">
                {{ outfit.outfit_name }} - {{ outfit.rent_price }} php
              </option>
            </select>
          </div>

          <!-- Confirm Button -->
          <div class="flex justify-center items-center mt-10 space-x-3">
            <button type="submit" class="w-32 h-10 bg-blue-500 text-gray-100 font-semibold rounded-lg shadow-md transition duration-300 transform hover:scale-105">
              Add Gown Package
            </button>
          </div>
        </div>
      </div>
    </form>
    
    
            <!-- Edit Venue Form -->
            <form v-if="editVenueForm" @submit.prevent="updateVenue" class="flex justify-center items-center fixed inset-0 bg-gray-800 bg-opacity-50 overflow-y-auto">
            <div class="bg-white w-[500px] p-5 rounded-lg shadow-lg overflow-y-auto">
                <div class="flex justify-between items-center m-3">
                <h1 class="font-semibold text-xl font-raleway text-gray-800">Edit Venue</h1>
                <button class="mt-2 bg-red-500 text-white px-3 py-1 rounded transform-transition duration-300 transform hover:scale-105" @click="closeEditVenueForm">
                    Close
                </button>
                </div>
    
                <div class="border border-gray-500 mt-5 items-center"></div>
                <div class="m-5">
                <span>{{ errorMessage }}</span>
    
                <!-- Venue Name -->
                <div class="mt-5">
                    <input type="text" class="mt-2 ml-2 p-2 w-full h-10 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:border-blue-700" v-model="selectedVenue.venue_name" placeholder="Venue Name" required>
                </div>
    
                <!-- Location -->
                <div class="mt-5">
                    <input type="text" class="mt-2 ml-2 p-2 w-full h-10 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:border-blue-700" v-model="selectedVenue.location" placeholder="Location" required>
                </div>
    
                <!-- Price -->
                <div class="mt-5">
                    <input type="number" class="mt-2 ml-2 p-2 w-full h-10 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:border-blue-700" v-model="selectedVenue.venue_price" placeholder="Price" required>
                </div>
    
                <!-- Confirm Button -->
                <div class="flex justify-center items-center mt-10 space-x-3">
                    <button @click.prevent="deleteVenue(selectedVenue.venue_id)" class="w-20 h-10 bg-yellow-500 text-gray-100 font-semibold rounded-lg shadow-md transform-transition duration-300 transform hover:scale-105">
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
        name: 'AddOutfitPackage',
        data() {
    return {
      showTable: 'GownPackages',
      currentGownPackagePage: 1,
      rowsPerGownPackagePage: 5,
      newGownPackage: {
        gown_package_name: '',
        description: '',
        outfits: []
      },
      gownPackages: [],
      addOutfitsPackageForm: false,
      gowns: [],
      tuxedos: [],
      errorMessage: ''
    };
  },

     computed: {
        totalOutfitPackages() {
            return this.gownPackages.length;
        },
        paginatedGownPackages() {
            const start = (this.currentGownPackagePage - 1) * this.rowsPerGownPackagePage;
            const end = start + this.rowsPerGownPackagePage;
            return this.gownPackages.slice(start, end);
        },
        totalGownPackagePages() {
            return Math.ceil(this.gownPackages.length / this.rowsPerGownPackagePage);
        },
    },
    methods: {
        async fetchGownPackages() {
        try {
            const token = localStorage.getItem('access_token');
            if (!token) {
                alert('You are not logged in. Please log in to view gown packages.');
                return;
            }

            const response = await axios.get('http://127.0.0.1:5000/gown-packages', {
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${token}`,
                },
                withCredentials: true,
            });

            // Populate gownPackages array with data from API
            this.gownPackages = response.data.map((item, index) => ({
                gown_package_id: item.gown_package_id,
                gown_package_name: item.gown_package_name,
                gown_package_price: item.gown_package_price,
                description: item.description,
                dummyIndex: index + 1,
            }));

        } catch (error) {
            console.error('Error fetching gown packages:', error.response?.data || error.message);
        }
    },


    async fetchOutfits() {
            try {
            const token = localStorage.getItem('access_token');
            if (!token) {
                alert('You are not logged in. Please log in to view outfits.');
                return;
            }

            const response = await axios.get('http://127.0.0.1:5000/outfits', {
                headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${token}`,
                },
                withCredentials: true,
            });

            // Populate outfits array with data from API
            this.outfits = response.data.map((item, index) => ({
                outfit_id: item.outfit_id,
                outfit_name: item.outfit_name,
                outfit_type: item.outfit_type,
                outfit_color: item.outfit_color,
                outfit_desc: item.outfit_desc,
                rent_price: item.rent_price,
                status: item.status,
                outfit_img: item.outfit_img,
                size: item.size,
                weight: item.weight,
                dummyIndex: index + 1,
            }));

            // Separate outfits by type
            this.gowns = this.outfits.filter(outfit => outfit.outfit_type === 'Gown');
            this.tuxedos = this.outfits.filter(outfit => outfit.outfit_type === 'Tuxedo');

            } catch (error) {
            console.error('Error fetching outfits:', error.response?.data || error.message);
            }
        },
        addGownOutfits(event) {
            const selectedOptions = Array.from(event.target.selectedOptions).map(option => option.value);
            this.newGownPackage.outfits = [...new Set([...this.newGownPackage.outfits, ...selectedOptions])];
        },
        addTuxedoOutfits(event) {
            const selectedOptions = Array.from(event.target.selectedOptions).map(option => option.value);
            this.newGownPackage.outfits = [...new Set([...this.newGownPackage.outfits, ...selectedOptions])];
        },

    
            async addGownPackage() {
                try {
                const token = localStorage.getItem('access_token');
                if (!token) {
                    alert('You are not logged in. Please log in to add a gown package.');
                    return;
                }

                // Log the data to be sent to the server
                console.log('Sending data:', this.newGownPackage);

                const response = await axios.post('http://127.0.0.1:5000/add-gown-package', this.newGownPackage, {
                    headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${token}`,
                    },
                    withCredentials: true,
                });

                alert('Gown package added successfully');
                // Optionally, reset the form or update the UI as needed
                this.newGownPackage = {
                    gown_package_name: '',
                    description: '',
                    outfits: []
                };
                this.addOutfitsPackageForm = false;  // Close the form after successful addition
                } catch (error) {
                console.error('Error adding gown package:', error.response?.data || error.message);
                this.errorMessage = 'An error occurred. Please try again.';
                }
            },

    
                async deleteVenue(venue_id) {
                    try {
                        if (!confirm('Are you sure you want to delete this venue? This action cannot be undone.')) {
                        return;
                        }
    
                        const token = localStorage.getItem('access_token');
                        if (!token) {
                        alert('You are not logged in. Please log in to delete venues.');
                        return;
                        }
    
                        const response = await axios.delete(`http://127.0.0.1:5000/delete-venue/${venue_id}`, {
                        headers: {
                            'Authorization': `Bearer ${token}`,
                        },
                        });
    
                        if (response.status === 200) {
                        alert('Venue deleted successfully!');
                        // Remove the deleted venue from the venues array
                        this.venues = this.venues.filter(venue => venue.venue_id !== venue_id);
                        this.closeEditVenueForm(); // Optionally close the form
                        } else {
                        alert('Failed to delete venue.');
                        }
                    } catch (error) {
                        console.error('Error deleting venue:', error);
                        if (error.response) {
                        alert(`Error deleting venue: ${error.response.data.message}`);
                        } else {
                        alert('Error deleting venue. Please try again.');
                        }
                    }
                },
    
            
        // Pagination methods
        prevGownPackagePage() {
            if (this.currentGownPackagePage > 1) {
                this.currentGownPackagePage--;
            }
        },
        nextGownPackagePage() {
            if (this.currentGownPackagePage < this.totalGownPackagePages) {
                this.currentGownPackagePage++;
            }
        },
        changeGownPackagePage(page) {
            this.currentGownPackagePage = page;
        },
        editVenueBtn(index) {
            // Handle edit action for venue
            console.log(`Edit venue at index: ${index}`);
        },
    
        addOutfitsPackageBtn()
        {
            this.addOutfitsPackageForm = true;
        },
        closeAddVenueForm()
        {
            this.addVenueForm = false;
            this.venue_name = '';
            this.location = '';
            this.venue_price = '';
            this.errorMessage = '';
          
        },
    
        editVenueBtn(index) {
                this.editVenueForm = true;
                const selectedVenue = this.venues[index];
                if (selectedVenue) {
                    this.selectedVenue = { ...selectedVenue }; // Ensure selectedVenue is deeply copied
                } else {
                    console.error('Invalid venue selected:', index);
                }
            },
    
            closeEditVenueForm() {
                this.editVenueForm = false;
                this.selectedVenue = {
                    venue_name: '',
                    location: '',
                    venue_price: '',
                }; // Reset the form fields
                this.errorMessage = '';
            },
    
    
    },
    
        mounted() {
            this.fetchGownPackages();
            this.fetchOutfits();
        },
    
    
    
    }
    
    
    </script>
    
    <style scoped>

    </style>