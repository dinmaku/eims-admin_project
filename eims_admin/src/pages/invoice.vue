<template>
    <div class = "w-full h-full bg-white overflow-x-hidden pb-20">
        <div class = "flex items-center m-5">
            <img class = "w-32" src="/img/logo.png" alt="">
            <div class = "inline m-2">
                  <h1 class ="text-3xl text-left font-semibold font-quicksand">Red Carpet</h1>
                  <p class = "text-md text-gray-600 font-medium font-raleway">Events and Wedding Services</p>
            </div>
        </div>

      <div class = "flex">
          <h1 class = "mt-2 ml-20 text-4xl font-raleway">Invoice</h1>
      </div>
      <div class = "flex mt-5 ml-20 space-x-20">
                <p class = "text-md font-amaticRegular text-gray-600">Invoice #:
                <span class = "text-black font-semibold">001</span></p>

                <p class = "text-md font-amaticRegular text-gray-600">Date:
                <span class = "text-black font-semibold">10/22/2024</span></p>

                <p class = "text-md font-amaticRegular text-gray-600">Invoice Type:
                <span class = "text-black font-semibold">Event</span></p>

                <p class = "text-md font-amaticRegular text-gray-600">Service:
                <span class = "text-black font-semibold">Wedding</span></p>

                <p class = "text-md font-amaticRegular text-gray-600">Name:
                <span class = "text-black font-semibold">Nido & Lactum Wedding</span></p>
        </div>

        <div class = "flex mt-10 ml-20 space-x-40">
            <div class = "flex flex-col text-left space-y-5">
                <p class = "text-lg font-amaticRegular text-blue-700">BILL FROM:</p>
                <p class = "text-xl font-amaticRegular font-semibold text-black">Red Carpet</p>
                <p class = "text-sm font-amaticBold text-gray-700">23B San Miguel Street, Iligan City, Lanao del Norte</p>
                <p class = "text-sm font-amaticRegular text-gray-700">+63 912 345 6789</p>
                <p class = "text-sm font-amaticRegular text-gray-700">redcarpet.weddingservices@gmail.com</p>
            </div>
            
            <div class = "flex flex-col text-left space-y-5">
                <p class = "text-lg font-amaticRegular text-green-500">BILL TO:</p>
                <p class = "text-xl font-amaticRegular font-semibold text-black">Nido Nikovado</p>
                <p class = "text-sm font-amaticBold text-gray-700">Del Carmen Ave, Iligan City, Lanao del Norte</p>
                <p class = "text-sm font-amaticRegular text-gray-700">+63 901 234 5678</p>
                <p class = "text-sm font-amaticRegular text-gray-700">jack.dawson@gmail.com</p> 
            </div>
        </div>

        <div class = "flex mt-12 ml-20 space-x-10">
            <p class ="text-md text-gray-700">Capacity: <span class="font-semibold">150 to 200 / attendees</span></p>
            <p class ="text-md text-gray-700">Total attendees: <span class="font-semibold">179 person</span></p>
        </div>


        <div class="flex justify-start ml-32 mt-14">
    <h1 class="font-bold font-raleway text-blue-700 text-center">Venue</h1>
</div>
<div class="flex justify-center mt-5">
    <div class="bg-gray-100 p-5 rounded-lg shadow-md">
        <table class="min-w-[900px] border-collapse ">
            <thead>
                <tr>
                    <th class="px-6 py-3 text-left text-xs font-medium text-gray-800 uppercase tracking-w-normal border-b  border-blue-500">#</th>
                    <th class="px-6 py-3 text-left text-xs font-medium text-gray-800 uppercase tracking-w-normal border-b  border-blue-500">Venue</th>
                    <th class="px-6 py-3 text-left text-xs font-medium text-gray-800 uppercase tracking-w-normal border-b  border-blue-500">Price</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="venue in venues" :key="venue.no">
                    <td class="px-6 py-4 text-left text-sm text-gray-800">{{ venue.no }}</td>
                    <td class="px-6 py-4 text-left text-sm text-gray-800">{{ venue.venueName }}</td>
                    <td class="px-6 py-4 text-left text-sm text-gray-800">{{ formatPrice(venue.price) }}</td>
                </tr>
            </tbody>
        </table>
    </div>
</div>


<div class="flex justify-start ml-32 mt-14">
    <h1 class="font-bold font-raleway text-blue-700 text-center">Package Deal</h1>
</div>
<div class="flex justify-center mt-5">
    <div class="bg-gray-100 p-5 rounded-lg shadow-md">
        <table class="min-w-[900px] border-collapse ">
            <thead>
                <tr>
                    <th class="px-6 py-3 text-left text-xs font-medium text-gray-800 uppercase tracking-w-normal border-b  border-blue-500">#</th>
                    <th class="px-6 py-3 text-left text-xs font-medium text-gray-800 uppercase tracking-w-normal border-b  border-blue-500">Package</th>
                    <th class="px-6 py-3 text-left text-xs font-medium text-gray-800 uppercase tracking-w-normal border-b  border-blue-500">Price</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="pkg in packageDeal" :key="pkg.no">
                    <td class="px-6 py-4 text-left text-sm text-gray-800">{{ pkg.no }}</td>
                    <td class="px-6 py-4 text-left text-sm text-gray-800">{{ pkg.packageName }}</td>
                    <td class="px-6 py-4 text-left text-sm text-gray-800">{{ formatPrice(pkg.price) }}</td>
                </tr>
            </tbody>
        </table>
    </div>
</div>

<div class="flex justify-start ml-32 mt-14">
    <h1 class="font-bold font-raleway text-blue-700 text-center">Vendor</h1>
</div>
<div class="flex justify-center mt-5">
    <div class="bg-gray-100 p-5 rounded-lg shadow-md">
        <table class="min-w-[900px] border-collapse ">
            <thead>
                <tr>
                    <th class="px-6 py-3 text-left text-xs font-medium text-gray-800 uppercase tracking-w-normal border-b  border-blue-500">#</th>
                    <th class="px-6 py-3 text-left text-xs font-medium text-gray-800 uppercase tracking-w-normal border-b  border-blue-500">Vendor</th>
                    <th class="px-6 py-3 text-left text-xs font-medium text-gray-800 uppercase tracking-w-normal border-b  border-blue-500">Name</th>
                    <th class="px-6 py-3 text-left text-xs font-medium text-gray-800 uppercase tracking-w-normal border-b  border-blue-500">Price</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="vendor in vendors" :key="vendor.no">
                    <td class="px-6 py-4 text-left text-sm text-gray-800">{{ vendor.no }}</td>
                    <td class="px-6 py-4 text-left text-sm text-gray-800">{{ vendor.type }}</td>
                    <td class="px-6 py-4 text-left text-sm text-gray-800">{{ vendor.name }}</td>
                    <td class="px-6 py-4 text-left text-sm text-gray-800">{{ formatPrice(vendor.price) }}</td>
                </tr>
            </tbody>
        </table>
    </div>
</div>

<div class="flex justify-start ml-32 mt-14">
    <h1 class="font-bold font-raleway text-blue-700 text-center">Attire Details</h1>
</div>
        <div class="flex justify-center mt-5">
            <div class="bg-gray-100 p-5 rounded-lg shadow-md">
                <table class="min-w-[900px] border-collapse ">
                    <thead>
                        <tr>
                            <th class="px-6 py-3 text-left text-xs font-medium text-gray-800 uppercase tracking-w-normal border-b  border-blue-500">#</th>
                            <th class="px-6 py-3 text-left text-xs font-medium text-gray-800 uppercase tracking-w-normal border-b  border-blue-500">Outfit</th>
                            <th class="px-6 py-3 text-left text-xs font-medium text-gray-800 uppercase tracking-w-normal border-b  border-blue-500">Name</th>
                            <th class="px-6 py-3 text-left text-xs font-medium text-gray-800 uppercase tracking-w-normal border-b  border-blue-500">Price</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="attire in attires" :key="attire.no">
                            <td class="px-6 py-4 text-left text-sm text-gray-800">{{ attire.no }}</td>
                            <td class="px-6 py-4 text-left text-sm text-gray-800">{{ attire.type }}</td>
                            <td class="px-6 py-4 text-left text-sm text-gray-800">{{ attire.name }}</td>
                            <td class="px-6 py-4 text-left text-sm text-gray-800">{{ formatPrice(attire.price) }}</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>

          <div class = "flex justify-end mx-32 my-12">
                <div class = "w-64 h-66 px-7 py-7 bg-gray-100 shadow-lg rounded-lg">
                  <div class = "flex flex-col text-left">
                     <h1 class = "font-semibold ">Subtotal</h1>
                     <p class = "mt-4 text-gray-700">Additional Charges: <span class ="font-semibold">₱ 0</span></p>
                     <p class = "mt-2 text-gray-700">Discount: <span class ="font-semibold">₱ 0</span></p>
                     <p class = "mt-2 text-gray-700">Down Payment: <span class ="font-semibold">{{ formatPrice(downPayment()) }}</span></p>
                     <p class = "mt-7 text-gray-700">Balance: <span class ="font-semibold">₱ 320,000</span></p>
                     <p class = "mt-1 text-gray-700">Total Charges: <span class ="font-semibold">{{ formatPrice(totalPrice()) }}</span></p>
                    
                     <button @click="showPaymentModal" class = "mt-4 p-2 h-10 bg-gray-800 text-gray-100 transition-transform duration-300 transform hover:scale-105">
                        Pay now
                     </button>
        
                     
                  </div>
 
                </div>
          </div>


<form v-if="paymentForm" class = "flex justify-end items-center fixed inset-0 bg-gray-800 bg-opacity-60">
  <div class = "bg-white w-[500px] h-full p-5 rounded-lg shadow-lg  overflow-y-hidden mr-2">
        <div class = "flex justify-between items-center m-3">
              <h1 class = "mt-2 font-semibold text-xl font-raleway text-gray-800">Payment Details</h1>
               <button class="mt-2 bg-gray-100 font-bold text-gray-500 px-3 py-1 rounded-full transform-transition duration-300 transform hover:scale-105" @click="closePaymentForm">
                  X
                </button>
            </div>
        <div class = "flex m-2 mt-8 space-x-5">
            <img src="/img/payment.png" alt="payment" class = "h-12 ml-2 mt-3 rounded-full bg-gray-100">
             <div class = "flex flex-col"> 
            <label for="paymentInput" class = "font-semibold text-start text-lg font-raleway text-gray-600">Amount</label>
                <div class="relative">
            <span class="absolute left-2 top-1/2 font-bold transform -translate-y-1/2 text-gray-500">₱</span>
            <input type="text" id="paymentInput" class="pl-6 w-36 font-amaticBold font-semibold border-t-0 border-l-0 border-r-0 border-b border-b-gray-300 focus:border-b-blue-500 focus:outline-none" >
                 </div>
            </div>
            <select class = "mt-8 p-2 w-[260px] h-9 rounded-lg font-raleway font-semibold text-sm shadow-md border border-gray-500 focus:outline-none focus:border-blue-700">
                    <option value="" class = "text-gray-700" disabled selected>Select Payment Method</option>
                    <option value="cash">In Cash</option>
                    <option value="gcash">GCash</option>
                    <option value="bank">Bank Transfer</option>
                    <option value="payment-counter">Payment Counter</option>
              </select>
        </div>
        <div class = "flex ml-5">
            
        </div>
        <div class = "border border-gray-400 mt-5"></div>

        <div class = "flex flex-col ml-2">
           <h1 class = "flex mt-4 font-semibold font-raleway">Payment Transactions</h1>

           <p class="flex justify-between items-center mt-3 font-semibold text-gray-500 text-sm">
                Status 
                <span :class="statusClass" class="p-1 px-2 rounded-full text-white">
                    {{ statusText }}
                </span>
             </p>

             <p class="flex justify-between items-center mt-4 font-semibold text-gray-500 text-sm">
                Payment Date
                <span class="text-black">Oct 22 2024, 2:40 PM</span>
             </p>
             <p class="flex justify-between items-center mt-4 font-semibold text-gray-500 text-sm">
                Reference No.
                <span class="text-black"># 1244</span>
             </p>
             <p class="flex justify-between items-center mt-4 font-semibold text-gray-500 text-sm">
                Remaining Balance
                <span class="text-black">₱ 320,000</span>
             </p>
             <p class="flex justify-between items-center mt-4 font-semibold text-gray-500 text-sm">
                Total Amount to pay
                <span class="text-black">₱ 360,000</span>
             </p>
        </div>
        <div class = "border border-gray-400 mt-5"></div>
        <div class = "flex flex-col ml-3">
            <h1 class = "flex mt-4 font-semibold font-raleway">Payment History</h1>

            <div class="flex justify-center mt-3">
                <div class="bg-gray-100 p-5 rounded-lg shadow-md">
                <div class="max-h-80 overflow-y-auto"> 
                    <table class="min-w-[400px] border-collapse overflow-y-auto">
                    <thead>
                        <tr>
                        <th class="px-6 py-3 text-left text-xs font-medium text-gray-800 uppercase tracking-w-normal border-b border-blue-900">#</th>
                        <th class="px-6 py-3 text-left text-xs font-medium text-gray-800 uppercase tracking-w-normal border-b border-blue-900">Amount</th>
                        <th class="px-6 py-3 text-left text-xs font-medium text-gray-800 uppercase tracking-w-normal border-b border-blue-900">Date</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="payment in limitedPayments" :key="payment.no">
                        <td class="px-6 py-4 text-left text-xs text-gray-800">{{ payment.no }}</td>
                        <td class="px-6 py-4 text-left text-xs text-gray-800">{{ formatAmount(payment.amount) }}</td>
                        <td class="px-6 py-4 text-left text-xs text-gray-800">{{ payment.date }}</td>
                        </tr>
                    </tbody>
                    </table>
                </div>
                </div>
            </div>
        </div>

        <div class = "flex justify-end mr-8 mt-10 space-x-6">
            <button class="border-b border-gray-500 bg-transparent text-sm text-gray-800 font-semibold py-2 px-2 
            focus:outline-none hover:bg-gray-400 hover:text-gray-700 rounded-lg transform-transition duration-200 transform hover:scale-105" @click="closePaymentForm">
                Cancel Payment
            </button>
            <button class = "bg-gray-600 py-2 px-5 rounded-full font-semibold text-sm text-white  transform-transition duration-200 transform hover:scale-105 " @click="handlePayment">
             Pay Now
            </button>
        </div>

        <div v-if="successAlert" class="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50">
        <div class="flex items-center bg-white p-4 rounded shadow-md">
            <img src="/img/success.png" class = "h-8">
          <p class = "font-raleway font-semibold ml-2 ">Payment successful!</p>
        </div>
      </div>



       
        
  </div>
</form> 








</div>






</template>

<script>
export default {
    Name: 'Invoice',
    data() {
        return {
         selectedVenue: null,
         paymentForm: false,
         successAlert: false,
         statusText: 'unpaid',


       venues: [
              { no: 1, venueName: 'Grand Ballroom', price: 5000 },
         ],

       packageDeal: [
             {no: 1, packageName: 'Premium Package', price: 60000},
         ],

       vendors:  [
             { no: 1, type: 'Catering', name: 'Delightful Bites Catering', price: 70000  },
             { no: 2, type: 'Multimedia', name: 'Vivid Memories Media', price: 30000  },
             { no: 3, type: 'Hair and Makeup', name: 'Elegant Essence', price: 15000  },
             { no: 4, type: 'Host', name: 'Edward Backward', price: 10000  },
             { no: 5, type: 'Sound and Lighting', name: 'Jadiel Walton', price: 30000  },
             { no: 6, type: 'Entertainment', name: 'Jovit Baldemonyo', price: 40000  },
             { no: 7, type: 'Transportation', name: 'Limousine Service Co.', price: 40000  }, 
             { no: 7, type: 'Invitations and Stationery', name: 'Digital Invitations Co.', price: 25000  },  
             { no: 8, type: 'Favors and Gifts', name: 'Edible Favors Bakery.', price: 30000  },  

        ],

        attires: [
            { no: 1, type: 'Gown', name: 'Royal Blue Evening Gown', price: 2000 },
            { no: 2, type: 'Tuxedo', name: 'Midnight Blue Tuxedo', price: 3000 },

        ],

        payments: [
            {no: 1221, amount: 12000, date: 'Sept 25, 2024' },
            {no: 1285, amount: 10000, date: 'Sept 25, 2024' },
            {no: 1221, amount: 12000, date: 'Sept 25, 2024' },
            {no: 1221, amount: 12000, date: 'Sept 25, 2024' },
        ],



            
        }
    },

    computed: {
        statusClass() {
        return {
            'bg-green-400': this.statusText === 'paid',
            'bg-red-400': this.statusText === 'unpaid',
        };
     },

     limitedPayments() {
      return this.payments.slice(0, 2);
    },
  },

    methods: {
    formatPrice(price) {
      return `₱${price.toLocaleString()}`;
    },
    formatAmount(amount) {
      return `₱${amount.toLocaleString()}`;
    },
    totalPrice() {
      const venueTotal = this.venues.reduce((total, venue) => total + venue.price, 0);
      const packageTotal = this.packageDeal.reduce((total, pkg) => total + pkg.price, 0);
      const vendorTotal = this.vendors.reduce((total, vendor) => total + vendor.price, 0);
      const attireTotal = this.attires.reduce((total, attire) => total + attire.price, 0);

      return venueTotal + packageTotal + vendorTotal + attireTotal;
    },

    downPayment() {
      const totalPrice = this.totalPrice();
      const downPaymentPercentage = 0.2; 
      return totalPrice * downPaymentPercentage;
    },

    showPaymentModal() {
      this.paymentForm = true;
    },

    closePaymentForm()
    {
        this.paymentForm = false;
    },

    handlePayment() {
        if(this.successAlert) return;
      this.successAlert = true;
      setTimeout(() => {
        this.successAlert = false;
      }, 5000);
    },

  },

 

}

</script>

<style scoped>

</style>