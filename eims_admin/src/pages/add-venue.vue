<template>
<div class="bg-gray-200 w-full h-full overflow-y-auto">
    <div class="w-full h-[65px] bg-gray-100 mt-2 flex items-center justify-between px-5 shadow-lg">
    <h1 class="font-amaticBold font-extraLight text-3xl">
        Add Venue
    </h1>
    </div>

    <div class="flex flex-row items-center m-5 space-x-5">
    <div class="flex justify-start w-52 h-20 bg-white rounded-lg shadow-lg px-2 items-center border-l-2 border-green-400 space-x-5">
        <img class="w-auto h-12" src="/img/venues.png" alt="Vendor Image">
        <h2 class="font-amaticRegular text-4xl font-bold mb-0"> {{ totalVenues }} <span class = "text-sm antialiased text-gray-600">venues</span></h2>
    </div>
</div>

            <div class="flex flex-row justify-between items-center m-5 my-5">
            <div class = "flex">
            <button :class="[ 
                'flex justify-center items-center w-28 h-10 m-2 font-raleway font-semibold rounded-lg shadow-lg transition-transform duration-300 transform hover:scale-105', 
                { 'bg-white text-teal-800': showTable === 'Venues', 'bg-gray-800 text-white': showTable !== 'Venues' } 
            ]" @click="showTable = 'Venues'">
                Venues
            </button>
            </div>
            <button class = "mr-2 w-28 h-10 bg-blue-600 font-semibold text-gray-100 font-quicksand rounded-full shadow-lg 
            transition-transform duration-300 transform hover:scale-105" @click="addVenueBtn">
            + Add Venue
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
                            <th scope="col" class="px-2 py-3">Price</th>
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
                            <td class="px-1 py-3 hidden sm:table-cell">{{ venue.venue_price }}</td>
                            <td class="px-1 py-3 hidden sm:table-cell">
                                <button
                                    class="h-8 w-12 bg-blue-900 font-amaticBold font-medium text-sm rounded-md text-white hover:bg-blue-600"
                                    @click="editVenueBtn(index)">
                                    Edit
                                </button>
                            </td>
                        </tr>
                    </tbody>
                </table>

                <!-- Pagination Controls -->
                <div class="flex justify-center space-x-2 mt-4 mb-6">
                    <button @click="prevVenuesPage" :disabled="currentVenuesPage === 1"
                        class="px-3 py-1 bg-blue-900 text-white rounded-md hover:bg-blue-600 disabled:opacity-50 text-md">Previous</button>
                    <button v-for="page in totalVenuesPages" :key="page" @click="changeVenuesPage(page)"
                        :class="{'bg-blue-900': currentVenuesPage === page, 'bg-gray-300': currentVenuesPage !== page}"
                        class="px-3 py-1 text-white rounded-md hover:bg-blue-600 text-xs">
                        {{ page }}
                    </button>
                    <button @click="nextVenuesPage" :disabled="currentVenuesPage === totalVenuesPages"
                        class="px-3 py-1 bg-blue-900 text-white rounded-md hover:bg-blue-600 disabled:opacity-50 text-xs">Next</button>
                </div>
            </div>
        </div>

        <!-- Add Venue Form -->
            <form v-if="addVenueForm" @submit.prevent="addVenue" class="flex justify-center items-center fixed inset-0 bg-gray-800 bg-opacity-50 overflow-y-auto">
            <div class="bg-white w-[500px] p-5 rounded-lg shadow-lg overflow-y-auto">
                <div class="flex justify-between items-center m-3">
                <h1 class="font-semibold text-xl font-raleway text-gray-800">Add Venue</h1>
                <button class="mt-2 bg-red-500 text-white px-3 py-1 rounded transform-transition duration-300 transform hover:scale-105" @click="closeAddVenueForm">
                    Close
                </button>
                </div>
                <div class="border border-gray-500 mt-5 items-center"></div>
                <div class="m-5">
                <span>{{ errorMessage }}</span>
                <!-- First Name and Last Name -->
                
                <!-- Venue Name -->
                <div class="mt-5">
                    <input type="text" class="mt-2 ml-2 p-2 w-full h-10 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:border-blue-700" v-model="venue_name" placeholder="Venue Name" required>
                </div>

                <!-- Location -->
                <div class="mt-5">
                    <input type="text" class="mt-2 ml-2 p-2 w-full h-10 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:border-blue-700" v-model="location" placeholder="Location" required>
                </div>

                <!-- Price -->
                <div class="mt-5">
                    <input type="number" class="mt-2 ml-2 p-2 w-full h-10 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:border-blue-700" v-model="venue_price" placeholder="Price" required>
                </div>

                <!-- Confirm Button -->
                <div class="flex justify-center items-center mt-10">
                    <button type="submit" class="w-20 h-10 bg-blue-500 text-gray-100 font-semibold rounded-lg shadow-md transform-transition duration-300 transform hover:scale-105">
                    Confirm
                    </button>
                </div>
                </div>
            </div>
        </form>


        <!-- Edit Venue Form -->
        <form v-if="editVenueForm" @submit.prevent="updateVenue" class="flex justify-center items-center fixed inset-0 bg-gray-800 bg-opacity-50 overflow-y-auto">
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

            <!-- Price -->
            <div class="mt-5">
                <input type="number" class="mt-2 ml-2 p-2 w-full h-10 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:border-blue-700" v-model="selectedVenue.venue_price" placeholder="Price" required>
            </div>

            <!-- Confirm Button -->
            <div class="flex justify-center items-center mt-10 space-x-3">
                <button @click.prevent="deleteVenue(selectedVenue.venue_id)" class="w-20 h-10 bg-yellow-500 text-gray-100 font-semibold rounded-lg shadow-md transform-transition duration-300 transform hover:scale-105">
                        Delete
                </button>
                <button type="submit" class="w-20 h-10 bg-blue-500 text-gray-100 font-semibold rounded-lg shadow-md transform-transition duration-300 transform hover:scale-105">
                Confirm
                </button>
            </div>
            </div>
        </div>
        </form>


      




</div>
</template>

<script>
import axios from 'axios';


axios.defaults.withCredentials = true;

export default {
    name: 'AddVenue',
 data(){
    return {
        showTable: 'Venues',
        venues: [],
        currentVenuesPage: 1,
        rowsPerVenuesPage: 10,

        addVenueForm: false,
        editVenueForm: false,
        
        //Venue form inputs
        venue_name: '',
        location: '',
        venue_price: '',
        errorMessage: '',

        selectedVenue: {
                venue_name: '',
                location: '',
                venue_price: '',
            },


    }



 },
 computed: {
    totalVenues() {
        return this.venues.length;
    },
    totalVenuesPages() {
        return Math.ceil(this.venues.length / this.rowsPerVenuesPage);
    },
    paginatedVenues() {
        const start = (this.currentVenuesPage - 1) * this.rowsPerVenuesPage;
        const end = start + this.rowsPerVenuesPage;
        return this.venues.slice(start, end);
    },
},
methods: {
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

                // Populate venues array with data from API
                this.venues = response.data.map((venue, index) => ({
                    venue_id: venue.venue_id,
                    venue_name: venue.venue_name,
                    location: venue.location,
                    venue_price: venue.venue_price, // Ensure these match your `selectedVenue` keys
                    dummyIndex: index + 1,
                }));

            } catch (error) {
                console.error('Error fetching venues:', error.response?.data || error.message);
            }
        },

        async addVenue() {
                try {
                    const token = localStorage.getItem('access_token');
                    if (!token) {
                        this.errorMessage = 'You are not logged in. Please log in to add a venue.';
                        return;
                    }

                    const payload = {
                        venue_name: this.venue_name,
                        location: this.location,
                        venue_price: this.venue_price,
                    };

                    const response = await axios.post('http://127.0.0.1:5000/create-venue', payload, {
                        headers: {
                            'Content-Type': 'application/json',
                            'Authorization': `Bearer ${token}`,
                        },
                        withCredentials: true,
                    });

                    if (response.status === 201) {
                        alert('Venue added successfully!');
                        this.closeAddVenueForm();
                        // Optionally reset fields
                        this.venue_name = '';
                        this.location = '';
                        this.venue_price = '';
                    }
                } catch (error) {
                    console.error('Error adding venue:', error.response?.data || error.message);
                    this.errorMessage = error.response?.data?.error || 'An error occurred while adding the venue.';
                }
            },


            async updateVenue() {
                try {
                const token = localStorage.getItem('access_token');
                if (!token) {
                    this.errorMessage = 'You are not logged in. Please log in to update the venue.';
                    return;
                }

                // Ensure the venue ID is available for updating
                if (!this.selectedVenue.venue_id) {
                    this.errorMessage = 'Venue ID is missing.';
                    return;
                }

                const payload = {
                    venue_name: this.selectedVenue.venue_name,
                    location: this.selectedVenue.location,
                    venue_price: this.selectedVenue.venue_price
                };

                const response = await axios.put(`http://127.0.0.1:5000/update-venue/${this.selectedVenue.venue_id}`, payload, {
                    headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${token}`
                    },
                    withCredentials: true
                });

                if (response.status === 200) {
                    alert('Venue updated successfully!');
                    this.closeEditVenueForm(); // Optionally close the form after success
                    this.fetchVenues(); // Refresh the list of venues
                }
                } catch (error) {
                console.error('Error updating venue:', error.response?.data || error.message);
                this.errorMessage = error.response?.data?.message || 'An error occurred while updating the venue.';
                }
            },

            async deleteVenue(venue_id) {
                try {
                    if (!confirm('Are you sure you want to delete this venue? This action cannot be undone.')) {
                    return;
                    }

                    const token = localStorage.getItem('access_token');
                    if (!token) {
                    alert('You are not logged in. Please log in to delete venues.');
                    return;
                    }

                    const response = await axios.delete(`http://127.0.0.1:5000/delete-venue/${venue_id}`, {
                    headers: {
                        'Authorization': `Bearer ${token}`,
                    },
                    });

                    if (response.status === 200) {
                    alert('Venue deleted successfully!');
                    // Remove the deleted venue from the venues array
                    this.venues = this.venues.filter(venue => venue.venue_id !== venue_id);
                    this.closeEditVenueForm(); // Optionally close the form
                    } else {
                    alert('Failed to delete venue.');
                    }
                } catch (error) {
                    console.error('Error deleting venue:', error);
                    if (error.response) {
                    alert(`Error deleting venue: ${error.response.data.message}`);
                    } else {
                    alert('Error deleting venue. Please try again.');
                    }
                }
            },

        
    prevVenuesPage() {
        if (this.currentVenuesPage > 1) {
            this.currentVenuesPage--;
        }
    },
    nextVenuesPage() {
        if (this.currentVenuesPage < this.totalVenuesPages) {
            this.currentVenuesPage++;
        }
    },
    changeVenuesPage(page) {
        this.currentVenuesPage = page;
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
        this.venue_price = '';
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
                venue_price: '',
            }; // Reset the form fields
            this.errorMessage = '';
        },


},

    mounted() {
        this.fetchVenues();
    },



}


</script>

<style scoped>
</style>