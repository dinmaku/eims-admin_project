<template>
  <!--Events Header-->
  <div class="bg-gray-200 w-full h-full">
    <div class="w-full h-[65px] bg-gray-100 mt-2 flex items-center justify-between px-5 shadow-lg">
  <h1 class="font-amaticBold font-extraLight text-3xl">
    Events
  </h1>
  <div class="flex items-center">
    <button class="bg-[#9B111E] text-white px-3 py-2 rounded shadow-lg 
    transition-transform duration-300 transform hover:scale-105 font-semibold" 
    @click="directToOnsiteBooking">Onsite Booking</button>
  </div>
</div>
 

<!--Information Cards-->
 <div class = "flex justify-start space-x-5">
    <div class ="w-60 h-[80px] bg-white py-2 px-3 ml-5 mt-10 border-l-2 border-green-400 shadow-md flex items-center justify-between ">
    <h1 class ="font-amaticBold font-regular text-3xl ml-3 text-blue-900">{{ totalWishlist }}</h1>
     <p class = "font-amaticBold font-regular text-lg text-gray-700 mr-5">Total Wishlist</p>
    </div>
    <div class ="w-60 h-[80px] bg-white py-2 px-3 ml-5 mt-10 border-l-2 border-red-400 shadow-md flex items-center justify-between ">
    <h1 class ="font-amaticBold font-regular text-3xl ml-3 text-blue-900">12</h1>
     <p class = "font-amaticBold font-regular text-lg text-gray-700 mr-5">In Progress</p>
    </div>
    <div class ="w-60 h-[80px] bg-white py-2 px-3 ml-5 mt-10 border-l-2 border-yellow-400 shadow-md flex items-center justify-between ">
    <h1 class ="font-amaticBold font-regular text-3xl ml-3 text-blue-900">98</h1>
     <p class = "font-amaticBold font-regular text-lg text-gray-700 mr-5">Completed</p>
    </div>
  </div>

  <!--Navigation Buttons on tables-->
  <div class="flex justify-between space-x-2 m-5">
  <div class="flex space-x-2">
    <button
      :class="[
        'w-[90px] h-[45px] border border-solid rounded-md shadow-md transition-transform transform hover:scale-105',
        { 'bg-gray-800 text-gray-400 hover:bg-gray-900': showTable !== 'wishlist', 'bg-white': showTable === 'wishlist' }
      ]"
      @click="showTable = 'wishlist'"
    >
      <h1 class="font-amaticBold font-medium">Wishlist</h1>
    </button>
    <button
      :class="[
        'w-[140px] h-[45px] border border-solid rounded-md shadow-md transition-transform transform hover:scale-105',
        { 'bg-gray-800 text-gray-400 hover:bg-gray-900': showTable !== 'events', 'bg-white': showTable === 'events' }
      ]"
      @click="showTable = 'events'"
    >
      <h1 class="font-amaticBold font-medium">Upcoming Events</h1>
    </button>
    <button
      :class="[
        'w-[90px] h-[45px] border border-solid rounded-md shadow-md transition-transform transform hover:scale-105',
        { 'bg-gray-800 text-gray-400 hover:bg-gray-900': showTable !== 'finished-events', 'bg-white': showTable === 'finished-events' }
      ]"
      @click="showTable = 'finished-events'"
    >
      <h1 class="font-amaticBold font-medium">Completed</h1>
    </button>
  </div>
</div>
   
    

    <!-- Tables -->
    <div v-if="showTable === 'wishlist'" class="relative shadow-md sm:rounded-xl w-[1170px] h-[200] ml-5 mt-2 font-amaticBold mb-10">
      <div class="overflow-x-auto">
        <table class="w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400 mb-4 max-h-30">
          <thead class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
            <tr>
              <th scope="col" class="px-2 py-3">#</th>
              <th scope="col" class="px-2 py-3">Event</th>
              <th scope="col" class="px-2 py-3">Theme</th>
              <th scope="col" class="px-2 py-3">Color</th>
              <th scope="col" class="px-2 py-3">Venue</th>
              <th scope="col" class="px-2 py-3">Booked by</th>
              <th scope="col" class="px-2 py-3">Contact Number</th>
              <th scope="col" class="px-2 py-3">Action</th>
            </tr>
          </thead>
          <tbody>
            <tr
                v-for="(event, index) in paginatedWishlist"
                :key="event.events_id"
                :class="{'bg-blue-100': selectedIndex === index, 'odd:bg-white odd:dark:bg-gray-900 even:bg-gray-50 even:dark:bg-gray-800': selectedIndex !== index}"
                class="border-b dark:border-gray-700">
              <th scope="row" class="px-2 py-3 font-medium text-gray-900 whitespace-nowrap dark:text-white">{{ index + 1 }}</th>
              <td class="px-1 py-3 hidden sm:table-cell">{{ event.event_name }}</td>
              <td class="px-1 py-3 hidden sm:table-cell">{{ event.event_theme }}</td>
              <td class="px-1 py-3 hidden sm:table-cell">{{ event.event_color }}</td>
              <td class="px-1 py-3 hidden sm:table-cell">{{ event.venue_name }}</td>
              <td class="px-1 py-3 hidden sm:table-cell">{{ event.bookedBy }}</td>
              <td class="px-1 py-3 hidden sm:table-cell">{{ event.contactnumber }}</td>
              <td class="px-1 py-3 hidden sm:table-cell">
                <button
                    @click="openWishlistModal(event)"
                    class="h-8 w-12 bg-[#9B111E] font-amaticBold font-medium text-sm rounded-md text-white hover:bg-[#B73A45]">
                    View
                </button>
              </td>
            </tr>
          </tbody>
        </table>

        <!-- Pagination Controls -->
        <div class="flex justify-center space-x-2 mt-4 mb-6">
          <button @click="prevWishlistPage" :disabled="currentWishlistPage === 1" class="px-3 py-1 bg-[#9B111E] text-white rounded-md hover:bg-[#B73A45] disabled:opacity-50 text-md">Previous</button>
          <button v-for="page in totalWishlistPages" :key="page" @click="changeWishlistPage(page)" :class="{'bg-[#9B111E]': currentWishlistPage === page, 'bg-gray-300': currentWishlistPage !== page}" class="px-3 py-1 text-white rounded-md hover:bg-blue-600 text-xs">
            {{ page }}
          </button>
          <button @click="nextWishlistPage" :disabled="currentWishlistPage === totalWishlistPages" class="px-3 py-1 bg-[#9B111E] text-white rounded-md hover:bg-[#B73A45] disabled:opacity-50 text-md">Next</button>
        </div>
      </div>
    </div>

    <!-- Event Details Modal -->
    <div v-if="showEventModal" class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50 overflow-y-auto">
          <div class="bg-white p-6 rounded-lg shadow-lg w-full max-w-2xl overflow-auto max-h-[90vh]">
            <h2 class="text-2xl font-semibold mb-4">Event Details</h2>
            <div class="mb-4">
              <p class="text-lg"><strong>Event Name:</strong> {{ selectedEvent.event_name }}</p>
              <p class="text-lg"><strong>Event Type:</strong> {{ selectedEvent.event_type }}</p>
              <p class="text-lg"><strong>Theme:</strong> {{ selectedEvent.event_theme }}</p>
              <p class="text-lg"><strong>Color:</strong> {{ selectedEvent.event_color }}</p>
              <p class="text-lg"><strong>Venue:</strong> {{ selectedEvent.venue_name }}</p>
              <p class="text-lg"><strong>Booked By:</strong> {{ selectedEvent.firstname }} {{ selectedEvent.lastname }}</p>
              <p class="text-lg"><strong>Contact Number:</strong> {{ selectedEvent.contactnumber }}</p>
              <p class="text-lg"><strong>Total Price:</strong> {{ selectedEvent.total_price }}</p>
              <p class="text-lg"><strong>Gown Package:</strong> {{ selectedEvent.gown_package_name }}</p>
              <p class="text-lg"><strong>Price:</strong> {{ selectedEvent.gown_package_price }}</p>
            </div>
            <div class="mb-4">
              <h3 class="text-xl font-semibold">Suppliers</h3>
              <div v-for="(supplier, index) in selectedEvent.suppliers" :key="index" class="mb-2">
                <p class="text-lg"><strong>Name:</strong> {{ supplier.name }}</p>
                <p class="text-lg"><strong>Service:</strong> {{ supplier.service }}</p>
                <p class="text-lg"><strong>Price:</strong> {{ supplier.price }}</p>
              </div>
            </div>
            <div class="flex justify-end">
              <button @click="closeEventModal" class="bg-red-600 text-white px-4 py-2 rounded-md hover:bg-red-700">Close</button>
            </div>
          </div>
        </div>
      

    <!--Upcoming Events Table-->
    <div v-if="showTable === 'events'" class="relative shadow-md sm:rounded-xl w-[1170px] h-[200] ml-5 mt-2 font-amaticBold mb-10">
      <div class="overflow-x-auto">
        <table class="w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400 mb-4 max-h-30">
          <thead class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
            <tr>
              <th scope="col" class="px-2 py-3">#</th>
              <th scope="col" class="px-2 py-3">Event</th>
              <th scope="col" class="px-2 py-3">Event Name</th>
              <th scope="col" class="px-2 py-3">Package Deal</th>
              <th scope="col" class="px-2 py-3">Venue</th>
              <th scope="col" class="px-2 py-3">Schedule</th>
              <th scope="col" class="px-2 py-3">Start Time</th>
              <th scope="col" class="px-2 py-3">End Time</th>
              <th scope="col" class="px-2 py-3">Action</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="event in paginatedEvents" :key="event.no" class="odd:bg-white odd:dark:bg-gray-900 even:bg-gray-50 even:dark:bg-gray-800 border-b dark:border-gray-700">
              <th scope="row" class="px-2 py-3 font-medium text-gray-900 whitespace-nowrap dark:text-white">{{ event.no }}</th>
              <td class="px-1 py-3 hidden sm:table-cell">{{ event.event }}</td>
              <td class="px-1 py-3 hidden sm:table-cell">{{ event.eventName }}</td>
              <td class="px-1 py-3 hidden sm:table-cell">{{ event.packageDeal }}</td>
              <td class="px-1 py-3 hidden sm:table-cell">{{ event.venue }}</td>
              <td class="px-1 py-3 hidden sm:table-cell">{{ event.schedule }}</td>
              <td class="px-1 py-3 hidden sm:table-cell">{{ event.startTime }}</td>
              <td class="px-1 py-3 hidden sm:table-cell">{{ event.endTime }}</td>
              <td class="px-1 py-3 hidden sm:table-cell">
                <button
                @click="viewEvent(event)"
                    class="h-8 w-12 mr-2 bg-blue-900 font-amaticBold font-medium text-sm rounded-md text-white hover:bg-blue-600">
                    View
                  </button>
              </td>
            </tr>
          </tbody>
        </table>

        <!-- Pagination Controls -->
        <div class="flex justify-center space-x-2 mt-4 mb-6"> <!-- Added mb-6 for bottom margin -->
          <button @click="prevPage" :disabled="currentPage === 1" class="px-3 py-1 bg-blue-900 text-white rounded-md hover:bg-blue-600 disabled:opacity-50 text-md">Previous</button> <!-- Smaller button -->
          <button v-for="page in totalPages" :key="page" @click="changePage(page)" :class="{'bg-blue-900': currentPage === page, 'bg-gray-300': currentPage !== page}" class="px-3 py-1 text-white rounded-md hover:bg-blue-600 text-xs">
            {{ page }}
          </button>
          <button @click="nextPage" :disabled="currentPage === totalPages" class="px-3 py-1 bg-blue-900 text-white rounded-md hover:bg-blue-600 disabled:opacity-50 text-xs">Next</button> <!-- Smaller button -->
        </div>
      </div>
    </div>




    <!--Completed Events-->
    <div v-if="showTable === 'finished-events'" class="relative shadow-md sm:rounded-xl w-[1170px] h-[200] ml-5 mt-2 font-amaticBold mb-10">
      <div class="overflow-x-auto">
        <table class="w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400 mb-4 max-h-30">
          <thead class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
            <tr>
              <th scope="col" class="px-2 py-3">#</th>
              <th scope="col" class="px-2 py-3">Event</th>
              <th scope="col" class="px-2 py-3">Event Name</th>
              <th scope="col" class="px-2 py-3">Package Deal</th>
              <th scope="col" class="px-2 py-3">Venue</th>
              <th scope="col" class="px-2 py-3">Schedule</th>
              <th scope="col" class="px-2 py-3">Total Charges</th>
              <th scope="col" class="px-2 py-3">Invoice</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="event in paginatedFinishedEvents" :key="event.no" class="odd:bg-white odd:dark:bg-gray-900 even:bg-gray-50 even:dark:bg-gray-800 border-b dark:border-gray-700">
              <th scope="row" class="px-2 py-3 font-medium text-gray-900 whitespace-nowrap dark:text-white">{{ event.no }}</th>
              <td class="px-1 py-3 hidden sm:table-cell">{{ event.event }}</td>
              <td class="px-1 py-3 hidden sm:table-cell">{{event.eventName }}</td>
              <td class="px-1 py-3 hidden sm:table-cell">{{ event.packageDeal }}</td>
              <td class="px-1 py-3 hidden sm:table-cell">{{ event.venue }}</td>
              <td class="px-1 py-3 hidden sm:table-cell">{{ event.schedule }}</td>
              <td class="px-1 py-3 hidden sm:table-cell">{{ event.totalCharges }}</td>
              <td class="px-1 py-3 hidden sm:table-cell">
                <button class="h-8 w-12 bg-blue-900 font-amaticBold font-medium text-sm rounded-md text-white hover:bg-blue-600">View</button>
              </td>
            </tr>
          </tbody>
        </table>

        <!-- Pagination Controls -->
        <div class="flex justify-center space-x-2 mt-4 mb-6"> <!-- Added mb-6 for bottom margin -->
          <button @click="prevFinishedPage" :disabled="currentFinishedPage === 1" class="px-3 py-1 bg-blue-900 text-white rounded-md hover:bg-blue-600 disabled:opacity-50 text-md">Previous</button> <!-- Smaller button -->
          <button v-for="page in totalPages" :key="page" @click="changeFinishedPage(page)" :class="{'bg-blue-900': changeFinishedPage === page, 'bg-gray-300': changeFinishedPage !== page}" class="px-3 py-1 text-white rounded-md hover:bg-blue-600 text-xs">
            {{ page }}
          </button>
          <button @click="nextFinishedPage" :disabled="currentFinishedPage === totalFinishedPages" class="px-3 py-1 bg-blue-900 text-white rounded-md hover:bg-blue-600 disabled:opacity-50 text-xs">Next</button> <!-- Smaller button -->
        </div>
      </div>
    </div>

    <!-- Wishlist Modal -->
    <div v-if="showWishlistModal" class="fixed inset-0 bg-gray-600 bg-opacity-50 flex justify-center items-center" @click.self = "closeWishlistModal()">
      <div class="bg-white w-[900px] p-5 rounded-lg shadow-lg overflow-y-auto max-h-[80vh]">
        <!-- Header -->
        <div class="flex justify-between mb-4">
          <h2 class="text-lg font-bold">Wishlist Details</h2>
          <button @click="closeWishlistModal" class="text-red-500 text-3xl">×</button>
        </div>

        <!-- Basic Info -->
        <div class="grid grid-cols-2 gap-4 mb-6 font-amaticSC">
          <div>
            <label class="block text-xs font-medium mb-1 text-gray-600">Event Name</label>
            <input v-model="selectedEvent.event_name" type="text" class="w-full p-2 border rounded rounded text-sm">
          </div>
          <div>
            <label class="block text-xs font-medium mb-1 text-gray-600">Theme</label>
            <input v-model="selectedEvent.event_theme" type="text" class="w-full p-2 border rounded rounded text-sm">
          </div>
          <div>
            <label class="block text-xs font-medium mb-1 text-gray-600">Color</label>
            <input v-model="selectedEvent.event_color" type="text" class="w-full p-2 border rounded rounded text-sm">
          </div>
          <div>
            <label class="block text-xs font-medium mb-1 text-gray-600">Booked By</label>
            <input v-model="fullName" type="text" class="w-full p-2 border rounded rounded text-sm">
          </div>
          <div>
            <label class="block text-xs font-medium mb-1 text-gray-600">Contact</label>
            <input v-model="selectedEvent.contactnumber" type="text" class="w-full p-2 border rounded rounded text-sm">
          </div>
          <div>
            <label class="block text-xs font-medium mb-1 text-gray-600">Schedule</label>
            <input v-model="selectedEvent.schedule" type="text" class="w-full p-2 border rounded text-sm">
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
                {{ gownPackage.gown_package_name }} - {{ formatPrice(gownPackage.gown_package_price) }}
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


        <!-- Inclusions Tables -->
        <div class="mb-6 space-y-4">
          <!-- Venue Table -->
          <div>
            <h3 class="font-medium mb-2 font-raleway">Venue</h3>
            <div class="bg-gray-50 p-3 rounded">
              <table class="table-auto w-full text-left text-sm">
                <thead class="bg-gray-200">
                  <tr>
                    <th class="px-2 py-1">Name</th>
                    <th class="px-2 py-1">Location</th>
                    <th class="px-2 py-1">Price</th>
                    <th class ="px-1 py-1">Action</th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-if="selectedEvent.venues && selectedEvent.venues.length > 0">
                    <td class="px-2 py-1">{{ selectedEvent.venues[0].name }}</td>
                    <td class="px-2 py-1">{{ selectedEvent.venues[0].location }}</td>
                    <td class="px-2 py-1">{{ formatPrice(selectedEvent.venues[0].price) }} php</td>
                    <td class="px-2 py-1">
                      <div class="flex justify-start items-center space-x-2">
                    <div @click="removeInclusion(index)" class="inline-block cursor-pointer">
                    <img 
                      alt="Delete Icon" 
                      class="w-[17px] h-[17px] ml-2 transition-transform transform hover:scale-110 hover:brightness-90" 
                      src="/img/delete.png" 
                    >
                  </div>
                  </div>
                  </td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>

          <!-- Suppliers Table -->
          <div>
          <h3 class="font-medium mb-2 font-raleway">Suppliers</h3>
          <table class="table-auto w-full text-left text-sm">
            <thead class="bg-gray-200">
              <tr>
                <th class="px-2 py-1">Name</th>
                <th class="px-2 py-1">Service</th>
                <th class="px-2 py-1">Price</th>
                <th class="px-2 py-1">Action</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(supplier, index) in selectedEvent.suppliers" :key="index">
                <td class="px-2 py-1">{{ supplier.name }}</td>
                <td class="px-2 py-1">{{ supplier.service }}</td>
                <td class="px-2 py-1">{{ formatPrice(supplier.price) }}</td>
                <td class="px-2 py-1">
                   <div class = "flex justify-start items-center space-x-2">
                    <div class="inline-block cursor-pointer">
                    <img 
                      alt="Approve Icon" 
                      class="w-[17px] h-[17px] transition-transform transform hover:scale-110 hover:brightness-90" 
                      src="/img/mark.png" 
                    >
                  </div>
                  <button type = "button" @click="editInclusion(index)" class="inline-block cursor-pointer">
                              <img 
                                alt="Edit Icon" 
                                class="w-[17px] h-[17px] transition-transform transform hover:scale-110 hover:brightness-90" 
                                src="/img/edit.png" 
                              >
                      </button>
                 
                  <div @click="removeInclusion(index)" class="inline-block cursor-pointer">
                  <img 
                    alt="Delete Icon" 
                    class="w-[17px] h-[17px] transition-transform transform hover:scale-110 hover:brightness-90" 
                    src="/img/delete.png" 
                  >
                </div>
                 </div>
                </td>
              </tr>
            </tbody>
          </table>
        </div>


          <!-- Outfit Package Table -->
          <div>
            <h3 class="font-medium mb-2 font-raleway">Outfit Package</h3>
            <div class="bg-gray-50 p-3 rounded">
              <table class="table-auto w-full text-left text-sm">
                <thead class="bg-gray-200">
                  <tr>
                    <th class="px-2 py-1">Package Name</th>
                    <th class="px-2 py-1">Price</th>
                    <th class="px-2 py-1">Action</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td class="px-2 py-1">{{ selectedEvent?.gown_package_name || 'N/A' }}</td>
                    <td class="px-2 py-1">{{ formatPrice(selectedEvent?.gown_package_price || 0) }}</td>
                    <td class="px-2 py-1">
                    <div class = "flex justify-start items-center space-x-2">
                    <div @click="removeInclusion(index)" class="inline-block cursor-pointer">
                    <img 
                      alt="Delete Icon" 
                      class="w-[17px] h-[17px] ml-2 transition-transform transform hover:scale-110 hover:brightness-90" 
                      src="/img/delete.png" 
                    >
                  </div>
                  </div>
                  </td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>


          <!-- Additional Services Table -->
          <div>
            <h3 class="font-medium mb-2 font-raleway">Additional Services</h3>
            <table class="table-auto w-full text-left text-sm">
              <thead class="bg-gray-200">
                <tr>
                  <th class="px-2 py-1">Service Name</th>
                  <th class="px-2 py-1">Description</th>
                  <th class="px-2 py-1">Price</th>
                  <th class="px-2 py-1">Action</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="(service, index) in selectedEvent.services" :key="index">
                  <td class="px-2 py-1">{{ service.add_service_name }}</td>
                  <td class="px-2 py-1">{{ service.add_service_description }}</td>
                  <td class="px-2 py-1">{{ formatPrice(service.add_service_price) }}</td>
                  <td class="px-2 py-1">
                    <div class = "flex justify-start items-center space-x-2">
                    <div @click="removeInclusion(index)" class="inline-block cursor-pointer">
                    <img 
                      alt="Delete Icon" 
                      class="w-[17px] h-[17px] ml-2 transition-transform transform hover:scale-110 hover:brightness-90" 
                      src="/img/delete.png" 
                    >
                  </div>
                  </div>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>

          <div class="grid grid-cols-1 gap-4 mt-4">
          <div>
            <div class="flex justify-between items-center mb-2 mt-2">
              <label class="block text-xs font-semibold font-raleway">Capacity Details</label>
            </div>
            <div class="grid grid-cols-2 gap-4">
              <div>
                <label class="block text-sm font-medium mb-1">Capacity </label>
                <div class="flex items-center space-x-2">
                  <input :value="selectedEvent.capacity" disabled type="number" class="w-full p-2 border rounded bg-gray-50">
                  <span class="text-sm text-gray-600">{{ selectedEvent.charge_unit }}</span>
                </div>
              </div>
              <div>
                <label class="block text-sm font-medium mb-1">Additional Capacity</label>
                <div class="flex items-center space-x-2">
                  <input v-model.number="additionalCapacity" type="number" class="w-full p-2 border rounded" placeholder="Enter additional capacity">
                  <button @click="addCapacity" class="px-3 py-2 text-sm bg-blue-500 text-white rounded hover:bg-blue-600">
                    Add
                  </button>
                </div>
              </div>
            </div>
            <div class="mt-4">
              <label class="block text-sm font-medium mb-1">Total Capacity</label>
              <div class="flex items-center space-x-2">
                <input :value="totalCapacity" disabled type="number" class="w-full p-2 border rounded bg-gray-50">
                <span class="text-sm text-gray-600">{{ selectedEvent.charge_unit }}</span>
              </div>
            </div>
            <div class="mt-4">
              <label class="block text-sm font-medium mb-1">Additional Capacity Charges</label>
              <div class="flex items-center space-x-2">
                <span class="text-sm">₱{{ selectedEvent.additional_capacity_charges }} per {{ selectedEvent.charge_unit }} person/s</span>
              </div>
            </div>
          </div>
        </div>

        </div>

        <!-- Total Price Section -->
        <div class="bg-blue-50 p-4 rounded mb-6">
          <div class="flex justify-between items-center">
            <h3 class="font-medium">Total Price</h3>
            <span class="text-xl font-bold">{{ formatPrice(calculateTotalPrice) }}</span>
          </div>
        </div>

        <!-- Actions -->
        <div class="flex justify-end space-x-3">
          <button @click="saveChanges" class="px-4 py-2 bg-blue-500 text-white rounded">Save Changes</button>
          <button @click="closeWishlistModal" class="px-4 py-2 bg-gray-300 rounded">Cancel</button>
        </div>
      </div>
    </div>




<!----View / Edit event details----------->
<div v-if="upcomingEventDetailsModal" class="fixed inset-0 bg-gray-600 bg-opacity-50 flex justify-center items-center">
  <div class="bg-white w-[900px] h-full p-5 rounded-lg shadow-lg  overflow-y-auto overflow-x-hidden">
    <div class = "flex justify-between m-2 items-center ">
    <h2 class="text-lg mt-2 font-bold font-raleway text-gray-600">Event Details</h2>
  
    <button class="mt-2 bg-red-500 text-white px-3 py-1 rounded transform-transition duration-300 transform hover:scale-105" @click="closeUpcomingEventsModal">
      Close
    </button>
    
              
    </div>
    <div class = "flex m-1 mt-4">
            <button
            @click="viewInvoice(event)"
                class="h-8 w-24 bg-blue-900 font-amaticBold font-medium text-sm rounded-full text-white hover:bg-blue-600 transform-transition duration-300 transform hover:scale-105">
                View Invoice 
              </button>

    </div>
  

    <div class = "border border-gray-500 mt-3 items-center"></div>
    

    <!--------------->
    <div class="flex flex-col space-y-7 font-raleway mx-10 m-3">
      <div class = "flex justify-end">
        <label
  class="relative inline-block h-5 w-11 cursor-pointer rounded-full bg-gray-300 transition
   [-webkit-tap-highlight-color:_transparent] has-[:checked]:bg-gray-900">
   <input
            v-model="enableEditDetails"
            class="peer sr-only"
            id="enableEdit"
            type="checkbox"
          />
  <span
    class="absolute inset-y-0 start-0 m-1 size-3 rounded-full bg-gray-300 ring-[2px] 
    ring-inset ring-white transition-all peer-checked:start-8 peer-checked:w-1 peer-checked:bg-white peer-checked:ring-transparent"></span>
    </label>


      </div>
     
  <div class="flex items-center">
    <label class="text-sm font-semibold text-gray-600" for="eventType">Event Type:</label>
    <input 
      type="text" 
      class="ml-6 h-9 w-80 text-center rounded-lg text-sm font-bold bg-[#fefff6]" 
      v-model="selectedEvent.event"
      :disabled="!enableEditDetails"
    />
  </div>
  
  <div class="flex items-center">
    <label class="text-sm font-semibold text-gray-600" for="eventName">Event Name:</label>
    <input 
      type="text" 
      class="ml-4 h-9 w-80 text-center mb-2 rounded-lg text-sm font-bold bg-[#fefff6]" 
      v-model="selectedEvent.eventName"
      :disabled="!enableEditDetails"
    />
  </div>

  <div class="flex items-center ">
    <label class="text-sm font-semibold text-gray-600" for="eventName">Event Venue:</label>
    <input 
      type="text" 
      class="ml-4 h-9 w-80 text-center rounded-lg text-sm font-bold bg-[#fefff6]" 
      v-model="selectedEvent.venue"
      :disabled="!enableEditDetails"
    />
  </div>

  <div class="flex items-center ">
    <label class="text-sm font-semibold text-gray-600" for="eventName">Schedule Date:</label>
    <input 
      type="text" 
      class="ml-2 h-9 w-80 text-center font-gothic rounded-lg text-sm font-bold bg-[#fefff6]" 
      v-model="selectedEvent.schedule"
      :disabled="!enableEditDetails"
    />
  </div>
  <div class="flex items-center space-y-4 space-x-3 ">
    <label class="text-sm font-semibold text-gray-600 mt-4" for="eventName">Theme</label>
    <input 
      type="text" 
      class="ml-2 h-9 w-36 text-center font-gothic rounded-lg text-sm font-bold bg-[#fefff6]" 
      v-model="selectedEvent.theme"
      :disabled="!enableEditDetails"
    />
    <label class="text-sm font-semibold text-gray-600" for="eventName">Color</label>
    <input 
      type="text" 
      class="ml-2 h-9 w-36 text-center font-gothic rounded-lg text-sm font-bold bg-[#fefff6]" 
      v-model="selectedEvent.color"
      :disabled="!enableEditDetails"
    />
  </div>

  <div class="flex items-center space-y-4 space-x-3 ">
    <label class="text-sm font-semibold text-gray-600 mt-4" for="eventName">Start Time:</label>
    <input 
      type="text" 
      class="ml-2 h-9 w-36 text-center font-gothic rounded-lg text-sm font-bold bg-[#fefff6]" 
      v-model="selectedEvent.startTime"
      :disabled="!enableEditDetails"
    />
    <label class="text-sm font-semibold text-gray-600" for="eventName">End Time:</label>
    <input 
      type="text" 
      class="ml-2 h-9 w-36 text-center font-gothic rounded-lg text-sm font-bold bg-[#fefff6]" 
      v-model="selectedEvent.endTime"
      :disabled="!enableEditDetails"
    />
    <label for="vendor-name" class="block text-sm font-semibold font-raleway text-gray-700 mt-2">
      Capacity:
    </label>
    <div class="flex grid-col ml-2">
      <select v-model="selectedCapacity" class="w-38 h-9 text-sm font-semibold rounded-lg font-amaticRegular bg-[#fefff6]"
        :disabled="!enableEditDetails">
        <option v-for="(option, index) in capacities" :key="index" :value="option.value">
        {{ option.label }}
      </option>
      </select>
    </div>
  </div>
</div>

<div class = "border border-gray-500 mt-16 items-center"></div>

<!------Vendor Details------------->
  <div div class = "flex justify-between m-2 items-center ">
    <h2 class="text-md mt-2 font-bold font-raleway text-gray-700">Vendor Details</h2>


    <div class = "flex justify-end">
        <label
  class="relative right-6 inline-block h-5 w-11 cursor-pointer rounded-full bg-gray-300 transition
   [-webkit-tap-highlight-color:_transparent] has-[:checked]:bg-gray-900">
   <input
            v-model="editVendorDetails"
            class="peer sr-only"
            id="enableEdit"
            type="checkbox"
          />
  <span
    class="absolute inset-y-0 start-0 m-1 size-3 rounded-full bg-gray-300 ring-[2px] 
    ring-inset ring-white transition-all peer-checked:start-8 peer-checked:w-1 peer-checked:bg-white peer-checked:ring-transparent"></span>
    </label>
      </div>
  </div>

  <div class="flex mx-5 mt-10">
    <div class="row text-start">
      <label for="catering-service" class="text-sm font-semibold font-raleway text-gray-600">Catering Service. *</label>
      <select v-model="selectedCatering" id="catering-service" class="w-80 h-9 m-3 ml-[115px] rounded-lg text-sm font-bold bg-[#fefff6]" :disabled="!editVendorDetails">
        <option value="catering1">Savory Spread Catering</option>
        <option value="catering2">Delightful Bites Catering</option>
        <option value="catering3">Elegant Eats Events</option>
      </select>
      <span class="ml-5 text-sm font-semibold font-amaticRegular text-blue-700"> ( {{ getCateringPrice() }} )</span>
    </div>
  </div>

  <div class="flex mx-5 mt-3">
    <div class="row text-start">
      <label for="catering-service" class="text-sm font-semibold font-raleway text-gray-600">Photographer and Videographer. *</label>
      <select v-model="selectedMultimedia" id="catering-service" class="w-80 h-9 m-3 rounded-lg text-sm font-bold bg-[#fefff6]" :disabled="!editVendorDetails">
        <option value = "multimedia1">Crystal Clear Imagery</option>
        <option value = "multimedia2">Vivid Memories Media</option>
        <option value = "multimedia3">Shutter & Frame Creations</option>
      </select>
      <span class="ml-5 text-sm font-semibold font-amaticRegular text-blue-700">( {{ getMultimediaPrice() }} )</span>
    </div>
  </div>
  
  <div class="flex mx-5 mt-3">
    <div class="row text-start">
      <label for="catering-service" class="text-sm font-semibold font-raleway text-gray-600">Hair and Makeup Artist. *</label>
      <select v-model="selectedGlam" id="catering-service" class="w-80 h-9 ml-[75px] m-3 rounded-lg text-sm font-bold bg-[#fefff6]" :disabled="!editVendorDetails">
        <option value ="glam1">Glamour Heights</option>
        <option value="glam2">Radiant Luxe Studio</option>
        <option value ="glam3">Elegant Essence</option>
      </select>
      <span class="ml-5 text-sm font-semibold font-amaticRegular text-blue-700">( {{ getGlamPrice() }} )</span>
    </div>
  </div>

  <div class="flex mx-5 mt-3">
    <div class="row text-start">
      <label for="catering-service" class="text-sm font-semibold font-raleway text-gray-600">Event Host. *</label>
      <select v-model="selectedHost" id="catering-service" class="w-80 h-9 ml-[153px] m-3 rounded-lg text-sm font-bold bg-[#fefff6]" :disabled="!editVendorDetails">
        <option value = "host1">Boy Semilia</option>
        <option value = "host2">Edward Backward</option>
        <option value=  "host3">Ray Castillo</option>
      </select>
      <span class="ml-5 text-sm font-semibold font-amaticRegular text-blue-700">( {{ getHostPrice() }} )</span>
    </div>
  </div>

  <div class="flex mx-5 mt-3">
    <div class="row text-start">
      <label for="catering-service" class="text-sm font-semibold font-raleway text-gray-600">Sound and Lighting. *</label>
      <select v-model="selectedAudioVisual" id="catering-service" class="w-80 ml-[97px] h-9 m-3 rounded-lg text-sm font-bold bg-[#fefff6]" :disabled="!editVendorDetails">
        <option value = "audiovisual1">Jadiel Walton</option>
        <option value = "audiovisual2">Korbyn Norton</option>
        <option value = "audiovisual3">Nico Shepherd</option>
      </select>
      <span class="ml-5 text-sm font-semibold font-amaticRegular text-blue-700">( {{ getAudioVisualPrice() }} )</span>
    </div>
  </div>

  <div class="flex mx-5 mt-3">
    <div class="row text-start">
      <label for="catering-service" class="text-sm font-semibold font-raleway text-gray-600">Music and Entertainment. *</label>
      <select v-model="selectedEntertainment" id="catering-service" class="w-80 h-9 ml-[62px] m-3 rounded-lg text-sm font-bold bg-[#fefff6]" :disabled="!editVendorDetails">
        <option value = "entertainment1">Jovit Baldemonyo</option>
        <option value = "entertainment2">November Revenue</option>
        <option value = "entertainment3">Lani Misaluy-a</option>
      </select>
      <span class="ml-5 text-sm font-semibold font-amaticRegular text-blue-700">( {{ getEntertainmentPrice() }} )</span>
    </div>
  </div>

  <div class="flex mx-5 mt-3">
    <div class="row text-start">
      <label for="catering-service" class="text-sm font-semibold font-raleway text-gray-600">Transportation. *</label>
      <select v-model="selectedTransportation" id="catering-service" class="w-80 h-9 ml-[130px] m-3 rounded-lg text-sm font-bold bg-[#fefff6]" :disabled="!editVendorDetails">
        <option value="transportation1">Limousine Service Co.</option>
        <option value="transportation2">Vintage Car Rentals</option>
        <option value="transportation3">Kalesa Services</option>
      </select>
      <span class="ml-5 text-sm font-semibold font-amaticRegular text-blue-700">( {{ getTransportationPrice() }} )</span>
    </div>
  </div>

  <div class="flex mx-5 mt-3">
    <div class="row text-start">
      <label for="catering-service" class="text-sm font-semibold font-raleway text-gray-600">Invitations and Stationery. *</label>
      <select v-model="selectedInvitations" id="catering-service" class="w-80 h-9 ml-[60px] m-3 rounded-lg text-sm font-bold bg-[#fefff6]" :disabled="!editVendorDetails">
        <option value="invitations1">Custom Invitations Studio</option>
        <option value="invitations2">Digital Invitations Co.</option>
        <option value="invitations3">Elegant Stationery Creations</option>
      </select>
      <span class="ml-5 text-sm font-semibold font-amaticRegular text-blue-700">( {{ getInvitationsPrice() }} )</span>
    </div>
  </div>

  <div class="flex mx-5 mt-3">
    <div class="row text-start">
      <label for="catering-service" class="text-sm font-semibold font-raleway text-gray-600">Favors and Gifts. *</label>
      <select v-model="selectedGifts" id="catering-service" class="w-80 h-9 ml-[122px] m-3 rounded-lg text-sm font-bold bg-[#fefff6]" :disabled="!editVendorDetails">
        <option value="gifts1">Personalized Keepsakes Co.</option>
        <option value="gifts2">Edible Favors Bakery</option>
        <option value="gifts3">Themed Gift Suppliers</option>
      </select>
      <span class="ml-5 text-sm font-semibold font-amaticRegular text-blue-700">( {{ getGiftsPrice() }} )</span>
    </div>
  </div>

  <div class = "border border-gray-500 mt-16 items-center"></div>

  <!-------Service Details----------->
  <div div class = "flex justify-between m-2 items-center ">
    <h2 class="text-md mt-2 font-bold font-raleway text-gray-700">Service Details</h2>

    <div class = "flex justify-end">
        <label
  class="relative right-6 inline-block h-5 w-11 cursor-pointer rounded-full bg-gray-300 transition
   [-webkit-tap-highlight-color:_transparent] has-[:checked]:bg-gray-900">
   <input
            v-model="editServiceDetails"
            class="peer sr-only"
            id="enableEdit"
            type="checkbox"
          />
  <span
    class="absolute inset-y-0 start-0 m-1 size-3 rounded-full bg-gray-300 ring-[2px] 
    ring-inset ring-white transition-all peer-checked:start-8 peer-checked:w-1 peer-checked:bg-white peer-checked:ring-transparent"></span>
    </label>
      </div>
  </div>
  
  <div class = "mt-9">
    <h1 class = "flex ml-5 text-sm mt-2 font-bold font-raleway text-blue-700">Packages</h1>
  <table class="min-w-full m-5 mt-5 border-collapse">
    <thead>
        <tr>
            <th class=" px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-w-normal border-b">
                #
            </th>
            <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-w-normal border-b">
                Package Deal
            </th>
            <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-w-normal border-b">
                Price
            </th>
        </tr>
    </thead>
    <tbody>
    <tr>
        <td class="px-6 py-4 text-left text-sm text-gray-500">1</td>
        <td class="px-6 py-4 text-left text-sm text-gray-500">
            <select 
                v-model="selectedPackage" 
                :disabled="!editServiceDetails" 
                style="border: none; outline: none; background: transparent; appearance: none; padding: 0.5rem;"
            >
                <option 
                    v-for="pkg in packageDeal" 
                    :key="pkg.no" 
                    :value="pkg.packageName"
                >
                    {{ pkg.packageName }}
                </option>
            </select>
        </td>
        <td class="px-6 py-4 text-left text-sm text-gray-500">{{ getPackagePrice(selectedPackage) }}</td>
    </tr>
</tbody>
</table>

    <div class = "mt-9">
      <h1 class = "flex ml-5 text-sm mt-2 font-bold font-raleway text-blue-700">Outfits</h1>
      <table class="min-w-full m-5 mt-5 border-collapse">
    <thead>
        <tr>
            <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-w-normal border-b">#</th>
            <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-w-normal border-b">Outfit Type</th>
            <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-w-normal border-b">Outfit Name</th>
            <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-w-normal border-b">Price</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="px-6 py-4 text-left text-sm text-gray-500">1</td>
            <td class="px-6 py-4 text-left text-sm text-gray-500">Gown</td>
            <td class="px-6 py-4 text-left text-sm text-gray-500">
                <select 
                    v-model="selectedGown" 
                    :disabled="!editServiceDetails" 
                    style="border: none; outline: none; background: transparent; appearance: none; padding: 0.5rem;"
                >
                    <option 
                        v-for="item in attire.filter(a => a.type === 'gown')" 
                        :key="item.no" 
                        :value="item.name"
                    >
                        {{ item.name }}
                    </option>
                </select>
            </td>
            <td class="px-6 py-4 text-left text-sm text-gray-500">{{ attire.find(item => item.name === selectedGown)?.price }}</td>
        </tr>
        <tr>
            <td class="px-6 py-4 text-left text-sm text-gray-500">2</td>
            <td class="px-6 py-4 text-left text-sm text-gray-500">Tuxedo</td>
            <td class="px-6 py-4 text-left text-sm text-gray-500">
                <select 
                    v-model="selectedTuxedo" 
                    :disabled="!editServiceDetails" 
                    style="border: none; outline: none; background: transparent; appearance: none; padding: 0.5rem;"
                >
                    <option 
                        v-for="item in attire.filter(a => a.type === 'tuxedo')" 
                        :key="item.no" 
                        :value="item.name"
                    >
                        {{ item.name }}
                    </option>
                </select>
            </td>
            <td class="px-6 py-4 text-left text-sm text-gray-500">{{ attire.find(item => item.name === selectedTuxedo)?.price }}</td>
        </tr>
    </tbody>
</table>

 </div>


</div>



  </div>
</div>

 </div>




  </template>
 


 <script>
  import axios from 'axios';

  axios.defaults.withCredentials = true;

 export default {
  
  name: 'ManageEvents',
  data() {
    return {
      showTable: 'wishlist',
      currentWishlistPage: 1,
      rowsPerWishlistPage: 6,
      currentPage: 1,
      rowsPerPage: 6,
      currentFinishedPage: 1,
      rowsPerFinishedPage: 6,
      selectedIndex: null,
      selectedEvent: null,
      event: null,
      upcomingEventDetailsModal: false,
      enableEditDetails: false,
      editVendorDetails: false,
      editServiceDetails: false,

      bookedEvents: [],
      wishlist: [],
      inclusions: [],
      additionalServices: [],

      showEventModal: false,
      showWishlistModal: false,
      selectedEvent: {
      event_name: '',
      event_theme: '',
      event_color: '',
      contactnumber: '',
      firstname: '', 
      lastname: '', 
      suppliers: [],
      services: [],
      outfits: [],
      venues: [],
      inclusions: [],
      additionalCapacity: '',
      additional_capacity_charges: 0,
      charge_unit: 1,
      gown_package_name: 'N/A', // Added default value
      gown_package_price: 0 // Added default value
    },
    showAddCapacityModal: false,
      capacityList: [
        { capacity: '50-100', charges: 1000, unit: 'per head' },
        { capacity: '101-200', charges: 900, unit: 'per head' },
        { capacity: '201-300', charges: 800, unit: 'per head' }
      ],
      newCapacity: {
        capacity: '',
        charges: 0,
        unit: 'per head'
      },

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
  

     //Dummy rani!!
     selectedCapacity: '150to200',
     selectedCatering: 'catering1',
     selectedMultimedia: 'multimedia2',
     selectedGlam: 'glam3',
     selectedHost: 'host2',
     selectedAudioVisual: 'audiovisual1',
     selectedEntertainment: 'entertainment1',
     selectedTransportation: 'transportation1',
     selectedInvitations: 'invitations2',
     selectedGifts: 'gifts2',

     selectedPackage: this.selectedEvent ? this.selectedEvent.packageDeal : '',
     selectedGown: 'Royal Blue Evening Gown',
     selectedTuxedo: 'Midnight Blue Tuxedo',
       

     capacities: [
        { value: 'lessThan50', label: 'Less than 50' },
        { value: '50to100', label: '50 to 100' },
        { value: '100to150', label: '100 to 150' },
        { value: '150to200', label: '150 to 200' },
        { value: 'moreThan200', label: 'More than 200' },
      ],

      packageDeal: [
             {no: '1', packageName: 'Basic Package', price: '₱30,000'},
             {no: '2', packageName: 'Premium Package', price: '₱60,000'},
             {no: '3', packageName: 'Vip Package', price: '₱100,000'},
      ],

      attire: [
            { no: 1, type: 'gown', name: 'Royal Blue Evening Gown', price: '₱2,000' },
            { no: 2, type: 'gown', name: 'Vintage Lace Gown', price: '₱3,000' },
            { no: 3, type: 'gown', name: 'Bohemian Dream Gown', price: '₱1,500' },
            { no: 4, type: 'gown', name: 'Simple Satin Gown', price: '₱1,200' },
            { no: 5, type: 'gown', name: 'Romantic Ball Gown', price: '₱1,800' },
            { no: 6, type: 'tuxedo', name: 'Classic Black Tuxedo', price: '₱2,800' },
            { no: 7, type: 'tuxedo', name: 'Velvet Tuxedo', price: '₱4,500' },
            { no: 8, type: 'tuxedo', name: 'Midnight Blue Tuxedo', price: '₱3,200' },
            { no: 9, type: 'tuxedo', name: 'White Dinner Jacket', price: '₱2,500' },
            { no: 10, type: 'tuxedo', name: 'Black Shawl Lapel Tuxedo', price: '₱3,000' },
            { no: 11, type: 'tuxedo', name: 'Patterned Tuxedo', price: '₱3,500' },
            { no: 12, type: 'tuxedo', name: 'Burgundy Tuxedo', price: '₱3,300' },
        ],

    

      events: [
        { no: 1, event: "Wedding", eventName: "Nido & Lactum Wedding", packageDeal: "Premium Package", venue: "Grand Ballroom", schedule: "2024-06-15", startTime: "16:00", endTime: "23:00", theme: 'Rustic Elegance', color: 'Sage Green', },
        { no: 2, event: "Birthday", eventName: "John's 30th Bash", packageDeal: "Basic Package", venue: "Riverside Pavilion", schedule: "2024-07-22", startTime: "18:00", endTime: "22:00", theme: 'Classic Romance', color: ' Ivory, Gold, and Champagne', },
        { no: 3, event: "Debut", eventName: "Emma's Debut", packageDeal: "Basic Package",  venue: "Royal Hall", schedule: "2024-08-05", startTime: "19:00", endTime: "22:00", theme: 'Beach Bliss', color: 'Navy Blue and Rose Gold', },
        { no: 4, event: "Seminar", eventName: "Health & Wellness", packageDeal: "Basic Package", venue: "City Conference Hall", schedule: "2024-09-10", startTime: "10:00", endTime: "15:00", theme: 'Vintage Glamour', color: ' Aqua Blue, Coral, Sand, and White', },
        { no: 5, event: "Conference", eventName: "Tech Innovate 2024", packageDeal: "VIP Package", venue: "Grand Hotel", schedule: "2024-10-01", startTime: "09:30", endTime: "17:30", theme: 'Garden Party', color: ' Mint Green, Soft Yellow, and White', },
        { no: 6, event: "Rally", eventName: "Community Rally", packageDeal: "Basic Package", venue: "Town Square", schedule: "2024-11-20", startTime: "12:00", endTime: "15:00", theme: 'Modern Minimalist', color: 'Black, White, and Gold', },
        { no: 7, event: "Wedding", eventName: "Elegant Evening", packageDeal: "Premium Package", venue: "Luxe Venue", schedule: "2024-12-25", startTime: "17:00", endTime: "23:00", theme: 'Fairytale Fantasy', color: 'Soft Lavender and Light Blue', },
        { no: 8, event: "Conference", eventName: "Annual Tech Summit", packageDeal: "VIP Package", venue: "Innovation Center", schedule: "2025-01-15", startTime: "08:00", endTime: "16:00", theme: 'Autumn Harvest', color: 'Deep Red, Olive Green, and Gold', }
        // Insert diri!!
      ],
      finishedEvents: [
        { no: 1, event: "Festival", eventName: 'Annual Tech Summit', packageDeal: 'Gold Package', venue: 'Innovation Center', schedule: '2025-01-15', totalCharges: "140k"},
        { no: 2, event: 'Exhibition', eventName: 'Art Expo 2025', packageDeal: 'Silver Package', venue: 'Exhibition Hall', schedule: '2025-03-10', totalCharges: "120k"},
        { no: 3, event: 'Workshop', eventName: 'Tech Skills Workshop', packageDeal: 'Standard Package', venue: 'Tech Hub', schedule: '2025-04-20', totalCharges: "100k"},
        { no: 4, event: 'Charity Gala', eventName: 'Annual Charity Ball', packageDeal: 'Platinum Package', venue: 'Grand Palace', schedule: '2025-05-30', totalCharges: "170k"},
          // Insert diri!!
      ],
      wishlist: [],
      
      
      vendors: [
        { no: 1, Name: 'Delightful Bites Catering', email: 'bites.catering@example.com', contact: '123-456-7890', service: 'Catering', minPrice:'30k php', maxPrice: '250k php' },
        { no: 2, Name: 'Vivid Memories Media', email: 'vivid.media@example.com', contact: '234-567-8901', service: 'Multimedia', minPrice:'20k php', maxPrice: '120k php' },
        { no: 3, Name: 'Elegant Eats Events', email: 'elegant.eats@example.com', contact: '345-678-9012', service: 'Catering', minPrice: '20k php', maxPrice: '150k php' },
        { no: 4, Name: 'Elegant Essence', email: 'essence22@example.com', contact: '456-789-0123', service: 'Hair and Makeup', minPrice: '10k php', maxPrice: '40k php' },
        { no: 5, Name: 'Nico Shepherd', email: 'nico.shepherd@example.com', contact: '567-890-1234', service: 'Sound and Light', minPrice: '20k php', maxPrice: '70k php' },
        { no: 6, Name: 'Jovit Baldemonyo', email: 'jovit.baldemonyo@example.com', contact: '678-901-2345', service: 'Entertainment', minPrice: '5k php', maxPrice: '80k php' },
        { no: 7, Name: 'November Revenue', email: 'november.revenue@example.com', contact: '789-012-3456', service: 'Entertainment', minPrice: '10k php', maxPrice: '100k php' },
        { no: 8, Name: 'Edward Backward', email: 'edward.backward@example.com', contact: '890-123-4567', service: 'Host', minPrice: '7k php', maxPrice: '40k php' },
        { no: 9, Name: 'Vintage Car Rentals', email: 'vintage.rentals@example.com', contact: '901-234-5678', service: 'Transportation', minPrice: '15k php', maxPrice: '60k php' },
        { no: 10, Name: 'Custom Invitations Studio', email: 'custom.studio@example.com', contact: '012-345-6789', service: 'Invitations and Stationery', minPrice: '20k php', maxPrice: '70k php' },
        { no: 11, Name: 'Personalized Keepsakes Co.', email: 'personalized.keepsakes@example.com', contact: '123-456-7890', service: 'Favors and Gifts', minPrice: '15k php', maxPrice: '100k php' },
        { no: 12, Name: 'Radiant Luxe Studio', email: 'radiant.luxe@example.com', contact: '234-567-8901', service: 'Hair and Makeup', minPrice: '7k php', maxPrice: '30k php' }
      ],
      

    };
  },
  watch: {
    selectedEvent(newEvent) {
        if (newEvent) {
            this.selectedPackage = newEvent.packageDeal;
        }
    },
    
},

  computed: {
    totalPages() {
      return Math.ceil(this.events.length / this.rowsPerPage);
    },
    paginatedEvents() {
      const start = (this.currentPage - 1) * this.rowsPerPage;
      const end = start + this.rowsPerPage;
      return this.events.slice(start, end);
    },
    totalFinishedPages() {
      return Math.ceil(this.finishedEvents.length / this.rowsPerFinishedPage);
    },
    paginatedFinishedEvents() {
      const start = (this.currentFinishedPage - 1) * this.rowsPerFinishedPage;
      const end = start + this.rowsPerFinishedPage;
      return this.finishedEvents.slice(start, end);
    },
    totalWishlistPages() {
      return Math.ceil(this.wishlist.length / this.rowsPerWishlistPage);
    },
    paginatedWishlist() {
      const start = (this.currentWishlistPage - 1) * this.rowsPerWishlistPage;
      const end = start + this.rowsPerWishlistPage;
      return this.wishlist.slice(start, end);
    },
    buttonCursor() {
      return this.selectedIndex === null? 'cursor-not-allowed' : 'cursor-pointer';
    },
    totalWishlist() {
       return this.wishlist.length;
    },
    fullName: {
      get() {
        return `${this.selectedEvent.firstname || ''} ${this.selectedEvent.lastname || ''}`.trim();
      },
      set(value) {
        const [firstname, ...rest] = value.split(' ');
        this.selectedEvent.firstname = firstname || '';
        this.selectedEvent.lastname = rest.join(' ') || '';
      }
    },
    filteredSuppliers() {
      return this.suppliers.filter(supplier => 
        supplier.service === this.selectedSupplierType
      );
    },
    
    filteredAdditionalServices() {
      return this.additionalServices.filter(service => 
        !this.selectedEvent.services.some(s => s.add_service_id === service.add_service_id)
      );
    },
    allInclusions() {
        const inclusions = [];
        const uniqueItems = new Map();

        // Add suppliers
        if (this.selectedEvent && Array.isArray(this.selectedEvent.suppliers)) {
          this.selectedEvent.suppliers.forEach(supplier => {
            const key = `${supplier.id}_${supplier.service}`;
            if (!uniqueItems.has(key)) {
              uniqueItems.set(key, {
                name: `${supplier.name} (${supplier.service})`,
                type: 'Supplier',
                price: supplier.price
              });
            }
          });
        }

        // Add venue details
        if (this.selectedEvent && this.selectedEvent.venue_name) {
          uniqueItems.set('venue', {
            name: `${this.selectedEvent.venue_name} (${this.selectedEvent.venue_location})`,
            type: 'Venue',
            price: parseFloat(this.selectedEvent.venue_price) || 0
          });
        }

        // Add additional services
        if (this.selectedEvent && Array.isArray(this.selectedEvent.services)) {
          this.selectedEvent.services.forEach(service => {
            const key = `service_${service.add_service_name}`;
            if (!uniqueItems.has(key)) {
              uniqueItems.set(key, {
                name: `${service.add_service_name} - ${service.add_service_description}`,
                type: 'Additional Service',
                price: service.add_service_price
              });
            }
          });
        }

        return Array.from(uniqueItems.values());
      },


    calculateTotalPrice() {
      return this.allInclusions.reduce((total, item) => total + (parseFloat(item.price) || 0), 0);
    },
    totalCapacity() {
    return Number(this.selectedEvent.capacity || 0) + Number(this.additionalCapacity || 0);
  }
},


  methods: {
    async fetchBookedWishlist() {
        try {
          const token = localStorage.getItem('access_token');
          if (!token) return;

          const response = await axios.get('http://127.0.0.1:5000/booked-wishlist', {
            headers: { 'Authorization': `Bearer ${token}` },
            withCredentials: true
          });

          this.wishlist = (Array.isArray(response.data) ? response.data : []).map(event => {
            // Process suppliers
            const suppliers = Array.isArray(event.suppliers) ? event.suppliers.map(s => ({
              id: s.supplier_id,
              name: s.external_supplier_name || `${s.supplier_firstname || ''} ${s.supplier_lastname || ''}`.trim(),
              service: s.service || '',
              price: parseFloat(s.external_supplier_price || s.price) || 0,
              contact: s.external_supplier_contact || s.supplier_email || '',
              remarks: s.remarks || ''
            })) : [];

            // Process venues
            const venues = Array.isArray(event.venues) ? event.venues.map(v => ({
              id: v.venue_id,
              name: v.venue_name || '',
              location: v.location || '',
              price: parseFloat(v.venue_price) || 0,
              capacity: parseInt(v.venue_capacity) || 0,
              description: v.description || ''
            })) : [];

            // Process services
            const services = Array.isArray(event.services) ? event.services.map(s => ({
              id: s.add_service_id,
              name: s.add_service_name || '',
              description: s.add_service_description || '',
              price: parseFloat(s.add_service_price) || 0
            })) : [];

            // Calculate total price
            const basePrice = parseFloat(event.total_price) || 0;
            const venuePrice = venues.reduce((sum, v) => sum + v.price, 0);
            const gownPrice = parseFloat(event.gown_package_price) || 0;
            const capacityCharges = parseFloat(event.additional_capacity_charges) || 0;
            const suppliersTotal = suppliers.reduce((sum, s) => sum + s.price, 0);
            const servicesTotal = services.reduce((sum, s) => sum + s.price, 0);

            return {
              events_id: event.events_id,
              userid: event.userid,
              event_name: event.event_name || '',
              event_type: event.event_type || '',
              event_theme: event.event_theme || '',
              event_color: event.event_color || '',
              schedule: event.schedule || '',
              start_time: event.start_time || '',
              end_time: event.end_time || '',
              status: event.status || '',
              package_id: event.package_id,
              package_name: event.package_name || '',
              package_type: event.package_type || '',
              capacity: event.capacity || 0,
              package_description: event.package_description || '',
              package_price: basePrice,
              total_price: basePrice + venuePrice + gownPrice + capacityCharges + suppliersTotal + servicesTotal,
              venue_price: venuePrice,
              firstname: event.firstname || '',
              lastname: event.lastname || '',
              contactnumber: event.contactnumber || '',
              email: event.email || '',
              bookedBy: `${event.firstname || ''} ${event.lastname || ''}`.trim(),
              additional_capacity_charges: capacityCharges,
              charge_unit: event.charge_unit || 'per head',
              gown_package_name: event.gown_package_name || '',
              gown_package_price: gownPrice,
              onsite_firstname: event.onsite_firstname || '',
              onsite_lastname: event.onsite_lastname || '',
              onsite_contact: event.onsite_contact || '',
              onsite_address: event.onsite_address || '',
              suppliers: suppliers,
              venues: venues,
              services: services,
              modified_suppliers: {
                added: [],
                modified: [],
                removed: []
              },
              modified_venues: {
                added: [],
                modified: [],
                removed: []
              }
            };
          });

          console.log('Processed wishlist:', this.wishlist);
        } catch (error) {
          console.error('Error:', error);
          this.wishlist = [];
        }
      },
            async fetchAdditionalServices() {
        try {
          const token = localStorage.getItem('access_token');
          const response = await axios.get('http://127.0.0.1:5000/additional-services', {
            headers: {
              Authorization: `Bearer ${token}`
            }
          });
          this.additionalServices = response.data.additional_services;
        } catch (error) {
          console.error('Error fetching additional services:', error);
        }
      },



    prevPage() {
      if (this.currentPage > 1) {
        this.currentPage--;
      }
    },
    nextPage() {
      if (this.currentPage < this.totalPages) {
        this.currentPage++;
      }
    },
    changePage(page) {
      this.currentPage = page;
    },
    prevFinishedPage() {
      if (this.currentFinishedPage > 1) {
        this.currentFinishedPage--;
      }
    },
    nextFinishedPage() {
      if (this.currentFinishedPage < this.totalFinishedPages) {
        this.currentFinishedPage++;
      }
    },
    changeFinishedPage(page) {
      this.currentFinishedPage = page;
    },
    prevWishlistPage() {
      if (this.currentWishlistPage > 1) {
        this.currentWishlistPage--;
      }
    },
    nextWishlistPage() {
      if (this.currentWishlistPage < this.totalWishlistPages) {
      this.currentWishlistPage++;

      this.selectedIndex = null;
      this.selectedEvent = null;
      }
    },
    changeWishlistPage(page) {
      this.currentWishlistPage = page;
    },
    toggleTable(tableName) {
      this.showTable = tableName;
    },

    selectRowAndRedirect(index) {
        const selectedEvent = this.paginatedWishlist[index];

        this.$router.push({
            path: '/create-event',
            query: {
                events_id: selectedEvent.events_id,
                event_name: selectedEvent.event_name,
                event_type: selectedEvent.event_type,
                event_theme: selectedEvent.event_theme,
                event_color: selectedEvent.event_color,
                venue_name: selectedEvent.venue_name,
                schedule: selectedEvent.schedule,
                start_time: selectedEvent.start_time,
                end_time: selectedEvent.end_time,
                status: selectedEvent.status,
                firstname: selectedEvent.firstname,
                lastname: selectedEvent.lastname,
                contactnumber: selectedEvent.contactnumber,
                suppliers: JSON.stringify(selectedEvent.suppliers),
                total_price: selectedEvent.total_price,
                gown_package_name: selectedEvent.gown_package_name,
                gown_package_price: selectedEvent.gown_package_price,
            }
        });
    },

    openEventModal(event) {
      this.selectedEvent = event;
      this.showEventModal = true;
    },
    closeEventModal() {
      this.showEventModal = false;
      this.selectedEvent = {};
    },

  

    viewEvent(event) {
      this.selectedEvent = event; 
      this.upcomingEventDetailsModal = true; 
    },

  viewInvoice(event) {
    this.selectedEvent = event; 
    this.$router.push('/invoice');
  },

  closeUpcomingEventsModal() 
  {
    this.upcomingEventDetailsModal = false;
    this.enableEditDetails = false;
    this.editVendorDetails = false;
  },

  updatePricing() {
      console.log(`Selected capacity: ${this.selectedCapacity}`);
    },
    addSelectedSupplier() {
    if (this.selectedSupplier) {
      const existingSupplier = this.selectedEvent.suppliers.find(
        s => s.supplier_id === this.selectedSupplier.supplier_id
      );
      
      if (!existingSupplier) {
        this.selectedEvent.suppliers.push({
          ...this.selectedSupplier,
          price: this.selectedSupplier.price || 0
        });
      }
      this.closeSupplierModal();
    }
  },

  addSelectedVenue() {
    if (this.selectedVenue) {
      this.selectedEvent.venue = this.selectedVenue;
      this.closeVenueModal();
    }
  },

  addSelectedOutfit() {
    if (this.selectedOutfit) {
      this.selectedEvent.outfit = this.selectedOutfit;
      this.closeOutfitModal();
    }
  },

  addSelectedService() {
    if (this.selectedService) {
      const existingService = this.selectedEvent.services.find(
        s => s.add_service_id === this.selectedService.add_service_id
      );
      
      if (!existingService) {
        this.selectedEvent.services.push({
          ...this.selectedService,
          price: this.selectedService.price || 0
        });
      }
      this.closeServiceModal();
    }
  },

  removeSupplier(index) {
    this.selectedEvent.suppliers.splice(index, 1);
  },

  removeService(index) {
    this.selectedEvent.services.splice(index, 1);
  },

  removeVenue() {
    this.selectedEvent.venue = null;
  },

  removeOutfit() {
    this.selectedEvent.outfit = null;
  },

  openInclusionModal(type) {
    this.selectedInclusionType = type;
    this.showInclusionModal = true;
    if (type === 'venue') {
      this.showVenueModal = true;
    } else if (type === 'outfit') {
      this.showOutfitModal = true;
    } else if (type === 'service') {
      this.showServiceModal = true;
    }
  },

  closeInclusionModal() {
    this.showInclusionModal = false;
    this.selectedInclusionType = '';
  },

  closeSupplierModal() {
    this.showSupplierModal = false;
    this.selectedSupplier = null;
  },

  closeVenueModal() {
    this.showVenueModal = false;
    this.selectedVenue = null;
  },

  closeOutfitModal() {
    this.showOutfitModal = false;
    this.selectedOutfit = null;
  },

  closeServiceModal() {
    this.showServiceModal = false;
    this.selectedService = null;
  },

  selectSupplierType(type) {
    this.selectedSupplierType = type;
    this.showInclusionModal = false;
    this.showSupplierModal = true;
  },
    getPackagePrice(packageName) {
        const Package = this.packageDeal.find(pkg => pkg.packageName === packageName);
        return Package ? Package.price : 'Price not available';
    },
    formatPrice(price) {
      const numPrice = Number(price) || 0;
      return numPrice.toLocaleString('en-PH', {
        style: 'currency',
        currency: 'PHP',
        minimumFractionDigits: 2,
        maximumFractionDigits: 2
      });
    },

  openWishlistModal(event) {
    this.selectedEvent = {
      ...this.selectedEvent, // Keep default values for undefined fields
      ...event,
      gown_package_name: event.gown_package_name || 'N/A',
      gown_package_price: event.gown_package_price || 0,
      firstname: event.firstname || '',
      lastname: event.lastname || '',
      contactnumber: event.contactnumber || ''
    };
    this.showWishlistModal = true;
  },
  addCapacity() {
    if (this.additionalCapacity > 0) {
      this.selectedEvent.capacity = this.totalCapacity;
      this.additionalCapacity = 0;
    }
  },



  addInclusion(type) {
      // Add a new inclusion based on the type
      const name = prompt('Enter inclusion name:');
      const price = parseFloat(prompt('Enter price:')) || 0;
      if (name) {
        const category = this.inclusions.find((cat) => cat.type === type);
        category.items.push({ name, price });
      }
    },
    editInclusion(type, index) {
        // Convert type to lowercase and match with the correct array
        const inclusionTypes = {
          'suppliers': 'suppliers',
          'venues': 'venues',
          'outfits': 'outfits',
          'additional services': 'services'
        };

        const arrayType = inclusionTypes[type.toLowerCase()];
        if (arrayType) {
          // Open a modal or perform edit logic
          // For example:
          this.editingInclusion = this.selectedEvent[arrayType][index];
          this.showInclusionModal = true;
        }
      },
      removeInclusion(type, index) {
        const inclusionTypes = {
          'suppliers': 'suppliers',
          'venues': 'venues',
          'outfits': 'outfits',
          'additional services': 'services'
        };

        const arrayType = inclusionTypes[type.toLowerCase()];
        if (arrayType) {
          // Remove the inclusion from the specific array
          this.selectedEvent[arrayType].splice(index, 1);
        }
      },

    saveChanges() {
      // Save changes logic
      alert('Changes saved!');
    },
    closeWishlistModal() {
      // Close modal logic
      this.showWishlistModal = false;
    },
    viewEvent(event) {
      // Deep clone the event to prevent direct mutation
      this.selectedEvent = JSON.parse(JSON.stringify(event)); 
      this.upcomingEventDetailsModal = true; 
    },
    openInclusionModal(type) {
      this.selectedInclusionType = type;
      this.showInclusionModal = true;
      if (type === 'venue') {
        this.showVenueModal = true;
      } else if (type === 'outfit') {
        this.showOutfitModal = true;
      } else if (type === 'service') {
        this.showServiceModal = true;
      }
    },
    closeInclusionModal() {
      this.showInclusionModal = false;
      this.selectedInclusionType = '';
    },
    closeSupplierModal() {
      this.showSupplierModal = false;
      this.selectedSupplier = '';
    },
    closeVenueModal() {
      this.showVenueModal = false;
      this.selectedVenue = '';
    },
    closeOutfitModal() {
      this.showOutfitModal = false;
      this.selectedOutfit = '';
    },
    closeServiceModal() {
      this.showServiceModal = false;
      this.selectedService = '';
    },
    selectSupplierType(type) {
      this.selectedSupplierType = type;
      this.showInclusionModal = false;
      this.showSupplierModal = true;
    },
    addSelectedSupplier() {
      if (this.selectedSupplier) {
        // Add supplier logic here
        this.closeSupplierModal();
      }
    },
    addSelectedVenue() {
      if (this.selectedVenue) {
        // Add venue logic here
        this.closeVenueModal();
      }
    },
    addSelectedOutfit() {
      if (this.selectedOutfit) {
        // Add outfit logic here
        this.closeOutfitModal();
      }
    },
    addSelectedService() {
      if (this.selectedService) {
        // Add service logic here
        this.closeServiceModal();
      }
    },

    directToOnsiteBooking(){
      this.$router.push('/add-wishlist');
    }
  

  },

  mounted() {
        this.fetchBookedWishlist();
        console.log(this.paginatedWishlist);
        this.fetchAdditionalServices(); 
         
    },


  
};
  </script>

<style>
.fade-enter-active, .fade-leave-active {
  transition: opacity 0.5s ease, transform 0.5s ease;
}
.fade-enter, .fade-leave-to {
  opacity: 0;
  transform: translateY(-10px);
}
</style> 