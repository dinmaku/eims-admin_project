<template>
  <div class="h-full bg-gray-300 flex-grow overflow-x-hidden overflow-y-auto font-amaticBold">
    <div class="flex justify-end items-center my-7 px-4 space-x-[780px] w-full h-20 bg-[#f9f9f3]">
      <h1 class="flex-grow mx-5 font-bold text-3xl text-gray-800 font-amaticBold">Create event</h1>
    <router-link to="/manage-events">
    <button 
    @click="createEvent"
    :disabled
    :class = "buttonCursor"
    class="w-[130px] h-11 bg-[#e4e5e7] hover:bg-blue-500 font-bold text-gray-500 hover:text-white shadow-lg rounded transition-transform transform hover:scale-105 mr-10">
    Cancel
    </button>
  </router-link>


</div>




  <!--Forms-->
  
  <div class="flex items-center font-amaticBold text-gray-600 font-bold">
    <div class="w-[1170px] h-[300px] bg-[#f9f9f3] mr-2 mx-5 rounded-md shadow-xl p-3 border border-gray-100">
      <p class="text-xl font-semibold mb-4 mr-[1080px]">Wishlist</p>

      <div class = "flex justify-end items-center mb-4">
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

      <div class="flex mb-3">
        <div class="flex flex-col mr-8">
          <span class="text-sm mb-2 mr-20">Event Type</span>
          <select
            v-model="eventType"
            :disabled="!isEditing"
            class="w-[170px] h-9 border text-sm border-gray-300 rounded-md focus:ring-blue-500 focus:border-blue-500"
          >
            <option value="wedding">Wedding</option>
            <option value="birthday">Birthday</option>
            <option value="conference">Conference</option>
            <option value="party">Party</option>
            <option value="debut">Debut</option>
          </select>
        </div>

        <div class="flex flex-col mr-10">
          <span class="text-sm mb-2 mr-[67px]">Color</span>
          <input
            v-model="color"
            :disabled="!isEditing"
            type="text"
            class="w-[120px] h-9 border text-sm border-gray-300 rounded-md focus:ring-blue-500 focus:border-blue-500"
          />
        </div>
        <div class="flex flex-col mr-10">
          <span class="text-sm mb-2 mr-[240px]">Booked by</span>
          <input
            v-model="bookedBy"
            :disabled="!isEditing"
            type="text"
            class="w-80 h-9 border text-sm border-gray-300 rounded-md focus:ring-blue-500 focus:border-blue-500"
          />
        </div>
        <div class="flex flex-col">
          <span class="text-sm mb-2 mr-[259px]">Contact</span>
          <input
            v-model="contact"
            :disabled="!isEditing"
            type="text"
            class="w-80 h-9 border border-gray-300 text-sm rounded-md focus:ring-blue-500 focus:border-blue-500"
          />
        </div>
      </div>
  
      <div class="flex mb-3">
        <div class="flex flex-col mr-10">
          <span class="text-sm mb-2 mr-[255px]">Theme</span>
          <input
            v-model="theme"
            :disabled="!isEditing"
            type="text"
            class="w-80 h-9 border border-gray-300 text-sm rounded-md focus:ring-blue-500 focus:border-blue-500"
          />
        </div>
        <div class="flex flex-col">
          <span class="text-sm mb-2 mr-[259px]">Venue</span>
          <input
            v-model="venue"
            :disabled="!isEditing"
            type="text"
            class="w-80 h-9 border border-gray-300 text-sm rounded-md focus:ring-blue-500 focus:border-blue-500"
          />
        </div>
      </div>

   
      <div class="flex justify-end space-x-2 mt-2">
        <button
        v-if="eventType"
        @click = "saveChanges"
          class="bg-blue-500 text-white text-sm rounded-md py-1 px-2 hover:bg-blue-600">
          Save Changes
        </button>
        <button class="bg-gray-300 text-gray-700 text-sm rounded-md py-1 px-3 hover:bg-gray-400">
          Cancel
        </button>
      </div>
    </div>

  </div>
 
  <!--Event details form-->

  
    <div class="w-[1170px] h-[760px] bg-[#f9f9f3] mr-2 mx-5 mt-2 mb-10 rounded-md shadow-xl p-3 border border-gray-100 overflow-y-auto overflow-x-hidden">

      <component :is="currentForm" v-if="currentForm"></component>
    

  </div>


  </div>
</template>

<script>
import WeddingForm from '../pages/wedding-form.vue';
import BirthdayForm from '../pages/birthday-form.vue';


export default {
  name: 'CreateEvent',
  components: {
    WeddingForm,
    BirthdayForm,
  },
  data() {
    return {
      isEditing: false,
      eventType: 'wedding',
      color: 'Blush Pink',
      theme: 'Romantic Garden',
      venue: 'Enchanted Rose Garden',
      bookedBy: 'Jolly Bog',
      contact: '09216588784',
    };
    },
  computed: {
    currentForm() {
      switch (this.eventType) {
        case 'wedding':
          return WeddingForm;
        case 'birthday':
          return BirthdayForm;
        // Add more cases for other forms
        default:
          return null; 
      }
    },
  },
  methods: {
    handleChange() {
   
    },
    saveChanges() {
      console.log(`Applying changes for: ${this.eventType}`);
     
    },
  },
};


</script>

<style scoped>
/* Add component-specific styles here */
</style>