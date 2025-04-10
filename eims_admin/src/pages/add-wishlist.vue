<template>
  <div class="h-full flex items-center justify-center">
    <form class="bg-gray-200 w-full h-full flex flex-col items-center overflow-y-auto mb-20">
      <div class="mt-20 flex flex-col items-center text-center space-y-2">
        <h1 class="text-5xl font-merriweatherBoldItalic font-semibold text-gray-800">On-Site Booking</h1>
      </div>
      
      <hr class="border-t border-gray-400 my-8 w-[60%] mx-auto" />
      <div class="bg-gray-100 min-h-[110vh] max-w-4xl w-full flex flex-col justify-start mb-10 rounded-lg shadow-xl px-4 sm:px-6 lg:px-8 overflow-y-auto">
        <!-- Phase 1: Personal Information -->
        <div v-if="personalInfoForm" class="m-5 items-center">
              <h1 class="mt-5 font-bold font-amaticBold text-lg text-blue-800">ⓘ Personal Information (For Onsite Bookings)</h1>
              <div class="ml-3 mt-6 space-y-3">
                <label for="onsiteFirstname" class="text-md font-semibold text-gray-700">First Name *</label>
                <p class="text-md text-gray-500">Enter the first name of the onsite contact person.</p>
                <input
                  type="text"
                  v-model="onsite_firstname"
                  class="w-full sm:w-9/12 h-12 rounded-lg font-medium shadow-md"
                  placeholder="Enter first name here"
                />
              </div>
              <div class="ml-3 mt-10 space-y-3">
                <label for="onsiteLastname" class="text-md font-semibold text-gray-700">Last Name *</label>
                <p class="text-md text-gray-500">Enter the last name of the onsite contact person.</p>
                <input
                  type="text"
                  v-model="onsite_lastname"
                  class="w-full sm:w-9/12 h-12 rounded-lg font-medium shadow-md"
                  placeholder="Enter last name here"
                />
              </div>
              <div class="ml-3 mt-10 space-y-3">
                <label for="onsiteContact" class="text-md font-semibold text-gray-700">Contact Number *</label>
                <p class="text-md text-gray-500">Provide a contact number for the onsite person.</p>
                <input
                  type="text"
                  v-model="onsite_contact"
                  class="w-full sm:w-9/12 h-12 rounded-lg font-medium shadow-md"
                  placeholder="Enter contact number here"
                />
              </div>
              <div class="ml-3 mt-10 space-y-3">
                <label for="onsiteAddress" class="text-md font-semibold text-gray-700">Address *</label>
                <p class="text-md text-gray-500">Provide the onsite address details.</p>
                <textarea
                  v-model="onsite_address"
                  class="w-full sm:w-9/12 h-24 rounded-lg font-medium shadow-md"
                  placeholder="Enter address here"
                ></textarea>
              </div>
              <div class="flex justify-center items-center space-x-4">
                <button class="mt-10 py-2 px-4 bg-gray-300 hover:bg-gray-400 font-semibold text-gray-900 rounded-lg shadow-lg transition-transform duration-300 transform hover:scale-105"
                 @click = "cancelOnsiteBooking"
                >
                 
                  Cancel
                </button>
                <button
                  type="button"
                  @click="nextPhase"
                  class="mt-10 py-2 px-4 bg-blue-300 hover:bg-blue-400 font-semibold text-gray-900 rounded-lg shadow-lg transition-transform duration-300 transform hover:scale-110"
                >
                  Next
                </button>
              </div>
            </div>


        <div v-if="wishlistDetailsForm" class="m-5 items-center justify-center">
          <h1 class="mt-5 font-bold font-amaticBold text-lg text-blue-800">ⓘ Event Details</h1>
          <div class="ml-3 mt-10 space-y-3">
            <label for="eventType" class="text-md font-semibold text-gray-700">Choose a type of event. *</label>
            <p class="text-md text-gray-500">Select the category that best describes your event.</p>

            <div v-if="eventTypesLoading" class="text-center">Loading event types...</div>
            <div v-else>
              <select v-model="event_type" class="w-full sm:w-9/12 h-12 rounded-lg font-medium shadow-md">
                <option disabled selected value="">Pick your event here</option>
                <option v-for="type in eventTypes" :key="type.event_type_id" :value="type.event_type_name">
                  {{ type.event_type_name }}
                </option>
              </select>
            </div>
          </div>
          <div class="ml-3 mt-10 space-y-3">
            <label for="eventInput" class="text-md font-semibold text-gray-700">Give your event a name. *</label>
            <p class="text-md text-gray-500">Provide a unique and descriptive name for your event.</p>
            <input type="text" v-model="event_name" class="w-full sm:w-9/12 h-12 rounded-lg font-medium shadow-md" placeholder="Enter event name here" required/>
          </div>
          <div class="ml-3 mt-10 space-y-3">
            <label for="eventTheme" class="text-md font-semibold text-gray-700">Theme of your event. *</label>
            <p class="text-md text-gray-500">Define a captivating theme that sets the mood for your event.</p>
            <input type="text" v-model="event_theme" class="w-full sm:w-9/12 h-12 rounded-lg font-medium shadow-md" placeholder="Enter theme here" required/>
          </div>

          <div class="ml-3 mt-10 space-y-3">
            <label for="eventColor" class="text-md font-semibold text-gray-700">Pick a color of your event. *</label>
            <p class="text-md text-gray-500">Select a vibrant color palette that embodies the spirit of your event.</p>

            <!-- Container for the text input and color picker -->
            <div class="flex relative justify-center items-center w-full">
              <!-- Native HTML color picker input -->
              <input 
                type="color" 
                v-model="event_color" 
                class="absolute left-28 top-2.5 w-6 h-6 opacity-0 cursor-pointer z-30"
                required
              /> 

              <!-- Custom circular button for color display inside the text input -->
              <div 
                :style="{ backgroundColor: event_color }" 
                class="absolute left-28 top-2.5 w-6 h-6 rounded-full border-none shadow-md cursor-pointer z-20"
              ></div>

              <!-- Regular text input field where user can also enter a color manually -->
              <input 
                type="text" 
                v-model="event_color" 
                class="w-full sm:w-9/12 h-12 rounded-lg font-medium shadow-md pl-12"
                placeholder="Enter the color(s) here" 
                required
              />
            </div>
          </div>

          <div class="flex justify-center items-center space-x-4">
            <button type = "button" @click = "backToPersonalInfo" class="mt-16 py-2 px-4 bg-gray-200 hover:bg-red-400 font-semibold text-gray-900 rounded-lg shadow-lg transition-transform duration-300 transform hover:scale-110">Back</button>
            <button type = "button" @click="displayPackages" class="mt-16 py-2 px-4 bg-blue-300 hover:bg-blue-400 font-semibold text-gray-900 rounded-lg shadow-lg transition-transform duration-300 transform hover:scale-110">Next</button>
          </div>
        </div>

        <div v-if="packagesForm" class="m-5 items-center">
           <div class = "flex justify-between items-center">
          <h1 class="mt-5 font-bold font-amaticBold text-lg text-blue-800">ⓘ Package Deals</h1>
           <button type = "button" @click="prevEventDetails" class="mt-5 py-1 px-5 bg-gray-200 hover:bg-red-400 font-semibold text-gray-900 rounded-lg shadow-lg transition-transform duration-300 transform hover:scale-110">
            Back</button>
        </div>
          <p class="text-md text-gray-500 mt-2">Choose from our variety of event packages and reserve your spot for an unforgettable celebration!</p>

 
      <!-- Packages Grid -->
    <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-6 mt-7">
      <div
        v-for="(pkg, index) in filteredPackages"
        :key="pkg.packageId"
        class="flex flex-col rounded-3xl h-[320px] w-[260px] cursor-pointer transition-all duration-300 ease-in-out hover:scale-105 hover:shadow-lg hover:bg-opacity-90"
        :style="{ backgroundColor: getRandomColor() }"
        @click="selectPackage(pkg)"
      >
        <div class="px-6 py-8 sm:p-10 sm:pb-6">
          <div class="grid items-center justify-center w-full grid-cols-1 text-left">
            <div>
              <h2 class="text-lg font-medium tracking-tighter text-gray-600 lg:text-2xl">
                {{ pkg.package_name }}
              </h2>
              <p class="mt-2 text-xs text-gray-500 font-raleway">
                {{ pkg.description }}
              
                
              </p>
            </div>

            <div class="mt-6">
              <p>
                <span class="text-4xl font-light tracking-tight text-black">
                  {{ formatPrice(pkg.total_price) }}
                </span>
                <span class="text-sm font-medium text-gray-500 ml-2">php only</span>
              </p>
            </div>

            <div class="mt-4">
              <p class="text-xs font-semibold text-gray-500">Venue: {{ pkg.venue_name }}</p>
              <p class="text-xs font-semibold text-gray-500">Capacity: {{ pkg.capacity }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

      <!-- Package Details Form -->
      <div v-if="packagesDetailsForm" class="m-5 items-center">
            <div class="flex justify-between items-center">
              <h1 class="mt-5 font-bold font-amaticBold text-lg text-blue-800">ⓘ Package Details</h1>
              <button type = "button" @click="prevPackageDeals" class="mt-5 py-1 px-5 bg-gray-200 hover:bg-red-400 font-semibold text-gray-900 rounded-lg shadow-lg transition-transform duration-300 transform hover:scale-110">
                Back
              </button>
            </div>

            <div v-if="selectedPackage" class="mt-5">
          <h2 class="text-xl font-bold mb-3">{{ selectedPackage.package_name }}</h2>
          <h2 class="text-xl font-bold mb-3">{{ formatPrice(calculatedTotalPrice) }} php</h2>

          <div class = "mb-4">
            <p class = "text-md font-medium font-poppins text-gray-500">(* Click the buttons to Add items to the list )</p>
          </div>

           <!-- Inclusion Buttons -->
           <div class="grid grid-cols-4 gap-4 mb-4">
            <button type = "button"
              @click.prevent="openInclusionModal('supplier')" 
              class="flex items-center justify-center bg-[#9B111E] text-white px-3 py-2 h-[50px] rounded-md hover:bg-[#B73A45]"
            >
              + Suppliers
            </button>
            <button type = "button"
              @click.prevent="openInclusionModal('venue')" 
              class="flex items-center justify-center bg-[#9B111E] text-white px-3 py-2 h-[50px] rounded-md hover:bg-[#B73A45]"
            >
             
             + Venues
            </button>
            <button type = "button"
              @click.prevent="openInclusionModal('outfit')" 
              class="flex items-center justify-center bg-[#9B111E] text-white px-3 py-2 h-[50px] rounded-md hover:bg-[#B73A45]"
            >
              
             + Outfits
            </button>
            <button type = "button"
              @click.prevent="openInclusionModal('service')" 
              class="flex items-center justify-center bg-[#9B111E] text-white px-3 py-2 h-[50px] rounded-md hover:bg-[#B73A45]"
            >  
            
              + Inclusions
            </button>
          </div>



          
            <!-- Inclusion Modal for Selecting Supplier Type -->
            <div v-if="showInclusionModal && selectedInclusionType === 'supplier'" @click.self="closeInclusionModal" class="fixed inset-0 bg-black bg-opacity-50 flex justify-center items-center z-50">
              <div class="bg-white w-[500px] p-6 rounded-lg shadow-lg">
                <div class="flex justify-between items-center mb-4">
                  <h2 class="text-lg font-semibold">Select Supplier Type</h2>
                  <button type = "button" @click="closeInclusionModal" class="text-red-500 hover:text-red-700">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
                    </svg>
                  </button>
                </div>
                <div class="grid grid-cols-1 gap-2">
                  <button type = "button" v-for="serviceType in supplierTypes" :key="serviceType" @click="selectSupplierType(serviceType)" class="w-full text-left px-4 py-2 bg-gray-50 hover:bg-gray-100 rounded-md transition duration-150">
                    {{ serviceType }}
                  </button>
                  <button type="button" @click="showExternalSupplierModal = true" class="bg-blue-500 text-white px-4 py-2 rounded-md hover:bg-blue-600">Add External Supplier</button>
                </div>
              </div>
            </div>

            <!-- Inclusion Modal for Selecting Specific Supplier -->
            <div v-if="showSupplierModal" @click.self="closeSupplierModal" class="fixed inset-0 bg-black bg-opacity-50 flex justify-center items-center z-50">
              <div class="bg-white w-[500px] p-6 rounded-lg shadow-lg">
                <div class="flex justify-between items-center mb-4">
                  <h2 class="text-lg font-semibold">Select Supplier</h2>
                  <button type = "button" @click="closeSupplierModal" class="text-red-500 hover:text-red-700">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
                    </svg>
                  </button>
                </div>
                <div>
                  <label for="supplier" class="block text-sm font-medium text-gray-700">Select Supplier</label>
                  <select v-model="selectedSupplier" class="w-full p-2 rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500">
                    <option selected disabled value="">Select {{ selectedSupplierType }}</option>
                    <option v-for="supplier in filteredSuppliers(selectedSupplierType)" :key="supplier.supplier_id" :value="supplier">
                      {{ supplier.firstname }} {{ supplier.lastname }} - {{ formatPrice(supplier.price) }} php
                    </option>
                  </select>
                </div>
                <div class="flex justify-center mt-4">
                  <button type="button" @click="addSelectedSupplier" class="bg-blue-500 text-white px-4 py-2 rounded-md hover:bg-blue-600">Add</button>
                </div>
              </div>
            </div>

            <!-- External Supplier Modal -->
            <div v-if="showExternalSupplierModal" @click.self="closeExternalSupplierModal" class="fixed inset-0 bg-black bg-opacity-50 flex justify-center items-center z-50">
                <div class="bg-white w-[500px] p-6 rounded-lg shadow-lg">
                    <div class="flex justify-between items-center mb-4">
                        <h2 class="text-lg font-semibold">Add External Supplier</h2>
                        <button type = "button" @click="closeExternalSupplierModal" class="text-red-500 hover:text-red-700">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
                            </svg>
                        </button>
                    </div>
                    <div class="space-y-4">
                        <div>
                            <label class="block text-sm font-medium text-gray-700">Service Type</label>
                            <select v-model="selectedExternalSupplierType" class="w-full p-2 rounded-md border-gray-300 shadow-sm focus:ring focus:ring-blue-200">
                                <option value="">Select Service Type</option>
                                <option v-for="type in supplierTypes" :key="type" :value="type">{{ type }}</option>
                            </select>
                        </div>
                        <div>
                            <label class="block text-sm font-medium text-gray-700">Supplier Name</label>
                            <input type="text" v-model="externalSupplierData.name" class="w-full p-2 rounded-md border-gray-300 shadow-sm focus:ring focus:ring-blue-200" placeholder="Enter supplier name">
                        </div>
                        <div>
                            <label class="block text-sm font-medium text-gray-700">Contact</label>
                            <input type="text" v-model="externalSupplierData.contact" class="w-full p-2 rounded-md border-gray-300 shadow-sm focus:ring focus:ring-blue-200" placeholder="Enter contact details">
                        </div>
                        <div>
                            <label class="block text-sm font-medium text-gray-700">Price</label>
                            <input type="number" v-model="externalSupplierData.price" class="w-full p-2 rounded-md border-gray-300 shadow-sm focus:ring focus:ring-blue-200" placeholder="Enter price">
                        </div>
                        <div>
                            <label class="block text-sm font-medium text-gray-700">Remarks</label>
                            <textarea v-model="externalSupplierData.remarks" class="w-full p-2 rounded-md border-gray-300 shadow-sm focus:ring focus:ring-blue-200" rows="3" placeholder="Enter remarks"></textarea>
                        </div>
                    </div>
                    <div class="flex justify-end mt-4 space-x-2">
                        <button type = "button" @click="closeExternalSupplierModal" class="px-4 py-2 text-gray-600 hover:text-gray-800">Cancel</button>
                        <button type = "button" @click="addExternalSupplier" class="bg-blue-500 text-white px-4 py-2 rounded-md hover:bg-blue-600">Add External Supplier</button>
                    </div>
                </div>
            </div>

            <!-- Inclusion Modal for Selecting Venue -->
            <div v-if="showVenueModal" @click.self="closeVenueModal" class="fixed inset-0 bg-black bg-opacity-50 flex justify-center items-center z-50">
              <div class="bg-white w-[500px] p-6 rounded-lg shadow-lg">
                <div class="flex justify-between items-center mb-4">
                  <h2 class="text-lg font-semibold">Select Venue</h2>
                  <button type = "button" @click="closeVenueModal" class="text-red-500 hover:text-red-700">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
                    </svg>
                  </button>
                </div>
                <div>
                  <label for="venue" class="block text-sm font-medium text-gray-700">Select Venue</label>
                  <select v-model="selectedVenue" class="w-full p-2 rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500">
                    <option selected disabled value="">Select Venue</option>
                    <option v-for="venue in venues" :key="venue.venue_id" :value="venue">
                      {{ venue.venue_name }} ({{ venue.location }}) - {{ formatPrice(venue.venue_price) }} php
                    </option>
                  </select>
                </div>
                <div class="flex justify-center mt-4">
                  <button type="button" @click="addSelectedVenue" class="bg-blue-500 text-white px-4 py-2 rounded-md hover:bg-blue-600">Add</button>
                </div>
              </div>
            </div>

            <!-- Inclusion Modal for Selecting Outfit Package -->
            <div v-if="showOutfitModal" @click.self="closeOutfitModal" class="fixed inset-0 bg-black bg-opacity-50 flex justify-center items-center z-50">
              <div class="bg-white w-[500px] p-6 rounded-lg shadow-lg">
                <div class="flex justify-between items-center mb-4">
                  <h2 class="text-lg font-semibold">Select Outfit Package</h2>
                  <button type = "button" @click="closeOutfitModal" class="text-red-500 hover:text-red-700">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
                    </svg>
                  </button>
                </div>
                <div>
                  <label for="outfit" class="block text-sm font-medium text-gray-700">Select Outfit Package</label>
                  <select v-model="selectedOutfit" class="w-full p-2 rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500">
                    <option selected disabled value="">Select Outfit Package</option>
                    <option v-for="gownPackage in gownPackages" :key="gownPackage.gown_package_id" :value="gownPackage">
                      {{ gownPackage.gown_package_name }} - {{ formatPrice(gownPackage.gown_package_price) }} php
                    </option>
                  </select>
                </div>
                <div class="flex justify-center mt-4">
                  <button type="button" @click="addSelectedOutfit" class="bg-blue-500 text-white px-4 py-2 rounded-md hover:bg-blue-600">Add</button>
                </div>
              </div>
            </div>

            <!-- Inclusion Modal for Selecting Outfit Package or Individual -->
          <div v-if="showOutfitModal" @click.self="closeOutfitModal" class="fixed inset-0 bg-black bg-opacity-50 flex justify-center items-center z-50">
            <div class="bg-white w-[500px] p-6 rounded-lg shadow-lg">
              <div class="flex justify-between items-center mb-4">
                <h2 class="text-lg font-semibold">Select Outfit</h2>
                <button @click="closeOutfitModal" class="text-red-500 hover:text-red-700">
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
                  </svg>
                </button>
              </div>

              <!-- Toggle between package and individual -->
              <div class="mb-4">
                <div class="flex space-x-4">
                  <div 
                    @click.prevent="outfitSelectionMode = 'package'"
                    :class="['px-4 py-2 rounded-md cursor-pointer', outfitSelectionMode === 'package' ? 'bg-blue-500 text-white' : 'bg-gray-200']"
                  >
                    Outfit Package
                  </div>
                  <div 
                    @click.prevent="outfitSelectionMode = 'individual'"
                    :class="['px-4 py-2 rounded-md cursor-pointer', outfitSelectionMode === 'individual' ? 'bg-blue-500 text-white' : 'bg-gray-200']"
                  >
                    Individual Outfit
                  </div>
                </div>
              </div>

              <!-- Package Selection -->
              <div v-if="outfitSelectionMode === 'package'">
                <label class="block text-sm font-medium text-gray-700">Select Outfit Package</label>
                <select v-model="selectedOutfit" class="w-full p-2 rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500">
                  <option selected disabled value="">Select Outfit Package</option>
                  <option v-for="gownPackage in gownPackages" :key="gownPackage.gown_package_id" :value="gownPackage">
                    {{ gownPackage.gown_package_name }} - {{ formatPrice(gownPackage.gown_package_price) }}
                  </option>
                </select>
              </div>

              <!-- Individual Outfit Selection -->
              <div v-if="outfitSelectionMode === 'individual'">
                <label class="block text-sm font-medium text-gray-700">Select Individual Outfit</label>
                <select v-model="selectedOutfit" class="w-full p-2 rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500">
                  <option selected disabled value="">Select Individual Outfit</option>
                  <option v-for="outfit in outfits" :key="outfit.outfit_id" :value="outfit">
                    {{ outfit.outfit_name }} - {{ outfit.outfit_type }} (Size: {{ outfit.size }}) - {{ formatPrice(outfit.rent_price) }}
                  </option>
                </select>
              </div>

              <div class="flex justify-center mt-4">
                <button 
                  type="button" 
                  @click="outfitSelectionMode === 'package' ? addSelectedOutfitPackage() : addSelectedOutfit()" 
                  class="bg-blue-500 text-white px-4 py-2 rounded-md hover:bg-blue-600"
                >
                  Add
                </button>
              </div>
            </div>
          </div>

            <!-- Inclusion Modal for Selecting Additional Services -->
              <div v-if="showServiceModal" @click.self="closeServiceModal" class="fixed inset-0 bg-black bg-opacity-50 flex justify-center items-center z-50">
                <div class="bg-white w-[500px] p-6 rounded-lg shadow-lg">
                  <div class="flex justify-between items-center mb-4">
                    <h2 class="text-lg font-semibold">Select Additional Service</h2>
                    <button type = "button" @click="closeServiceModal" class="text-red-500 hover:text-red-700">
                      <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
                      </svg>
                    </button>
                  </div>
                  <div>
                    <label for="service" class="block text-sm font-medium text-gray-700">Select Additional Service</label>
                    <select v-model="selectedService" class="w-full p-2 rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500">
                      <option selected disabled value="">Select Additional Service</option>
                      <option v-for="service in filteredAdditionalServices" :key="service.add_service_id" :value="service">
                        {{ service.add_service_name }} - {{ formatPrice(service.add_service_price) }} php
                      </option>
                    </select>
                  </div>
                  <div class="flex justify-center mt-4">
                    <button type="button" @click="addSelectedService" class="bg-blue-500 text-white px-4 py-2 rounded-md hover:bg-blue-600">Add</button>
                  </div>
                </div>
              </div>

             <!-- Inclusions Table -->
              <div v-if="packagesDetailsForm" class="mt-6">
                <h3 class="text-lg font-semibold mb-4">Package Inclusions</h3>
                <div class="overflow-x-auto bg-white rounded-lg shadow">
                  <table class="min-w-full divide-y divide-gray-200">
                    <thead class="bg-gray-50">
                      <tr>
                        <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                          Type
                        </th>
                        <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                          Details
                        </th>
                        <th scope="col" class="px-6 py-3 text-center text-xs font-medium text-gray-500 uppercase tracking-wider">
                          Price
                        </th>
                        <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                          Actions
                        </th>
                      </tr>
                    </thead>
                    <tbody class="bg-white divide-y divide-gray-200">
                      <tr v-for="(inclusion, index) in inclusions" :key="index">
                        <td class="px-6 text-sm py-4 whitespace-nowrap text-start">
                          <span class="capitalize">{{ inclusion.type }}</span>
                          <span v-if="inclusion.type === 'supplier'" class="text-xs text-gray-500">
                            ({{ inclusion.serviceType }})
                          </span>
                        </td>
                        <td class="px-6 text-sm py-4 whitespace-nowrap text-start">
                          {{ getInclusionName(inclusion) }}
                        </td>
                        <td class="px-6 text-sm py-4 whitespace-nowrap">
                          {{ getInclusionPrice(inclusion) }}
                        </td>
                        <td class="px-6 text-sm py-4 whitespace-nowrap">
                          <div class="flex items-center space-x-2">
                            <button type = "button" @click="editInclusion(index)" class="inline-block cursor-pointer">
                              <img 
                                alt="Edit Icon" 
                                class="w-[20px] h-[20px] transition-transform transform hover:scale-110 hover:brightness-90" 
                                src="/img/edit.png" 
                              >
                            </button>
                            <button type = "button" @click="removeInclusion(index)" class="inline-block cursor-pointer">
                              <img 
                                alt="Delete Icon" 
                                class="w-[20px] h-[20px] transition-transform transform hover:scale-110 hover:brightness-90" 
                                src="/img/delete.png" 
                              >
                            </button>
                          </div>
                        </td>
                      </tr>
                      <tr v-if="inclusions.length === 0">
                        <td colspan="4" class="px-6 py-4 text-center text-gray-500">
                          No inclusions added yet
                        </td>
                      </tr>
                    </tbody>
                    <tfoot v-if="inclusions.length > 0" class="bg-gray-50">
                      <tr>
                        <td colspan="2" class="px-6 py-4 text-right font-medium">
                          Total Price:
                        </td>
                        <td colspan="2" class="px-6 py-4 font-bold">
                          {{ formatPrice(calculatedTotalPrice) }} php
                        </td>
                      </tr>
                    </tfoot>
                  </table>
                </div>
              </div>



              <div class="mb-5 mt-5">
              <h3 class="text-lg font-semibold mb-2">Capacity Pax</h3>
              <p class="w-full p-2 border rounded bg-gray-100">
                  Package Pax: 
                  <span class="font-semibold">
                      {{ selectedPackage.capacity + (selectedPackage.additional_capacity || 0) }} persons
                  </span>
                  <br>
                  Additional Charges: {{ formatPrice(selectedPackage.additional_capacity_charges) }} per {{ selectedPackage.charge_unit }} person(s)
              </p>
              <button type = "button"
                  @click="showCapacityModal = true"
                  class="mt-2 bg-[#9B111E] hover:bg-[#B73A45] text-white py-2 px-4 rounded-lg shadow-lg transition-transform duration-300 transform hover:scale-105"
              >
                 + Capacity
              </button>
          </div>
              <!-- Capacity Modal -->
              <div v-if="showCapacityModal" @click.self="showCapacityModal = false" class="fixed inset-0 bg-gray-600 bg-opacity-50 overflow-y-auto h-full w-full flex items-center justify-center">
                  <div class="relative text-left bg-white rounded-lg shadow-xl p-6 max-w-md w-full">
                      <div class="flex justify-between items-center mb-4">
                          <h3 class="text-lg font-semibold">Add Additional Pax</h3>
                          <button type = "button" @click="showCapacityModal = false" class="text-gray-500 hover:text-gray-700">
                              <span class="text-2xl">&times;</span>
                          </button>
                      </div>

                      <div class="space-y-4">
                          <div>
                              <label class="block text-sm font-medium text-gray-700">Current Package Pax</label>
                              <p class="text-sm">{{ selectedPackage.capacity }} persons</p>
                          </div>

                          <div>
                              <label class="block text-sm font-medium text-gray-700">Additional Charge per {{ selectedPackage.charge_unit }} pax</label>
                              <p class="text-sm">{{ formatPrice(selectedPackage.additional_capacity_charges) }} php</p>
                          </div>

                          <div>
                              <label class="block text-sm font-medium text-gray-700">Additional Pax</label>
                              <input 
                                  type="number" 
                                  v-model.number="additionalCapacity" 
                                  class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500"
                                  min="0"
                              >
                          </div>

                          <div v-if="additionalCapacity > 0" class="bg-blue-50 p-3 rounded">
                              <p class="text-sm">
                                  Additional charges: {{ formatPrice(calculateAdditionalCharges()) }}
                              </p>
                              <p class="text-xs text-gray-600 mt-1">
                                  ({{ additionalCapacity }} persons × {{ formatPrice(selectedPackage.additional_capacity_charges) }}/{{ selectedPackage.charge_unit }} person(s))
                              </p>
                          </div>
                      </div>

                      <div class="mt-6 flex justify-end space-x-3">
                          <button 
                              @click="showCapacityModal = false" 
                              class="px-4 py-2 border rounded-md text-gray-600 hover:bg-gray-50"
                          >
                              Cancel
                          </button>
                          <button type = "button"
                              @click="addCapacity" 
                              class="px-4 py-2 bg-blue-500 text-white rounded-md hover:bg-blue-600"
                              :disabled="!additionalCapacity"
                          >
                              Save
                          </button>
                      </div>
                  </div>
              </div>

              
            <!-- Edit Inclusion Modal -->
            <div v-if="showEditInclusionModal" class="fixed inset-0 bg-black bg-opacity-50 flex justify-center items-center z-50">
                <div class="bg-white w-[500px] p-6 rounded-lg shadow-lg">
                    <div class="flex justify-between items-center mb-4">
                        <h2 class="text-lg font-semibold">Edit {{ editingInclusion?.type }}</h2>
                        <button type = "button" @click="closeEditInclusionModal" class="text-red-500 hover:text-red-700">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
                            </svg>
                        </button>
                    </div>

                    <!-- Edit Form Content -->
                    <div class="space-y-4">
                        <!-- For Supplier -->
                        <div v-if="editingInclusion?.type === 'supplier'" class="space-y-3">
                            <!-- Internal supplier fields -->
                            <div v-if="editingInclusion.data.type !== 'external'">
                                <div>
                                    <label class="block text-sm font-medium text-gray-700">Service Type</label>
                                    <p class="text-xs text-gray-500">Debug: Current serviceType: {{ editingInclusion.serviceType }}</p>
                                    <select 
                                        v-model="editingInclusion.serviceType" 
                                        class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500"
                                        @change="fetchAvailableSuppliers"
                                    >
                                        <option value="">Select a service type</option>
                                        <option 
                                            v-for="type in supplierTypes" 
                                            :key="type" 
                                            :value="type"
                                        >
                                            {{ type }}
                                        </option>
                                    </select>
                                </div>
                                <div>
  
                                    <select 
                                        v-model="editingInclusion.data.supplier_id" 
                                        class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500"
                                    >
                                        <option value="">Select a supplier</option>
                                        <option 
                                            v-for="supplier in filteredSuppliers(editingInclusion.serviceType || '')" 
                                            :key="supplier.supplier_id" 
                                            :value="supplier.supplier_id"
                                        >
                                            {{ supplier.supplier_name }} - {{ formatPrice(supplier.price)}} php
                                        </option>
                                    </select>
                                </div>
                            </div>

                            <!-- External supplier fields -->
                            <div v-else>
                                <div>
                                    <label class="block text-sm font-medium text-gray-700">Service Type</label>
                                    <select v-model="editingInclusion.serviceType" class="w-full p-2 rounded-md border-gray-300 shadow-sm focus:ring focus:ring-blue-200">
                                        <option value="">Select Service Type</option>
                                        <option v-for="type in supplierTypes" :key="type" :value="type">{{ type }}</option>
                                    </select>
                                </div>
                                <div>
                                    <label class="block text-sm font-medium text-gray-700">Supplier Name</label>
                                    <input type="text" v-model="editingInclusion.data.external_supplier_name" class="w-full p-2 rounded-md border-gray-300 shadow-sm focus:ring focus:ring-blue-200" placeholder="Enter supplier name">
                                </div>
                                <div>
                                    <label class="block text-sm font-medium text-gray-700">Contact</label>
                                    <input type="text" v-model="editingInclusion.data.external_supplier_contact" class="w-full p-2 rounded-md border-gray-300 shadow-sm focus:ring focus:ring-blue-200" placeholder="Enter contact details">
                                </div>
                                <div>
                                    <label class="block text-sm font-medium text-gray-700">Price</label>
                                    <input type="number" v-model="editingInclusion.data.external_supplier_price" class="w-full p-2 rounded-md border-gray-300 shadow-sm focus:ring focus:ring-blue-200" placeholder="Enter price">
                                </div>
                                <div>
                                    <label class="block text-sm font-medium text-gray-700">Remarks</label>
                                    <textarea v-model="editingInclusion.data.remarks" class="w-full p-2 rounded-md border-gray-300 shadow-sm focus:ring focus:ring-blue-200" rows="3" placeholder="Enter remarks"></textarea>
                                </div>
                            </div>
                        </div>
                        <!-- For Venue -->
                        <div v-if="editingInclusion?.type === 'venue'" class="space-y-3">
                            <div>
                                <label class="block text-sm font-medium text-gray-700">Venue</label>
                                <select v-model="editingInclusion.data.venue_id" class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500">
                                    <option value="">Select a venue</option>
                                    <option v-for="venue in availableVenues" :key="venue.venue_id" :value="venue.venue_id">
                                        {{ venue.venue_name || venue.name }} - {{ formatPrice(venue.venue_price) }} php
                                    </option>
                                </select>
                            </div>
                        </div>

                        <!-- For Outfit -->
                        <div v-if="editingInclusion?.type === 'outfit'" class="space-y-3">
                            <div>
                                <label class="block text-sm font-medium text-gray-700">Outfit Package</label>
                                <select v-model="editingInclusion.data.outfit_id" class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500">
                                    <option value="">Select an outfit package</option>
                                    <template v-if="availableGownPackages && availableGownPackages.length > 0">
                                        <option v-for="outfit in availableGownPackages" 
                                                :key="outfit.gown_package_id" 
                                                :value="outfit.gown_package_id">
                                            {{ outfit.gown_package_name }} - {{ outfit.gown_package_price }} php
                                        </option>
                                    </template>
                                </select>
                            </div>
                        </div>

                    

                        <!-- For Additional Service -->
                        <div v-if="editingInclusion?.type === 'service'" class="space-y-3">
                            <div>
                                <label class="block text-sm font-medium text-gray-700">Additional Service</label>
                                <select v-model="editingInclusion.data.service_id" class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500">
                                    <option value="">Select a service</option>
                                    <option v-for="service in additionalServices" :key="service.service_id" :value="service.service_id">
                                        {{ service.service_name }}
                                    </option>
                                </select>
                            </div>
                        </div>

                        <div class="flex justify-end space-x-3 mt-6">
                            <button type = "button" @click="closeEditInclusionModal" class="px-4 py-2 bg-gray-200 text-gray-800 rounded-md hover:bg-gray-300">
                                Cancel
                            </button>
                            <button type = "button" @click="saveEditedInclusion" class="px-4 py-2 bg-blue-500 text-white rounded-md hover:bg-blue-600">
                                Save Changes
                            </button>
                        </div>
                    </div>
                </div>
            </div>


            <!-- Event Schedule Section -->
            <div class="mb-5">
                <h3 class="text-lg font-semibold mb-2">Event Schedule</h3>
                <div class="grid grid-cols-3 gap-4">
                    <div>
                        <label class="text-xs text-gray-600 mb-1 block">Date</label>
                        <input 
                            v-model="eventSchedule.date" 
                            type="date" 
                            class="w-full p-2 border rounded"
                            @change="checkScheduleAvailability"
                            :disabled="isDateBooked"
                        >
                    </div>
                    <div>
                        <label class="text-xs text-gray-600 mb-1 block">Start Time</label>
                        <input 
                            v-model="eventSchedule.start_time" 
                            type="time" 
                            class="w-full p-2 border rounded"
                            :disabled="!eventSchedule.date || isDateBooked"
                        >
                    </div>
                    <div>
                        <label class="text-xs text-gray-600 mb-1 block">End Time</label>
                        <input 
                            v-model="eventSchedule.end_time" 
                            type="time" 
                            class="w-full p-2 border rounded"
                            :disabled="!eventSchedule.start_time || isDateBooked"
                        >
                    </div>
                </div>
                <p v-if="scheduleError" class="text-red-500 text-sm mt-2">{{ scheduleError }}</p>
            </div>

            <div class = "flex justify-center mb-5">
                <button type = "button" @click="submitWishlist" class="mt-5 py-2 px-4 bg-blue-500 hover:bg-blue-600 text-white font-semibold rounded-lg shadow-lg transition-transform duration-300 transform hover:scale-105">
                  Save Wishlist
                </button>
            </div>
          
 
            </div>
          </div>

      </div>
    </form>

    <div v-if="showAlert" class="fixed inset-x-0 top-1/3 mx-auto max-w-md bg-green-100 border border-green-400 text-green-700 px-4 py-5 rounded shadow-lg transform transition-all duration-500 ease-in-out" role="alert">
    <div class="flex items-center">
      <div class = "text-3xl font-bold ml-1 rounded-full bg-gray-200 px-2">
        &check;
      </div>
      <div>
        <div class = "flex flex-col ml-5">
        <strong class="font-bold">Success!</strong>
        <span class="block sm:inline">Event successfully added to your wishlist!</span>
      </div>
      </div>
    </div>
  </div>



  </div>
</template>

<script>
import axios from 'axios';
import { resolveTransitionHooks } from 'vue';


// Ensure Axios is configured to send credentials with requests globally
axios.defaults.withCredentials = true;

export default {
  name: 'AddWishlist',
  data() {
    return {
      event_name: '',
      event_type: '',
      event_theme: '',
      event_color: "#000000",
      venue: '',
      showCapacityModal: false, // To control modal visibility
      additionalCapacity: 0,
      isUserLoggedIn: false,
      showAlert: false,
      wishlistDetailsForm: false,
      packagesForm: false,
      packagesDetailsForm: false,
      prevEventDetailsForm: false,
      eventTypes: [],
      packages: [],
      filteredPackages: [],
      selectedPackage: null,

      eventTypesLoading: true,
      availableSuppliers: [], 
      availableVenues: [], 
      availableGownPackages: [],
      eventSchedule: {
        date: '',
        start_time: '',
        end_time: ''
      },
      isSubmitting: false,
      showInclusionModal: false,
      showSupplierModal: false,
      showVenueModal: false,
      showOutfitModal: false,
      showServiceModal: false,
      selectedInclusionType: '',
      selectedSupplierType: '',
      selectedSupplier: null,
      selectedVenue: null,
      selectedOutfit: null,
      selectedService: null,
      selectedAdditionalService: null,
      additionalServiceSearchQuery: '',
      inclusions: [],
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
      venues: [],
      gownPackages: [],
      additionalServices: [],
      showEditInclusionModal: false,
      editingInclusion: null,
      editingInclusionIndex: -1,
      showExternalSupplierModal: false,
      externalSupplierData: {
            name: '',
            contact: '',
            price: 0,
            remarks: ''
        },
        selectedExternalSupplierType: '',
        bookedDates: [],
        isDateBooked: false,
        scheduleError: '',

        personalInfoForm: true,
        onsite_firstname: '',
        onsite_lastname: '',
        onsite_contact: '',
        onsite_address: '',

        outfitSelectionMode: 'package', // 'package' or 'individual'
        outfits: [],
        selectedOutfit: null,
        showOutfitModal: false,
    };
  },
  methods: {
    async fetchBookedDates() {
        try {
            const token = localStorage.getItem('access_token');
            if (!token) {
                console.error('No access token found');
                return;
            }
            
            console.log('Fetching booked dates...');
            const response = await axios.get('http://localhost:5000/events/schedules', {
                headers: { 'Authorization': `Bearer ${token}` }
            });
            
            if (response.data && Array.isArray(response.data)) {
                this.bookedDates = response.data.filter(booking => 
                    booking.schedule && booking.start_time && booking.end_time
                );
                console.log('Successfully fetched booked dates:', this.bookedDates);
            } else {
                console.error('Invalid response format:', response.data);
            }
        } catch (error) {
            console.error('Error fetching booked dates:', error);
            if (error.response) {
                console.error('Error details:', {
                    status: error.response.status,
                    data: error.response.data,
                    headers: error.response.headers
                });
            }
        }
    },
    async checkScheduleAvailability() {
        if (!this.eventSchedule.date || !this.eventSchedule.start_time || !this.eventSchedule.end_time) {
            console.log('Schedule not fully selected yet');
            return;
        }

        const formatTime = (time) => {
            // Convert time to HH:mm format for comparison
            return time.split(':').slice(0, 2).join(':');
        };

        const selectedDate = this.eventSchedule.date;
        const selectedStartTime = formatTime(this.eventSchedule.start_time);
        const selectedEndTime = formatTime(this.eventSchedule.end_time);

        console.log('Checking schedule availability for:', {
            date: selectedDate,
            start: selectedStartTime,
            end: selectedEndTime,
            bookedDates: this.bookedDates
        });

        // Check if any booked date overlaps with selected schedule
        this.isDateBooked = this.bookedDates.some(booking => {
            const bookingStartTime = formatTime(booking.start_time);
            const bookingEndTime = formatTime(booking.end_time);

            const overlap = (
                booking.schedule === selectedDate &&
                ((selectedStartTime >= bookingStartTime && selectedStartTime < bookingEndTime) ||
                 (selectedEndTime > bookingStartTime && selectedEndTime <= bookingEndTime) ||
                 (selectedStartTime <= bookingStartTime && selectedEndTime >= bookingEndTime))
            );
            
            if (overlap) {
                console.log('Found overlapping booking:', {
                    bookedDate: booking.schedule,
                    bookedStart: bookingStartTime,
                    bookedEnd: bookingEndTime
                });
            }
            
            return overlap;
        });

        if (this.isDateBooked) {
            this.scheduleError = 'This schedule overlaps with an existing booking';
            console.log('Schedule is not available');
        } else {
            this.scheduleError = '';
            console.log('Schedule is available');
        }
    },
    checkLoginStatus() {
      const token = localStorage.getItem('access_token');
      console.log('Token being sent:', token); // Ensure token is not undefined
      if (!token) {
        console.log('No token found');
        return;
      }

      axios.get('http://127.0.0.1:5000/check-auth', {
        headers: {
          'Authorization': `Bearer ${localStorage.getItem('access_token')}`
        }
      })
      .then(response => {
        console.log('Auth check successful:', response.data);
      })
      .catch(error => {
        console.error('Error checking auth status:', error.response.data);
      });
    },
    displayWishlistAlert() {
      this.showAlert = true;
      setTimeout(() => {
        this.showAlert = false;
      }, 3000); // Auto-hide after 3 seconds
    },
    prevEventDetails() {
      this.wishlistDetailsForm = false;
      this.prevEventDetailsForm = true;
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

          console.log('Raw response data:', response.data);

          // Process packages response
          this.packages = response.data.map((pkg) => {
            console.log('Processing package:', pkg);
            return {
              packageId: pkg.package_id,
              package_name: pkg.package_name,
              package_type: pkg.event_type_name, // Change this line to use event_type_name
              venue_id: pkg.venue_id,
              venue_name: pkg.venue_name,
              venue_location: pkg.venue_location,
              venue_price: pkg.venue_price,
              total_price: pkg.total_price,
              capacity: pkg.capacity,
              description: pkg.description,
              gown_package_id: pkg.gown_package_id,
              gown_package_name: pkg.gown_package_name,
              gown_package_price: pkg.gown_package_price,
              additional_capacity_charges: pkg.additional_capacity_charges,
              charge_unit: pkg.charge_unit,
              suppliers: pkg.suppliers ? pkg.suppliers.map(supplier => ({
                type: 'internal',
                supplier_id: supplier.supplier_id,
                name: supplier.name,
                service: supplier.service,
                price: supplier.price,
                remarks: supplier.remarks
              })) : [],
              selected: false,
              detailsVisible: false,
            };
          });

          console.log('Processed packages:', this.packages);
          this.filterPackages();
          this.loading = false;
        } catch (error) {
          console.error('Error fetching packages:', error);
        }
      },

      async selectPackage(pkg) {
          this.packagesForm = false;
          this.packagesDetailsForm = true;
          this.selectedPackage = { ...pkg };
          this.inclusions = []; // Reset inclusions when selecting a new package
          console.log('Initial package selection:', pkg);

          try {
            // Fetch package details first
            const details = await this.fetchPackageDetails(pkg.packageId);
            console.log('Raw package details:', details);

            if (details) {
              // Update the selected package with complete details
              this.selectedPackage = {
                ...this.selectedPackage,
                ...details,
                detailsFetched: true
              };

              // Add venue if it exists with complete data
              if (details.venue_name) {
                const venueData = {
                  venue_id: pkg.venue_id,
                  venue_name: details.venue_name,
                  location: details.venue_location,
                  venue_price: details.venue_price
                };
                console.log('Adding venue:', venueData);
                this.inclusions.push({
                  type: 'venue',
                  data: venueData
                });
              }

               // Add gown package if it exists with complete data
               if (details.gown_package_name) {
                const gownData = {
                  gown_package_id: pkg.gown_package_id,
                  gown_package_name: details.gown_package_name,
                  gown_package_price: parseFloat(details.gown_package_price)
                };
                console.log('Adding gown package:', gownData);
                this.inclusions.push({
                  type: 'outfit_package',
                  data: gownData
                });
              }

              // Add suppliers if they exist
              if (details.supplier_ids && Array.isArray(details.supplier_ids)) {
                details.supplier_ids.forEach((id, index) => {
                  if (id) { // Only add if supplier_id exists
                    const supplierData = {
                      supplier_id: id,
                      firstname: details.supplier_firstnames?.[index] || '',
                      lastname: details.supplier_lastnames?.[index] || '',
                      service: details.services?.[index] || '',
                      price: details.service_prices?.[index] || 0,
                      type: details.external_supplier_names?.[index] ? 'external' : 'internal',
                      external_supplier_name: details.external_supplier_names?.[index] || '',
                      external_supplier_contact: details.external_supplier_contacts?.[index] || '',
                      external_supplier_price: details.external_supplier_prices?.[index] || 0,
                      remarks: details.remarks?.[index] || ''
                    };
                    console.log('Adding supplier:', supplierData);
                    this.inclusions.push({
                      type: 'supplier',
                      serviceType: details.services?.[index] || '',
                      data: supplierData
                    });
                  }
                });
              }

              // Store capacity-related information
              this.selectedPackage.capacity = details.capacity || 0;
              this.selectedPackage.additional_capacity_charges = details.additional_capacity_charges || 0;
              this.selectedPackage.charge_unit = details.charge_unit || 1;
            }

            console.log('Final inclusions:', this.inclusions);
            console.log('Final selected package:', this.selectedPackage);

          } catch (error) {
            console.error('Error selecting package:', error);
          }
        },


        async fetchOutfits() {
            try {
              const token = localStorage.getItem('access_token');
              if (!token) return;

              const response = await axios.get('http://127.0.0.1:5000/outfits', {
                headers: { Authorization: `Bearer ${token}` }
              });

              this.outfits = response.data.map(outfit => ({
                outfit_id: outfit.outfit_id,
                outfit_name: outfit.outfit_name,
                outfit_type: outfit.outfit_type,
                outfit_color: outfit.outfit_color,
                outfit_desc: outfit.outfit_desc,
                rent_price: parseFloat(outfit.rent_price) || 0,
                status: outfit.status,
                size: outfit.size
              }));
            } catch (error) {
              if (error.response) {
                console.error('Error response:', error.response.data);
              }
            }
          },
      

    filterPackages() {
        console.log('Current event_type:', this.event_type);
        if (this.event_type && this.event_type !== '') {
          this.filteredPackages = this.packages.filter((pkg) => {
            console.log('Full package object:', pkg); // Add this to see each package
            console.log('Package type:', pkg.package_type); // Add this to see package type
            return pkg.package_type === this.event_type;
          });
        } else {
          this.filteredPackages = this.packages;
        }
        console.log('Filtered Packages:', this.filteredPackages);
      },

      async fetchPackageDetails(packageId) {
          try {
            const token = localStorage.getItem('access_token');
            const response = await axios.get(`http://127.0.0.1:5000/packages/${packageId}`, {
              headers: {
                'Authorization': `Bearer ${token}`,
                'Content-Type': 'application/json'
              }
            });
            console.log('Raw package details response:', response.data);
            return response.data;
          } catch (error) {
            console.error('Error fetching package details:', error);
            throw error;
          }
        },
    prevPackageDeals() {
      this.packagesDetailsForm = false;
      this.packagesForm = true;
    },
    addSupplier() {
      if (!this.selectedPackage.suppliers) {
        this.selectedPackage.suppliers = [];
      }
      this.selectedPackage.suppliers.push({
        type: 'external',
        external_supplier_name: '',
        external_supplier_contact: '',
        external_supplier_price: 0,
        remarks: '',
      });
    },

    async fetchAvailableSuppliers() {
        try {
            const token = localStorage.getItem('access_token');
            const response = await axios.get('http://127.0.0.1:5000/available-suppliers', {
                headers: {
                    'Authorization': `Bearer ${token}`,
                    'Content-Type': 'application/json'
                }
            });
            console.log('Raw supplier data:', response.data);
            this.availableSuppliers = response.data.map(supplier => ({
                ...supplier,
                supplier_name: supplier.supplier_name || `${supplier.firstname} ${supplier.lastname}`,
                service_type: supplier.service_type || supplier.supplier_type
            }));
            console.log('Stored suppliers:', this.availableSuppliers);
        } catch (error) {
            console.error('Error fetching available suppliers:', error);
        }
    },


        updateSelectedSupplier(supplier, type) {
          if (type === 'internal') {
            const selectedSupplier = this.availableSuppliers.find(
              (s) => s.supplier_id === supplier.supplier_id
            );
            if (selectedSupplier) {
              supplier.name = selectedSupplier.name;
              supplier.email = selectedSupplier.email;
              supplier.service = selectedSupplier.service;
              supplier.price = parseFloat(selectedSupplier.price || 0); // Ensure price is numeric
            }
          }
          // Total price will automatically recalculate because of the computed property
        },

        async fetchAvailableVenues() {
          try {
              const token = localStorage.getItem('access_token');
              const response = await axios.get('http://127.0.0.1:5000/available-venues', {
                  headers: {
                      'Authorization': `Bearer ${token}`,
                      'Content-Type': 'application/json'
                  }
              });
              console.log('Raw venue data:', response.data);
              // Set both venues and availableVenues
              this.venues = response.data;
              this.availableVenues = response.data;
              console.log('Processed venues:', this.venues);
          } catch (error) {
              console.error('Error fetching available venues:', error);
              this.venues = []; // Reset on error
              this.availableVenues = []; // Reset on error
          }
      },

    updateSelectedVenue() {
      const selectedVenue = this.availableVenues.find(venue => venue.venue_id === this.selectedPackage.venue_id);
      if (selectedVenue) {
        this.selectedPackage.venue_name = selectedVenue.venue_name;
        this.selectedPackage.venue_location = selectedVenue.location;
        this.selectedPackage.venue_price = selectedVenue.venue_price;
      }
    },
    async fetchAvailableGownPackages() {
      try {
          const token = localStorage.getItem('access_token');
          const response = await axios.get('http://127.0.0.1:5000/available-gown-packages', {
              headers: {
                  'Authorization': `Bearer ${token}`,
                  'Content-Type': 'application/json'
              }
          });
          console.log('Raw outfit data:', response.data);
          // Set both gownPackages and availableGownPackages
          this.gownPackages = response.data;
          this.availableGownPackages = response.data;
          console.log('Processed outfits:', this.gownPackages);
      } catch (error) {
          console.error('Error fetching available gown packages:', error);
          this.gownPackages = []; // Reset on error
          this.availableGownPackages = []; // Reset on error
      }
  },
    updateSelectedGownPackage() {
        const selectedGownPackage = this.availableGownPackages.find(
          (gown) => gown.gown_package_id === parseInt(this.selectedPackage.gown_package_id)
        );
        if (selectedGownPackage) {
          this.selectedPackage.gown_package_name = selectedGownPackage.gown_package_name;
          this.selectedPackage.gown_package_price = selectedGownPackage.gown_package_price;
        }
      },

      async fetchEventTypes() {
          this.eventTypesLoading = true;
          try {
            const response = await axios.get('http://127.0.0.1:5000/event-types', {
              headers: {
                Authorization: `Bearer ${localStorage.getItem('access_token')}`,
              },
            });
            this.eventTypes = response.data;
            console.log('Event Types:', this.eventTypes);
          } catch (error) {
            console.error('Error fetching event types:', error);
          } finally {
            this.eventTypesLoading = false;
          }
        },

        async fetchAdditionalServices() {
          try {
            const token = localStorage.getItem('access_token');
            const response = await axios.get('http://127.0.0.1:5000/additional-services', {
              headers: {
                'Authorization': `Bearer ${token}`,
                'Content-Type': 'application/json'
              }
            });
            this.additionalServices = response.data;
            console.log('Available additional services:', this.additionalServices);
          } catch (error) {
            console.error('Error fetching additional services:', error);
          }
        },

        addSelectedService() {
    if (this.selectedService) {
        // Check if service already exists
        const hasExistingService = this.inclusions.some(item => 
            item.type === 'service' && 
            item.data.service_id === this.selectedService.add_service_id
        );

        if (hasExistingService) {
            alert('This service is already added.');
            this.closeServiceModal();
            return;
        }

        const serviceData = {
            type: 'service',
            data: {
                add_service_id: this.selectedService.add_service_id,
                service_name: this.selectedService.add_service_name,
                price: parseFloat(this.selectedService.add_service_price || 0),
                service_description: this.selectedService.add_service_description,
                is_modified: true,
                remarks: ''
            }
        };
        
        this.inclusions = [...this.inclusions, serviceData];

        this.updateTotalPrice();
        this.selectedService = null;
        this.showServiceModal = false;
    }
},

      selectService(service) {
          this.selectedService = service;
      },
      async submitWishlist() {
    try {
        // Get authentication token
        const token = localStorage.getItem('access_token');
        if (!token) {
            alert('You are not logged in. Please log in to add to the wishlist.');
            return;
        }

        // Validate required fields
        if (!this.selectedPackage) {
            alert('Please select a package');
            return;
        }

        if (!this.eventSchedule.date || !this.eventSchedule.start_time || !this.eventSchedule.end_time) {
            alert('Please fill in all event schedule details');
            return;
        }

        // Validate onsite booking information
        if (!this.onsite_firstname || !this.onsite_lastname || !this.onsite_contact || !this.onsite_address) {
            alert('Please fill in all onsite booking information');
            return;
        }

        // Transform suppliers into the new format
        const suppliers = this.inclusions
            .filter(inclusion => inclusion.type === 'supplier')
            .map(inclusion => {
                if (inclusion.data.type === 'external') {
                    return {
                        supplier_id: null,
                        price: inclusion.data.external_supplier_price || 0,
                        remarks: `External: ${inclusion.data.external_supplier_name} (${inclusion.data.external_supplier_contact})`
                    };
                } else {
                    return {
                        supplier_id: inclusion.data.supplier_id,
                        price: inclusion.data.price,
                        remarks: inclusion.data.remarks || ''
                    };
                }
            });

        // Transform outfits into the new format
        const outfits = this.inclusions
            .filter(inclusion => inclusion.type === 'outfit_package' || inclusion.type === 'individual_outfit')
            .map(inclusion => {
                if (inclusion.type === 'outfit_package') {
                    return {
                        outfit_id: null,
                        gown_package_id: inclusion.data.gown_package_id,
                        price: parseFloat(inclusion.data.gown_package_price || 0),
                        remarks: inclusion.data.remarks || ''
                    };
                } else {
                    return {
                        outfit_id: inclusion.data.outfit_id,
                        gown_package_id: null,
                        price: parseFloat(inclusion.data.rent_price || 0),
                        remarks: inclusion.data.remarks || ''
                    };
                }
            });

        // Transform services into the new format
        const services = this.inclusions
            .filter(inclusion => inclusion.type === 'service')
            .map(inclusion => ({
                add_service_id: inclusion.data.add_service_id,
                price: inclusion.data.price || 0,
                remarks: inclusion.data.remarks || ''
            }));

        // Get venue data from inclusions
        const venueInclusion = this.inclusions.find(inclusion => inclusion.type === 'venue');
        const venueData = venueInclusion ? {
            venue_id: venueInclusion.data.venue_id,
            venue_price: parseFloat(venueInclusion.data.venue_price || 0),
            venue_status: 'Pending',  // Set initial status as Pending
            remarks: ''  // Add empty remarks field
        } : null;

        // First create the event
        const eventData = {
            event_name: this.event_name,
            event_type: this.event_type,
            event_theme: this.event_theme,
            event_color: this.event_color,
            schedule: this.eventSchedule.date,
            start_time: this.eventSchedule.start_time,
            end_time: this.eventSchedule.end_time,
            onsite_firstname: this.onsite_firstname,
            onsite_lastname: this.onsite_lastname,
            onsite_contact: this.onsite_contact,
            onsite_address: this.onsite_address,
            status: 'Wishlist',
            booking_type: 'Onsite'
        };

        // Create event first
        const eventResponse = await axios.post('http://127.0.0.1:5000/events', eventData, {
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${token}`
            },
            withCredentials: true
        });

        if (!eventResponse.data.success) {
            throw new Error(eventResponse.data.message || 'Failed to create event');
        }

        // Now create the wishlist package
        const wishlistData = {
            events_id: eventResponse.data.events_id,
            package_name: this.selectedPackage.package_name,
            capacity: this.selectedPackage.capacity,
            description: this.selectedPackage.description,
            venue_id: venueData ? venueData.venue_id : null,
            gown_package_id: this.selectedPackage.gown_package_id,
            additional_capacity_charges: this.selectedPackage.additional_capacity_charges,
            charge_unit: this.selectedPackage.charge_unit,
            total_price: this.calculatedTotalPrice,
            event_type_id: this.selectedPackage.event_type_id,
            suppliers: suppliers,
            outfits: outfits,
            services: services,
            venue: venueData  // Include venue data for wishlist_venues table
        };
            
        console.log('Submitting wishlist data:', wishlistData);

        // Make API call to save wishlist with authentication
        const response = await axios.post('http://127.0.0.1:5000/wishlist-packages', wishlistData, {
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${token}`
            },
            withCredentials: true
        });

        if (response.data.success) {
            alert('Wishlist submitted successfully!');
            this.$router.push('/manage-events');
        } else {
            // If wishlist creation fails, delete the event we just created
            await axios.delete(`http://127.0.0.1:5000/events/${eventResponse.data.events_id}`, {
                headers: {
                    'Authorization': `Bearer ${token}`
                },
                withCredentials: true
            });
            throw new Error(response.data.message || 'Failed to create wishlist');
        }
    } catch (error) {
        console.error('Error submitting wishlist:', error);
        alert('Failed to create wishlist: ' + (error.response?.data?.message || error.message));
    }
},
    addSupplier(type) {
      if (type === 'internal') {
        this.selectedPackage.suppliers.push({
          type: 'internal',
          supplier_id: '',
          name: '',
          service: '',
          price: null,
          remarks: ''
        });
      } else if (type === 'external') {
        this.selectedPackage.suppliers.push({
          type: 'external',
          supplier_id: '',
          external_supplier_name: '',
          external_supplier_contact: '',
          external_supplier_price: null,
          remarks: ''
        });
      }
    },

  removeSupplier(index) {
      this.selectedPackage.suppliers.splice(index, 1);
    },
    closeExternalSupplierModal() {
        this.showExternalSupplierModal = false;
        this.externalSupplierData = {
            name: '',
            contact: '',
            price: 0,
            remarks: ''
        };
        this.selectedExternalSupplierType = '';
    },

    addExternalSupplier() {
        if (!this.selectedExternalSupplierType || !this.externalSupplierData.name) {
            alert('Please fill in all required fields');
            return;
        }

        // Check if this supplier type already exists
        const hasSupplierType = this.inclusions.some(item => 
            item.type === 'supplier' && 
            item.serviceType === this.selectedExternalSupplierType
        );
        if (hasSupplierType) {
            alert(`A ${this.selectedExternalSupplierType} supplier is already added. Please edit or remove the existing supplier first.`);
            return;
        }

        const supplierData = {
            supplier_id: null, // External suppliers don't have an internal ID
            name: this.externalSupplierData.name,
            price: parseFloat(this.externalSupplierData.price),
            type: 'external',
            external_supplier_contact: this.externalSupplierData.contact,
            external_supplier_name: this.externalSupplierData.name,
            external_supplier_price: parseFloat(this.externalSupplierData.price),
            remarks: this.externalSupplierData.remarks
        };

        this.inclusions = [...this.inclusions, {
            type: 'supplier',
            serviceType: this.selectedExternalSupplierType,
            data: supplierData
        }];

        this.updateTotalPrice();
        this.closeExternalSupplierModal();
        this.closeSupplierModal();
    
    },

    cancelSubmitWishlist() {
      window.scrollTo(0, 0);
      this.$router.push('/');
    },
    displayPackages() {
      this.wishlistDetailsForm = false;
      this.packagesForm = true;
    },
    prevEventDetails() {
      this.packagesForm = false;
      this.wishlistDetailsForm = true;
    },
    getRandomColor() {
      const colors = [
        '#f7c5f7', // Light pink
        '#afe2f8', // Light blue
        '#f6f9a0', // Light yellow
        '#f7c5c5', // Light red
        '#e3f5d4', // Pale green
        '#fce6e2', // Pale peach
      ];
      return colors[Math.floor(Math.random() * colors.length)];
    },
    addCapacity() {
      if (this.additionalCapacity > 0) {
          this.selectedPackage.capacity += this.additionalCapacity;
          this.updateTotalPrice();
          this.showCapacityModal = false; // Hide the modal after updating
          this.additionalCapacity = 0; // Reset the input field
          alert('Capacity updated successfully!');
      } else {
          alert('Please enter a valid additional capacity.');
      }
    },
    openCapacityModal() {
    this.showCapacityModal = true; // Open the capacity modal
    },
    updateAdditionalCapacity(newCapacity) {
      const baseCapacity = this.selectedPackage.capacity || 0;
      this.additionalCapacity = Math.max(0, newCapacity - baseCapacity); // Calculate excess capacity
    },
    formatPrice(price) {
      if (price === null || price === undefined || isNaN(price)) {
        return 'N/A'; // Return a fallback if price is invalid
      }
      // Round the price to 2 decimal places and format with commas
      return parseFloat(price).toFixed(2).replace(/\d(?=(\d{3})+\.)/g, '$&,');
    },
    openInclusionModal(type) {
      this.selectedInclusionType = type;
      switch (type) {
        case 'supplier':
          this.showInclusionModal = true;
          break;
        case 'venue':
          this.showVenueModal = true;
          break;
        case 'outfit':
          this.showOutfitModal = true;
          break;
        case 'service':
          this.showServiceModal = true;
          break;
      }
    },
    closeInclusionModal() {
      this.showInclusionModal = false;
    },
    closeSupplierModal() {
      this.showSupplierModal = false;
    },
    closeVenueModal() {
      this.showVenueModal = false;
    },
    closeOutfitModal() {
      this.showOutfitModal = false;
    },
    closeServiceModal() {
      this.showServiceModal = false;
    },
    selectSupplierType(serviceType) {
      this.selectedSupplierType = serviceType;
      this.closeInclusionModal();
      this.showSupplierModal = true;
    },
    addSelectedSupplier() {
      if (this.selectedSupplier && this.selectedSupplierType) {
          // Remove any existing supplier of the same type
          this.inclusions = this.inclusions.filter(item => 
              !(item.type === 'supplier' && item.serviceType === this.selectedSupplierType)
          );

          const price = parseFloat(this.selectedSupplier.price || 0);
          const supplierData = {
              supplier_id: this.selectedSupplier.supplier_id,
              name: this.selectedSupplier.name || this.selectedSupplier.supplier_name,
              service_type: this.selectedSupplierType,
              price: price,
              type: this.selectedSupplier.type || 'internal'
          };
          
          this.inclusions.push({
              type: 'supplier',
              serviceType: this.selectedSupplierType,
              data: supplierData
          });
          
          this.updateTotalPrice();
          this.selectedSupplier = null;
          this.selectedSupplierType = null;
          this.closeSupplierModal();
      }
  },

  addSelectedVenue() {
    if (this.selectedVenue) {
        const hasVenue = this.inclusions.some(item => item.type === 'venue');
        if (hasVenue) {
            this.$toast.error('A venue is already added. Please edit or remove the existing venue first.');
            this.closeVenueModal();
            return;
        }

        console.log('Selected venue:', this.selectedVenue);
        const price = parseFloat(this.selectedVenue.venue_price || 0);
        const venueData = {
            venue_id: this.selectedVenue.venue_id,
            venue_name: this.selectedVenue.venue_name,
            location: this.selectedVenue.location,
            venue_price: price,
            venue_status: 'Pending'  // Add default status
        };
        console.log('Venue data to add:', venueData);
        this.inclusions = [...this.inclusions, {
            type: 'venue',
            data: venueData
        }];
        this.updateTotalPrice();
        this.selectedVenue = null;
        this.closeVenueModal();
    }
},


addSelectedOutfit() {
    if (!this.selectedOutfit) {
        console.error('No outfit selected');
        return;
    }

    console.log('Current inclusions:', this.inclusions);
    
    // Check if this specific outfit type already exists
    const hasExistingOutfit = this.inclusions.some(item => 
        item.type === 'individual_outfit' && 
        item.data.outfit_id === this.selectedOutfit.outfit_id
    );
    
    if (hasExistingOutfit) {
        alert('This outfit is already added.');
        this.closeOutfitModal();
        return;
    }

    // Create outfit data with proper name and price
    const outfitData = {
        outfit_id: this.selectedOutfit.outfit_id,
        outfit_name: this.selectedOutfit.outfit_name,
        outfit_type: this.selectedOutfit.outfit_type,
        rent_price: parseFloat(this.selectedOutfit.rent_price || 0),
        size: this.selectedOutfit.size
    };

    // Add to inclusions with the correct type and data
    this.inclusions = [...this.inclusions, {
        type: 'individual_outfit',
        data: outfitData
    }];

    console.log('Added outfit:', outfitData);
    this.updateTotalPrice();
    this.selectedOutfit = null;
    this.closeOutfitModal();
},


  addSelectedOutfitPackage() {
    if (this.selectedOutfit) {
      this.inclusions.push({
        type: 'outfit_package',
        data: {
          gown_package_id: this.selectedOutfit.gown_package_id,
          gown_package_name: this.selectedOutfit.gown_package_name,
          gown_package_price: this.selectedOutfit.gown_package_price
        }
      });
      this.closeOutfitModal();
    }
  },

 

  switchOutfitMode(mode) {
      this.outfitSelectionMode = mode;
      this.selectedOutfit = null; // Reset selection when switching modes
    },

  closeOutfitModal() {
    this.showOutfitModal = false;
    this.selectedOutfit = null;
    this.outfitSelectionMode = 'package'; // Reset to default mode
  },
  removeInclusion(index) {
      this.inclusions = this.inclusions.filter((_, i) => i !== index);
      this.updateTotalPrice(); // Add this line
      console.log('Removed inclusion, new inclusions:', this.inclusions);
  },

    async editInclusion(index) {
      this.editingInclusionIndex = index;
      const inclusion = this.inclusions[index];
      
      console.log('Original inclusion:', inclusion);
      
      // Create a deep copy of the inclusion
      this.editingInclusion = JSON.parse(JSON.stringify(inclusion));
      
      console.log('Editing inclusion:', this.editingInclusion);
      
      // Pre-load the necessary data based on inclusion type
      try {
          if (inclusion.type === 'supplier') {
              if (!this.availableSuppliers.length) {
                  await this.fetchAvailableSuppliers();
              }
          } else if (inclusion.type === 'venue') {
              await this.fetchAvailableVenues();
              console.log('Venues after fetch:', this.availableVenues);
          } else if (inclusion.type === 'outfit') {
              await this.fetchAvailableGownPackages();
              console.log('Outfits after fetch:', this.availableGownPackages);
          } else if (inclusion.type === 'service') {
              await this.fetchAdditionalServices();
              console.log('Services after fetch:', this.additionalServices);
          }
          
          this.showEditInclusionModal = true;
          
      } catch (error) {
          console.error('Error loading data for edit modal:', error);
      }
  },

      closeEditInclusionModal() {
        this.showEditInclusionModal = false;
        this.editingInclusion = null;
        this.editingInclusionIndex = -1;
      },

      saveEditedInclusion() {
        if (!this.editingInclusion) return;

        if (this.editingInclusion.type === 'supplier') {
            if (this.editingInclusion.data.type === 'external') {
                if (!this.editingInclusion.data.external_supplier_name || !this.editingInclusion.serviceType) {
                    alert('Please fill in all required fields');
                    return;
                }

                this.editingInclusion.data.name = this.editingInclusion.data.external_supplier_name;
                const price = parseFloat(this.editingInclusion.data.external_supplier_price);
                this.editingInclusion.data.price = price;
            } else {
                const selectedSupplier = this.availableSuppliers.find(s => s.supplier_id === this.editingInclusion.data.supplier_id);
                if (selectedSupplier) {
                    this.editingInclusion.data = {
                        ...selectedSupplier,
                        supplier_id: selectedSupplier.supplier_id,
                        firstname: selectedSupplier.firstname,
                        lastname: selectedSupplier.lastname,
                        price: parseFloat(selectedSupplier.price || 0),
                        type: 'internal'
                    };
                }
            }

            const duplicateSupplier = this.inclusions.find((inclusion, index) => 
                index !== this.editingInclusionIndex &&
                inclusion.type === 'supplier' &&
                inclusion.serviceType === this.editingInclusion.serviceType
            );

            if (duplicateSupplier) {
                alert(`A supplier for ${this.editingInclusion.serviceType} already exists`);
                return;
            }
        }

        if (this.editingInclusion.type === 'outfit') {
            const selectedOutfit = this.availableGownPackages.find(o => o.gown_package_id === parseInt(this.editingInclusion.data.outfit_id));
            console.log('Selected outfit:', selectedOutfit);
            
            if (selectedOutfit) {
                this.editingInclusion.data = {
                    outfit_id: selectedOutfit.gown_package_id,
                    gown_package_id: selectedOutfit.gown_package_id,
                    name: selectedOutfit.gown_package_name,
                    gown_package_name: selectedOutfit.gown_package_name,
                    price: parseFloat(selectedOutfit.gown_package_price || 0),
                    gown_package_price: parseFloat(selectedOutfit.gown_package_price || 0)
                };
                console.log('Updated outfit data:', this.editingInclusion.data);
            }
        }

        if (this.editingInclusion.type === 'venue') {
            const selectedVenue = this.availableVenues.find(v => v.venue_id === this.editingInclusion.data.venue_id);
            if (selectedVenue) {
                this.editingInclusion.data = {
                    ...selectedVenue,
                    venue_id: selectedVenue.venue_id,
                    venue_name: selectedVenue.venue_name || selectedVenue.name,
                    price: parseFloat(selectedVenue.venue_price || selectedVenue.price || 0),
                    venue_price: parseFloat(selectedVenue.venue_price || selectedVenue.price || 0)
                };
            }
        }

        this.inclusions.splice(this.editingInclusionIndex, 1, this.editingInclusion);
        this.updateTotalPrice();
        this.closeEditInclusionModal();
    },
      getInclusionName(inclusion) {
          if (!inclusion || !inclusion.data) return 'Unknown Item';
          
          switch (inclusion.type) {
              case 'venue':
                  return inclusion.data.venue_name || 'Unknown Venue';
              case 'outfit_package':
                  return inclusion.data.gown_package_name || 'Unknown Package';
              case 'individual_outfit':
                  return inclusion.data.outfit_name || 'Unknown Outfit';
              case 'supplier':
                  if (inclusion.data.type === 'external') {
                      return `${inclusion.data.external_supplier_name || 'Unknown'} (External)`;
                  }
                  // Check for various field name combinations
                  if (inclusion.data.supplier_name) {
                      return inclusion.data.supplier_name;
                  }
                  if (inclusion.data.name) {
                      return inclusion.data.name;
                  }
                  if (inclusion.data.company_name) {
                      return inclusion.data.company_name;
                  }
                  if (inclusion.data.business_name) {
                      return inclusion.data.business_name;
                  }
                  if (inclusion.data.vendor_name) {
                      return inclusion.data.vendor_name;
                  }
                  // Fall back to firstname/lastname combination
                  const fullName = `${inclusion.data.firstname || ''} ${inclusion.data.lastname || ''}`.trim();
                  if (fullName) {
                      return fullName;
                  }
                  // If we have an ID, use a more descriptive fallback
                  if (inclusion.data.supplier_id) {
                      return `Supplier #${inclusion.data.supplier_id}`;
                  }
                  return 'Unnamed Supplier';
              case 'service':
                  return inclusion.data.service_name || 'Unknown Service';
              default:
                  return 'Unknown Item';
          }
      },
      getInclusionPrice(inclusion) {
          if (!inclusion || !inclusion.data) return '-';
          
          let price = 0;
          switch (inclusion.type) {
            case 'venue':
              price = parseFloat(inclusion.data.venue_price || 0);
              break;
          case 'outfit_package':
              price = parseFloat(inclusion.data.gown_package_price || 0);
              break;
          case 'individual_outfit':
          case 'outfit':
              price = parseFloat(inclusion.data.rent_price || 0);
              break;
          case 'supplier':
              price = parseFloat(inclusion.data.price || 0);
              break;
          case 'service':
              price = parseFloat(inclusion.data.price || 0);
              break;
              default:
                  price = 0;
          }

          // Format the price with commas and 2 decimal places
          return price.toLocaleString('en-PH', {
              style: 'decimal',
              minimumFractionDigits: 2,
              maximumFractionDigits: 2
          }) + ' php';
      },
    formatPrice(price) {
      if (!price) return '0.00';
      return parseFloat(price).toFixed(2).replace(/\d(?=(\d{3})+\.)/g, '$&,');
    },
    addCapacity() {
      if (this.additionalCapacity > 0) {
          this.selectedPackage.capacity += this.additionalCapacity;
          this.updateTotalPrice();
          this.showCapacityModal = false; // Hide the modal after updating
          this.additionalCapacity = 0; // Reset the input field
          alert('Capacity updated successfully!');
      } else {
          alert('Please enter a valid additional capacity.');
      }
    },
    calculateAdditionalCharges() {
        if (!this.additionalCapacity) return 0;
        const chargePerUnit = parseFloat(this.selectedPackage.additional_capacity_charges || 0);
        const chargeUnit = parseInt(this.selectedPackage.charge_unit || 1);
        const units = Math.ceil(this.additionalCapacity / chargeUnit);
        return units * chargePerUnit;
    },
    prevPackageDeals() {
        this.packagesDetailsForm = false;
        this.packagesForm = true;
    },

    updateTotalPrice() {
    let totalPrice = 0;
    console.log('Starting price calculation...');

    // Create Sets to track unique service types and outfit types
    const addedServices = new Set();
    const addedOutfitTypes = new Set();

    // Process all inclusions
    this.inclusions.forEach(inclusion => {
        let price = 0;
        console.log('Processing inclusion:', inclusion);
        
        // Only skip duplicates for suppliers and outfits, NOT for additional services
        if (inclusion.type === 'supplier' && addedServices.has(inclusion.serviceType)) {
            console.log(`Skipping duplicate supplier service: ${inclusion.serviceType}`);
            return;
        }

        if (inclusion.type === 'venue') {
            price = parseFloat(inclusion.data.venue_price || 0);
            console.log(`Adding venue price: ${price}`);
        } 
        else if (inclusion.type === 'outfit_package' || inclusion.type === 'outfit') {
            price = parseFloat(inclusion.data.price || inclusion.data.gown_package_price || 0);
            addedOutfitTypes.add(inclusion.type);
            console.log(`Adding outfit price: ${price}`);
        }
        else if (inclusion.type === 'supplier') {
            price = parseFloat(inclusion.data.price || 0);
            addedServices.add(inclusion.serviceType);
            console.log(`Adding supplier price (${inclusion.serviceType}): ${price}`);
        }
        else if (inclusion.type === 'service') {
            // Allow multiple services by not tracking them in addedServices
            price = parseFloat(inclusion.data.price || 0);
            console.log(`Adding additional service price: ${price}`);
        }

        totalPrice += price;
        console.log(`Current total after adding ${inclusion.type}: ${totalPrice}`);
    });

    // Add additional capacity charges if any
    if (this.selectedPackage && this.selectedPackage.additional_capacity > 0) {
        const additionalCapacity = this.selectedPackage.additional_capacity;
        const chargePerUnit = parseFloat(this.selectedPackage.additional_capacity_charges || 0);
        const chargeUnit = parseInt(this.selectedPackage.charge_unit || 1);
        const units = Math.ceil(additionalCapacity / chargeUnit);
        const additionalCharges = units * chargePerUnit;
        
        totalPrice += additionalCharges;
        console.log(`Additional capacity charges: ${additionalCharges}`);
        console.log(`Final total after capacity charges: ${totalPrice}`);
    }

    console.log('Final total:', totalPrice);
    this.totalPrice = totalPrice;
},

    cleanupDuplicateInclusions() {
        // Use a Map to keep track of unique items based on type and service type/ID
        const uniqueMap = new Map();
        
        this.inclusions = this.inclusions.filter(inclusion => {
            const key = inclusion.type === 'supplier' 
                ? `${inclusion.type}-${inclusion.serviceType}`
                : `${inclusion.type}-${inclusion.data.id || inclusion.data.venue_id || inclusion.data.gown_package_id}`;
                
            if (!uniqueMap.has(key)) {
                uniqueMap.set(key, true);
                return true;
            }
            return false;
        });
    },
    cancelOnsiteBooking() {
      this.$router.push('/manage-events');
    },
    addSelectedOutfit() {
        if (!this.selectedOutfit) {
            console.error('No outfit selected');
            return;
        }

        console.log('Current inclusions:', this.inclusions);
        
        // Check if this specific outfit type already exists
        const hasExistingOutfit = this.inclusions.some(item => 
            item.type === 'individual_outfit' && 
            item.data.outfit_id === this.selectedOutfit.outfit_id
        );
        
        if (hasExistingOutfit) {
            alert('This outfit is already added.');
            this.closeOutfitModal();
            return;
        }

        // Create outfit data with proper name and price
        const outfitData = {
            outfit_id: this.selectedOutfit.outfit_id,
            outfit_name: this.selectedOutfit.outfit_name,
            outfit_type: this.selectedOutfit.outfit_type,
            rent_price: parseFloat(this.selectedOutfit.rent_price || 0),
            size: this.selectedOutfit.size
        };

        // Add to inclusions with the correct type and data
        this.inclusions = [...this.inclusions, {
            type: 'individual_outfit',
            data: outfitData
        }];

        console.log('Added outfit:', outfitData);
        this.updateTotalPrice();
        this.selectedOutfit = null;
        this.closeOutfitModal();
    },
    filteredSuppliers(serviceType) {
        if (!this.availableSuppliers) return [];
        return this.availableSuppliers.filter(supplier => 
          supplier.service_type === serviceType || 
          supplier.supplier_type === serviceType
        );
      },
  },

  computed: {
    uniquePackageTypes() {
      const types = this.packages.map((pkg) => pkg.package_type);
      return [...new Set(types)]; // Use Set to remove duplicates
    },
  
    filteredInternalSuppliers() {
    return (currentSupplierId) => {
      return this.availableSuppliers.filter(supplier => {
        // Include suppliers not selected or currently selected for this dropdown
        return !this.selectedPackage.suppliers.some(
          selected => selected.type === 'internal' && selected.supplier_id === supplier.supplier_id && selected.supplier_id !== currentSupplierId
        );
      });
    };
  },

  filteredAdditionalServices() {
    if (!this.additionalServices) return [];
    
    const query = this.additionalServiceSearchQuery?.toLowerCase() || '';
    return this.additionalServices.filter(service => 
      service.add_service_name.toLowerCase().includes(query) ||
      service.add_service_description.toLowerCase().includes(query)
    );
  },
  
  calculatedTotalPrice() {
    let total = 0;
    this.inclusions.forEach(inclusion => {
        let price = 0;
        switch (inclusion.type) {
            case 'venue':
                price = parseFloat(inclusion.data.price || 0);
                break;
            case 'outfit_package':
                price = parseFloat(inclusion.data.price || 0);
                break;
            case 'individual_outfit':
            case 'outfit':
                price = parseFloat(inclusion.data.price || 0);
                break;
            case 'supplier':
                price = parseFloat(inclusion.data.price || 0);
                break;
            case 'service':
                price = parseFloat(inclusion.data.price || 0);
                break;
        }
        total += price;
    });

    // Add additional capacity charges if any
    if (this.selectedPackage && this.selectedPackage.additional_capacity > 0) {
        const additionalCapacity = this.selectedPackage.additional_capacity;
        const chargePerUnit = parseFloat(this.selectedPackage.additional_capacity_charges || 0);
        const chargeUnit = parseInt(this.selectedPackage.charge_unit || 1);
        const units = Math.ceil(additionalCapacity / chargeUnit);
        const additionalCharges = units * chargePerUnit;
        total += additionalCharges;
    }

    console.log('Total price calculation:', total);
    return total.toFixed(2);
},

   nextPhase() {
     this.personalInfoForm = false;
     this.wishlistDetailsForm = true;
   },
   backToPersonalInfo() {
     this.wishlistDetailsForm = false;
     this.personalInfoForm = true;
    },
       
  },
  mounted() {
    this.checkLoginStatus();
    this.fetchPackages();
    this.fetchAvailableSuppliers();
    this.fetchAvailableVenues();
    this.fetchAvailableGownPackages();
    this.fetchEventTypes();
    this.fetchAdditionalServices();
    this.cleanupDuplicateInclusions();
    this.fetchOutfits();
  },
  watch: {
    event_type(newValue) {
      console.log('Event type changed to:', newValue); // Add this
      if (newValue) {
        this.filterPackages();
      }
    },
  },
  created() {
    this.fetchBookedDates();
},
};
</script>






<style scoped>

</style>