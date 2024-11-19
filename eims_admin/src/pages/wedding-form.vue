<template>
  <!--Package Form-->
  <form v-if="showPackageForm">  
  <div class="flex justify-center items-center font-amaticBold text-gray-600">
  <p class="text-2xl font-semibold mb-9">Wedding Event Details
  </p>
</div>

<div class ="inline text-start">
<h1 class = "text-3xl font-semibold mt-5 font-amaticBold mx-2 text-gray-">Package Deal
  <span class = "text-base font-bold text-gray-600">(1 of 5 to complete the process)</span>
</h1>
<div class = "border border-gray-700 mt-5">
</div>

<!--Basic package-->
<div class = "flex">
  <div class="flex flex-col bg-[#f7c5f7] rounded-3xl m-10 h-[520]">
  <div class="px-6 py-8 sm:p-10 sm:pb-6">
    <div class="grid items-center justify-center w-full grid-cols-1 text-left">
      <div>
        <h2
          class="text-lg font-medium tracking-tighter text-gray-600 lg:text-3xl"
        >
          Basic 
        </h2>
        <p class="mt-2 text-sm text-gray-500 font-raleway">Essential for your wedding.</p>
      </div>
      <div class="mt-6">
        <p>
          <span class="text-5xl font-light tracking-tight text-black">
            35k
          </span>
          <span class="text-base font-medium text-gray-500">php only</span>
        </p>
      </div>

      <div class = "flex mt-4">
        <img src="/img/check-icon.png" alt="" class="w-5 flex h-5 mr-2">
        <span class="text-base font-semibold text-gray-800">Reception Venue</span>
      </div>
        <div class ="flex mt-1 ml-7">
          <span class="text-xs font-medium text-gray-800">Creative design of lively decors</span>
        </div>
        <div class = "flex mt-4">
        <img src="/img/check-icon.png" alt="" class="w-5 flex h-5 mr-2">
        <span class="text-base font-semibold text-gray-800">Stage Decor</span>
      </div>
        <div class ="flex mt-1 ml-7">
          <span class="text-xs font-medium text-gray-800">Beautiful Backdrop</span>
        </div>
        <div class = "flex mt-4">
        <img src="/img/check-icon.png" alt="" class="w-5 flex h-5 mr-2">
        <span class="text-base font-semibold text-gray-800">Entrance</span>
      </div>
      <div class = "flex mt-4">
        <img src="/img/check-icon.png" alt="" class="w-5 flex h-5 mr-2">
        <span class="text-base font-semibold text-gray-800">Boquet</span>
      </div>


    </div>
  </div>
  <div class="flex px-6 pb-8 sm:px-8 mt-5 ">
    <a
      aria-describedby="tier-company"
      class="flex items-center justify-center w-full px-6 py-2.5 text-center text-white duration-200 bg-black border-2 border-black rounded-full nline-flex hover:bg-transparent hover:border-black hover:text-black focus:outline-none focus-visible:outline-black text-sm focus-visible:ring-black"
      href="#"
       @click.prevent="selectPackage"
    >
     Select
    </a>
  </div>
</div>

<!--Premium package-->
<div class = "flex">
  <div class="flex flex-col bg-[#afe2f8] rounded-3xl m-10 h-[520px]">
  <div class="px-6 py-8 sm:p-10 sm:pb-6">
    <div class="grid items-center justify-center w-full grid-cols-1 text-left">
      <div>
        <h2
          class="text-lg font-medium tracking-tighter text-gray-600 lg:text-3xl"
        >
          Premium
        </h2>
        <p class="mt-2 text-sm text-gray-500 font-raleway ">Enhanced elegance and details..</p>
      </div>
      <div class="mt-6">
        <p>
          <span class="text-5xl font-light tracking-tight text-black">
            60k
          </span>
          <span class="text-base font-medium text-gray-500">php only</span>
        </p>
      </div>

      <div class = "flex mt-4">
        <img src="/img/check-icon.png" alt="" class="w-5 flex h-5 mr-2">
        <span class="text-base font-semibold text-gray-800">Everything in Basic</span>
      </div>
        <div class = "flex mt-4">
        <img src="/img/check-icon.png" alt="" class="w-5 flex h-5 mr-2">
        <span class="text-base font-semibold text-gray-800">Ceiling Works</span>
      </div>
        <div class ="flex mt-1 ml-7">
          <span class="text-xs font-medium text-gray-800">Stylish stands with flower</span>
        </div>
        <div class = "flex mt-4">
        <img src="/img/check-icon.png" alt="" class="w-5 flex h-5 mr-1">
        <span class="text-base font-semibold text-gray-800">Vanity Wall with couple's name</span>
      </div>
      <div class = "flex mt-4">
        <img src="/img/check-icon.png" alt="" class="w-5 flex h-5 mr-2">
        <span class="text-base font-semibold text-gray-800">Boquet</span>
      </div>
      <div class ="flex mt-1 ml-7">
          <span class="text-xs font-medium text-gray-800">Premium flowers</span>
        </div>


    </div>
  </div>
  <div class="flex px-6 pb-8 sm:px-8 mt-4">
    <a
      aria-describedby="tier-company"
      class="flex items-center justify-center w-full px-6 py-2.5 text-center text-white duration-200 bg-black border-2 border-black rounded-full nline-flex hover:bg-transparent hover:border-black hover:text-black focus:outline-none focus-visible:outline-black text-sm focus-visible:ring-black"
      href="#"
      @click.prevent="selectPackage"
    >
     Select
    </a>
  </div>
</div>
</div>


<!--VIP package-->
<div class = "flex">
  <div class="flex flex-col bg-[#f6f9a0] rounded-3xl m-10 h-[520px]">
  <div class="px-6 py-8 sm:p-10 sm:pb-6">
    <div class="grid items-center justify-center w-full grid-cols-1 text-left">
      <div>
        <h2
          class="text-lg font-medium tracking-tighter text-gray-600 lg:text-3xl"
        >
         VIP
        </h2>
        <p class="mt-2 text-sm text-gray-500 font-raleway">Ultimate experience and exclusivity.</p>
      </div>
      <div class="mt-6">
        <p>
          <span class="text-5xl font-light tracking-tight text-black">
            100k
          </span>
          <span class="text-base font-medium text-gray-500">php only</span>
        </p>
      </div>

      <div class = "flex mt-4">
        <img src="/img/check-icon.png" alt="" class="w-5 flex h-5 mr-2">
        <span class="text-base font-semibold text-gray-800">Everything in Premium</span>
      </div>
        <div class = "flex mt-4">
        <img src="/img/check-icon.png" alt="" class="w-5 flex h-5 mr-2">
        <span class="text-base font-semibold text-gray-800">Elegant Grand Entrance Arch</span>
      </div>
        <div class = "flex mt-4">
        <img src="/img/check-icon.png" alt="" class="w-5 flex h-5 mr-2">
        <span class="text-base font-semibold text-gray-800">Customized drapery and linens</span>
      </div>
      <div class = "flex mt-4">
        <img src="/img/check-icon.png" alt="" class="w-5 flex h-5 mr-2">
        <span class="text-base font-semibold text-gray-800">Themed table settings</span>
      </div>


    </div>
  </div>
  <div class="flex px-6 pb-8 sm:px-8 mt-8">
    <a
      aria-describedby="tier-company"
      class="flex items-center justify-center w-full px-6 py-2.5 text-center text-white duration-200 bg-black border-2 border-black rounded-full nline-flex hover:bg-transparent hover:border-black hover:text-black focus:outline-none focus-visible:outline-black text-sm focus-visible:ring-black"
      href="#"
       @click.prevent="selectPackage"
    >
     Select
    </a>
  </div>
</div>
</div>

</div>
</div>

</form>

<!--Vendor Details Form-->
<form v-if="showVendorDetailsForm" class="pb-[50px]">
 <div class = "flex m-2">
 <button class = "w-20 h-10 bg-gray-200 rounded shadow-md text-sm font-amaticBold font-semibold hover:bg-blue-400 transition-transform transform hover:scale-105"
 @click="backBtnVendor"
 >
  Back</button>
 </div>

     <div class ="inline text-start">
       <h1 class = "text-3xl font-semibold mt-10 font-amaticBold mx-2 text-gray-">Vendor Details
        <span class = "text-base font-bold text-gray-600">(2 of 5 to complete the process)</span>
       </h1>
      <div class = "border border-gray-700 mt-5">
   </div>
  </div>

 

  <div class="flex m-5">
    <label for="vendor-name" class="block text-md font-semibold font-raleway text-gray-700 mt-2">
      Set Capacity:
    </label>
    <div class="flex grid-col ml-2">
      <select v-model="selectedQuantity" class="w-40 h-10 text-sm font-semibold">
        <option disabled value="">Select quantity</option>
        <option v-for="(item, index) in quantity" :key="index" :value="item.value" class="text-sm">
          {{ item.label }}
        </option>
      </select>
    </div>
  </div>

  <div class="flex mx-5">
    <div class="row text-start">
      <label for="catering-service" class="text-md font-bold">Catering Service. *</label>
      <p class="text-base font-semibold text-gray-600">
        Select and enjoy customized food and beverages for your event.
        <a href="" class="text-underline text-blue-500 hover:text-blue-700">View vendors!</a>
      </p>
      <select v-model="selectedCatering" id="catering-service" class="w-[400px] m-3 text-sm font-bold">
        <option disabled value="">Pick your catering</option>
        <option v-for="(vendor, index) in cateringOptions" :key="index" :value="vendor.value">
          {{ vendor.label }}
        </option>
      </select>
    </div>
  </div>

  <div class="flex mx-5 mt-5">
    <div class="row text-start">
      <label for="multimedia-service" class="text-md font-bold">
        Photographer and Videographer. *
      </label>
      <p class="text-base font-semibold text-gray-600">
        Captures the moments of the wedding day.
        <a href="" class="text-underline text-blue-500 hover:text-blue-700">View vendors!</a>
      </p>
      <select v-model="selectedMultimedia" id="multimedia-service" class="w-[400px] m-3 text-sm font-bold">
        <option disabled value="">Pick your multimedia</option>
        <option v-for="(vendor, index) in multimediaOptions" :key="index" :value="vendor.value">
          {{ vendor.label }}
        </option>
      </select>
    </div>
  </div>
  <div class="flex mx-5 mt-5">
    <div class="row text-start">
      <label for="glam-service" class="text-md font-bold">
        Hair and Makeup Artists. *
      </label>
      <p class="text-base font-semibold text-gray-600">
        Provides luxurious and sophisticated styling to enhance the visual appeal.
        <a href="" class="text-underline text-blue-500 hover:text-blue-700">View vendors!</a>
      </p>
      <select v-model="selectedGlam" id="glam-service" class="w-[400px] m-3 text-sm font-bold">
        <option disabled value="">Pick your Glams</option>
        <option v-for="(artist, index) in glamOptions" :key="index" :value="artist.value">
          {{ artist.label }}
        </option>
      </select>
    </div>
  </div>

  <div class="flex mx-5 mt-5">
    <div class="row text-start">
      <label for="host-service" class="text-md font-bold">
        Host. *
      </label>
      <p class="text-base font-semibold text-gray-600">
        Guides and entertains guests, facilitating a smooth and engaging flow of the event.
        <a href="" class="text-underline text-blue-500 hover:text-blue-700">View vendors!</a>
      </p>
      <select v-model="selectedHost" id="host-service" class="w-[400px] m-3 text-sm font-bold">
        <option disabled value="">Pick your Host</option>
        <option v-for="(host, index) in hostOptions" :key="index" :value="host.value">
          {{ host.label }}
        </option>
      </select>
    </div>
  </div>

  <div>
    <!-- Lighting and Sound -->
    <div class="flex mx-5 mt-5">
      <div class="row text-start">
        <label for="audio-visual-service" class="text-md font-bold">
          Lighting and Sound. *
        </label>
        <p class="text-base font-semibold text-gray-600">
          Ensures the venue has the appropriate lighting and sound equipment for the reception.
          <a href="" class="text-underline text-blue-500 hover:text-blue-700">View vendors!</a>
        </p>
        <select v-model="selectedAudioVisual" id="audio-visual-service" class="w-[400px] m-3 text-sm font-bold">
          <option disabled value="">Pick your audio-visual</option>
          <option v-for="(vendor, index) in audioVisualOptions" :key="index" :value="vendor.value">
            {{ vendor.label }}
          </option>
        </select>
      </div>
    </div>

    <!-- Music and Entertainment -->
    <div class="flex mx-5 mt-5">
      <div class="row text-start">
        <label for="music-entertainment-service" class="text-md font-bold">
          Music and Entertainment *
        </label>
        <p class="text-base font-semibold text-gray-600">
          Ensures an unforgettable experience with live music and performances.
          <a href="" class="text-underline text-blue-500 hover:text-blue-700">View vendors!</a>
        </p>
        <select v-model="selectedMusic" id="music-entertainment-service" class="w-[400px] m-3 text-sm font-bold">
          <option disabled value="">Pick your performers</option>
          <option v-for="(performer, index) in musicOptions" :key="index" :value="performer.value">
            {{ performer.label }}
          </option>
        </select>
      </div>
    </div>

    <!-- Transportation -->
    <div class="flex mx-5 mt-5">
      <div class="row text-start">
        <label for="transportation-service" class="text-md font-bold">
          Transportation. *
        </label>
        <p class="text-base font-semibold text-gray-600">
          Provides stylish and reliable transportation for the wedding party.
          <a href="" class="text-underline text-blue-500 hover:text-blue-700">View vendors!</a>
        </p>
        <select v-model="selectedTransportation" id="transportation-service" class="w-[400px] m-3 text-sm font-bold">
          <option disabled value="">Pick your car</option>
          <option v-for="(car, index) in transportationOptions" :key="index" :value="car.value">
            {{ car.label }}
          </option>
        </select>
      </div>
    </div>

    <!-- Invitations and Stationery -->
    <div class="flex mx-5 mt-5">
      <div class="row text-start">
        <label for="invitation-service" class="text-md font-bold">
          Invitations and Stationery. *
        </label>
        <p class="text-base font-semibold text-gray-600">
          Designs beautiful invitations and keepsakes for your guests.
          <a href="" class="text-underline text-blue-500 hover:text-blue-700">View vendors!</a>
        </p>
        <select v-model="selectedInvitations" id="invitation-service" class="w-[400px] m-3 text-sm font-bold">
          <option disabled value="">Pick your invitation</option>
          <option v-for="(invitation, index) in invitationOptions" :key="index" :value="invitation.value">
            {{ invitation.label }}
          </option>
        </select>
      </div>
    </div>

    <!-- Favors and Gifts -->
    <div class="flex mx-5 mt-5">
      <div class="row text-start">
        <label for="favors-gifts-service" class="text-md font-bold">
          Favors and Gifts. *
        </label>
        <p class="text-base font-semibold text-gray-600">
          Provides unique keepsakes for your guests to remember the day.
          <a href="" class="text-underline text-blue-500 hover:text-blue-700">View vendors!</a>
        </p>
        <select v-model="selectedFavors" id="favors-gifts-service" class="w-[400px] m-3 text-sm font-bold">
          <option disabled value="">Pick your keepsakes</option>
          <option v-for="(favor, index) in favorsOptions" :key="index" :value="favor.value">
            {{ favor.label }}
          </option>
        </select>
      </div>
    </div>
  </div>

  <div class="flex justify-center">
       <button class = "w-20 h-10 bg-blue-500 rounded-lg shadow-md text-md font-semibold text-gray-100 hover:bg-blue-600 transition-transform transform hover:scale-105"
       @click = "nextBtnVendorForm">
        Next</button>
  </div>

</form>



<!--Gown and Tuxedo Selection Form-->
<form v-if="showGownSelectionForm">
  <div class = "flex m-2 space-x-[900px]">
 <button class = "w-20 h-10 bg-gray-200 rounded shadow-md text-sm font-amaticBold font-semibold hover:bg-blue-400 transition-transform transform hover:scale-105"
 @click="backBtnGown"
 >
  Back</button>
  <button class = "flex justify-center items-center w-40 h-10 bg-blue-300 rounded shadow-md text-sm font-amaticBold font-bold hover:bg-blue-400 transition-transform transform hover:scale-105"
 @click="ProceedToDetails"
 >
  Proceed</button>
 </div>

    <div v-if ="showGownCatalog">
     <div class ="inline text-start">
       <h1 class = "text-3xl font-semibold mt-10 font-amaticBold mx-2 text-gray-">Outfit Selection
        <span class = "text-base font-bold text-gray-600">(3 of 4 to complete the process)</span>
       </h1>
      <div class = "border border-gray-700 mt-5">
   </div>
  </div>
  <div class = "flex m-3 ml-5">
       <select v-model="selectedOption" @change="selectCatalog" class = "w-[105px] h-9 text-sm font-semibold">
       <option value="gown1">Gown</option>
       <option value="tuxedo1">Tuxedo</option>
      </select>
    </div>
  <div class = "grid grid-cols-4 gap-4 mt-8">
    <div
       v-for="(gown, gownIndex) in gowns"
      :key="index"
      class="row cursor-pointer w-[270px] h-[360px] bg-[#E6E6FA] border border-black rounded-xl p-1 shadow transition-all duration-300"
      :class="[
        'border', 
        activeGownIndex === gownIndex ? 'border-blue-500 ring-2 ring-blue-500' : 'border-black'
      ]">

        <div class = "flex h-44 bg-gray-100 justify-center items-center">
           <img :src="gown.img" alt="gown" class = "w-28 h-34">
        </div>
        <div class = "m-2">
              <h1 class = "font-bold font-raleway text-lg "> {{ gown.name }}</h1>
              <p class = "text-md text-gray-700 font-medium"> {{ gown.description }}</p>
        </div>
              <div class = "flex m-4">
                    <h1 class = "font-bold font-amaticBold text-lg text-start">{{ gown.price }}
                      <span class = "text-base text-sm text-gray-600">/per day</span>
                    </h1>
                    <button class = "w-16 h-8 ml-12 bg-blue-500 rounded-md shadow-md text-white font-semibold hover:bg-blue-600 transition-transform transform hover:scale-105 "
              @click.prevent="selectGownCard(gownIndex)"
              > Pick</button>
              </div>
     </div>
  </div>
  </div>

  <div v-if ="showTuxedoCatalog">
     <div class ="inline text-start">
       <h1 class = "text-3xl font-semibold mt-10 font-amaticBold mx-2 text-gray-">Outfit Selection
        <span class = "text-base font-bold text-gray-600">(3 of 3 to complete the process)</span>
       </h1>
      <div class = "border border-gray-700 mt-5">
   </div>
  </div>
  <div class = "flex m-3 ml-5">
       <select v-model="selectedOption" @change="selectCatalog" class = "w-[105px] h-9 text-sm font-semibold">
       <option value="gown1">Gown</option>
       <option value="tuxedo1">Tuxedo</option>
      </select>
    </div>
  <div class = "grid grid-cols-4 gap-4 mt-8">
    <div
       v-for="(tuxedo, tuxedoIndex) in tuxedos"
      :key="index"
      class="row cursor-pointer w-[270px] h-[360px] bg-[#E6E6FA] border border-black rounded-xl p-1 shadow transition-all duration-300"
      :class="[
        'border', 
        activeTuxedoIndex ===  tuxedoIndex ?  'border-blue-500 ring-2 ring-blue-500' : 'border-black'
      ]">
      
      <div class = "flex h-44 bg-gray-100 justify-center items-center">
           <img :src="tuxedo.img" alt="gown" class = "w-28 h-34">
        </div>
        <div class = "m-2">
              <h1 class = "font-bold font-raleway text-lg "> {{tuxedo.name }}</h1>
              <p class = "text-md text-gray-700 font-medium"> {{ tuxedo.description }}</p>
        </div>
              <div class = "flex m-4">
                    <h1 class = "font-bold font-amaticBold text-lg text-start">{{tuxedo.price }}
                      <span class = "text-base text-sm text-gray-600">/per day</span>
                    </h1>
                    <button class = "w-16 h-8 ml-12 bg-blue-500 rounded-md shadow-md text-white font-semibold hover:bg-blue-600 transition-transform transform hover:scale-105 "
              @click.prevent="selectTuxedoCard(tuxedoIndex)"
              > Pick</button>
              </div>
    </div>
  </div>
  </div>
</form>


<!--Review the Event Form-->
<div v-if="showCompleteEventProcess">
  <div class = "flex">
 <button class = "w-20 h-10 bg-gray-200 rounded shadow-md text-sm font-amaticBold font-semibold hover:bg-blue-400 transition-transform transform hover:scale-105"
 @click="backBtnReviewDetails"
 >
  Back</button>
 </div>

  <div class ="inline">
       <h1 class = "text-3xl font-semibold mt-10 font-amaticBold mx-2 text-gray-">Review your Event Details
        <span class = "text-base font-bold text-gray-600">(4 of 4 to complete the process)</span>
       </h1>
      <div class = "border border-gray-700 mt-5">
   </div>
  </div>
  
 <div class = "inline text-start m-6 items-center">
     <h1 class = "text-2xl font-bold text-[#2b9feb]">Package Deal</h1>
     <div class = "flex m-2">
        <div class = "row">
          <p class = "mt-3 text-md font-semibold text-gray-700">Type: 
            <span class ="ml-2 font-bold text-gray-900">Premium</span>
          </p>
          <p class = "text-md font-semibold text-gray-700">Price: 
            <span class ="ml-2 font-bold text-gray-900">60k</span>
          </p>
        </div>
     </div>
     <div class="flex items-center mt-6">
   <h1 class="text-md font-semibold font-amaticBold text-gray-900 ml-2">Expected invited guest:</h1>
    <p class="ml-2 text-md font-bold font-amaticBold text-gray-800">{{ getSelectedLabel(selectedQuantity, quantity) }} attendees.</p>
  </div>
     <div class = "border border-gray-500 mt-10"></div>
 </div>


 <div class="m-2">
  <h1 class="text-2xl text-start font-bold text-[#2b9feb]">Vendors Selected</h1>
  <div class="flex items-center mt-5">
    <div class ="row text-start">
   <p class="text-md font-semibold font-amaticBold text-gray-700">Catering Service:
    <span class="ml-2 text-md font-bold font-amaticBold text-gray-800">{{ getSelectedLabel(selectedCatering, cateringOptions) }}</span>
   </p>
   <p class="mt-2 text-md font-semibold font-amaticBold text-gray-700">Photographer and Videographer:
    <span class="ml-2 text-md font-bold font-amaticBold text-gray-800">{{ getSelectedLabel(selectedMultimedia, multimediaOptions) }}</span>
   </p>
   <p class="mt-2 text-md font-semibold font-amaticBold text-gray-700">Hair and Makeup Artist:
    <span class="ml-2 text-md font-bold font-amaticBold text-gray-800">{{ getSelectedLabel(selectedGlam, glamOptions) }}</span>
   </p>
   <p class="mt-2 text-md font-semibold font-amaticBold text-gray-700">Event Host:
    <span class="ml-2 text-md font-bold font-amaticBold text-gray-800">{{ getSelectedLabel(selectedHost, hostOptions) }}</span>
   </p>
   <p class="mt-2 text-md font-semibold font-amaticBold text-gray-700">Sound and Lighting:
    <span class="ml-2 text-md font-bold font-amaticBold text-gray-800">{{ getSelectedLabel(selectedAudioVisual, audioVisualOptions) }}</span>
   </p>
   <p class="mt-2 text-md font-semibold font-amaticBold text-gray-700">Music and Entertainment:
    <span class="ml-2 text-md font-bold font-amaticBold text-gray-800">{{ getSelectedLabel(selectedMusic, musicOptions) }}</span>
   </p>
   <p class="mt-2 text-md font-semibold font-amaticBold text-gray-700">Transportation:
    <span class="ml-2 text-md font-bold font-amaticBold text-gray-800">{{ getSelectedLabel(selectedTransportation, transportationOptions) }}</span>
   </p>
   <p class="mt-2 text-md font-semibold font-amaticBold text-gray-700">Invitations and Stationery:
    <span class="ml-2 text-md font-bold font-amaticBold text-gray-800">{{ getSelectedLabel(selectedInvitations, invitationOptions) }}</span>
   </p>
   <p class="mt-2 text-md font-semibold font-amaticBold text-gray-700">Favors and Gifts:
    <span class="ml-2 text-md font-bold font-amaticBold text-gray-800">{{ getSelectedLabel(selectedFavors, favorsOptions) }}</span>
   </p>
   
  </div>
   
  </div>
  <div class = "border border-gray-500 mt-10"></div>


</div>

<div class = "flex m-3 py-3">
  <h1 class ="text-2xl font-bold text-[#2b9feb]">Gown and Tuxedo</h1>
</div>

<div class="flex items-center m-2 mb-10">
  <img v-if = "activeGownIndex !== null" :src="gowns[activeGownIndex].img" alt="Gown Image" class="w-32 h-32 rounded-md mr-4">
  <div class="flex flex-col items-start">
    <p class="text-md font-semibold text-gray-700 mb-2">
      Selected Gown No: <span class="font-bold text-gray-900">{{ activeGownIndex !== null ? activeGownIndex : 'Not Selected' }}</span>
    </p>
    <p v-if="activeGownIndex !== null" class="text-md font-semibold text-gray-700">
      Name: <span class="font-bold text-gray-800">{{ gowns[activeGownIndex].name }}</span>
    </p>
    <p v-if="activeGownIndex !== null" class="text-md font-semibold text-gray-700 mt-2">
      Description: <span class="font-bold text-gray-800">{{ gowns[activeGownIndex].description }}</span>
    </p>
    <p v-if="activeGownIndex !== null" class="text-md font-semibold text-gray-700 mt-2">
      Price: <span class="font-bold text-gray-800">{{ gowns[activeGownIndex].price }}</span>
    </p>
    <p v-if="activeGownIndex === null" class="text-md font-semibold text-red-500 mt-2">
      * Please select a gown.
    </p>
  </div>
</div>

<div class="flex items-center m-2">
  <img v-if="activeTuxedoIndex !== null" :src="tuxedos[activeTuxedoIndex].img" alt="Tuxedo Image" class="w-32 h-32 rounded-md mr-4">
  
  <div class="flex flex-col items-start">
    <p class="text-md font-semibold text-gray-700 mb-2">
      Selected Tuxedo No: <span class="font-bold text-gray-900">{{ activeTuxedoIndex !== null ? activeTuxedoIndex : 'Not Selected' }}</span>
    </p>

   
    <p v-if="activeTuxedoIndex !== null" class="text-md font-semibold text-gray-700">
      Name: <span class="font-bold text-gray-800">{{ tuxedos[activeTuxedoIndex].name }}</span>
    </p>
    <p v-if="activeTuxedoIndex !== null" class="text-md font-semibold text-gray-700 mt-2">
      Description: <span class="font-bold text-gray-800">{{ tuxedos[activeTuxedoIndex].description }}</span>
    </p>
    <p v-if="activeTuxedoIndex !== null" class="text-md font-semibold text-gray-700 mt-2">
      Price: <span class="font-bold text-gray-800">{{ tuxedos[activeTuxedoIndex].price }}</span>
    </p>

    <p v-if="activeTuxedoIndex === null" class="text-md font-semibold text-red-500 mt-2">
      * Please select a tuxedo.
    </p>
  </div>
</div>

<div class = "border border-gray-500 mt-10"></div>

  <div class = "flex text-center m-3 py-3">
  <h1 class ="text-2xl font-bold text-[#2b9feb]">Set a Date and Time for your Event</h1>
</div>
   <div class = "row">
          <label for="" class = "flex items-center text-md text-gray-700 font-semibold ml-2">Date: 
            <input type="date" id="eventDate" name="eventDate" class="form-control ml-2 w-1/4 h-9" required>
          </label>
          <label for="" class = "flex items-center text-md text-gray-700 font-semibold ml-2 mt-5">Start Time: 
            <input type = "time" class = "h-9 ml-3">
          </label>
          <label for="" class = "flex items-center text-md text-gray-700 font-semibold ml-2 mt-5">End Time: 
            <input type = "time" class = "h-9 ml-3">
          </label>
   </div>



<router-link to="/manage-events">
 <div class = "flex justify-center mt-20 py-5">
 <button class = "w-20 h-10 bg-blue-500 rounded shadow-md text-sm font-amaticBold font-semibold hover:bg-blue-400 transition-transform
  transform hover:scale-105"
 @click="BtnEventCreation"
 >
  Create </button>
 </div>
</router-link>











</div>


</template>

<script>
export default {
  name: 'WeddingForm',
  data() {
    return {
      activeGownIndex: null,
      activeTuxedoIndex: null,

      selectedOption: 'gown1',
      showTuxedoCatalog: false,
      showGownCatalog: true,

       showPackageForm: true,
       showVendorDetailsForm: false,
       showGownSelectionForm: false,
       showCompleteEventProcess: false,


       quantity: [
        { label: 'less than 50', value: 'less than 50' },
        { label: '50 to 100', value: '50 to 100' },
        { label: '100 to 150', value: '100 to 150' },
        { label: '150 to 200', value: '150 to 200' },
        { label: 'more than 200', value: 'more than 200' },
      ],
      selectedQuantity: '',


      cateringOptions: [
        { label: 'Delightful Bites Catering', value: '1' },
        { label: 'Savory Spread Catering', value: '2' },
        { label: 'Elegant Eats Events', value: '3' },
      ],
      selectedCatering: '',

      
      multimediaOptions: [
        { label: 'Crystal Clear Imagery', value: '1' },
        { label: 'Vivid Memories Media', value: '2' },
        { label: 'Shutter & Frame Creations', value: '3' },
      ],
      selectedMultimedia: '',


      glamOptions: [
        { label: 'Glamour Heights', value: '1' },
        { label: 'Radiant Luxe Studio', value: '2' },
        { label: 'Elegant Essence', value: '3' },
      ],
      selectedGlam: '',

      
      hostOptions: [
        { label: 'Boy Semilia', value: '1' },
        { label: 'Edward Backward', value: '2' },
        { label: 'Ray Castillo', value: '3' },
      ],
      selectedHost: '',


      audioVisualOptions: [
        { label: 'Jadiel Walton', value: '1' },
        { label: 'Korbyn Norton', value: '2' },
        { label: 'Nico Shepherd', value: '3' },
      ],
      selectedAudioVisual: '',



      musicOptions: [
        { label: 'Jovit Baldemonyo', value: '1' },
        { label: 'November Revenue', value: '2' },
        { label: 'Lani Misaluy-a', value: '3' },
      ],
      selectedMusic: '',



      transportationOptions: [
        { label: 'Limousine Service Co.', value: '1' },
        { label: 'Vintage Car Rentals', value: '2' },
        { label: 'Kalesa Services', value: '3' },
      ],
      selectedTransportation: '',



      invitationOptions: [
        { label: 'Custom Invitations Studio', value: '1' },
        { label: 'Digital Invitations Co.', value: '2' },
        { label: 'Elegant Stationery Creations', value: '3' },
      ],
      selectedInvitations: '',



      favorsOptions: [
        { label: 'Personalized Keepsakes Co.', value: '1' },
        { label: 'Edible Favors Bakery', value: '2' },
        { label: 'Themed Gift Suppliers', value: '3' },
      ],
      selectedFavors: '',

      
       

       gowns: [
        {name: 'Royal Blue Evening Gown', description: ' Sequined blue gown with sweetheart neckline.', price: '₱2,000', img: '/img/img-gown/gown1.png'},
        {name: 'Vintage Lace Gown', description: ' Charming vintage gown with lace overlay.',price: '₱3,000', img: '/img/img-gown/gown2.png'},
        {name: 'Bohemian Dream Gown', description: ' Whimsical gown with flowing sleeves.', price: '₱1,500', img: '/img/img-gown/gown3.png'},
        {name: 'Simple Satin Gown', description: ' Elegant satin gown with timeless design', price: '₱1,200', img: '/img/img-gown/gown4.png'},
        {name: 'Romantic Ball Gown', description: ' Classic chiffon A-line gown with train.',price: '₱1,800', img: '/img/img-gown/gown5.png'},
        
       ],

       tuxedos: [
          {name: 'Classic Black Tuxedo', description: ' Timeless black tuxedo with satin lapels.', price: '₱2,800', img: '/img/img-tuxedo/tuxedo1.png' },
          {name: 'Velvet Tuxedo', description: ' Luxurious velvet tuxedo for standout occasions.', price: '₱4,500', img: '/img/img-tuxedo/tuxedo2.png' },
          {name: 'Midnight Blue Tuxedo', description: 'Elegant blue tuxedo with a modern cut.', price: '₱3,200', img: '/img/img-tuxedo/tuxedo3.png' },
          {name: 'White Dinner Jacket', description: ' Stylish white jacket for formal events.', price: '₱2,500', img: '/img/img-tuxedo/tuxedo4.png' },
          {name: 'Black Shawl Lapel Tuxedo', description: 'Classic black tuxedo with shawl lapel.', price: '₱3,000', img: '/img/img-tuxedo/tuxedo5.png' },
          {name: 'Patterned Tuxedo', description: 'Unique patterned tuxedo for trendy looks.', price: '₱3,500', img: '/img/img-tuxedo/tuxedo6.png' },
          {name: 'Burgundy Tuxedo', description: 'Rich burgundy tuxedo for special events.', price: '₱3,300', img: '/img/img-tuxedo/tuxedo7.png' },

        ],
    };
  },
  methods: {
     selectPackage() {
       this.showPackageForm = false;
       this.showVendorDetailsForm = true;
     },
     backBtnVendor() {
      this.showPackageForm = true;
      this.showVendorDetailsForm = false;
     },
     nextBtnVendorForm() {
      this.showVendorDetailsForm = false;
      this.showGownSelectionForm = true;
     },
     backBtnGown() {
      this.showVendorDetailsForm = true;
      this.showGownSelectionForm = false;
     },

     backBtnReviewDetails()
     {
      this.showGownSelectionForm = true;
      this.showCompleteEventProcess = false;
     },
    


    ProceedToDetails() {
      this.showGownSelectionForm = false;
      this.showCompleteEventProcess = true;
    },


    getSelectedLabel(selectedValue, options) {
      const selectedOption = options.find(option => option.value === selectedValue);
      return selectedOption ? selectedOption.label : 'N/A';
    },


    selectGownCard(gownIndex) {
      this.activeGownIndex =this.activeGownIndex === gownIndex ? null : gownIndex;
    },
    selectTuxedoCard(tuxedoIndex) {
      this.activeTuxedoIndex =  this.activeTuxedoIndex === tuxedoIndex ? null : tuxedoIndex;
    },

    selectCatalog(){
       this.showGownCatalog = false;
       this.showTuxedoCatalog = false;

       if(this.selectedOption ===  'gown1') {
        this.showGownCatalog = true;

       } else if(this.selectedOption ===  'tuxedo1') {
        this.showTuxedoCatalog = true;
       
       } 
    },
     
  }
};


</script>

<style scoped>
 html {
    scroll-behavior: smooth;
  }
</style>