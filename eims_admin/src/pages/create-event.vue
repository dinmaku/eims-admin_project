<template>
  <div class="h-full bg-gray-300 flex-grow overflow-x-hidden overflow-y-auto font-amaticBold">
    <div class="flex justify-end items-center my-7 px-4 space-x-[780px] w-full h-20 bg-[#f9f9f3]">
      <h1 class="flex-grow mx-5 font-bold text-3xl text-gray-800 font-amaticBold">Create event</h1>
    <router-link to="/manage-events">
    <button 
    @click="createEvent"
    class="w-[130px] h-11 bg-[#e4e5e7] hover:bg-[#9B111E] font-bold text-gray-500 hover:text-white shadow-lg rounded transition-transform transform hover:scale-105 mr-10">
    Cancel
    </button>
  </router-link>


</div>




  <!--Forms-->
  
  <form class="flex items-center font-amaticBold text-gray-600 font-bold " @submit.prevent="saveWishlistChanges">
    <div class="w-[1170px] h-[300px] bg-[#f9f9f3] mr-2 mx-5 rounded-md shadow-xl p-3 border border-gray-100">
      <p class="text-xl font-semibold mb-4 mr-[1080px]">Wishlist</p>

      <div class="flex justify-end items-center mb-4">
        <label
          class="relative inline-block h-6 w-12 cursor-pointer rounded-full bg-gray-300 transition
          [-webkit-tap-highlight-color:_transparent] has-[:checked]:bg-gray-900">
          <input
            v-model="isEditing"
            class="peer sr-only"
            id="enableEdit"
            type="checkbox"
          />
          <span
            class="absolute inset-y-0 start-0 m-1 size-4 rounded-full bg-gray-300 ring-[6px] 
            ring-inset ring-white transition-all peer-checked:start-8 peer-checked:w-2 peer-checked:bg-white peer-checked:ring-transparent"></span>
        </label>
        <span class="ml-2 text-sm">Enable edit</span>
      </div>

      <div class="flex mb-3 text-start">
        <div class="flex flex-col mr-8">
          <span class="text-sm mb-2 indent-1">Event Type</span>
          <select
           v-model="selectedWishlist.event_type"
          :disabled="!isEditing"
          class="w-[170px] h-9 border text-sm border-gray-300 rounded-md focus:ring-blue-500 focus:border-blue-500"
        >
          <option value="Wedding">Wedding</option>
          <option value="Birthday">Birthday</option>
          <option value="Debut">Debut</option>
        </select>
        </div>

        <div class="flex flex-col mr-10">
          <span class="text-sm mb-2 indent-1">Color</span>
          <input
            v-model="selectedWishlist.event_color"
            :disabled="!isEditing"
            type="text"
            class="w-[120px] h-9 border text-sm border-gray-300 rounded-md focus:ring-blue-500 focus:border-blue-500"
          />
        </div>
        <div class="flex flex-col mr-10">
        <span class="text-sm mb-2 indent-1">Booked by</span>
        <input
          v-model="selectedWishlist.bookedBy"
          disabled
          type="text"
          class="w-80 h-9 border text-sm border-gray-300 rounded-md focus:ring-blue-500 focus:border-blue-500 bg-gray-100 cursor-not-allowed"
        />
      </div>
      <div class="flex flex-col">
        <span class="text-sm mb-2 indent-1">Contact</span>
        <input
          v-model="selectedWishlist.contact"
          disabled
          type="text"
          class="w-80 h-9 border border-gray-300 text-sm rounded-md focus:ring-blue-500 focus:border-blue-500 bg-gray-100 cursor-not-allowed"
        />
      </div>
      </div>

      <div class="flex mb-3 space-x-8 text-start">
        <div class="flex flex-col mr-3">
          <span class="text-sm mb-2 indent-1">Event Name</span>
          <input
            v-model="selectedWishlist.event_name"
            :disabled="!isEditing"
            type="text"
            class="w-80 h-9 border border-gray-300 text-sm rounded-md focus:ring-blue-500 focus:border-blue-500"
          />
        </div>
        <div class="flex flex-col">
          <span class="text-sm mb-2 indent-1">Venue</span>
          <input
            v-model="selectedWishlist.venue"
            :disabled="!isEditing"
            type="text"
            class="w-80 h-9 border border-gray-300 text-sm rounded-md focus:ring-blue-500 focus:border-blue-500"
          />
        </div>
        <div class="flex flex-col">
          <span class="text-sm mb-2 indent-1">Theme</span>
          <input
            v-model="selectedWishlist.event_theme"
            :disabled="!isEditing"
            type="text"
            class="w-80 h-9 border border-gray-300 text-sm rounded-md focus:ring-blue-500 focus:border-blue-500"
          />
        </div>
      </div>
      

      <div class="flex justify-end mt-2">
        <button
          type="submit"
          class="bg-[#B73A45] text-white text-sm rounded-md py-1 px-2 hover:bg-[#9B111E]"
        >
          Save Changes
        </button>
      </div>
    </div>
  </form>
 
  <!--Event details form-->

  
    <div class="w-[1170px] h-[760px] bg-[#f9f9f3] mr-2 mx-5 mt-2 mb-10 rounded-md shadow-xl p-3 border border-gray-100 overflow-y-auto overflow-x-hidden">

      <component :is="currentForm" v-if="currentForm"></component>
    

  </div>


  </div>
</template>

<script>
import axios from 'axios';

axios.defaults.withCredentials = true;


import WeddingForm from '../pages/wedding-form.vue';
import BirthdayForm from '../pages/birthday-form.vue';
import DebutForm from '../pages/debut-form.vue';


export default {
  name: 'CreateEvent',
  components: {
    WeddingForm,
    BirthdayForm,
    DebutForm,
  },
  data() {
    return {
      isEditing: false,
      selectedWishlist: {
      event_type: '',  // Initialize as empty
      event_name: '',
      event_theme: '',
      event_color: '',
      venue: '',
      bookedBy: '',
      contact: ''
    }
    };
  },
 
  computed: {
    currentForm() {
      // Ensure selectedWishlist is defined and event_type is available
      const eventType = this.selectedWishlist ? this.selectedWishlist.event_type : null;
      console.log('Current event type:', eventType); // Debugging line

      switch (eventType) {
        case 'Wedding':
          return 'WeddingForm';  // Dynamic component for wedding
        case 'Birthday':
          return 'BirthdayForm';  // Dynamic component for birthday
        case 'Debut':
          return 'DebutForm';  // Add more case for debut
        default:
          return null;  // No form displayed if event_type is not selected or unrecognized
      }
    },
  },

  methods: {
    async saveWishlistChanges(event) {
          event.preventDefault();

          try {
              const token = localStorage.getItem('access_token');

              // Check if selectedWishlist has necessary data, including events_id
              if (!this.selectedWishlist || !this.selectedWishlist.events_id) {
                  alert("Event ID is missing or invalid.");
                  return;
              }

              const response = await axios.put(
                  `http://127.0.0.1:5000/booked-wishlist/${this.selectedWishlist.events_id}`,
                  {
                      event_name: this.selectedWishlist.event_name,
                      event_type: this.selectedWishlist.event_type,
                      event_theme: this.selectedWishlist.event_theme,
                      event_color: this.selectedWishlist.event_color,
                      venue: this.selectedWishlist.venue,
                  },
                  {
                      headers: {
                          Authorization: `Bearer ${token}`,
                      },
                  }
              );

              if (response.status === 200) {
                  alert("Event updated successfully!");
              } else {
                  alert("Failed to update event.");
              }
          } catch (error) {
              console.error("Error updating event:", error);
              alert("Error updating event. Please try again.");
          }
        },





  },


  created() {
  const selectedEvent = this.$route.query;
    console.log('selectedEvent:', selectedEvent);

    if (selectedEvent) {
      // Initialize selectedWishlist
      this.selectedWishlist = {
        events_id: selectedEvent.events_id || '',  // Default to an empty string if not provided
        event_type: selectedEvent.event_type || '',  // Default to empty if not provided
        event_name: selectedEvent.event_name || '',  
        event_theme: selectedEvent.event_theme || '',
        event_color: selectedEvent.event_color || '',
        venue: selectedEvent.venue || '',
        bookedBy: `${selectedEvent.firstname} ${selectedEvent.lastname}` || '',
        contact: selectedEvent.contactnumber || ''
      };
    } else {
      console.log('No selectedEvent found in route query.');
    }
},
watch: {
    selectedWishlist(newValue) {
        console.log('selectedWishlist updated:', newValue);
    }
}


};


</script>

<style scoped>
/* Add component-specific styles here */
</style>