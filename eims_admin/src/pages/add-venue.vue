<template>
    <div class="bg-gray-200 w-full h-full overflow-y-auto">
        <div class="w-full h-[65px] bg-gray-100 mt-2 flex items-center justify-between px-5 shadow-lg">
        <h1 class="font-amaticBold font-extraLight text-3xl">
            Venues
        </h1>
        <button class="bg-[#9B111E] text-white px-3 py-2 rounded shadow-lg 
        transition-transform duration-300 transform hover:scale-105 font-semibold"
        @click="showInactiveVenues">
            Inactive Venues
        </button>
        </div>

        <div class="flex flex-row items-center m-5 space-x-5">
        <div class="flex justify-start w-52 h-20 bg-white rounded-lg shadow-lg px-2 items-center border-l-2 border-green-400 space-x-5">
            <img class="w-auto h-12" src="/img/venues.png" alt="Vendor Image">
            <h2 class="font-amaticRegular text-4xl font-bold mb-0"> {{ totalVenues }} <span class = "text-sm antialiased text-gray-600">venues</span></h2>
        </div>
        <form class="flex items-center w-[300px] mt-9">
              <label for="voice-search" class="sr-only">Search</label>
              <div class="relative w-full">
                <div class="flex absolute inset-y-0 left-0 items-center pl-3 pointer-events-none">
                  <svg aria-hidden="true" class="w-5 h-auto text-gray-500 dark:text-gray-400" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                    <path fill-rule="evenodd" d="M8 4a4 4 0 100 8 4 4 0 000-8zM2 8a6 6 0 1110.89 3.476l4.817 4.817a1 1 0 01-1.414 1.414l-4.816-4.816A6 6 0 012 8z" clip-rule="evenodd"></path>
                  </svg>
                </div>
                <input type="text" id="search-bar" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full pl-10 p-2.5  dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="Search Venue..." required v-model="searchTerm">
                <router-link to="/" class="flex absolute inset-y-0 right-0 items-center pr-3">
                  <svg aria-hidden="true" class="w-4 h-4 text-gray-500 dark:text-gray-400 hover:text-gray-900 dark:hover:text-white" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                  </svg>
                </router-link>
              </div>
        </form>
    </div>

            <div class="flex flex-row justify-end items-center m-5 my-7">
                <button class = "mr-2 w-28 h-10 bg-[#9B111E] font-semibold text-gray-100 font-quicksand rounded-md shadow-lg 
                transition-transform duration-300 transform hover:scale-105" @click="addVenueBtn">
                Add Venue
                </button>
            </div> 

        <!--- Venues Table --->

        <div v-if="showTable === 'Venues'" class="relative shadow-md sm:rounded-xl w-[1170px] h-[200] ml-5 mt-2 font-amaticBold mb-10">
            <div class="overflow-x-auto">
                <table class="w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400 mb-4 max-h-30">
                    <thead class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
                        <tr>
                            <th scope="col" class="px-2 py-3">#</th>
                            <th scope="col" class="px-2 py-3">Venue Name</th>
                            <th scope="col" class="px-2 py-3">Location</th>
                            <th scope="col" class="px-2 py-3">Rate</th>
                            <th scope="col" class="px-2 py-3">Capacity</th>
                            <th scope="col" class="px-2 py-3">Action</th>

                        </tr>
                    </thead>
                    <tbody>
                        <tr
                            v-for="(venue, index) in paginatedVenues"
                            :key="venue.selectVenueId"
                            class="border-b dark:border-gray-700 odd:bg-white odd:dark:bg-gray-900 even:bg-gray-50 even:dark:bg-gray-800">
                            <th scope="row" class="px-2 py-3 font-medium text-gray-900 whitespace-nowrap dark:text-white">{{ venue.dummyIndex }}</th>
                            <td class="px-1 py-3 hidden sm:table-cell">{{ venue.venue_name }}</td>
                            <td class="px-1 py-3 hidden sm:table-cell">{{ venue.location }}</td>
                            <td class="px-1 py-3 hidden sm:table-cell">{{ formatPrice(venue.venue_price) }} php</td>
                            <td class="px-1 py-3 hidden sm:table-cell">{{ venue.venue_capacity }}</td>
                            <td class="px-1 py-3 hidden sm:table-cell">
                                <div class="flex items-center space-x-2">
                                    <button
                                        class="p-2 hover:opacity-80 transform hover:scale-110 transition-transform duration-200"
                                        @click="editVenueBtn(index)"
                                        title="Edit">
                                        <img src="/img/update.png" alt="Update" class="w-6 h-6">
                                    </button>
                                    <button
                                        class="p-2 hover:opacity-80 transform hover:scale-110 transition-transform duration-200"
                                        @click="showRateModal = true; selectedVenue = venue"
                                        title="Set Rate">
                                        <img src="/img/rate.png" alt="Set Rate" class="w-6 h-6">
                                    </button>
                                    <button
                                        class="p-2 hover:opacity-80 transform hover:scale-110 transition-transform duration-200"
                                        @click="toggleVenueStatus(venue)"
                                        title="Set Inactive">
                                        <img src="/img/inactive.png" alt="Set Inactive" class="w-6 h-6">
                                    </button>
                                </div>
                            </td>
                        </tr>
                    </tbody>
                </table>

                <!-- Pagination Controls -->
                <div class="flex justify-center space-x-2 mt-4 mb-6">
                    <button @click="prevVenuesPage" :disabled="currentPage === 1"
                        class="px-3 py-1 bg-[#9B111E] text-white rounded-md hover:bg-[#B73A45] disabled:opacity-50 text-sm">Previous</button>
                    <button v-for="page in totalPages" :key="page" @click="changeVenuesPage(page)"
                        :class="{'bg-[#9B111E]': currentPage === page, 'bg-gray-300 ': currentPage !== page}"
                        class="px-3 py-1 text-white rounded-md hover:bg-[#B73A45] text-xs">
                        {{ page }}
                    </button>
                    <button @click="nextVenuesPage" :disabled="currentPage === totalPages"
                        class="px-3 py-1 bg-[#9B111E] text-white rounded-md hover:bg-[#B73A45]  disabled:opacity-50 text-xs">Next</button>
                </div>
            </div>
        </div>

        <!-- Inactive Venues Modal -->
        <div v-if="showInactiveVenuesModal" @click.self="closeInactiveVenuesModal" class="fixed inset-0 bg-gray-800 bg-opacity-50 overflow-y-auto flex justify-center items-center">
          <div class="bg-white p-5 rounded-lg shadow-lg w-[1000px]">
            <div class="flex justify-between items-center mb-4">
              <h2 class="text-xl font-semibold">Inactive Venues</h2>
              <button @click="closeInactiveVenuesModal" class="text-gray-500 hover:text-gray-700">
                <span class="text-2xl">&times;</span>
              </button>
            </div>

            <div class="overflow-x-auto">
              <table class="w-full text-sm text-left text-gray-500">
                <thead class="text-xs text-gray-700 uppercase bg-gray-50">
                  <tr>
                    <th class="px-6 py-3">No.</th>
                    <th class="px-6 py-3">Venue Name</th>
                    <th class="px-6 py-3">Location</th>
                    <th class="px-6 py-3">Price</th>
                    <th class="px-6 py-3">Description</th>
                    <th class="px-6 py-3">Capacity</th>
                    <th class="px-6 py-3">Actions</th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="(venue, index) in inactiveVenues" :key="venue.venue_id" 
                      class="bg-white border-b hover:bg-gray-50">
                    <td class="px-6 py-4">{{ index + 1 }}</td>
                    <td class="px-6 py-4">{{ venue.venue_name }}</td>
                    <td class="px-6 py-4">{{ venue.location }}</td>
                    <td class="px-6 py-4">₱{{ formatPrice(venue.venue_price) }}</td>
                    <td class="px-6 py-4">{{ venue.description }}</td>
                    <td class="px-6 py-4">{{ venue.venue_capacity }}</td>
                    <td class="px-6 py-4">
                      <button
                        class="p-2 hover:opacity-80 transform hover:scale-110 transition-transform duration-200"
                        @click="toggleVenueStatus(venue)"
                        title="Set Active">
                        <img src="/img/mark.png" alt="Set Active" class="w-6 h-6">
                      </button>
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>

        <!-- Status Confirmation Modal -->
        <div v-if="showStatusConfirmModal" @click.self="closeStatusConfirmModal" class="fixed inset-0 bg-gray-800 bg-opacity-50 overflow-y-auto flex justify-center items-center z-50">
          <div class="bg-white p-5 rounded-lg shadow-lg w-[400px]">
            <div class="flex flex-col items-center">
              <h2 class="text-xl font-semibold mb-4">Confirm Status Change</h2>
              <p class="mb-6 text-center">Are you sure you want to set this venue to {{ pendingStatus }}?</p>
              <div class="flex space-x-4">
                <button 
                  @click="confirmStatusChange" 
                  class="bg-[#9B111E] text-white px-4 py-2 rounded hover:bg-opacity-90">
                  Yes
                </button>
                <button 
                  @click="closeStatusConfirmModal" 
                  class="bg-gray-500 text-white px-4 py-2 rounded hover:bg-opacity-90">
                  Cancel
                </button>
              </div>
            </div>
          </div>
        </div>

        <!-- Add Venue Form -->
            <form v-if="addVenueForm" @submit.prevent="handleSubmit" class="flex justify-center items-center fixed inset-0 bg-gray-800 bg-opacity-50 overflow-y-auto" @click.self="closeAddVenueForm">
            <div class="bg-white w-[500px] p-5 rounded-lg shadow-lg overflow-y-auto">
                <div class="flex justify-between items-center m-3">
                <h1 class="font-semibold text-xl font-raleway text-gray-800">Add Venue</h1>
                </div>
                <div class="border border-gray-500 mt-5 items-center"></div>
                <div class="m-5">
                <span class = "text-red-500">{{ errorMessage }}</span>
                <!-- First Name and Last Name -->
                
                <!-- Venue Name -->
                <div class="mt-5">
                    <label class="text-xs text-gray-600 ml-2">Venue Name</label>
                    <input type="text" class="mt-2 ml-2 p-2 w-full h-10 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:border-blue-700" v-model="venue_name" placeholder="Venue Name" required>
                </div>

                <!-- Location -->
                <div class="mt-5">
                    <label class="text-xs text-gray-600 ml-2">Location</label>
                    <input type="text" class="mt-2 ml-2 p-2 w-full h-10 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:border-blue-700" v-model="location" placeholder="Location" required>
                </div>

                <!-- Description -->
                <div class="mt-5">
                    <label class="text-xs text-gray-600 ml-2">Description</label>
                    <textarea class="mt-2 ml-2 p-2 w-full h-20 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:border-blue-700" v-model="description" placeholder="Description" required></textarea>
                </div>

                <!-- Capacity -->
                <div class="mt-5">
                    <label class="text-xs text-gray-600 ml-2">Capacity</label>
                    <input type="number" class="mt-2 ml-2 p-2 w-full h-10 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:border-blue-700" v-model="venue_capacity" placeholder="Capacity" required>
                </div>

                <!-- Confirm and Cancel Button -->
                <div class="flex justify-center items-center mt-10 space-x-2">
                    <button class="w-20 h-10 bg-gray-300 text-white px-3 py-1 rounded transform-transition duration-300 transform hover:scale-105 hover:bg-gray-400" @click="closeAddVenueForm">
                        Cancel
                    </button>
                    <button type="submit" class="w-20 h-10 bg-blue-500 text-gray-100 font-semibold rounded-lg shadow-md transform-transition duration-300 transform hover:scale-105">
                        Save
                    </button>
                </div>
                </div>
            </div>
        </form>

        <!-- Edit Venue Form -->
        <form v-if="editVenueForm" @submit.prevent="updateVenue" class="flex justify-center items-center fixed inset-0 bg-gray-800 bg-opacity-50 overflow-y-auto" @click.self="closeEditVenueForm">
        <div class="bg-white w-[500px] p-5 rounded-lg shadow-lg overflow-y-auto">
            <div class="flex justify-between items-center m-3">
            <h1 class="font-semibold text-xl font-raleway text-gray-800">Edit Venue</h1>
            <button class="mt-2 bg-red-500 text-white px-3 py-1 rounded transform-transition duration-300 transform hover:scale-105" @click="closeEditVenueForm">
                Close
            </button>
            </div>

            <div class="border border-gray-500 mt-5 items-center"></div>
            <div class="m-5">
            <span>{{ errorMessage }}</span>

            <!-- Venue Name -->
            <div class="mt-5">
                <input type="text" class="mt-2 ml-2 p-2 w-full h-10 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:border-blue-700" v-model="selectedVenue.venue_name" placeholder="Venue Name" required>
            </div>

            <!-- Location -->
            <div class="mt-5">
                <input type="text" class="mt-2 ml-2 p-2 w-full h-10 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:border-blue-700" v-model="selectedVenue.location" placeholder="Location" required>
            </div>

            <!-- Description -->
            <div class="mt-5">
                <textarea class="mt-2 ml-2 p-2 w-full h-20 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:border-blue-700" v-model="selectedVenue.description" placeholder="Description" required></textarea>
            </div>

            <!-- Capacity -->
            <div class="mt-5">
                <input type="number" class="mt-2 ml-2 p-2 w-full h-10 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:border-blue-700" v-model="selectedVenue.venue_capacity" placeholder="Capacity" required>
            </div>

            <!-- Confirm Button -->
            <div class="flex justify-center items-center mt-10 space-x-3">
                <button type="submit" class="w-32 h-10 bg-blue-500 text-gray-100 font-semibold rounded-lg shadow-md transform-transition duration-300 transform hover:scale-105">
                Save Changes
                </button>
            </div>
            </div>
        </div>
        </form>

        <!-- Rate Modal -->
        <div v-if="showRateModal" @click.self="closeRateModal" class="fixed inset-0 bg-gray-800 bg-opacity-50 overflow-y-auto flex justify-center items-center">
          <div class="bg-white p-5 rounded-lg shadow-lg w-[400px]">
            <div class="flex flex-col">
              <div class="flex justify-between items-center mb-4">
                <h2 class="text-xl font-semibold">Set Venue Rate</h2>
                <button @click="closeRateModal" class="text-gray-500 hover:text-gray-700">
                  <span class="text-2xl">&times;</span>
                </button>
              </div>
              <div class="mt-4">
                <input type="number" v-model="venueRate" class="w-full p-2 border rounded" placeholder="Enter rate">
              </div>
              <div class="mt-4 flex justify-end space-x-2">
               
                <button @click="closeRateModal" class="bg-gray-500 text-white px-4 py-2 rounded hover:bg-opacity-90">Cancel</button>
                <button @click="saveVenueRate" class="bg-[#9B111E] text-white px-4 py-2 rounded hover:bg-opacity-90">Save</button>
            </div>
            </div>
          </div>
        </div>

      



</div>
</template>

<script>
import axios from 'axios';

// axios.defaults.baseURL = 'http://127.0.0.1:5000';
axios.defaults.withCredentials = true;

export default {
    name: 'AddVenue',
 data(){
    return {
        showTable: 'Venues',
        venues: [],
        currentPage: 1,
        itemsPerPage: 5,

        addVenueForm: false,
        editVenueForm: false,

        searchTerm: '',
        
        //Venue form inputs
        venue_name: '',
        location: '',
        description: '',
        venue_capacity: '',
        errorMessage: '',

        selectedVenue: {
                venue_name: '',
                location: '',
                description: '',
                venue_capacity: '',
            },

        showInactiveVenuesModal: false,
        showStatusConfirmModal: false,
        pendingStatus: '',
        pendingVenue: null,
        inactiveVenues: [],

        showRateModal: false,
        venueRate: '',

    }



 },
 computed: {
    totalVenues() {
        return this.filteredVenues.length;
    },
    totalPages() {
        return Math.ceil(this.filteredVenues.length / this.itemsPerPage);
    },
    paginatedVenues() {
        const startIndex = (this.currentPage - 1) * this.itemsPerPage;
        const endIndex = startIndex + this.itemsPerPage;
        
        return this.venues.map((venue, index) => ({
            ...venue,
            dummyIndex: index + 1
        })).slice(startIndex, endIndex);
    },
    filteredVenues() {
      if (!this.searchTerm) return this.venues;
      const searchLower = this.searchTerm.toLowerCase().trim();
      return this.venues.filter(venue => {
        const searchableFields = [
          venue.venue_name,
          venue.location,
          String(venue.venue_price),
          String(venue.venue_capacity),
          venue.description
        ];
        return searchableFields.some(field => 
          String(field || '').toLowerCase().includes(searchLower)
        );
      });
    },
},
methods: {
    async fetchVenues() {
        try {
            const token = localStorage.getItem('access_token');
            const response = await axios.get('http://127.0.0.1:5000/venues', {
                headers: {
                    'Authorization': `Bearer ${token}`
                }
            });

            this.venues = response.data.map((venue, index) => ({
                venue_id: venue.venue_id,
                venue_name: venue.venue_name,
                location: venue.location,
                venue_price: venue.venue_price,
                venue_capacity: venue.venue_capacity,
                description: venue.description,
                dummyIndex: index + 1,
            }));

        } catch (error) {
            console.error('Error fetching venues:', error);
            this.errorMessage = 'Failed to fetch venues';
        }
    },

    async handleSubmit() {
        try {
            if (!this.venue_name || !this.location || !this.description || !this.venue_capacity) {
                this.errorMessage = 'All fields are required';
                return;
            }

            const token = localStorage.getItem('access_token');
            const payload = {
                venue_name: this.venue_name,
                location: this.location,
                description: this.description,
                venue_capacity: this.venue_capacity
            };

            const response = await axios.post('http://127.0.0.1:5000/venues', payload, {
                headers: {
                    'Authorization': `Bearer ${token}`
                }
            });

            if (response.status === 201) {
                alert('Venue added successfully!');
                await this.fetchVenues();
                this.closeAddVenueForm();
                this.venue_name = '';
                this.location = '';
                this.description = '';
                this.venue_capacity = '';
            }
        } catch (error) {
            console.error('Error adding venue:', error.response?.data || error.message);
            this.errorMessage = error.response?.data?.message || 'Failed to add venue';
        }
    },

    async updateVenue() {
        try {
            const token = localStorage.getItem('access_token');
            const payload = {
                venue_name: this.selectedVenue.venue_name,
                location: this.selectedVenue.location,
                description: this.selectedVenue.description,
                venue_capacity: this.selectedVenue.venue_capacity,
            };

            const response = await axios.put(`http://127.0.0.1:5000/venues/${this.selectedVenue.venue_id}`, payload, {
                headers: {
                    'Authorization': `Bearer ${token}`
                }
            });

            if (response.status === 200) {
                alert('Venue updated successfully!');
                await this.fetchVenues();
                this.closeEditVenueForm();
            }
        } catch (error) {
            console.error('Error updating venue:', error);
            this.errorMessage = error.response?.data?.message || 'Failed to update venue';
        }
    },


        
    prevVenuesPage() {
        if (this.currentPage > 1) {
            this.currentPage--;
        }
    },
    nextVenuesPage() {
        if (this.currentPage < this.totalPages) {
            this.currentPage++;
        }
    },
    changeVenuesPage(page) {
        this.currentPage = page;
    },
    editVenueBtn(index) {
        // Handle edit action for venue
        console.log(`Edit venue at index: ${index}`);
    },

    addVenueBtn()
    {
        this.addVenueForm = true;
    },
    closeAddVenueForm()
    {
        this.addVenueForm = false;
        this.venue_name = '';
        this.location = '';
        this.description = '';
        this.venue_capacity = '';
        this.errorMessage = '';
      
    },

    editVenueBtn(index) {
            this.editVenueForm = true;
            const selectedVenue = this.venues[index];
            if (selectedVenue) {
                this.selectedVenue = { ...selectedVenue }; // Ensure selectedVenue is deeply copied
            } else {
                console.error('Invalid venue selected:', index);
            }
        },

        closeEditVenueForm() {
            this.editVenueForm = false;
            this.selectedVenue = {
                venue_name: '',
                location: '',
                description: '',
                venue_capacity: '',
            }; // Reset the form fields
            this.errorMessage = '';
        },

        formatPrice(price) {
            if (price === null || price === undefined || typeof price === 'object' || isNaN(price)) {
                return 'N/A'; // Return a fallback if price is invalid
            }
            // Ensure price is treated as a number, round to 2 decimal places, and format with commas
            return parseFloat(price).toFixed(2).replace(/\d(?=(\d{3})+\.)/g, '$&,');
        },


        async showInactiveVenues() {
          try {
            const token = localStorage.getItem('access_token');
            const response = await axios.get('http://127.0.0.1:5000/inactive-venues', {
              headers: {
                Authorization: `Bearer ${token}`,
              },
            });

            this.inactiveVenues = response.data;
            this.showInactiveVenuesModal = true;
          } catch (error) {
            console.error("Error fetching inactive venues:", error);
            alert("Error fetching inactive venues. Please try again.");
          }
        },

        closeInactiveVenuesModal() {
          this.showInactiveVenuesModal = false;
          this.inactiveVenues = [];
        },

        toggleVenueStatus(venue) {
          this.pendingVenue = venue;
          this.pendingStatus = venue.status === 'Active' ? 'Inactive' : 'Active';
          this.showStatusConfirmModal = true;
        },

        closeStatusConfirmModal() {
          this.showStatusConfirmModal = false;
          this.pendingVenue = null;
          this.pendingStatus = '';
        },

        async confirmStatusChange() {
          try {
            const token = localStorage.getItem('access_token');
            
            const response = await axios.put(
              `http://127.0.0.1:5000/toggle-venue-status/${this.pendingVenue.venue_id}`,
              {},
              {
                headers: {
                  Authorization: `Bearer ${token}`,
                },
              }
            );

            if (response.status === 200) {
              if (response.data.new_status === 'Inactive') {
                const index = this.venues.findIndex(v => v.venue_id === this.pendingVenue.venue_id);
                if (index !== -1) {
                  this.venues.splice(index, 1);
                }
                alert('Venue has been set to Inactive');
              } else {
                const index = this.inactiveVenues.findIndex(v => v.venue_id === this.pendingVenue.venue_id);
                if (index !== -1) {
                  this.inactiveVenues.splice(index, 1);
                }
                await this.fetchVenues();
                alert('Venue has been set to Active');
              }
              this.closeStatusConfirmModal();
            }
          } catch (error) {
            console.error("Error toggling venue status:", error);
            if (error.response) {
              alert(error.response.data.message);
            } else {
              alert("Error updating venue status. Please try again.");
            }
            this.closeStatusConfirmModal();
          }
        },


        closeRateModal() {
            this.showRateModal = false;
            this.venueRate = '';
            this.selectedVenue = null;
        },

        async saveVenueRate() {
            try {
                const token = localStorage.getItem('access_token');
                
                if (!this.selectedVenue || !this.selectedVenue.venue_id) {
                    alert("Venue ID is missing or invalid.");
                    return;
                }

                const response = await axios.put(
                    `http://127.0.0.1:5000/update-venue-price/${this.selectedVenue.venue_id}`,
                    {
                        price: this.venueRate
                    },
                    {
                        headers: {
                            Authorization: `Bearer ${token}`,
                        },
                    }
                );

                if (response.status === 200) {
                    alert("Venue rate updated successfully!");
                    
                    // Update the venues list with new price
                    const index = this.venues.findIndex(
                        (venue) => venue.venue_id === this.selectedVenue.venue_id
                    );
                    if (index !== -1) {
                        this.venues[index].venue_price = this.venueRate;
                    }
                    
                    this.closeRateModal();
                }
            } catch (error) {
                console.error("Error updating venue rate:", error);
                if (error.response) {
                    alert(error.response.data.message);
                } else {
                    alert("Error updating venue rate. Please try again.");
                }
            }
        },


},

    mounted() {
        this.fetchVenues();
    },



}


</script>

<style scoped>
</style>