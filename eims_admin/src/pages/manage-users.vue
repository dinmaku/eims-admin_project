<template>
   <div class="bg-gray-200 w-full h-full">
    <div class="w-full h-[65px] bg-gray-100 mt-2 flex items-center justify-between px-5 shadow-lg">
    <h1 class="font-amaticBold font-extraLight text-3xl">
    Manage Users
  </h1>
  </div>

  <div class="flex flex-row items-center m-5 space-x-5">
    <div class="flex justify-start w-52 h-20 bg-white rounded-lg shadow-lg px-2 items-center border-l-2 border-green-400 space-x-5">
        <img class="w-auto h-12" src="/img/vendor2.png" alt="Vendor Image">
        <h2 class="font-amaticRegular text-4xl font-bold mb-0">{{ totalVendors }} <span class = "text-sm antialiased text-gray-600">suppliers</span></h2>
    </div>
    <div class="flex justify-start w-52 h-20 bg-white rounded-lg shadow-lg px-2 items-center border-l-2 border-blue-400 space-x-5">
        <img class="w-auto h-12" src="/img/staff.png" alt="Vendor Image">
        <h2 class="font-amaticRegular text-4xl font-bold mb-0">{{ totalStaff }} <span class = "text-sm antialiased text-gray-600">crews</span></h2>
    </div>
</div>

<div class="flex flex-row justify-between items-center m-5 my-5">
  <div class = "flex">
  <button :class="[ 
    'flex justify-center items-center w-28 h-10 m-2 font-raleway font-semibold rounded-lg shadow-lg transition-transform duration-300 transform hover:scale-105', 
    { 'bg-white text-teal-800': showTable === 'vendors', 'bg-gray-800 text-white': showTable !== 'vendors' } 
  ]" @click="showTable = 'vendors'">
    Suppliers
  </button>
  
  <button :class="[ 
    'flex justify-center items-center w-28 h-10 m-2 font-raleway font-semibold rounded-lg shadow-lg transition-transform duration-300 transform hover:scale-105', 
    { 'bg-white text-teal-800': showTable === 'staffs', 'bg-gray-800 text-white': showTable !== 'staffs' } 
  ]" @click="showTable = 'staffs'">
    Crews
  </button>
</div>
<button class = "mr-2 w-28 h-10 bg-blue-600 font-semibold text-gray-100 font-quicksand rounded-full shadow-lg 
transition-transform duration-300 transform hover:scale-105" @click="addUserBtn">
 + Add User
</button>
</div>

<!--- Vendor Table--->
<div v-if="showTable === 'vendors'" class="relative shadow-md sm:rounded-xl w-[1170px] h-[200] ml-5 mt-2 font-amaticBold mb-10">
    <div class="overflow-x-auto">
      <table class="w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400 mb-4 max-h-30">
        <thead class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
          <tr>
            <th scope="col" class="px-2 py-3">#</th>
            <th scope="col" class="px-2 py-3">Name</th>
            <th scope="col" class="px-2 py-3">Email</th>
            <th scope="col" class="px-2 py-3">Contact</th>
            <th scope="col" class="px-2 py-3">Service</th>
            <th scope="col" class="px-2 py-3">Minimum price</th>
            <th scope="col" class="px-2 py-3">Maximum price</th>
            <th scope="col" class="px-2 py-3">Action</th>
          </tr>
        </thead>
        <tbody>
          <tr
              v-for="(vendor, index) in paginatedVendors"
              :key="vendor.no"
              class="border-b dark:border-gray-700 odd:bg-white odd:dark:bg-gray-900 even:bg-gray-50 even:dark:bg-gray-800">
            <th scope="row" class="px-2 py-3 font-medium text-gray-900 whitespace-nowrap dark:text-white">{{ vendor.no }}</th>
            <td class="px-1 py-3 hidden sm:table-cell">{{ vendor.fullName }}</td>
            <td class="px-1 py-3 hidden sm:table-cell">{{ vendor.email }}</td>
            <td class="px-1 py-3 hidden sm:table-cell">{{ vendor.contact }}</td>
            <td class="px-1 py-3 hidden sm:table-cell">{{ vendor.service }}</td>
            <td class="px-1 py-3 hidden sm:table-cell">{{ vendor.minPrice }}</td>
            <td class="px-1 py-3 hidden sm:table-cell">{{ vendor.maxPrice }}</td>
            <td class="px-1 py-3 hidden sm:table-cell">
              <button
                  class="h-8 w-12 bg-blue-900 font-amaticBold font-medium text-sm rounded-md text-white hover:bg-blue-600" @click="editVendorBtn(index)">
                  Edit
                </button>
            </td>
          </tr>
        </tbody>
      </table>

      <!-- Pagination Controls -->
      <div class="flex justify-center space-x-2 mt-4 mb-6">
        <button @click="prevVendorsPage" :disabled="currentVendorsPage === 1" class="px-3 py-1 bg-blue-900 text-white rounded-md hover:bg-blue-600 disabled:opacity-50 text-md">Previous</button>
        <button v-for="page in totalVendorsPages" :key="page" @click="changeVendorsPage(page)" :class="{'bg-blue-900': currentVendorsPage === page, 'bg-gray-300': currentVendorsPage !== page}" class="px-3 py-1 text-white rounded-md hover:bg-blue-600 text-xs">
          {{ page }}
        </button>
        <button @click="nextVendorsPage" :disabled="currentVendorsPage === totalVendorsPages" class="px-3 py-1 bg-blue-900 text-white rounded-md hover:bg-blue-600 disabled:opacity-50 text-xs">Next</button>
      </div>
    </div>
  </div>

  <!--- Staff Table--->
  <div v-if="showTable === 'staffs'" class="relative shadow-md sm:rounded-xl w-[1170px] h-[200] ml-5 mt-2 font-amaticBold mb-10">
    <div class="overflow-x-auto">
      <table class="w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400 mb-4 max-h-30">
        <thead class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
          <tr>
            <th scope="col" class="px-2 py-3">#</th>
            <th scope="col" class="px-2 py-3">FullName</th>
            <th scope="col" class="px-2 py-3">Email</th>
            <th scope="col" class="px-2 py-3">Contact</th>
            <th scope="col" class="px-2 py-3">Position</th>
            <th scope="col" class="px-2 py-3">Action</th>
          </tr>
        </thead>
        <tbody>
          <tr
              v-for="(staff, index) in paginatedStaffs"
              :key="staff.no"
              class="border-b dark:border-gray-700 odd:bg-white odd:dark:bg-gray-900 even:bg-gray-50 even:dark:bg-gray-800">
            <th scope="row" class="px-2 py-3 font-medium text-gray-900 whitespace-nowrap dark:text-white">{{ staff.no }}</th>
            <td class="px-1 py-3 hidden sm:table-cell">{{ staff.fullName }}</td>
            <td class="px-1 py-3 hidden sm:table-cell">{{ staff.email }}</td>
            <td class="px-1 py-3 hidden sm:table-cell">{{ staff.contact }}</td>
            <td class="px-1 py-3 hidden sm:table-cell">{{ staff.position }}</td>
  
            <td class="px-1 py-3 hidden sm:table-cell">
              <button class="h-8 w-12 bg-blue-900 font-amaticBold font-medium text-sm rounded-md text-white hover:bg-blue-600"
              @click="editStaffBtn(index)">
                  Edit
                </button>
            </td>
          </tr>
        </tbody>
      </table>

      <!-- Pagination Controls -->
      <div class="flex justify-center space-x-2 mt-4 mb-6">
        <button @click="prevStaffsPage" :disabled="currentStaffsPage === 1" class="px-3 py-1 bg-blue-900 text-white rounded-md hover:bg-blue-600 disabled:opacity-50 text-md">Previous</button>
        <button v-for="page in totalStaffsPages" :key="page" @click="changeStaffsPage(page)" :class="{'bg-blue-900': currentStaffsPage === page, 'bg-gray-300': currentStaffsPage !== page}" class="px-3 py-1 text-white rounded-md hover:bg-blue-600 text-xs">
          {{ page }}
        </button>
        <button @click="nextStaffsPage" :disabled="currentStaffsPage === totalStaffsPages" class="px-3 py-1 bg-blue-900 text-white rounded-md hover:bg-blue-600 disabled:opacity-50 text-xs">Next</button>
      </div>
    </div>
  </div>

 <!-- Add User Form -->
 <form v-if="addUserForm" @submit.prevent="handleRegister" class="flex justify-center items-center fixed inset-0 bg-gray-800 bg-opacity-50 overflow-y-auto">
  <div class="bg-white w-[500px] p-5 rounded-lg shadow-lg overflow-y-auto">
    <div class="flex justify-between items-center m-3">
      <h1 class="font-semibold text-xl font-raleway text-gray-800">Add User</h1>
      <button class="mt-2 bg-red-500 text-white px-3 py-1 rounded transform-transition duration-300 transform hover:scale-105" @click="closeAddUserForm">
        Close
      </button>
    </div>
    <div class="border border-gray-500 mt-5 items-center"></div>
    <div class="m-5">
      <span>{{ errorMessage }}</span>
      <!-- First Name and Last Name -->
      <div class="flex flex-row">
        <div class="flex items-center space-x-2">
          <input type="text" class="mt-2 ml-2 p-2 w-full h-10 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:border-blue-700" v-model="firstName" placeholder="First Name" required>
        </div>
        <div class="flex items-center space-x-2">
          <input type="text" class="mt-2 ml-2 p-2 w-full h-10 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:border-blue-700" v-model="lastName" placeholder="Last Name" required>
        </div>
      </div>

      <!-- Email -->
      <div class="mt-5">
        <input type="email" class="mt-2 ml-2 p-2 w-full h-10 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:border-blue-700" v-model="email" placeholder="Email" required>
      </div>

      <!-- Contact Number -->
      <div class="mt-5">
        <input type="text" class="mt-2 ml-2 p-2 w-full h-10 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:border-blue-700" v-model="contactNumber" placeholder="Contact Number" required>
      </div>

      <!-- Address -->
      <div class="mt-5">
        <input type="text" class="mt-2 ml-2 p-2 w-full h-10 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:border-blue-700" v-model="country" placeholder="Country" required>
      </div>

      <div class="mt-5 flex flex-row">
        <div class="flex items-center space-x-2">
          <input type="text" class="mt-2 ml-2 p-2 w-full h-10 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:border-blue-700" v-model="city" placeholder="City" required>
        </div>
        <div class="flex items-center space-x-2">
          <input type="text" class="mt-2 ml-2 p-2 w-full h-10 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:border-blue-700" v-model="street" placeholder="Street" required>
        </div>
      </div>

      <!-- Password -->
      <div class="mt-5">
        <input type="password" class="mt-2 ml-2 p-2 w-full h-10 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:border-blue-700" v-model="registerPassword" placeholder="Password" required>
      </div>

      <!-- User Type Selection -->
      <div class="mt-5">
        <select class="flex mt-4 ml-2 p-2 w-52 h-10 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:border-blue-700" v-model="selectedUserType" @change="selectAddForm">
          <option value="" class="text-gray-700" disabled selected>Select a Type of User</option>
          <option value="vendor">Vendors</option>
          <option value="assistant">Assistant</option>
          <option value="staff">Staff</option>
        </select>
      </div>

      <!-- Vendor Details (only if vendor is selected) -->
      <div v-if="addVendorDetails" class="mt-5">
        <select class="mt-2 ml-2 p-2 w-full h-10 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:border-blue-700" v-model="service">
          <option value="" class="text-gray-700" disabled selected>Select Service Type</option>
          <option value="Catering">Catering</option>
          <option value="Glam">Hair and Makeup</option>
          <option value="Host">Host</option>
          <option value="Entertainment">Entertainer / Singer</option>
          <option value="Multimedia">Photographer and Videographer</option>
          <option value="Sound and Lighting">Sound and Lighting</option>
          <option value="Transportation">Transportation</option>
          <option value="Invitations">Invitations and Stationery</option>
          <option value="Keepsakes">Favor and Gifts</option>
        </select>

        <div class="flex items-center mt-4">
          <input type="text" class="mt-2 ml-2 p-2 w-[200px] h-10 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:border-blue-700" v-model="minPrice" placeholder="Minimum Price" required>
          <input type="text" class="mt-2 ml-2 p-2 w-[200px] h-10 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:border-blue-700" v-model="maxPrice" placeholder="Maximum Price" required>
        </div>
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


<!--Edit Vendor Form-->
<form v-if="editVendorForm" class = "flex justify-center items-center fixed inset-0 bg-gray-800 bg-opacity-50 flex justify-center items-center">
  <div class = "bg-white w-[500px] p-5 rounded-lg shadow-lg  overflow-y-auto">
        <div class = "flex justify-between items-center m-3">
              <h1 class = "font-semibold text-xl font-raleway text-gray-800">Edit Vendor</h1>
               <button class="mt-2 bg-red-500 text-white px-3 py-1 rounded transform-transition duration-300 transform hover:scale-105" @click="closeEditVendorBtn">
                  Close
                </button>
        </div>
        <div class = "border border-gray-500 mt-5 items-center"></div>
               <div class = "m-5">

             
                <div class = "flex items-center space-x-2">
                  <input type="text"  v-model="selectedVendor.fullName" class = "mt-2 ml-2 p-2 w-full h-10 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:border-blue-700" placeholder="Name" required>
              
              </div>
              <div class = "mt-5">
                <div class = "flex items-center">
                  <input type="text"  v-model="selectedVendor.email" class = "mt-2 ml-2 p-2 w-full h-10 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:border-blue-700" placeholder="Email" required>
                </div>
              </div>
              <div class = "mt-5">
                <div class = "flex items-center">
                  <input type="text"  v-model="selectedVendor.contact" class = "mt-2 ml-2 p-2 w-full h-10 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:border-blue-700" placeholder="Contact Number" required>
                </div>
              </div>

              <div class = "mt-5">
                <div class = "flex items-center">
                  <select v-model="selectedVendor.service" class = "mt-2 ml-2 p-2 w-full h-10 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:border-blue-700">
                    <option value="" class = "text-gray-700" disabled selected>Select Service Type</option>
                    <option value="Catering">Catering</option>
                    <option value="Hair and Makeup">Hair and Makeup</option>
                    <option value="Host">Host</option>
                    <option value="Entertainment">Entertainer / Singer</option>
                    <option value="Multimedia">Photographer and Videographer</option>
                    <option value="Sound and Light">Sound and Lighting</option>
                    <option value="Transportation">Transportation</option>
                    <option value="Invitations and Stationery">Invitations and Stationery</option>
                    <option value="Favors and Gifts">Favors and Gifts</option>
                </select>
                </div>
                <div class = "flex items-center mt-4">
                  <input type="text" v-model="selectedVendor.minPrice" class = "mt-2 ml-2 p-2 w-[200px] h-10 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:border-blue-700" id ="minPrice" placeholder="Minimum Price" required>
                  <input type="text" v-model="selectedVendor.maxPrice" class = "mt-2 ml-2 p-2 w-[200px] h-10 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:border-blue-700" id ="maxPrice" placeholder="Maximum Price" required>
                </div>
 
              </div>

              <div v-if = "addStaffDetails" class = "mt-5">
                <div class = "flex items-center">
                  <select class = "mt-2 ml-2 p-2 w-full h-10 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:border-blue-700">
                    <option value="" class = "text-gray-700" disabled selected>Select Position</option>
                    <option value="Assistant">Assistant</option>
                    <option value="Staff">Staff</option>
                  </select>
                </div>
 
              </div>

              <div class = "flex  justify-center items-center mt-10 space-x-3">
                   <button class = "w-20 h-10 bg-yellow-500 text-gray-100 font-semibold rounded-lg shadow-md  transform-transition duration-300 transform hover:scale-105">
                     Delete
                   </button>
                   <button class = "w-20 h-10 bg-blue-500 text-gray-100 font-semibold rounded-lg shadow-md  transform-transition duration-300 transform hover:scale-105">
                     Confirm
                   </button>
              </div>


        </div>
  </div>
</form> 

<!--Edit Staff Form-->
<form v-if="editStaffForm" class = "flex justify-center items-center fixed inset-0 bg-gray-800 bg-opacity-50 flex justify-center items-center">
  <div class = "bg-white w-[500px] p-5 rounded-lg shadow-lg  overflow-y-auto">
        <div class = "flex justify-between items-center m-3">
              <h1 class = "font-semibold text-xl font-raleway text-gray-800">Edit Staff</h1>
               <button class="mt-2 bg-red-500 text-white px-3 py-1 rounded transform-transition duration-300 transform hover:scale-105" @click="closeEditStaffBtn">
                  Close
                </button>
        </div>
        <div class = "border border-gray-500 mt-5 items-center"></div>
               <div class = "m-5">

             
                <div class = "flex items-center space-x-2">
                  <input type="text"  v-model="selectedStaff.fullName" class = "mt-2 ml-2 p-2 w-full h-10 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:border-blue-700" placeholder="Name" required>
                
              </div>
              <div class = "mt-5">
                <div class = "flex items-center">
                  <input type="text"  v-model="selectedStaff.email" class = "mt-2 ml-2 p-2 w-full h-10 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:border-blue-700" placeholder="Email" required>
                </div>
              </div>
              <div class = "mt-5">
                <div class = "flex items-center">
                  <input type="text"  v-model="selectedStaff.contact" class = "mt-2 ml-2 p-2 w-full h-10 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:border-blue-700" placeholder="Contact Number" required>
                </div>
              </div>


              <div class = "mt-5">
                <div class = "flex items-center">
                  <select v-model="selectedStaff.position" class = "mt-2 ml-2 p-2 w-full h-10 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:border-blue-700">
                    <option value="" class = "text-gray-700" disabled selected>Select Position</option>
                    <option value="Assistant">Assistant</option>
                    <option value="Staff">Staff</option>       
                  </select>
                </div>   
             </div>

              <div class = "flex justify-center items-center mt-10 space-x-3">
                   <button @click.prevent="deleteUserItem(selectedStaff.no)" class = "w-20 h-10 bg-yellow-500 text-gray-100 font-semibold rounded-lg shadow-md  transform-transition duration-300 transform hover:scale-105">
                     Delete
                   </button>
                   <button @click.prevent="confirmEditStaff" class = "w-20 h-10 bg-blue-500 text-gray-100 font-semibold rounded-lg shadow-md  transform-transition duration-300 transform hover:scale-105">
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
  name: 'ManageUsers',
  data() {
    return {
      showTable: 'vendors',
      currentVendorsPage: 1,
      rowsPerVendorsPage: 6,

      currentStaffsPage: 1,
      rowsPerStaffsPage: 6,

      addUserForm: false,
      addVendorDetails: false,
      addStaffDetails: false,
      selectedOption: '',

      editVendorForm: false,
      selectedVendor: null, 
      editVendorForm: false,

      editStaffForm: false,
      selectedStaff: null, 
      editStaffForm: false,

      //add users inputs
      selectedUserType: '',
      email: '',
      firstName: '',
      lastName: '',
      contactNumber: '',
      country: '',
      city: '',
      street: '',
      registerPassword: '',
      service: '',
      minPrice: '',
      maxPrice: '',
      errorMessage: '',


      staffs: [],
      vendors: [],
  
      


      
    };
  },
  computed: {
    totalVendorsPages() {
      return Math.ceil(this.vendors.length / this.rowsPerVendorsPage);
    },
    paginatedVendors() {
      const start = (this.currentVendorsPage - 1) * this.rowsPerVendorsPage;
      const end = start + this.rowsPerVendorsPage;
      return this.vendors.slice(start, end);
    },
    totalVendors() {
       return this.vendors.length;
    },

    totalStaff() {
       return this.staffs.length;
    },

    totalStaffsPages() {
      return Math.ceil(this.staffs.length / this.rowsPerStaffsPage);
    },
    paginatedStaffs() {
      const start = (this.currentStaffsPage - 1) * this.rowsPerStaffsPage;
      const end = start + this.rowsPerStaffsPage;
      return this.staffs.slice(start, end);
    },

    
  },
  methods: {
    async handleRegister() {
          try {
              // Validate required fields
              const fields = [
                  this.firstName, this.lastName, this.email, this.contactNumber,
                  this.registerPassword, this.country, this.city, this.street
              ];

              if (fields.some(field => !field)) {
                  this.errorMessage = 'All fields are required!';
                  return;
              }

              // Additional validation for vendors
              if (this.selectedUserType === 'vendor') {
                  if (!this.service || !this.minPrice || !this.maxPrice) {
                      this.errorMessage = 'Vendor details are incomplete!';
                      return;
                  }
              }

              // Prepare the data payload
              const requestData = {
                  firstName: this.firstName,
                  lastName: this.lastName,
                  email: this.email,
                  contactNumber: this.contactNumber,
                  password: this.registerPassword,
                  country: this.country,
                  city: this.city,
                  street: this.street,
                  user_type: this.selectedUserType,
              };

              // Include vendor-specific details if applicable
              if (this.selectedUserType === 'vendor') {
                  requestData.service = this.service;
                  requestData.minPrice = this.minPrice;
                  requestData.maxPrice = this.maxPrice;
              }

              // Send the request to the backend
              const response = await axios.post('http://127.0.0.1:5000/add-user', requestData);

              if (response.status === 201) {
                  alert('User added successfully!');
                  this.resetRegisterForm(); // Reset the form after success
              }
          } catch (error) {
              // Handle error feedback
              this.errorMessage = error.response?.data?.message || 'An error occurred. Please try again.';
          }
      },


      resetRegisterForm() {
          this.firstName = '';
          this.lastName = '';
          this.email = '';
          this.contactNumber = '';
          this.country = '';
          this.city = '';
          this.street = '';
          this.registerPassword = '';
          this.selectedUserType = '';
          this.service = '';
          this.minPrice = '';
          this.maxPrice = '';
          this.errorMessage = '';
      },
      async fetchStaffs() {
              try {
                const token = localStorage.getItem('access_token');
                if (!token) {
                  alert('You are not logged in. Please log in to view staff users.');
                  return;
                }

                const response = await axios.get('http://127.0.0.1:5000/created-users', {
                  headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${token}`,
                  },
                  withCredentials: true,
                });

                this.staffs = response.data.map((user) => ({
                  no: user.userid,
                  fullName: `${user.firstname} ${user.lastname}`,
                  email: user.email,
                  contact: user.contactnumber,
                  position: user.user_type === 'assistant' ? 'Assistant' : 'Staff',
                }));

              
              } catch (error) {
                console.error('Error fetching staff users:', error.response?.data || error.message);
              }
            },
        async fetchVendors() {
            try {
                const token = localStorage.getItem('access_token'); // Get the JWT token
                if (!token) {
                    alert('You are not logged in. Please log in to view vendor data.');
                    return;
                }

                const response = await axios.get('http://127.0.0.1:5000/vendors', {
                    headers: {
                        'Content-Type': 'application/json',
                        'Authorization': `Bearer ${token}`, // Send the JWT token
                    },
                    withCredentials: true, // Send cookies if needed
                });

                // Populate vendors array with data from API
                this.vendors = response.data.map((vendor, index) => ({
                    no: index + 1,
                    fullName: `${vendor.firstname} ${vendor.lastname}`,
                    email: vendor.email,
                    contact: vendor.contactnumber,
                    service: vendor.service,
                    minPrice: vendor.min_price,
                    maxPrice: vendor.max_price,
                }));
            } catch (error) {
                console.error('Error fetching vendors:', error.response?.data || error.message);
            }
        },


        async confirmEditStaff() {
            try {
              const token = localStorage.getItem('access_token');

              if (!this.selectedStaff || !this.selectedStaff.no) {
                alert("Staff ID is missing or invalid.");
                return;
              }

              const [firstName, ...lastNameParts] = this.selectedStaff.fullName.split(' ');
              const lastName = lastNameParts.join(' ');

              const response = await axios.put(
                `http://127.0.0.1:5000/created-users/${this.selectedStaff.no}`,
                {
                  firstname: firstName,
                  lastname: lastName,
                  email: this.selectedStaff.email,
                  contactnumber: this.selectedStaff.contact,
                  user_type: this.selectedStaff.position.toLowerCase() // Convert 'Assistant' or 'Staff' to lowercase
                },
                {
                  headers: {
                    Authorization: `Bearer ${token}`,
                  },
                }
              );

              if (response.status === 200) {
                alert('Staff updated successfully!');
                
                const index = this.staffs.findIndex(staff => staff.no === this.selectedStaff.no);
                if (index !== -1) {
                  this.staffs[index] = { ...this.selectedStaff };
                }
                
                this.closeEditStaffBtn();
              } else {
                alert('Failed to update staff.');
              }
            } catch (error) {
              console.error('Error updating staff:', error);
              if (error.response) {
                alert(`Error updating staff: ${error.response.data.message}`);
              } else {
                alert('Error updating staff. Please try again.');
              }
            }
          },

          async deleteUserItem(userid) {
              try {
                if (!confirm('Are you sure you want to delete this user? This action cannot be undone.')) {
                  return;
                }

                const token = localStorage.getItem('access_token');
                if (!token) {
                  alert('You are not logged in. Please log in to delete users.');
                  return;
                }

                const response = await axios.delete(`http://127.0.0.1:5000/created-users/${userid}`, {
                  headers: {
                    'Authorization': `Bearer ${token}`,
                  },
                });

                if (response.status === 200) {
                  alert('User deleted successfully!');
                  // Remove the deleted user from the staffs array
                  this.staffs = this.staffs.filter(staff => staff.no !== userid);
                  this.closeEditStaffBtn();
                } else {
                  alert('Failed to delete user.');
                }
              } catch (error) {
                console.error('Error deleting user:', error);
                if (error.response) {
                  alert(`Error deleting user: ${error.response.data.message}`);
                } else {
                  alert('Error deleting user. Please try again.');
                }
              }
            },
      





    changeVendorsPage(page) {
      this.currentVendorsPage = page;
    },
    prevVendorsPage() {
      if (this.currentVendorsPage > 1) {
        this.currentVendorsPage--;
      }
    },
    nextVendorsPage() {
      if (this.currentVendorsPage < this.totalVendorsPages) {
        this.currentVendorsPage++;
      }
    },

    prevStaffsPage() {
      if (this.currentStaffsPage > 1) {
        this.currentStaffsPage--;
      }
    },
    nextStaffsPage() {
      if (this.currentStaffsPage < this.totalStaffsPages) {
        this.currentStaffsPage++;
      }
    },
    changeStaffsPage(page) {
      this.currentStaffsPage = page;
    },

    addUserBtn() {
      this.addUserForm = true;
    },
    closeAddUserForm() {
      this.addUserForm = false;
      this.selectedOption = '';
    },

    selectAddForm() {
          if (this.selectedUserType === 'vendor') {
              this.addVendorDetails = true;
              this.addStaffDetails = false;
          } else if (this.selectedUserType === 'assistant' || this.selectedUserType === 'staff') {
              this.addStaffDetails = true;
              this.addVendorDetails = false;
          } else {
              this.addVendorDetails = false;
              this.addStaffDetails = false;
          }
      },
  


    editVendorBtn(){
      this.editVendorForm = true;
    },

    closeEditVendorBtn() {
      this.editVendorForm = false;
    },

    editVendorBtn(index) {
        this.selectedVendor = this.paginatedVendors[index]; 
        this.editVendorForm = true; // Show the edit form
    },
    closeEditUserBtn() {
        this.editUserForm = false; 
        this.selectedVendor = null; 
    },

    editStaffBtn(){
      this.editStaffForm = true;
    },

    closeStaffVendorBtn() {
      this.editStaffForm = false;
    },

    editStaffBtn(index) {
          console.log("Selected Staff from paginatedStaffs: ", JSON.parse(JSON.stringify(this.paginatedStaffs[index])));
          this.selectedStaff = this.paginatedStaffs[index]; 
          this.editStaffForm = true;
      },
    closeEditStaffBtn() {
        this.editStaffForm = false;
        this.selectedStaff = null; 
    },
    
  },
  mounted() {
    if (this.showTable === 'staffs') {
        this.fetchStaffs(); // Fetch staff data on component mount
    } else if (this.showTable === 'vendors') {
        this.fetchVendors(); // Fetch vendor data on component mount
    }
},
watch: {
    showTable(newTable) {
        if (newTable === 'staffs') {
            this.fetchStaffs();
        } else if (newTable === 'vendors') {
            this.fetchVendors();
        }
    },
},
};
</script>

<style scoped>
/* Add any scoped styles here */
</style>
