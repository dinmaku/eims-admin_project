<template>
    <div class="bg-gray-200 w-full h-full overflow-y-auto">
        <div class="w-full h-[65px] bg-gray-100 mt-2 flex items-center justify-between px-5 shadow-lg">
        <h1 class="font-amaticBold font-extraLight text-3xl">
            Other Inclusions
        </h1>
        <button class="bg-[#9B111E] text-white px-3 py-2 rounded shadow-lg 
        transition-transform duration-300 transform hover:scale-105 font-semibold" @click="showInactiveServicesModal = true">
            Inactive Inclusions
            </button>
        </div>

        <div class="flex flex-row items-center m-5 space-x-5">
        <div class="flex justify-start w-52 h-20 bg-white rounded-lg shadow-lg px-2 items-center border-l-2 border-green-400 space-x-5">
            <h2 class="font-amaticRegular text-4xl font-bold mb-0"> {{ totalServices }} <span class = "text-sm antialiased text-gray-600">inclusions</span></h2>
        </div>
    </div>

        <div class="flex flex-row justify-between items-center m-5 my-7">
            <form class="flex items-center w-[300px]">
              <label for="voice-search" class="sr-only">Search</label>
              <div class="relative w-full">
                <div class="flex absolute inset-y-0 left-0 items-center pl-3 pointer-events-none">
                  <svg aria-hidden="true" class="w-5 h-auto text-gray-500 dark:text-gray-400" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                    <path fill-rule="evenodd" d="M8 4a4 4 0 100 8 4 4 0 000-8zM2 8a6 6 0 1110.89 3.476l4.817 4.817a1 1 0 01-1.414 1.414l-4.816-4.816A6 6 0 012 8z" clip-rule="evenodd"></path>
                  </svg>
                </div>
                <input type="text" id="search-bar" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full pl-10 p-2.5  dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="Search Other Inclusions..." required v-model="searchTerm">
                <router-link to="/" class="flex absolute inset-y-0 right-0 items-center pr-3">
                  <svg aria-hidden="true" class="w-4 h-4 text-gray-500 dark:text-gray-400 hover:text-gray-900 dark:hover:text-white" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                  </svg>
                </router-link>
              </div>
        </form>
             <button class="mr-2 w-44 h-10 bg-[#9B111E] font-semibold text-gray-100 font-quicksand rounded-md shadow-lg 
            transition-transform duration-300 transform hover:scale-105" @click="addServiceBtn">
            Add Other Inclusions
            </button>
        </div>

        <!--- Additional Services Table --->

        <div v-if="showTable === 'Services'" class="relative shadow-md sm:rounded-xl w-full max-w-[1170px] h-[200] ml-5 mt-2 font-amaticBold mb-10">
            <div class="overflow-x-auto">
                <table class="w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400 mb-4 max-h-30 table-fixed">
                    <thead class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
                        <tr>
                            <th scope="col" class="w-16 px-2 py-3">#</th>
                            <th scope="col" class="w-52 px-2 py-3">Inclusion Name</th>
                            <th scope="col" class="w-96 px-2 py-3">Description</th>
                            <th scope="col" class="w-36 px-2 py-3">Price</th>
                            <th scope="col" class="w-28 px-2 py-3">Action</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr
                            v-for="(service, index) in paginatedServices"
                            :key="service.add_service_id"
                            class="border-b dark:border-gray-700 odd:bg-white odd:dark:bg-gray-900 even:bg-gray-50 even:dark:bg-gray-800">
                            <th scope="row" class="w-16 px-2 py-3 font-medium text-gray-900 whitespace-nowrap dark:text-white">{{ service.dummyIndex }}</th>
                            <td class="w-52 px-2 py-3 truncate">{{ service.add_service_name }}</td>
                            <td class="w-96 px-2 py-3 truncate">{{ service.add_service_description }}</td>
                            <td class="w-36 px-2 py-3 truncate">{{ formatPrice(service.add_service_price) }} php</td>
                            <td class="w-28 px-2 py-3">
                                <div class="flex items-center space-x-2">
                                    <button
                                        class="p-2 hover:opacity-80 transform hover:scale-110 transition-transform duration-200"
                                        @click="editServiceBtn(index)"
                                        title="Update Other Inclusions Info">
                                        <img src="/img/update2.png" alt="Update" class="w-5 h-5">
                                    </button>
                                    <button
                                        class="p-2 hover:opacity-80 transform hover:scale-110 transition-transform duration-200"
                                        @click="showRateModal = true; selectedService = service"
                                        title="Set Rate">
                                        <img src="/img/rate2.png" alt="Set Rate" class="w-5 h-5">
                                    </button>
                                    <button
                                        class="p-2 hover:opacity-80 transform hover:scale-110 transition-transform duration-200"
                                        @click="openStatusConfirmModal(service, 'Inactive')"
                                        title="Deactivate">
                                        <img src="/img/inactive2.png" alt="Set Inactive" class="w-5 h-5">
                                    </button>
                                </div>
                            </td>
                        </tr>
                    </tbody>
                </table>

                <!-- Pagination Controls -->
                <div class="flex justify-center space-x-2 mt-4 mb-6">
                    <button @click="prevServicesPage" :disabled="currentServicesPage === 1"
                        class="px-3 py-1 bg-[#9B111E] text-white rounded-md hover:bg-[#B73A45] disabled:opacity-50 text-sm">Previous</button>
                    <button v-for="page in totalServicesPages" :key="page" @click="changeServicesPage(page)"
                        :class="{'bg-[#9B111E]': currentServicesPage === page, 'bg-gray-300 ': currentServicesPage !== page}"
                        class="px-3 py-1 text-white rounded-md hover:bg-[#B73A45] text-xs">
                        {{ page }}
                    </button>
                    <button @click="nextServicesPage" :disabled="currentServicesPage === totalServicesPages"
                        class="px-3 py-1 bg-[#9B111E] text-white rounded-md hover:bg-[#B73A45] disabled:opacity-50 text-xs">Next</button>
                </div>
            </div>
        </div>

        <!-- Add Service Form -->
        <form v-if="addServiceForm" @submit.prevent="submitAddServiceForm" class="flex justify-center items-center fixed inset-0 bg-gray-800 bg-opacity-50 overflow-y-auto" @click.self="closeAddServiceForm">
            <div class="bg-white w-[500px] p-5 rounded-lg shadow-lg overflow-y-auto">
                <div class="flex justify-between items-center m-3">
                    <h1 class="font-semibold text-xl font-raleway text-gray-800">Add Other Inclusions</h1>
                </div>
                <div class="border border-gray-500 mt-5 items-center"></div>
                <div class="m-5">
                    <span>{{ errorMessage }}</span>
                    
                    <!-- Service Name -->
                    <div class="flex flex-col mt-5">
                        <label class="text-xs text-gray-600 text-start">Inclusion Name</label>
                        <input type="text" class="mt-2 p-2 w-full h-10 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:border-blue-700" v-model.trim="add_service_name" placeholder="Service Name" required>
                    </div>

                    <!-- Description -->
                    <div class="flex flex-col mt-5">
                        <label class="text-xs text-gray-600 text-start">Description</label>
                        <textarea class="mt-2 p-2 w-full h-32 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:border-blue-700" v-model.trim="add_service_description" placeholder="Description" required></textarea>
                    </div>

                    <!-- Confirm Button -->
                    <div class="flex justify-end items-center mt-10 space-x-2">
                        <button class="w-20 h-10 bg-gray-300 text-white px-3 py-1 rounded transform-transition duration-300 transform hover:scale-105 hover:bg-gray-400" @click="closeAddServiceForm">
                        Cancel
                         </button>
                        <button type="submit" class="w-20 h-10 bg-blue-500 text-gray-100 font-semibold rounded-lg shadow-md transform-transition duration-300 transform hover:scale-105">
                        Save
                        </button>
                    </div>
                </div>
            </div>
        </form>

        <!-- Edit Service Form -->
        <form v-if="editServiceForm" @submit.prevent="updateService" class="flex justify-center items-center fixed inset-0 bg-gray-800 bg-opacity-50 overflow-y-auto" @click.self="closeEditServiceForm">
            <div class="bg-white w-[500px] p-5 rounded-lg shadow-lg overflow-y-auto">
                <div class="flex justify-between items-center m-3">
                    <h1 class="font-semibold text-xl font-raleway text-gray-800">Update Other Inclusions</h1>
                </div>

                <div class="border border-gray-500 mt-5 items-center"></div>
                <div class="m-5">
                    <span>{{ errorMessage }}</span>

                    <!-- Service Name -->
                    <div class="flex flex-col mt-5">
                        <label class="text-xs text-gray-600 text-start">Inclusion Name</label>
                        <input type="text" class="mt-2 p-2 w-full h-10 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:border-blue-700" v-model="selectedService.add_service_name" placeholder="Service Name" required>
                    </div>

                    <!-- Description -->
                    <div class="flex flex-col mt-5">
                        <label class="text-xs text-gray-600 text-start">Description</label>
                        <textarea class="mt-2 p-2 w-full h-32 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:border-blue-700" v-model="selectedService.add_service_description" placeholder="Description" required></textarea>
                    </div>

                    <!-- Confirm Button -->
                    <div class="flex justify-end items-center mt-10 space-x-2">
                        <button class="w-20 h-10 bg-gray-300 text-white px-3 py-1 rounded transform-transition duration-300 transform hover:scale-105 hover:bg-gray-400" @click="closeEditServiceForm">
                        Cancel
                        </button>
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
                        <h2 class="text-xl font-semibold">Set Inclusion Rate</h2>
                        <button @click="closeRateModal" class="text-gray-500 hover:text-gray-700">
                            <span class="text-2xl">&times;</span>
                        </button>
                    </div>
                    <div class="mt-4">
                        <input type="number" v-model="serviceRate" class="w-full p-2 border rounded" placeholder="Enter rate">
                    </div>
                    <div class="mt-4 flex justify-end space-x-2">
                        <button @click="closeRateModal" class="bg-gray-500 text-white px-4 py-2 rounded hover:bg-opacity-90">Cancel</button>
                        <button @click="saveServiceRate" class="bg-blue-500 text-white px-4 py-2 rounded hover:bg-opacity-90">Save</button>
                    </div>
                </div>
            </div>
        </div>

        <!-- Inactive Services Modal -->
        <div v-if="showInactiveServicesModal" @click.self="closeInactiveServicesModal" class="fixed inset-0 bg-gray-800 bg-opacity-50 overflow-y-auto flex justify-center items-center">
            <div class="bg-white p-5 rounded-lg shadow-lg w-[800px]">
                <div class="flex flex-col">
                    <div class="flex justify-between items-center mb-4">
                        <h2 class="text-xl font-semibold">Inactive Services</h2>
                        <button @click="closeInactiveServicesModal" class="text-gray-500 hover:text-gray-700">
                            <span class="text-2xl">&times;</span>
                        </button>
                    </div>
                    <div class="mt-4">
                        <table class="w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400 mb-4">
                            <thead class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
                                <tr>
                                    <th scope="col" class="px-2 py-3">#</th>
                                    <th scope="col" class="px-2 py-3">Service Name</th>
                                    <th scope="col" class="px-2 py-3">Description</th>
                                    <th scope="col" class="px-2 py-3">Rate</th>
                                    <th scope="col" class="px-2 py-3">Action</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr v-for="(service, index) in inactiveServices" 
                                    :key="service.add_service_id"
                                    class="border-b dark:border-gray-700 odd:bg-white odd:dark:bg-gray-900 even:bg-gray-50 even:dark:bg-gray-800">
                                    <th scope="row" class="px-2 py-3 font-medium text-gray-900 whitespace-nowrap dark:text-white">
                                        {{ index + 1 }}
                                    </th>
                                    <td class="px-2 py-3">{{ service.add_service_name }}</td>
                                    <td class="px-2 py-3">{{ service.add_service_description }}</td>
                                    <td class="px-2 py-3">{{ formatPrice(service.add_service_price) }} php</td>
                                    <td class="px-2 py-3">
                                        <button
                                            class="p-2 hover:opacity-80 transform hover:scale-110 transition-transform duration-200"
                                            @click="openStatusConfirmModal(service, 'Active')"
                                            title="Activate">
                                            <img src="/img/active2.png" alt="Set Active" class="w-5 h-5">
                                        </button>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>

        <!-- Status Confirmation Modal -->
        <div v-if="showStatusConfirmModal" @click.self="closeStatusConfirmModal" class="fixed inset-0 bg-gray-800 bg-opacity-50 overflow-y-auto flex justify-center items-center z-50">
            <div class="bg-white p-5 rounded-lg shadow-lg w-[400px]">
                <div class="flex flex-col items-center">
                    <h2 class="text-xl font-semibold mb-4">Confirm Status Change</h2>
                    <p class="mb-6 text-center">Are you sure you want to set this inclusion to {{ pendingStatus }}?</p>
                    <div class="flex space-x-4">  
                        <button 
                            @click="closeStatusConfirmModal" 
                            class="bg-gray-500 text-white px-4 py-2 rounded hover:bg-opacity-90">
                            Cancel
                        </button>
                        <button 
                            @click="confirmStatusChange" 
                            class="bg-blue-500 text-white px-4 py-2 rounded hover:bg-opacity-90">
                            Yes
                        </button>
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
    name: 'AdditionalServices',
    data() {
        return {
            showTable: 'Services',
            searchTerm: '',
            addServiceForm: false,
            editServiceForm: false,
            showRateModal: false,
            showInactiveServicesModal: false,
            showStatusConfirmModal: false,
            serviceRate: '',
            selectedService: null,
            inactiveServices: [],
            pendingStatus: '',
            serviceToToggle: null,
            errorMessage: '',
            currentServicesPage: 1,
            servicesPerPage: 5,
            add_service_name: '',
            add_service_description: '',
            totalServices: 0,
            services: []
        };
    },
    computed: {
        totalServicesPages() {
            return Math.ceil(this.filteredAdditionalServices.length / this.servicesPerPage);
        },
        paginatedServices() {
            const start = (this.currentServicesPage - 1) * this.servicesPerPage;
            const end = start + this.servicesPerPage;
            const paginatedList = this.filteredAdditionalServices.slice(start, end);
            
            // Add dummy index for display
            return paginatedList.map((service, index) => ({
                ...service,
                dummyIndex: start + index + 1
            }));
        },
        filteredAdditionalServices() {
            if (!this.searchTerm) {
                return this.services;
            }
            const searchLower = this.searchTerm.toLowerCase();
            return this.services.filter(service => 
                service.add_service_name.toLowerCase().includes(searchLower) ||
                service.add_service_description.toLowerCase().includes(searchLower)
            );
        }
    },
    methods: {
        formatPrice(price) {
            if (!price) return '0.00';
            return parseFloat(price).toFixed(2);
        },
        openStatusConfirmModal(service, status) {
            this.serviceToToggle = service;
            this.pendingStatus = status;
            this.showStatusConfirmModal = true;
        },

        closeStatusConfirmModal() {
            this.showStatusConfirmModal = false;
            this.serviceToToggle = null;
            this.pendingStatus = '';
        },

        async confirmStatusChange() {
            if (this.serviceToToggle) {
                await this.toggleServiceStatus(this.serviceToToggle);
                this.closeStatusConfirmModal();
            }
        },

        async fetchServices() {
            try {
                const token = localStorage.getItem('access_token');
                if (!token) {
                    alert('You are not logged in. Please log in to view services.');
                    return;
                }

                const response = await axios.get('http://127.0.0.1:5000/additional-services', {
                    headers: {
                        'Content-Type': 'application/json',
                        'Authorization': `Bearer ${token}`,
                    },
                    withCredentials: true,
                });

                // Populate services array with data from API
                this.services = response.data;
                this.totalServices = response.data.length;

            } catch (error) {
                console.error('Error fetching services:', error.response?.data || error.message);
            }
        },

        async submitAddServiceForm() {
            try {
                const token = localStorage.getItem('access_token');
                if (!token) {
                    this.errorMessage = 'Authentication token not found';
                    return;
                }

                if (!this.add_service_name || !this.add_service_description) {
                    this.errorMessage = 'Please fill in all required fields';
                    return;
                }

                const response = await axios.post('http://127.0.0.1:5000/additional-services', {
                    add_service_name: this.add_service_name,
                    add_service_description: this.add_service_description
                }, {
                    headers: {
                        'Content-Type': 'application/json',
                        'Authorization': `Bearer ${token}`
                    }
                });

                if (response.status === 200) {
                    alert('Service created successfully!');
                    this.closeAddServiceForm();
                    await this.fetchServices();
                }
            } catch (error) {
                console.error('Error creating service:', error.response?.data || error.message);
                this.errorMessage = error.response?.data?.error || 'Failed to create service';
            }
        },

        async updateService() {
            try {
                const token = localStorage.getItem('access_token');
                // Ensure the service ID is available for updating
                if (!this.selectedService.add_service_id) {
                    this.errorMessage = 'Service ID is missing.';
                    return;
                }

                const payload = {
                    add_service_name: this.selectedService.add_service_name.trim(),
                    add_service_description: this.selectedService.add_service_description.trim(),
                    add_service_price: this.selectedService.add_service_price,
                };

                const response = await axios.put(`http://127.0.0.1:5000/update-service/${this.selectedService.add_service_id}`, payload, {
                    headers: {
                        'Content-Type': 'application/json',
                        'Authorization': `Bearer ${token}`,
                    },
                    withCredentials: true,
                });

                if (response.status === 200) {
                    alert('Service updated successfully!');
                    this.closeEditServiceForm(); // Optionally close the form after success
                    this.fetchServices(); // Refresh the list of services
                }
            } catch (error) {
                console.error('Error updating service:', error.response?.data || error.message);
                this.errorMessage = error.response?.data?.message || 'An error occurred while updating the service.';
            }
        },

        prevServicesPage() {
            if (this.currentServicesPage > 1) {
                this.currentServicesPage--;
            }
        },
        nextServicesPage() {
            if (this.currentServicesPage < this.totalServicesPages) {
                this.currentServicesPage++;
            }
        },
        changeServicesPage(page) {
            this.currentServicesPage = page;
        },
        editServiceBtn(index) {
            // Handle edit action for service
            console.log(`Edit service at index: ${index}`);
        },

        addServiceBtn() {
            this.addServiceForm = true;
            // Initialize form fields
            this.add_service_name = '';
            this.add_service_description = '';
            this.errorMessage = '';
        },
        closeAddServiceForm() {
            this.addServiceForm = false;
            // Reset form fields
            this.add_service_name = '';
            this.add_service_description = '';
            this.errorMessage = '';
        },

        editServiceBtn(index) {
            this.editServiceForm = true;
            const selectedService = this.services[index];
            if (selectedService) {
                this.selectedService = { ...selectedService }; // Ensure selectedService is deeply copied
            } else {
                console.error('Invalid service selected:', index);
            }
        },

        closeEditServiceForm() {
            this.editServiceForm = false;
            this.selectedService = {
                add_service_id: null,
                add_service_name: '',
                add_service_description: '',
                add_service_price: null
            }; // Reset the form fields
            this.errorMessage = '';
        },
        async fetchInactiveServices() {
            try {
                const token = localStorage.getItem('access_token');
                const response = await axios.get('http://127.0.0.1:5000/inactive-additional-services', {
                    headers: {
                        Authorization: `Bearer ${token}`
                    }
                });
                this.inactiveServices = response.data;
            } catch (error) {
                console.error('Error fetching inactive services:', error);
                alert('Failed to fetch inactive services. Please try again.');
            }
        },

        async toggleServiceStatus(service) {
            try {
                const token = localStorage.getItem('access_token');
                const response = await axios.put(
                    `http://127.0.0.1:5000/toggle-additional-service-status/${service.add_service_id}`,
                    {},
                    {
                        headers: {
                            Authorization: `Bearer ${token}`
                        }
                    }
                );

                if (response.status === 200) {
                    // Show success message
                    alert("Service status updated successfully!");
                    // Refresh both active and inactive services
                    await this.fetchServices();
                    await this.fetchInactiveServices();
                    // Close modal if it was opened from inactive services list
                    if (this.showInactiveServicesModal) {
                        this.closeInactiveServicesModal();
                    }
                }
            } catch (error) {
                console.error('Error toggling service status:', error);
                alert('Failed to update service status. Please try again.');
            }
        },

        closeRateModal() {
            this.showRateModal = false;
            this.serviceRate = '';
            this.selectedService = null;
        },

        async saveServiceRate() {
            try {
                const token = localStorage.getItem('access_token');
                
                if (!this.selectedService || !this.selectedService.add_service_id) {
                    alert("Service ID is missing or invalid.");
                    return;
                }

                const response = await axios.put(
                    `http://127.0.0.1:5000/update-additional-service-price/${this.selectedService.add_service_id}`,
                    {
                        price: this.serviceRate
                    },
                    {
                        headers: {
                            Authorization: `Bearer ${token}`
                        }
                    }
                );

                if (response.status === 200) {
                    alert("Service rate updated successfully!");
                    await this.fetchServices();
                    this.closeRateModal();
                }
            } catch (error) {
                console.error("Error updating service rate:", error);
                alert("Error updating service rate. Please try again.");
            }
        },

        closeInactiveServicesModal() {
            this.showInactiveServicesModal = false;
        },
    },

    mounted() {
        this.fetchServices();
        this.fetchInactiveServices();
    }
}
</script>

<style scoped>
</style>