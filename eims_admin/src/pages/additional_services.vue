<template>
    <div class="bg-gray-200 w-full h-full overflow-y-auto">
        <div class="w-full h-[65px] bg-gray-100 mt-2 flex items-center justify-between px-5 shadow-lg">
        <h1 class="font-amaticBold font-extraLight text-3xl">
            Additional Services
        </h1>
        </div>

        <div class="flex flex-row items-center m-5 space-x-5">
        <div class="flex justify-start w-52 h-20 bg-white rounded-lg shadow-lg px-2 items-center border-l-2 border-green-400 space-x-5">
            <img class="w-auto h-12" src="/img/bar-counter.png" alt="Service Image">
            <h2 class="font-amaticRegular text-4xl font-bold mb-0"> {{ totalServices }} <span class = "text-sm antialiased text-gray-600">services</span></h2>
        </div>
    </div>

        <div class="flex flex-row justify-between items-center m-5 my-7">
            <div class="flex">
                <button class="mr-2 w-28 h-10 bg-[#9B111E] font-semibold text-gray-100 font-quicksand rounded-full shadow-lg 
                transition-transform duration-300 transform hover:scale-105" @click="addServiceBtn">
                + Add Service
                </button>
            </div>
        </div> 

        <!--- Additional Services Table --->

        <div v-if="showTable === 'Services'" class="relative shadow-md sm:rounded-xl w-[1170px] h-[200] ml-5 mt-2 font-amaticBold mb-10">
            <div class="overflow-x-auto">
                <table class="w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400 mb-4 max-h-30">
                    <thead class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
                        <tr>
                            <th scope="col" class="px-2 py-3">#</th>
                            <th scope="col" class="px-2 py-3">Service Name</th>
                            <th scope="col" class="px-2 py-3">Description</th>
                            <th scope="col" class="px-2 py-3">Price</th>
                            <th scope="col" class="px-2 py-3">Action</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr
                            v-for="(service, index) in paginatedServices"
                            :key="service.add_service_id"
                            class="border-b dark:border-gray-700 odd:bg-white odd:dark:bg-gray-900 even:bg-gray-50 even:dark:bg-gray-800">
                            <th scope="row" class="px-2 py-3 font-medium text-gray-900 whitespace-nowrap dark:text-white">{{ service.dummyIndex }}</th>
                            <td class="px-1 py-3 hidden sm:table-cell">{{ service.add_service_name }}</td>
                            <td class="px-1 py-3 hidden sm:table-cell">{{ service.add_service_description }}</td>
                            <td class="px-1 py-3 hidden sm:table-cell">{{ service.add_service_price }} php</td>
                            <td class="px-1 py-3 hidden sm:table-cell">
                                <button
                                    class="h-8 w-12 bg-[#9B111E] font-amaticBold font-medium text-sm rounded-md text-white hover:bg-[#B73A45] "
                                    @click="editServiceBtn(index)">
                                    Edit
                                </button>
                            </td>
                        </tr>
                    </tbody>
                </table>

                <!-- Pagination Controls -->
                <div class="flex justify-center space-x-2 mt-4 mb-6">
                    <button @click="prevServicesPage" :disabled="currentServicesPage === 1"
                        class="px-3 py-1 bg-[#9B111E] text-white rounded-md hover:bg-[#B73A45] disabled:opacity-50 text-md">Previous</button>
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
        <form v-if="addServiceForm" @submit.prevent="addService" class="flex justify-center items-center fixed inset-0 bg-gray-800 bg-opacity-50 overflow-y-auto" @click.self="closeAddServiceForm">
            <div class="bg-white w-[500px] p-5 rounded-lg shadow-lg overflow-y-auto">
                <div class="flex justify-between items-center m-3">
                    <h1 class="font-semibold text-xl font-raleway text-gray-800">Add Service</h1>
                    <button class="mt-2 bg-red-500 text-white px-3 py-1 rounded transform-transition duration-300 transform hover:scale-105" @click="closeAddServiceForm">
                        Close
                    </button>
                </div>
                <div class="border border-gray-500 mt-5 items-center"></div>
                <div class="m-5">
                    <span>{{ errorMessage }}</span>
                    
                    <!-- Service Name -->
                    <div class="mt-5">
                        <input type="text" class="mt-2 ml-2 p-2 w-full h-10 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:border-blue-700" v-model.trim="add_service_name" placeholder="Service Name" required>
                    </div>

                    <!-- Description -->
                    <div class="mt-5">
                        <textarea class="mt-2 ml-2 p-2 w-full h-32 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:border-blue-700" v-model.trim="add_service_description" placeholder="Description" required></textarea>
                    </div>

                    <!-- Price -->
                    <div class="mt-5">
                        <input type="number" class="mt-2 ml-2 p-2 w-full h-10 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:border-blue-700" v-model.number="add_service_price" placeholder="Price" required>
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

        <!-- Edit Service Form -->
        <form v-if="editServiceForm" @submit.prevent="updateService" class="flex justify-center items-center fixed inset-0 bg-gray-800 bg-opacity-50 overflow-y-auto" @click.self="closeEditServiceForm">
            <div class="bg-white w-[500px] p-5 rounded-lg shadow-lg overflow-y-auto">
                <div class="flex justify-between items-center m-3">
                    <h1 class="font-semibold text-xl font-raleway text-gray-800">Edit Service</h1>
                    <button class="mt-2 bg-red-500 text-white px-3 py-1 rounded transform-transition duration-300 transform hover:scale-105" @click="closeEditServiceForm">
                        Close
                    </button>
                </div>

                <div class="border border-gray-500 mt-5 items-center"></div>
                <div class="m-5">
                    <span>{{ errorMessage }}</span>

                    <!-- Service Name -->
                    <div class="mt-5">
                        <input type="text" class="mt-2 ml-2 p-2 w-full h-10 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:border-blue-700" v-model="selectedService.add_service_name" placeholder="Service Name" required>
                    </div>

                    <!-- Description -->
                    <div class="mt-5">
                        <textarea class="mt-2 ml-2 p-2 w-full h-32 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:border-blue-700" v-model="selectedService.add_service_description" placeholder="Description" required></textarea>
                    </div>

                    <!-- Price -->
                    <div class="mt-5">
                        <input type="number" class="mt-2 ml-2 p-2 w-full h-10 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:border-blue-700" v-model="selectedService.add_service_price" placeholder="Price" required>
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
            services: [],
            currentServicesPage: 1,
            rowsPerServicesPage: 5,

            addServiceForm: false,
            editServiceForm: false,

            // Service form inputs
            add_service_name: '',
            add_service_description: '',
            add_service_price: null,
            errorMessage: '',

            selectedService: {
                add_service_id: null,
                add_service_name: '',
                add_service_description: '',
                add_service_price: null
            }
        };
    },
    computed: {
        totalServices() {
            return this.services.length;
        },
        totalServicesPages() {
            return Math.ceil(this.services.length / this.rowsPerServicesPage);
        },
        paginatedServices() {
            const start = (this.currentServicesPage - 1) * this.rowsPerServicesPage;
            const end = start + this.rowsPerServicesPage;
            return this.services.slice(start, end);
        },
    },
    methods: {
        async fetchServices() {
            try {
                const token = localStorage.getItem('access_token');
                if (!token) {
                    alert('You are not logged in. Please log in to view services.');
                    return;
                }

                const response = await axios.get('http://127.0.0.1:5000/created-services', {
                    headers: {
                        'Content-Type': 'application/json',
                        'Authorization': `Bearer ${token}`,
                    },
                    withCredentials: true,
                });

                // Populate services array with data from API
                this.services = response.data.map((service, index) => ({
                    add_service_id: service.add_service_id,
                    add_service_name: service.add_service_name,
                    add_service_description: service.add_service_description,
                    add_service_price: service.add_service_price,
                    dummyIndex: index + 1,
                }));

            } catch (error) {
                console.error('Error fetching services:', error.response?.data || error.message);
            }
        },

        async addService() {
            try {
                const token = localStorage.getItem('access_token');
                if (!token) {
                    this.errorMessage = 'You are not logged in. Please log in to add a service.';
                    return;
                }

                console.log('Form values before validation:', {
                    name: this.add_service_name,
                    description: this.add_service_description,
                    price: this.add_service_price,
                });

                // Validate all required fields
                if (!this.add_service_name || !this.add_service_description || !this.add_service_price) {
                    this.errorMessage = 'Please fill in all required fields';
                    console.log('Validation failed:', {
                        nameEmpty: !this.add_service_name,
                        descriptionEmpty: !this.add_service_description,
                        priceEmpty: !this.add_service_price
                    });
                    return;
                }

                const payload = {
                    add_service_name: this.add_service_name.trim(),
                    add_service_description: this.add_service_description.trim(),
                    add_service_price: parseFloat(this.add_service_price)
                };

                console.log('Sending payload:', payload); // Debug log

                const response = await axios.post('http://127.0.0.1:5000/create-service', payload, {
                    headers: {
                        'Content-Type': 'application/json',
                        'Authorization': `Bearer ${token}`,
                    },
                    withCredentials: true,
                });

                if (response.status === 201) {
                    alert('Service added successfully!');
                    this.closeAddServiceForm();
                    // Optionally reset fields
                    this.add_service_name = '';
                    this.add_service_description = '';
                    this.add_service_price = '';
                }
            } catch (error) {
                console.error('Error adding service:', error.response?.data || error.message);
                this.errorMessage = error.response?.data?.error || 'An error occurred while adding the service.';
            }
        },

        async updateService() {
            try {
                const token = localStorage.getItem('access_token');
                if (!token) {
                    this.errorMessage = 'You are not logged in. Please log in to update the service.';
                    return;
                }

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
            this.add_service_price = null;
            this.errorMessage = '';
        },
        closeAddServiceForm() {
            this.addServiceForm = false;
            // Reset form fields
            this.add_service_name = '';
            this.add_service_description = '';
            this.add_service_price = null;
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
    },

    mounted() {
        this.fetchServices();
    },
}
</script>

<style scoped>
</style>