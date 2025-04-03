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
        'w-[120px] h-[45px] border border-solid rounded-md shadow-md transition-transform transform hover:scale-105',
        { 'bg-gray-800 text-white hover:bg-gray-900': showTable !== 'ongoing-events', 'bg-white': showTable === 'ongoing-events' }
      ]"
      @click="showTable = 'ongoing-events'"
    >
      <h1 class="font-amaticBold font-medium">Ongoing</h1>
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
              <th scope="col" class="px-2 py-3 w-32">Booked by</th>
              <th scope="col" class="px-2 py-3 w-32">Contact Number</th>
              <th scope="col" class="px-2 py-3 w-32">Booking Type</th>
              <th scope="col" class="px-2 py-3 w-20">Action</th>
            </tr>
          </thead>
          <tbody>
            <tr
                v-for="(event, index) in paginatedWishlist"
                :key="event.events_id"
                :class="{'bg-blue-100': selectedIndex === index, 'odd:bg-white odd:dark:bg-gray-900 even:bg-gray-50 even:dark:bg-gray-800': selectedIndex !== index}"
                class="border-b dark:border-gray-700">
              <th scope="row" class="px-2 py-3 font-medium text-gray-900 dark:text-white">{{ (currentWishlistPage - 1) * rowsPerWishlistPage + index + 1 }}</th>
              <td class="px-1 py-3 truncate">{{ event.event_name }}</td>
              <td class="px-1 py-3 truncate">{{ event.event_theme }}</td>
              <td class="px-1 py-3 truncate">{{ event.bookedBy || 'Not assigned' }}</td>
              <td class="px-1 py-3 truncate">{{ event.onsite_contact || event.contactnumber || 'Not provided' }}</td>
              <td class="px-1 py-3 truncate">{{ event.booking_type || 'N/A' }}</td>
              <td class="px-1 py-3 flex justify-start">
                <button
                    @click="openWishlistModal(event)"
                    class="p-2 hover:opacity-80 transform hover:scale-110 transition-transform duration-200">
                    <img src="/img/update3.png" alt="Update" class="w-5 h-5" title="Update Details">
                </button>
                <button
                  @click="confirmAndCreateInvoice(event)"
                class="p-2 hover:opacity-80 transform hover:scale-110 transition-transform duration-200">
                <img src="/img/invoice.png" alt="Invoice" class="w-5 h-5" title="View Invoice">
               </button>
               <button
                @click="updateEventStatus(event)"
                class="p-2 hover:opacity-80 transform hover:scale-110 transition-transform duration-200">
                <img src="/img/approve.png" alt="Update" class="w-5 h-5" title="Confirm Booking">
               </button>
               
              </td>
            </tr>
          </tbody>
        </table>

        <!-- Pagination Controls -->
        <div v-if="showTable === 'wishlist' && totalWishlistPages > 1" class="flex justify-center space-x-2 mt-4 mb-6">
          <button @click="prevWishlistPage" :disabled="currentWishlistPage === 1" 
            class="px-3 py-1 bg-[#9B111E] text-white rounded-md hover:bg-[#B73A45] disabled:opacity-50 text-sm">Previous</button>
          <button v-for="page in totalWishlistPages" :key="page" @click="changeWishlistPage(page)" 
            :class="{'bg-[#9B111E]': currentWishlistPage === page, 'bg-gray-300': currentWishlistPage !== page}" 
            class="px-3 py-1 text-white rounded-md hover:bg-[#B73A45] text-xs">
            {{ page }}
          </button>
          <button @click="nextWishlistPage" :disabled="currentWishlistPage === totalWishlistPages" 
            class="px-3 py-1 bg-[#9B111E] text-white rounded-md hover:bg-[#B73A45] disabled:opacity-50 text-xs">Next</button>
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
              <th scope="col" class="px-2 py-3">Event</th>
              <th scope="col" class="px-2 py-3">Event Theme</th>
              <th scope="col" class="px-2 py-3">Booked By</th>
              <th scope="col" class="px-2 py-3">Contact</th>
              <th scope="col" class="px-2 py-3">Booking Type</th>
              <th scope="col" class="px-2 py-3">Action</th>
            </tr>
          </thead>
          <tbody>
            <tr
                v-for="(event, index) in paginatedUpcomingEvents"
                :key="event.events_id"
                :class="{'bg-blue-100': selectedIndex === index, 'odd:bg-white odd:dark:bg-gray-900 even:bg-gray-50 even:dark:bg-gray-800': selectedIndex !== index}"
                class="border-b dark:border-gray-700">
              <th scope="row" class="px-2 py-3 font-medium text-gray-900 dark:text-white">{{ (currentPage - 1) * itemsPerPage + index + 1 }}</th>
              <td class="px-1 py-3 truncate">{{ event.event_name }}</td>
              <td class="px-1 py-3 truncate">{{ event.event_theme }}</td>
              <td class="px-1 py-3 truncate">{{ event.bookedBy || 'Not assigned' }}</td>
              <td class="px-1 py-3 truncate">{{ event.onsite_contact || event.contactnumber || 'Not provided' }}</td>
              <td class="px-1 py-3 truncate">{{ event.booking_type || 'N/A' }}</td>
              <td class="px-1 py-3 flex justify-start">
                <button
                    @click="openWishlistModal(event)"
                    class="p-2 hover:opacity-80 transform hover:scale-110 transition-transform duration-200">
                    <img src="/img/update3.png" alt="Update" class="w-5 h-5" title="Update Details">
                </button>
                <button
                  @click="confirmAndCreateInvoice(event)"
                  class="p-2 hover:opacity-80 transform hover:scale-110 transition-transform duration-200">
                  <img src="/img/invoice.png" alt="Invoice" class="w-5 h-5" title="View Invoice">
                  </button>
              </td>
            </tr>
            <tr v-if="paginatedUpcomingEvents.length === 0" class="border-b dark:border-gray-700">
              <td colspan="7" class="px-6 py-4 text-center text-gray-500">
                <p>No upcoming events found.</p>
                <p class="text-xs mt-2">Events with status 'Upcoming' will appear here.</p>
              </td>
            </tr>
          </tbody>
        </table>

        <!-- Pagination Controls -->
        <div class="flex justify-center space-x-2 mt-4 mb-6" v-if="showTable === 'events' && totalPages > 1">
          <button @click="prevPage" :disabled="currentPage === 1" 
            class="px-3 py-1 bg-[#9B111E] text-white rounded-md hover:bg-[#B73A45] disabled:opacity-50 text-sm">Previous</button>
          <button v-for="page in totalPages" :key="page" @click="changePage(page)" 
            :class="{'bg-[#9B111E]': currentPage === page, 'bg-gray-300': currentPage !== page}" 
            class="px-3 py-1 text-white rounded-md hover:bg-[#B73A45] text-xs">
            {{ page }}
          </button>
          <button @click="nextPage" :disabled="currentPage === totalPages" 
            class="px-3 py-1 bg-[#9B111E] text-white rounded-md hover:bg-[#B73A45] disabled:opacity-50 text-xs">Next</button>
        </div>
        
      </div>
    </div>

        <!-- Ongoing Events Section -->
        <div v-if="showTable === 'ongoing-events'" class="relative shadow-md sm:rounded-xl w-full max-w-[1170px] h-[200] ml-5 mt-2 font-amaticBold mb-10">
      <div class="overflow-x-auto">
        <!-- Remove debug button -->
        
        <!-- Rest of the table -->
        <table class="w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400 mb-4 table-fixed">
          <thead class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
            <tr>
              <th scope="col" class="px-2 py-3">#</th>
              <th scope="col" class="px-2 py-3">Event</th>
              <th scope="col" class="px-2 py-3">Client Name</th>
              <th scope="col" class="px-2 py-3">Date Scheduled</th>
              <th scope="col" class="px-2 py-3">Event Type</th>
              <th scope="col" class="px-2 py-3">Total Price</th>
              <th scope="col" class="px-2 py-3">Action</th>
            </tr>
          </thead>
          <tbody>
            <tr v-if="ongoingEvents.length === 0" class="border-b dark:border-gray-700">
              <td colspan="7" class="px-6 py-4 text-center text-gray-500">
                <p>No ongoing events found.</p>
                <p class="text-xs mt-2">Events with status 'Upcoming' and today's date or earlier will appear here.</p>
              </td>
            </tr>
            <tr
                v-for="(event, index) in paginatedOngoingEvents"
                :key="event.events_id"
                :class="{'bg-blue-100': selectedIndex === index, 'odd:bg-white odd:dark:bg-gray-900 even:bg-gray-50 even:dark:bg-gray-800': selectedIndex !== index}"
                class="border-b dark:border-gray-700">
              <th scope="row" class="px-2 py-3 font-medium text-gray-900 dark:text-white">{{ (currentOngoingPage - 1) * rowsPerOngoingPage + index + 1 }}</th>
              <td class="px-1 py-3 truncate">{{ event.event_name || 'Unnamed Event' }}</td>
              <td class="px-1 py-3 truncate">
                <span v-if="event.booking_type && event.booking_type.toLowerCase() === 'online'">
                  {{ event.bookedBy || 'Unknown User' }}
                </span>
                <span v-else>
                  {{ getOnsiteClientName(event) }}
                </span>
                <span class="ml-1 text-xs text-gray-500">
                  {{ event.booking_type ? `(${event.booking_type})` : '' }}
                </span>
              </td>
              <td class="px-1 py-3 truncate" :class="getDateCellClass(event)">
                {{ formatDate(event.event_date || event.schedule) }}
              </td>
              <td class="px-1 py-3 truncate">{{ event.event_type || 'Standard Event' }}</td>
              <td class="px-1 py-3 truncate font-medium" :class="getPriceCellClass(event)">
                ₱ {{ formatPrice(event.total_price) }}
              </td>
              <td class="px-1 py-3 flex justify-start">
                <button
                    @click="openWishlistModal(event)"
                    class="p-2 hover:opacity-80 transform hover:scale-110 transition-transform duration-200">
                    <img src="/img/update3.png" alt="View" class="w-5 h-5" title="View Details">
                </button>
                <button
                  @click="confirmAndCreateInvoice(event)"
                  class="p-2 hover:opacity-80 transform hover:scale-110 transition-transform duration-200">
                  <img src="/img/invoice.png" alt="Invoice" class="w-5 h-5" title="View Invoice">
                </button>
                <button
                  @click="markAsCompleted(event)"
                  class="p-2 hover:opacity-80 transform hover:scale-110 transition-transform duration-200">
                  <img src="/img/approve.png" alt="Mark as Completed" class="w-5 h-5" title="Mark as Completed">
                </button>
              </td>
            </tr>
          </tbody>
        </table>
        
        <!-- Pagination Controls -->
        <div v-if="ongoingEvents.length > 0 && totalOngoingPages > 1" class="flex justify-center space-x-2 mt-4 mb-6">
          <button @click="prevOngoingPage" :disabled="currentOngoingPage === 1" 
            class="px-3 py-1 bg-[#9B111E] text-white rounded-md hover:bg-[#B73A45] disabled:opacity-50 text-sm">Previous</button>
          <button v-for="page in totalOngoingPages" :key="page" @click="changeOngoingPage(page)" 
            :class="{'bg-[#9B111E]': currentOngoingPage === page, 'bg-gray-300': currentOngoingPage !== page}" 
            class="px-3 py-1 text-white rounded-md hover:bg-[#B73A45] text-xs">
            {{ page }}
          </button>
          <button @click="nextOngoingPage" :disabled="currentOngoingPage === totalOngoingPages" 
            class="px-3 py-1 bg-[#9B111E] text-white rounded-md hover:bg-[#B73A45] disabled:opacity-50 text-xs">Next</button>
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
              <th scope="row" class="px-2 py-3 font-medium text-gray-900 dark:text-white">{{ (currentFinishedPage - 1) * rowsPerFinishedPage + index + 1 }}</th>
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
        <div class="flex justify-center space-x-2 mt-4 mb-6" v-if="finishedEvents.length > 0">
          <button @click="prevFinishedPage" :disabled="currentFinishedPage === 1" 
            class="px-3 py-1 bg-[#9B111E] text-white rounded-md hover:bg-[#B73A45] disabled:opacity-50 text-sm">Previous</button>
          <button v-for="page in totalFinishedPages" :key="page" @click="changeFinishedPage(page)" 
            :class="{'bg-[#9B111E]': currentFinishedPage === page, 'bg-gray-300': currentFinishedPage !== page}" 
            class="px-3 py-1 text-white rounded-md hover:bg-[#B73A45] text-xs">
            {{ page }}
          </button>
          <button @click="nextFinishedPage" :disabled="currentFinishedPage === totalFinishedPages" 
            class="px-3 py-1 bg-[#9B111E] text-white rounded-md hover:bg-[#B73A45] disabled:opacity-50 text-xs">Next</button>
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
          <div>
            <label class="block text-xs font-medium mb-1 text-gray-600 text-start">Start Time</label>
            <input v-model="selectedEvent.start_time" disabled type="text" class="w-full p-2 border rounded text-sm">
          </div>
          <div>
            <label class="block text-xs font-medium mb-1 text-gray-600 text-start">End Time</label>
            <input v-model="selectedEvent.end_time" disabled type="text" class="w-full p-2 border rounded text-sm">
          </div>
        </div>
        <div class ="mb-2">
            <label class="text-xs font-medium mb-1 text-gray-600">Package Name</label>
            <p class="text-lg font-semibold">{{ selectedEvent.package_name }}</p>
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
                  <tr v-if="selectedEvent.venue && selectedEvent.venue.venue_id">
                    <td class="px-2 py-1">{{ selectedEvent.venue.venue_name }}</td>
                    <td class="px-2 py-1">{{ selectedEvent.venue.location }}</td>
                    <td class="px-2 py-1">₱{{ formatPrice(selectedEvent.venue.venue_price) }}</td>
                    <td class="px-2 py-1">
                      <span :class="{
                        'text-yellow-600': !selectedEvent.venue_status || selectedEvent.venue_status === 'Pending',
                        'text-green-600': selectedEvent.venue_status === 'Approved',
                        'text-red-600': selectedEvent.venue_status === 'Declined'
                      }">
                        {{ selectedEvent.venue_status || 'Pending' }}
                      </span>
                    </td>
                    <td class="px-2 py-1">
                      <div class="flex justify-start items-center space-x-2">
                        <div class="inline-block cursor-pointer">
                        <img 
                          alt="Approve Icon" 
                          class="w-[17px] h-[17px] transition-transform transform hover:scale-110 hover:brightness-90" 
                          src="/img/mark.png" 
                          @click="toggleVenueStatus"
                        >
                      </div>
                        <button type="button" @click="editVenue" class="inline-block cursor-pointer">
                        <img 
                          alt="Edit Icon" 
                          class="w-[17px] h-[17px] transition-transform transform hover:scale-110 hover:brightness-90" 
                          src="/img/edit.png" 
                        >
                      </button>
                      <div @click="removeVenue" class="inline-block cursor-pointer">
                        <img 
                          alt="Delete Icon" 
                          class="w-[17px] h-[17px] transition-transform transform hover:scale-110 hover:brightness-90" 
                          src="/img/delete.png" 
                        >
                      </div>
                    </div>
                    </td>
                  </tr>
                  <tr v-else-if="selectedEvent.venues && selectedEvent.venues.length > 0">
                    <td class="px-2 py-1">{{ selectedEvent.venues[0].venue_name }}</td>
                    <td class="px-2 py-1">{{ selectedEvent.venues[0].location }}</td>
                    <td class="px-2 py-1">₱{{ formatPrice(selectedEvent.venues[0].venue_price) }}</td>
                    <td class="px-2 py-1">
                      <span :class="{
                        'text-yellow-600': !selectedEvent.venues[0].status || selectedEvent.venues[0].status === 'Pending',
                        'text-green-600': selectedEvent.venues[0].status === 'Approved',
                        'text-red-600': selectedEvent.venues[0].status === 'Declined'
                      }">
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
                    {{ getSupplierName(supplier) }}
                  </td>
                  <td class="px-2 py-1">{{ supplier.service_type || supplier.service }}</td>
                  <td class="px-2 py-1">₱{{ formatPrice(supplier.price) }}</td>
                  <td class="px-2 py-1">
                    <span :class="{
                      'text-yellow-600': !supplier.status || supplier.status === 'Pending',
                      'text-green-600': supplier.status === 'Approved',
                      'text-red-600': supplier.status === 'Declined'
                    }">
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
                    <span :class="{
                      'text-yellow-600': !outfit.status || outfit.status === 'Pending',
                      'text-green-600': outfit.status === 'Approved',
                      'text-red-600': outfit.status === 'Declined'
                    }">
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
              <!-- Removing the debug button -->
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
                    <td class="px-2 py-1">{{ service.add_service_name || 'N/A' }}</td>
                    <td class="px-2 py-1">{{ service.add_service_description || 'N/A' }}</td>
                    <td class="px-2 py-1">₱{{ formatPrice(service.price || service.add_service_price || 0) }}</td>
                  <td class="px-2 py-1">
                      <span :class="{
                        'text-yellow-600': !service.status || service.status === 'Pending',
                        'text-green-600': service.status === 'Approved',
                        'text-red-600': service.status === 'Declined'
                      }">
                        {{ service.status || 'Pending' }}
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
            <h3 class="font-semibold">Estimated Rate</h3>
            <span class="text-xl font-bold">₱ {{ formatPrice(calculateTotalPrice) }}</span>
          </div>
          <div class="flex justify-between items-center mt-2 pt-2 border-t border-blue-100">
            <h3 class="font-semibold text-gray-700">Total Price Rate (*approved inclusions)</h3>
            <span class="text-xl font-bold text-gray-700">₱ {{ formatPrice(calculateExpectedPrice) }}</span>
          </div>
        </div>

        <!-- Actions -->
        <div class="flex justify-end space-x-3">
          <button @click="saveUpdatedWishlist" class="px-4 py-2 bg-blue-500 text-white rounded">Save Changes</button>
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
            @click="viewInvoice(selectedEvent)"
                class="h-8 w-24 bg-blue-900 font-amaticBold font-medium text-sm rounded-full text-white hover:bg-blue-600 transform-transition duration-300 transform hover:scale-105">
                View Invoice 
              </button>

            <button
            @click="viewTestInvoice()"
                class="h-8 w-32 ml-2 bg-green-900 font-amaticBold font-medium text-sm rounded-full text-white hover:bg-green-600 transform-transition duration-300 transform hover:scale-105">
                Test Invoice 
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
        <select v-model="selectedExternalSupplierType" class="w-full p-2 rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500">
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
  
  <!-- Status Approval Modal -->
  <div v-if="showStatusModal" class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
    <div class="bg-white rounded-lg p-6 w-96">
      <h3 class="text-lg font-semibold mb-4">Update Status</h3>
      <div class="mb-4">
        <label class="block text-sm font-medium text-gray-700 mb-2">Current Status: {{ inclusionToUpdate?.status || 'Pending' }}</label>
        <select v-model="newStatus" class="w-full p-2 border rounded-md">
          <option value="Pending">Pending</option>
          <option value="Approved">Approved</option>
          <option value="Declined">Declined</option>
        </select>
      </div>
      <div class="flex justify-end space-x-3">
        <button @click="closeStatusModal" class="px-4 py-2 text-gray-600 hover:text-gray-800">Cancel</button>
        <button @click="updateInclusionStatus" class="px-4 py-2 bg-blue-500 text-white rounded-md hover:bg-blue-600">Update</button>
      </div>
    </div>
  </div>

  <!-- Edit Event Modal -->
  <div v-if="showEditEventModal" @click.self="closeEditEventModal" class="fixed inset-0 bg-black bg-opacity-50 flex justify-center items-center z-50">
    <div class="bg-white w-[800px] p-6 rounded-lg shadow-lg">
      <div class="flex justify-between items-center mb-4">
        <h2 class="text-lg font-semibold">Edit Event Details</h2>
        <button type="button" @click="closeEditEventModal" class="text-red-500 hover:text-red-700">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
          </svg>
        </button>
      </div>

      <div class="grid grid-cols-2 gap-4">
        <!-- Event Details Section -->
        <div class="col-span-2">
          <h3 class="text-md font-bold font-raleway text-gray-700 mb-4">Event Details</h3>
          <div class="grid grid-cols-2 gap-4">
            <div>
              <label class="block text-sm font-medium text-gray-700">Event Name</label>
              <input v-model="selectedEvent.event_name" type="text" class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500">
            </div>
            <div>
              <label class="block text-sm font-medium text-gray-700">Event Theme</label>
              <input v-model="selectedEvent.event_theme" type="text" class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500">
            </div>
            <div>
              <label class="block text-sm font-medium text-gray-700">Schedule Date</label>
              <input v-model="selectedEvent.schedule" type="date" class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500">
            </div>
            <div>
              <label class="block text-sm font-medium text-gray-700">Capacity</label>
              <input v-model="selectedEvent.capacity" type="number" class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500">
            </div>
          </div>
        </div>

        <!-- Venue Section -->
        <div class="col-span-2">
          <div class="flex justify-between items-center mb-4">
            <h3 class="text-md font-bold font-raleway text-gray-700">Venue</h3>
            <button @click="editVenue" class="text-blue-500 hover:text-blue-700">Change Venue</button>
          </div>
          <div v-if="selectedEvent.venue" class="bg-gray-50 p-4 rounded-md">
            <p class="text-sm text-gray-700">{{ selectedEvent.venue.venue_name }}</p>
            <p class="text-sm text-gray-500">{{ selectedEvent.venue.location }}</p>
            <p class="text-sm text-gray-500">Status: {{ selectedEvent.venue_status }}</p>
          </div>
        </div>

        <!-- Services Section -->
        <div class="col-span-2">
          <div class="flex justify-between items-center mb-4">
            <h3 class="text-md font-bold font-raleway text-gray-700">Services</h3>
            <button @click="openInclusionModal('service')" class="text-blue-500 hover:text-blue-700">Add Service</button>
          </div>
          <div class="space-y-2">
            <div v-for="(service, index) in selectedEvent.services" :key="index" class="flex justify-between items-center bg-gray-50 p-2 rounded-md">
              <div>
                <p class="text-sm text-gray-700">{{ service.add_service_name }}</p>
                <p class="text-sm text-gray-500">{{ service.add_service_description }}</p>
              </div>
              <div class="flex items-center space-x-2">
                <button @click="editInclusion('services', index)" class="text-blue-500 hover:text-blue-700">Edit</button>
                <button @click="removeInclusion('services', index)" class="text-red-500 hover:text-red-700">Remove</button>
              </div>
            </div>
          </div>
        </div>

        <!-- Outfits Section -->
        <div class="col-span-2">
          <div class="flex justify-between items-center mb-4">
            <h3 class="text-md font-bold font-raleway text-gray-700">Outfits</h3>
            <button @click="openInclusionModal('outfit')" class="text-blue-500 hover:text-blue-700">Add Outfit</button>
          </div>
          <div class="space-y-2">
            <div v-for="(outfit, index) in selectedEvent.outfits" :key="index" class="flex justify-between items-center bg-gray-50 p-2 rounded-md">
              <div>
                <p class="text-sm text-gray-700">{{ outfit.outfit_name || outfit.gown_package_name }}</p>
                <p class="text-sm text-gray-500">{{ outfit.type === 'package' ? 'Package' : 'Individual' }}</p>
              </div>
              <div class="flex items-center space-x-2">
                <button @click="editInclusion('outfits', index)" class="text-blue-500 hover:text-blue-700">Edit</button>
                <button @click="removeInclusion('outfits', index)" class="text-red-500 hover:text-red-700">Remove</button>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="flex justify-end mt-6 space-x-4">
        <button @click="closeEditEventModal" class="px-4 py-2 bg-gray-500 text-white rounded-md hover:bg-gray-600">Cancel</button>
        <button @click="saveEventChanges" class="px-4 py-2 bg-blue-500 text-white rounded-md hover:bg-blue-600">Save Changes</button>
      </div>
    </div>
  </div>

  <!-- Add this notification modal after the other modals in the template -->
  <div v-if="showNotificationModal" @click.self="closeNotificationModal" class="fixed inset-0 bg-gray-800 bg-opacity-50 overflow-y-auto flex justify-center items-center z-50">
    <div class="bg-white p-5 rounded-lg shadow-lg w-[400px]">
      <div class="flex flex-col items-center">
        <div class="flex items-center justify-center w-12 h-12 rounded-full bg-red-100 mb-4">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-red-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z" />
          </svg>
        </div>
        <h2 class="text-xl font-semibold mb-4">{{ notificationTitle }}</h2>
        <p class="mb-6 text-center">{{ notificationMessage }}</p>
        <button 
          @click="closeNotificationModal" 
          class="bg-red-600 text-white px-4 py-2 rounded hover:bg-red-700">
          OK
        </button>
      </div>
    </div>
  </div>

  <!-- Add the invoice creation modal -->
  <div v-if="showInvoiceCreationModal" class="fixed inset-0 bg-gray-800 bg-opacity-50 overflow-y-auto flex justify-center items-center z-50">
    <div class="bg-white p-6 rounded-lg shadow-lg w-[450px]">
      <div class="flex flex-col items-center">
        <div class="flex items-center mb-5">
          <img src="/img/invoice.png" alt="Invoice" class="w-8 h-8 mr-3">
          <h2 class="text-xl font-semibold">Create Invoice</h2>
        </div>
        
        <div class="w-full mb-6 p-5 bg-gray-50 rounded-lg">
          <div class="mb-3">
            <p class="text-gray-600 text-sm">Event Name:</p>
            <p class="font-semibold">{{ selectedEventForInvoice?.event_name || 'Unknown Event' }}</p>
          </div>
          
          <div class="mb-3">
            <p class="text-gray-600 text-sm">Event Type:</p>
            <p class="font-semibold">{{ selectedEventForInvoice?.event_type || 'Standard Event' }}</p>
          </div>
          
          <div>
            <p class="text-gray-600 text-sm">Client:</p>
            <p class="font-semibold">{{ getOnsiteClientName(selectedEventForInvoice) || 'Unknown Client' }}</p>
          </div>
        </div>
        
        <p class="mb-6 text-center text-sm text-gray-600">
          No invoice exists for this event. Creating an invoice will allow you to track payments and generate receipts.
        </p>
        
        <div class="flex space-x-4">
          <button 
            @click="cancelInvoiceCreation" 
            class="bg-gray-200 text-gray-800 px-4 py-2 rounded hover:bg-gray-300 transition-colors">
            Cancel
          </button>
          <button 
            @click="confirmCreateInvoice" 
            class="bg-blue-600 text-white px-6 py-2 rounded hover:bg-blue-700 transition-colors flex items-center">
            <img src="/img/invoice.png" alt="Invoice" class="w-5 h-5 mr-2 invert">
            Create Invoice
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
      showTable: 'wishlist', // Default to wishlist
      itemsPerPage: 5, // Limit to 5 items per page
      currentPage: 1,
      currentWishlistPage: 1,
      rowsPerWishlistPage: 5,
      currentFinishedPage: 1,
      rowsPerFinishedPage: 5,
      selectedIndex: null,
      isEditingInclusion: false,
      editingInclusionIndex: -1,
      selectedService: null,
      additionalServices: [],
      wishlist: [],
      upcomingEvents: [],
      currentOngoingPage: 1,
      rowsPerOngoingPage: 5, // Changed from 10 to 5 to limit to 5 items per page
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
      
      showStatusModal: false,
      inclusionToUpdate: null,
      newStatus: 'Pending',
      showEditEventModal: false,
      showNotificationModal: false,
      notificationTitle: '',
      notificationMessage: '',
      filteredOngoingEvents: [], // Add this new property
      selectedEventForInvoice: null,
      showInvoiceCreationModal: false,
    };
  },
  watch: {
    selectedEvent(newEvent) {
        if (newEvent) {
            this.selectedPackage = newEvent.packageDeal;
        }
    },
    
    showTable(newValue) {
      if (newValue === 'events') {
        this.fetchUpcomingEvents();
      } else if (newValue === 'ongoing-events') {
        this.fetchOngoingEvents();
      }
    }
},

  computed: {
    paginatedUpcomingEvents() {
      const start = (this.currentPage - 1) * this.itemsPerPage;
      const end = start + this.itemsPerPage;
      return this.upcomingEvents.slice(start, end);
    },
    totalPages() {
      return Math.ceil(this.upcomingEvents.length / this.itemsPerPage);
    },
    paginatedOngoingEvents() {
      const start = (this.currentOngoingPage - 1) * this.rowsPerOngoingPage;
      const end = start + this.rowsPerOngoingPage;
      return this.ongoingEvents.slice(start, end);
    },

    totalOngoingPages() {
      return Math.ceil(this.ongoingEvents.length / this.rowsPerOngoingPage);
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
    },
    calculateExpectedPrice() {
      let total = 0;

      // Add venue price if approved
      if (this.selectedEvent.venue && this.selectedEvent.venue_status === 'Approved') {
        total += parseFloat(this.selectedEvent.venue.venue_price) || 0;
      }

      // Add approved suppliers
      if (this.selectedEvent.suppliers) {
        total += this.selectedEvent.suppliers
          .filter(supplier => supplier.status === 'Approved')
          .reduce((sum, supplier) => sum + (parseFloat(supplier.price) || 0), 0);
      }

      // Add approved outfits
      if (this.selectedEvent.outfits) {
        total += this.selectedEvent.outfits
          .filter(outfit => outfit.status === 'Approved')
          .reduce((sum, outfit) => {
            const price = outfit.type === 'package' 
              ? parseFloat(outfit.gown_package_price) || 0
              : parseFloat(outfit.rent_price) || 0;
            return sum + price;
          }, 0);
      }

      // Add approved services
      if (this.selectedEvent.services) {
        total += this.selectedEvent.services
          .filter(service => service.status === 'Approved')
          .reduce((sum, service) => sum + (parseFloat(service.add_service_price) || 0), 0);
      }

      return total;
    },
    upcomingEventStats() {
      // Create debug information about upcoming events
      if (!this.upcomingEvents || this.upcomingEvents.length === 0) {
        return 'No upcoming events found';
      }
      
      // Check for status values
      const statusValues = this.upcomingEvents.map(e => e.status);
      const uniqueStatuses = [...new Set(statusValues)];
      
      return {
        total: this.upcomingEvents.length,
        statuses: uniqueStatuses,
        withUpcomingStatus: this.upcomingEvents.filter(e => e.status === 'Upcoming').length,
        withStatus: this.upcomingEvents.filter(e => e.status).length,
        firstEvent: this.upcomingEvents.length > 0 ? JSON.stringify(this.upcomingEvents[0]) : 'No events'
      };
    },
    
    filteredUpcomingEvents() {
      // Filter events to only include those with "Upcoming" status (case insensitive)
      return this.upcomingEvents.filter(
        event => event.status && event.status.toUpperCase() === 'UPCOMING'
      );
    },
    ongoingEvents() {
      // Just return the pre-filtered events
      return this.filteredOngoingEvents;
    },
    
    paginatedOngoingEvents() {
      const start = (this.currentOngoingPage - 1) * this.rowsPerOngoingPage;
      const end = start + this.rowsPerOngoingPage;
      return this.ongoingEvents.slice(start, end);
    },
    
    totalOngoingPages() {
      return Math.ceil(this.ongoingEvents.length / this.rowsPerOngoingPage);
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
        const accessToken = localStorage.getItem('access_token');
        if (!accessToken) {
          console.error('No access token found');
          return;
        }

        const response = await fetch('http://127.0.0.1:5000/booked-wishlist', {
          method: 'GET',
          headers: {
            'Authorization': `Bearer ${accessToken}`,
            'Content-Type': 'application/json'
          },
          credentials: 'include'
        });

        if (!response.ok) {
          throw new Error('Failed to fetch booked wishlist');
        }

        const data = await response.json();
        console.log('Raw response data:', data);

        // Process the data to extract venue names and outfits
        const processedEvents = data.map(event => {
          // Create a proper venue object if venue data exists
          let venue = null;
          if (event.venue_id) {
            venue = {
              venue_id: event.venue_id,
              venue_name: event.venue_name,
              location: event.venue_location,
              description: event.venue_description,
              venue_price: event.venue_price,
              venue_capacity: event.venue_capacity
            };
            console.log(`Created venue object for ${event.event_name} with id ${venue.venue_id}`);
          }
          
          console.log(`Event ${event.event_name} venue_status: ${event.venue_status || 'not set'}`);
          
          // Extract outfits from the outfits array if it exists
          const outfits = event.outfits || [];
          
          return {
            ...event,
            venue: venue,
            outfits: outfits,
            booking_type: event.booking_type || 'N/A'  // Include booking_type
          };
        });

        // Separate events based on status
        this.wishlist = processedEvents.filter(event => event.status === 'Wishlist');
        this.upcomingEvents = processedEvents.filter(event => event.status === 'Upcoming');
        
        console.log('Processed wishlist:', this.wishlist);
        console.log('Processed upcoming events:', this.upcomingEvents);
      } catch (error) {
        console.error('Error fetching booked wishlist:', error);
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

  goToInvoice(event) {
    try {
      if (!event || !event.events_id) {
        console.error('Cannot view invoice: Invalid event data', event);
        alert('Error: Cannot view invoice for this event - missing event ID');
        return;
      }
      
      console.log('Invoice requested for event:', event.event_name);
      console.log('Event ID:', event.events_id, 'Type:', typeof event.events_id);
      
      // Ensure event_id is a string
      const eventId = String(event.events_id);
      console.log('Formatted event ID:', eventId);
      
      // Store event ID in localStorage for the invoice page
      localStorage.setItem('current_invoice_event_id', eventId);
      
      // Check if an invoice already exists in localStorage
      const storedInvoice = localStorage.getItem(`invoice_${eventId}`);
      let invoiceExists = false;
      
      if (storedInvoice) {
        try {
          const invoiceData = JSON.parse(storedInvoice);
          if (invoiceData && invoiceData.invoice_id) {
            invoiceExists = true;
            console.log('✅ Invoice found, navigating to view it:', invoiceData.invoice_number);
          }
        } catch (parseError) {
          console.error('Error parsing stored invoice:', parseError);
        }
      }
      
      if (invoiceExists) {
        // If invoice exists, navigate to it directly
        this.$router.push(`/invoice/${eventId}`);
      } else {
        // No invoice exists, show a confirmation dialog
        if (confirm(`No invoice exists for "${event.event_name}". Would you like to create one now?`)) {
          // User confirmed, set create_new_invoice flag and go to invoice page
          localStorage.setItem('create_new_invoice', 'true');
          this.$router.push(`/invoice/${eventId}`);
        }
      }
    } catch (error) {
      console.error('Error navigating to invoice:', error);
      alert('Error: Unable to view invoice - ' + error.message);
    }
  },

  async checkOrCreateInvoice(event, eventId) {
    try {
      console.log('DEBUG invoice modal: Starting checkOrCreateInvoice');
      console.log('DEBUG invoice modal: Current showInvoiceCreationModal state:', this.showInvoiceCreationModal);
      console.log('DEBUG invoice modal: selectedEventForInvoice:', this.selectedEventForInvoice);
      
      // Store event ID in localStorage as a backup method
      localStorage.setItem('current_invoice_event_id', eventId);
      
      // Show loading message to user
      this.notificationTitle = 'Please wait';
      this.notificationMessage = 'Checking invoice status...';
      this.showNotificationModal = true;
      
      // Since the backend call isn't working, check localStorage directly
      const storedInvoice = localStorage.getItem(`invoice_${eventId}`);
      let invoiceExists = false;
      
      if (storedInvoice) {
        try {
          const invoiceData = JSON.parse(storedInvoice);
          if (invoiceData && invoiceData.invoice_id) {
            invoiceExists = true;
            console.log('✅ Invoice found in localStorage, navigating to view it:', invoiceData);
          }
        } catch (parseError) {
          console.error('Error parsing stored invoice:', parseError);
        }
      }
      
      // Close the notification modal
      this.showNotificationModal = false;
      
      if (invoiceExists) {
        // Navigate to invoice view with the event ID using params
        this.$router.push(`/invoice/${eventId}`);
      } else {
        // Set the event for the modal to use and show the creation modal
        console.log('⚠️ No invoice found, showing creation modal for event:', event.event_name);
        this.selectedEventForInvoice = event;
        this.showInvoiceCreationModal = true;
        console.log('DEBUG invoice modal: Set showInvoiceCreationModal to:', this.showInvoiceCreationModal);
        console.log('DEBUG invoice modal: Set selectedEventForInvoice to:', this.selectedEventForInvoice);
      }
    } catch (error) {
      this.showNotificationModal = false;
      console.error('Error checking invoice status:', error);
      alert(`Error: ${error.message}`);
    }
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

    async addSelectedSupplier() {
      if (!this.selectedSupplier) {
        console.error('No supplier selected');
        return;
      }

      try {
        // Initialize suppliers array if it doesn't exist
        if (!this.selectedEvent.suppliers) {
          this.selectedEvent.suppliers = [];
        }

        // Add the supplier with a default status of 'Pending'
        const supplierData = {
          ...this.selectedSupplier,
          status: 'Pending'
        };

        // Add to local state first
      if (this.isEditingInclusion) {
        // Update existing supplier
          this.selectedEvent.suppliers[this.editingInclusionIndex] = supplierData;
        this.isEditingInclusion = false;
        this.editingInclusionIndex = -1;
      } else {
        // Add new supplier
          this.selectedEvent.suppliers.push(supplierData);
        }

        // Save changes to the database immediately
        await this.saveUpdatedWishlist(false); // Don't show success alert

      // Reset and close modal
      this.selectedSupplier = null;
      this.showInclusionModal = false;
      this.selectedInclusionType = '';
      } catch (error) {
        console.error('Error adding supplier:', error);
        alert(`Error adding supplier: ${error.message}`);
      }
  },

    async addSelectedVenue() {
      if (!this.selectedVenue) {
        alert('Please select a venue.');
        return;
      }

      // Check if venue already exists
      if (this.selectedEvent.venue) {
        alert('This event already has a venue. Please remove the existing venue first.');
        return;
      }

      // Add the venue to the selected event
      this.selectedEvent.venue = {
        venue_id: this.selectedVenue.venue_id,
        venue_name: this.selectedVenue.venue_name,
        location: this.selectedVenue.location,
        venue_price: this.selectedVenue.venue_price,
        venue_capacity: this.selectedVenue.venue_capacity
      };

      // Set initial venue status
      this.selectedEvent.venue_status = 'Pending';

      // Close the venue modal
      this.closeInclusionModal();

      // Save changes to the database
      this.saveUpdatedWishlist(false);
    },

    async addSelectedOutfit() {
      if (!this.selectedOutfit) {
        console.error('No outfit selected');
        return;
      }

      try {
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

        // Add the outfit to local state
      this.selectedEvent.outfits.push(outfitData);

        // Save changes to the database immediately
        await this.saveUpdatedWishlist(false); // Don't show success alert

      // Reset and close modal
      this.selectedOutfit = null;
      this.showInclusionModal = false;
      this.selectedInclusionType = '';
      this.outfitSelectionMode = 'package'; // Reset to default mode
      } catch (error) {
        console.error('Error adding outfit:', error);
        alert(`Error adding outfit: ${error.message}`);
      }
  },

    async addSelectedService() {
      if (!this.selectedService) {
        console.error('No service selected');
        return;
      }

      try {
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
          add_service_price: parseFloat(this.selectedService.add_service_price || 0),
          status: 'Pending' // Add default status
      };

        // Add to local state first
      if (this.isEditingInclusion) {
        // Update existing service
        this.selectedEvent.services[this.editingInclusionIndex] = serviceData;
        this.isEditingInclusion = false;
        this.editingInclusionIndex = -1;
      } else {
        // Add new service
      this.selectedEvent.services.push(serviceData);
      }

        // Save changes to the database immediately
        await this.saveUpdatedWishlist(false); // Don't show success alert

      this.selectedService = null;
      this.closeInclusionModal();
      } catch (error) {
        console.error('Error adding service:', error);
        alert(`Error adding service: ${error.message}`);
      }
  },

  removeSupplier(index) {
    this.selectedEvent.suppliers.splice(index, 1);
  },

  removeService(index) {
    this.selectedEvent.services.splice(index, 1);
  },

  removeVenue() {
    // Check if the venue exists
    if (!this.selectedEvent.venue) {
      console.error('No venue to remove');
      return;
    }
    
    if (confirm('Are you sure you want to remove this venue?')) {
      // Clear the venue data
    this.selectedEvent.venue = null;
      this.selectedEvent.venue_id = null;
      this.selectedEvent.venue_status = 'Pending';
      
      // Save changes
      this.saveUpdatedWishlist(false).then(success => {
        if (success) {
          alert('Venue removed successfully');
        } else {
          alert('Failed to remove venue');
        }
      });
    }
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
            rent_price: this.selectedOutfit.rent_price,
            status: 'Pending',
            is_initialized: false
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
            status: 'Pending',
            is_initialized: false
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
        venue_status: event.venue_status || 'Pending',
        gown_package_name: event.gown_package_name || '',
        gown_package_price: event.gown_package_price || 0,
        firstname: event.firstname || '',
        lastname: event.lastname || '',
        contactnumber: event.contactnumber || ''
      }));

      // Create a venue object if one doesn't exist but we have venue data
      if (!this.selectedEvent.venue && this.selectedEvent.venue_id) {
        this.selectedEvent.venue = {
          venue_id: this.selectedEvent.venue_id,
          venue_name: this.selectedEvent.venue_name,
          location: this.selectedEvent.venue_location,
          venue_price: this.selectedEvent.venue_price,
          description: this.selectedEvent.venue_description,
          venue_capacity: this.selectedEvent.venue_capacity
        };
      }
      
      // Initialize outfits array if it doesn't exist
      if (!this.selectedEvent.outfits) {
        this.selectedEvent.outfits = [];
      }

      // If there's a gown package but no outfits, initialize the outfits array with the package
      if (event.gown_package_id && this.selectedEvent.outfits.length === 0) {
        this.selectedEvent.outfits.push({
          type: 'outfit_package',
          gown_package_id: event.gown_package_id,
          gown_package_name: event.gown_package_name,
          gown_package_price: event.gown_package_price,
          status: 'Pending',
          is_initialized: true
        });
      }

      // Make sure services array is properly initialized
      if (!this.selectedEvent.services || !Array.isArray(this.selectedEvent.services)) {
        this.selectedEvent.services = [];
      }

      // Ensure all services have a status field
      this.selectedEvent.services = this.selectedEvent.services.map(service => ({
          ...service,
        status: service.status || 'Pending'
      }));

      // Ensure all outfits have a status field
      this.selectedEvent.outfits = this.selectedEvent.outfits.map(outfit => ({
        ...outfit,
        status: outfit.status || 'Pending'
      }));

      // Ensure all suppliers have a status field
      if (Array.isArray(this.selectedEvent.suppliers)) {
        this.selectedEvent.suppliers = this.selectedEvent.suppliers.map(supplier => ({
          ...supplier,
          status: supplier.status || 'Pending'
        }));
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

    async confirmRemoveInclusion() {
      if (!this.inclusionToRemove) {
        console.error('No inclusion to remove');
        return;
      }

      try {
        const token = localStorage.getItem('access_token');
        if (!token) {
          throw new Error('No authentication token found');
        }

        const { type, index, item } = this.inclusionToRemove;
        let endpoint;
        let requestData = {};
        let method = 'DELETE'; // Change to DELETE

        switch (type) {
          case 'outfits': {
            if (!item.wishlist_outfit_id) {
              // For outfits without IDs, just remove from local state
              this.selectedEvent.outfits.splice(index, 1);
              alert('Outfit removed successfully');
              return;
            } else {
              // Use direct DELETE for wishlist outfit
              endpoint = `http://127.0.0.1:5000/api/wishlist-outfits-direct/${item.wishlist_outfit_id}`;
            }
            break;
          }
          
          case 'services': {
            if (!item.id) {
              // For services without IDs, just remove from local state
              this.selectedEvent.services.splice(index, 1);
              alert('Service removed successfully');
              return;
            } else {
              // Use direct DELETE for wishlist service
              endpoint = `http://127.0.0.1:5000/api/wishlist-services-direct/${item.id}`;
            }
            break;
          }
          
          case 'suppliers': {
            if (!item.wishlist_supplier_id) {
              // For suppliers without IDs, just remove from local state
              this.selectedEvent.suppliers.splice(index, 1);
              alert('Supplier removed successfully');
              return;
            } else {
              // Use direct DELETE for wishlist supplier
              endpoint = `http://127.0.0.1:5000/api/wishlist-suppliers-direct/${item.wishlist_supplier_id}`;
            }
            break;
          }
          
          case 'venues': {
            if (!item.wishlist_venue_id) {
              // For venues without IDs, just remove from local state
              this.selectedEvent.venues.splice(index, 1);
              alert('Venue removed successfully');
              return;
            } else {
              // Use direct DELETE for wishlist venue
              endpoint = `http://127.0.0.1:5000/api/wishlist-venues-direct/${item.wishlist_venue_id}`;
            }
            break;
          }
          default:
            throw new Error(`Unsupported inclusion type: ${type}`);
        }

        console.log(`Making API call to: ${endpoint} with method: ${method}`);
        
        // First attempt direct DELETE
        try {
          const response = await fetch(endpoint, {
            method: method,
            headers: {
              'Authorization': `Bearer ${token}`,
              'Content-Type': 'application/json'
            },
            credentials: 'include'
          });

          if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
          }

          // Remove from local state only after successful API call
      this.selectedEvent[type].splice(index, 1);
          alert(`${type.slice(0, -1)} removed successfully`);
        } catch (directDeleteError) {
          console.error('Direct DELETE failed, falling back to status update:', directDeleteError);
          
          // Fallback: update status to 'Deleted'
          let fallbackEndpoint;
          
          switch (type) {
            case 'outfits':
              fallbackEndpoint = `http://127.0.0.1:5000/api/wishlist-outfits/${item.wishlist_outfit_id}`;
              break;
            case 'services':
              fallbackEndpoint = `http://127.0.0.1:5000/api/wishlist-additional-services/${item.id}`;
              break;
            case 'suppliers':
              fallbackEndpoint = `http://127.0.0.1:5000/api/wishlist-suppliers/${item.wishlist_supplier_id}`;
              break;
            case 'venues':
              fallbackEndpoint = `http://127.0.0.1:5000/api/wishlist-venues/${item.wishlist_venue_id}`;
              break;
          }
          
          const fallbackResponse = await fetch(fallbackEndpoint, {
            method: 'PUT',
            headers: {
              'Authorization': `Bearer ${token}`,
              'Content-Type': 'application/json'
            },
            credentials: 'include',
            body: JSON.stringify({ status: 'Deleted' })
          });
          
          if (!fallbackResponse.ok) {
            throw new Error(`Fallback update failed! status: ${fallbackResponse.status}`);
          }
          
          // Remove from local state after successful fallback
          this.selectedEvent[type].splice(index, 1);
          alert(`${type.slice(0, -1)} marked as deleted successfully`);
        }
      } catch (error) {
        console.error('Error in confirmRemoveInclusion:', error);
        alert(`Error removing item: ${error.message}`);
      } finally {
      // Close the confirmation modal
      this.showRemoveConfirmationModal = false;
      this.inclusionToRemove = null;
      }
    },

    closeRemoveConfirmationModal() {
      this.showRemoveConfirmationModal = false;
      this.inclusionToRemove = null;
    },
    editInclusion(type, index) {
      // Convert inclusion type to modal type
      const modalTypes = {
        'suppliers': 'supplier',
        'venues': 'venue',
        'outfits': 'outfit',
        'services': 'service'
      };

      const modalType = modalTypes[type];
      if (!modalType) {
        console.error(`Unsupported inclusion type: ${type}`);
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

      // Preserve the current status
      const currentStatus = data.status || 'Pending';

      // Set up editing state
      this.isEditingInclusion = true;
      this.editingInclusionIndex = index;
      this.selectedInclusionType = modalType;

      // Pre-fill the form based on the inclusion type
      if (modalType === 'supplier') {
        // Set the supplier type first
        this.selectedSupplierType = data.service || data.service_type;
        // Then set the supplier data
        this.selectedSupplier = { 
          ...data,
          status: currentStatus
        };
        // Show the specific service type modal
        this.showInclusionModal = false;
        this.showSupplierModal = true;
      } else if (modalType === 'venue') {
        this.selectedVenue = { 
          ...data,
          status: currentStatus
        };
        this.showInclusionModal = true;
      } else if (modalType === 'outfit') {
        this.selectedOutfit = { 
          ...data,
          status: currentStatus
        };
        this.showInclusionModal = true;
      } else if (modalType === 'service') {
        this.selectedService = { 
          ...data,
          status: currentStatus
        };
      this.showInclusionModal = true;
      }
    },

    closeEditInclusionModal() {
      this.showEditInclusionModal = false;
      this.editingInclusion = { type: '', index: -1, data: {} };
    },

    async saveEditedInclusion() {
      try {
        // Update the inclusion in the selectedEvent based on the type and index
      const { type, index, data } = this.editingInclusion;
        
        if (!type || index < 0 || !this.selectedEvent[type] || !this.selectedEvent[type][index]) {
          throw new Error('Invalid inclusion data');
        }
        
        // Update the specific inclusion with edited data
        // First create a copy of the original item
        const updatedItem = { ...this.selectedEvent[type][index] };
        
        // Map the edited data to the correct fields based on inclusion type
        switch (type) {
          case 'suppliers':
            updatedItem.supplier_name = data.supplier_name;
            updatedItem.contact = data.contact;
            updatedItem.price = parseFloat(data.price) || 0;
            updatedItem.remarks = data.remarks;
            break;
          case 'venues':
            updatedItem.venue_name = data.venue_name;
            updatedItem.location = data.location;
            updatedItem.venue_price = parseFloat(data.price) || 0;
            break;
          case 'outfits':
            if (updatedItem.type === 'package') {
              updatedItem.gown_package_name = data.outfit_name;
              updatedItem.gown_package_price = parseFloat(data.price) || 0;
            } else {
              updatedItem.outfit_name = data.outfit_name;
              updatedItem.size = data.size;
              updatedItem.rent_price = parseFloat(data.price) || 0;
            }
            break;
          case 'services':
            updatedItem.add_service_name = data.service_name;
            updatedItem.add_service_description = data.description;
            updatedItem.add_service_price = parseFloat(data.price) || 0;
            break;
        }
        
        // Update the inclusion in the selectedEvent
        this.selectedEvent[type][index] = updatedItem;
        
        // Save changes to the database
        await this.saveUpdatedWishlist(false);
        
        // Close the modal
      this.closeEditInclusionModal();
        alert('Inclusion updated successfully');
      } catch (error) {
        console.error('Error saving edited inclusion:', error);
        alert(`Error updating inclusion: ${error.message}`);
      }
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
        const token = localStorage.getItem('access_token');
        if (!token) {
          throw new Error('No authentication token found');
        }

        let item = this.selectedEvent[type][index];
        let endpoint;
        let requestData;
        let method = 'PUT';
        
        // Determine the new status - toggle between Approved and Pending
        const newStatus = item.status === 'Approved' ? 'Pending' : 'Approved';
        const statusVerb = newStatus === 'Approved' ? 'approved' : 'reverted to pending';

        switch (type) {
          case 'outfits': {
            // Check if the wishlist_outfit_id exists
            if (!item.wishlist_outfit_id) {
              // For outfits without IDs, just update locally
              this.selectedEvent.outfits[index].status = newStatus;
              alert(`Outfit ${statusVerb} successfully`);
              return;
            } else {
              // Update existing wishlist outfit
              endpoint = `http://127.0.0.1:5000/api/wishlist-outfits/${item.wishlist_outfit_id}`;
              requestData = {
                status: newStatus
              };
            }
            break;
          }
          
          case 'services': {
            // Check if the service id exists
            if (!item.id) {
              // For services without IDs, just update locally
              this.selectedEvent.services[index].status = newStatus;
              alert(`Service ${statusVerb} successfully`);
              return;
            } else {
              // Update existing wishlist service
              endpoint = `http://127.0.0.1:5000/api/wishlist-additional-services/${item.id}`;
              requestData = {
                status: newStatus
              };
            }
            break;
          }
          
          case 'suppliers': {
            // Check if the wishlist_supplier_id exists
            if (!item.wishlist_supplier_id) {
              // For suppliers without IDs, just update locally
              this.selectedEvent.suppliers[index].status = newStatus;
              alert(`Supplier ${statusVerb} successfully`);
              return;
            } else {
              // Update existing wishlist supplier
              endpoint = `http://127.0.0.1:5000/api/wishlist-suppliers/${item.wishlist_supplier_id}`;
              requestData = {
                status: newStatus
              };
            }
            break;
          }
          
          case 'venues': {
            // Check if the wishlist_venue_id exists
            if (!item.wishlist_venue_id) {
              // For venues without IDs, just update locally
              this.selectedEvent.venues[index].status = newStatus;
              alert(`Venue ${statusVerb} successfully`);
              return;
            } else {
              // Update existing wishlist venue
              endpoint = `http://127.0.0.1:5000/api/wishlist-venues/${item.wishlist_venue_id}`;
              requestData = {
                status: newStatus
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
        
        // Update local state
        this.selectedEvent[type][index].status = newStatus;
        
        alert(`Item ${statusVerb} successfully`);
      } catch (error) {
        console.error('Error in approveInclusion:', error);
        alert(`Error updating item status: ${error.message}`);
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
          throw new Error('No authentication token found');
        }

        const response = await fetch('http://127.0.0.1:5000/api/upcoming-events', {
          headers: {
            'Authorization': `Bearer ${token}`
          },
          credentials: 'include'
        });

        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();
        
        // Ensure we set the upcomingEvents array correctly
        // And normalize the status to "Upcoming" if it's any variation of "upcoming"
        this.upcomingEvents = Array.isArray(data) ? data.map(event => {
          // If status doesn't exist or is null, set it to "Upcoming"
          if (!event.status) {
            return { ...event, status: 'Upcoming' };
          }
          // If status case doesn't match exactly, normalize it
          if (event.status && event.status.toUpperCase() === 'UPCOMING' && event.status !== 'Upcoming') {
            return { ...event, status: 'Upcoming' };
          }
          return event;
        }) : [];
        
        // Return the upcomingEvents array for promise chaining
        return this.upcomingEvents;
      } catch (error) {
        console.error('Error fetching upcoming events:', error);
        alert(`Error fetching upcoming events: ${error.message}`);
        // Return empty array on error for consistent promise handling
        return [];
      }
    },

    async markAsCompleted(event) {
      try {
        const token = localStorage.getItem('access_token');
        if (!token) {
          throw new Error('No authentication token found');
        }

        if (!confirm(`Are you sure you want to mark "${event.event_name}" as completed?`)) {
          return;
        }

        const response = await fetch(`http://127.0.0.1:5000/events/${event.events_id}/status`, {
          method: 'PUT',
          headers: {
            'Authorization': `Bearer ${token}`,
            'Content-Type': 'application/json'
          },
          credentials: 'include',
          body: JSON.stringify({
            status: 'Finished'
          })
        });

        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }

        const result = await response.json();
        
        if (result.success) {
          // Update the event status in upcomingEvents
          const eventIndex = this.upcomingEvents.findIndex(e => e.events_id === event.events_id);
          if (eventIndex !== -1) {
            this.upcomingEvents[eventIndex].status = 'Finished';
            
            // Add to finished events if that array exists
            if (this.finishedEvents) {
              this.finishedEvents.push({...this.upcomingEvents[eventIndex]});
            }
          }
          
          // Show success message
          this.notificationTitle = 'Success';
          this.notificationMessage = 'Event marked as completed successfully';
          this.showNotificationModal = true;
        } else {
          throw new Error(result.message || 'Failed to update event status');
        }
      } catch (error) {
        console.error('Error marking event as completed:', error);
        this.notificationTitle = 'Error';
        this.notificationMessage = `Error marking event as completed: ${error.message}`;
        this.showNotificationModal = true;
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
    async saveUpdatedWishlist(showAlert = true) {
      try {
        const token = localStorage.getItem('access_token');
        if (!token) {
          throw new Error('No authentication token found');
        }

        // Ensure venue_status is set
        if (!this.selectedEvent.venue_status) {
          console.log('venue_status was not set, defaulting to Pending');
          this.selectedEvent.venue_status = 'Pending';
        } else {
          console.log(`Using existing venue_status: ${this.selectedEvent.venue_status}`);
        }

        // Prepare data for API
        const updatedEvent = {
          events_id: this.selectedEvent.events_id,
          package_name: this.selectedEvent.package_name || '',
          description: this.selectedEvent.description || '',
          capacity: parseInt(this.selectedEvent.capacity) || 0,
          venue_id: this.selectedEvent.venue ? this.selectedEvent.venue.venue_id : null,
          venue_status: this.selectedEvent.venue_status,
          gown_package_id: this.selectedEvent.gown_package_id || null,
          additional_capacity_charges: parseFloat(this.selectedEvent.additional_capacity_charges) || 0,
          charge_unit: parseInt(this.selectedEvent.charge_unit) || 1,
          total_price: parseFloat(this.selectedEvent.total_price) || 0,
          event_type_id: this.selectedEvent.event_type_id || null,
          status: this.selectedEvent.status || 'Wishlist',
          outfits: this.selectedEvent.outfits.map(outfit => ({
            ...outfit,
            status: outfit.status || 'Pending'
          })),
          services: this.selectedEvent.services.map(service => ({
            ...service,
            status: service.status || 'Pending'
          })),
          suppliers: this.selectedEvent.suppliers.map(supplier => ({
            ...supplier,
            status: supplier.status || 'Pending'
          }))
        };

        console.log('Updating wishlist with data:', updatedEvent);
        console.log('Wishlist ID:', this.selectedEvent.wishlist_id);

        // Create API URL
        const apiUrl = `http://127.0.0.1:5000/wishlist-packages/${this.selectedEvent.wishlist_id}`;
        console.log('API URL:', apiUrl);

        // Configure axios request
        const config = {
          method: 'put',
          url: apiUrl,
          headers: { 
            'Authorization': `Bearer ${token}`, 
            'Content-Type': 'application/json'
          },
          data: updatedEvent,
          withCredentials: true
        };

        // Log the exact data being sent to the API
        console.log('API request data:', JSON.stringify(config.data));

        // Make the request
        const response = await axios(config);
        console.log('Response:', response);

        // Handle API response
        if (response.data && response.data.success) {
          if (showAlert) {
            alert('Wishlist updated successfully');
            this.closeWishlistModal();
          }
          // Refresh data
          console.log('Refreshing data after successful wishlist update...');
          await this.fetchBookedWishlist();
          console.log('Data refresh complete');
          return true;
        } else {
          throw new Error((response.data && response.data.message) || 'Failed to update wishlist');
        }
      } catch (error) {
        console.error('Error in saveUpdatedWishlist:', error);
        if (showAlert) {
          alert(`Error updating wishlist: ${error.message}`);
        }
        return false;
      }
    },
    async toggleVenueStatus() {
      try {
        // Determine the new status - toggle between Approved and Pending
        const newStatus = this.selectedEvent.venue_status === 'Approved' ? 'Pending' : 'Approved';
        const statusVerb = newStatus === 'Approved' ? 'approved' : 'reverted to pending';
        
        console.log(`Toggling venue status from ${this.selectedEvent.venue_status} to ${newStatus}`);
        
        // Get authentication token
        const token = localStorage.getItem('access_token');
        if (!token) {
          throw new Error('No authentication token found');
        }
        
        // Call the new API endpoint to update venue status
        const response = await axios({
          method: 'put',
          url: `http://127.0.0.1:5000/api/wishlist-packages/${this.selectedEvent.wishlist_id}/venue-status`,
          headers: { 
            'Authorization': `Bearer ${token}`, 
            'Content-Type': 'application/json'
          },
          data: {
            venue_status: newStatus
          },
          withCredentials: true
        });
        
        // Check if update was successful
        if (response.data && response.data.success) {
          // Update the status in the selected event
          this.selectedEvent.venue_status = newStatus;
          console.log(`Venue status successfully updated to: ${newStatus}`);
          alert(`Venue status ${statusVerb} successfully`);
          
          // Refresh the data to ensure UI is in sync with backend
          await this.fetchBookedWishlist();
          return true;
        } else {
          throw new Error('Failed to update venue status');
        }
      } catch (error) {
        console.error('Error in toggleVenueStatus:', error);
        alert(`Error updating venue status: ${error.message}`);
        return false;
      }
    },
    
    editVenue() {
      // Open the venue selection modal for editing
      this.openInclusionModal('venue');
    },
    approveInclusion(type, index) {
      this.inclusionToUpdate = this.selectedEvent[type][index];
      this.newStatus = this.inclusionToUpdate.status || 'Pending';
      this.showStatusModal = true;
    },

    closeStatusModal() {
      this.showStatusModal = false;
      this.inclusionToUpdate = null;
      this.newStatus = 'Pending';
    },

    async updateInclusionStatus() {
      try {
        if (!this.inclusionToUpdate) {
          throw new Error('No inclusion selected');
        }

        const token = localStorage.getItem('access_token');
        if (!token) {
          throw new Error('No authentication token found');
        }

        const data = {
          status: this.newStatus
        };

        let endpoint = '';
        if (this.inclusionToUpdate.wishlist_supplier_id) {
          endpoint = `http://127.0.0.1:5000/api/wishlist-suppliers/${this.inclusionToUpdate.wishlist_supplier_id}`;
        } else if (this.inclusionToUpdate.wishlist_outfit_id) {
          endpoint = `http://127.0.0.1:5000/api/wishlist-outfits/${this.inclusionToUpdate.wishlist_outfit_id}`;
        } else if (this.inclusionToUpdate.id) {
          endpoint = `http://127.0.0.1:5000/api/wishlist-additional-services/${this.inclusionToUpdate.id}`;
        } else if (this.inclusionToUpdate.wishlist_venue_id) {
          endpoint = `http://127.0.0.1:5000/api/wishlist-venues/${this.inclusionToUpdate.wishlist_venue_id}`;
        } else {
          throw new Error('Invalid inclusion type');
        }

        const response = await fetch(endpoint, {
          method: 'PUT',
          headers: {
            'Authorization': `Bearer ${token}`,
            'Content-Type': 'application/json'
          },
          credentials: 'include',
          body: JSON.stringify(data)
        });

        const result = await response.json();

        if (response.ok) {
          // Update the status in the local state
          this.inclusionToUpdate.status = this.newStatus;
          this.notificationTitle = 'Success';
          this.notificationMessage = 'Status updated successfully';
          this.showNotificationModal = true;
          this.closeStatusModal();
        } else {
          throw new Error(result.message || 'Failed to update status');
        }
      } catch (error) {
        console.error('Error updating status:', error);
        this.notificationTitle = 'Error';
        this.notificationMessage = error.message;
        this.showNotificationModal = true;
      }
    },

    async checkDatabaseEvents() {
      try {
        const token = localStorage.getItem('access_token');
        if (!token) {
          throw new Error('No authentication token found');
        }

        // Fetch all events with their status
        const response = await fetch('http://127.0.0.1:5000/api/check-events-status', {
          headers: {
            'Authorization': `Bearer ${token}`
          },
          credentials: 'include'
        });

        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();
        console.log('All events with their status:', data);
        
        // Check for uppercase/lowercase variations of "Upcoming"
        const upcomingVariations = data.filter(event => 
          event.status && event.status.toUpperCase() === 'UPCOMING'
        );
        console.log('Events with any casing of "Upcoming":', upcomingVariations);
        
        alert(`Found ${data.length} events total, ${upcomingVariations.length} with 'Upcoming' status (any casing). Check console for details.`);
      } catch (error) {
        console.error('Error checking events status:', error);
        alert(`Error checking events status: ${error.message}`);
      }
    },
    
    async fixEventStatus(event) {
      try {
        if (!event || !event.events_id) {
          alert('No valid event provided');
          return;
        }
        
        const token = localStorage.getItem('access_token');
        if (!token) {
          throw new Error('No authentication token found');
        }

        // Update the event status to exactly 'Upcoming'
        const response = await fetch(`http://127.0.0.1:5000/events/${event.events_id}/status`, {
          method: 'PUT',
          headers: {
            'Authorization': `Bearer ${token}`,
            'Content-Type': 'application/json'
          },
          credentials: 'include',
          body: JSON.stringify({
            status: 'Upcoming'  // Use exactly this casing
          })
        });

        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }

        const result = await response.json();
        if (result.success) {
          alert(`Event status updated to 'Upcoming'. Refreshing data...`);
          // Refresh the data
          await this.fetchUpcomingEvents();
        } else {
          throw new Error(result.message || 'Failed to update event status');
        }
      } catch (error) {
        console.error('Error fixing event status:', error);
        alert(`Error fixing event status: ${error.message}`);
      }
    },

    openEditEventModal(event) {
      this.selectedEvent = { ...event };
      this.showEditEventModal = true;
    },
    closeEditEventModal() {
      this.showEditEventModal = false;
      this.selectedEvent = null;
    },
    async saveEventChanges() {
      try {
        await this.saveUpdatedWishlist(true);
        this.closeEditEventModal();
      } catch (error) {
        console.error('Error saving event changes:', error);
        alert(`Error saving changes: ${error.message}`);
      }
    },
    closeNotificationModal() {
      this.showNotificationModal = false;
      this.notificationTitle = '';
      this.notificationMessage = '';
    },
    prevOngoingPage() {
      if (this.currentOngoingPage > 1) {
        this.currentOngoingPage -= 1;
      }
    },
    
    nextOngoingPage() {
      if (this.currentOngoingPage < this.totalOngoingPages) {
        this.currentOngoingPage += 1;
      }
    },
    
    changeOngoingPage(page) {
      this.currentOngoingPage = page;
    },
    debugOngoingEvents() {
      console.log('Debugging ongoing events:');
      console.log('Total upcomingEvents:', this.upcomingEvents.length);
      
      const today = new Date();
      today.setHours(0, 0, 0, 0);
      console.log('Today is:', today.toISOString());
      
      // Log the filtered events
      const filteredEvents = this.upcomingEvents.filter(event => {
        // Only include events with status = 'Upcoming'
        if (!event.status || event.status !== 'Upcoming') {
          return false;
        }
        
        // Skip if no event date
        if (!event.event_date) {
          return false;
        }
        
        // Convert event_date to Date object
        const eventDate = new Date(event.event_date);
        eventDate.setHours(0, 0, 0, 0);
        
        console.log(`Event: ${event.event_name}, Date: ${event.event_date}, Parsed: ${eventDate.toISOString()}, Status: ${event.status}`);
        
        // Check if event date is today or in the past
        const isToday = eventDate.getTime() === today.getTime();
        const isPast = eventDate.getTime() < today.getTime();
        
        console.log(`- Is today: ${isToday}, Is past: ${isPast}`);
        
        return eventDate.getTime() <= today.getTime();
      });
      
      console.log('Filtered ongoing events:', filteredEvents.length);
      console.log('These events should appear in the ongoing table:', filteredEvents);
      
      // Check if our computed property is working
      console.log('Computed ongoingEvents:', this.ongoingEvents.length);
      console.log('Computed matches filtered:', this.ongoingEvents.length === filteredEvents.length);
      
      return 'Check console for details';
    },
    formatDate(dateStr) {
      if (!dateStr) return 'Unscheduled';
      
      // Try to parse the date
      const date = new Date(dateStr);
      if (isNaN(date.getTime())) {
        return 'Invalid Date Format';
      }
      
      // Format the date
      return date.toLocaleDateString('en-US', {
        year: 'numeric',
        month: 'long',
        day: 'numeric'
      });
    },
    // Add this new method after fetchUpcomingEvents
    async fetchOngoingEvents() {
      try {
        const token = localStorage.getItem('access_token');
        if (!token) {
          throw new Error('No authentication token found');
        }

        // Get current date for filtering
        const today = new Date();
        today.setHours(0, 0, 0, 0); // Set to beginning of day
        
        console.log('Fetching events for filtering by date:', today.toISOString());

        // Use the existing upcoming-events endpoint 
        const url = 'http://127.0.0.1:5000/api/upcoming-events';
        
        const response = await fetch(url, {
          headers: {
            'Authorization': `Bearer ${token}`
          },
          credentials: 'include'
        });

        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();
        console.log('Fetched events for ongoing filtering:', data);
        
        // Filter the events on the client side
        const ongoingEvents = Array.isArray(data) ? data.filter(event => {
          // Skip if status is not 'Upcoming'
          if (!event.status || event.status.toUpperCase() !== 'UPCOMING') {
            return false;
          }
          
          // Check if event has a date (either event_date or schedule)
          const dateField = event.event_date || event.schedule;
          if (!dateField) {
            return false;
          }
          
          // Parse event date
          const eventDate = new Date(dateField);
          
          // Check if valid date
          if (isNaN(eventDate.getTime())) {
            console.warn(`Invalid date format for event ${event.event_name}: ${dateField}`);
            return false;
          }
          
          eventDate.setHours(0, 0, 0, 0); // Set to beginning of day for comparison
          
          // Event is today or has passed
          return eventDate.getTime() <= today.getTime();
        }).map(event => ({
          ...event,
          status: 'Upcoming', // Normalize the status
          firstname: event.firstname || '',
          lastname: event.lastname || '',
          onsite_firstname: event.onsite_firstname || '',
          onsite_lastname: event.onsite_lastname || '',
          bookedBy: event.bookedBy || event.username || '',
          booking_type: event.booking_type || '',
          total_price: event.total_price || 0,
          event_name: event.event_name || 'Unnamed Event',
          event_type: event.event_type || 'Standard Event'
        })) : [];
        
        console.log('Filtered ongoing events client-side:', ongoingEvents);
        
        // Store the filtered events in filteredOngoingEvents instead of upcomingEvents
        this.filteredOngoingEvents = ongoingEvents;
        
        return this.filteredOngoingEvents;
      } catch (error) {
        console.error('Error fetching ongoing events:', error);
        this.notificationTitle = 'Error';
        this.notificationMessage = `Error fetching ongoing events: ${error.message}`;
        this.showNotificationModal = true;
        return [];
      }
    },
    getOnsiteClientName(event) {
      // Check for onsite client name fields first
      if (event.onsite_firstname || event.onsite_lastname) {
        return `${event.onsite_firstname || ''} ${event.onsite_lastname || ''}`.trim();
      }
      
      // Fall back to regular firstname/lastname if onsite fields aren't available
      if (event.firstname || event.lastname) {
        return `${event.firstname || ''} ${event.lastname || ''}`.trim();
      }
      
      return 'Not specified';
    },
    getDateCellClass(event) {
      const today = new Date();
      today.setHours(0, 0, 0, 0); // Set to beginning of day
      
      const dateField = event.event_date || event.schedule;
      if (!dateField) return '';
      
      const eventDate = new Date(dateField);
      if (isNaN(eventDate.getTime())) return '';
      
      eventDate.setHours(0, 0, 0, 0); // Set to beginning of day
      
      // Check if date is today
      if (eventDate.getTime() === today.getTime()) {
        return 'text-blue-600 font-medium';
      }
      
      // Check if date is in the past
      if (eventDate.getTime() < today.getTime()) {
        return 'text-red-600 font-medium';
      }
      
      return '';
    },

    getPriceCellClass(event) {
      const price = parseFloat(event.total_price) || 0;
      
      if (price === 0) {
        return 'text-green-600';
      } else {
        return 'text-red-600';
      }
    },
    viewTestInvoice() {
      try {
        console.clear(); // Clear previous logs
        console.log('🧪 viewTestInvoice called - using hardcoded event ID');
        
        // Hardcoded test event ID - use a valid ID from your database
        const testEventId = '1';
        
        // Store in localStorage for the invoice page to find
        localStorage.setItem('current_invoice_event_id', testEventId);
        console.log('💾 Saved test event ID to localStorage:', testEventId);
        
        // Use direct navigation instead of Vue Router
        console.log('🔗 Navigating directly to: /invoice/' + testEventId);
        window.location.href = '/invoice/' + testEventId;
      } catch (error) {
        console.error('❌ Error in viewTestInvoice:', error);
        alert('Error: ' + error.message);
      }
    },
    cancelInvoiceCreation() {
      // Just close the modal without creating an invoice
      this.showInvoiceCreationModal = false;
      this.selectedEventForInvoice = null;
    },
    confirmCreateInvoice() {
      if (!this.selectedEventForInvoice || !this.selectedEventForInvoice.events_id) {
        console.error('No event selected for invoice creation');
        return;
      }
      
      const eventId = String(this.selectedEventForInvoice.events_id);
      console.log('🔄 Creating new invoice for event:', eventId);
      
      // Set a flag in localStorage to indicate we're creating a new invoice
      localStorage.setItem('create_new_invoice', 'true');
      
      // Close the modal
      this.showInvoiceCreationModal = false;
      
      // Navigate to invoice to create a new one
      this.$router.push(`/invoice/${eventId}`);
    },
    async confirmAndCreateInvoice(event) {
      try {
        if (!event || !event.events_id) {
          console.error('Cannot create invoice: Invalid event data', event);
          alert('Error: Cannot create invoice for this event - missing event ID');
          return;
        }
        
        // Ensure event_id is a string
        const eventId = String(event.events_id);
        console.log('Working with event ID:', eventId, 'Type:', typeof eventId);
        
        // Store event ID in localStorage for the invoice page
        localStorage.setItem('current_invoice_event_id', eventId);
        
        // Check if an invoice exists in the database
        try {
          const token = localStorage.getItem('access_token');
          if (!token) {
            throw new Error('No authentication token found');
          }
          
          // Show loading notification
          this.notificationTitle = 'Please wait';
          this.notificationMessage = 'Checking for existing invoice...';
          this.showNotificationModal = true;
          
          // Check for existing invoice by event ID
          const checkResponse = await fetch(`http://127.0.0.1:5000/api/invoices/event/${eventId}`, {
            method: 'GET',
            headers: {
              'Authorization': `Bearer ${token}`
            },
            credentials: 'include'
          });
          
          if (checkResponse.ok) {
            // Invoice exists, navigate to it
            console.log('Found existing invoice for event ID:', eventId);
            this.showNotificationModal = false;
            this.$router.push(`/invoice/${eventId}`);
            return;
          } else if (checkResponse.status !== 404) {
            // Only treat 404 as "invoice doesn't exist" - any other error should be reported
            console.error('Error checking for invoice:', checkResponse.status, checkResponse.statusText);
          }
          
          // If we get here, either the invoice doesn't exist (404) or we couldn't check effectively
          // Ask user if they want to create an invoice
          this.showNotificationModal = false;
          const confirmed = confirm(`No invoice exists for "${event.event_name}". Would you like to create one now?`);
          console.log('User confirmed invoice creation:', confirmed);
          
          if (confirmed) {
            // User confirmed, fetch the auth token
            if (!token) {
              throw new Error('No authentication token found');
            }
            
            // Show loading notification
            this.notificationTitle = 'Please wait';
            this.notificationMessage = 'Creating invoice...';
            this.showNotificationModal = true;
            
            try {
              // Initialize invoice tables first
              console.log('Initializing invoice tables...');
              const initResponse = await fetch('http://127.0.0.1:5000/api/initialize-invoice-tables', {
                method: 'POST',
                headers: {
                  'Authorization': `Bearer ${token}`
                },
                credentials: 'include'
              });
              
              if (!initResponse.ok) {
                console.warn('Table initialization response not OK, but continuing anyway:', 
                  initResponse.status, initResponse.statusText);
              } else {
                const initResult = await initResponse.json();
                console.log('Table initialization result:', initResult);
              }
              
              // Create a reasonable invoice estimate based on event data
              const totalAmount = this.estimateEventTotal(event) || 100000; // Fallback to 100,000 if estimation fails
              
              // Create a unique invoice number
              const invoiceNumber = `INV-${new Date().getFullYear()}-${Math.floor(Math.random() * 10000).toString().padStart(4, '0')}`;
              
              // Prepare invoice data - ensure events_id is a number
              const eventIdNumber = parseInt(eventId);
              if (isNaN(eventIdNumber)) {
                throw new Error(`Invalid event ID format: ${eventId} cannot be parsed as a number`);
              }
              
              const invoiceData = {
                events_id: eventIdNumber,
                invoice_number: invoiceNumber,
                invoice_date: new Date().toISOString().split('T')[0],
                total_amount: totalAmount,
                discount_amount: 0,
                final_amount: totalAmount,
                status: 'Unpaid',
                notes: `Invoice for ${event.event_name || 'event'}`
              };
              
              console.log('Creating invoice with data:', JSON.stringify(invoiceData, null, 2));
              
              // Make the API call to create the invoice
              const response = await fetch('http://127.0.0.1:5000/api/invoices', {
                method: 'POST',
                headers: {
                  'Authorization': `Bearer ${token}`,
                  'Content-Type': 'application/json'
                },
                body: JSON.stringify(invoiceData),
                credentials: 'include'
              });
              
              // Hide notification after response
              this.showNotificationModal = false;
              
              if (!response.ok) {
                const errorText = await response.text();
                console.error('API error response:', response.status, response.statusText, errorText);
                throw new Error(`HTTP error creating invoice! status: ${response.status}, details: ${errorText}`);
              }
              
              // Parse the JSON response
              let result;
              try {
                result = await response.json();
              } catch (jsonError) {
                console.error('Error parsing JSON response:', jsonError);
                const responseText = await response.text();
                throw new Error(`Invalid response from server: ${responseText.substring(0, 100)}...`);
              }
              
              console.log('Invoice created successfully:', result);
              
              // Store the invoice data in localStorage for backup
              localStorage.setItem(`invoice_${eventId}`, JSON.stringify(result));
              
              // Navigate to invoice view
              this.$router.push(`/invoice/${eventId}`);
            } catch (apiError) {
              this.showNotificationModal = false;
              console.error('API call failed, falling back to flag-based creation:', apiError);
              
              // Set a flag in localStorage to indicate we're creating a new invoice
              localStorage.setItem('create_new_invoice', 'true');
              
              // Navigate to invoice to create a new one
              this.$router.push(`/invoice/${eventId}`);
            }
          }
        } catch (error) {
          this.showNotificationModal = false;
          console.error('Error checking for existing invoice:', error);
          
          // Set a flag in localStorage to indicate we're creating a new invoice
          if (confirm(`Error checking for invoice: ${error.message}. Would you like to create a new invoice anyway?`)) {
            localStorage.setItem('create_new_invoice', 'true');
            this.$router.push(`/invoice/${eventId}`);
          }
        }
      } catch (error) {
        this.showNotificationModal = false;
        console.error('Error handling invoice:', error);
        alert('Error: ' + error.message);
      }
    },
    
    estimateEventTotal(event) {
      try {
        let total = 0;
        
        // Add venue price if available
        if (event.venue && event.venue.venue_price) {
          total += parseFloat(event.venue.venue_price) || 0;
        }
        
        // Add supplier prices if available
        if (event.suppliers && Array.isArray(event.suppliers)) {
          event.suppliers.forEach(supplier => {
            total += parseFloat(supplier.price || 0);
          });
        }
        
        // Add outfit prices if available
        if (event.outfits && Array.isArray(event.outfits)) {
          event.outfits.forEach(outfit => {
            total += parseFloat(outfit.price || 0);
          });
        }
        
        // Return total or fallback if it's zero
        return total > 0 ? total : 100000; // Default to 100,000 if no prices found
      } catch (error) {
        console.error('Error estimating event total:', error);
        return 100000; // Default value on error
      }
    },
    getSupplierName(supplier) {
      console.log('Displaying supplier:', JSON.stringify(supplier));
      
      // Check for supplier_name with highest priority
      if (supplier.supplier_name) {
        console.log('Using supplier.supplier_name:', supplier.supplier_name);
        return supplier.supplier_name;
      }
      
      // Check firstname/lastname combination - highest priority after supplier_name
      if (supplier.firstname || supplier.lastname) {
        const fullName = `${supplier.firstname || ''} ${supplier.lastname || ''}`.trim();
        console.log('Using firstname/lastname:', fullName);
        return fullName;
      }
      
      // Check supplier_firstname/supplier_lastname combination
      if (supplier.supplier_firstname || supplier.supplier_lastname) {
        const fullName = `${supplier.supplier_firstname || ''} ${supplier.supplier_lastname || ''}`.trim();
        console.log('Using supplier_firstname/supplier_lastname:', fullName);
        return fullName;
      }
      
      // Check for name property directly
      if (supplier.name) {
        console.log('Using supplier.name:', supplier.name);
        return supplier.name;
      }
      
      // Check for other possible properties where name might be stored
      if (supplier.company_name) {
        console.log('Using supplier.company_name:', supplier.company_name);
        return supplier.company_name;
      }
      
      if (supplier.business_name) {
        console.log('Using supplier.business_name:', supplier.business_name);
        return supplier.business_name;
      }
      
      if (supplier.vendor_name) {
        console.log('Using supplier.vendor_name:', supplier.vendor_name);
        return supplier.vendor_name;
      }
      
      // If we have supplier ID, provide a more informative fallback
      if (supplier.supplier_id) {
        return `Supplier #${supplier.supplier_id}`;
      }
      
      if (supplier.id) {
        return `Supplier #${supplier.id}`;
      }
      
      // Generic index-based fallback if available
      if (typeof supplier.index === 'number') {
        return `Supplier #${supplier.index + 1}`;
      }
      
      console.log('No name found in supplier object');
      return 'Unnamed Supplier';
    },
  },

  mounted() {
      this.fetchBookedWishlist();
      
      // Determine which events to fetch based on the active tab
      if (this.showTable === 'ongoing-events') {
        this.fetchOngoingEvents();
      } else {
      this.fetchUpcomingEvents();
      }
      
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
