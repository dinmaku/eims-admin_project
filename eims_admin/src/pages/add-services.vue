    <template>
    <div class="bg-gray-200 w-full h-full">
        <div class="w-full h-[65px] bg-gray-100 mt-2 flex items-center justify-between px-5 shadow-lg">
            <h1 class="font-amaticBold font-extraLight text-3xl">
                Events Packages
            </h1>
            <button class="bg-[#9B111E] text-white px-3 py-1 rounded shadow-lg 
              transition-transform duration-300 transform hover:scale-105" @click="displayEventTypeBtn">+ Event Type</button>
        </div>
        
        <div class="flex flex-row items-center m-5 space-x-5">
            <div class="flex justify-start w-52 h-20 bg-white rounded-lg shadow-lg px-2 items-center border-l-2 border-green-400 space-x-5">
                <img class="w-auto h-12" src="/img/box.png" alt="Vendor Image">
                <h2 class="font-amaticRegular text-4xl font-bold mb-0"> {{ totalPackages }} <span class = "text-sm antialiased text-gray-600">packages</span></h2>
            </div>
        </div>
        
        <div class="flex flex-row justify-end items-center m-5 my-7">
        <div class = "flex">
        <button class = "mr-2 w-36 h-10 bg-[#9B111E] font-semibold text-gray-100 font-quicksand rounded-md shadow-lg 
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
                        <td class="px-4 py-3">{{ getEventTypeName(packageItem.event_type_id) }}</td>
                        <td class="px-4 py-3">{{ packageItem.venue_name }}</td>
                        <td class="px-4 py-3">{{ formatPrice(packageItem.total_price) }} php</td>
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
                    class="px-3 py-1 bg-[#9B111E] text-white rounded-md hover:bg-[#B73A45] disabled:opacity-50 text-sm">
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
          </div>

          <div class="border-b border-gray-300 mb-5"></div>

          <!-- Package Details -->
          <div>
            <h2 class="font-semibold text-lg text-gray-800 mb-4">Package Details</h2>
            <div class="grid grid-cols-2 gap-4">
              <input type="text" v-model="packageData.package_name" class="p-2 w-full rounded-md border-gray-300 shadow-sm focus:ring focus:ring-blue-200" placeholder="Package Name" required />
              <select v-model="packageData.event_type_id" class="p-2 w-full rounded-md border-gray-300 shadow-sm focus:ring focus:ring-blue-200">
                <option disabled value="">Select Event Type</option>
                <option v-for="type in eventTypes" :key="type.event_type_id" :value="type.event_type_id">
                  {{ type.event_type_name }}
                </option>
                <option value="add-new">+ Add New Event Type</option>
              </select>

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
          <!-- Add New Event Type Modal -->
          <!-- Inclusion Buttons -->
          <div class="grid grid-cols-4 gap-4 mb-4">
            <button 
              @click.prevent="openInclusionModal('supplier')" 
              class="flex items-center justify-center bg-blue-500 text-white px-3 py-2 h-[50px] rounded-md hover:bg-blue-600"
            >
              <img alt="Supplier Icon" class="mr-2 w-[20px] h-[20px]" src="/img/supplier.png">
              Suppliers
            </button>
            <button 
              @click.prevent="openInclusionModal('venue')" 
              class="flex items-center justify-center bg-blue-500 text-white px-3 py-2 h-[50px] rounded-md hover:bg-blue-600"
            >
              <img alt="Venue Icon" class="mr-2 w-[20px] h-[20px]" src="/img/venues1.png">
             Venue
            </button>
            <button 
              @click.prevent="openInclusionModal('outfit')" 
              class="flex items-center justify-center bg-blue-500 text-white px-3 py-2 h-[50px] rounded-md hover:bg-blue-600"
            >
              <img alt="Outfit Icon" class="mr-2 w-[20px] h-[20px]" src="/img/costume.png">
             Outfit Package
            </button>
            <button 
              @click.prevent="openInclusionModal('service')" 
              class="flex items-center justify-center bg-blue-500 text-white px-3 py-2 h-[50px] rounded-md hover:bg-blue-600"
            >
              <img alt="Service Icon" class="mr-2 w-[20px] h-[20px]" src="/img/additionals.png">
              Additionals
            </button>
          </div>

      <!-- Inclusion Modal for Selecting Supplier Type -->
      <div v-if="showInclusionModal && selectedInclusionType === 'supplier'" @click.self="closeInclusionModal" class="fixed inset-0 bg-black bg-opacity-50 flex justify-center items-center z-50">
        <div class="bg-white w-[500px] p-6 rounded-lg shadow-lg">
          <div class="flex justify-between items-center mb-4">
            <h2 class="text-lg font-semibold">Select Supplier Type</h2>
            <button @click="closeInclusionModal" class="text-red-500 hover:text-red-700">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
              </svg>
            </button>
          </div>
          <div class="grid grid-cols-1 gap-2">
            <button v-for="serviceType in supplierTypes" :key="serviceType" @click="selectSupplierType(serviceType)" class="w-full text-left px-4 py-2 bg-gray-50 hover:bg-gray-100 rounded-md transition duration-150">
              {{ serviceType }}
            </button>
          </div>
        </div>
      </div>

      <!-- Inclusion Modal for Selecting Specific Supplier -->
      <div v-if="showSupplierModal" @click.self="closeSupplierModal" class="fixed inset-0 bg-black bg-opacity-50 flex justify-center items-center z-50">
        <div class="bg-white w-[500px] p-6 rounded-lg shadow-lg">
          <div class="flex justify-between items-center mb-4">
            <h2 class="text-lg font-semibold">Select Supplier</h2>
            <button @click="closeSupplierModal" class="text-red-500 hover:text-red-700">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
              </svg>
            </button>
          </div>
          <div>
            <label for="supplier" class="block text-sm font-medium text-gray-700">Select Supplier</label>
            <select v-model="selectedSupplier" class="w-full p-2 rounded-md border-gray-300 shadow-sm focus:ring focus:ring-blue-200">
              <option selected disabled value="">Select {{ selectedSupplierType }}</option>
              <option v-for="supplier in filteredSuppliers(selectedSupplierType)" :key="supplier.supplier_id" :value="supplier">
                {{ supplier.firstname }} {{ supplier.lastname }}
              </option>
            </select>
          </div>
          <div class="flex justify-center mt-4">
            <button type="button" @click="addSelectedSupplier" class="bg-green-500 text-white px-4 py-2 rounded-md hover:bg-green-600">Add</button>
          </div>
        </div>
      </div>

      <!-- Inclusion Modal for Selecting Venue -->
      <div v-if="showVenueModal" @click.self="closeVenueModal" class="fixed inset-0 bg-black bg-opacity-50 flex justify-center items-center z-50">
        <div class="bg-white w-[500px] p-6 rounded-lg shadow-lg">
          <div class="flex justify-between items-center mb-4">
            <h2 class="text-lg font-semibold">Select Venue</h2>
            <button @click="closeVenueModal" class="text-red-500 hover:text-red-700">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
              </svg>
            </button>
          </div>
          <div>
            <label for="venue" class="block text-sm font-medium text-gray-700">Select Venue</label>
            <select v-model="selectedVenue" class="w-full p-2 rounded-md border-gray-300 shadow-sm focus:ring focus:ring-blue-200">
              <option selected disabled value="">Select Venue</option>
              <option v-for="venue in venues" :key="venue.venue_id" :value="venue">
                {{ venue.venue_name }} ({{ venue.location }}) - {{ formatPrice(venue.venue_price) }}
              </option>
            </select>
          </div>
          <div class="flex justify-center mt-4">
            <button type="button" @click="addSelectedVenue" class="bg-green-500 text-white px-4 py-2 rounded-md hover:bg-green-600">Add</button>
          </div>
        </div>
      </div>

      <!-- Inclusion Modal for Selecting Outfit Package -->
      <div v-if="showOutfitModal" @click.self="closeOutfitModal" class="fixed inset-0 bg-black bg-opacity-50 flex justify-center items-center z-50">
        <div class="bg-white w-[500px] p-6 rounded-lg shadow-lg">
          <div class="flex justify-between items-center mb-4">
            <h2 class="text-lg font-semibold">Select Outfit Package</h2>
            <button @click="closeOutfitModal" class="text-red-500 hover:text-red-700">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
              </svg>
            </button>
          </div>
          <div>
            <label for="outfit" class="block text-sm font-medium text-gray-700">Select Outfit Package</label>
            <select v-model="selectedOutfit" class="w-full p-2 rounded-md border-gray-300 shadow-sm focus:ring focus:ring-blue-200">
              <option selected disabled value="">Select Outfit Package</option>
              <option v-for="gownPackage in gownPackages" :key="gownPackage.gown_package_id" :value="gownPackage">
                {{ gownPackage.gown_package_name }} - {{ formatPrice(gownPackage.gown_package_price) }} php
              </option>
            </select>
          </div>
          <div class="flex justify-center mt-4">
            <button type="button" @click="addSelectedOutfit" class="bg-green-500 text-white px-4 py-2 rounded-md hover:bg-green-600">Add</button>
          </div>
        </div>
      </div>

      <!-- Inclusion Modal for Selecting Additional Services -->
        <div v-if="showServiceModal" @click.self="closeServiceModal" class="fixed inset-0 bg-black bg-opacity-50 flex justify-center items-center z-50">
          <div class="bg-white w-[500px] p-6 rounded-lg shadow-lg">
            <div class="flex justify-between items-center mb-4">
              <h2 class="text-lg font-semibold">Select Additional Service</h2>
              <button @click="closeServiceModal" class="text-red-500 hover:text-red-700">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
                </svg>
              </button>
            </div>
            <div>
              <label for="service" class="block text-sm font-medium text-gray-700">Select Additional Service</label>
              <select v-model="selectedService" class="w-full p-2 rounded-md border-gray-300 shadow-sm focus:ring focus:ring-blue-200">
                <option selected disabled value="">Select Additional Service</option>
                <option v-for="service in filteredAdditionalServices" :key="service.add_service_id" :value="service">
                  {{ service.add_service_name }}
                </option>
              </select>
            </div>
            <div class="flex justify-center mt-4">
              <button type="button" @click="addSelectedService" class="bg-green-500 text-white px-4 py-2 rounded-md hover:bg-green-600">Add</button>
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
              <td class="border border-gray-300 px-4 py-2 capitalize">
                {{ inclusion.type === 'supplier' ? `Supplier(${inclusion.serviceType})` : inclusion.type }}
              </td>
              <td class="border border-gray-300 px-4 py-2">{{ getInclusionName(inclusion) }}</td>
              <td class="border border-gray-300 px-4 py-2">{{ getInclusionPrice(inclusion) }}</td>
              <td class="border border-gray-300 py-2">
                <div @click="removeInclusion(index)" class="inline-block cursor-pointer">
                  <img 
                    alt="Delete Icon" 
                    class="w-[20px] h-[20px] transition-transform transform hover:scale-110 hover:brightness-90" 
                    src="/img/delete.png" 
                  >
                </div>
              </td>
            </tr>
          </tbody>
        </table>
        <div class="mt-4 p-4 bg-gray-50 rounded-lg shadow-sm">
          <div class="flex justify-between items-center">
            <div class="text-lg font-semibold text-gray-700">Total Package Price:</div>
            <div class="text-xl font-bold text-blue-600">₱{{ formatPrice(
              inclusions.reduce((total, inc) => {
                if (inc.type === 'supplier' && inc.data) total += Number(inc.data.price || 0);
                if (inc.type === 'venue' && inc.data) total += Number(inc.data.venue_price || 0);
                if (inc.type === 'outfit' && inc.data) total += Number(inc.data.gown_package_price || 0);
                if (inc.type === 'service' && inc.data) total += Number(inc.data.add_service_price || 0);
                return total;
              }, 0)
            ) }}</div>
          </div>
          <div class="mt-2 text-sm text-gray-500">
            * Price includes all selected inclusions (suppliers, services, venue, and outfit package)
          </div>
        </div>
      </div>

      <!-- Submit Button -->
      <div class="flex justify-center mt-8 space-x-3">
        <button class="bg-gray-300 text-white px-3 py-1 rounded hover:bg-gray-400" @click="closePackagesForm">Cancel</button>
        <button type="submit" class="bg-blue-500 text-white px-4 py-2 rounded-md hover:bg-blue-600">Save</button>
      </div>
    </div>
  </form>

  <!-- Add New Event Type Modal -->
  <div
    v-if="showAddEventTypeModal"
    @click.self="closeAddEventTypeModal"
    class="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50 z-50"
  >
    <div class="bg-white rounded-lg shadow-lg w-[400px] p-6">
      <h2 class="text-xl font-semibold mb-4 text-gray-800">Add New Event Type</h2>
      <input
        v-model="newEventTypeName"
        type="text"
        class="p-2 w-full rounded-md border-gray-300 shadow-sm focus:ring focus:ring-blue-200"
        placeholder="Enter Event Type Name"
      />
      <div class="flex justify-end mt-4 space-x-2">
        <button
          @click="saveNewEventType"
          class="px-4 py-2 text-white bg-blue-500 rounded-md hover:bg-blue-600"
        >
          Save
        </button>
        <button
          @click="closeAddEventTypeModal"
          class="px-4 py-2 text-gray-700 bg-gray-300 rounded-md hover:bg-gray-400 mr-2"
        >
          Cancel
        </button>
      </div>
    </div>
  </div>

  <!-- Edit Packages Form -->
  <form v-if="editPackagesForm" @submit.prevent="confirmEditPackage" class="flex justify-center items-center fixed inset-0 bg-gray-800 bg-opacity-50 overflow-y-auto" @click.self="closeEditPackagesBtn">
    <div class="bg-white w-[800px] p-5 rounded-lg shadow-lg overflow-y-auto max-h-[90vh]">
      <div class="flex justify-between items-center mb-5">
        <h1 class="font-semibold text-xl text-gray-800">Edit Package</h1>
        <button class="bg-red-500 text-white px-3 py-1 rounded hover:bg-red-600" @click="closeEditPackagesBtn">Close</button>
      </div>

      <div class="border-b border-gray-300 mb-5"></div>

      <!-- Package Details -->
      <div>
        <h2 class="font-semibold text-lg text-gray-800 mb-4">Package Details</h2>
        <div class="grid grid-cols-2 gap-4">
          <input type="text" v-model="selectedPackage.package_name" class="p-2 w-full rounded-md border-gray-300 shadow-sm focus:ring focus:ring-blue-200" placeholder="Package Name" required />
          <select v-model="selectedPackage.package_type" class="p-2 w-full rounded-md border-gray-300 shadow-sm focus:ring focus:ring-blue-200" required>
            <option value="">Select Package Type</option>
            <option value="Wedding">Wedding</option>
            <option value="Birthday">Birthday</option>
            <option value="Debut">Debut</option>
          </select>
          <input type="number" v-model="selectedPackage.capacity" class="p-2 w-full rounded-md border-gray-300 shadow-sm focus:ring focus:ring-blue-200" placeholder="Set Capacity" required />
          <input type="number" v-model="selectedPackage.total_price" class="p-2 w-full rounded-md border-gray-300 shadow-sm focus:ring focus:ring-blue-200" placeholder="Total Price" required />
        </div>

        <div class="mt-5">
          <textarea v-model="selectedPackage.description" class="p-2 w-full h-24 rounded-md border-gray-300 shadow-sm focus:ring focus:ring-blue-200 resize-none" placeholder="Description" required></textarea>
        </div>
      </div>

      <!-- Inclusion Buttons -->
      <div class="grid grid-cols-4 gap-4 mb-4">
        <button 
          @click.prevent="openInclusionModal('supplier')" 
          class="flex items-center justify-center bg-blue-500 text-white px-3 py-2 h-[50px] rounded-md hover:bg-blue-600"
        >
          <img alt="Supplier Icon" class="mr-2 w-[20px] h-[20px]" src="/img/supplier.png">
          Suppliers
        </button>
        <button 
          @click.prevent="openInclusionModal('venue')" 
          class="flex items-center justify-center bg-blue-500 text-white px-3 py-2 h-[50px] rounded-md hover:bg-blue-600"
        >
          <img alt="Venue Icon" class="mr-2 w-[20px] h-[20px]" src="/img/venues1.png">
         Venue
        </button>
        <button 
          @click.prevent="openInclusionModal('outfit')" 
          class="flex items-center justify-center bg-blue-500 text-white px-3 py-2 h-[50px] rounded-md hover:bg-blue-600"
        >
          <img alt="Outfit Icon" class="mr-2 w-[20px] h-[20px]" src="/img/costume.png">
         Outfit Package
        </button>
        <button 
          @click.prevent="openInclusionModal('service')" 
          class="flex items-center justify-center bg-blue-500 text-white px-3 py-2 h-[50px] rounded-md hover:bg-blue-600"
        >
          <img alt="Service Icon" class="mr-2 w-[20px] h-[20px]" src="/img/additionals.png">
          Additionals
        </button>
      </div>

      <!-- Inclusions Table -->
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
            <tr v-for="(inclusion, index) in selectedPackage.inclusions" :key="index" class="border border-gray-300">
              <td class="border border-gray-300 px-4 py-2 capitalize">
                {{ inclusion.type === 'supplier' ? `Supplier(${inclusion.serviceType})` : inclusion.type }}
              </td>
              <td class="border border-gray-300 px-4 py-2">
                <!-- Supplier select -->
                <span v-if="inclusion.type === 'supplier'">
                  <select v-model="inclusion.data" class="w-full p-2 rounded-md border-gray-300 shadow-sm focus:ring focus:ring-blue-200">
                    <option value="">Select {{ inclusion.serviceType }}</option>
                    <option v-for="supplier in filteredSuppliers(inclusion.serviceType)" :key="supplier.supplier_id" :value="supplier">
                      {{ supplier.firstname }} {{ supplier.lastname }}
                    </option>
                  </select>
                </span>

                <!-- Venue select -->
                <select v-if="inclusion.type === 'venue'" v-model="inclusion.data" class="w-full p-2 rounded-md border-gray-300 shadow-sm focus:ring focus:ring-blue-200">
                  <option value="">Select Venue</option>
                  <option v-for="venue in venues" :key="venue.selectVenueId" :value="venue">
                    {{ venue.selectVenue_name }}
                  </option>
                </select>

                <!-- Outfit select -->
                <select v-if="inclusion.type === 'outfit'" v-model="inclusion.data" class="w-full p-2 rounded-md border-gray-300 shadow-sm focus:ring focus:ring-blue-200">
                  <option value="">Select Outfit Package</option>
                  <option v-for="gp in gownPackages" :key="gp.gown_package_id" :value="gp">
                    {{ gp.gown_package_name }}
                  </option>
                </select>

                <!-- Additional Services select -->
                <select v-if="inclusion.type === 'service'" v-model="inclusion.data" class="w-full p-2 rounded-md border-gray-300 shadow-sm focus:ring focus:ring-blue-200">
                  <option value="">Select Additional Service</option>
                  <option v-for="service in filteredAdditionalServices" :key="service.add_service_id" :value="service">
                    {{ service.add_service_name }}
                  </option>
                </select>
              </td>
              <td class="border border-gray-300 px-4 py-2">{{ formatPrice(inclusion.data?.price || 0) }}</td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- Submit and Delete Buttons -->
      <div class="flex justify-center space-x-4 mt-8">
        <button type="submit" class="bg-green-500 text-white px-4 py-2 rounded-md hover:bg-green-600">Update Package</button>
        <button type="button" @click="deletePackage(selectedPackage.packageId)" class="bg-red-500 text-white px-4 py-2 rounded-md hover:bg-red-600">Delete Package</button>
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
      showAddEventTypeModal: false,
      newEventTypeName: "",
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
      selectedSupplierType: '',
      selectedSupplier: null,
      selectedVenue: null,
      selectedOutfit: null,
      selectedService: null,
      showInclusionModal: false,
      showSupplierModal: false,
      showVenueModal: false,
      showOutfitModal: false,
      showServiceModal: false,
      inclusions: [],
      selectedInclusionType: '',
      supplierTypes: [
        'Catering',
        'Photographer',
        'Videographer',
        'Entertainment',
        'Sound and Lighting',
        'Transportation',
        'Host',
        'Invitations',
        'Favors and Gifts',
        'Hair Stylist',
        'Makeup Artist',
      ],
      eventTypes: [],
      availableSuppliers: [],
      venues: [],
      gownPackages: [],
      additionalServices: [],
      packageData: {
        package_name: '',
        event_type_id: '',
        venue_id: null,
        capacity: null,
        additional_capacity_charges: null,
        charge_unit: 1,
        description: '',
        suppliers: [],
        additional_services: [],
      },
      packages: [],
      selectedPackage: {
        packageId: null,
        package_name: '',
        event_type_id: '',
        capacity: 0,
        total_price: 0,
        description: '',
        inclusions: [],
        selectedSuppliers: [],
        selectedVenue: null,
        selectedOutfitPackage: null,
        selectedAdditionalServices: []
      },
      
    };
  },
 
  methods: {
    addNewEventType() {
      this.showAddEventTypeModal = true; // Show modal
      this.packageData.event_type_id = ""; // Reset selection
    },
    closeAddEventTypeModal() {
      this.showAddEventTypeModal = false; // Hide modal
      this.newEventTypeName = ""; // Reset input
    },
    
    async saveNewEventType() {
        if (!this.newEventTypeName.trim()) {
          alert("Event type name cannot be empty.");
          return;
        }

        try {
          const response = await axios.post('http://127.0.0.1:5000/create-event-type', 
            { event_type_name: this.newEventTypeName.trim() },
            {
              headers: {
                'Authorization': `Bearer ${localStorage.getItem('access_token')}`,
              },
            }
          );

          const newEventType = response.data.event_type;
          this.eventTypes.push(newEventType);
          this.packageData.event_type_id = newEventType.event_type_id;
          this.closeAddEventTypeModal();
          alert('Event type added successfully!');
        } catch (error) {
          console.error('Error creating event type:', error);
          alert(error.response?.data?.error || 'Failed to create event type');
        }
      },
    openInclusionModal(type) {
        this.selectedInclusionType = type;  // Add this line
        switch (type) {
          case 'supplier':
            this.showInclusionModal = true;
            break;
          case 'venue':
            this.openVenueModal();
            break;
          case 'outfit':
            this.openOutfitModal();
            break;
          case 'service':
            this.openServiceModal();
            break;
        }
      },
    closeInclusionModal() {
      this.showInclusionModal = false;
    },
    openSupplierModal() {
      this.showSupplierModal = true;
    },
    closeSupplierModal() {
      this.showSupplierModal = false;
    },
    openVenueModal() {
      this.showVenueModal = true;
    },
    closeVenueModal() {
      this.showVenueModal = false;
    },
    openOutfitModal() {
      this.showOutfitModal = true;
    },
    closeOutfitModal() {
      this.showOutfitModal = false;
    },
    openServiceModal() {
      this.showServiceModal = true;
    },
    closeServiceModal() {
      this.showServiceModal = false;
    },
    selectSupplierType(serviceType) {
      this.selectedSupplierType = serviceType;
      this.closeInclusionModal();
      this.openSupplierModal();
    },
    addSelectedSupplier() {
      if (this.selectedSupplier && this.selectedSupplierType) {
        this.inclusions.push({
          type: 'supplier',
          serviceType: this.selectedSupplierType,
          data: {
            ...this.selectedSupplier,
            service: this.selectedSupplierType
          }
        });
        this.selectedSupplier = null;
        this.closeSupplierModal();
      }
    },
    addSelectedVenue() {
      this.inclusions.push({
        type: 'venue',
        data: this.selectedVenue
      });
      this.selectedVenue = null;
      this.closeVenueModal();
    },
    addSelectedOutfit() {
      this.inclusions.push({
        type: 'outfit',
        data: this.selectedOutfit
      });
      this.selectedOutfit = null;
      this.closeOutfitModal();
    },
    addSelectedService() {
      this.inclusions.push({
        type: 'service',
        data: this.selectedService
      });
      this.selectedService = null;
      this.closeServiceModal();
    },
    getEventTypeName(eventTypeId) {
      const eventType = this.eventTypes.find(type => type.event_type_id === eventTypeId);
      return eventType ? eventType.event_type_name : 'N/A';
    },
    removeInclusion(index) {
      this.inclusions.splice(index, 1);
    },
    filteredSuppliers(serviceType) {
      return this.availableSuppliers.filter(supplier => supplier.service === serviceType && !this.inclusions.find(inclusion => inclusion.type === 'supplier' && inclusion.data && inclusion.data.supplier_id === supplier.supplier_id));
    },
    filteredVenues() {
      const selectedVenueIds = this.inclusions.filter(inc => inc.type === 'venue' && inc.data).map(inc => inc.data.venue_id);
      return this.venues.filter(venue => !selectedVenueIds.includes(venue.venue_id));
    },
    filteredGownPackages() {
      const selectedGownPackageIds = this.inclusions.filter(inc => inc.type === 'outfit' && inc.data).map(inc => inc.data.gown_package_id);
      return this.gownPackages.filter(pkg => !selectedGownPackageIds.includes(pkg.gown_package_id));
    },
    getInclusionName(inclusion) {
      if (inclusion.type === 'supplier' && inclusion.data) {
        return `${inclusion.data.firstname} ${inclusion.data.lastname}`;
      }
      if (inclusion.type === 'venue' && inclusion.data) {
        return inclusion.data.venue_name;
      }
      if (inclusion.type === 'outfit' && inclusion.data) {
        return inclusion.data.gown_package_name;
      }
      if (inclusion.type === 'service' && inclusion.data) {
        return inclusion.data.add_service_name;
      }
      return '';
    },
    getInclusionName(inclusion) {
      if (!inclusion || !inclusion.data) return '';
      
      switch (inclusion.type) {
        case 'supplier':
          return `${inclusion.data.firstname} ${inclusion.data.lastname}`;
        case 'venue':
          return inclusion.data.venue_name;
        case 'outfit':
          return inclusion.data.gown_package_name;
        case 'service':
          return inclusion.data.add_service_name;
        default:
          return '';
      }
    },
    getInclusionPrice(inclusion) {
        if (!inclusion || !inclusion.data) return '-';
        
        switch (inclusion.type) {
          case 'supplier':
            return `${this.formatPrice(inclusion.data.price)} php`;
          case 'venue':
            return `${this.formatPrice(inclusion.data.venue_price)} php`;
          case 'outfit':
            return `${this.formatPrice(inclusion.data.gown_package_price)} php`;
          case 'service':
            return `${this.formatPrice(inclusion.data.add_service_price)} php`;
          default:
            return '-';
        }
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
              event_type_id: this.packageData.event_type_id,
              venue_id: this.inclusions.find(inc => inc.type === 'venue' && inc.data)?.data?.venue_id || null,
              capacity: Number(this.packageData.capacity),
              additional_capacity_charges: Number(this.packageData.additional_capacity_charges),
              charge_unit: Number(this.packageData.charge_unit),
              description: this.packageData.description,
              suppliers: this.inclusions
              .filter(inclusion => inclusion.type === 'supplier' && inclusion.data)
              .map(inclusion => ({
                supplier_id: Number(inclusion.data.supplier_id),
                type: 'internal',  // All suppliers are internal
                price: Number(inclusion.data.price || 0),
                remarks: `${inclusion.serviceType} service`
              })),
              gown_package_id: this.inclusions.find(inc => inc.type === 'outfit' && inc.data)?.data?.gown_package_id || null,
              additional_services: this.inclusions
                .filter(inclusion => inclusion.type === 'service' && inclusion.data)
                .map(inclusion => ({
                  add_service_id: Number(inclusion.data.add_service_id),
                  add_service_price: Number(inclusion.data.add_service_price),
                })),
              total_price: 0, // Initialize total price
            };

           // Calculate total price
            packageData.total_price = 
              // Supplier prices
              packageData.suppliers.reduce((acc, supplier) => acc + (supplier.price || 0), 0) +
              // Additional service prices
              packageData.additional_services.reduce((acc, service) => acc + (service.add_service_price || 0), 0) +
              // Venue price
              Number(this.inclusions.find(inc => inc.type === 'venue' && inc.data)?.data?.venue_price || 0) +
              // Outfit package price
              Number(this.inclusions.find(inc => inc.type === 'outfit' && inc.data)?.data?.gown_package_price || 0);
                
              // Add this for debugging
              console.log('Price breakdown:', {
                suppliers: packageData.suppliers.reduce((acc, supplier) => acc + (supplier.price || 0), 0),
                additionalServices: packageData.additional_services.reduce((acc, service) => acc + (service.add_service_price || 0), 0),
                venue: Number(this.inclusions.find(inc => inc.type === 'venue' && inc.data)?.data?.venue_price || 0),
                outfit: Number(this.inclusions.find(inc => inc.type === 'outfit' && inc.data)?.data?.gown_package_price || 0),
                total: packageData.total_price
              });

              if (!packageData.package_name || !packageData.event_type_id) {
                  alert('Package name and event type are required.');
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
        event_type_id: '',
        venue_id: null,
        capacity: null,
        additional_capacity_charges: null,
        charge_unit: 1,
        description: '',
        suppliers: [],
        additional_services: [],
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
          alert('You are not logged in. Please log in to view packages.');
          return;
        }

        const response = await axios.get('http://127.0.0.1:5000/created-packages', {
          headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${token}`,
          },
          withCredentials: true,
        });

        this.packages = response.data.map((pkg, index) => {
          const inclusions = [
            ...(pkg.suppliers || []).map(supplier => ({
              type: 'supplier',
              serviceType: supplier.service_type,
              data: supplier
            })),
            ...(pkg.venue_id ? [{
              type: 'venue',
              data: { selectVenueId: pkg.venue_id, selectVenue_name: pkg.venue_name }
            }] : []),
            ...(pkg.outfit_packages || []).map(outfit => ({
              type: 'outfit',
              data: outfit
            })),
            ...(pkg.additional_services || []).map(service => ({
              type: 'service',
              data: service
            }))
          ];

          return {
            packageId: pkg.package_id,
            package_name: pkg.package_name,
            event_type_id: pkg.event_type_id,
            capacity: pkg.capacity,
            total_price: pkg.total_price,
            description: pkg.description,
            venue_name: pkg.venue_name,
            venue_price: pkg.venue_price,
            inclusions,
            dummyIndex: index + 1
          };
        });
      } catch (error) {
        console.error('Error fetching packages:', error.response?.data || error.message);
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

              // Ensure the response data is consistent with template expectations
              this.venues = response.data.map(venue => ({
                  venue_id: venue.venue_id,  // Matches v-for and filteredVenues
                  venue_name: venue.venue_name,
                  location: venue.location,
                  venue_price: venue.venue_price,  // Include any other fields needed
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
                venue_id: venue.venue_id,
                venue_name: venue.venue_name,
                venue_price: venue.venue_price,
              }));
              console.log('Venues fetched:', this.venues); // Add this line
              this.gownPackages = gownPackagesResponse.data.map(gp => ({
                ...gp,
                gown_package_id: gp.gown_package_id,
                gown_package_name: gp.gown_package_name,
                gown_package_price: gp.gown_package_price,
              }));
            } catch (error) {
              console.error('Error fetching data:', error.response?.data || error.message);
            }
        },

        async fetchEventTypes() {
          try {
              console.log('Fetching event types...');
              console.log('Using URL:', 'http://127.0.0.1:5000/event-types');
              const response = await axios.get('http://127.0.0.1:5000/event-types');
              console.log('Event types response:', response.data);
              this.eventTypes = response.data;
              console.log('Event types stored:', this.eventTypes);
          } catch (error) {
              console.error('Error fetching event types:', error);
              console.error('Error details:', error.response ? error.response.data : error.message);
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
      async fetchAdditionalServices() {
        try {
          const token = localStorage.getItem('access_token');
          if (!token) {
            alert('You are not logged in. Please log in to view additional services.');
            return;
          }

          const response = await axios.get('http://127.0.0.1:5000/created-services', {
            headers: {
              'Content-Type': 'application/json',
              'Authorization': `Bearer ${token}`,
            },
            withCredentials: true,
          });

          this.additionalServices = response.data.map((service, index) => ({
            add_service_id: service.add_service_id,
            add_service_name: service.add_service_name,
            add_service_description: service.add_service_description,
            add_service_price: service.add_service_price,
            dummyIndex: index + 1,
          }));
        } catch (error) {
          console.error('Error fetching additional services:', error.response?.data || error.message);
        }
      },


      async confirmEditPackage() {
          try {
            const token = localStorage.getItem('access_token');

            if (!this.selectedPackage || !this.selectedPackage.packageId) {
              alert("Package ID is missing or invalid.");
              return;
            }

            // Format inclusions data
            const formattedInclusions = this.selectedPackage.inclusions.map(inclusion => {
              const data = inclusion.data || {};
              return {
                type: inclusion.type,
                serviceType: inclusion.serviceType,
                id: inclusion.type === 'supplier' ? data.supplier_id :
                    inclusion.type === 'venue' ? data.selectVenueId :
                    inclusion.type === 'outfit' ? data.gown_package_id :
                    inclusion.type === 'service' ? data.add_service_id : null,
                price: data.price || 0
              };
            });

            const response = await axios.put(
              `http://127.0.0.1:5000/created-package/${this.selectedPackage.packageId}`,
              {
                package_name: this.selectedPackage.package_name,
                package_type: this.selectedPackage.package_type,
                capacity: this.selectedPackage.capacity,
                price: this.selectedPackage.price,
                description: this.selectedPackage.description,
                inclusions: formattedInclusions
              },
              {
                headers: {
                  Authorization: `Bearer ${token}`,
                },
              }
            );

            if (response.status === 200) {
              alert('Package updated successfully!');
              await this.fetchPackages(); // Refresh the packages list
              this.closeEditPackagesBtn();
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

    editPackageBtn(index) {
        const packageToEdit = this.paginatedPackages[index];
        
        // Initialize the selected package with basic info
        this.selectedPackage = {
            packageId: packageToEdit.packageId,
            package_name: packageToEdit.package_name,
            package_type: packageToEdit.package_type || '',
            capacity: packageToEdit.capacity,
            total_price: packageToEdit.total_price,
            description: packageToEdit.description,
            inclusions: [],
            selectedSuppliers: packageToEdit.suppliers || [],
            selectedVenue: packageToEdit.venue_id ? {
                selectVenueId: packageToEdit.venue_id,
                selectVenue_name: packageToEdit.venue_name,
                price: packageToEdit.venue_price
            } : null,
            selectedOutfitPackage: packageToEdit.outfit_packages?.[0] || null,
            selectedAdditionalServices: packageToEdit.additional_services || []
        };

        // Add suppliers to inclusions
        if (this.selectedPackage.selectedSuppliers.length > 0) {
            this.selectedPackage.selectedSuppliers.forEach(supplier => {
                this.selectedPackage.inclusions.push({
                    type: 'supplier',
                    serviceType: supplier.service_type || '',
                    data: supplier
                });
            });
        }

        // Add venue to inclusions if exists
        if (this.selectedPackage.selectedVenue) {
            this.selectedPackage.inclusions.push({
                type: 'venue',
                data: this.selectedPackage.selectedVenue
            });
        }

        // Add outfit package to inclusions if exists
        if (this.selectedPackage.selectedOutfitPackage) {
            this.selectedPackage.inclusions.push({
                type: 'outfit',
                data: this.selectedPackage.selectedOutfitPackage
            });
        }

        // Add additional services to inclusions
        if (this.selectedPackage.selectedAdditionalServices.length > 0) {
            this.selectedPackage.selectedAdditionalServices.forEach(service => {
                this.selectedPackage.inclusions.push({
                    type: 'service',
                    data: service
                });
            });
        }

        this.editPackagesForm = true;
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

    displayEventTypeBtn() {
      this.showAddEventTypeModal = true;
      this.newEventTypeName = '';  // Reset the input field
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
   filteredAdditionalServices() {
      const selectedServiceIds = this.selectedPackage.inclusions
          .filter(inclusion => inclusion.type === 'service' && inclusion.data)
          .map(inclusion => inclusion.data.add_service_id);
      return this.additionalServices.filter(service => !selectedServiceIds.includes(service.add_service_id));
  },

  dynamicTotalPrice() {
      return (
        // Supplier prices
        this.inclusions
          .filter(inc => inc.type === 'supplier' && inc.data)
          .reduce((acc, inc) => acc + (Number(inc.data.price) || 0), 0) +
        // Additional service prices
        this.inclusions
          .filter(inc => inc.type === 'service' && inc.data)
          .reduce((acc, inc) => acc + (Number(inc.data.add_service_price) || 0), 0) +
        // Venue price
        Number(this.inclusions.find(inc => inc.type === 'venue' && inc.data)?.data?.venue_price || 0) +
        // Outfit package price
        Number(this.inclusions.find(inc => inc.type === 'outfit' && inc.data)?.data?.gown_package_price || 0)
      );
    }

  
},

    mounted() {
      this.fetchPackages();
      console.log('Component mounted');
      this.fetchSuppliersAndPackageServices();
      console.log('Fetch completed');
      this.fetchAdditionalServices();
      this.fetchEventTypes();
  },
    watch: {
        showTable(newTable) {
            if (newTable === 'packages') {
                this.fetchPackages();
            } else if (newTable === 'vendors') {
                this.fetchVendors();
            }
        },
        packageData: {
          handler(newVal) {
            if (newVal.event_type_id === "add-new") {
              this.addNewEventType();
            }
          },
          deep: true,
        },
    },
};
    </script>

    <style scoped>
    </style>