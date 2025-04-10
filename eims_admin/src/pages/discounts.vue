<template>
    <div class="bg-gray-200 w-full h-full overflow-y-auto">
        <div class="w-full h-[65px] bg-gray-100 mt-2 flex items-center justify-between px-5 shadow-lg">
        <h1 class="font-amaticBold font-extraLight text-3xl">
            Discounts
        </h1>
        <button class="bg-[#9B111E] text-white px-3 py-2 rounded shadow-lg 
        transition-transform duration-300 transform hover:scale-105 font-semibold"
        @click="showInactiveDiscounts">
            Inactive Discounts
        </button>
        </div>

        <div class="flex flex-row items-center m-5 space-x-5">
        <div class="flex justify-start w-52 h-20 bg-white rounded-lg shadow-lg px-2 items-center border-l-2 border-green-400 space-x-5">
            <h2 class="font-amaticRegular text-4xl font-bold mb-0"> {{ totalDiscounts }} <span class = "text-sm antialiased text-gray-600">discounts</span></h2>
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
                <input type="text" id="search-bar" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full pl-10 p-2.5  dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="Search Discount..." required v-model="searchQuery">
                <router-link to="/" class="flex absolute inset-y-0 right-0 items-center pr-3">
                  <svg aria-hidden="true" class="w-4 h-4 text-gray-500 dark:text-gray-400 hover:text-gray-900 dark:hover:text-white" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                  </svg>
                </router-link>
              </div>
        </form>
                <button class = "mr-2 w-28 h-10 bg-[#9B111E] font-semibold text-gray-100 font-quicksand rounded-md shadow-lg 
                transition-transform duration-300 transform hover:scale-105" @click="openAddModal">
                Add Discount
                </button>
            </div> 

        <!--- Discounts Table --->

        <div v-if="showTable === 'Discounts'" class="relative shadow-md sm:rounded-xl w-full max-w-[1170px] h-[200] ml-5 mt-2 font-amaticBold mb-10">
            <div class="overflow-x-auto">
                <table class="w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400 mb-4 max-h-30 table-fixed">
                    <thead class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
                        <tr>
                            <th scope="col" class="w-16 px-2 py-3">#</th>
                            <th scope="col" class="w-52 px-2 py-3">Name</th>
                            <th scope="col" class="w-52 px-2 py-3">Type</th>
                            <th scope="col" class="w-36 px-2 py-3">Value</th>
                            <th scope="col" class="w-36 px-2 py-3">Start Date</th>
                            <th scope="col" class="w-36 px-2 py-3">End Date</th>
                            <th scope="col" class="w-28 px-2 py-3">Action</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr
                            v-for="(discount, index) in paginatedDiscounts"
                            :key="discount.discount_id"
                            class="border-b dark:border-gray-700 odd:bg-white odd:dark:bg-gray-900 even:bg-gray-50 even:dark:bg-gray-800">
                            <th scope="row" class="w-16 px-2 py-3 font-medium text-gray-900 whitespace-nowrap dark:text-white">{{ discount.dummyIndex }}</th>
                            <td class="w-52 px-2 py-3 truncate">{{ discount.name }}</td>
                            <td class="w-52 px-2 py-3 truncate">{{ discount.type }}</td>
                            <td class="w-36 px-2 py-3 truncate">{{ formatDiscountValue(discount) }}</td>
                            <td class="w-36 px-2 py-3 truncate" :class="getDateClass(discount, 'start')">{{ formatDate(discount.start_date) }}</td>
                            <td class="w-36 px-2 py-3 truncate" :class="getDateClass(discount, 'end')">{{ formatDate(discount.end_date) }}</td>
                            <td class="w-28 px-2 py-3">
                                <div class="flex items-center space-x-2">
                                    <button
                                        class="p-2 hover:opacity-80 transform hover:scale-110 transition-transform duration-200"
                                        @click="editDiscountBtn(index)"
                                        title="Update Discount Info">
                                        <img src="/img/update3.png" alt="Update" class="w-5 h-5">
                                    </button>
                                    <button
                                        class="p-2 hover:opacity-80 transform hover:scale-110 transition-transform duration-200"
                                        @click="toggleDiscountStatus(discount)"
                                        title="Deactivate">
                                        <img src="/img/deactivate.png" alt="Set Inactive" class="w-5 h-5">
                                    </button>
                                </div>
                            </td>
                        </tr>
                    </tbody>
                </table>

                <!-- Pagination Controls -->
                <div class="flex justify-center space-x-2 mt-4 mb-6">
                    <button @click="prevDiscountsPage" :disabled="currentPage === 1"
                        class="px-3 py-1 bg-[#9B111E] text-white rounded-md hover:bg-[#B73A45] disabled:opacity-50 text-sm">Previous</button>
                    <button v-for="page in totalPages" :key="page" @click="changeDiscountsPage(page)"
                        :class="{'bg-[#9B111E]': currentPage === page, 'bg-gray-300 ': currentPage !== page}"
                        class="px-3 py-1 text-white rounded-md hover:bg-[#B73A45] text-xs">
                        {{ page }}
                    </button>
                    <button @click="nextDiscountsPage" :disabled="currentPage === totalPages"
                        class="px-3 py-1 bg-[#9B111E] text-white rounded-md hover:bg-[#B73A45]  disabled:opacity-50 text-xs">Next</button>
                </div>
            </div>
        </div>

        <!-- Inactive Discounts Modal -->
        <div v-if="showInactiveDiscountsModal" class="fixed inset-0 bg-black bg-opacity-50 flex justify-center items-center z-50">
          <div class="bg-white w-[900px] p-6 rounded-lg shadow-lg max-h-[80vh] overflow-y-auto">
            <div class="flex justify-between items-center mb-4">
              <h2 class="text-xl font-semibold">Inactive Discounts</h2>
              <button @click="closeInactiveDiscountsModal" class="text-red-500 hover:text-red-700">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
                </svg>
              </button>
            </div>
            <div class="overflow-x-auto">
              <table class="min-w-full divide-y divide-gray-200">
                <thead class="bg-gray-50">
                  <tr>
                    <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">#</th>
                    <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Name</th>
                    <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Type</th>
                    <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Value</th>
                    <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Start Date</th>
                    <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">End Date</th>
                    <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Action</th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="(discount, index) in inactiveDiscounts" :key="discount.discount_id" 
                      class="bg-white border-b hover:bg-gray-50">
                    <td class="px-6 py-4">{{ index + 1 }}</td>
                    <td class="px-6 py-4">{{ discount.name }}</td>
                    <td class="px-6 py-4">{{ discount.type }}</td>
                    <td class="px-6 py-4">{{ formatDiscountValue(discount) }}</td>
                    <td class="px-6 py-4" :class="getDateClass(discount, 'start')">{{ formatDate(discount.start_date) }}</td>
                    <td class="px-6 py-4" :class="getDateClass(discount, 'end')">{{ formatDate(discount.end_date) }}</td>
                    <td class="px-6 py-4">
                      <button
                        class="p-2 hover:opacity-80 transform hover:scale-110 transition-transform duration-200"
                        @click="toggleDiscountStatus(discount)"
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

        <!-- Status Confirmation Modal -->
        <div v-if="showStatusConfirmModal" class="fixed inset-0 bg-black bg-opacity-50 flex justify-center items-center z-50">
          <div class="bg-white p-6 rounded-lg shadow-lg w-[400px]">
            <h2 class="text-xl font-semibold mb-4">Confirm Status Change</h2>
            <p class="mb-4">Are you sure you want to set this discount to <span class="font-bold">{{ pendingStatus }}</span>?</p>
            <div class="flex justify-end space-x-2">
              <button @click="closeStatusConfirmModal" class="bg-gray-300 text-gray-800 px-4 py-2 rounded hover:bg-gray-400">
                Cancel
              </button>
              <button @click="confirmStatusChange" class="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600">
                Confirm
              </button>
            </div>
          </div>
        </div>

        <!-- Add/Edit Modal -->
        <div v-if="showModal" class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center" @click.self="closeModal">
          <div class="bg-white rounded-lg p-8 max-w-2xl w-full">
            <h2 class="text-xl font-bold mb-4">{{ isEditing ? 'Update Discount' : 'Add Discount' }}</h2>
            <form @submit.prevent="handleSubmit" class="space-y-4">
              <div>
                <label class="block text-sm font-medium text-gray-700 text-left">Name</label>
                <input
                  v-model="formData.name"
                  type="text"
                  required
                  class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500"
                />
              </div>

              <div>
                <label class="block text-sm font-medium text-gray-700 text-left">Description</label>
                <textarea
                  v-model="formData.description"
                  rows="3"
                  class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500"
                ></textarea>
              </div>

              <div class="grid grid-cols-2 gap-4">
                <div>
                  <label class="block text-sm font-medium text-gray-700 text-left">Type</label>
                  <select
                    v-model="formData.type"
                    required
                    class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500"
                  >
                    <option value="percentage">Percentage</option>
                    <option value="fixed">Fixed Amount</option>
                  </select>
                </div>

                <div>
                  <label class="block text-sm font-medium text-gray-700 text-left">Value</label>
                  <input
                    v-model="formData.value"
                    type="number"
                    required
                    min="0"
                    :max="formData.type === 'percentage' ? 100 : null"
                    class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500"
                  />
                </div>
              </div>

              <div class="grid grid-cols-2 gap-4">
                <div>
                  <label class="block text-sm font-medium text-gray-700 text-left">Start Date</label>
                  <input
                    v-model="formData.start_date"
                    type="date"
                    class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500"
                  />
                </div>

                <div>
                  <label class="block text-sm font-medium text-gray-700 text-left">End Date</label>
                  <input
                    v-model="formData.end_date"
                    type="date"
                    class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500"
                  />
                </div>
              </div>

              <div class="flex justify-end space-x-3 mt-6">
                <button
                  type="button"
                  @click="closeModal"
                  class="px-4 py-2 border rounded-md hover:bg-gray-100"
                >
                  Cancel
                </button>
                <button
                  type="submit"
                  class="px-4 py-2 bg-blue-500 text-white rounded-md hover:bg-blue-600"
                >
                  {{ isEditing ? 'Update' : 'Add' }}
                </button>
              </div>
            </form>
          </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';

// axios.defaults.baseURL = 'http://127.0.0.1:5000';
axios.defaults.withCredentials = true;

export default {
    name: 'Discounts',
    data() {
        return {
            showTable: 'Discounts',
            discounts: [],
            currentPage: 1,
            itemsPerPage: 5,

            showModal: false,
            isEditing: false,

            searchQuery: '',
            
            //Discount form inputs
            formData: {
                name: '',
                description: '',
                type: 'percentage',
                value: 0,
                start_date: '',
                end_date: '',
                status: 'active'
            },

            selectedDiscount: {
                discount_id: '',
                name: '',
                description: '',
                type: '',
                value: '',
                start_date: '',
                end_date: '',
                status: 'active'
            },

            showInactiveDiscountsModal: false,
            showStatusConfirmModal: false,
            pendingStatus: '',
            pendingDiscount: null,
            inactiveDiscounts: [],
        }
    },
    computed: {
        totalDiscounts() {
            return this.filteredDiscounts.length;
        },
        totalPages() {
            return Math.ceil(this.filteredDiscounts.length / this.itemsPerPage);
        },
        paginatedDiscounts() {
            const startIndex = (this.currentPage - 1) * this.itemsPerPage;
            const endIndex = startIndex + this.itemsPerPage;
            
            return this.discounts.map((discount, index) => ({
                ...discount,
                dummyIndex: index + 1
            })).slice(startIndex, endIndex);
        },
        filteredDiscounts() {
            if (!this.searchQuery) return this.discounts;
            const searchLower = this.searchQuery.toLowerCase().trim();
            return this.discounts.filter(discount => {
                const searchableFields = [
                    discount.name,
                    discount.type,
                    String(discount.value),
                    discount.description
                ];
                return searchableFields.some(field => 
                    String(field || '').toLowerCase().includes(searchLower)
                );
            });
        },
    },
    methods: {
        async fetchDiscounts() {
            try {
                const token = localStorage.getItem('access_token');
                const response = await axios.get('http://127.0.0.1:5000/api/discounts', {
                    headers: {
                        'Authorization': `Bearer ${token}`
                    }
                });

                // Check if response.data has a 'data' property containing the discounts array
                const discountsData = response.data.data || response.data;
                
                this.discounts = discountsData.map((discount, index) => ({
                    discount_id: discount.discount_id,
                    name: discount.name,
                    description: discount.description,
                    type: discount.type,
                    value: discount.value,
                    start_date: discount.start_date,
                    end_date: discount.end_date,
                    status: discount.status,
                    dummyIndex: index + 1,
                }));

            } catch (error) {
                console.error('Error fetching discounts:', error);
                this.errorMessage = 'Failed to fetch discounts';
            }
        },

        async handleSubmit() {
            try {
                if (!this.formData.name || !this.formData.type || !this.formData.value) {
                    this.errorMessage = 'Name, type, and value are required';
                    return;
                }

                const token = localStorage.getItem('access_token');
                const payload = {
                    name: this.formData.name,
                    description: this.formData.description,
                    type: this.formData.type,
                    value: this.formData.value,
                    start_date: this.formData.start_date || null,
                    end_date: this.formData.end_date || null,
                    status: this.formData.status || 'active'
                };

                if (this.isEditing) {
                    const response = await axios.put(
                        `http://127.0.0.1:5000/api/discounts/${this.selectedDiscount.discount_id}`, 
                        payload, 
                        {
                            headers: {
                                'Authorization': `Bearer ${token}`
                            }
                        }
                    );
                    
                    if (response.data.success) {
                        alert('Discount updated successfully!');
                        this.closeModal();
                        await this.fetchDiscounts();
                    } else {
                        alert(response.data.error || 'Failed to update discount');
                    }
                } else {
                    const response = await axios.post(
                        'http://127.0.0.1:5000/api/discounts', 
                        payload, 
                        {
                            headers: {
                                'Authorization': `Bearer ${token}`
                            }
                        }
                    );
                    
                    if (response.data.success) {
                        alert('Discount added successfully!');
                        this.closeModal();
                        await this.fetchDiscounts();
                    } else {
                        alert(response.data.error || 'Failed to add discount');
                    }
                }
            } catch (error) {
                console.error('Error saving discount:', error.response?.data || error.message);
                alert(error.response?.data?.error || 'Failed to save discount. Please try again.');
            }
        },

        prevDiscountsPage() {
            if (this.currentPage > 1) {
                this.currentPage--;
            }
        },
        nextDiscountsPage() {
            if (this.currentPage < this.totalPages) {
                this.currentPage++;
            }
        },
        changeDiscountsPage(page) {
            this.currentPage = page;
        },

        openAddModal() {
            this.isEditing = false;
            this.formData = {
                name: '',
                description: '',
                type: 'percentage',
                value: 0,
                start_date: '',
                end_date: '',
                status: 'active'
            };
            this.showModal = true;
        },
        closeModal() {
            this.showModal = false;
            this.formData = {
                name: '',
                description: '',
                type: 'percentage',
                value: 0,
                start_date: '',
                end_date: '',
                status: 'active'
            };
        },

        editDiscountBtn(index) {
            this.isEditing = true;
            const selectedDiscount = this.discounts[index];
            if (selectedDiscount) {
                this.selectedDiscount = { ...selectedDiscount };
                
                // Populate the form with the selected discount's data
                this.formData = {
                    name: selectedDiscount.name,
                    description: selectedDiscount.description || '',
                    type: selectedDiscount.type,
                    value: selectedDiscount.value,
                    start_date: selectedDiscount.start_date ? selectedDiscount.start_date.split('T')[0] : '',
                    end_date: selectedDiscount.end_date ? selectedDiscount.end_date.split('T')[0] : '',
                    status: selectedDiscount.status
                };
                
                // Show the modal
                this.showModal = true;
            } else {
                console.error('Invalid discount selected:', index);
            }
        },

        formatDiscountValue(discount) {
            if (discount.type === 'percentage') {
                return `${discount.value}%`;
            } else {
                return `₱${this.formatPrice(discount.value)}`;
            }
        },

        formatPrice(price) {
            if (price === null || price === undefined || typeof price === 'object' || isNaN(price)) {
                return 'N/A'; // Return a fallback if price is invalid
            }
            // Ensure price is treated as a number, round to 2 decimal places, and format with commas
            return parseFloat(price).toFixed(2).replace(/\d(?=(\d{3})+\.)/g, '$&,');
        },

        async showInactiveDiscounts() {
            try {
                const token = localStorage.getItem('access_token');
                const response = await axios.get('http://127.0.0.1:5000/api/discounts/inactive', {
                    headers: {
                        Authorization: `Bearer ${token}`,
                    },
                });

                // Check if response.data has a 'data' property containing the discounts array
                this.inactiveDiscounts = response.data.data || response.data;
                
                if (this.inactiveDiscounts.length === 0) {
                    alert('There are no inactive discounts.');
                    return;
                }
                
                this.showInactiveDiscountsModal = true;
            } catch (error) {
                console.error("Error fetching inactive discounts:", error);
                alert("Error fetching inactive discounts. Please try again.");
            }
        },

        closeInactiveDiscountsModal() {
            this.showInactiveDiscountsModal = false;
            this.inactiveDiscounts = [];
        },

        toggleDiscountStatus(discount) {
            this.pendingDiscount = discount;
            this.pendingStatus = discount.status === 'active' ? 'inactive' : 'active';
            this.showStatusConfirmModal = true;
        },

        closeStatusConfirmModal() {
            this.showStatusConfirmModal = false;
            this.pendingDiscount = null;
            this.pendingStatus = '';
        },

        async confirmStatusChange() {
            try {
                const token = localStorage.getItem('access_token');
                
                const response = await axios.put(
                    `http://127.0.0.1:5000/api/discounts/${this.pendingDiscount.discount_id}/status`,
                    { status: this.pendingStatus },
                    {
                        headers: {
                            Authorization: `Bearer ${token}`,
                        },
                    }
                );

                if (response.status === 200) {
                    // Check if the response has the expected structure
                    const responseData = response.data.data || response.data;
                    const newStatus = responseData.new_status || this.pendingStatus;
                    
                    if (newStatus === 'inactive') {
                        const index = this.discounts.findIndex(d => d.discount_id === this.pendingDiscount.discount_id);
                        if (index !== -1) {
                            this.discounts.splice(index, 1);
                        }
                        alert('Discount has been set to Inactive');
                    } else {
                        const index = this.inactiveDiscounts.findIndex(d => d.discount_id === this.pendingDiscount.discount_id);
                        if (index !== -1) {
                            this.inactiveDiscounts.splice(index, 1);
                        }
                        await this.fetchDiscounts();
                        alert('Discount has been set to Active');
                    }
                    this.closeStatusConfirmModal();
                }
            } catch (error) {
                console.error("Error toggling discount status:", error);
                if (error.response) {
                    alert(error.response.data.message || "Error updating discount status");
                } else {
                    alert("Error updating discount status. Please try again.");
                }
                this.closeStatusConfirmModal();
            }
        },

        getDateClass(discount, type) {
            const today = new Date().toISOString().split('T')[0];
            const startDate = discount.start_date ? discount.start_date.split('T')[0] : today;
            const endDate = discount.end_date ? discount.end_date.split('T')[0] : today;
            
            // Check if the discount is currently valid
            const isCurrentlyValid = startDate <= today && (endDate === null || endDate >= today);
            
            // Return the same color for both start and end dates
            return {
                'text-green-500': isCurrentlyValid,
                'text-red-500': !isCurrentlyValid
            };
        },

        formatDate(date) {
            if (!date) return 'N/A';
            const formattedDate = new Date(date).toLocaleDateString();
            return formattedDate.split('/').join('-');
        },
    },
    mounted() {
        this.fetchDiscounts();
    },
}
</script>

<style scoped>
</style>    