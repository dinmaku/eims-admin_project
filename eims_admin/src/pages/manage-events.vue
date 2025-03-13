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
        { 'bg-gray-800 text-white hover:bg-gray-900': showTable !== 'wishlist', 'bg-white': showTable === 'wishlist' }
      ]"
      @click="showTable = 'wishlist'"
    >
      <h1 class="font-amaticBold font-medium">Wishlist</h1>
    </button>
    <button
      :class="[
        'w-[140px] h-[45px] border border-solid rounded-md shadow-md transition-transform transform hover:scale-105',
        { 'bg-gray-800 text-white hover:bg-gray-900': showTable !== 'events', 'bg-white': showTable === 'events' }
      ]"
      @click="showTable = 'events'"
    >
      <h1 class="font-amaticBold font-medium">Upcoming Events</h1>
    </button>
    <button
      :class="[
        'w-[90px] h-[45px] border border-solid rounded-md shadow-md transition-transform transform hover:scale-105',
        { 'bg-gray-800 text-white hover:bg-gray-900': showTable !== 'finished-events', 'bg-white': showTable === 'finished-events' }
      ]"
      @click="showTable = 'finished-events'"
    >
      <h1 class="font-amaticBold font-medium">Completed</h1>
    </button>
  </div>
</div>
   
    

    <!-- Tables -->
    <div v-if="showTable === 'wishlist'" class="relative shadow-md sm:rounded-xl w-full max-w-[1170px] h-[200] ml-5 mt-2 font-amaticBold mb-10">
      <div class="overflow-x-auto">
        <table class="w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400 mb-4 table-fixed">
          <thead class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
            <tr>
              <th scope="col" class="px-2 py-3 w-12">#</th>
              <th scope="col" class="px-2 py-3 w-32">Event</th>
              <th scope="col" class="px-2 py-3 w-32">Theme</th>
              <th scope="col" class="px-2 py-3 w-32">Venue</th>
              <th scope="col" class="px-2 py-3 w-32">Booked by</th>
              <th scope="col" class="px-2 py-3 w-32">Contact Number</th>
              <th scope="col" class="px-2 py-3 w-20">Action</th>
            </tr>
          </thead>
          <tbody>
            <tr
                v-for="(event, index) in paginatedWishlist"
                :key="event.events_id"
                :class="{'bg-blue-100': selectedIndex === index, 'odd:bg-white odd:dark:bg-gray-900 even:bg-gray-50 even:dark:bg-gray-800': selectedIndex !== index}"
                class="border-b dark:border-gray-700">
              <th scope="row" class="px-2 py-3 font-medium text-gray-900 dark:text-white">{{ index + 1 }}</th>
              <td class="px-1 py-3 truncate">{{ event.event_name }}</td>
              <td class="px-1 py-3 truncate">{{ event.event_theme }}</td>
              <td class="px-1 py-3 truncate">{{ event.venue_name || 'Not assigned' }}</td>
              <td class="px-1 py-3 truncate">{{ event.bookedBy || 'Not assigned' }}</td>
              <td class="px-1 py-3 truncate">{{ event.onsite_contact || event.contactnumber || 'Not provided' }}</td>
              <td class="px-1 py-3 flex justify-start">
                <button
                    @click="openWishlistModal(event)"
                    class="p-2 hover:opacity-80 transform hover:scale-110 transition-transform duration-200">
                    <img src="/img/update3.png" alt="Update" class="w-5 h-5">
                </button>
                <button
                  @click="goToInvoice()"
                class="p-2 hover:opacity-80 transform hover:scale-110 transition-transform duration-200">
                <img src="/img/invoice.png" alt="Update" class="w-5 h-5">
               </button>
               <button
                @click="updateEventStatus(event)"
                class="p-2 hover:opacity-80 transform hover:scale-110 transition-transform duration-200">
                <img src="/img/approve.png" alt="Update" class="w-5 h-5" title="Upcoming Event">
               </button>
               
              </td>
            </tr>
          </tbody>
        </table>

        <!-- Pagination Controls -->
        <div class="flex justify-center space-x-2 mt-4 mb-6">
          <button @click="prevWishlistPage" :disabled="currentWishlistPage === 1" class="px-3 py-1 bg-[#9B111E] text-white rounded-md hover:bg-[#B73A45] disabled:opacity-50 text-md">Previous</button>
          <button v-for="page in totalWishlistPages" :key="page" @click="changeWishlistPage(page)" :class="{'bg-[#9B111E]': currentWishlistPage === page, 'bg-gray-300': currentWishlistPage !== page}" class="px-3 py-1 text-white rounded-md hover:bg-[#B73A45] text-xs">
            {{ page }}
          </button>
          <button @click="nextWishlistPage" :disabled="currentWishlistPage === totalWishlistPages" class="px-3 py-1 bg-[#9B111E] text-white rounded-md hover:bg-[#B73A45] disabled:opacity-50 text-md">Next</button>
        </div>
      </div>
    </div>

    <!-- Status Update Confirmation Modal -->
    <div v-if="showStatusConfirmationModal" @click.self="closeStatusConfirmationModal" class="fixed inset-0 bg-gray-800 bg-opacity-50 overflow-y-auto flex justify-center items-center z-50">
      <div class="bg-white p-5 rounded-lg shadow-lg w-[400px]">
        <div class="flex flex-col items-center">
          <h2 class="text-xl font-semibold mb-4">Confirm Status Change</h2>
          <p class="mb-6 text-center">Are you sure you want to move this event to Upcoming Events?</p>
          <div class="flex space-x-4">
            <button 
              @click="closeStatusConfirmationModal" 
              class="bg-gray-500 text-white px-4 py-2 rounded hover:bg-opacity-90">
              Cancel
            </button>
            <button 
              @click="confirmUpdateStatus" 
              class="bg-blue-500 text-white px-4 py-2 rounded hover:bg-opacity-90">
              Yes
            </button>
          </div>
        </div>
      </div>
    </div>

    <!--Upcoming Events Table-->
    <div v-if="showTable === 'events'" class="relative shadow-md sm:rounded-xl w-full max-w-[1170px] h-[200] ml-5 mt-2 font-amaticBold mb-10">
      <div class="overflow-x-auto">
        <table class="w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400 mb-4 max-h-30">
          <thead class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
            <tr>
              <th scope="col" class="px-2 py-3">#</th>
              <th scope="col" class="px-2 py-3">Event Name</th>
              <th scope="col" class="px-2 py-3">Event Theme</th>
              <th scope="col" class="px-2 py-3">Venue</th>
              <th scope="col" class="px-2 py-3">Booked By</th>
              <th scope="col" class="px-2 py-3">Contact</th>
              <th scope="col" class="px-2 py-3">Action</th>
            </tr>
          </thead>
          <tbody>
            <tr
                v-for="(event, index) in paginatedUpcomingEvents"
                :key="event.events_id"
                :class="{'bg-blue-100': selectedIndex === index, 'odd:bg-white odd:dark:bg-gray-900 even:bg-gray-50 even:dark:bg-gray-800': selectedIndex !== index}"
                class="border-b dark:border-gray-700">
              <th scope="row" class="px-2 py-3 font-medium text-gray-900 dark:text-white">{{ index + 1 }}</th>
              <td class="px-1 py-3 truncate">{{ event.event_name }}</td>
              <td class="px-1 py-3 truncate">{{ event.event_theme }}</td>
              <td class="px-1 py-3 truncate">{{ event.venue_name || 'Not assigned' }}</td>
              <td class="px-1 py-3 truncate">{{ event.bookedBy || 'Not assigned' }}</td>
              <td class="px-1 py-3 truncate">{{ event.onsite_contact || event.contactnumber || 'Not provided' }}</td>
              <td class="px-1 py-3 flex justify-start">
                <button
                    @click="openWishlistModal(event)"
                    class="p-2 hover:opacity-80 transform hover:scale-110 transition-transform duration-200">
                    <img src="/img/update3.png" alt="Update" class="w-5 h-5">
                </button>
                <button
                  @click="goToInvoice()"
                  class="p-2 hover:opacity-80 transform hover:scale-110 transition-transform duration-200">
                  <img src="/img/invoice.png" alt="Update" class="w-5 h-5">
                  </button>
              </td>
            </tr>
          </tbody>
        </table>

        <!-- Pagination Controls -->
        <div class="flex justify-center space-x-2 mt-4 mb-6">
          <button @click="prevPage" :disabled="currentPage === 1" class="px-3 py-1 bg-[#9B111E] text-white rounded-md hover:bg-[#B73A45] disabled:opacity-50 text-md">Previous</button>
          <button v-for="page in totalPages" :key="page" @click="changePage(page)" :class="{'bg-[#9B111E]': currentPage === page, 'bg-gray-300': currentPage !== page}" class="px-3 py-1 text-white rounded-md hover:bg-[#B73A45] text-xs">
            {{ page }}
          </button>
          <button @click="nextPage" :disabled="currentPage === totalPages" class="px-3 py-1 bg-[#9B111E] text-white rounded-md hover:bg-[#B73A45] disabled:opacity-50 text-xs">Next</button>
        </div>
        
        <!-- Debug Button -->
        <div class="flex justify-center mb-4">
          <button @click="debugUpcomingEvents" class="px-4 py-2 bg-blue-500 text-white rounded">
            Debug Upcoming Events
          </button>
        </div>
      </div>
    </div>




    <!--Completed Events-->
    <div v-if="showTable === 'finished-events'" class="relative shadow-md sm:rounded-xl w-full max-w-[1170px] h-[200] ml-5 mt-2 font-amaticBold mb-10">
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
      <div class="bg-white w-[900px] p-5 rounded-lg shadow-lg overflow-y-auto max-h-[97vh]">
        <!-- Header -->
        <div class="flex justify-between mb-4">
          <h2 class="text-lg font-bold">Wishlist Details</h2>
          <button @click="closeWishlistModal" class="text-red-500 text-3xl">×</button>
        </div>

        <!-- Basic Info -->
        <div class="grid grid-cols-2 gap-4 mb-6 font-amaticSC">
          <div>
            <label class="block text-xs font-medium mb-1 text-gray-600 text-start">Event Name</label>
            <input v-model="selectedEvent.event_name" disabled  type="text" class="w-full p-2 border rounded rounded text-sm">
          </div>
          <div>
            <label class="block text-xs font-medium mb-1 text-gray-600 text-start">Theme</label>
            <input v-model="selectedEvent.event_theme" disabled type="text" class="w-full p-2 border rounded rounded text-sm">
          </div>
          <div>
            <label class="block text-xs font-medium mb-1 text-gray-600 text-start">Color</label>
            <input v-model="selectedEvent.event_color" disabled  type="text" class="w-full p-2 border rounded rounded text-sm">
          </div>
          <div>
            <label class="block text-xs font-medium mb-1 text-gray-600 text-start">Booked By</label>
            <input v-model="fullName" type="text" disabled class="w-full p-2 border rounded rounded text-sm">
          </div>
          <div>
            <label class="block text-xs font-medium mb-1 text-gray-600 text-start">Contact</label>
            <input v-model="selectedEvent.contactnumber" disabled type="text" class="w-full p-2 border rounded rounded text-sm">
          </div>
          <div>
            <label class="block text-xs font-medium mb-1 text-gray-600 text-start">Schedule</label>
            <input v-model="selectedEvent.schedule" disabled type="text" class="w-full p-2 border rounded text-sm">
          </div>
        </div>

        <div class = "mb-4">
            <p class = "text-md font-medium font-poppins text-gray-500">(* Click the buttons to Add items to the list )</p>
          </div>


        <!-- Inclusion Buttons -->
        <div class="grid grid-cols-4 gap-4 mb-4">
            <button 
              @click.prevent="openInclusionModal('supplier')" 
              class="flex items-center justify-center bg-[#9B111E] text-white px-3 py-2 h-[50px] rounded-md hover:bg-[#B73A45]"
            >
              <img alt="Supplier Icon" class="mr-2 w-[20px] h-[20px]" src="/img/supplier.png">
              Suppliers
            </button>
            <button 
              @click.prevent="openInclusionModal('venue')" 
              class="flex items-center justify-center bg-[#9B111E] text-white px-3 py-2 h-[50px] rounded-md hover:bg-[#B73A45]"
            >
              <img alt="Venue Icon" class="mr-2 w-[20px] h-[20px]" src="/img/venues1.png">
             Venue
            </button>
            <button 
              @click.prevent="openInclusionModal('outfit')" 
              class="flex items-center justify-center bg-[#9B111E] text-white px-3 py-2 h-[50px] rounded-md hover:bg-[#B73A45]"
            >
              <img alt="Outfit Icon" class="mr-2 w-[20px] h-[20px]" src="/img/costume.png">
             Outfits
            </button>
            <button 
              @click.prevent="openInclusionModal('service')" 
              class="flex items-center justify-center bg-[#9B111E] text-white px-3 py-2 h-[50px] rounded-md hover:bg-[#B73A45]"
            >
              <img alt="Service Icon" class="mr-2 w-[20px] h-[20px]" src="/img/additionals.png">
              Other Inclusions
            </button>
          </div>




        <!-- Inclusions Tables -->
        <div class="mb-6 space-y-4">
          <!-- Venue Table -->
          <div>
            <h3 class="font-semibold text-blue-900 mb-2 font-raleway text-start ml-3">Venue</h3>
              <table class="table-auto w-full text-left text-sm">
                <thead class="bg-gray-200">
                  <tr>
                    <th class="px-2 py-1">Name</th>
                    <th class="px-2 py-1">Location</th>
                    <th class="px-2 py-1">Rate</th>
                    <th class="px-2 py-1">Status</th>
                    <th class="px-2 py-1">Action</th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-if="selectedEvent.venues && selectedEvent.venues.length > 0">
                    <td class="px-2 py-1">{{ selectedEvent.venues[0].venue_name }}</td>
                    <td class="px-2 py-1">{{ selectedEvent.venues[0].location }}</td>
                    <td class="px-2 py-1">₱{{ formatPrice(selectedEvent.venues[0].venue_price) }}</td>
                    <td class="px-2 py-1">
                      <span :class="{'text-yellow-600': !selectedEvent.venues[0].status || selectedEvent.venues[0].status === 'Pending', 'text-green-600': selectedEvent.venues[0].status === 'Approved'}">
                        {{ selectedEvent.venues[0].status || 'Pending' }}
                      </span>
                    </td>
                    <td class="px-2 py-1">
                      <div class="flex justify-start items-center space-x-2">
                        <div class="inline-block cursor-pointer">
                        <img 
                          alt="Approve Icon" 
                          class="w-[17px] h-[17px] transition-transform transform hover:scale-110 hover:brightness-90" 
                          src="/img/mark.png" 
                            @click="approveInclusion('venues', 0)"
                        >
                      </div>
                        <button type="button" @click="editInclusion('venues', 0)" class="inline-block cursor-pointer">
                        <img 
                          alt="Edit Icon" 
                          class="w-[17px] h-[17px] transition-transform transform hover:scale-110 hover:brightness-90" 
                          src="/img/edit.png" 
                        >
                      </button>
                    <div @click="removeInclusion('venues', 0)" class="inline-block cursor-pointer">
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

          <!-- Suppliers Table -->
          <div>
            <h3 class="font-semibold text-blue-900 mb-2 font-raleway text-start ml-3">Suppliers</h3>
            <table class="table-auto w-full text-left text-sm">
              <thead class="bg-gray-200">
                <tr>
                  <th class="px-2 py-1">Name</th>
                  <th class="px-2 py-1">Service</th>
                  <th class="px-2 py-1">Price</th>
                  <th class="px-2 py-1">Status</th>
                  <th class="px-2 py-1">Action</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="(supplier, index) in selectedEvent.suppliers" :key="index">
                  <td class="px-2 py-1">
                    {{ supplier.name || supplier.supplier_name || (supplier.supplier_firstname && supplier.supplier_lastname ? supplier.supplier_firstname + ' ' + supplier.supplier_lastname : 'Unknown Supplier') }}
                  </td>
                  <td class="px-2 py-1">{{ supplier.service_type || supplier.service }}</td>
                  <td class="px-2 py-1">₱{{ formatPrice(supplier.price) }}</td>
                  <td class="px-2 py-1">
                    <span :class="{'text-yellow-600': !supplier.status || supplier.status === 'Pending', 'text-green-600': supplier.status === 'Approved'}">
                      {{ supplier.status || 'Pending' }}
                    </span>
                  </td>
                  <td class="px-2 py-1">
                    <div class="flex justify-start items-center space-x-2">
                      <div class="inline-block cursor-pointer" @click="approveInclusion('suppliers', index)">
                        <img 
                          alt="Approve Icon" 
                          class="w-[17px] h-[17px] transition-transform transform hover:scale-110 hover:brightness-90" 
                          src="/img/mark.png" 
                        >
                      </div>
                      <button type="button" @click="editInclusion('suppliers', index)" class="inline-block cursor-pointer">
                        <img 
                          alt="Edit Icon" 
                          class="w-[17px] h-[17px] transition-transform transform hover:scale-110 hover:brightness-90" 
                          src="/img/edit.png" 
                        >
                      </button>
                      <div @click="removeInclusion('suppliers', index)" class="inline-block cursor-pointer">
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
            <h3 class="font-semibold text-blue-900 mb-2 font-raleway text-start ml-3">Outfits</h3>
            <table class="table-auto w-full text-left text-sm">
              <thead class="bg-gray-200">
                <tr>
                  <th class="px-2 py-1">Outfit Name</th>
                  <th class="px-2 py-1">Rate</th>
                  <th class="px-2 py-1">Status</th>
                  <th class="px-2 py-1">Action</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="(outfit, index) in selectedEvent.outfits" :key="index">
                  <td class="px-2 py-1">{{ outfit.gown_package_name || outfit.outfit_name }}</td>
                  <td class="px-2 py-1">₱{{ formatPrice(outfit.gown_package_price || outfit.price || outfit.rent_price) }}</td>
                  <td class="px-2 py-1">
                    <span :class="{'text-yellow-600': !outfit.status || outfit.status === 'Pending', 'text-green-600': outfit.status === 'Approved'}">
                      {{ outfit.status || 'Pending' }}
                    </span>
                  </td>
                  <td class="px-2 py-1">
                    <div class="flex justify-start items-center space-x-2">
                      <div class="inline-block cursor-pointer">
                        <img 
                          alt="Approve Icon" 
                          class="w-[17px] h-[17px] transition-transform transform hover:scale-110 hover:brightness-90" 
                          src="/img/mark.png" 
                          @click="approveInclusion('outfits', index)"
                        >
                      </div>
                      <button type="button" @click="editInclusion('outfits', index)" class="inline-block cursor-pointer">
                        <img 
                          alt="Edit Icon" 
                          class="w-[17px] h-[17px] transition-transform transform hover:scale-110 hover:brightness-90" 
                          src="/img/edit.png" 
                        >
                      </button>
                      <button 
                        v-if="!outfit.is_initialized"
                        @click="removeInclusion('outfits', index)" 
                        class="inline-block cursor-pointer"
                      >
                        <img 
                          alt="Delete Icon" 
                          class="w-[17px] h-[17px] transition-transform transform hover:scale-110 hover:brightness-90" 
                          src="/img/delete.png" 
                        >
                      </button>
                    </div>
                  </td>
                </tr>
              </tbody>
            </table>
</div>


          <!-- Additional Services Table -->
          <div>
            <h3 class="font-semibold text-blue-900 mb-2 font-raleway text-start ml-3">
              Other Inclusions 
              <button @click="debugServices" class="ml-2 text-xs bg-gray-200 px-2 py-1 rounded">Debug</button>
            </h3>
            <table class="table-auto w-full text-left text-sm">
              <thead class="bg-gray-200">
                <tr>
                  <th class="px-2 py-1">Inclusion Name</th>
                  <th class="px-2 py-1">Description</th>
                  <th class="px-2 py-1">Rate</th>
                  <th class="px-2 py-1">Status</th>
                  <th class="px-2 py-1">Action</th>
                </tr>
              </thead>
              <tbody>
                <tr v-if="!selectedEvent.services || selectedEvent.services.length === 0">
                  <td colspan="5" class="px-2 py-4 text-center text-gray-500">No services added yet</td>
                </tr>
                <tr v-for="(service, index) in selectedEvent.services" :key="index">
                  <td class="px-2 py-1">{{ service?.add_service_name || 'N/A' }}</td>
                  <td class="px-2 py-1">{{ service?.add_service_description || 'N/A' }}</td>
                  <td class="px-2 py-1">₱{{ formatPrice(service?.add_service_price || 0) }}</td>
                  <td class="px-2 py-1">
                    <span :class="{'text-yellow-600': !service?.status || service?.status === 'Pending', 'text-green-600': service?.status === 'Approved'}">
                      {{ service?.status || 'Pending' }}
                    </span>
                  </td>
                  <td class="px-2 py-1">
                    <div class="flex justify-start items-center space-x-2">
                      <div class="inline-block cursor-pointer">
                        <img 
                          alt="Approve Icon" 
                          class="w-[17px] h-[17px] transition-transform transform hover:scale-110 hover:brightness-90" 
                          src="/img/mark.png" 
                          @click="approveInclusion('services', index)"
                        >
                      </div>
                      <button type="button" @click="editInclusion('services', index)" class="inline-block cursor-pointer">
                        <img 
                          alt="Edit Icon" 
                          class="w-[17px] h-[17px] transition-transform transform hover:scale-110 hover:brightness-90" 
                          src="/img/edit.png" 
                        >
                      </button>
                    <div @click="removeInclusion('services', index)" class="inline-block cursor-pointer">
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
        </div>

      <div class ="mt-5 mb-5">
            <h3 class ="font-semibold text-blue-900 mb-2 font-raleway text-start ml-3">Capcity Pax</h3>
          <div class ="w-full p-2 border rounded bg-gray-100 flex flex-col justify-center items-center">
            <p class = "text-md font-medium">Package Pax: <span class = "font-semibold">{{ selectedEvent.capacity }} persons</span></p>
            <p class = "text-md ">Additional Charges: <span class = "font-medium">₱{{ selectedEvent.additional_capacity_charges }} per {{ selectedEvent.charge_unit }} person/s</span></p>
            <button type = "button"
                  @click="showCapacityModal = true"
                  class="mt-2 bg-[#9B111E] hover:bg-[#B73A45] text-white py-2 px-4 rounded-lg shadow-lg transition-transform duration-300 transform hover:scale-105"
              >
                  Add Capacity
              </button>
          </div>
      </div>

      <!-- Capacity Modal -->
      <div v-if="showCapacityModal" @click.self="showCapacityModal = false" class="fixed inset-0 bg-gray-600 bg-opacity-50 overflow-y-auto h-full w-full flex items-center justify-center">
                  <div class="relative bg-white rounded-lg shadow-xl p-6 max-w-md w-full">
                      <div class="flex justify-between items-center mb-4">
                          <h3 class="text-lg font-semibold text-gray-800">Add Additional Pax</h3>
                          <button type = "button" @click="showCapacityModal = false" class="text-gray-500 hover:text-gray-700">
                              <span class="text-2xl">&times;</span>
                          </button>
                      </div>

                      <div class="space-y-4">
                          <div class="bg-gray-50 p-3 rounded text-start">
                              <label class="block text-sm font-medium text-gray-700 mb-1">Current Event Pax</label>
                              <p class="text-lg font-semibold">{{ selectedEvent.capacity }} persons</p>
                          </div>

                          <div class="bg-gray-50 p-3 rounded text-start">
                              <label class="block text-sm font-medium text-gray-700 mb-1">Additional Charge Rate</label>
                              <p class="text-lg font-semibold">{{ formatPrice(selectedEvent.additional_capacity_charges) }} per {{ selectedEvent.charge_unit }} person(s)</p>
                          </div>

                          <div>
                              <label class="block text-sm font-medium text-gray-700 mb-2 text-start">Additional Pax</label>
                              <div class="flex items-center space-x-2">
                                  <input 
                                      type="number" 
                                      v-model.number="additionalCapacity"
                                      @input="updateAdditionalCapacity($event.target.value)"
                                      class="w-full p-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
                                      min="0"
                                  >
                                  <span class="text-sm text-gray-600">persons</span>
                              </div>
                          </div>

                          <div v-show="additionalCapacity > 0" class="bg-blue-50 p-4 rounded transition-all duration-200">
                              <p class="text-sm font-medium text-blue-900">
                                  Additional charges: {{ formatPrice(calculateAdditionalCharges()) }}
                              </p>
                              <p class="text-xs text-blue-700 mt-1">
                                  ({{ additionalCapacity }} persons × {{ formatPrice(selectedEvent.additional_capacity_charges) }}/{{ selectedEvent.charge_unit }} person(s))
                              </p>
                              <p class="text-sm font-medium text-blue-900 mt-3">
                                  New total capacity: {{ selectedEvent.capacity + additionalCapacity }} persons
                              </p>
                          </div>
                      </div>

                      <div class="mt-6 flex justify-end space-x-3">
                          <button 
                              @click="showCapacityModal = false" 
                              class="px-4 py-2 border border-gray-300 rounded-lg text-gray-700 hover:bg-gray-50 transition-colors"
                          >
                              Cancel
                          </button>
                          <button 
                              @click="addCapacity" 
                              class="px-4 py-2 bg-[#9B111E] text-white rounded-lg hover:bg-[#B73A45] transition-colors"
                              :disabled="!additionalCapacity"
                              :class="{'opacity-50 cursor-not-allowed': !additionalCapacity}"
                          >
                              Save Changes
                          </button>
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
      <label class="text-sm font-semibold text-gray-600" for="catering-service">Hair and Makeup Artist. *</label>
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
      <label class="text-sm font-semibold text-gray-600" for="catering-service">Event Host. *</label>
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
      <label class="text-sm font-semibold text-gray-600" for="catering-service">Sound and Lighting. *</label>
      <select v-model="selectedAudioVisual" id="catering-service" class="w-80 h-9 m-3 ml-[97px] rounded-lg text-sm font-bold bg-[#fefff6]" :disabled="!editVendorDetails">
        <option value = "audiovisual1">Jadiel Walton</option>
        <option value = "audiovisual2">Korbyn Norton</option>
        <option value = "audiovisual3">Nico Shepherd</option>
      </select>
      <span class="ml-5 text-sm font-semibold font-amaticRegular text-blue-700">( {{ getAudioVisualPrice() }} )</span>
    </div>
  </div>

  <div class="flex mx-5 mt-3">
    <div class="row text-start">
      <label class="text-sm font-semibold text-gray-600" for="catering-service">Music and Entertainment. *</label>
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
      <label class="text-sm font-semibold text-gray-600" for="catering-service">Transportation. *</label>
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
      <label class="text-sm font-semibold text-gray-600" for="catering-service">Invitations and Stationery. *</label>
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
      <label class="text-sm font-semibold text-gray-600" for="catering-service">Favors and Gifts. *</label>
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



 <!-- Add these modals to your template section, right before the closing </template> tag -->

<!-- Inclusion Modal for Selecting Supplier Type -->
<div v-if="showInclusionModal && selectedInclusionType === 'supplier'" @click.self="closeInclusionModal" class="fixed inset-0 bg-black bg-opacity-50 flex justify-center items-center z-50">
  <div class="bg-white w-[500px] p-6 rounded-lg shadow-lg">
    <div class="flex justify-between items-center mb-4">
      <h2 class="text-lg font-semibold">Select Supplier Type</h2>
      <button type="button" @click="closeInclusionModal" class="text-red-500 hover:text-red-700">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
        </svg>
      </button>
    </div>
    <div class="grid grid-cols-1 gap-2">
      <button type="button" v-for="serviceType in supplierTypes" :key="serviceType" @click="selectSupplierType(serviceType)" class="w-full text-left px-4 py-2 bg-gray-50 hover:bg-gray-100 rounded-md transition duration-150">
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
      <button type="button" @click="closeSupplierModal" class="text-red-500 hover:text-red-700">
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
          {{ displaySupplierName(supplier) }} - {{ formatPrice(supplier.price) }} php
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
      <button type="button" @click="closeExternalSupplierModal" class="text-red-500 hover:text-red-700">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
        </svg>
      </button>
    </div>
    <div class="space-y-4">
      <div>
        <label class="block text-sm font-medium text-gray-700 text-left">Service Type</label>
        <select v-model="selectedExternalSupplierType" class="w-full p-2 rounded-md border-gray-300 shadow-sm focus:ring focus:ring-blue-200">
          <option value="">Select Service Type</option>
          <option v-for="type in supplierTypes" :key="type" :value="type">{{ type }}</option>
        </select>
      </div>
      <div>
        <label class="block text-sm font-medium text-gray-700 text-left">Supplier Name</label>
        <input type="text" v-model="externalSupplierData.name" class="w-full p-2 rounded-md border-gray-300 shadow-sm focus:ring focus:ring-blue-200">
      </div>
      <div>
        <label class="block text-sm font-medium text-gray-700 text-left">Contact</label>
        <input type="text" v-model="externalSupplierData.contact" class="w-full p-2 rounded-md border-gray-300 shadow-sm focus:ring focus:ring-blue-200">
      </div>
      <div>
        <label class="block text-sm font-medium text-gray-700 text-left">Price</label>
        <input type="number" v-model="externalSupplierData.price" class="w-full p-2 rounded-md border-gray-300 shadow-sm focus:ring focus:ring-blue-200">
      </div>
      <div>
        <label class="block text-sm font-medium text-gray-700 text-left">Remarks</label>
        <textarea v-model="externalSupplierData.remarks" class="w-full p-2 rounded-md border-gray-300 shadow-sm focus:ring focus:ring-blue-200" rows="3"></textarea>
      </div>
    </div>
    <div class="flex justify-end mt-4 space-x-2">
      <button type="button" @click="closeExternalSupplierModal" class="px-4 py-2 text-gray-600 hover:text-gray-800">Cancel</button>
      <button type="button" @click="addExternalSupplier" class="bg-blue-500 text-white px-4 py-2 rounded-md hover:bg-blue-600">Add External Supplier</button>
    </div>
  </div>
</div>

<!-- Inclusion Modal for Selecting Venue -->
<div v-if="showInclusionModal && selectedInclusionType === 'venue'" @click.self="closeInclusionModal" class="fixed inset-0 bg-black bg-opacity-50 flex justify-center items-center z-50">
  <div class="bg-white w-[500px] p-6 rounded-lg shadow-lg">
    <div class="flex justify-between items-center mb-4">
      <h2 class="text-lg font-semibold">Select Venue</h2>
      <button type="button" @click="closeInclusionModal" class="text-red-500 hover:text-red-700">
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

<!-- Inclusion Modal for Selecting Outfit -->
<div v-if="showInclusionModal && selectedInclusionType === 'outfit'" @click.self="closeInclusionModal" class="fixed inset-0 bg-black bg-opacity-50 flex justify-center items-center z-50">
  <div class="bg-white w-[500px] p-6 rounded-lg shadow-lg">
    <div class="flex justify-between items-center mb-4">
      <h2 class="text-lg font-semibold">Select Outfit</h2>
      <button @click="closeInclusionModal" class="text-red-500 hover:text-red-700">
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
        @click="outfitSelectionMode === 'package' ? addSelectedOutfitPackage() : addSelectedIndividualOutfit()" 
        class="bg-blue-500 text-white px-4 py-2 rounded-md hover:bg-blue-600"
      >
        Add
      </button>
    </div>
  </div>
</div>

<!-- Inclusion Modal for Selecting Additional Service -->
<div v-if="showInclusionModal && selectedInclusionType === 'service'" @click.self="closeInclusionModal" class="fixed inset-0 bg-black bg-opacity-50 flex justify-center items-center z-50">
  <div class="bg-white w-[500px] p-6 rounded-lg shadow-lg">
    <div class="flex justify-between items-center mb-4">
      <h2 class="text-lg font-semibold">{{ isEditingInclusion ? 'Edit' : 'Select' }} Additional Service</h2>
      <button type="button" @click="closeInclusionModal" class="text-red-500 hover:text-red-700">
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
          {{ service.add_service_name }} - ₱{{ service.add_service_price ? formatPrice(service.add_service_price) : '0.00' }}
        </option>
      </select>
    </div>
    <div class="flex justify-center mt-4">
      <button type="button" @click="addSelectedService" class="bg-blue-500 text-white px-4 py-2 rounded-md hover:bg-blue-600">
        {{ isEditingInclusion ? 'Save Changes' : 'Add' }}
      </button>
    </div>
  </div>
</div>

<!-- Confirmation Modal for Removing Inclusions -->
<div v-if="showRemoveConfirmationModal" @click.self="closeRemoveConfirmationModal" class="fixed inset-0 bg-black bg-opacity-50 flex justify-center items-center z-50">
  <div class="bg-white w-[400px] p-6 rounded-lg shadow-lg">
    <div class="flex flex-col items-center mb-4">
      <h2 class="text-lg font-semibold mb-4">Remove Confirmation</h2>
      <p class="text-gray-600 mb-6">
        Are you sure you want to remove this 
        {{ inclusionToRemove && inclusionToRemove.type === 'outfits' ? 'outfit' : 
           inclusionToRemove && inclusionToRemove.type === 'services' ? 'service' : 
           inclusionToRemove && inclusionToRemove.type === 'suppliers' ? 'supplier' : 
           inclusionToRemove && inclusionToRemove.type === 'venues' ? 'venue' : 'item' }}?
      </p>
      <div class="flex space-x-4">
        <button @click="closeRemoveConfirmationModal" class="px-4 py-2 bg-gray-300 text-gray-700 rounded hover:bg-gray-400">
          Cancel
        </button>
        <button @click="confirmRemoveInclusion" class="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600">
          Remove
        </button>
      </div>
    </div>
  </div>
</div>

  <!-- Edit Inclusion Modal -->
  <div v-if="showEditInclusionModal" class="fixed inset-0 bg-black bg-opacity-50 flex justify-center items-center z-50">
    <div class="bg-white w-[500px] p-6 rounded-lg shadow-lg">
      <div class="flex justify-between items-center mb-4">
        <h2 class="text-lg font-semibold">Edit Inclusion</h2>
        <button @click="closeEditInclusionModal" class="text-red-500 hover:text-red-700 text-2xl">&times;</button>
      </div>

      <div class="mb-4">
        <label class="block text-sm font-medium text-gray-700 mb-2">Type</label>
        <input v-model="editingInclusion.type" class="w-full p-2 border rounded" disabled>
      </div>

      <!-- Dynamic fields based on inclusion type -->
      <div v-if="editingInclusion.type === 'suppliers'" class="mb-4">
        <label class="block text-sm font-medium text-gray-700 mb-2">Supplier Name</label>
        <input v-model="editingInclusion.data.supplier_name" class="w-full p-2 border rounded">
        <label class="block text-sm font-medium text-gray-700 mt-2 mb-2">Contact</label>
        <input v-model="editingInclusion.data.contact" class="w-full p-2 border rounded">
        <label class="block text-sm font-medium text-gray-700 mt-2 mb-2">Price</label>
        <input v-model="editingInclusion.data.price" type="number" class="w-full p-2 border rounded">
        <label class="block text-sm font-medium text-gray-700 mt-2 mb-2">Remarks</label>
        <textarea v-model="editingInclusion.data.remarks" class="w-full p-2 border rounded" rows="3"></textarea>
      </div>

      <div v-if="editingInclusion.type === 'venues'" class="mb-4">
        <label class="block text-sm font-medium text-gray-700 mb-2">Venue Name</label>
        <input v-model="editingInclusion.data.venue_name" class="w-full p-2 border rounded">
        <label class="block text-sm font-medium text-gray-700 mt-2 mb-2">Location</label>
        <input v-model="editingInclusion.data.location" class="w-full p-2 border rounded">
        <label class="block text-sm font-medium text-gray-700 mt-2 mb-2">Price</label>
        <input v-model="editingInclusion.data.price" type="number" class="w-full p-2 border rounded">
      </div>

      <div v-if="editingInclusion.type === 'outfits'" class="mb-4">
        <label class="block text-sm font-medium text-gray-700 mb-2">Outfit Name</label>
        <input v-model="editingInclusion.data.outfit_name" class="w-full p-2 border rounded">
        <label class="block text-sm font-medium text-gray-700 mt-2 mb-2">Size</label>
        <input v-model="editingInclusion.data.size" class="w-full p-2 border rounded">
        <label class="block text-sm font-medium text-gray-700 mt-2 mb-2">Price</label>
        <input v-model="editingInclusion.data.price" type="number" class="w-full p-2 border rounded">
      </div>

      <div v-if="editingInclusion.type === 'services'" class="mb-4">
        <label class="block text-sm font-medium text-gray-700 mb-2">Service Name</label>
        <input v-model="editingInclusion.data.service_name" class="w-full p-2 border rounded">
        <label class="block text-sm font-medium text-gray-700 mt-2 mb-2">Description</label>
        <textarea v-model="editingInclusion.data.description" class="w-full p-2 border rounded" rows="3"></textarea>
        <label class="block text-sm font-medium text-gray-700 mt-2 mb-2">Price</label>
        <input v-model="editingInclusion.data.price" type="number" class="w-full p-2 border rounded">
      </div>

      <div class="flex justify-end space-x-2 mt-6">
        <button @click="closeEditInclusionModal" class="px-4 py-2 bg-gray-200 text-gray-800 rounded-md hover:bg-gray-300">
          Cancel
        </button>
        <button @click="saveEditedInclusion" class="px-4 py-2 bg-blue-500 text-white rounded-md hover:bg-blue-600">
          Save Changes
        </button>
      </div>
    </div>
  </div>

  <!-- Status Update Confirmation Modal -->
  <div v-if="showStatusConfirmationModal" @click.self="closeStatusConfirmationModal" class="fixed inset-0 bg-gray-800 bg-opacity-50 overflow-y-auto flex justify-center items-center z-50">
    <div class="bg-white p-5 rounded-lg shadow-lg w-[400px]">
      <div class="flex flex-col items-center">
        <h2 class="text-xl font-semibold mb-4">Confirm Status Change</h2>
        <p class="mb-6 text-center">Are you sure you want to move this event to Upcoming Events?</p>
        <div class="flex space-x-4">
          <button 
            @click="closeStatusConfirmationModal" 
            class="bg-gray-500 text-white px-4 py-2 rounded hover:bg-opacity-90">
            Cancel
          </button>
          <button 
            @click="confirmUpdateStatus" 
            class="bg-blue-500 text-white px-4 py-2 rounded hover:bg-opacity-90">
            Yes
          </button>
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
      showStatusConfirmationModal: false,
      eventToUpdate: null,
      showRemoveConfirmationModal: false,
      inclusionToRemove: {
        type: '',
        index: -1
      },
      showTable: 'wishlist',
      currentWishlistPage: 1,
      rowsPerWishlistPage: 5,
      currentPage: 1,
      rowsPerPage: 4,
      currentFinishedPage: 1,
      rowsPerFinishedPage: 5,
      selectedIndex: null,
      isEditingInclusion: false,
      editingInclusionIndex: -1,
      selectedService: null,
      additionalServices: [],
      wishlist: [],
      upcomingEvents: [],
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
      },
      event: null,
      upcomingEventDetailsModal: false,
      enableEditDetails: false,
      editVendorDetails: false,
      editServiceDetails: false,
      additionalCapacity: 0,
      showCapacityModal: false,
      capacityList: [
        { capacity: '50-100', charges: 1000, unit: 'per head' },
        { capacity: '101-200', charges: 900, unit: 'per head' },
        { capacity: '201-300', charges: 800, unit: 'per head' }
      ],

      bookedEvents: [],
      wishlist: [],
      inclusions: [],
      additionalServices: [],

      showEventModal: false,
      showWishlistModal: false,
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
      outfitSelectionMode: 'package', // 'package' or 'individual'
      externalSupplierData: {
        name: '',
        contact: '',
        price: 0,
        remarks: ''
      },
      selectedExternalSupplierType: '',
      availableSuppliers: [],
      venues: [],
      gownPackages: [],
      outfits: [],
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


      showInclusionModal: false,
      selectedInclusionType: null,
      showSupplierModal: false,
      showExternalSupplierModal: false,
      selectedSupplierType: '',
      outfitSelectionMode: 'package',
      supplierTypes: ['Catering',
        'Photographer',
        'Videographer',
        'Entertainment',
        'Sound and Lighting',
        'Transportation',
        'Host',
        'Invitations',
        'Favors and Gifts',
        'Hair Stylist',
        'Makeup Artist',],
      externalSupplierData: {
        name: '',
        contact: '',
        price: 0,
        remarks: ''
      },
      selectedExternalSupplierType: '',

      showEditInclusionModal: false,
      editingInclusion: {
        type: '',
        index: -1,
        data: {}
      },
  

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
    paginatedUpcomingEvents() {
      console.log('Paginating upcoming events:', this.upcomingEvents);
      const start = (this.currentPage - 1) * this.rowsPerPage;
      const end = start + this.rowsPerPage;
      return this.upcomingEvents.slice(start, end);
    },

    totalPages() {
      return Math.ceil((this.upcomingEvents?.length || 0) / this.rowsPerPage);
    },

    paginatedWishlist() {
      const start = (this.currentWishlistPage - 1) * this.rowsPerWishlistPage;
      const end = start + this.rowsPerWishlistPage;
      return this.wishlist.slice(start, end);
    },

    totalWishlistPages() {
      return Math.ceil((this.wishlist?.length || 0) / this.rowsPerWishlistPage);
    },

    totalFinishedPages() {
      return Math.ceil(this.finishedEvents.length / this.rowsPerFinishedPage);
    },
    paginatedFinishedEvents() {
      const start = (this.currentFinishedPage - 1) * this.rowsPerFinishedPage;
      const end = start + this.rowsPerFinishedPage;
      return this.finishedEvents.slice(start, end);
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
    allInclusions() {
        const inclusions = [];
        const uniqueItems = new Map();

        // Add suppliers
        if (this.selectedEvent && Array.isArray(this.selectedEvent.suppliers)) {
          this.selectedEvent.suppliers.forEach(supplier => {
            const serviceType = supplier.service_type || supplier.service;
            const key = `${supplier.supplier_id}_${serviceType}`;
            if (!uniqueItems.has(key)) {
              uniqueItems.set(key, {
                name: `${this.displaySupplierName(supplier)} (${serviceType})`,
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
  },
    filteredAdditionalServices() {
      if (!this.additionalServices || !this.selectedEvent || !this.selectedEvent.services) {
        return this.additionalServices || [];
      }
      // When editing, include the currently edited service
      return this.additionalServices.filter(service => {
        if (this.isEditingInclusion && this.editingInclusionIndex >= 0) {
          // Don't filter out the service being edited
          return !this.selectedEvent.services.some((s, index) => 
            index !== this.editingInclusionIndex && s.add_service_id === service.add_service_id
          );
        }
        // Normal filtering for adding new services
        return !this.selectedEvent.services.some(s => s.add_service_id === service.add_service_id);
      });
    }
  },

  methods: {
    formatPrice(price) {
      if (!price && price !== 0) return '0.00';
      const numPrice = Number(price) || 0;
      return numPrice.toLocaleString('en-PH', {
        minimumFractionDigits: 2,
        maximumFractionDigits: 2
      });
    },
    updateAdditionalCapacity(value) {
      // Remove any non-numeric characters except decimal point
      const cleanValue = value.replace(/[^\d]/g, '');
      
      // Convert to number and ensure it's positive
      const numValue = parseInt(cleanValue) || 0;
      this.additionalCapacity = Math.max(0, numValue);
    },
    
    filteredSuppliers(serviceType) {
      if (!this.availableSuppliers || !serviceType) {
        console.log('Cannot filter suppliers: missing availableSuppliers or serviceType');
        return [];
      }
      
      console.log('Filtering suppliers for service type:', serviceType);
      console.log('Available suppliers count:', this.availableSuppliers.length);
      
      // Log a few suppliers for debugging
      if (this.availableSuppliers.length > 0) {
        console.log('Sample supplier data:', this.availableSuppliers[0]);
      }
      
      const filtered = this.availableSuppliers.filter(supplier => {
        const matchesServiceType = 
          (supplier.service_type && supplier.service_type.toLowerCase() === serviceType.toLowerCase()) || 
          (supplier.supplier_type && supplier.supplier_type.toLowerCase() === serviceType.toLowerCase()) ||
          (supplier.service && supplier.service.toLowerCase() === serviceType.toLowerCase());
        
        if (matchesServiceType) {
          console.log('Matched supplier:', supplier);
        }
        
        return matchesServiceType;
      });
      
      console.log('Filtered suppliers count:', filtered.length);
      return filtered;
    },
    
    async fetchAdditionalServices() {
      try {
        console.log('Fetching additional services...');
        const token = localStorage.getItem('access_token');
        if (!token) {
          console.error('No access token found');
          return;
        }

        const response = await axios.get('http://127.0.0.1:5000/additional-services', {
          headers: { 
            'Authorization': `Bearer ${token}`,
            'Content-Type': 'application/json'
          }
        });

        // Store the raw response data directly
        this.additionalServices = response.data;
        console.log('Fetched additional services:', this.additionalServices);
      } catch (error) {
        console.error('Error fetching additional services:', error);
        if (error.response) {
          console.error('Error response:', error.response.data);
          console.error('Error status:', error.response.status);
        }
        this.additionalServices = []; // Reset on error
      }
    },

    async fetchBookedWishlist() {
      try {
        const token = localStorage.getItem('access_token');
        if (!token) {
          console.error('No access token found');
          return;
        }

        const response = await fetch('http://127.0.0.1:5000/booked-wishlist', {
          headers: {
            'Authorization': `Bearer ${token}`,
            'Content-Type': 'application/json'
          },
          credentials: 'include'
        });

        const data = await response.json();
        console.log('Raw response:', data);

        // Process all events
        const processedEvents = data.map(event => ({
            ...event,
          venue_name: event.venue_name || null,
          outfits: (event.outfits || []).map(outfit => ({
            wishlist_outfit_id: outfit.wishlist_outfit_id,
              outfit_id: outfit.outfit_id,
              outfit_name: outfit.outfit_name,
            price: parseFloat(outfit.price || 0),
              outfit_type: outfit.outfit_type,
            status: outfit.status || 'Pending'
          }))
        }));

        // Separate events based on status
        this.wishlist = processedEvents.filter(event => event.status === 'Wishlist');
        this.upcomingEvents = processedEvents.filter(event => event.status === 'Upcoming');

        console.log('Processed wishlist:', this.wishlist);
        console.log('Processed upcoming events:', this.upcomingEvents);
      } catch (error) {
        console.error('Error fetching data:', error);
        this.wishlist = [];
        this.upcomingEvents = [];
      }
    },

    async fetchAvailableSuppliers() {
      try {
        const token = localStorage.getItem('access_token');
        if (!token) {
          console.error('No access token found');
          return;
        }
        
        console.log('Fetching available suppliers...');
        const response = await axios.get('http://127.0.0.1:5000/available-suppliers', {
          headers: {
            'Authorization': `Bearer ${token}`,
            'Content-Type': 'application/json'
          }
        });
        
        console.log('Raw supplier data:', response.data);
        
        if (!response.data || !Array.isArray(response.data)) {
          console.error('Invalid supplier data format:', response.data);
          return;
        }
        
        this.availableSuppliers = response.data.map(supplier => ({
          ...supplier,
          supplier_name: supplier.supplier_name || `${supplier.firstname || ''} ${supplier.lastname || ''}`.trim(),
          service_type: supplier.service_type || supplier.supplier_type
        }));
        
        console.log('Processed suppliers:', this.availableSuppliers);
        
        // Log a few suppliers for debugging
        if (this.availableSuppliers.length > 0) {
          console.log('Sample supplier:', this.availableSuppliers[0]);
        }
      } catch (error) {
        console.error('Error fetching available suppliers:', error);
        if (error.response) {
          console.error('Error response:', error.response.data);
        }
      }
    },

    async fetchAvailableVenues() {
      try {
        const token = localStorage.getItem('access_token');
        if (!token) {
          console.error('No access token found');
          return;
        }
        
        const response = await axios.get('http://127.0.0.1:5000/available-venues', {
          headers: {
            'Authorization': `Bearer ${token}`,
            'Content-Type': 'application/json'
          }
        });
        
        console.log('Raw venue data:', response.data);
        this.venues = response.data;
        console.log('Processed venues:', this.venues);
      } catch (error) {
        console.error('Error fetching available venues:', error);
        this.venues = []; // Reset on error
      }
    },

    async fetchAvailableGownPackages() {
      try {
        const token = localStorage.getItem('access_token');
        if (!token) {
          console.error('No access token found');
          return;
        }
        
        const response = await axios.get('http://127.0.0.1:5000/available-gown-packages', {
          headers: {
            'Authorization': `Bearer ${token}`,
            'Content-Type': 'application/json'
          }
        });
        
        console.log('Raw outfit data:', response.data);
        this.gownPackages = response.data;
        console.log('Processed outfits:', this.gownPackages);
      } catch (error) {
        console.error('Error fetching available gown packages:', error);
        this.gownPackages = []; // Reset on error
      }
    },

    async fetchOutfits() {
      try {
        const token = localStorage.getItem('access_token');
        if (!token) {
          console.error('No access token found');
          return;
        }

        const response = await axios.get('http://127.0.0.1:5000/outfits', {
          headers: { 
            'Authorization': `Bearer ${token}`,
            'Content-Type': 'application/json'
          }
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
        
        console.log('Processed outfits:', this.outfits);
      } catch (error) {
        console.error('Error fetching outfits:', error);
        this.outfits = []; // Reset on error
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
  },

  updatePricing() {
      console.log(`Selected capacity: ${this.selectedCapacity}`);
    },
    calculateAdditionalCharges() {
      if (!this.additionalCapacity || !this.selectedEvent) return 0;
      
      try {
        const chargePerUnit = parseFloat(this.selectedEvent.additional_capacity_charges) || 0;
        const chargeUnit = parseInt(this.selectedEvent.charge_unit) || 1;
        
        if (chargePerUnit <= 0 || chargeUnit <= 0) return 0;
        
        const units = Math.ceil(this.additionalCapacity / chargeUnit);
        return units * chargePerUnit;
      } catch (error) {
        console.error('Error calculating additional charges:', error);
        return 0;
      }
    },
    addCapacity() {
      // Check if selectedEvent exists
      if (!this.selectedEvent) {
        console.error('No event selected');
        alert('Please select an event first.');
        return;
      }

      // Validate additional capacity
      if (!this.additionalCapacity || this.additionalCapacity <= 0) {
        alert('Please enter a valid number of additional persons.');
        return;
      }
      
      try {
        const totalCharges = this.calculateAdditionalCharges();
        if (totalCharges > 0) {
          // Ensure we have valid numbers
          const currentCapacity = parseInt(this.selectedEvent.capacity) || 0;
          const additionalCapacity = parseInt(this.additionalCapacity) || 0;
          const currentPrice = parseFloat(this.selectedEvent.total_price) || 0;
          
          // Update total price and capacity
          this.selectedEvent.total_price = (currentPrice + totalCharges).toFixed(2);
          this.selectedEvent.capacity = currentCapacity + additionalCapacity;
          
          // Reset modal
          this.closeCapacityModal();
          
          // Show success message
          alert('Additional capacity added successfully!');
        }
      } catch (error) {
        console.error('Error adding capacity:', error);
        alert('An error occurred while adding capacity. Please try again.');
      }
    },

    addSelectedSupplier() {
      if (!this.selectedSupplier) {
        console.error('No supplier selected');
        return;
      }

      if (this.isEditingInclusion) {
        // Update existing supplier
        this.selectedEvent.suppliers[this.editingInclusionIndex] = { ...this.selectedSupplier };
        this.isEditingInclusion = false;
        this.editingInclusionIndex = -1;
      } else {
        // Add new supplier
        if (!this.selectedEvent.suppliers) {
          this.selectedEvent.suppliers = [];
        }
        // Add the supplier with a default status of 'Pending'
      this.selectedEvent.suppliers.push({
          ...this.selectedSupplier,
          status: 'Pending'
        });
      }

      // Reset and close modal
      this.selectedSupplier = null;
      this.showInclusionModal = false;
      this.selectedInclusionType = '';
  },

  addSelectedVenue() {
      if (!this.selectedVenue) {
        console.error('No venue selected');
        return;
      }

      if (this.isEditingInclusion) {
        // Update existing venue
        this.selectedEvent.venues[this.editingInclusionIndex] = { ...this.selectedVenue };
        this.isEditingInclusion = false;
        this.editingInclusionIndex = -1;
        } else {
        // Add new venue
        if (!this.selectedEvent.venues) {
          this.selectedEvent.venues = [];
        }
        this.selectedEvent.venues.push({ ...this.selectedVenue });
      }

      // Reset and close modal
      this.selectedVenue = null;
      this.showInclusionModal = false;
      this.selectedInclusionType = '';
    },

  addSelectedOutfit() {
      if (!this.selectedOutfit) {
        console.error('No outfit selected');
        return;
      }

      // Initialize outfits array if it doesn't exist
    if (!this.selectedEvent.outfits) {
      this.selectedEvent.outfits = [];
    }
    
      // Check if outfit already exists
      const hasExistingOutfit = this.selectedEvent.outfits.some(outfit => {
        if (this.outfitSelectionMode === 'package') {
          return outfit.gown_package_id === this.selectedOutfit.gown_package_id;
      } else {
          return outfit.outfit_id === this.selectedOutfit.outfit_id;
      }
      });

      if (hasExistingOutfit) {
        alert('This outfit is already added.');
    this.closeInclusionModal();
        return;
      }

      // Create outfit data based on selection mode
      const outfitData = this.outfitSelectionMode === 'package' ? {
        type: 'package',
        gown_package_id: this.selectedOutfit.gown_package_id,
        gown_package_name: this.selectedOutfit.gown_package_name,
        gown_package_price: parseFloat(this.selectedOutfit.gown_package_price || 0),
        status: 'Pending',
        is_initialized: false
      } : {
        type: 'individual',
        outfit_id: this.selectedOutfit.outfit_id,
        outfit_name: this.selectedOutfit.outfit_name,
        outfit_type: this.selectedOutfit.outfit_type,
        size: this.selectedOutfit.size,
        rent_price: parseFloat(this.selectedOutfit.rent_price || 0),
        status: 'Pending',
        is_initialized: false
      };

      // Add the outfit
      this.selectedEvent.outfits.push(outfitData);

      // Reset and close modal
      this.selectedOutfit = null;
      this.showInclusionModal = false;
      this.selectedInclusionType = '';
      this.outfitSelectionMode = 'package'; // Reset to default mode
  },

  addSelectedService() {
      if (!this.selectedService) {
        console.error('No service selected');
        return;
      }

      // Initialize services array if it doesn't exist
      if (!this.selectedEvent.services) {
        this.selectedEvent.services = [];
      }

      // Check if service already exists
      const hasExistingService = this.selectedEvent.services.some(item => 
        item.add_service_id === this.selectedService.add_service_id
      );

      if (hasExistingService && !this.isEditingInclusion) {
        alert('This service is already added.');
        return;
      }

      const serviceData = {
        add_service_id: this.selectedService.add_service_id,
        add_service_name: this.selectedService.add_service_name,
        add_service_description: this.selectedService.add_service_description,
        add_service_price: parseFloat(this.selectedService.add_service_price || 0)
      };

      if (this.isEditingInclusion) {
        // Update existing service
        this.selectedEvent.services[this.editingInclusionIndex] = serviceData;
        this.isEditingInclusion = false;
        this.editingInclusionIndex = -1;
      } else {
        // Add new service
      this.selectedEvent.services.push(serviceData);
      }

      this.selectedService = null;
      this.closeInclusionModal();
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

  removeOutfit(index) {
    if (this.selectedEvent.outfits && this.selectedEvent.outfits.length > index) {
      this.selectedEvent.outfits.splice(index, 1);
      this.updatePricing();
    }
  },

  openCapacityModal() {
    this.showCapacityModal = true;
  },

  closeCapacityModal() {
    this.showCapacityModal = false;
    this.additionalCapacity = 0;
  },

  addCapacity() {
    if (!this.newCapacity.capacity) {
      alert('Please enter capacity range.');
      return;
    }
      
    if (!this.newCapacity.charges) {
      alert('Please enter charges.');
      return;
    }
      
    this.capacityList.push({
      capacity: this.newCapacity.capacity,
      charges: parseFloat(this.newCapacity.charges),
      unit: this.newCapacity.unit
    });
      
    this.closeCapacityModal();
  },

  closeOutfitModal() {
    this.showOutfitModal = false; // Assuming you have a modal state for outfits
  },

  removeCapacity(index) {
    this.capacityList.splice(index, 1);
  },
  directToOnsiteBooking(){
      this.$router.push('/add-wishlist');
    },
  addSelectedIndividualOutfit() {
      if (this.selectedOutfit) {
        // Check if outfit already exists
        const hasExistingOutfit = this.selectedEvent.outfits.some(outfit => 
          outfit.outfit_id === this.selectedOutfit.outfit_id
        );

        if (hasExistingOutfit) {
          alert('This outfit is already added.');
        } else {
          this.selectedEvent.outfits.push({
            type: 'individual',
            outfit_id: this.selectedOutfit.outfit_id,
            outfit_name: this.selectedOutfit.outfit_name,
            outfit_type: this.selectedOutfit.outfit_type,
            size: this.selectedOutfit.size,
            rent_price: this.selectedOutfit.rent_price
          });
          this.closeOutfitModal();
        }
      } else {
        alert('Please select an outfit.');
      }
    },

    addSelectedOutfitPackage() {
      if (!this.selectedOutfit) {
        alert('Please select an outfit package.');
        return;
      }

      // Initialize outfits array if it doesn't exist
      if (!this.selectedEvent.outfits) {
        this.selectedEvent.outfits = [];
      }

      // Check if package already exists
        const hasExistingPackage = this.selectedEvent.outfits.some(outfit => 
        outfit.type === 'package' && outfit.gown_package_id === this.selectedOutfit.gown_package_id
        );

        if (hasExistingPackage) {
          alert('This outfit package is already added.');
        return;
      }

      // Add the package outfit
          this.selectedEvent.outfits.push({
            type: 'package',
            gown_package_id: this.selectedOutfit.gown_package_id,
            gown_package_name: this.selectedOutfit.gown_package_name,
        gown_package_price: parseFloat(this.selectedOutfit.gown_package_price || 0),
        status: 'Pending'
          });

          this.closeOutfitModal();
    },

    addExternalSupplier() {
      if (!this.selectedExternalSupplierType) {
        alert('Please select a service type.');
        return;
      }
      
      if (!this.externalSupplierData.name) {
        alert('Please enter supplier name.');
        return;
      }
      
      this.selectedEvent.suppliers.push({
        type: 'external',
        service: this.selectedExternalSupplierType,
        external_supplier_name: this.externalSupplierData.name,
        external_supplier_contact: this.externalSupplierData.contact,
        price: parseFloat(this.externalSupplierData.price) || 0,
        remarks: this.externalSupplierData.remarks
      });
      
      this.closeExternalSupplierModal();
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

    openInclusionModal(type) {
      this.selectedInclusionType = type;
      this.showInclusionModal = true;
      if (type === 'supplier') {
        this.showSupplierModal = true;
      } else if (type === 'venue') {
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
      this.selectedService = null;
      this.selectedVenue = null;
      this.selectedOutfit = null;
    },
    openWishlistModal(event) {
      console.log('Opening wishlist modal for event:', event);
      
      // Create a deep copy of the event to avoid modifying the original
      this.selectedEvent = JSON.parse(JSON.stringify({
        ...event,
        suppliers: event.suppliers || [],
        services: event.services || [],
        outfits: event.outfits || [],
        venues: event.venues || [],
        gown_package_name: event.gown_package_name || '',
        gown_package_price: event.gown_package_price || 0,
        firstname: event.firstname || '',
        lastname: event.lastname || '',
        contactnumber: event.contactnumber || ''
      }));

      // If there's a gown package but no outfits, initialize the outfits array
      if (event.gown_package_id && (!this.selectedEvent.outfits || this.selectedEvent.outfits.length === 0)) {
        this.selectedEvent.outfits = [{
          type: 'outfit_package',
          gown_package_id: event.gown_package_id,
          gown_package_name: event.gown_package_name,
          gown_package_price: event.gown_package_price,
          status: 'Pending',
          is_initialized: true
        }];
      }

      // Add any additional outfits from the event
      if (event.outfits && event.outfits.length > 0) {
        const additionalOutfits = event.outfits.map(outfit => ({
          ...outfit,
          is_initialized: outfit.is_initialized || false
        }));
        this.selectedEvent.outfits = [...this.selectedEvent.outfits, ...additionalOutfits];
      }

      // Make sure services array is properly initialized
      if (!this.selectedEvent.services || !Array.isArray(this.selectedEvent.services)) {
        this.selectedEvent.services = [];
      }

      // Add any additional services from the event
      if (event.services && event.services.length > 0) {
        const additionalServices = event.services.map(service => ({
          ...service,
          is_initialized: service.is_initialized || false
        }));
        this.selectedEvent.services = [...this.selectedEvent.services, ...additionalServices];
      }

      console.log('Selected event for editing:', this.selectedEvent);
      console.log('Outfits array:', this.selectedEvent.outfits);
      console.log('Services array:', this.selectedEvent.services);
      this.showWishlistModal = true;
    },

    closeWishlistModal() {
      this.showWishlistModal = false;
    },
    removeInclusion(type, index) {
      if (!this.selectedEvent || !this.selectedEvent[type]) {
        console.error('Invalid event or type:', type);
        return;
      }

      if (index < 0 || index >= this.selectedEvent[type].length) {
        console.error('Invalid index:', index);
        return;
      }

      const item = this.selectedEvent[type][index];
      
      // Don't allow removal of initialized outfits
      if (type === 'outfits' && item.is_initialized) {
        alert('Cannot remove initialized outfits');
        return;
      }

      // Store the item to be removed
      this.inclusionToRemove = {
        type,
        index,
        item
      };
      
      // Show confirmation modal
      this.showRemoveConfirmationModal = true;
    },

    confirmRemoveInclusion() {
      if (!this.inclusionToRemove) {
        console.error('No inclusion to remove');
        return;
      }

      const { type, index } = this.inclusionToRemove;
      
      // Remove from local state
      this.selectedEvent[type].splice(index, 1);
      
      // Close the confirmation modal
      this.showRemoveConfirmationModal = false;
      this.inclusionToRemove = null;
    },

    closeRemoveConfirmationModal() {
      this.showRemoveConfirmationModal = false;
      this.inclusionToRemove = null;
    },
    editInclusion(type, index) {
      const inclusionTypes = {
        'suppliers': 'supplier',
        'venues': 'venue',
        'outfits': 'outfit',
        'services': 'service'
      };

      const modalType = inclusionTypes[type.toLowerCase()];
      if (!modalType) {
        console.error('Invalid inclusion type:', type);
        return;
      }

      // Initialize arrays if they don't exist
      if (!this.selectedEvent[type]) {
        this.selectedEvent[type] = [];
        console.error(`${type} array is not initialized`);
        return;
      }

      const data = this.selectedEvent[type][index];
      if (!data) {
        console.error('No data found for index:', index);
        return;
      }

      // Set up editing state
      this.isEditingInclusion = true;
      this.editingInclusionIndex = index;
      this.selectedInclusionType = modalType;

      // Pre-fill the form based on the inclusion type
      if (modalType === 'supplier') {
        this.selectedSupplier = { ...data };
      } else if (modalType === 'venue') {
        this.selectedVenue = { ...data };
      } else if (modalType === 'outfit') {
        this.selectedOutfit = { ...data };
      } else if (modalType === 'service') {
        this.selectedService = { ...data };
      }

      // Open the inclusion modal
      this.showInclusionModal = true;
    },

    closeEditInclusionModal() {
      this.showEditInclusionModal = false;
      this.editingInclusion = {
        type: '',
        index: -1,
        data: {}
      };
    },

    saveEditedInclusion() {
      const { type, index, data } = this.editingInclusion;
      const inclusionTypes = {
        'suppliers': 'suppliers',
        'venues': 'venues',
        'outfits': 'outfits',
        'services': 'services',
        'additional services': 'services'
      };

      const arrayType = inclusionTypes[type.toLowerCase()];
      if (arrayType && this.selectedEvent[arrayType]) {
        // Update the data in the correct array
        this.selectedEvent[arrayType][index] = { ...data };
        console.log(`Updated ${type} at index ${index}:`, data);
      }

      this.closeEditInclusionModal();
    },

    selectSupplierType(serviceType) {
      this.selectedSupplierType = serviceType;
      this.showInclusionModal = false;
      this.showSupplierModal = true;
    },

      closeSupplierModal() {
        this.showSupplierModal = false;
      },
    displaySupplierName(supplier) {
      console.log('Displaying supplier:', JSON.stringify(supplier));
      if (!supplier) {
        console.log('Supplier is null or undefined');
        return 'Unknown';
      }
      
      if (supplier.name) {
        console.log('Using supplier.name:', supplier.name);
        return supplier.name;
      }
      
      if (supplier.supplier_name) {
        console.log('Using supplier.supplier_name:', supplier.supplier_name);
        return supplier.supplier_name;
      }
      
      const firstName = supplier.firstname || '';
      const lastName = supplier.lastname || '';
      console.log('First name:', firstName, 'Last name:', lastName);
      
      if (firstName || lastName) {
        const fullName = `${firstName} ${lastName}`.trim();
        console.log('Using firstname/lastname:', fullName);
        return fullName;
      }
      
      console.log('No name found in supplier object');
      return 'Unknown Supplier';
    },
    goToInvoice() {
      this.$router.push({ name: 'Invoice' });
    },
    async approveInclusion(type, index) {
      try {
        if (!this.selectedEvent || !this.selectedEvent[type]) {
          throw new Error(`Invalid event or type: ${type}`);
        }

        if (index < 0 || index >= this.selectedEvent[type].length) {
          throw new Error(`Invalid ${type} index: ${index}`);
        }

        const token = localStorage.getItem('access_token');
        if (!token) {
          throw new Error('No authentication token found');
        }

        let item = this.selectedEvent[type][index];
        let endpoint;
        let requestData;
        let method = 'PUT';

        switch (type) {
          case 'outfits': {
            // Check if the wishlist_outfit_id exists
            if (!item.wishlist_outfit_id) {
              // For outfits without IDs, just update locally
              this.selectedEvent.outfits[index].status = 'Approved';
              alert('Outfit approved successfully');
              return;
            } else {
              // Update existing wishlist outfit
              endpoint = `http://127.0.0.1:5000/api/wishlist-outfits/${item.wishlist_outfit_id}`;
              requestData = {
                status: 'Approved'
              };
            }
            break;
          }
          
          case 'services': {
            // Check if the wishlist_service_id exists
            if (!item.wishlist_service_id) {
              // For services without IDs, just update locally
              this.selectedEvent.services[index].status = 'Approved';
              alert('Service approved successfully');
              return;
            } else {
              // Update existing wishlist service
              endpoint = `http://127.0.0.1:5000/api/wishlist-additional-services/${item.wishlist_service_id}`;
              requestData = {
                status: 'Approved'
              };
            }
            break;
          }
          
          case 'suppliers': {
            // Check if the wishlist_supplier_id exists
            if (!item.wishlist_supplier_id) {
              // For suppliers without IDs, just update locally
              this.selectedEvent.suppliers[index].status = 'Approved';
              alert('Supplier approved successfully');
              return;
            } else {
              // Update existing wishlist supplier
              endpoint = `http://127.0.0.1:5000/api/wishlist-suppliers/${item.wishlist_supplier_id}`;
              requestData = {
                status: 'Approved'
              };
            }
            break;
          }
          
          case 'venues': {
            // Check if the wishlist_venue_id exists
            if (!item.wishlist_venue_id) {
              // For venues without IDs, just update locally
              this.selectedEvent.venues[index].status = 'Approved';
              alert('Venue approved successfully');
              return;
            } else {
              // Update existing wishlist venue
              endpoint = `http://127.0.0.1:5000/api/wishlist-venues/${item.wishlist_venue_id}`;
              requestData = {
                status: 'Approved'
              };
            }
            break;
          }
          default:
            throw new Error(`Unsupported inclusion type: ${type}`);
        }

        console.log(`Making API call to: ${endpoint} with method: ${method}`);
        console.log('Request data:', requestData);
        
        const response = await fetch(endpoint, {
          method: method,
          headers: {
            'Authorization': `Bearer ${token}`,
            'Content-Type': 'application/json'
          },
          credentials: 'include',
          body: JSON.stringify(requestData)
        });

        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }

        const result = await response.json();
        
        // If we created a new wishlist item, update the local item with the new ID
        if (method === 'POST' && result.id) {
          const idField = `wishlist_${type.slice(0, -1)}_id`; // Convert 'outfits' to 'wishlist_outfit_id'
          this.selectedEvent[type][index][idField] = result.id;
        }
        
        // Update local state
        this.selectedEvent[type][index].status = 'Approved';
        
        alert('Item approved successfully');
      } catch (error) {
        console.error('Error in approveInclusion:', error);
        alert(`Error approving item: ${error.message}`);
      }
    },

    async updateEventStatus(event) {
      this.eventToUpdate = event;
      this.showStatusConfirmationModal = true;
    },

    closeStatusConfirmationModal() {
      this.showStatusConfirmationModal = false;
      this.eventToUpdate = null;
    },

    async confirmUpdateStatus() {
      try {
        const token = localStorage.getItem('access_token');
        if (!token) {
          throw new Error('No authentication token found');
        }

        const response = await fetch(`http://127.0.0.1:5000/events/${this.eventToUpdate.events_id}/status`, {
          method: 'PUT',
          headers: {
            'Authorization': `Bearer ${token}`,
            'Content-Type': 'application/json'
          },
          credentials: 'include',
          body: JSON.stringify({
            status: 'Upcoming'
          })
        });

        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }

        const result = await response.json();
        
        if (result.success) {
          // Update the event status
          const updatedEvent = { ...this.eventToUpdate, status: 'Upcoming' };
          
          // Remove from wishlist and add to upcoming events
          this.wishlist = this.wishlist.filter(e => e.events_id !== updatedEvent.events_id);
          this.upcomingEvents.push(updatedEvent);
          
          // Show success message
          alert('Event status updated to Upcoming');
          
          // Close the confirmation modal
          this.closeStatusConfirmationModal();
          
          // Reset the event to update
          this.eventToUpdate = null;
        } else {
          throw new Error(result.message || 'Failed to update event status');
        }
      } catch (error) {
        console.error('Error updating event status:', error);
        alert(`Error updating event status: ${error.message}`);
      }
    },

    debugUpcomingEvents() {
      console.log('All wishlist events:', this.wishlist);
      
      // Check if any events have status 'Upcoming'
      const upcomingEvents = this.wishlist.filter(event => event.status === 'Upcoming');
      console.log('Filtered upcoming events:', upcomingEvents);
      
      // Check if status is case sensitive
      const upcomingCaseInsensitive = this.wishlist.filter(event => 
        event.status && event.status.toLowerCase() === 'upcoming'
      );
      console.log('Case insensitive upcoming events:', upcomingCaseInsensitive);
      
      // Check for status field existence
      const eventsWithStatus = this.wishlist.filter(event => event.status);
      console.log('Events with status field:', eventsWithStatus);
      
      // Log all unique status values
      const uniqueStatuses = [...new Set(this.wishlist.map(event => event.status))];
      console.log('Unique status values:', uniqueStatuses);
    },

    async fetchUpcomingEvents() {
      try {
        const token = localStorage.getItem('access_token');
        if (!token) {
          console.error('No access token found');
          return;
        }

        const response = await fetch('http://127.0.0.1:5000/upcoming-events', {
          headers: {
            'Authorization': `Bearer ${token}`,
            'Content-Type': 'application/json'
          },
          credentials: 'include'
        });

        const data = await response.json();
        console.log('Raw upcoming events:', data);

        this.upcomingEvents = data.map(event => ({
          ...event,
          venue_name: event.venue_name || null,
          status: 'Upcoming'
        }));
        
        console.log('Processed upcoming events:', this.upcomingEvents);
      } catch (error) {
        console.error('Error fetching upcoming events:', error);
        this.upcomingEvents = [];
      }
    },
    debugServices() {
      console.log('Debug Services:');
      console.log('selectedEvent:', this.selectedEvent);
      console.log('services array:', this.selectedEvent.services);
      console.log('additionalServices:', this.additionalServices);
      console.log('filteredAdditionalServices:', this.filteredAdditionalServices);
      
      // Check if services array is properly initialized
      if (!this.selectedEvent.services) {
        console.log('Services array is undefined');
        this.selectedEvent.services = [];
      } else if (!Array.isArray(this.selectedEvent.services)) {
        console.log('Services is not an array, type:', typeof this.selectedEvent.services);
        this.selectedEvent.services = [];
      }
      
      // Add a test service if needed
      if (confirm('Add a test service?')) {
        this.addTestService();
      }
      
      alert(`Services count: ${this.selectedEvent.services.length}\nCheck console for details`);
    },
    
    addTestService() {
      if (!this.selectedEvent.services) {
        this.selectedEvent.services = [];
      }
      
      // Create a test service
      const testService = {
        add_service_id: Date.now(), // Use timestamp as a unique ID
        add_service_name: 'Test Service',
        add_service_description: 'This is a test service added for debugging',
        add_service_price: 1000,
        status: 'Pending'
      };
      
      // Add to services array
      this.selectedEvent.services.push(testService);
      console.log('Added test service:', testService);
      console.log('Updated services array:', this.selectedEvent.services);
    },
  },

  mounted() {
      this.fetchBookedWishlist();
      this.fetchUpcomingEvents();
      this.fetchAdditionalServices();
      this.fetchAvailableSuppliers();
      this.fetchAvailableVenues();
      this.fetchAvailableGownPackages();
      this.fetchOutfits();
  }
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
