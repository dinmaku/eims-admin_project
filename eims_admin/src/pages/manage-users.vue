<template>
  <div class="bg-gray-200 w-full h-full">
    <div class="w-full h-[65px] bg-gray-100 mt-2 flex items-center justify-between px-5 shadow-lg">
    <h1 class="font-amaticBold font-extraLight text-3xl">
    Accounts
  </h1>
    <button class="bg-[#9B111E] text-white px-3 py-2 rounded shadow-lg 
    transition-transform duration-300 transform hover:scale-105 font-semibold"
    @click="showInactiveSuppliers">
      Inactive Suppliers
    </button>
  </div>

  <div class="flex flex-row items-center m-5 space-x-5">
    <div class="flex justify-start w-52 h-20 bg-white rounded-lg shadow-lg px-2 items-center border-l-2 border-green-400 space-x-5">
        <h2 class="font-amaticRegular text-4xl font-bold mb-0 ml-5">{{ totalSuppliers }} <span class = "text-sm antialiased text-gray-600 ml-2">suppliers</span></h2>
    </div>
    <div class="flex justify-start w-52 h-20 bg-white rounded-lg shadow-lg px-2 items-center border-l-2 border-blue-400 space-x-5">
        <h2 class="font-amaticRegular text-4xl font-bold mb-0 ml-5">{{ totalStaff }} <span class = "text-sm antialiased text-gray-600 ml-2">staff</span></h2>
    </div>
    <div class="flex justify-start w-52 h-20 bg-white rounded-lg shadow-lg px-2 items-center border-l-2 border-blue-400 space-x-5">
        <h2 class="font-amaticRegular text-4xl font-bold mb-0 ml-5">{{ totalAdmin }} <span class = "text-sm antialiased text-gray-600 ml-2">admin</span></h2>
    </div>
    <form class="flex items-center w-[300px] mt-9">
              <label for="voice-search" class="sr-only">Search</label>
              <div class="relative w-full">
                <div class="flex absolute inset-y-0 left-0 items-center pl-3 pointer-events-none">
                  <svg aria-hidden="true" class="w-5 h-auto text-gray-500 dark:text-gray-400" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                    <path fill-rule="evenodd" d="M8 4a4 4 0 100 8 4 4 0 000-8zM2 8a6 6 0 1110.89 3.476l4.817 4.817a1 1 0 01-1.414 1.414l-4.816-4.816A6 6 0 012 8z" clip-rule="evenodd"></path>
                  </svg>
                </div>
                <input type="text" id="search-bar" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full pl-10 p-2.5  dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="Search Account..." required v-model="searchTerm">
                <router-link to="/" class="flex absolute inset-y-0 right-0 items-center pr-3">
                  <svg aria-hidden="true" class="w-4 h-4 text-gray-500 dark:text-gray-400 hover:text-gray-900 dark:hover:text-white" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                  </svg>
                </router-link>
              </div>
        </form>
</div>

<div class="flex flex-row justify-between items-center m-5 space-x-5">
  <div class = "flex">
  <button :class="[ 
    'flex justify-center items-center w-28 h-10 m-2 font-raleway font-semibold rounded-lg shadow-lg transition-transform duration-300 transform hover:scale-105', 
    { 'bg-gray-800 text-white ': showTable === 'Suppliers', 'bg-white text-teal-800': showTable !== 'Suppliers' } 
  ]" @click="showTable = 'Suppliers'">
    Suppliers
  </button>
  
  <button :class="[ 
    'flex justify-center items-center w-28 h-10 m-2 font-raleway font-semibold rounded-lg shadow-lg transition-transform duration-300 transform hover:scale-105', 
    { 'bg-gray-800 text-white': showTable === 'Staffs', 'bg-white text-teal-800': showTable !== 'Staffs' } 
  ]" @click="showTable = 'Staffs'">
    Staff
  </button>
  <button :class="[ 
    'flex justify-center items-center w-28 h-10 m-2 font-raleway font-semibold rounded-lg shadow-lg transition-transform duration-300 transform hover:scale-105', 
    { 'bg-gray-800 text-white': showTable === 'Admin', 'bg-white text-teal-800': showTable !== 'Admin' } 
  ]" @click="showTable = 'Admin'">
    Admin
  </button>
</div>
<button class = "mr-2 w-32 h-10 bg-[#9B111E] font-semibold text-gray-100 font-quicksand rounded-md shadow-lg 
transition-transform duration-300 transform hover:scale-105" @click="addUserBtn">
  Add Account
</button>
</div>


<!--- Supplier Table --->
<div v-if="showTable === 'Suppliers'" class="relative shadow-md sm:rounded-xl w-full max-w-[1170px] h-[200] ml-5 mt-2 font-amaticBold mb-10">
    <div class="overflow-x-auto">
        <table class="w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400 mb-4 max-h-30">
            <thead class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
                <tr>
                    <th scope="col" class="px-2 py-3">#</th>
                    <th scope="col" class="px-2 py-3">Name</th>
                    <th scope="col" class="px-2 py-3">Email</th>
                    <th scope="col" class="px-2 py-3">Contact</th>
                    <th scope="col" class="px-2 py-3">Service</th>
                    <th scope="col" class="px-2 py-3">Rate</th>
                    <th scope="col" class="px-2 py-3">Action</th>
                </tr>
            </thead>
            <tbody>
                <tr
                    v-for="(supplier, index) in paginatedSuppliers"
                    :key="supplier.no"
                    class="border-b dark:border-gray-700 odd:bg-white odd:dark:bg-gray-900 even:bg-gray-50 even:dark:bg-gray-800">
                    <th scope="row" class="px-2 py-3 font-medium text-gray-900 whitespace-nowrap dark:text-white">{{ supplier.dummyIndex }}</th>
                    <td class="px-1 py-3 hidden sm:table-cell">{{ supplier.fullName }}</td>
                    <td class="px-1 py-3 hidden sm:table-cell">{{ supplier.email }}</td>
                    <td class="px-1 py-3 hidden sm:table-cell">{{ supplier.contact }}</td>
                    <td class="px-1 py-3 hidden sm:table-cell">{{ supplier.service }}</td>
                    <td class="px-1 py-3 hidden sm:table-cell">{{ formatPrice(supplier.price) }} php</td>
                    <td class="px-1 py-3 hidden sm:table-cell">
                        <div class="flex items-center space-x-1">
                            <button
                                class="p-2 hover:opacity-80 transform hover:scale-110 transition-transform duration-200"
                                @click="editSupplier(supplier)"
                                title="Update Supplier Info">
                                <img src="/img/update2.png" alt="Edit" class="w-5 h-5">
                            </button>
                            <button
                                class="p-2 hover:opacity-80 transform hover:scale-110 transition-transform duration-200"
                                @click="showRateModal = true; selectedSupplier = supplier"
                                title="Set Rate">
                                <img src="/img/rate2.png" alt="Set Rate" class="w-5 h-5">
                            </button>
                            <button
                                class="p-2 hover:opacity-80 transform hover:scale-110 transition-transform duration-200"
                                @click="toggleSupplierStatus(supplier)"
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
            <button @click="prevSuppliersPage" :disabled="currentSuppliersPage === 1" 
                class="px-3 py-1 bg-[#9B111E] text-white rounded-md hover:bg-[#B73A45] disabled:opacity-50 text-sm">Previous</button>
            <button v-for="page in totalSuppliersPages" :key="page" @click="changeSuppliersPage(page)" 
                :class="{'bg-[#9B111E]': currentSuppliersPage === page, 'bg-gray-300': currentSuppliersPage !== page}" 
                class="px-3 py-1 text-white rounded-md hover:bg-[#B73A45] text-xs">
                {{ page }}
            </button>
            <button @click="nextSuppliersPage" :disabled="currentSuppliersPage === totalSuppliersPages" 
                class="px-3 py-1 bg-[#9B111E] text-white rounded-md hover:bg-[#B73A45] disabled:opacity-50 text-xs">Next</button>
        </div>
    </div>
</div>


  <!--- Staff Table--->
  <div v-if="showTable === 'Staffs'" class="relative shadow-md sm:rounded-xl w-full max-w-[1170px] h-[200] ml-5 mt-2 font-amaticBold mb-10">
    <div class="overflow-x-auto">
      <table class="w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400 mb-4 max-h-30">
      <thead class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
        <tr>
          <th scope="col" class="px-2 py-3">#</th>
          <th scope="col" class="px-2 py-3">Name</th>
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
          <th scope="row" class="px-2 py-3 font-medium text-gray-900 whitespace-nowrap dark:text-white">{{ staff.dummyIndex }}</th>
          <td class="px-1 py-3 hidden sm:table-cell">{{ staff.fullName }}</td>
          <td class="px-1 py-3 hidden sm:table-cell">{{ staff.email }}</td>
          <td class="px-1 py-3 hidden sm:table-cell">{{ staff.contact }}</td>
          <td class="px-1 py-3 hidden sm:table-cell">{{ staff.position }}</td>

          <td class="px-1 py-3 hidden sm:table-cell">
            <button class="p-2 hover:opacity-80 transform hover:scale-110 transition-transform duration-200" 
            @click="editStaffBtn(index)" 
            title="Update Staff Info">
            <img src="/img/update2.png" alt="Update" class="w-5 h-5">
           
              </button>
          </td>
        </tr>
      </tbody>
    </table>

      <!-- Pagination Controls -->
      <div class="flex justify-center space-x-2 mt-4 mb-6">
        <button @click="prevStaffsPage" :disabled="currentStaffsPage === 1" 
            class="px-3 py-1 bg-[#9B111E] text-white rounded-md hover:bg-[#B73A45] disabled:opacity-50 text-sm">Previous</button>
        <button v-for="page in totalStaffsPages" :key="page" @click="changeStaffsPage(page)" 
            :class="{'bg-[#9B111E]': currentStaffsPage === page, 'bg-gray-300': currentStaffsPage !== page}" 
            class="px-3 py-1 text-white rounded-md hover:bg-[#B73A45] text-xs">
          {{ page }}
        </button>
        <button @click="nextStaffsPage" :disabled="currentStaffsPage === totalStaffsPages" 
            class="px-3 py-1 bg-[#9B111E] text-white rounded-md hover:bg-[#B73A45] disabled:opacity-50 text-xs">Next</button>
      </div>
    </div>
  </div>

  <!-- Admin Table -->
<div v-if="showTable === 'Admin'" class="relative shadow-md sm:rounded-xl w-full max-w-[1170px] h-[200] ml-5 mt-2 font-amaticBold mb-10">
    <div class="overflow-x-auto">
        <table class="w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400 mb-4 max-h-30">
            <thead class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
                <tr>
                    <th scope="col" class="px-2 py-3">#</th>
                    <th scope="col" class="px-2 py-3">Name</th>
                    <th scope="col" class="px-2 py-3">Email</th>
                    <th scope="col" class="px-2 py-3">Contact</th>
                    <th scope="col" class="px-2 py-3">User Type</th>
                    <th scope="col" class="px-2 py-3">Action</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="(admin, index) in paginatedAdmins" :key="admin.userid" class="border-b dark:border-gray-700 odd:bg-white odd:dark:bg-gray-900 even:bg-gray-50 even:dark:bg-gray-800">
                    <th scope="row" class="px-2 py-3 font-medium text-gray-900 whitespace-nowrap dark:text-white">{{ admin.dummyIndex }}</th>
                    <td class="px-1 py-3 hidden sm:table-cell">{{ admin.fullName }}</td>
                    <td class="px-1 py-3 hidden sm:table-cell">{{ admin.email }}</td>
                    <td class="px-1 py-3 hidden sm:table-cell">{{ admin.contactnumber }}</td>
                    <td class="px-1 py-3 hidden sm:table-cell">{{ admin.user_type }}</td>
                    <td class="px-1 py-3 hidden sm:table-cell">
                        <button class="p-2 hover:opacity-80 transform hover:scale-110 transition-transform duration-200" @click="editAdminBtn(index)" title = "Update Admin Info">
                          <img src="/img/update2.png" alt="Update" class="w-5 h-5">
                          </button>
                    </td>
                </tr>
            </tbody>
        </table>
        <div class="flex justify-center space-x-2 mt-4 mb-6">
            <button @click="prevAdminPage" :disabled="currentAdminPage === 1" class="px-3 py-1 bg-[#9B111E] text-white rounded-md hover:bg-[#B73A45] disabled:opacity-50 text-sm">Previous</button>
            <button v-for="page in totalAdminPages" :key="page" @click="changeAdminPage(page)" :class="{'bg-[#9B111E]': currentAdminPage === page, 'bg-gray-300': currentAdminPage !== page}" class="px-3 py-1 text-white rounded-md hover:bg-[#B73A45] text-xs">{{ page }}</button>
            <button @click="nextAdminPage" :disabled="currentAdminPage === totalAdminPages" class="px-3 py-1 bg-[#9B111E] text-white rounded-md hover:bg-[#B73A45] disabled:opacity-50 text-xs">Next</button>
        </div>
    </div>
</div>

 <!-- Add User Form -->
 <form v-if="addUserForm" @submit.prevent="handleRegister" class="fixed inset-0 bg-gray-800 bg-opacity-50 overflow-y-auto flex justify-center items-center" @click.self="closeAddUserForm">
  <div class="bg-white w-[500px] p-5 rounded-lg shadow-lg overflow-y-auto">
    <div class="flex justify-between items-center m-3">
      <h1 class="font-semibold text-xl font-raleway text-gray-800">Add Account</h1>
    </div>
    <div class="border border-gray-500 mt-5 items-center"></div>
    <div class="m-5">
      <span class = "text-red-500"> {{ errorMessage }}</span>
      <!-- First Name and Last Name -->
      <div class="flex flex-row">
        <div class="flex flex-col space-y-1 w-full">
          <label class="text-xs text-gray-600 ml-2 text-start">First Name</label>
          <input type="text" class="p-2 h-10 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:border-blue-700" v-model="firstName" required>
        </div>
        <div class="flex flex-col space-y-1 w-full ml-2">
          <label class="text-xs text-gray-600 ml-2 text-start">Last Name</label>
          <input type="text" class="p-2 h-10 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:border-blue-700" v-model="lastName" required>
        </div>
      </div>

      <!-- Username -->
      <div class="flex flex-col  mt-5">
        <label class="text-xs text-gray-600 ml-2 text-start">Username</label>
        <input type="text" class="mt-1 p-2 w-full h-10 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:border-blue-700" v-model="username" @click="deriveUsername" required>
      </div>

      <!-- Email -->
      <div class="flex flex-col  mt-5">
        <label class="text-xs text-gray-600 ml-2 text-start">Email</label>
        <input type="text" class="mt-1 p-2 w-full h-10 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:border-blue-700" v-model="email" @click="deriveEmail" required>
      </div>

      <!-- Contact Number -->
      <div class="flex flex-col  mt-5">
        <label class="text-xs text-gray-600 ml-2 text-start">Contact Number</label>
        <input type="text" class="mt-1 p-2 w-full h-10 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:border-blue-700" v-model="contactNumber" required>
      </div>

      <!-- Address -->
      <div class="flex flex-col  mt-5">
        <label class="text-xs text-gray-600 ml-2 text-start">Address</label>
        <input type="text" class="mt-1 p-2 w-full h-10 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:border-blue-700" v-model="address" required>
      </div>

      <!-- User Type Selection -->
      <div class="flex flex-col  mt-5">
        <label class="text-xs text-gray-600 ml-2 text-start">Account Type</label>
        <select class="flex mt-1 p-2 w-full h-10 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:border-blue-700" v-model="selectedUserType" @change="selectAddForm">
          <option value="" class="text-gray-700" disabled selected>Select Account Type</option>
          <option value="Suppliers">Supplier</option>
          <option value="Staff">Staff</option>
          <option value="Admin">Admin</option>
        </select>
      </div>

      <!-- Suppliers Details (only if supplier is selected) -->
      <div v-if="addSupplierDetails" class="mt-5">
        <select class="mt-2 p-2 w-full h-10 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:border-blue-700" v-model="service">
          <option value="" class="text-gray-700" disabled selected>Select Service Type</option>
          <option value="Catering">Catering</option>
          <option value="Hair Stylist">Hair Stylist</option>
          <option value="Makeup Artist">Makeup Artist</option>
          <option value="Host">Host</option>
          <option value="Entertainment">Entertainer / Singer</option>
          <option value="Photographer">Photographer</option>
          <option value="Videographer">Videographer</option>
          <option value="Sound and Lighting">Sound and Lighting</option>
          <option value="Transportation">Transportation</option>
          <option value="Invitations">Invitations and Stationery</option>
          <option value="Keepsakes">Favor and Gifts</option>
        </select>
      </div>

      <div v-if="addSupplierDetails" class="flex justify-start items-center mt-5">
        <button class= "w-40 h-10 bg-[#9B111E] text-white px-3 py-1 rounded transform-transition duration-300 transform hover:scale-105 "
         @click.prevent ="addSocialMediaModal(selectedSupplier)">
          Add Social Media
        </button>
      </div>

      <!-- Confirm Button -->
      <div class="flex justify-end items-center mt-5 space-x-2">
          <button class="bg-gray-300 text-white w-20 h-10 rounded-lg transform-transition duration-300 transform hover:scale-105 hover:bg-gray-400" @click="closeAddUserForm">
          Cancel
        </button>
        <button type="submit" class="w-20 h-10 bg-blue-500 text-gray-100 font-semibold rounded-lg shadow-md transform-transition duration-300 transform hover:scale-105">
          Save
        </button>
      </div>
    </div>
  </div>
</form>

<!-- Status Confirmation Modal -->
<div v-if="showStatusConfirmModal" @click.self="closeStatusConfirmModal" class="fixed inset-0 bg-gray-800 bg-opacity-50 overflow-y-auto flex justify-center items-center z-50">
  <div class="bg-white p-5 rounded-lg shadow-lg w-[400px]">
    <div class="flex flex-col items-center">
      <h2 class="text-xl font-semibold mb-4">Confirm Status Change</h2>
      <p class="mb-6 text-center">Are you sure you want to set this supplier to {{ pendingStatus }}?</p>
      <div class="flex space-x-4">
        <button 
          @click="closeStatusConfirmModal" 
          class="bg-gray-500 text-white px-4 py-2 rounded hover:bg-opacity-90">
          Cancel
        </button>
        <button 
          @click="confirmStatusChange" 
          class = "w-20 h-10 bg-blue-500 text-gray-100 font-semibold rounded-lg shadow-md  transform-transition duration-300 transform hover:scale-105">
          Yes
        </button>
      </div>
    </div>
  </div>
</div>

<!-- Inactive Suppliers Modal -->
<div v-if="showInactiveSuppliersModal" @click.self="closeInactiveSuppliersModal" class="fixed inset-0 bg-gray-800 bg-opacity-50 overflow-y-auto flex justify-center items-center z-40">
  <div class="bg-white p-5 rounded-lg shadow-lg w-[1000px]">
    <div class="flex justify-between items-center mb-4">
      <h2 class="text-xl font-semibold">Inactive Suppliers</h2>
      <button @click="closeInactiveSuppliersModal" class="text-gray-500 hover:text-gray-700">
        <span class="text-2xl">&times;</span>
      </button>
    </div>

    <div class="overflow-x-auto">
      <table class="w-full text-sm text-left text-gray-500">
        <thead class="text-xs text-gray-700 uppercase bg-gray-50">
          <tr>
            <th class="px-6 py-3">No.</th>
            <th class="px-6 py-3">Name</th>
            <th class="px-6 py-3">Email</th>
            <th class="px-6 py-3">Contact</th>
            <th class="px-6 py-3">Service</th>
            <th class="px-6 py-3">Price</th>
            <th class="px-6 py-3">Actions</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(supplier, index) in inactiveSuppliers" :key="supplier.supplier_id" 
              class="bg-white border-b hover:bg-gray-50">
            <td class="px-6 py-4">{{ index + 1 }}</td>
            <td class="px-6 py-4">{{ supplier.firstname }} {{ supplier.lastname }}</td>
            <td class="px-6 py-4">{{ supplier.email }}</td>
            <td class="px-6 py-4">{{ supplier.contactnumber }}</td>
            <td class="px-6 py-4">{{ supplier.service }}</td>
            <td class="px-6 py-4">₱{{ formatPrice(supplier.price) }}</td>
            <td class="px-6 py-4 flex space-x-2">
              <button
                class="p-2 hover:opacity-80 transform hover:scale-110 transition-transform duration-200"
                @click.stop="toggleInactiveSupplierStatus(supplier)"
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

 <!-- Rate Modal -->
<div v-if="showRateModal" @click.self="closeRateModal" class="fixed inset-0 bg-gray-800 bg-opacity-50 overflow-y-auto flex justify-center items-center z-20">
  <div class="bg-white p-5 rounded-lg shadow-lg w-[400px]">
    <div class="flex justify-between items-center">
      <h2 class="text-xl font-semibold">Set Supplier Rate</h2>
      <button @click="closeRateModal" class="text-gray-500 hover:text-gray-700">
        <span class="text-2xl">&times;</span>
      </button>
    </div>
    <div class="mt-4">
      <label class="text-xs text-gray-600">Rate</label>
      <input type="number" v-model="supplierRate" class="mt-1 p-2 w-full h-10 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:border-blue-700" placeholder="Enter rate">
    </div>
    <div class="flex justify-end mt-4 space-x-2">
      
      <button @click="closeRateModal" class="bg-gray-500 text-white px-4 py-2 rounded hover:bg-opacity-90">Cancel</button>
      <button @click="saveSupplierRate" class = "w-20 h-10 bg-blue-500 text-gray-100 font-semibold rounded-lg shadow-md  transform-transition duration-300 transform hover:scale-105">Save</button>
    </div>
  </div>
</div>

 <!-- Social Media Modal -->
<div v-if="showSocialMediaModal" @click.self="closeSocialMediaModal" class="fixed inset-0 bg-gray-800 bg-opacity-50 overflow-y-auto h-full w-full flex justify-center items-center z-40">
    <div class="bg-white p-8 rounded-lg shadow-xl w-[500px] relative">
        <div class="flex justify-between items-center mb-6">
            <h2 class="text-2xl font-semibold text-gray-800">Add Social Media</h2>
            <button @click="closeSocialMediaModal" class="text-gray-600 hover:text-gray-800">
                <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
                </svg>
            </button>
        </div>

        <form @submit.prevent="submitSocialMedia" class="space-y-4">
            <div>
                <label class="block text-sm font-medium text-gray-700 mb-1 text-start">Platform *</label>
                <select 
                    v-model="socialMediaForm.platform" 
                    class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-1 focus:ring-[#9B111E]"
                    required
                >
                    <option value="">Select Platform</option>
                    <option value="Facebook">Facebook</option>
                    <option value="Instagram">Instagram</option>
                    <option value="Twitter">Twitter</option>
                    <option value="LinkedIn">LinkedIn</option>
                    <option value="TikTok">TikTok</option>
                    <option value="YouTube">YouTube</option>
                </select>
            </div>

            <div>
                <label class="block text-sm font-medium text-gray-700 mb-1 text-start">Handle/Username *</label>
                <input 
                    type="text" 
                    v-model="socialMediaForm.handle"
                    class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-1 focus:ring-[#9B111E]"
                    placeholder="@username"
                    required
                >
            </div>

            <div>
                <label class="block text-sm font-medium text-gray-700 mb-1 text-start">URL (Optional)</label>
                <input 
                    type="url" 
                    v-model="socialMediaForm.url"
                    class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-1 focus:ring-[#9B111E]"
                    placeholder="https://example.com/profile"
                >
            </div>

            <div class="flex justify-end space-x-3 mt-6">
                <button 
                    type="button"
                    @click="closeSocialMediaModal"
                    class="px-4 py-2 border border-gray-300 rounded-md text-gray-700 hover:bg-gray-50"
                >
                    Cancel
                </button>
                <button 
                    type="submit"
                    class = "w-44 h-10 bg-blue-500 text-gray-100 font-semibold rounded-lg shadow-md  transform-transition duration-300 transform hover:scale-105"
                >
                    Add Social Media
                </button>
            </div>
        </form>
    </div>
</div>

 <!--Edit Supplier Form-->
<form v-if="editSupplierForm" class = "fixed inset-0 bg-gray-800 bg-opacity-50 flex justify-center items-center z-30" @click.self="closeEditSupplierBtn">
  <div class = "bg-white w-[800px] p-5 rounded-lg shadow-lg  overflow-y-auto">
        <div class = "flex justify-between items-center m-3">
              <h1 class = "font-semibold text-xl font-raleway text-gray-800">Update Supplier Info</h1>
        </div>
        <div class = "border border-gray-500 mt-5 items-center"></div>
        <div class="m-5 flex gap-8">
          <!-- Input Fields Section - Left Side -->
          <div class="w-3/5 space-y-5">
            <div>
              <label class="text-xs text-gray-600 block">Full Name</label>
              <input type="text" v-model="selectedSupplier.fullName" class="mt-2 p-2 w-full h-10 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:border-blue-700" required>
            </div>

            <div>
              <label class="text-xs text-gray-600 block">Username</label>
              <input type="text" v-model="selectedSupplier.username" class="mt-2 p-2 w-full h-10 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:border-blue-700" required>
            </div>

            <div>
              <label class="text-xs text-gray-600 block">Email</label>
              <input type="text" v-model="selectedSupplier.email" class="mt-2 p-2 w-full h-10 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:border-blue-700" required>
            </div>

            <div>
              <label class="text-xs text-gray-600 block">Contact</label>
              <input type="text" v-model="selectedSupplier.contact" class="mt-2 p-2 w-full h-10 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:border-blue-700" placeholder="Contact Number" required>
            </div>

            <div>
              <label class="text-xs text-gray-600 block">Service Type</label>
              <select v-model="selectedSupplier.service" class="mt-2 p-2 w-full h-10 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:border-blue-700">
                <option value="" class="text-gray-700" disabled selected>Select Service Type</option>
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

            <div v-if="addStaffDetails">
              <label class="text-xs text-gray-600 block">Position</label>
              <select class="mt-2 p-2 w-full h-10 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:border-blue-700">
                <option value="" class="text-gray-700" disabled selected>Select Position</option>
                <option value="Staff">Staff</option>
              </select>
            </div>
          </div>

          <!-- Social Media Section - Right Side -->
          <div class="w-1/2">
            <div class="border border-gray-200 rounded-lg p-4">
              <div class="flex justify-between items-center mb-3">
                <p class="text-gray-700 font-medium">Social Media Accounts</p>
                <button @click="addSocialMedia" type="button" class="text-blue-600 hover:text-blue-800 text-sm">
                  + Add Account
                </button>
              </div>
              <div class="max-h-[400px] overflow-y-auto pr-2">
                <div v-if="selectedSupplier.socialMedia && selectedSupplier.socialMedia.length > 0" class="space-y-2">
                  <div v-for="social in selectedSupplier.socialMedia" :key="social.social_media_id" 
                       class="flex items-center p-2 bg-gray-50 rounded-lg border border-gray-100">
                    <div class="flex-1">
                      <div class="flex items-center gap-2">
                        <span class="font-medium text-gray-700">{{ social.platform }}</span>
                        <span class="text-gray-500">{{ social.handle }}</span>
                      </div>
                      <a v-if="social.url" :href="social.url" target="_blank" 
                         class="text-sm text-blue-600 hover:text-blue-800 break-all">
                        {{ social.url }}
                      </a>
                    </div>
                  </div>
                </div>
                <div v-else class="text-gray-500 text-sm text-center py-4">
                  No social media accounts added yet
                </div>
              </div>
            </div>
          </div>
        </div>

        <div class="flex justify-end items-center mt-4 space-x-3 px-5">
          <button class="w-20 h-10 bg-gray-300 text-white px-3 py-1 rounded transform-transition duration-300 transform hover:scale-105 hover:bg-gray-400" @click="closeEditSupplierBtn">
            Cancel
          </button>
          <button @click.prevent="confirmEditSupplier" class="w-20 h-10 bg-blue-500 text-gray-100 font-semibold rounded-lg shadow-md transform-transition duration-300 transform hover:scale-105">
            Save
          </button>
        </div>
  </div>
</form> 

<!--Edit Staff Form-->
<form v-if="editStaffForm" class = "flex justify-center items-center fixed inset-0 bg-gray-800 bg-opacity-50 flex justify-center items-center z-20" @click.self="closeEditStaffBtn">
  <div class = "bg-white w-[500px] p-5 rounded-lg shadow-lg  overflow-y-auto">
        <div class = "flex justify-between items-center m-3">
              <h1 class = "font-semibold text-xl font-raleway text-gray-800">Update Staff Info</h1>
        </div>
        <div class = "border border-gray-500 mt-5 items-center"></div>
               <div class = "m-5">
                <div class = "flex flex-col">
                  <label class="text-xs text-gray-600 block text-start">Full Name</label>
                  <input type="text"  v-model="selectedStaff.fullName" class = "mt-2 p-2 w-full h-10 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:border-blue-700" placeholder="Name" required>
                
              </div>
              <div class = "mt-5">
                <div class = "flex flex-col">
                  <label class="text-xs text-gray-600 block text-start">Email</label>
                  <input type="text"  v-model="selectedStaff.email" class = "mt-2 p-2 w-full h-10 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:border-blue-700" placeholder="Email" required>
                </div>
              </div>
              <div class = "mt-5">
                <div class = "flex flex-col">
                  <label class="text-xs text-gray-600 block text-start">Contact</label>
                  <input type="text"  v-model="selectedStaff.contact" class = "mt-2 p-2 w-full h-10 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:border-blue-700" placeholder="Contact Number" required>
                </div>
              </div>


              <div class = "mt-5">
                <div class = "flex flex-col">
                  <label class="text-xs text-gray-600 block text-start">Position</label>
                  <select v-model="selectedStaff.position" class = "mt-2p-2 w-full h-10 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:border-blue-700">
                    <option value="" class = "text-gray-700" disabled selected>Select Position</option>
                    <option value="Assistant">Assistant</option>
                    <option value="Staff">Staff</option>
                    <option value="Admin">Admin</option>     
                  </select>
                </div>   
             </div>

              <div class = "flex justify-end items-center mt-10 space-x-3">
                <button class="w-20 h-10 bg-gray-300 text-white px-3 py-1 rounded transform-transition duration-300 transform hover:scale-105 hover:bg-gray-400" @click="closeEditStaffBtn">
                  Close
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
      baseURL: 'http://127.0.0.1:5000',
      showTable: 'Suppliers',
      currentSuppliersPage: 1,
      rowsPerSuppliersPage: 5,

      currentStaffsPage: 1,
      rowsPerStaffsPage: 5,
      
      currentAdminPage: 1,
      adminPerPage: 5,

      addUserForm: false,
      addSupplierDetails: false,
      addStaffDetails: false,
      selectedOption: '',

      editSupplierForm: false,
      selectedSupplier: null,

      editStaffForm: false,
      selectedStaff: null, 

      //add users inputs
      selectedUserType: '',
      email: '',
      username: '',
      firstName: '',
      lastName: '',
      contactNumber: '',
      address: '',
      registerPassword: '',
      service: '',
      price: '',
      status: '',
      errorMessage: '',

      staffs: [],
      suppliers: [],
      admins: [],
      searchTerm: '',

      showRateModal: false,
      supplierRate: '',

      showStatusConfirmModal: false,
      pendingStatus: '',
      pendingSupplier: null,

      showInactiveSuppliersModal: false,
      inactiveSuppliers: [],

      showSocialMediaModal: false,
      socialMediaForm: {
        platform: '',
        handle: '',
        url: ''
      },
    };
  },
  computed: {
    totalSuppliersPages() {
        return Math.ceil(this.filteredSuppliers.length / this.rowsPerSuppliersPage);
    },
    paginatedSuppliers() {
        const start = (this.currentSuppliersPage - 1) * this.rowsPerSuppliersPage;
        const end = start + this.rowsPerSuppliersPage;
        return this.filteredSuppliers.map((supplier, index) => ({
        ...supplier,
        dummyIndex: start + index + 1
      })).slice(start, end);
    },
    totalSuppliers() {
        return this.suppliers.length;
    },

    totalStaff() {
      return this.staffs.length;
    },
    totalStaffsPages() {
      return Math.ceil(this.filteredStaffs.length / this.rowsPerStaffsPage);
    },
    paginatedStaffs() {
      const start = (this.currentStaffsPage - 1) * this.rowsPerStaffsPage;
      const end = start + this.rowsPerStaffsPage;
      return this.filteredStaffs.map((staff, index) => ({
        ...staff,
        dummyIndex: start + index + 1
      })).slice(start, end);
    },

    totalAdmin() {
      return this.admins.length;
    },

    totalAdminPages() {
        return Math.ceil(this.filteredAdmins.length / this.adminPerPage);
      },

      paginatedAdmins() {
        const start = (this.currentAdminPage - 1) * this.adminPerPage;
        const end = start + this.adminPerPage;
        return this.filteredAdmins.map((admin, index) => ({
          ...admin,
          dummyIndex: start + index + 1,
          fullName: `${admin.firstname} ${admin.lastname}`
        })).slice(start, end);
      },
    
    filteredSuppliers() {
      if (!this.searchTerm) return this.suppliers;
      const searchLower = this.searchTerm.toLowerCase();
      return this.suppliers.filter(supplier => 
        supplier.fullName.toLowerCase().includes(searchLower) ||
        supplier.email.toLowerCase().includes(searchLower) ||
        supplier.contact.toLowerCase().includes(searchLower) ||
        supplier.service.toLowerCase().includes(searchLower)
      );
    },

    filteredStaffs() {
      if (!this.searchTerm) return this.staffs;
      const searchLower = this.searchTerm.toLowerCase();
      return this.staffs.filter(staff => 
        staff.fullName.toLowerCase().includes(searchLower) ||
        staff.email.toLowerCase().includes(searchLower) ||
        staff.contact.toLowerCase().includes(searchLower) ||
        staff.position.toLowerCase().includes(searchLower)
      );
    },

    filteredAdmins() {
      if (!this.searchTerm) return this.admins;
      const searchLower = this.searchTerm.toLowerCase();
      return this.admins.filter(admin => 
        admin.firstname.toLowerCase().includes(searchLower) ||
        admin.lastname.toLowerCase().includes(searchLower) ||
        admin.email.toLowerCase().includes(searchLower) ||
        admin.contactnumber.toLowerCase().includes(searchLower)
      );
    },
  },
  methods: {
    async handleRegister() {
            try {
                // Validate required fields
                const fields = [
                    this.username, this.email, this.firstName, this.lastName,
                    this.contactNumber, this.address,
                ];

                if (fields.some(field => !field)) {
                    this.errorMessage = 'All fields are required!';
                    return;
                }

                // Automatically set registerPassword to match username if username is provided
                if (this.username) {
                    this.registerPassword = this.username;
                }

                // Additional validation for vendors
                if (this.selectedUserType === 'Suppliers') {
                    if (!this.service) {
                        this.errorMessage = 'Vendor details are incomplete!';
                        return;
                    }
                }

                // Prepare the data payload
                const requestData = {
                    email: this.email,
                    username: this.username,
                    firstName: this.firstName,
                    lastName: this.lastName,
                    contactNumber: this.contactNumber,
                    address: this.address,
                    password: this.registerPassword,
                    user_type: this.selectedUserType,
                };

                // Include vendor-specific details if applicable
                if (this.selectedUserType === 'Suppliers') {
                    requestData.service = this.service;
                    requestData.price = 0;  // Set initial price as 0
                    requestData.status = 'Active';  // Set status as active for suppliers
                }

                // Send the request to the backend
                const response = await axios.post(`${this.baseURL}/add-user`, requestData);

                if (response.status === 201) {
                    alert('User added successfully!');
                    this.resetRegisterForm(); // Reset the form after success
                    this.closeAddUserForm();
                }
            } catch (error) {
                // Handle error feedback
                this.errorMessage = error.response?.data?.message || 'An error occurred. Please try again.';
            }
        },

        resetRegisterForm() {
            this.email = '';
            this.username = '';
            this.firstName = '';
            this.lastName = '';
            this.contactNumber = '';
            this.address = '';
            this.registerPassword = '';
            this.selectedUserType = '';
            this.service = '';
            this.errorMessage = '';
        },


        async fetchStaffs() {
            try {
              const token = localStorage.getItem('access_token');
              if (!token) {
                console.error('No access token found');
                this.$router.push('/login'); // Redirect to login if no token
                return;
              }

              const response = await axios.get(`${this.baseURL}/created-users`, {
                headers: {
                  'Content-Type': 'application/json',
                  'Authorization': `Bearer ${token}`, // Corrected syntax error
                },
                withCredentials: true,
              });

              // Log the response to inspect its structure and content
              console.log('Fetched users response:', response.data);

              // Validate response data
              if (!response.data || !Array.isArray(response.data)) {
                console.error('Invalid response format', response.data);
                return;
              }

              // Process staff data with more robust mapping
              this.staffs = response.data.map((user, index) => {
                // Add null checks and default values
                return {
                  no: user.userid || 'N/A',
                  fullName: user.firstname && user.lastname 
                    ? `${user.firstname} ${user.lastname}` 
                    : 'Unknown Name',
                  email: user.email || 'No email',
                  contact: user.contactnumber || 'No contact',
                  position: user.user_type === 'assistant' ? 'Assistant' : 'Staff',
                  dummyIndex: index + 1,
                };
              });

              // Convert Proxy to plain array for logging purposes
              const plainStaffsArray = JSON.parse(JSON.stringify(this.staffs));
              console.log('Processed Staff Data:', plainStaffsArray);

            } catch (error) {
              console.error('Error fetching staffs:', error.response?.data || error.message);

              // Handle specific error scenarios
              if (error.response?.status === 401) {
                // Token might be expired
                localStorage.removeItem('access_token');
                this.$router.push('/login');
              }
            }
          },

        async fetchSuppliers() {
          try {
              const token = localStorage.getItem('access_token');
              if (!token) {
                  alert('You are not logged in. Please log in to view supplier data.');
                  return;
              }

              const response = await axios.get(`${this.baseURL}/suppliers`, {
                  headers: {
                      'Content-Type': 'application/json',
                      'Authorization': `Bearer ${token}`,
                  },
                  withCredentials: true,
              });

              console.log(response.data); // Log the response to verify

              // Populate suppliers array with data from API
              this.suppliers = response.data.map((supplier, index) => ({
                  supplier_id: supplier.supplier_id, // Add this line to properly set supplier_id
                  no: supplier.supplier_id,
                  fullName: `${supplier.firstname} ${supplier.lastname}`,
                  email: supplier.email,
                  username: supplier.username,
                  password: supplier.password,
                  contact: supplier.contactnumber,
                  service: supplier.service,
                  price: supplier.price,
                  userid: supplier.userid,
                  dummyIndex: index + 1,
              }));
          } catch (error) {
              console.error('Error fetching suppliers:', error.response?.data || error.message);
          }
      },

      async fetchAdmins() {
        try {
            const token = localStorage.getItem('access_token');
            if (!token) {
                console.error('No token found');
                return;
            }
            const response = await axios.get(`${this.baseURL}/get_admin`, {
                headers: {
                    'Authorization': `Bearer ${token}`,
                    'Content-Type': 'application/json'
                }
            });
            if (response.data) {
                this.admins = response.data;
            }
        } catch (error) {
            console.error('Error fetching admins:', error);
            if (error.response) {
                console.error('Error response:', error.response.data);
            }
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
                `${this.baseURL}/created-users/${this.selectedStaff.no}`,
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


          async confirmEditSupplier() {
              try {
                const token = localStorage.getItem('access_token');

                if (!this.selectedSupplier) {
                  alert("No supplier selected for editing.");
                  return;
                }

                if (!this.selectedSupplier.no) {
                  alert("Supplier ID is missing or invalid.");
                  return;
                }

                // Use the userid from the selectedSupplier
                const userid = this.selectedSupplier.userid;

                if (!userid) {
                  alert("User ID is missing for this supplier. Unable to edit.");
                  return;
                }

                const requiredFields = [
                  'fullName', 'email', 'contact', 'service', 'username', 'password'
                ];
                
                const missingFields = requiredFields.filter(field => !this.selectedSupplier[field]);
                
                if (missingFields.length > 0) {
                  console.error('Missing fields:', missingFields);
                  alert(`Missing fields: ${missingFields.join(', ')}`);
                  return;
                }

                const [firstname, ...lastnameParts] = this.selectedSupplier.fullName.split(' ');
                if (!firstname || lastnameParts.length === 0) {
                  alert("Full name must contain both first and last name.");
                  return;
                }
                const lastname = lastnameParts.join(' ');

                const supplierData = {
                  firstname,
                  lastname,
                  email: this.selectedSupplier.email,
                  contactnumber: this.selectedSupplier.contact,
                  service: this.selectedSupplier.service,
                  username: this.selectedSupplier.username,
                  password: this.selectedSupplier.password,
                  userid: userid
                };

                console.log('Payload:', supplierData);

                const response = await axios.put(
                  `${this.baseURL}/edit-supplier/${this.selectedSupplier.no}`,
                  supplierData,
                  {
                    headers: {
                      Authorization: `Bearer ${token}`,
                    },
                  }
                );

                if (response.status === 200) {
                  alert("Supplier updated successfully!");

                  // Update the suppliers list with new price
                  const index = this.suppliers.findIndex(
                    (supplier) => supplier.no === this.selectedSupplier.no
                  );
                  if (index !== -1) {
                    this.suppliers[index] = {
                      ...this.selectedSupplier,
                      fullName: `${firstname} ${lastname}`,
                    };
                  }

                  this.closeEditSupplierBtn();
                } else {
                  alert("Failed to update supplier.");
                }
              } catch (error) {
                console.error("Error updating supplier:", error);
                if (error.response) {
                  alert(error.response.data.message);
                } else {
                  alert("Error updating supplier. Please try again.");
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

                const response = await axios.delete(`${this.baseURL}/created-users/${userid}`, {
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
            
      

    changeSuppliersPage(page) {
        this.currentSuppliersPage = page;
    },
    prevSuppliersPage() {
        if (this.currentSuppliersPage > 1) {
            this.currentSuppliersPage--;
        }
    },
    nextSuppliersPage() {
        if (this.currentSuppliersPage < this.totalSuppliersPages) {
            this.currentSuppliersPage++;
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
          if (this.selectedUserType === 'Suppliers') {
              this.addSupplierDetails = true;
              this.addStaffDetails = false;
          } else if (this.selectedUserType === 'Assistant' || this.selectedUserType === 'Staff') {
              this.addStaffDetails = true;
              this.addSupplierDetails = false;
          } else if (this.selectedUserType === 'Admin') {
              this.addStaffDetails = true;
              this.addSupplierDetails = false;    
          } else {
              this.addSupplierDetails = false;
              this.addStaffDetails = false;
          }
      },
  


    async editSupplier(supplier) {
      try {
        console.log('Editing supplier:', supplier);
        this.selectedSupplier = { ...supplier };
        // Fetch social media for the supplier
        const supplierId = supplier.no || supplier.supplier_id; // Handle both properties
        console.log('Fetching social media for supplier_id:', supplierId);
        const token = localStorage.getItem('access_token');
        const response = await axios.get(`${this.baseURL}/api/supplier/${supplierId}/social-media`, {
          headers: {
            Authorization: `Bearer ${token}`
          }
        });
        console.log('Social media response:', response.data);
        this.selectedSupplier.socialMedia = response.data;
        this.editSupplierForm = true;
        // Close any other modals that might be open
        this.showInactiveSuppliersModal = false;
        this.showSocialMediaModal = false;
        this.showStatusConfirmModal = false;
      } catch (error) {
        console.error('Error fetching supplier social media:', error);
        this.selectedSupplier.socialMedia = [];
        this.editSupplierForm = true;
      }
    },
    closeEditSupplierBtn() {
      this.editSupplierForm = false;
      this.selectedSupplier = null; 
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
    formatPrice(price) {
      if (price === null || price === undefined || typeof price === 'object' || isNaN(price)) {
        return 'N/A'; // Return a fallback if price is invalid
      }
      // Ensure price is treated as a number, round to 2 decimal places, and format with commas
      return parseFloat(price).toFixed(2).replace(/\d(?=(\d{3})+\.)/g, '$&,');
    },

    deriveUsername() {
      if (this.firstName && this.lastName) {
        const randomNum = Math.floor(Math.random() * 1000);
        this.username = `${this.firstName.toLowerCase()}${this.lastName.toLowerCase()}${randomNum}`;
      }
    },

    deriveEmail() {
      if (this.firstName && this.lastName) {
        this.email = `${this.firstName.toLowerCase()}.${this.lastName.toLowerCase()}@gmail.com`;
      }
    },

    prevAdminPage() {
      if (this.currentAdminPage > 1) {
        this.currentAdminPage--;
      }
    },
    nextAdminPage() {
      if (this.currentAdminPage < this.totalAdminPages) {
        this.currentAdminPage++;
      }
    },
    changeAdminPage(page) {
      this.currentAdminPage = page;
    },

    closeRateModal() {
      this.showRateModal = false;
      this.supplierRate = '';
    },

    async saveSupplierRate() {
      try {
        const token = localStorage.getItem('access_token');

        if (!this.selectedSupplier || !this.selectedSupplier.no) {
          alert("Supplier ID is missing or invalid.");
          return;
        }

        const response = await axios.put(
          `${this.baseURL}/edit-supplier/${this.selectedSupplier.no}`,
          {
            price: this.supplierRate
          },
          {
            headers: {
              Authorization: `Bearer ${token}`,
            },
          }
        );

        if (response.status === 200) {
          alert("Supplier rate updated successfully!");

          // Update the suppliers list with new price
          const index = this.suppliers.findIndex(
            (supplier) => supplier.no === this.selectedSupplier.no
          );
          if (index !== -1) {
            this.suppliers[index].price = this.supplierRate;
          }

          this.closeRateModal();
        }
      } catch (error) {
        console.error("Error updating supplier rate:", error);
        if (error.response) {
          alert(error.response.data.message);
        } else {
          alert("Error updating supplier rate. Please try again.");
        }
      }
    },
    async toggleSupplierStatus(supplier) {
      this.pendingSupplier = supplier;
      this.pendingStatus = supplier.status === 'active' ? 'inactive' : 'active';
      this.showStatusConfirmModal = true;
    },
    closeStatusConfirmModal() {
      this.showStatusConfirmModal = false;
      this.pendingSupplier = null;
      this.pendingStatus = '';
    },
    async confirmStatusChange() {
      try {
        const token = localStorage.getItem('access_token');
        
        const response = await axios.put(
          `${this.baseURL}/toggle-supplier-status/${this.pendingSupplier.no}`,
          {},
          {
            headers: {
              Authorization: `Bearer ${token}`,
            },
          }
        );

        if (response.status === 200) {
          if (response.data.new_status === 'inactive') {
            const index = this.suppliers.findIndex(s => s.no === this.pendingSupplier.no);
            if (index !== -1) {
              this.suppliers.splice(index, 1);
            }
            alert('Supplier has been set to Inactive');
          } else {
            const index = this.inactiveSuppliers.findIndex(s => s.no === this.pendingSupplier.no);
            if (index !== -1) {
              this.inactiveSuppliers.splice(index, 1);
            }
            await this.fetchSuppliers();
            alert('Supplier has been set to Active');
          }
          this.closeStatusConfirmModal();
        }
      } catch (error) {
        console.error("Error toggling supplier status:", error);
        if (error.response) {
          alert(`Error toggling supplier status: ${error.response.data.message}`);
        } else {
          alert("Error updating supplier status. Please try again.");
        }
        this.closeStatusConfirmModal();
      }
    },
    async showInactiveSuppliers() {
      try {
        const token = localStorage.getItem('access_token');
        const response = await axios.get(`${this.baseURL}/inactive-suppliers`, {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        });

        this.inactiveSuppliers = response.data.map(supplier => ({
          ...supplier,
          no: supplier.supplier_id // Ensure we have the 'no' property for consistency
        }));
        this.showInactiveSuppliersModal = true;
        this.editSupplierForm = false;
        this.showSocialMediaModal = false;
        this.showStatusConfirmModal = false;
      } catch (error) {
        console.error("Error fetching inactive suppliers:", error);
        alert("Error fetching inactive suppliers. Please try again.");
      }
    },

    closeInactiveSuppliersModal() {
      this.showInactiveSuppliersModal = false;
      this.inactiveSuppliers = [];
    },
    addSocialMediaModal(supplier) {
      console.log('Opening social media modal for supplier:', supplier);
      this.selectedSupplier = supplier;
      this.showSocialMediaModal = true;
      // Close any other modals that might be open
      this.showInactiveSuppliersModal = false;
      this.editSupplierForm = false;
      this.showStatusConfirmModal = false;
    },
    closeSocialMediaModal() {
      this.showSocialMediaModal = false;
      this.socialMediaForm = {
        platform: '',
        handle: '',
        url: ''
      };
    },
    async submitSocialMedia() {
      try {
        const token = localStorage.getItem('access_token');
        if (!token) {
          alert('Authentication token not found');
          return;
        }

        if (!this.selectedSupplier) {
          alert('No supplier selected');
          return;
        }

        if (!this.socialMediaForm.platform || !this.socialMediaForm.handle) {
          alert('Platform and handle are required fields');
          return;
        }

        const response = await axios.post(
          `${this.baseURL}/add-supplier-social-media`,
          {
            supplier_id: this.selectedSupplier.no || this.selectedSupplier.supplier_id, 
            ...this.socialMediaForm
          },
          {
            headers: {
              'Content-Type': 'application/json',
              'Authorization': `Bearer ${token}`
            }
          }
        );

        if (response.status === 200) {
          alert('Social media added successfully!');
          this.closeSocialMediaModal();
          await this.fetchSuppliers(); // Refresh supplier data
        }
      } catch (error) {
        console.error('Error adding social media:', error);
        alert(error.response?.data?.error || 'Failed to add social media');
      }
    },
    async editSupplier(supplier) {
      try {
        console.log('Editing supplier:', supplier);
        this.selectedSupplier = { ...supplier };
        // Fetch social media for the supplier
        console.log('Fetching social media for supplier_id:', supplier.no); 
        const response = await axios.get(`${this.baseURL}/api/supplier/${supplier.no}/social-media`, {
          headers: {
            Authorization: `Bearer ${localStorage.getItem('access_token')}`
          }
        });
        console.log('Social media response:', response.data);
        this.selectedSupplier.socialMedia = response.data;
        this.editSupplierForm = true;
      } catch (error) {
        console.error('Error fetching supplier social media:', error);
        this.selectedSupplier.socialMedia = [];
      }
    },
    addSocialMedia() {
      console.log('Opening social media modal for supplier:', this.selectedSupplier);
      this.showSocialMediaModal = true;
    },
    async toggleInactiveSupplierStatus(supplier) {
      this.pendingSupplier = supplier;
      this.pendingStatus = 'active';
      this.showStatusConfirmModal = true;
    },
    editInactiveSupplier(supplier) {
      console.log('Editing inactive supplier:', supplier);
      this.selectedSupplier = { ...supplier };
      // Ensure we have the supplier_id
      this.selectedSupplier.no = supplier.supplier_id;
      this.editSupplierForm = true;
      this.showInactiveSuppliersModal = false;
    },
    addInactiveSupplierSocialMedia(supplier) {
      console.log('Adding social media for inactive supplier:', supplier);
      this.selectedSupplier = { ...supplier };
      // Ensure we have the supplier_id
      this.selectedSupplier.no = supplier.supplier_id;
      this.showSocialMediaModal = true;
      this.showInactiveSuppliersModal = false;
    },
    async confirmStatusChange() {
      try {
        const token = localStorage.getItem('access_token');
        
        const response = await axios.put(
          `${this.baseURL}/toggle-supplier-status/${this.pendingSupplier.no}`,
          {},
          {
            headers: {
              Authorization: `Bearer ${token}`,
            },
          }
        );

        if (response.status === 200) {
          if (response.data.new_status === 'inactive') {
            const index = this.suppliers.findIndex(s => s.no === this.pendingSupplier.no);
            if (index !== -1) {
              this.suppliers.splice(index, 1);
            }
            alert('Supplier has been set to Inactive');
          } else {
            const index = this.inactiveSuppliers.findIndex(s => s.no === this.pendingSupplier.no);
            if (index !== -1) {
              this.inactiveSuppliers.splice(index, 1);
            }
            await this.fetchSuppliers();
            alert('Supplier has been set to Active');
          }
          this.closeStatusConfirmModal();
        }
      } catch (error) {
        console.error("Error toggling supplier status:", error);
        if (error.response) {
          alert(`Error toggling supplier status: ${error.response.data.message}`);
        } else {
          alert("Error updating supplier status. Please try again.");
        }
        this.closeStatusConfirmModal();
      }
    },
  },
  mounted() {
    if (this.showTable === 'Suppliers') {
        this.fetchSuppliers(); // Fetch staff data on component mount
    } else if (this.showTable === 'Staffs') {
        this.fetchStaffs();  // Fetch vendor data on component mount
    } else if (this.showTable === 'Admin') {
      this.fetchAdmins();
    }
},

watch: {
    showTable(newTable) {
        if (newTable === 'Staffs') {
            this.fetchStaffs();
        } else if (newTable === 'Suppliers') {
            this.fetchSuppliers();
        } else if (newTable === 'Admin') {
            this.fetchAdmins();
        }
    },

    staffs(newStaffs) {
    console.log('Staffs updated:', newStaffs);
    console.log('Number of staffs:', newStaffs.length);
    console.log('Current staffs page:', this.currentStaffsPage);
    console.log('Total staffs pages:', this.totalStaffsPages);
  }
},
};
</script>

<style scoped>
/* Add any scoped styles here */
</style>
