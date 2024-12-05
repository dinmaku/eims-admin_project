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
    </div>
    
    <div class="flex flex-row justify-between items-center m-5 my-5">
    <div class = "flex">
    <button :class="[ 
        'flex justify-center items-center w-32 h-10 m-2 font-raleway font-semibold rounded-lg shadow-lg transition-transform duration-300 transform hover:scale-105', 
        { 'bg-white text-teal-800': showTable === 'packages', 'bg-gray-800 text-white': showTable !== 'packages' } 
    ]" @click="showTable = 'packages'">
        Package Deals
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
                    :key="packageItem.packageId"
                    class="border-b dark:border-gray-700 odd:bg-white odd:dark:bg-gray-900 even:bg-gray-50 even:dark:bg-gray-800">
                    <th scope="row" class="px-4 py-3 font-medium text-gray-900 whitespace-nowrap dark:text-white">{{ packageItem.dummyIndex }}</th>
                    <td class="px-4 py-3">{{ packageItem.package_name }}</td>
                    <td class="px-4 py-3">{{ packageItem.package_type }}</td>
                    <td class="px-4 py-3">{{ packageItem.venue_name }}</td>
                    <td class="px-4 py-3">{{ formatPrice(packageItem.total_price) }}</td>
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
    <div class="bg-white w-[800px] p-5 rounded-lg shadow-lg overflow-y-auto max-h-[90vh]">
      <div class="flex justify-between items-center m-3">
        <h1 class="font-semibold text-xl font-raleway text-gray-800">Add Package</h1>
        <button class="mt-2 bg-red-500 text-white px-3 py-1 rounded transform-transition duration-300 transform hover:scale-105" @click="closePackagesForm">
          Close
        </button>
      </div>
      <div class="border border-gray-500 mt-5 items-center"></div>
      <div class="m-5">
        <span class="text-red-500">{{ errorMessage }}</span>

        <h1 class="font-semibold text-xl font-raleway text-gray-800 mb-4">Package Details</h1>   
        
        <div class="grid grid-cols-2 gap-4">
          <div>
            <input type="text" class="mt-2 p-2 w-full h-10 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:ring-2 focus:ring-blue-500" v-model="packageData.package_name" placeholder="Package Name" required>
          </div>
          <div>
            <input type="text" class="mt-2 p-2 w-full h-10 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:ring-2 focus:ring-blue-500" v-model="packageData.package_type" placeholder="Package Type (Ex. Wedding)" required>
          </div>
        </div>

        <div class="mt-5">
        <select 
            v-model="packageData.venue_id" 
            class="mt-2 p-2 w-full h-10 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:ring-2 focus:ring-blue-500" 
            required>
            <option value="" disabled selected>Select a venue</option>
            <option v-for="venue in venues" :key="venue.selectVenueId" :value="venue.selectVenueId">
            {{ venue.selectVenue_name }} - {{ venue.selectVenue_price }} php
            </option>
            <option value="">N/A</option>
        </select>
        </div>


        <div class="grid grid-cols-2 gap-4 mt-5">
          <div>
            <input type="number" class="mt-2 p-2 w-full h-10 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:ring-2 focus:ring-blue-500" v-model="packageData.capacity" placeholder="Set Capacity" required>
          </div>
          <div>
            <input type="number" class="mt-2 p-2 w-full h-10 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:ring-2 focus:ring-blue-500" v-model="packageData.additional_capacity_charges" placeholder="Additional Capacity Charges" required>
          </div>
        </div>

        <div class="mt-5">
          <label for="charge_unit" class="block text-sm font-medium text-blue-700">Set unit for additional charges</label>
          <input type="number" id="charge_unit" class="mt-2 p-2 w-full h-10 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:ring-2 focus:ring-blue-500" v-model="packageData.charge_unit" placeholder="Set person unit" required>
        </div>

        <div class="mt-5">
          <textarea
            class="mt-2 p-2 w-full h-24 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:ring-2 focus:ring-blue-500 align-top resize-none"
            v-model="packageData.description"
            placeholder="Description"
            required
          ></textarea>
        </div>

        <h2 class="font-semibold text-lg font-raleway text-gray-800 mt-8 mb-4">Gown Package</h2>
      <div class="mb-4 p-4 border border-gray-300 rounded-lg">
        <label class="block text-sm font-medium text-gray-700 mb-2">Select Gown Package</label>
        <select v-model="packageData.gown_package_id" class="mt-2 p-2 w-full h-10 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:ring-2 focus:ring-blue-500">
          <option value="" disabled selected>Select a gown package</option>
          <option v-for="gp in gownPackages" :key="gp.gown_package_id" :value="gp.gown_package_id">
            {{ gp.gown_package_name }} - {{ gp.gown_package_price }} php
          </option>
        </select>
      </div>

        <h2 class="font-semibold text-lg font-raleway text-gray-800 mt-8 mb-4">Suppliers</h2>
        <div v-for="(supplier, index) in packageData.suppliers" :key="index" class="mb-4 p-4 border border-gray-300 rounded-lg">
            <div class="grid grid-cols-2 gap-4 mb-4">
            <div>
                <label class="block text-sm font-medium text-gray-700 mb-2">Supplier Type</label>
                <select v-model="supplier.type" @change="resetSupplierFields(supplier)" class="mt-2 p-2 w-full h-10 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:ring-2 focus:ring-blue-500" required>
                <option value="internal">Internal Supplier</option>
                <option value="external">External Supplier</option>
                </select>
            </div>
            </div>

            

            <div v-if="supplier.type === 'internal'" class="grid grid-cols-2 gap-4">
            <div>
                <label class="block text-sm font-medium text-gray-700 mb-2">Select Internal Supplier</label>
                <select v-model="supplier.supplier_id" class="mt-2 p-2 w-full h-10 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:ring-2 focus:ring-blue-500" required>
                <option value="" disabled selected>Select a supplier</option>
                <option v-for="s in availableSuppliers" :key="s.supplier_id" :value="s.supplier_id">
                  {{ s.firstname }} {{ s.lastname }} - {{ s.service }} - {{ s.price }} php
                </option>
              </select>
            </div>
            <div>
                <label class="block text-sm font-medium text-gray-700 mb-2">Remarks</label>
                <input type="text" class="mt-2 p-2 w-full h-10 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:ring-2 focus:ring-blue-500" v-model="supplier.remarks" placeholder="Remarks">
            </div>
            </div>

            <div v-if="supplier.type === 'external'" class="grid grid-cols-2 gap-4">
            <div>
                <label class="block text-sm font-medium text-gray-700 mb-2">External Supplier Name</label>
                <input type="text" class="mt-2 p-2 w-full h-10 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:ring-2 focus:ring-blue-500" v-model="supplier.external_supplier_name" placeholder="External Supplier Name" required>
            </div>
            <div>
                <label class="block text-sm font-medium text-gray-700 mb-2">External Supplier Contact</label>
                <input type="text" class="mt-2 p-2 w-full h-10 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:ring-2 focus:ring-blue-500" v-model="supplier.external_supplier_contact" placeholder="External Supplier Contact" required>
            </div>
            <div>
                <label class="block text-sm font-medium text-gray-700 mb-2">External Supplier Price</label>
                <input type="number" step="0.01" class="mt-2 p-2 w-full h-10 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:ring-2 focus:ring-blue-500" v-model="supplier.external_supplier_price" placeholder="External Supplier Price" required>
            </div>
            <div>
                <label class="block text-sm font-medium text-gray-700 mb-2">Remarks</label>
                <input type="text" class="mt-2 p-2 w-full h-10 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:ring-2 focus:ring-blue-500" v-model="supplier.remarks" placeholder="Remarks">
            </div>
            </div>

            <button @click.prevent="removeSupplier(index)" class="mt-4 bg-red-500 text-white px-3 py-1 rounded">Remove Supplier</button>
        </div>
        <button @click.prevent="addSupplier" class="mt-4 bg-green-500 text-white px-3 py-1 rounded">Add Supplier</button>


        <div class="flex justify-center items-center mt-10">
          <button type="submit" class="w-32 h-10 bg-blue-500 text-gray-100 font-semibold rounded-lg shadow-md transform-transition duration-300 transform hover:scale-105">
            Create Package
          </button>
        </div>
      </div>
    </div>
  </form>

 <!-- Edit Packages Form -->
<form v-if="editPackagesForm" @submit.prevent="confirmEditPackage" class="flex justify-center items-center fixed inset-0 bg-gray-800 bg-opacity-50 overflow-y-auto">
  <div class="bg-white w-[800px] p-5 rounded-lg shadow-lg overflow-y-auto max-h-[90vh]">
    <div class="flex justify-between items-center m-3">
      <h1 class="font-semibold text-xl font-raleway text-gray-800">Edit Package</h1>
      <button class="mt-2 bg-red-500 text-white px-3 py-1 rounded transform-transition duration-300 transform hover:scale-105" @click="closeEditPackagesBtn" aria-label="Close edit form">
        Close
      </button>
    </div>
    <div class="border border-gray-500 mt-5"></div>

    <div class="m-5">
      <span class="text-red-500">{{ errorMessage }}</span>

      <div class="mt-5 grid grid-cols-2 gap-4">
        <div>
          <label for="package-name" class="block text-sm font-medium text-gray-700">Package Name</label>
          <input id="package-name" type="text" class="mt-1 p-2 w-full h-10 rounded-lg shadow-sm border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500" v-model="selectedPackage.package_name" placeholder="Package Name" required>
        </div>
        <div>
          <label for="package-type" class="block text-sm font-medium text-gray-700">Package Type</label>
          <select id="package-type" class="mt-1 p-2 w-full h-10 rounded-lg shadow-sm border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500" v-model="selectedPackage.package_type">
            <option value="" disabled>Select a Type of Package</option>
            <option value="Wedding">Wedding</option>
            <option value="Birthday">Birthday</option>
            <option value="Debut">Debut</option>
          </select>
        </div>
      </div>

      <div class="mt-5 grid grid-cols-2 gap-4">
        <div>
          <label for="capacity" class="block text-sm font-medium text-gray-700">Capacity</label>
          <input id="capacity" type="number" class="mt-1 p-2 w-full h-10 rounded-lg shadow-sm border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500" v-model="selectedPackage.capacity" placeholder="Capacity" required>
        </div>
        <div>
          <label for="total-price" class="block text-sm font-medium text-gray-700">Total Price</label>
          <input id="total-price" type="number" class="mt-1 p-2 w-full h-10 rounded-lg shadow-sm border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500" v-model="selectedPackage.total_price" placeholder="Total Price" required>
        </div>
      </div>

      <div class="mt-5">
        <label for="description" class="block text-sm font-medium text-gray-700">Description</label>
        <textarea id="description" class="mt-1 p-2 w-full h-24 rounded-lg shadow-sm border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500 align-top resize-none" v-model="selectedPackage.description" placeholder="Description" required></textarea>
      </div>

      <div class="mt-5 grid grid-cols-2 gap-4">
        <div>
          <h2 class="font-semibold text-lg">Gown Package</h2>
          <div class="mt-2">
            <label for="gown-package-name" class="block text-sm font-medium text-gray-700">Name</label>
            <input id="gown-package-name" type="text" class="mt-1 p-2 w-full h-10 rounded-lg shadow-sm border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500" v-model="selectedPackage.gown_package_name" placeholder="Gown Package Name" readonly>
          </div>
          <div class="mt-2">
            <label for="gown-package-price" class="block text-sm font-medium text-gray-700">Price</label>
            <input id="gown-package-price" type="number" class="mt-1 p-2 w-full h-10 rounded-lg shadow-sm border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500" v-model="selectedPackage.gown_package_price" placeholder="Gown Package Price" readonly>
          </div>
        </div>

        <div>
          <h2 class="font-semibold text-lg">Venue</h2>
          <div class="mt-2">
            <label for="venue-name" class="block text-sm font-medium text-gray-700">Name</label>
            <input id="venue-name" type="text" class="mt-1 p-2 w-full h-10 rounded-lg shadow-sm border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500" v-model="selectedPackage.venue_name" placeholder="Venue Name" readonly>
          </div>
          <div class="mt-2">
            <label for="venue-location" class="block text-sm font-medium text-gray-700">Location</label>
            <input id="venue-location" type="text" class="mt-1 p-2 w-full h-10 rounded-lg shadow-sm border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500" v-model="selectedPackage.venue_location" placeholder="Venue Location" readonly>
          </div>
          <div class="mt-2">
            <label for="venue-price" class="block text-sm font-medium text-gray-700">Price</label>
            <input id="venue-price" type="number" class="mt-1 p-2 w-full h-10 rounded-lg shadow-sm border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500" v-model="selectedPackage.venue_price" placeholder="Venue Price" readonly>
          </div>
        </div>
      </div>

      <div class="mt-5">
    <h2 class="font-semibold text-lg">Suppliers</h2>
    <div v-for="(supplier, index) in selectedPackage.suppliers" :key="index" class="mt-3 p-3 border border-gray-300 rounded-lg">
      <div v-if="supplier.type === 'internal'">
        <h3 class="font-semibold">Internal Supplier</h3>
        <div class="grid grid-cols-2 gap-4">
          <div>
            <label :for="'supplier-name-' + index" class="block text-sm font-medium text-gray-700">Name</label>
            <input :id="'supplier-name-' + index" type="text" class="mt-1 p-2 w-full h-10 rounded-lg shadow-sm border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500" :value="supplier.firstname + ' ' + supplier.lastname" readonly>
          </div>
          <div>
            <label :for="'supplier-email-' + index" class="block text-sm font-medium text-gray-700">Email</label>
            <input :id="'supplier-email-' + index" type="text" class="mt-1 p-2 w-full h-10 rounded-lg shadow-sm border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500" :value="supplier.email" readonly>
          </div>
        </div>
        <div class="mt-2">
          <label :for="'supplier-service-' + index" class="block text-sm font-medium text-gray-700">Service</label>
          <input :id="'supplier-service-' + index" type="text" class="mt-1 p-2 w-full h-10 rounded-lg shadow-sm border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500" :value="supplier.service" readonly>
        </div>
        <div class="mt-2">
          <label :for="'supplier-price-' + index" class="block text-sm font-medium text-gray-700">Price</label>
          <input :id="'supplier-price-' + index" type="number" class="mt-1 p-2 w-full h-10 rounded-lg shadow-sm border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500" :value="supplier.price" readonly>
        </div>
      </div>
      <div v-else>
        <h3 class="font-semibold">External Supplier</h3>
        <div class="grid grid-cols-2 gap-4">
          <div>
            <label :for="'external-supplier-name-' + index" class="block text-sm font-medium text-gray-700">Name</label>
            <input :id="'external-supplier-name-' + index" type="text" class="mt-1 p-2 w-full h-10 rounded-lg shadow-sm border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500" :value="supplier.external_supplier_name" readonly>
          </div>
          <div>
            <label :for="'external-supplier-contact-' + index" class="block text-sm font-medium text-gray-700">Contact</label>
            <input :id="'external-supplier-contact-' + index" type="text" class="mt-1 p-2 w-full h-10 rounded-lg shadow-sm border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500" :value="supplier.external_supplier_contact" readonly>
          </div>
        </div>
        <div class="mt-2">
          <label :for="'external-supplier-price-' + index" class="block text-sm font-medium text-gray-700">Price</label>
          <input :id="'external-supplier-price-' + index" type="number" class="mt-1 p-2 w-full h-10 rounded-lg shadow-sm border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500" :value="supplier.external_supplier_price" readonly>
        </div>
        <div class="mt-2">
          <label :for="'external-supplier-service-' + index" class="block text-sm font-medium text-gray-700">Remarks</label>
          <input :id="'external-supplier-service-' + index" type="text" class="mt-1 p-2 w-full h-10 rounded-lg shadow-sm border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500" :value="supplier.remarks" readonly>
        </div>
      </div>
    </div>
  </div>

      <!-- Submit Button -->
      <div class="flex justify-center items-center mt-10 space-x-3">
      <button @click.prevent="deletePackage(selectedPackage.packageId)" class="w-20 h-10 bg-yellow-500 text-gray-100 font-semibold rounded-lg shadow-md transform-transition duration-300 transform hover:scale-105">
        Delete
      </button>
      <button type="submit" class="w-52 h-10 bg-blue-500 text-gray-100 font-semibold rounded-lg shadow-md transform-transition duration-300 transform hover:scale-105">
        Confirm Changes
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

      chargeUnit: '', // Default value

      availableSuppliers: [],
      packageData: {
        package_name: '',
        package_type: '',
        venue_id: '',
        capacity: null,
        additional_capacity_charges: null,
        charge_unit: 1,
        description: '',
        suppliers: []
      },

      selectedPackage: null,
      packageDetails: true,
   



      packages: [],
      venues: [],
  
      


      
    };
  },
 
  methods: {
   
    async addPackages() {
      try {
        const formattedPackageData = {
          ...this.packageData,
          suppliers: this.packageData.suppliers.map(supplier => {
            const commonFields = {
              type: supplier.type,
              remarks: supplier.remarks
            };
            if (supplier.type === 'internal') {
              return {
                ...commonFields,
                supplier_id: supplier.supplier_id
              };
            } else {
              return {
                ...commonFields,
                external_supplier_name: supplier.external_supplier_name,
                external_supplier_contact: supplier.external_supplier_contact,
                external_supplier_price: parseFloat(supplier.external_supplier_price)
              };
            }
          }),
          gown_package_id: this.packageData.gown_package_id,
          venue_id: parseInt(this.packageData.venue_id),
          capacity: parseInt(this.packageData.capacity),
          additional_capacity_charges: parseFloat(this.packageData.additional_capacity_charges),
          charge_unit: parseInt(this.packageData.charge_unit)
        };

        console.log('Sending package data:', formattedPackageData);

        const response = await axios.post('http://127.0.0.1:5000/create-package', formattedPackageData, {
          headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${localStorage.getItem('access_token')}`
          }
        });

        if (response.status === 201) {
          alert('Package created successfully!');
          this.resetPackageForm();
          this.fetchPackages(); // Refresh the packages list
        }
      } catch (error) {
        console.error('Error creating package:', error);
        this.errorMessage = error.response?.data?.message || 'An error occurred. Please try again.';
      }
    },

    resetPackageForm() {
      this.packageData = {
        package_name: '',
        package_type: '',
        venue_id: '',
        capacity: null,
        additional_capacity_charges: null,
        charge_unit: null,
        description: '',
        suppliers: []
      };
      this.addPackagesForm = false;
    },
    closePackagesForm() {
      this.resetPackageForm();
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

              this.packages = response.data.map((pkg, index) => ({
                  packageId: pkg.package_id,
                  package_name: pkg.package_name,
                  package_type: pkg.package_type,
                  venue_name: pkg.venue_name,
                  venue_location: pkg.venue_location,
                  venue_price: pkg.venue_price,
                  total_price: pkg.total_price,
                  capacity: pkg.capacity,
                  description: pkg.description,
                  gown_package_name: pkg.gown_package_name,
                  gown_package_price: pkg.gown_package_price,
                  suppliers: pkg.package_service_ids.map((id, i) => {
                      if (pkg.supplier_ids[i]) {
                          // Internal supplier
                          return {
                              id: pkg.supplier_ids[i],
                              type: 'internal',
                              firstname: pkg.supplier_firstnames[i],
                              lastname: pkg.supplier_lastnames[i],
                              email: pkg.supplier_emails[i],
                              contact: pkg.supplier_contacts[i],
                              service: pkg.services[i],
                              price: pkg.service_prices[i],
                              remarks: pkg.remarks[i] // Include remarks for internal suppliers
                          };
                      } else {
                          // External supplier
                          return {
                              id: id,
                              type: 'external',
                              external_supplier_name: pkg.external_supplier_names[i],
                              external_supplier_contact: pkg.external_supplier_contacts[i],
                              external_supplier_price: pkg.external_supplier_prices[i],
                              remarks: pkg.remarks[i] // Include remarks for external suppliers
                          };
                      }
                  }),
                  dummyIndex: index + 1,
              }));
          } catch (error) {
              console.error('Error fetching event packages:', error.response?.data || error.message);
          }
      },

        async fetchVenues() {
            try {
                const token = localStorage.getItem('access_token');
                if (!token) {
                    alert('You are not logged in. Please log in to view venues.');
                    return;
                }

                const response = await axios.get('http://127.0.0.1:5000/created-venues', {
                    headers: {
                        'Content-Type': 'application/json',
                        'Authorization': `Bearer ${token}`,
                    },
                    withCredentials: true,
                });

                // Populate venues array with data from API
                this.venues = response.data.map((venue, index) => ({
                    selectVenueId: venue.venue_id,
                    selectVenue_name: venue.venue_name,
                    selectVenue_location: venue.location,
                    selectVenue_price: venue.venue_price,  // Include any other fields you want to show
                    dummyIndex: index + 1,
                }));

            } catch (error) {
                console.error('Error fetching venues:', error.response?.data || error.message);
            }
        },

        async fetchSuppliersAndPackageServices() {
          try {
              const token = localStorage.getItem('access_token');
              if (!token) {
                  alert('You are not logged in. Please log in to fetch suppliers and package services.');
                  return;
              }

              // Fetch suppliers
              const suppliersResponse = await axios.get('http://127.0.0.1:5000/suppliers', {
                  headers: {
                      'Authorization': `Bearer ${token}`,
                  },
              });

              // Fetch package services
              const packageServicesResponse = await axios.get('http://127.0.0.1:5000/package-service-suppliers', {
                  headers: {
                      'Authorization': `Bearer ${token}`,
                  },
              });

              // Fetch gown packages
              const gownPackagesResponse = await axios.get('http://127.0.0.1:5000/gown-packages', {
                  headers: {
                      'Authorization': `Bearer ${token}`,
                  },
              });

              // Set the data
              this.availableSuppliers = suppliersResponse.data;
              this.packageServices = packageServicesResponse.data;
              this.gownPackages = gownPackagesResponse.data;
          } catch (error) {
              console.error('Error fetching data:', error.response?.data || error.message);
          }
      },


    addSupplier() {
        this.packageData.suppliers.push({
        type: 'internal',
        supplier_id: '',
        external_supplier_name: '',
        external_supplier_contact: '',
        external_supplier_price: null,
        remarks: ''
      });
    },
    resetSupplierFields(supplier) {
      if (supplier.type === 'internal') {
        supplier.external_supplier_name = '';
        supplier.external_supplier_contact = '';
        supplier.external_supplier_price = null;
      } else {
        supplier.supplier_id = '';
      }
      supplier.remarks = '';
    },
    removeSupplier(index) {
      this.packageData.suppliers.splice(index, 1);
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
                      this.closeEditPackagesBtn();                      
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


          updateSupplierPrice(value) {
            if (this.supplier.price !== undefined) {
            this.supplier.price = value;
            } else {
            this.supplier.external_supplier_price = value;
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

    nextPackageForm() {
        this.packageDetails = false;
    },

    formatPrice(price) {
      if (price === null || price === undefined || typeof price === 'object' || isNaN(price)) {
        return 'N/A'; // Return a fallback if price is invalid
      }
      // Ensure price is treated as a number, round to 2 decimal places, and format with commas
      return parseFloat(price).toFixed(2).replace(/\d(?=(\d{3})+\.)/g, '$&,');
    },
    
        
    
    
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
    supplierPrice() {
    return this.supplier.price || this.supplier.external_supplier_price || 0;
   },

},

    mounted() {
      this.fetchPackages();
      this.fetchVenues();
      this.fetchSuppliersAndPackageServices();
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