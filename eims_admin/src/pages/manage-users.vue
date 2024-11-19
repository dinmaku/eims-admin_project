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
        <h2 class="font-amaticRegular text-4xl font-bold mb-0">{{ totalVendors }} <span class = "text-sm antialiased text-gray-600">vendors</span></h2>
    </div>
    <div class="flex justify-start w-52 h-20 bg-white rounded-lg shadow-lg px-2 items-center border-l-2 border-blue-400 space-x-5">
        <img class="w-auto h-12" src="/img/staff.png" alt="Vendor Image">
        <h2 class="font-amaticRegular text-4xl font-bold mb-0">{{ totalStaff }} <span class = "text-sm antialiased text-gray-600">staffs</span></h2>
    </div>
</div>

<div class="flex flex-row justify-between items-center m-5 my-5">
  <div class = "flex">
  <button :class="[ 
    'flex justify-center items-center w-28 h-10 m-2 font-raleway font-semibold rounded-lg shadow-lg transition-transform duration-300 transform hover:scale-105', 
    { 'bg-white text-teal-800': showTable === 'vendors', 'bg-gray-800 text-white': showTable !== 'vendors' } 
  ]" @click="showTable = 'vendors'">
    Vendors
  </button>
  
  <button :class="[ 
    'flex justify-center items-center w-28 h-10 m-2 font-raleway font-semibold rounded-lg shadow-lg transition-transform duration-300 transform hover:scale-105', 
    { 'bg-white text-teal-800': showTable === 'staffs', 'bg-gray-800 text-white': showTable !== 'staffs' } 
  ]" @click="showTable = 'staffs'">
    Staffs
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
            <td class="px-1 py-3 hidden sm:table-cell">{{ vendor.Name }}</td>
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
            <th scope="col" class="px-2 py-3">Salary per Month</th>
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
            <td class="px-1 py-3 hidden sm:table-cell">{{ staff.salary }}</td>
  
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

  <!--Add User Form-->
<form v-if="addUserForm" class = "flex justify-center items-center fixed inset-0 bg-gray-800 bg-opacity-50 flex justify-center items-center">
  <div class = "bg-white w-[500px] p-5 rounded-lg shadow-lg  overflow-y-auto">
        <div class = "flex justify-between items-center m-3">
              <h1 class = "font-semibold text-xl font-raleway text-gray-800">Add User</h1>
               <button class="mt-2 bg-red-500 text-white px-3 py-1 rounded transform-transition duration-300 transform hover:scale-105" @click="closeAddUserForm">
                  Close
                </button>
        </div>
        <div class = "border border-gray-500 mt-5 items-center"></div>
               <div class = "m-5">

              
                <div class = "flex items-center space-x-2">
                  <input type="text"class = "mt-2 ml-2 p-2 w-full h-10 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:border-blue-700" placeholder="Full Name" required>
                </div>
  
              <div class = "mt-5">
                <div class = "flex items-center">
                  <input type="text" class = "mt-2 ml-2 p-2 w-full h-10 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:border-blue-700" id ="full-name" placeholder="Email" required>
                </div>
              </div>
              <div class = "mt-5">
                <div class = "flex items-center">
                  <input type="text" class = "mt-2 ml-2 p-2 w-full h-10 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:border-blue-700" id ="full-name" placeholder="Contact Number" required>
                </div>
              </div>
              <div class = "mt-5">
                <div class = "flex items-center">
                  <input type="text" class = "mt-2 ml-2 p-2 w-full h-10 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:border-blue-700" id ="full-name" placeholder="Address" required>
                </div>
              </div>
              <div class = "mt-5">
                <div class = "flex items-center">
                  <input type="password" class = "mt-2 ml-2 p-2 w-full h-10 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:border-blue-700" id ="full-name" placeholder="Password" required>
                </div>
              </div>

              <div class="mt-5">
                      <select 
                        class="flex mt-4 ml-2 p-2 w-52 h-10 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:border-blue-700"
                        v-model="selectedOption" 
                        @change="selectAddForm"
                      >
                        <option value="" class = "text-gray-700" disabled selected>Select a Type of User</option>
                        <option value="vendors">Vendors</option>
                        <option value="staffs">Staffs</option>
                      </select>
                    </div>

              <div v-if = "addVendorDetails" class = "mt-5">
                <div class = "flex items-center">
                  <select type="text" class = "mt-2 ml-2 p-2 w-full h-10 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:border-blue-700">
                    <option value="" class = "text-gray-700" disabled selected>Select Service Type</option>
                    <option value="">Catering</option>
                    <option value="">Hair and Makeup</option>
                    <option value="">Host</option>
                    <option value="">Entertainer / Singer</option>
                    <option value="">Photographer and Videographer</option>
                    <option value="">Sound and Lighting</option>
                    <option value="">Transportation</option>
                    <option value="">Invitations and Stationery</option>
                    <option value="">Favor and Gifts</option>
                </select>
                </div>
                <div class = "flex items-center mt-4">
                  <input type="text" class = "mt-2 ml-2 p-2 w-[200px] h-10 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:border-blue-700" id ="minPrice" placeholder="Minimum Price" required>
                  <input type="text" class = "mt-2 ml-2 p-2 w-[200px] h-10 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:border-blue-700" id ="maxPrice" placeholder="Maximum Price" required>
                </div>
 
              </div>

              <div v-if = "addStaffDetails" class = "mt-5">
                <div class = "flex items-center">
                  <select class = "mt-2 ml-2 p-2 w-full h-10 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:border-blue-700">
                    <option value="" class = "text-gray-700" disabled selected>Select Position</option>
                    <option value="manager">Assistant</option>
                    <option value="secretary">Secretary</option>
                    <option value="receptionist">Receptionist</option>
                    <option value="waiter">Waiter</option>
                  </select>
                </div>
                <div class = "flex items-center mt-4">
                  <input type="text" class = "mt-2 ml-2 p-2 w-[200px] h-10 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:border-blue-700" id ="salary" placeholder="Salary per Month" required>
                </div>
              </div>
           

              <div class = "flex justify-center items-center mt-10">
                   <button class = "w-20 h-10 bg-blue-500 text-gray-100 font-semibold rounded-lg shadow-md  transform-transition duration-300 transform hover:scale-105">
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
                  <input type="text"  v-model="selectedVendor.Name" class = "mt-2 ml-2 p-2 w-full h-10 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:border-blue-700" placeholder="Name" required>
              
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
                    <option value="manager">Manager</option>
                    <option value="secretary">Secretary</option>
                    <option value="receptionist">Receptionist</option>
                    <option value="waiter">Waiter</option>
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
                    <option value="Manager">Assistant</option>
                    <option value="Assistant">Assistant</option>
                    <option value="Secretary">Secretary</option>
                    <option value="Tailor">Tailoring</option>
                  
                  </select>
                </div>
                
                <div class = "flex items-center mt-4">
                  <input type="text" v-model="selectedStaff.salary" class = "mt-2 ml-2 p-2 w-[200px] h-10 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:border-blue-700" id ="salary" placeholder="Salary per Month" required>
                </div>
 
              </div>
              <div class = "flex items-center mt-4">
                  <input type="text" v-model="selectedStaff.salary" class = "mt-2 ml-2 p-2 w-[200px] h-10 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:border-blue-700" id ="salary" placeholder="Salary per Month" required>
                </div>

              <div class = "flex justify-center items-center mt-10 space-x-3">
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

</div>
</template>

<script>
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



      vendors: [
        { no: 1, Name: 'Delightful Bites Catering', email: 'bites.catering@example.com', contact: '123-456-7890', service: 'Catering', minPrice:'30k php', maxPrice: '250k php' },
        { no: 2, Name: 'Vivid Memories Media', email: 'vivid.media@example.com', contact: '234-567-8901', service: 'Multimedia', minPrice:'20k php', maxPrice: '120k php' },
        { no: 3, Name: 'Elegant Eats Events', email: 'elegant.eats@example.com', contact: '345-678-9012', service: 'Catering', minPrice: '20k php', maxPrice: '150k php' },
        { no: 4, Name: 'Elegant Essence', email: 'essence22@example.com', contact: '456-789-0123', service: 'Hair and Makeup', minPrice: '10k php', maxPrice: '40k php' },
        { no: 5, Name: 'Nico Shepherd', email: 'nico.shepherd@example.com', contact: '567-890-1234', service: 'Sound and Light', minPrice: '20k php', maxPrice: '70k php' },
        { no: 6, Name: 'Jovit Baldemonyo', email: 'jovit.baldemonyo@example.com', contact: '678-901-2345', service: 'Entertainment', minPrice: '5k php', maxPrice: '80k php' },
        { no: 7, Name: 'November Revenue', email: 'november.revenue@example.com', contact: '789-012-3456', service: 'Entertainment', minPrice: '10k php', maxPrice: '100k php' },
        { no: 8, Name: 'Edward Backward', email: 'edward.backward@example.com', contact: '890-123-4567', service: 'Host', minPrice: '7k php', maxPrice: '40k php' },
        { no: 9, Name: 'Vintage Car Rentals', email: 'vintage.rentals@example.com', contact: '901-234-5678', service: 'Transportation', minPrice: '15k php', maxPrice: '60k php' },
        { no: 10, Name: 'Custom Invitations Studio', email: 'custom.studio@example.com', contact: '012-345-6789', service: 'Invitations and Stationery', minPrice: '20k php', maxPrice: '70k php' },
        { no: 11, Name: 'Personalized Keepsakes Co.', email: 'personalized.keepsakes@example.com', contact: '123-456-7890', service: 'Favors and Gifts', minPrice: '15k php', maxPrice: '100k php' },
        { no: 12, Name: 'Radiant Luxe Studio', email: 'radiant.luxe@example.com', contact: '234-567-8901', service: 'Hair and Makeup', minPrice: '7k php', maxPrice: '30k php' }
      ],


      staffs: [
        { no: 1, fullName: 'Ashley Calimpong', email: 'ashley.calimpong@example.com', contact: '555-123-4567', position: 'Manager', salary: 'Null'},
        { no: 2, fullName: 'Bob Smith', email: 'bob.s@example.com', contact: '555-234-5678', position: 'Assistant',salary: '12k php' },
        { no: 3, fullName: 'Charlie Brown', email: 'charlie.b@example.com', contact: '555-345-6789', position: 'Tailor', salary: '10k php'},
        { no: 4, fullName: 'Diana Prince', email: 'diana.p@example.com', contact: '555-456-7890', position: 'Assistant', salary: '12k php'},
        { no: 5, fullName: 'Ethan Hunt', email: 'ethan.h@example.com', contact: '555-567-8901', position: 'Assistant', salary: '12k php'},
        { no: 6, fullName: 'Fiona Green', email: 'fiona.g@example.com', contact: '555-678-9012', position: 'Tailor', salary: '10k php'},
      ],
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

    selectAddForm(){
       this.addVendorDetails = false;
       this.addStaffDetails = false;

       if(this.selectedOption ===  'vendors') {
        this.addVendorDetails = true;

       } else if(this.selectedOption ===  'staffs') {
          this.addStaffDetails = true;
        
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
        this.selectedStaff = this.paginatedStaffs[index]; 
        this.editStaffForm = true; 
    },
    closeEditStaffBtn() {
        this.editStaffForm = false;
        this.selectedStaff = null; 
    },
    
  }
};
</script>

<style scoped>
/* Add any scoped styles here */
</style>
