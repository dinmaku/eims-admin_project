<template>
    <div class="bg-gray-200 w-full h-full">
    <div class="w-full h-[65px] bg-gray-100 mt-2 flex items-center justify-between px-5 shadow-lg">
    <h1 class="font-amaticBold font-extraLight text-3xl">
    Manage Outfits
  </h1>
   <div class ="flex items-center">
    <select @change="setOutfitDisplay" v-model="selectedOption" class="bg-white font-amaticBold font-semibold border border-gray-100 rounded-md py-2 px-3 text-gray-700 shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 mr-5">
    <option value ="booked-outfit">Booked Attire</option>
    <option value="outfits-arch">Outfits Archive</option>
  </select>
   </div>
  </div>

  <!--Booked Outfits-->
  <div v-if="displayBookedOutfits">
  <div class="flex flex-row items-center m-5 space-x-5">
    <div class="flex justify-start w-52 h-20 bg-white rounded-lg shadow-lg px-2 items-center border-l-2 border-red-400 space-x-5">
        <img class="w-auto h-12" src="/img/gowns-booked.png" alt="Gown Image">
        <h2 class="font-amaticRegular text-4xl font-bold mb-0"> {{ totalBookedGowns() }} <span class = "text-xs antialiased text-gray-600">booked gowns</span></h2>
    </div>
    <div class="flex justify-start w-52 h-20 bg-white rounded-lg shadow-lg px-2 items-center border-l-2 border-cyan-400 space-x-5">
        <img class="w-auto h-12" src="/img/suit.png" alt="Gown Image">
        <h2 class="font-amaticRegular text-4xl font-bold mb-0"> {{ totalBookedGowns() }} <span class = "text-xs antialiased text-gray-600">booked suits</span></h2>
    </div>
</div>


<div class="flex flex-row justify-between items-center m-5 my-5">
  <div class = "flex">
  <button :class="[ 
    'flex justify-center items-center w-28 h-10 m-2 font-raleway font-semibold rounded-lg shadow-lg transition-transform duration-300 transform hover:scale-105', 
    { 'bg-gray-800 text-white ': showTable === 'gowns', 'bg-white text-teal-800': showTable !== 'gowns' } 
  ]" @click="showTable = 'gowns'">
    Gowns
  </button>
  
  <button :class="[ 
    'flex justify-center items-center w-28 h-10 m-2 font-raleway font-semibold rounded-lg shadow-lg transition-transform duration-300 transform hover:scale-105', 
    { 'bg-gray-800 text-white ': showTable === 'tuxedos', 'bg-white text-teal-800': showTable !== 'tuxedos' } 
  ]" @click="showTable = 'tuxedos'">
    Tuxedo
  </button>
</div>
<button class = "mr-2 w-28 h-10 bg-[#9B111E] font-semibold text-gray-100 font-quicksand rounded-full shadow-lg 
transition-transform duration-300 transform hover:scale-105" @click="addOutBtn">
 + Add Outfit
</button>
</div>


<!---Booked Gowns Table-->
<div v-if="showTable === 'gowns'" class="relative shadow-md sm:rounded-xl w-[1170px] h-[200] ml-5 mt-2 font-amaticBold mb-10">
    <div class="overflow-x-auto">
      <table class="w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400 mb-4 max-h-30">
        <thead class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
          <tr>
            <th scope="col" class="px-2 py-3">#</th>
            <th scope="col" class="px-2 py-3">Outfit Name</th>
            <th scope="col" class="px-2 py-3">Booked By</th>
            <th scope="col" class="px-2 py-3">Contact</th>
            <th scope="col" class="px-2 py-3">Pickup Date</th>
            <th scope="col" class="px-2 py-3">Return Date</th>
            <th scope="col" class="px-2 py-3">Status</th>
            <th scope="col" class="px-2 py-3">Price</th>
            <th scope="col" class="px-2 py-3">Additional Charges</th>
            <th scope="col" class="px-2 py-3">Action</th>
          </tr>
        </thead>
        <tbody>
          <tr
              v-for="(gown, index) in paginatedGowns"
              :key="gown.no"
              class="border-b dark:border-gray-700 odd:bg-white odd:dark:bg-gray-900 even:bg-gray-50 even:dark:bg-gray-800">
            <th scope="row" class="px-2 py-3 font-medium text-gray-900 whitespace-nowrap dark:text-white">{{ gown.no }}</th>
            <td class="px-1 py-3 hidden sm:table-cell">{{ gown.name }}</td>
            <td class="px-1 py-3 hidden sm:table-cell">{{ gown.bookedBy }}</td>
            <td class="px-1 py-3 hidden sm:table-cell">{{ gown.contact }}</td>
            <td class="px-1 py-3 hidden sm:table-cell">{{ gown.pickupDate }}</td>
            <td class="px-1 py-3 hidden sm:table-cell">{{ gown.returnDate }}</td>
            <td class="px-1 py-3 hidden sm:table-cell">{{ gown.status }}</td>
            <td class="px-1 py-3 hidden sm:table-cell">{{ gown.price }}</td>
            <td class="px-1 py-3 hidden sm:table-cell">{{ gown.additionalCharges }}</td>
            <td class="px-1 py-3 hidden sm:table-cell">
              <button
                  class="h-8 w-12 bg-[#9B111E] font-amaticBold font-medium text-sm rounded-md text-white hover:bg-[#B73A45]" @click="editGownBtn(index)">
                  Edit
                </button>
            </td>
          </tr>
        </tbody>
      </table>

       <!-- Pagination Controls -->
       <div class="flex justify-center space-x-2 mt-4 mb-6">
        <button @click="prevGownsPage" :disabled="currentGownsPage === 1" class="px-3 py-1 bg-[#9B111E] text-white rounded-md hover:bg-[#B73A45] disabled:opacity-50 text-md">Previous</button>
        <button v-for="page in totalGownsPages" :key="page" @click="changeGownsPage(page)" :class="{'bg-[#9B111E]': currentGownsPage === page, 'bg-gray-300': currentGownsPage !== page}" class="px-3 py-1 text-white rounded-md hover:bg-[#B73A45] text-xs">
          {{ page }}
        </button>
        <button @click="nextGownsPage" :disabled="currentGownsPage === totalGownsPages" class="px-3 py-1 bg-[#9B111E] text-white rounded-md hover:bg-[#B73A45] disabled:opacity-50 text-xs">Next</button>
      </div>
    </div>
  </div>

  <!---Booked Tuxedo Table-->
  <div v-if="showTable === 'tuxedos'" class="relative shadow-md sm:rounded-xl w-[1170px] h-[200] ml-5 mt-2 font-amaticBold mb-10">
    <div class="overflow-x-auto">
      <table class="w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400 mb-4 max-h-30">
        <thead class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
          <tr>
            <th scope="col" class="px-2 py-3">#</th>
            <th scope="col" class="px-2 py-3">Outfit Name</th>
            <th scope="col" class="px-2 py-3">Booked By</th>
            <th scope="col" class="px-2 py-3">Contact</th>
            <th scope="col" class="px-2 py-3">Pickup Date</th>
            <th scope="col" class="px-2 py-3">Return Date</th>
            <th scope="col" class="px-2 py-3">Status</th>
            <th scope="col" class="px-2 py-3">Price</th>
            <th scope="col" class="px-2 py-3">Additional Charges</th>
            <th scope="col" class="px-2 py-3">Action</th>
          </tr>
        </thead>
        <tbody>
          <tr
              v-for="(tuxedo, index) in paginatedTuxedos"
              :key="tuxedo.no"
              class="border-b dark:border-gray-700 odd:bg-white odd:dark:bg-gray-900 even:bg-gray-50 even:dark:bg-gray-800">
            <th scope="row" class="px-2 py-3 font-medium text-gray-900 whitespace-nowrap dark:text-white">{{ tuxedo.no }}</th>
            <td class="px-1 py-3 hidden sm:table-cell">{{ tuxedo.name }}</td>
            <td class="px-1 py-3 hidden sm:table-cell">{{ tuxedo.bookedBy }}</td>
            <td class="px-1 py-3 hidden sm:table-cell">{{ tuxedo.contact }}</td>
            <td class="px-1 py-3 hidden sm:table-cell">{{ tuxedo.pickupDate }}</td>
            <td class="px-1 py-3 hidden sm:table-cell">{{ tuxedo.returnDate }}</td>
            <td class="px-1 py-3 hidden sm:table-cell">{{ tuxedo.status }}</td>
            <td class="px-1 py-3 hidden sm:table-cell">{{ tuxedo.price }}</td>
            <td class="px-1 py-3 hidden sm:table-cell">{{ tuxedo.additionalCharges }}</td>
            <td class="px-1 py-3 hidden sm:table-cell">
              <button
                  class="h-8 w-12 bg-[#9B111E]font-amaticBold font-medium text-sm rounded-md text-white hover:bg-[#B73A45]" @click="editTuxedoBtn(index)">
                  Edit
                </button>
            </td>
          </tr>
        </tbody>
      </table>

      <!-- Pagination Controls -->
      <div class="flex justify-center space-x-2 mt-4 mb-6">
        <button @click="prevTuxedosPage" :disabled="currentTuxedosPage === 1" class="px-3 py-1 bg-[#9B111E] text-white rounded-md hover:bg-[#B73A45] disabled:opacity-50 text-md">Previous</button>
        <button v-for="page in totalTuxedosPages" :key="page" @click="changeTuxedosPage(page)" :class="{'bg-[#9B111E]': currentTuxedosPage === page, 'bg-gray-300': currentTuxedosPage !== page}" class="px-3 py-1 text-white rounded-md hover:bg-[#B73A45] text-xs">
          {{ page }}
        </button>
        <button @click="nextTuxedosPage" :disabled="currentTuxedosPage === totalTuxedosPages" class="px-3 py-1 bg-[#9B111E] text-white rounded-md hover:bg-[#B73A45] disabled:opacity-50 text-xs">Next</button>
      </div>
    </div>
  </div>

</div>

 <div v-if="displayArchivedOutfits">
  <div class="flex flex-row items-center m-5 space-x-5">
    <div class="flex justify-start w-52 h-20 bg-white rounded-lg shadow-lg px-2 items-center border-l-2 border-red-400 space-x-5">
        <img class="w-auto h-12" src="/img/gowns-booked.png" alt="Gown Image">
        <h2 class="font-amaticRegular text-4xl font-bold mb-0"> <span class = "text-sm antialiased text-gray-600">gowns</span></h2>
    </div>
    <div class="flex justify-start w-52 h-20 bg-white rounded-lg shadow-lg px-2 items-center border-l-2 border-cyan-400 space-x-5">
        <img class="w-auto h-12" src="/img/suit.png" alt="Gown Image">
        <h2 class="font-amaticRegular text-4xl font-bold mb-0"> <span class = "text-sm antialiased text-gray-600">suits</span></h2>
    </div>

  </div>


  <div v-if="displayAttire === 'arch-outfit'"  class="relative shadow-md sm:rounded-xl w-[1170px] h-[200] ml-5 mt-2 font-amaticBold mb-10">
    <div class="overflow-x-auto">
        <table class="w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400 mb-4 max-h-30">
            <thead class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
                <tr>
                    <th scope="col" class="px-2 py-3">#</th>
                    <th scope="col" class="px-2 py-3">Type</th>
                    <th scope="col" class="px-2 py-3">Outfit Name</th>
                    <th scope="col" class="px-2 py-3">Price</th>
                    <th scope="col" class="px-2 py-3">Place of Creation</th>
                    <th scope="col" class="px-2 py-3">Owner</th>
                    <th scope="col" class="px-2 py-3">Action</th>
                </tr>
            </thead>
            <tbody>
                <tr
                    v-for="(outfit, index) in paginatedAttire"
                    :key="outfit.no"
                    class="border-b dark:border-gray-700 odd:bg-white odd:dark:bg-gray-900 even:bg-gray-50 even:dark:bg-gray-800">
                    <th scope="row" class="px-2 py-3 font-medium text-gray-900 whitespace-nowrap dark:text-white">{{ outfit.no }}</th>
                    <td class="px-1 py-3 hidden sm:table-cell">{{ outfit.type }}</td>
                    <td class="px-1 py-3 hidden sm:table-cell">{{ outfit.name }}</td>
                    <td class="px-1 py-3 hidden sm:table-cell">{{ outfit.price }}</td>
                    <td class="px-1 py-3 hidden sm:table-cell">{{ outfit.creationAddress }}</td>
                    <td class="px-1 py-3 hidden sm:table-cell">{{ outfit.owner }}</td>
                    <td class="px-1 py-3 hidden sm:table-cell">
                        <button
                            class="h-8 w-12 bg-blue-900 font-amaticBold font-medium text-sm rounded-md text-white hover:bg-blue-600" @click="editAttireBtn(index)">
                            Edit
                        </button>
                    </td>
                </tr>
            </tbody>
        </table>

        <!-- Pagination Controls -->
        <div class="flex justify-center space-x-2 mt-4 mb-6">
            <button @click="prevAttirePage" :disabled="currentAttirePage === 1" class="px-3 py-1 bg-blue-900 text-white rounded-md hover:bg-blue-600 disabled:opacity-50 text-md">Previous</button>
            <button v-for="page in totalAttirePages" :key="page" @click="changeAttirePage(page)" :class="{'bg-blue-900': currentAttirePage === page, 'bg-gray-300': currentAttirePage !== page}" class="px-3 py-1 text-white rounded-md hover:bg-blue-600 text-xs">
                {{ page }}
            </button>
            <button @click="nextAttirePage" :disabled="currentAttirePage === totalAttirePages" class="px-3 py-1 bg-blue-900 text-white rounded-md hover:bg-blue-600 disabled:opacity-50 text-xs">Next</button>
        </div>
    </div>
</div>




  </div>







</div>

  </template>
  
  <script>
export default {
  data() {
    return {
      showTable: 'gowns',
      displayAttire: 'arch-outfit',
      selectedOption: 'booked-outfit',

      displayBookedOutfits: true, 
      displayArchivedOutfits: false,
    

      attire: [
    { no: 1, type: 'gown', name: 'Royal Blue Evening Gown', price: '₱2,000', bookedBy: 'Alice Johnson', contact: '0917-123-4567', pickupDate: '2024-10-22', returnDate: '2024-10-30', status: 'Booked', additionalCharges: '', description: 'An elegant evening gown in royal blue, perfect for formal events.', creationAddress: '123 Glamour Ave, Style City', owner: 'Red Carpet' },
    { no: 2, type: 'gown', name: 'Vintage Lace Gown', price: '₱3,000', bookedBy: 'Maria Reyes', contact: '0918-234-5678', pickupDate: '2024-11-01', returnDate: '2024-11-05', status: 'Booked', additionalCharges: '', description: 'A beautiful vintage lace gown, ideal for classic occasions.', creationAddress: '456 Elegant St, Fashion Town', owner: 'Red Carpet' },
    { no: 3, type: 'gown', name: 'Bohemian Dream Gown', price: '₱1,500', bookedBy: 'Sarah Lim', contact: '0919-345-6789', pickupDate: '2024-11-10', returnDate: '2024-11-15', status: 'Available', additionalCharges: '', description: 'A free-spirited gown with a bohemian style, perfect for outdoor events.', creationAddress: '789 Indie Rd, Boho Village', owner: 'Red Carpet' },
    { no: 4, type: 'gown', name: 'Simple Satin Gown', price: '₱1,200', bookedBy: 'Jessica Tan', contact: '0920-456-7890', pickupDate: '2024-11-20', returnDate: '2024-11-25', status: 'Available', additionalCharges: '', description: 'A classic satin gown with a simple yet elegant design.', creationAddress: '707 Simple Rd, Minimal Town', owner: 'Red Carpet' },
    { no: 5, type: 'gown', name: 'Romantic Ball Gown', price: '₱1,800', bookedBy: 'Emily Davis', contact: '0921-567-8901', pickupDate: '2024-12-01', returnDate: '2024-12-05', status: 'Booked', additionalCharges: '', description: 'A romantic ball gown perfect for grand events.', creationAddress: '123 Romantic Ave, Fairytale City', owner: 'Red Carpet' },
    { no: 6, type: 'tuxedo', name: 'Classic Black Tuxedo', price: '₱2,800', bookedBy: 'John Doe', contact: '0923-123-4567', pickupDate: '2024-10-28', returnDate: '2024-11-02', status: 'Booked', additionalCharges: '', description: 'A timeless black tuxedo for formal occasions.', creationAddress: '101 Formal Blvd, Classy City', owner: 'Red Carpet' },
    { no: 7, type: 'tuxedo', name: 'Velvet Tuxedo', price: '₱4,500', bookedBy: 'Michael Lee', contact: '0924-234-5678', pickupDate: '2024-11-05', returnDate: '2024-11-10', status: 'Available', additionalCharges: '', description: 'A luxurious velvet tuxedo for a unique look.', creationAddress: '606 Luxe St, Prestige Place', owner: 'Red Carpet' },
    { no: 8, type: 'tuxedo', name: 'Midnight Blue Tuxedo', price: '₱3,200', bookedBy: 'Daniel Kim', contact: '0925-345-6789', pickupDate: '2024-11-12', returnDate: '2024-11-17', status: 'Booked', additionalCharges: '', description: 'A stunning midnight blue tuxedo for modern grooms.', creationAddress: '202 Elegant Ln, Chic Town', owner: 'Red Carpet' },
    { no: 9, type: 'tuxedo', name: 'White Dinner Jacket', price: '₱2,500', bookedBy: 'Chris Brown', contact: '0926-456-7890', pickupDate: '2024-11-20', returnDate: '2024-11-25', status: 'Available', additionalCharges: '', description: 'A sharp white dinner jacket ideal for formal dinners.', creationAddress: '404 Chic Ave, Elite District', owner: 'Red Carpet' },
    { no: 10, type: 'tuxedo', name: 'Black Shawl Lapel Tuxedo', price: '₱3,000', bookedBy: 'James Wilson', contact: '0927-567-8901', pickupDate: '2024-11-28', returnDate: '2024-12-03', status: 'Booked', additionalCharges: '', description: 'An elegant black tuxedo with a shawl lapel.', creationAddress: '505 Stylish Rd, Trendy City', owner: 'Red Carpet' },
    { no: 11, type: 'tuxedo', name: 'Patterned Tuxedo', price: '₱3,500', bookedBy: 'Robert White', contact: '0928-678-9012', pickupDate: '2024-12-05', returnDate: '2024-12-10', status: 'Available', additionalCharges: '', description: 'A stylish patterned tuxedo for those who want to stand out.', creationAddress: '808 Style St, Trendy City', owner: 'Red Carpet' },
    { no: 12, type: 'tuxedo', name: 'Burgundy Tuxedo', price: '₱3,300', bookedBy: 'David Green', contact: '0929-789-0123', pickupDate: '2024-12-12', returnDate: '2024-12-17', status: 'Booked', additionalCharges: '', description: 'A sophisticated burgundy tuxedo for formal events.', creationAddress: '909 Classy Ave, Elegant City', owner: 'Red Carpet' },
  ],




      paginatedGowns: [],
      currentGownsPage: 1,
      gownsPerPage: 5,

      paginatedTuxedos: [],
      currentTuxedosPage: 1,
      tuxedosPerPage: 5,

      currentAttirePage: 1,
      itemsPerPage: 7,
      
    };
  },
  computed: {
    totalGownsPages() {
      return Math.ceil(this.gowns.length / this.gownsPerPage);
    },
    gowns() {
      return this.attire.filter(item => item.type === 'gown'); // Fixed
    },
    totalTuxedosPages() {
      return Math.ceil(this.tuxedos.length / this.tuxedosPerPage);
    },
    tuxedos() {
      return this.attire.filter(item => item.type === 'tuxedo');
    },

    paginatedAttire() {
      const start = (this.currentAttirePage - 1) * this.itemsPerPage;
      return this.attire.slice(start, start + this.itemsPerPage);
    },
    totalAttirePages() {
      return Math.ceil(this.attire.length / this.itemsPerPage);
    },
  


    
  },
  methods: {
    paginateGowns() {
      const start = (this.currentGownsPage - 1) * this.gownsPerPage;
      this.paginatedGowns = this.gowns.slice(start, start + this.gownsPerPage);
    },
    changeGownsPage(page) {
      this.currentGownsPage = page;
      this.paginateGowns();
    },
    prevGownsPage() {
      if (this.currentGownsPage > 1) {
        this.currentGownsPage--;
        this.paginateGowns();
      }
    },
    nextGownsPage() {
      if (this.currentGownsPage < this.totalGownsPages) {
        this.currentGownsPage++;
        this.paginateGowns();
      }
    },
    editGownBtn(index) {
      console.log("Edit gown:", this.paginatedGowns[index]);
    },



    paginateTuxedos() {
      const start = (this.currentTuxedosPage - 1) * this.tuxedosPerPage;
      this.paginatedTuxedos = this.tuxedos.slice(start, start + this.tuxedosPerPage);
    },
    changeTuxedosPage(page) {
      this.currentTuxedosPage = page;
      this.paginateTuxedos();
    },
    prevTuxedosPage() {
      if (this.currentTuxedosPage > 1) {
        this.currentTuxedosPage--;
        this.paginateTuxedos();
      }
    },
    nextTuxedosPage() {
      if (this.currentTuxedosPage < this.totalTuxedosPages) {
        this.currentTuxedosPage++;
        this.paginateTuxedos();
      }
    },
    editTuxedoBtn(index) {
      console.log("Edit tuxedo:", this.paginatedTuxedos[index]);
    },



    prevAttirePage() {
      if (this.currentAttirePage > 1) {
        this.currentAttirePage--;
      }
    },
    nextAttirePage() {
      if (this.currentAttirePage < this.totalAttirePages) {
        this.currentAttirePage++;
      }
    },
    changeAttirePage(page) {
      this.currentAttirePage = page;
    },



    totalBookedGowns() {
      const bookedGowns = this.gowns.filter(gown => gown.status === 'Booked');
      return bookedGowns.length;
    },
    
    totalBookedTuxedos() {
      const bookedTuxedos = this.tuxedos.filter(tuxedo => tuxedo.status === 'Booked');
      return bookedTuxedos.length;
    },




    setOutfitDisplay() {
        this.displayBookedOutfits = false;
        this.displayArchivedOutfits = false;

        if (this.selectedOption === 'booked-outfit') {
          this.displayBookedOutfits = true;
        } else if (this.selectedOption === 'outfits-arch') {
          this.displayArchivedOutfits = true;
        }
      }



  },
  mounted() {
    this.paginateGowns();
    this.paginateTuxedos();

  },
   created() {
    // Fetch or initialize your attire data here
    this.attire = [
    { no: 1, type: 'gown', name: 'Royal Blue Evening Gown', price: '₱2,000', bookedBy: 'Alice Johnson', contact: '0917-123-4567', pickupDate: '2024-10-22', returnDate: '2024-10-30', status: 'Booked', additionalCharges: '', description: 'An elegant evening gown in royal blue, perfect for formal events.', creationAddress: '123 Glamour Ave, Style City', owner: 'Red Carpet' },
    { no: 2, type: 'gown', name: 'Vintage Lace Gown', price: '₱3,000', bookedBy: 'Maria Reyes', contact: '0918-234-5678', pickupDate: '2024-11-01', returnDate: '2024-11-05', status: 'Booked', additionalCharges: '', description: 'A beautiful vintage lace gown, ideal for classic occasions.', creationAddress: '456 Elegant St, Fashion Town', owner: 'Red Carpet' },
    { no: 3, type: 'gown', name: 'Bohemian Dream Gown', price: '₱1,500', bookedBy: 'Sarah Lim', contact: '0919-345-6789', pickupDate: '2024-11-10', returnDate: '2024-11-15', status: 'Available', additionalCharges: '', description: 'A free-spirited gown with a bohemian style, perfect for outdoor events.', creationAddress: '789 Indie Rd, Boho Village', owner: 'Red Carpet' },
    { no: 4, type: 'gown', name: 'Simple Satin Gown', price: '₱1,200', bookedBy: 'Jessica Tan', contact: '0920-456-7890', pickupDate: '2024-11-20', returnDate: '2024-11-25', status: 'Available', additionalCharges: '', description: 'A classic satin gown with a simple yet elegant design.', creationAddress: '707 Simple Rd, Minimal Town', owner: 'Red Carpet' },
    { no: 5, type: 'gown', name: 'Romantic Ball Gown', price: '₱1,800', bookedBy: 'Emily Davis', contact: '0921-567-8901', pickupDate: '2024-12-01', returnDate: '2024-12-05', status: 'Booked', additionalCharges: '', description: 'A romantic ball gown perfect for grand events.', creationAddress: '123 Romantic Ave, Fairytale City', owner: 'Red Carpet' },
    { no: 6, type: 'tuxedo', name: 'Classic Black Tuxedo', price: '₱2,800', bookedBy: 'John Doe', contact: '0923-123-4567', pickupDate: '2024-10-28', returnDate: '2024-11-02', status: 'Booked', additionalCharges: '', description: 'A timeless black tuxedo for formal occasions.', creationAddress: '101 Formal Blvd, Classy City', owner: 'Red Carpet' },
    { no: 7, type: 'tuxedo', name: 'Velvet Tuxedo', price: '₱4,500', bookedBy: 'Michael Lee', contact: '0924-234-5678', pickupDate: '2024-11-05', returnDate: '2024-11-10', status: 'Available', additionalCharges: '', description: 'A luxurious velvet tuxedo for a unique look.', creationAddress: '606 Luxe St, Prestige Place', owner: 'Red Carpet' },
    { no: 8, type: 'tuxedo', name: 'Midnight Blue Tuxedo', price: '₱3,200', bookedBy: 'Daniel Kim', contact: '0925-345-6789', pickupDate: '2024-11-12', returnDate: '2024-11-17', status: 'Booked', additionalCharges: '', description: 'A stunning midnight blue tuxedo for modern grooms.', creationAddress: '202 Elegant Ln, Chic Town', owner: 'Red Carpet' },
    { no: 9, type: 'tuxedo', name: 'White Dinner Jacket', price: '₱2,500', bookedBy: 'Chris Brown', contact: '0926-456-7890', pickupDate: '2024-11-20', returnDate: '2024-11-25', status: 'Available', additionalCharges: '', description: 'A sharp white dinner jacket ideal for formal dinners.', creationAddress: '404 Chic Ave, Elite District', owner: 'Red Carpet' },
    { no: 10, type: 'tuxedo', name: 'Black Shawl Lapel Tuxedo', price: '₱3,000', bookedBy: 'James Wilson', contact: '0927-567-8901', pickupDate: '2024-11-28', returnDate: '2024-12-03', status: 'Booked', additionalCharges: '', description: 'An elegant black tuxedo with a shawl lapel.', creationAddress: '505 Stylish Rd, Trendy City', owner: 'Red Carpet' },
    { no: 11, type: 'tuxedo', name: 'Patterned Tuxedo', price: '₱3,500', bookedBy: 'Robert White', contact: '0928-678-9012', pickupDate: '2024-12-05', returnDate: '2024-12-10', status: 'Available', additionalCharges: '', description: 'A stylish patterned tuxedo for those who want to stand out.', creationAddress: '808 Style St, Trendy City', owner: 'Red Carpet' },
    { no: 12, type: 'tuxedo', name: 'Burgundy Tuxedo', price: '₱3,300', bookedBy: 'David Green', contact: '0929-789-0123', pickupDate: '2024-12-12', returnDate: '2024-12-17', status: 'Booked', additionalCharges: '', description: 'A sophisticated burgundy tuxedo for formal events.', creationAddress: '909 Classy Ave, Elegant City', owner: 'Red Carpet' },

     
    ];
  },
}
</script>
  
  <style scoped>
  /* Add component-specific styles here */
  </style>