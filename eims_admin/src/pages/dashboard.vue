<template>
    <div class = "w-screen h-screen flex overflow-hidden font-amaticBold">
      <!-- Side bar -->
      <div class="w-[250px] h-full bg-gray-200 text-center text-white top-0 left-0 overflow-y-auto">
       <div class ="h-[50px] bg-gray-200 flex justify-start items-center">
          <div class="flex text-center items-center px-[20px]">
        <h3 class="font-bold text-2xl text-gray-800">EIMS</h3>
      </div>

       </div>
       <div class="h-[calc(100vh-50px)] bg-[#B22222] py-[20px]">
        <div class="flex flex-col justify-between h-full px-[20px] space-y-[10px]">
          <div class="flex flex-col justify-between space-y-[10px]">
            <router-link to="/dashboard" class="inline-flex relative items-center py-[20px] px-[10px] w-full text-sm font-amaticBold font-semibold rounded-md border-gray-200 hover:bg-[#F7E7CE] hover:text-gray-900 transition duration-400 ease-in-out">
              <img aria-hidden="true" class="mr-2 w-[20px] h-[20px] fill-current" src="/img/stats.png">
              Dashboard
            </router-link>

            <p @click="toggleSection('setup')" class="ml-2 mb-5 text-lg text-left font-bold text-[#FFE4C4] cursor-pointer">Setup</p>
            <div v-if="visibleSections.setup" class="ml-4 border-l-2 border-gray-50">
              <router-link to="/manage-users" class="inline-flex items-center py-[15px] px-[10px] w-full text-sm font-amaticBold font-semibold hover:bg-[#F7E7CE] hover:text-gray-900 transition duration-400 ease-in-out">
                <img aria-hidden="true" class="mr-2 w-[20px] h-[20px] fill-current" src="/img/manage-user.png">
                Accounts
              </router-link>
              <router-link to="/add-venue" class="inline-flex items-center py-[15px] px-[10px] w-full text-sm font-amaticBold font-semibold hover:bg-[#F7E7CE] hover:text-gray-900 transition duration-400 ease-in-out">
                <img aria-hidden="true" class="mr-2 w-[20px] h-[20px] fill-current" src="/img/venue.png">
                Venues
              </router-link>
              <router-link to="/additional-services" class="inline-flex items-center py-[15px] px-[10px] w-full text-sm font-amaticBold font-semibold hover:bg-[#F7E7CE] hover:text-gray-900 transition duration-400 ease-in-out">
                <img aria-hidden="true" class="mr-2 w-[20px] h-[20px] fill-current" src="/img/birthday-cake.png">
                Additionals
              </router-link>
              <router-link to="/add-outfitPackage" class="inline-flex items-center py-[15px] px-[6.3px] w-full text-sm font-amaticBold font-semibold hover:bg-[#F7E7CE] hover:text-gray-900 transition duration-400 ease-in-out">
                <img aria-hidden="true" class="mr-2 w-[20px] h-[20px] fill-current" src="/img/add-wardrobe.png">
                Outfits Packages
              </router-link>
              <router-link to="/add-services" class="inline-flex items-center py-[15px] px-[6.3px] w-full text-sm font-amaticBold font-semibold hover:bg-[#F7E7CE] hover:text-gray-900 transition duration-400 ease-in-out">
                <img aria-hidden="true" class="mr-2 w-[20px] h-[20px] fill-current" src="/img/events-ticket.png">
                Events Packages
              </router-link>
            </div>

            <p @click="toggleSection('management')" class="ml-2 text-left text-lg font-bold text-[#FFE4C4] cursor-pointer">Management</p>
            <div v-if="visibleSections.management" class="ml-4 border-l-2 border-gray-50">
              <router-link to="/manage-events" class="inline-flex items-center py-[15px] px-[10px] w-full text-sm font-amaticBold font-semibold hover:bg-[#F7E7CE] hover:text-gray-900 transition duration-400 ease-in-out">
                <img aria-hidden="true" class="mr-2 w-[20px] h-[20px] fill-current" src="/img/events-booked.png">
                Events
              </router-link>
              <router-link to="/event-calendar" class="inline-flex items-center py-[15px] px-[7px] w-full text-sm font-amaticBold font-semibold hover:bg-[#F7E7CE] hover:text-gray-900 transition duration-400 ease-in-out">
                <img aria-hidden="true" class="mr-2 w-[20px] h-[20px] fill-current" src="/img/upload.png">
                Event Schedules
              </router-link>
              <router-link to="/manage-outfits" class="inline-flex items-center py-[15px] px-[10px] w-full text-sm font-amaticBold font-semibold hover:bg-[#F7E7CE] hover:text-gray-900 transition duration-400 ease-in-out">
                <img aria-hidden="true" class="mr-2 w-[20px] h-[20px] fill-current" src="/img/wedding-dress.png">
                Booked Outfits
              </router-link>
            </div>
          </div>

          <div class="h-[50px]">
            <router-link to="/settings" class="inline-flex items-center py-[10px] px-[10px] w-full text-sm font-amaticBold font-semibold rounded-md border-gray-200 hover:bg-[#F7E7CE] hover:text-gray-900 transition duration-400 ease-in-out">
              <svg aria-hidden="true" class="mr-2 w-[25px] h-[25px] fill-current" xmlns="http://www.w3.org/2000/svg">
                <path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-6-3a2 2 0 11-4 0 2 2 0 014 0zm-2 4a5 5 0 00-4.546 2.916A5.986 5.986 0 0010 16a5.986 5.986 0 004.546-2.084A5 5 0 0010 11z" clip-rule="evenodd"></path>
              </svg>
              Setting
            </router-link>
          </div>
        </div>
      </div>
      </div>
       <!--Head Bar-->

      <div class ="w-full h-full bg-gray-500 text-center">
        <div class ="h-[50px] bg-gray-100 flex items-center shadow-xl px-[20px] w-full py-[10px] z-10 border-b">
        <!--Hamburger Menu-->
        <div class="w-[calc(100%-200px)] flex justify-center ">
            <!-- Search bar -->
            <form class="flex items-center w-[500px]">
              <label for="voice-search" class="sr-only">Search</label>
              <div class="relative w-full">
                <div class="flex absolute inset-y-0 left-0 items-center pl-3 pointer-events-none">
                  <svg aria-hidden="true" class="w-5 h-auto text-gray-500 dark:text-gray-400" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                    <path fill-rule="evenodd" d="M8 4a4 4 0 100 8 4 4 0 000-8zM2 8a6 6 0 1110.89 3.476l4.817 4.817a1 1 0 01-1.414 1.414l-4.816-4.816A6 6 0 012 8z" clip-rule="evenodd"></path>
                  </svg>
                </div>
                <input type="text" id="search-bar" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full pl-10 p-2.5  dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="Search..." required>
                <router-link to="/" class="flex absolute inset-y-0 right-0 items-center pr-3">
                  <svg aria-hidden="true" class="w-4 h-4 text-gray-500 dark:text-gray-400 hover:text-gray-900 dark:hover:text-white" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                  </svg>
                </router-link>
              </div>
            </form>
          </div>
          
          <!--Date--->
          <div class = "mx-5 font-amaticBold font-semibold text-sm">
          <span>Sept 15, 2024</span>
          </div>

          <!--User Icon-->
          <div class="w-[200px] ">
            <div class="flex items-center justify-start space-x-4" @click="toggleDrop">
              <img class="w-9 h-9 rounded-full border-2 border-gray-50 bg-white cursor-pointer" src="/img/ID.jpg" alt="">
              <div class="font-semibold dark:text-white text-left">
                <div>Dean Mark</div>
                <div class="text-xs text-gray-500 dark:text-gray-400">Admin</div>
              </div>
            </div>
            <!-- Drop down -->
            <div v-show="showDropDown" class="absolute right-[10px] z-10 mt-2 w-56 origin-top-right rounded-md bg-white shadow-lg ring-1 ring-black ring-opacity-5 focus:outline-none" role="menu" aria-orientation="vertical" aria-labelledby="menu-button" tabindex="-1">
              <div class="py-1 text-left" role="none">
                <!-- Active: "bg-gray-100 text-gray-900", Not Active: "text-gray-700" -->
                <a href="/profile" class="text-gray-700 block px-4 py-2 text-sm hover:bg-gray-200" role="menuitem" tabindex="-1" id="menu-item-0">Profile</a>
                <a href="#" class="text-gray-700 block px-4 py-2 text-sm hover:bg-gray-200" role="menuitem" tabindex="-1" id="menu-item-1">Support</a>
                <a href="#" class="text-gray-700 block px-4 py-2 text-sm hover:bg-gray-200" role="menuitem" tabindex="-1" id="menu-item-2">License</a>
                  <button type="submit" @click="handleLogout" class="text-gray-700 block w-full px-4 py-2 text-left text-sm hover:bg-gray-200" role="menuitem" tabindex="-1" id="menu-item-3">Log out</button>
              </div>
            </div>
          </div>
       </div>


       <div class="h-[calc(100vh-50px)] bg-white overflow-y-auto">

        <router-view />

       </div>

      </div>
        
      
    </div>
  </template>
  
  <script>
  import axios from 'axios';


  axios.defaults.withCredentials = true;

  export default {
    name: 'AdminDashboard',
  data() {
    return {
      showDropDown: false,
      showSide: true,
      toggleSideBar: false,
      visibleSections: {
        setup: true,
        management: true,
      },
    }
  },
  methods: {
    // hide show side bar
    toggleSideBar() {
      this.showSide = !this.showSide

    },
    toggleSection(section) {
      this.visibleSections[section] = !this.visibleSections[section];
    },
    // toggle user 
    toggleDrop() {
      this.showDropDown = !this.showDropDown
      localStorage.removeItem('access_token');

    },
    handleLogout() {
      this.loggedIn = false; // Update Vue component state
      localStorage.removeItem('loggedIn'); // Remove login status from localStorage
      localStorage.removeItem('access_token');
      localStorage.removeItem('userid');
      this.showDropDown = false; // Close dropdown
      this.$router.push('/'); // Optionally redirect to home or login page
      },
  }

};
  </script>
  
  <style scoped>
  html {
    scroll-behavior: smooth;
  }
    
  </style>