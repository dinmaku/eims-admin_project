<template>
  <!--Events Header-->
  <div class="bg-gray-200 w-full h-full">
    <div class="w-full h-[65px] bg-gray-100 mt-2 flex items-center justify-between px-5 shadow-lg">
  <h1 class="font-amaticBold font-extraLight text-3xl">
    Events
  </h1>
  <div class="flex items-center">
    <select class="bg-white font-amaticBold border border-gray-100 rounded-md py-2 px-3 text-gray-700 shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 mr-5">
    <option>Today</option>
    <option>Yesterday</option>
    <option>Last 7 days</option>
    <option>This Month</option>
    <option>This Year</option>
  </select>
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

  <button
    class="w-40 h-[45px] bg-blue-600 border border-solid rounded-lg shadow-md hover:bg-blue-700 transition-transform transform hover:scale-105 ml-auto"
    @click="showTable = ''"
  >
    <h1 class="font-amaticBold font-semiBold text-white">Finished Events</h1>
  </button>
</div>
   
    

    <!-- Tables -->

    <!--Wishlist Table-->
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
            :key="event.no"
            :class="{'bg-blue-100': selectedIndex === index, 'odd:bg-white odd:dark:bg-gray-900 even:bg-gray-50 even:dark:bg-gray-800': selectedIndex !== index}"
            class="border-b dark:border-gray-700">
          <th scope="row" class="px-2 py-3 font-medium text-gray-900 whitespace-nowrap dark:text-white">{{ index + 1 }}</th>
          <td class="px-1 py-3 hidden sm:table-cell">{{ event.event_name }}</td>
          <td class="px-1 py-3 hidden sm:table-cell">{{ event.event_theme}}</td>
          <td class="px-1 py-3 hidden sm:table-cell">{{ event.event_color}}</td>
          <td class="px-1 py-3 hidden sm:table-cell">{{ event.venue }}</td>
          <td class="px-1 py-3 hidden sm:table-cell">{{ event.firstname }} {{ event.lastname }}</td>
          <td class="px-1 py-3 hidden sm:table-cell">{{ event.contactnumber }}</td>
          <td class="px-1 py-3 hidden sm:table-cell">
            <button
                @click="selectRowAndRedirect(index)"
                class="h-8 w-12 bg-blue-900 font-amaticBold font-medium text-sm rounded-md text-white hover:bg-blue-600">
                Select
              </button>
          </td>
        </tr>
      </tbody>
    </table>

    <!-- Pagination Controls -->
    <div class="flex justify-center space-x-2 mt-4 mb-6"> <!-- Added mb-6 for bottom margin -->
      <button @click="prevWishlistPage" :disabled="currentWishlistPage === 1" class="px-3 py-1 bg-blue-900 text-white rounded-md hover:bg-blue-600 disabled:opacity-50 text-md">Previous</button> <!-- Smaller button -->
      <button v-for="page in totalWishlistPages" :key="page" @click="changeWishlistPage(page)" :class="{'bg-blue-900': currentWishlistPage === page, 'bg-gray-300': currentWishlistPage !== page}" class="px-3 py-1 text-white rounded-md hover:bg-blue-600 text-xs">
        {{ page }}
      </button>
      <button @click="nextWishlistPage" :disabled="currentWishlistPage === totalWishlistPages" class="px-3 py-1 bg-blue-900 text-white rounded-md hover:bg-blue-600 disabled:opacity-50 text-xs">Next</button> <!-- Smaller button -->
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
  },

  methods: {
    async fetchBookedWishlist() {
          try {
        const token = localStorage.getItem('access_token');  // Get the JWT token from localStorage

        if (!token) {
            console.error('No access token found');
            return;
        }

        // Make the GET request to fetch the booked wishlist
        const response = await axios.get('http://127.0.0.1:5000/booked-wishlist', {
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${token}`,  // Send the JWT token in the Authorization header
            },
            withCredentials: true  // Send cookies with the request if needed
        });

        // Check if response contains data and map it accordingly
        if (response.data && Array.isArray(response.data)) {
            this.wishlist = response.data.map(item => ({
                events_id: item.events_id,
                userid: item.userid,
                event_name: item.event_name,
                event_type: item.event_type,
                event_theme: item.event_theme,
                event_color: item.event_color,
                venue: item.venue,
                schedule: item.schedule,
                start_time: item.start_time,
                end_time: item.end_time,
                status: item.status,
                firstname: item.firstname,
                lastname: item.lastname,
                contactnumber: item.contactnumber,
                
            }));
        } else {
            console.warn('No wishlist data found or data is not an array');
        }

    } catch (error) {
        console.error('Error fetching booked wishlist:', error.message || error);
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
        // Get the selected event data based on the index
        const selectedEvent = this.paginatedWishlist[index];

        // Use Vue Router to navigate to /create-event and pass selected data via query params
        this.$router.push({
            path: '/create-event',
            query: {
                events_id: selectedEvent.events_id,
                event_name: selectedEvent.event_name,
                event_type: selectedEvent.event_type,
                event_theme: selectedEvent.event_theme,
                event_color: selectedEvent.event_color,
                venue: selectedEvent.venue,
                schedule: selectedEvent.schedule,
                start_time: selectedEvent.start_time,
                end_time: selectedEvent.end_time,
                status: selectedEvent.status,
                firstname: selectedEvent.firstname,
                lastname: selectedEvent.lastname,
                contactnumber: selectedEvent.contactnumber,
            }
        });
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
    getCateringPrice() {
      switch (this.selectedCatering) {
        case 'catering1':
          return '₱15,000 - ₱70,000';
        case 'catering2':
          return '₱30,000 - ₱250,000';
        case 'catering3':
          return '₱20,000 - ₱150,000';
        default:
          return 'Price not available';
      }
    },
    getMultimediaPrice() {
      switch (this.selectedMultimedia) {
        case 'multimedia1':
          return '₱20,000 - ₱60,000';
        case 'multimedia2':
          return '₱10,000 - ₱30,000';
        case 'multimedia3':
          return '₱7,000 - ₱20,000';
        default:
          return 'Price not available';
      }
    },
    getGlamPrice() {
      switch (this.selectedGlam) {
        case 'glam1':
          return 'PHP 15,000 - 25,000';
        case 'glam2':
          return '₱7,000 - ₱30,000';
        case 'glam3':
          return '₱5,000 - ₱15,000';
        default:
          return 'Price not available';
      }
    },
    getHostPrice() {
      switch (this.selectedHost) {
        case 'host1':
          return '₱5,000 - ₱19,000';
        case 'host2':
          return '₱7,000 - ₱30,000';
        case 'host3':
          return '₱10,000 - ₱25,000';
        default:
          return 'Price not available';
      }
    },
    getAudioVisualPrice() {
      switch (this.selectedAudioVisual) {
        case 'audiovisual1':
          return '₱30,000 - ₱80,000';
        case 'audiovisual2':
          return '₱20,000 - ₱45,000';
        case 'audiovisual3':
          return '₱20,000 - ₱70,000';
        default:
          return 'Price not available';
      }
    },
    getEntertainmentPrice() {
      switch (this.selectedEntertainment) {
        case 'entertainment1':
          return '₱5,000 - ₱40,000';
        case 'entertainment2':
          return '₱10,000 - ₱100,000';
        case 'entertainment3':
          return '₱40,000 - ₱170,000';
        default:
          return 'Price not available';
      }
    },
    getTransportationPrice() {
      switch (this.selectedTransportation) {
        case 'transportation1':
          return '₱10,000 - ₱40,000';
        case 'transportation2':
          return '₱15,000 - ₱60,000';
        case 'transportation3':
          return '₱5,000 - ₱25,000';
        default:
          return 'Price not available';
      }
    },
    getInvitationsPrice() {
      switch (this.selectedInvitations) {
        case 'invitations1':
          return '₱20,000 - ₱70,000';
        case 'invitations2':
          return '₱10,000 - ₱25,000';
        case 'invitations3':
          return '₱30,000 - ₱90,000';
        default:
          return 'Price not available';
      }
    },
    getGiftsPrice() {
      switch (this.selectedGifts) {
        case 'gifts1':
          return '₱15,500 - ₱100,000';
        case 'gifts2':
          return '₱7,000 - ₱30,000';
        case 'gifts3':
          return '₱10,000 - ₱80,000';
        default:
          return 'Price not available';
      }
    },

    getPackagePrice() {
      switch (this.selectedPackage) {
        case 'package2':
          return '30k php';
        case 'package3':
          return '60k php';
        case 'package4':
          return '40k php';
        default:
          return 'Price not available';
      }
    },

    getPackagePrice(packageName) {
        const Package = this.packageDeal.find(pkg => pkg.packageName === packageName);
        return Package ? Package.price : 'Price not available';
    },

  },

  mounted() {
        this.fetchBookedWishlist();
        console.log(this.paginatedWishlist);
         
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