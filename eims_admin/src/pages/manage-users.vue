<template>
   <div class="bg-gray-200 w-full h-full">
    <div class="w-full h-[65px] bg-gray-100 mt-2 flex items-center justify-between px-5 shadow-lg">
    <h1 class="font-amaticBold font-extraLight text-3xl">
    Accounts
  </h1>
  </div>

  <div class="flex flex-row items-center m-5 space-x-5">
    <div class="flex justify-start w-52 h-20 bg-white rounded-lg shadow-lg px-2 items-center border-l-2 border-green-400 space-x-5">
        <img class="w-auto h-12" src="/img/vendor2.png" alt="Vendor Image">
        <h2 class="font-amaticRegular text-4xl font-bold mb-0">{{ totalSuppliers }} <span class = "text-sm antialiased text-gray-600">suppliers</span></h2>
    </div>
    <div class="flex justify-start w-52 h-20 bg-white rounded-lg shadow-lg px-2 items-center border-l-2 border-blue-400 space-x-5">
        <img class="w-auto h-12" src="/img/staff.png" alt="Vendor Image">
        <h2 class="font-amaticRegular text-4xl font-bold mb-0">{{ totalStaff }} <span class = "text-sm antialiased text-gray-600">staff</span></h2>
    </div>
    <div class="flex justify-start w-52 h-20 bg-white rounded-lg shadow-lg px-2 items-center border-l-2 border-blue-400 space-x-5">
        <img class="w-auto h-12" src="/img/admin.png" alt="Vendor Image">
        <h2 class="font-amaticRegular text-4xl font-bold mb-0">{{ totalAdmin }} <span class = "text-sm antialiased text-gray-600">admin</span></h2>
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

<div class="flex flex-row justify-between items-center m-5 my-5">
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
 + Add Account
</button>
</div>


<!--- Supplier Table --->
<div v-if="showTable === 'Suppliers'" class="relative shadow-md sm:rounded-xl w-[1170px] h-[200] ml-5 mt-2 font-amaticBold mb-10">
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
                        <button
                            class="h-8 w-12 bg-[#9B111E] font-amaticBold font-medium text-sm rounded-md text-white hover:bg-[#B73A45]" 
                            @click="editSupplierBtn(index)">
                            Edit
                        </button>
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
  <div v-if="showTable === 'Staffs'" class="relative shadow-md sm:rounded-xl w-[1170px] h-[200] ml-5 mt-2 font-amaticBold mb-10">
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
          <th scope="row" class="px-2 py-3 font-medium text-gray-900 whitespace-nowrap dark:text-white">{{ staff.dummyIndex }}</th>
          <td class="px-1 py-3 hidden sm:table-cell">{{ staff.fullName }}</td>
          <td class="px-1 py-3 hidden sm:table-cell">{{ staff.email }}</td>
          <td class="px-1 py-3 hidden sm:table-cell">{{ staff.contact }}</td>
          <td class="px-1 py-3 hidden sm:table-cell">{{ staff.position }}</td>

          <td class="px-1 py-3 hidden sm:table-cell">
            <button class="h-8 w-12 bg-[#9B111E] font-amaticBold font-medium text-sm rounded-md text-white hover:bg-[#B73A45]"
            @click="editStaffBtn(index)">
                Edit
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
<div v-if="showTable === 'Admin'" class="relative shadow-md sm:rounded-xl w-[1170px] h-[200] ml-5 mt-2 font-amaticBold mb-10">
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
                        <button class="h-8 w-12 bg-[#9B111E] font-amaticBold font-medium text-sm rounded-md text-white hover:bg-[#B73A45]" @click="editAdminBtn(index)">Edit</button>
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
 <form v-if="addUserForm" @submit.prevent="handleRegister" class="flex justify-center items-center fixed inset-0 bg-gray-800 bg-opacity-50 overflow-y-auto" @click.self="closeAddUserForm">
  <div class="bg-white w-[500px] p-5 rounded-lg shadow-lg overflow-y-auto">
    <div class="flex justify-between items-center m-3">
      <h1 class="font-semibold text-xl font-raleway text-gray-800">Add Account</h1>
    </div>
    <div class="border border-gray-500 mt-5 items-center"></div>
    <div class="m-5">
      <span class = "text-red-500">* {{ errorMessage }}</span>
      <!-- First Name and Last Name -->
      <div class="flex flex-row">
        <div class="flex items-center space-x-2">
          <input type="text" class="mt-2 ml-2 p-2 w-full h-10 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:border-blue-700" v-model="firstName" placeholder="First Name" required>
        </div>
        <div class="flex items-center space-x-2">
          <input type="text" class="mt-2 ml-2 p-2 w-full h-10 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:border-blue-700" v-model="lastName" placeholder="Last Name" required>
        </div>
      </div>

      <!-- Username -->
      <div class="mt-5">
        <input type="text" class="mt-2 ml-2 p-2 w-full h-10 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:border-blue-700" v-model="username" @click="deriveUsername" placeholder="Username" required>
      </div>

      <!-- Email -->
      <div class="mt-5">
        <input type="text" class="mt-2 ml-2 p-2 w-full h-10 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:border-blue-700" v-model="email" @click="deriveEmail" placeholder="Email" required>
      </div>

      <!-- Contact Number -->
      <div class="mt-5">
        <input type="text" class="mt-2 ml-2 p-2 w-full h-10 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:border-blue-700" v-model="contactNumber" placeholder="Contact Number" required>
      </div>

      <!-- Address -->
      <div class="mt-5">
        <input type="text" class="mt-2 ml-2 p-2 w-full h-10 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:border-blue-700" v-model="address" placeholder="Address" required>
      </div>


      <!-- User Type Selection -->
      <div class="mt-5">
        <select class="flex mt-4 ml-2 p-2 w-52 h-10 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:border-blue-700" v-model="selectedUserType" @change="selectAddForm">
          <option value="" class="text-gray-700" disabled selected>Select a Type of User</option>
          <option value="Suppliers">Supplier</option>
          <option value="Staff">Staff</option>
          <option value="Admin">Admin</option>
        </select>
      </div>

      <!-- Suppliers Details (only if supplier is selected) -->
      <div v-if="addSupplierDetails" class="mt-5">
        <select class="mt-2 ml-2 p-2 w-full h-10 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:border-blue-700" v-model="service">
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

        <div class="flex items-center mt-4">
          <input type="text" class="mt-2 ml-2 p-2 w-[200px] h-10 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:border-blue-700" v-model="price" placeholder="Supplier Rate" required>
    
        </div>
      </div>

      <!-- Confirm Button -->
      <div class="flex justify-center items-center mt-10 space-x-2">
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


<!--Edit Supplier Form-->
<form v-if="editSupplierForm" class = "flex justify-center items-center fixed inset-0 bg-gray-800 bg-opacity-50 flex justify-center items-center" @click.self="closeEditSupplierBtn">
  <div class = "bg-white w-[500px] p-5 rounded-lg shadow-lg  overflow-y-auto">
        <div class = "flex justify-between items-center m-3">
              <h1 class = "font-semibold text-xl font-raleway text-gray-800">Edit Supplier</h1>
        </div>
        <div class = "border border-gray-500 mt-5 items-center"></div>
               <div class = "m-5">

             
                <div class = "flex items-center space-x-2">
                  <input type="text"  v-model="selectedSupplier.fullName" class = "mt-2 ml-2 p-2 w-full h-10 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:border-blue-700" placeholder="Name" required>
              
              </div>
              <div class = "mt-5">
                <div class = "flex items-center">
                  <input type="text"  v-model="selectedSupplier.username" class = "mt-2 ml-2 p-2 w-full h-10 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:border-blue-700" placeholder="Username" required>
                </div>
              </div>
              <div class = "mt-5">
                <div class = "flex items-center">
                  <input type="text"  v-model="selectedSupplier.email" class = "mt-2 ml-2 p-2 w-full h-10 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:border-blue-700" placeholder="Email" required>
                </div>
              </div>

              <div class = "mt-5">
                <div class = "flex items-center">
                  <input type="text"  v-model="selectedSupplier.contact" class = "mt-2 ml-2 p-2 w-full h-10 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:border-blue-700" placeholder="Contact Number" required>
                </div>
              </div>
  
              <div class = "mt-5">
                <div class = "flex items-center">
                  <select v-model="selectedSupplier.service" class = "mt-2 ml-2 p-2 w-full h-10 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:border-blue-700">
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
                  <input type="text" v-model="selectedSupplier.price" class = "mt-2 ml-2 p-2 w-[200px] h-10 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:border-blue-700" id ="minPrice" placeholder="Price" required>
                </div>
 
              </div>

              <div v-if = "addStaffDetails" class = "mt-5">
                <div class = "flex items-center">
                  <select class = "mt-2 ml-2 p-2 w-full h-10 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:border-blue-700">
                    <option value="" class = "text-gray-700" disabled selected>Select Position</option>
                    <option value="Staff">Staff</option>
                  </select>
                </div>
 
              </div>

              <div class = "flex  justify-center items-center mt-10 space-x-3">
                <button class="w-20 h-10 bg-gray-300 text-white px-3 py-1 rounded transform-transition duration-300 transform hover:scale-105 hover:bg-gray-400" @click="closeEditSupplierBtn">
                  Cancel
                </button>
                   <button @click.prevent ="confirmEditSupplier" class = "w-20 h-10 bg-blue-500 text-gray-100 font-semibold rounded-lg shadow-md  transform-transition duration-300 transform hover:scale-105">
                     Save
                   </button>
              </div>


        </div>
  </div>
</form> 

<!--Edit Staff Form-->
<form v-if="editStaffForm" class = "flex justify-center items-center fixed inset-0 bg-gray-800 bg-opacity-50 flex justify-center items-center" @click.self="closeEditStaffBtn">
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
                    <option value="Admin">Admin</option>     
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
      showTable: 'Suppliers',
      currentSuppliersPage: 1,
      rowsPerSuppliersPage: 6,

      currentStaffsPage: 1,
      rowsPerStaffsPage: 6,
      
      currentAdminPage: 1,
      adminPerPage: 6,

      addUserForm: false,
      addSupplierDetails: false,
      addStaffDetails: false,
      selectedOption: '',

      editSupplierForm: false,
      selectedSupplier: null, 
      editSupplierForm: false,

      editStaffForm: false,
      selectedStaff: null, 
      editStaffForm: false,

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
      errorMessage: '',

      staffs: [],
      suppliers: [],
      admins: [],
      searchTerm: '',

      


      
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
                    if (!this.service || !this.price) {
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
                    requestData.price = this.price;
                }

                // Send the request to the backend
                const response = await axios.post('http://127.0.0.1:5000/add-user', requestData);

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
            this.price = '';
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

              const response = await axios.get('http://127.0.0.1:5000/created-users', {
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

              const response = await axios.get('http://127.0.0.1:5000/suppliers', {
                  headers: {
                      'Content-Type': 'application/json',
                      'Authorization': `Bearer ${token}`,
                  },
                  withCredentials: true,
              });

              console.log(response.data); // Log the response to verify

              // Populate suppliers array with data from API
              this.suppliers = response.data.map((supplier, index) => ({
                  no: supplier.supplier_id,
                  fullName: `${supplier.firstname} ${supplier.lastname}`,
                  email: supplier.email,
                  username: supplier.username,
                  password: supplier.password,
                  contact: supplier.contactnumber,
                  service: supplier.service,
                  price: supplier.price,
                  userid: supplier.userid, // Include userid here
                  dummyIndex: index + 1, // Properly set the dummyIndex here
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
            const response = await axios.get('http://127.0.0.1:5000/get_admin', {
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
                  'fullName', 'email', 'contact', 'service', 'price', 'username', 'password'
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
                  price: this.selectedSupplier.price,
                  username: this.selectedSupplier.username,
                  password: this.selectedSupplier.password,
                  userid: userid
                };

                console.log('Payload:', supplierData);

                const response = await axios.put(
                  `http://127.0.0.1:5000/edit-supplier/${this.selectedSupplier.no}`,
                  supplierData,
                  {
                    headers: {
                      Authorization: `Bearer ${token}`,
                    },
                  }
                );

                if (response.status === 200) {
                  alert("Supplier updated successfully!");

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
                  alert(`Error updating supplier: ${error.response.data.message}`);
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
  


    editSupplierBtn(index){
      this.editSupplierForm = true;
      const selectedSupplier = this.suppliers[index]; 
      this.supplierFormData = { ...selectedSupplier };
    },

    closeEditSupplierBtn() {
      this.editSupplierForm = false;
    },

    editSupplierBtn(index) {
        this.selectedSupplier = this.paginatedSuppliers[index]; 
        this.editSupplierForm = true; // Show the edit form
    },
    closeEditUserBtn() {
        this.editUserForm = false; 
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
