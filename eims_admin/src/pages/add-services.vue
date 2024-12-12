    <template>
        <div class="bg-gray-200 w-full h-full">
        <div class="w-full h-[65px] bg-gray-100 mt-2 flex items-center justify-between px-5 shadow-lg">
        <h1 class="font-amaticBold font-extraLight text-3xl">
        Events Packages
    </h1>
    </div>
    
    <div class="flex flex-row items-center m-5 space-x-5">
        <div class="flex justify-start w-52 h-20 bg-white rounded-lg shadow-lg px-2 items-center border-l-2 border-green-400 space-x-5">
            <img class="w-auto h-12" src="/img/box.png" alt="Vendor Image">
            <h2 class="font-amaticRegular text-4xl font-bold mb-0"> {{ totalPackages }} <span class = "text-sm antialiased text-gray-600">packages</span></h2>
        </div>
    </div>
    
    <div class="flex flex-row justify-between items-center m-5 my-7">
    <div class = "flex">
    <button class = "mr-2 w-36 h-10 bg-[#9B111E] font-semibold text-gray-100 font-quicksand rounded-full shadow-lg 
    transition-transform duration-300 transform hover:scale-105" @click="addPackagesBtn">
    + Add Package
    </button>
    </div>
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
    <form v-if="addPackagesForm" @submit.prevent="addPackages" class="flex justify-center items-center fixed inset-0 bg-gray-800 bg-opacity-50 overflow-y-auto" @click.self="closePackagesForm">
      <div class="bg-white w-[800px] p-5 rounded-lg shadow-lg overflow-y-auto max-h-[90vh]">
        <div class="flex justify-between items-center mb-5">
          <h1 class="font-semibold text-xl text-gray-800">Add Package</h1>
          <button class="bg-red-500 text-white px-3 py-1 rounded hover:bg-red-600" @click="closePackagesForm">
            Close
          </button>
        </div>

        <div class="border-b border-gray-300 mb-5"></div>

        <!-- Package Details -->
        <div>
          <h2 class="font-semibold text-lg text-gray-800 mb-4">Package Details</h2>
          <div class="grid grid-cols-2 gap-4">
            <input type="text" v-model="packageData.package_name" class="p-2 w-full rounded-md border-gray-300 shadow-sm focus:ring focus:ring-blue-200" placeholder="Package Name" required />
            <input type="text" v-model="packageData.package_type" class="p-2 w-full rounded-md border-gray-300 shadow-sm focus:ring focus:ring-blue-200" placeholder="Package Type (Ex. Wedding)" required />
            <input type="number" v-model="packageData.capacity" class="p-2 w-full rounded-md border-gray-300 shadow-sm focus:ring focus:ring-blue-200" placeholder="Set Capacity" required />
            <input type="number" v-model="packageData.additional_capacity_charges" class="p-2 w-full rounded-md border-gray-300 shadow-sm focus:ring focus:ring-blue-200" placeholder="Additional Capacity Charges" required />
          </div>

          <div class="mt-5">
            <label for="charge_unit" class="block text-sm font-medium text-gray-700">Unit for Additional Charges</label>
            <input type="number" id="charge_unit" v-model="packageData.charge_unit" class="mt-2 p-2 w-full rounded-md border-gray-300 shadow-sm focus:ring focus:ring-blue-200" placeholder="Set person unit" required />
          </div>

          <div class="mt-5">
            <textarea v-model="packageData.description" class="p-2 w-full h-24 rounded-md border-gray-300 shadow-sm focus:ring focus:ring-blue-200 resize-none" placeholder="Description" required></textarea>
          </div>
        </div>

        <!-- Inclusion Buttons -->
        <h2 class="font-semibold text-lg text-gray-800 mt-8 mb-4">Add Inclusions</h2>
        <div class="grid grid-cols-3 gap-4 mb-4">
          <button @click.prevent="openInclusionModal('supplier')" class="bg-blue-500 text-white px-3 py-2 rounded-md hover:bg-blue-600">Suppliers</button>
          <button @click.prevent="addEmptyInclusion('venue')" class="bg-blue-500 text-white px-3 py-2 rounded-md hover:bg-blue-600">Venue</button>
          <button @click.prevent="addEmptyInclusion('outfit')" class="bg-blue-500 text-white px-3 py-2 rounded-md hover:bg-blue-600">Outfit Package</button>
        </div>

    <!-- Inclusion Modal -->
      <div v-if="showInclusionModal" @click.self="closeInclusionModal" class="fixed inset-0 bg-black bg-opacity-50 flex justify-center items-center z-50">
        <div class="bg-white w-[500px] p-6 rounded-lg shadow-lg">
          <div class="flex justify-between items-center mb-4">
            <h2 class="text-lg font-semibold">Select Service Type</h2>
            <button @click="closeInclusionModal" class="text-red-500 hover:text-red-700">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
              </svg>
            </button>
          </div>

          <div class="grid grid-cols-1 gap-2">
            <button 
              v-for="serviceType in supplierTypes" 
              :key="serviceType"
              @click="addEmptySupplierInclusion(serviceType)"
              class="w-full text-left px-4 py-2 bg-gray-50 hover:bg-gray-100 rounded-md transition duration-150"
            >
              {{ serviceType }}
            </button>
          </div>
        </div>
      </div>
            


        <!-- Inclusion Table -->
        <div class="overflow-x-auto">
          <table class="w-full table-auto border-collapse border border-gray-300">
            <thead class="bg-gray-200">
                <tr>
                  <th class="border border-gray-300 px-4 py-2 text-left">Type</th>
                  <th class="border border-gray-300 px-4 py-2 text-left">Details</th>
                  <th class="border border-gray-300 px-4 py-2 text-left">Price</th>
                  <th class="border border-gray-300 px-4 py-2 text-left">Actions</th>
                </tr>
              </thead>
              <tbody>
              <tr v-for="(inclusion, index) in inclusions" :key="index" class="border border-gray-300">
                <td class="border border-gray-300 px-4 py-2 capitalize">{{ inclusion.type }}</td>
                <td class="border border-gray-300 px-4 py-2">
                  <!-- Supplier select -->
                  <span v-if="inclusion.type === 'supplier'">
                    <select 
                      v-model="inclusion.data" 
                      class="w-full p-2 rounded-md border-gray-300 shadow-sm focus:ring focus:ring-blue-200"
                    >
                      <option value="">Select {{ inclusion.serviceType }}</option>
                      <option 
                        v-for="supplier in filteredSuppliers(inclusion.serviceType)" 
                        :key="supplier.supplier_id" 
                        :value="supplier"
                      >
                        {{ supplier.firstname }} {{ supplier.lastname }}
                      </option>
                    </select>
                  </span>
                  <!-- Venue select -->
                  <select v-if="inclusion.type === 'venue'" 
                          v-model="inclusion.data" 
                          class="w-full p-2 rounded-md border-gray-300 shadow-sm focus:ring focus:ring-blue-200">
                    <option value="">Select Venue</option>
                    <option v-for="venue in venues" :key="venue.selectVenueId" :value="venue">
                      {{ venue.selectVenue_name }}
                    </option>
                  </select>
                  <!-- Outfit select -->
                  <select v-if="inclusion.type === 'outfit'" 
                          v-model="inclusion.data" 
                          class="w-full p-2 rounded-md border-gray-300 shadow-sm focus:ring focus:ring-blue-200">
                    <option value="">Select Outfit Package</option>
                    <option v-for="gp in gownPackages" :key="gp.gown_package_id" :value="gp">
                      {{ gp.gown_package_name }}
                    </option>
                  </select>
                </td>
                <td class="border border-gray-300 px-4 py-2">
                <!-- Price based on type -->
                <span v-if="inclusion.type === 'supplier' && inclusion.data">
                  {{ formatPrice(inclusion.data.price) }} php
                </span>
                <span v-else-if="inclusion.type === 'venue' && inclusion.data">
                  {{ formatPrice(inclusion.data.selectVenue_price) }} php
                </span>
                <span v-else-if="inclusion.type === 'outfit' && inclusion.data">
                  {{ formatPrice(inclusion.data.gown_package_price) }} php
                </span>
                <span v-else>-</span>
              </td>
                <td class="border border-gray-300 px-4 py-2">
                  <button 
                    @click="removeInclusion(index)" 
                    class="bg-red-500 text-white px-2 py-1 rounded hover:bg-red-600"
                  >
                    Remove
                  </button>
                </td>
              </tr>
            </tbody>
            </table>
        </div>

        <!-- Submit Button -->
        <div class="flex justify-center mt-8">
          <button type="submit" class="bg-green-500 text-white px-4 py-2 rounded-md hover:bg-green-600">Create Package</button>
        </div>
      </div>
    </form>


 <!-- Edit Packages Form -->
 <form v-if="editPackagesForm" @submit.prevent="confirmEditPackage" class="flex justify-center items-center fixed inset-0 bg-gray-800 bg-opacity-50 overflow-y-auto" @click.self="closeEditPackagesBtn">
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
      editPackagesForm: false,
      addPackagesDetails: false,
      addStaffDetails: false,

      inclusionType: '',
      selectedInclusion: '',
      showInclusionModal: false,
      inclusions: [],
      selectedInclusionType: '',
      supplierTypes: [
        'Catering',
        'Photography',
        'Videography',
        'Entertainment',
        'Sound and Lighting',
        'Transportation',
        'Host',
        'Invitation and Stationery',
        'Favors and Gifts',
        'Hair Stylist',
        'Makeup Artist',
      ],
      availableSuppliers: [],
      venues: [],
      gownPackages: [],
      packageData: {
        package_name: '',
        package_type: '',
        venue_id: null,
        capacity: null,
        additional_capacity_charges: null,
        charge_unit: 1,
        description: '',
        suppliers: [],
      },
      packages: [],
      selectedVenue: null,
      selectedOutfit: null,
  
      


      
    };
  },
 
  methods: {
    openInclusionModal(type) {
        this.showInclusionModal = true;
      },

      closeInclusionModal() {
        this.showInclusionModal = false;
      },

      addEmptySupplierInclusion(serviceType) {
        console.log('Adding supplier inclusion for service type:', serviceType);
        this.inclusions.push({
          type: 'supplier',
          serviceType: serviceType,
          data: null
        });
        this.closeInclusionModal();
      },

      addEmptyInclusion(type) {
        this.inclusions.push({
          type: type,
          data: null
        });
      },

      removeInclusion(index) {
        this.inclusions.splice(index, 1);
      },

      filteredSuppliers(serviceType) {
        return this.availableSuppliers.filter(supplier => supplier.service === serviceType);
      },

      async addPackages() {
          try {
            // Validate that all inclusions have data selected
            const hasEmptyInclusions = this.inclusions.some(inclusion => !inclusion.data);
            if (hasEmptyInclusions) {
              alert('Please select all inclusion details before submitting.');
              return;
            }

            // Prepare package data with explicit conversion and validation
            const packageData = {
              package_name: this.packageData.package_name,
              package_type: this.packageData.package_type,
              venue_id: this.inclusions.find(inc => inc.type === 'venue' && inc.data)?.data?.selectVenueId || null,
              capacity: Number(this.packageData.capacity),
              additional_capacity_charges: Number(this.packageData.additional_capacity_charges),
              charge_unit: Number(this.packageData.charge_unit),
              description: this.packageData.description,
              suppliers: this.inclusions
                .filter(inclusion => inclusion.type === 'supplier' && inclusion.data)
                .map(inclusion => ({
                  supplier_id: Number(inclusion.data.supplier_id),
                  type: 'internal',
                  remarks: `${inclusion.data.service} service`
                })),
              gown_package_id: this.inclusions.find(inc => inc.type === 'outfit' && inc.data)?.data?.gown_package_id || null,
            };

            // Additional validation
            if (!packageData.package_name || !packageData.package_type) {
              alert('Package name and type are required.');
              return;
            }

            if (packageData.suppliers.length === 0) {
              alert('At least one supplier is required.');
              return;
            }

            console.log('Sending package data:', packageData);  // Debug log

            const response = await axios.post('http://127.0.0.1:5000/create-package', packageData, {
              headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${localStorage.getItem('access_token')}`,
              },
            });

            if (response.status === 201) {
              alert('Package created successfully!');
              this.resetPackageForm();
              this.fetchPackages(); // Refresh the packages list
            }
          } catch (error) {
            console.error('Error creating package:', error);
            let errorMessage = 'Failed to create package. Please try again.';
            
            if (error.response) {
              console.error('Error response:', error.response.data);
              errorMessage = error.response.data.message || 
                            error.response.data.error || 
                            'Failed to create package. Please check your input.';
            }
            
            alert(errorMessage);
            this.errorMessage = errorMessage;
          }
        },
    resetPackageForm() {
      this.packageData = {
        package_name: '',
        package_type: '',
        venue_id: null,
        capacity: null,
        additional_capacity_charges: null,
        charge_unit: 1,
        description: '',
        suppliers: [],
      };
      this.inclusions = [];
      this.addPackagesForm = false;
    },
    closePackagesForm() {
      this.resetPackageForm();
    },

    addVenue() {
    if (this.selectedVenue) {
      this.inclusions.push({
        type: 'venue',
        data: this.selectedVenue
      });
      this.selectedVenue = null;
    }
  },
  addOutfit() {
    if (this.selectedOutfit) {
      this.inclusions.push({
        type: 'outfit',
        data: this.selectedOutfit
      });
      this.selectedOutfit = null;
    }
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
                alert('You are not logged in. Please log in to fetch data.');
                return;
              }

              const [suppliersResponse, venuesResponse, gownPackagesResponse] = await Promise.all([
                axios.get('http://127.0.0.1:5000/suppliers', {
                  headers: { Authorization: `Bearer ${token}` },
                }),
                axios.get('http://127.0.0.1:5000/created-venues', {
                  headers: { Authorization: `Bearer ${token}` },
                }),
                axios.get('http://127.0.0.1:5000/gown-packages', {
                  headers: { Authorization: `Bearer ${token}` },
                }),
              ]);

              this.availableSuppliers = suppliersResponse.data;
              this.venues = venuesResponse.data.map(venue => ({
                ...venue,
                selectVenueId: venue.venue_id,
                selectVenue_name: venue.venue_name,
                selectVenue_price: venue.venue_price,
              }));
              this.gownPackages = gownPackagesResponse.data;
            } catch (error) {
              console.error('Error fetching data:', error.response?.data || error.message);
            }
          },
    formatInclusionDetails(inclusion) {
      if (this.inclusionType === 'supplier') {
        return `${inclusion.firstname} ${inclusion.lastname} - ${inclusion.service}`;
      }
      if (this.inclusionType === 'venue') {
        return `${inclusion.selectVenue_name} - ${this.formatPrice(inclusion.selectVenue_price)}`;
      }
      if (this.inclusionType === 'outfit') {
        return `${inclusion.gown_package_name} - ${this.formatPrice(inclusion.gown_package_price)}`;
      }
      return '';
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
      console.log('Component mounted');
      this.fetchSuppliersAndPackageServices();
      console.log('Fetch completed');
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