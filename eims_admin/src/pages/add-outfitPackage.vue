<template>
    <div class="bg-gray-200 w-full h-full overflow-y-auto">
        <div class="w-full h-[65px] bg-gray-100 mt-2 flex items-center justify-between px-5 shadow-lg">
        <h1 class="font-amaticBold font-extraLight text-3xl">
            Outfit Packages
        </h1>
        </div>
    
        <div class="flex flex-row items-center m-5 space-x-5">
        <div class="flex justify-start w-52 h-20 bg-white rounded-lg shadow-lg px-2 items-center border-l-2 border-green-400 space-x-5">
            <img class="w-auto h-12" src="/img/wardrobes.png" alt="Vendor Image">
            <h2 class="font-amaticRegular text-4xl font-bold mb-0"> {{ totalOutfitPackages }} <span class = "text-sm antialiased text-gray-600">packages</span></h2>
        </div>
       
    </div>
    
    <div class="flex flex-row justify-end items-center m-5 my-7">
        <button class = "mr-2 w-44 h-10 bg-[#9B111E] font-semibold text-gray-100 font-quicksand rounded-md shadow-lg 
        transition-transform duration-300 transform hover:scale-105" @click="addOutfitsPackageBtn">
        Create Package
        </button>
		<button class = "mr-2 w-44 h-10 bg-[#9B111E] font-semibold text-gray-100 font-quicksand rounded-md shadow-lg 
        transition-transform duration-300 transform hover:scale-105" @click="addOutfitsBtn">
        Add Outfit
        </button>
    </div>
    
            <!-- Gown Packages Table -->
                <div v-if="showTable === 'GownPackages'" class="relative shadow-md sm:rounded-xl w-[1170px] h-[200] ml-5 mt-2 font-amaticBold mb-10">
                    <div class="overflow-x-auto">
                        <table class="w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400 mb-4 max-h-30">
                            <thead class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
                                <tr>
                                    <th scope="col" class="px-2 py-3">#</th>
                                    <th scope="col" class="px-2 py-3">Package Name</th>
                                    <th scope="col" class="px-2 py-3">Description</th>
                                    <th scope="col" class="px-2 py-3">Price</th>
                                    <th scope="col" class="px-2 py-3">Action</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr
                                    v-for="(gownPackage, index) in paginatedGownPackages"
                                    :key="gownPackage.gown_package_id"
                                    class="border-b dark:border-gray-700 odd:bg-white odd:dark:bg-gray-900 even:bg-gray-50 even:dark:bg-gray-800">
                                    <th scope="row" class="px-2 py-3 font-medium text-gray-900 whitespace-nowrap dark:text-white">{{ gownPackage.dummyIndex }}</th>
                                    <td class="px-1 py-3 hidden sm:table-cell">{{ gownPackage.gown_package_name }}</td>
                                    <td class="px-1 py-3 hidden sm:table-cell">{{ gownPackage.description }}</td>
                                    <td class="px-1 py-3 hidden sm:table-cell">{{ formatPrice(gownPackage.gown_package_price) }} php</td> 
                                    <td class="px-1 py-3 hidden sm:table-cell">
                                        <button
                                            class="h-8 w-14 bg-[#9B111E] font-amaticBold font-medium text-sm rounded-md text-white hover:bg-[#B73A45]"
                                            @click="editGownPackageBtn(index)">
                                            Update
                                        </button>
                                    </td>
                                </tr>
                            </tbody>
                        </table>

                        <!-- Pagination Controls -->
                        <div class="flex justify-center space-x-2 mt-4 mb-6">
                            <button @click="prevGownPackagePage" :disabled="currentGownPackagePage === 1"
                                class="px-3 py-1 bg-[#9B111E] text-white rounded-md hover:bg-[#B73A45] disabled:opacity-50 text-sm">Previous</button>
                            <button v-for="page in totalGownPackagePages" :key="page" @click="changeGownPackagePage(page)"
                                :class="{'bg-[#9B111E]': currentGownPackagePage === page, 'bg-gray-300': currentGownPackagePage !== page}"
                                class="px-3 py-1 text-white rounded-md hover:bg-[#B73A45] text-xs">
                                {{ page }}
                            </button>
                            <button @click="nextGownPackagePage" :disabled="currentGownPackagePage === totalGownPackagePages"
                                class="px-3 py-1 bg-[#9B111E] text-white rounded-md hover:bg-[#B73A45] disabled:opacity-50 text-xs">Next</button>
                        </div>
                    </div>
                </div>

    
         
         <!-- Add Package Form -->    
        <form v-if="showOutfitPackageForm" @submit.prevent="submitPackage"
                @click.self="closePackageForm"
                class="fixed inset-0 bg-black bg-opacity-50 flex justify-center items-center overflow-y-auto z-50"
            >
                <div class="bg-white w-full max-w-lg p-6 rounded-lg shadow-xl transform transition duration-300 relative">
                    <!-- Header -->
                    <div class="mb-6">
                        <h2 class="text-2xl font-bold text-gray-800 text-center">Add Outfit Package</h2>
                    </div>

                    <!-- Package Name -->
                    <div class="mb-4">
                        <input
                            id="package-name"
                            type="text"
                            v-model="packageDetails.name"
                            class="mt-2 block w-full rounded-lg border-gray-300 shadow-sm focus:border-blue-500 focus:ring focus:ring-blue-200"
                            placeholder="Enter package name"
                            required
                        />
                    </div>

               <!-- Description -->
                <div class="mb-4">
                    <textarea
                        id="description"
                        v-model="packageDetails.description"
                        class="mt-2 block w-full rounded-lg border-gray-300 shadow-sm focus:border-blue-500 focus:ring focus:ring-blue-200"
                        placeholder="Enter description"
                        rows="3"
                        style="resize: none;"
                    ></textarea>
                </div>



                    <!-- Outfit Selection Buttons -->
                    <div class="flex justify-center space-x-4 my-6">
                        <button  @click="openOutfitSelection"
                            type="button"
                            class="px-4 py-2 bg-blue-600 text-white rounded-lg shadow-sm hover:bg-blue-700 transition duration-300"
                        >
                            Add Outfits
                        </button>
                    </div>

                    
            <!-- Inclusions Table -->
            <div class="mb-6">
                <h3 class="text-lg font-semibold text-gray-800 mb-2">Inclusions</h3>
                <div class="border rounded-lg" style="height: 150px; overflow-y: auto;">
                    <table class="w-full">
                        <thead class="bg-gray-200 sticky top-0 z-10">
                            <tr>
                                <th class="p-2 text-left">Type</th>
                                <th class="p-2 text-left">Name</th>
                                <th class="p-2 text-left">Price</th>
                                <th class="p-2 text-left">Actions</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr
                                v-for="item in packageInclusions"
                                :key="item.outfit_id"
                                class="hover:bg-gray-100 border-t"
                            >
                                <td class="p-2 text-sm capitalize">{{ item.outfit_type }}</td>
                                <td class="p-2 text-sm">{{ item.outfit_name }}</td>
                                <td class="p-2 text-sm">{{ formatPrice(item.rent_price) }} php</td>
                                <td class="p-2 text-sm">
                                    <button
                                    @click="removeInclusion(item.outfit_id)"
                                    class="rounded p-1 hover:bg-red-100"
                                >
                                    <img 
                                        src="/img/delete.png"
                                        alt="Remove"
                                        class="w-4 h-4"
                                    />
                                </button>
                                </td>
                            </tr>
                        </tbody>
                </table>
            </div>
        </div>


            <!-- Price Summary Section -->
                <div class="mt-6 border-t pt-4">
                    <div class="flex justify-between items-center mb-2">
                        <span class="text-gray-600">Subtotal:</span>
                        <span class="font-semibold">₱ {{ formatPrice(calculateSubtotal()) }}</span>
                    </div>
                    
                    <!-- Discount Input -->
                    <div class="flex justify-between items-center mb-2">
                        <div class="flex items-center">
                            <span class="text-gray-600 mr-2">Discount (%):</span>
                            <input 
                                type="number" 
                                v-model.number="packageDetails.discount"
                                min="0"
                                max="100"
                                class="w-20 px-2 py-1 border rounded"
                            >
                        </div>
                        <span class="font-semibold ">- ₱ {{ formatPrice(calculateDiscount()) }}</span>
                    </div>

                    <!-- Total -->
                    <div class="flex justify-between items-center mt-4 pt-2 border-t">
                        <span class="text-lg font-bold">Total:</span>
                        <span class="text-lg font-bold ">₱ {{ formatPrice(calculateTotal()) }}</span>
                    </div>
                </div>

                    <!-- Actions -->
                    <div class="flex justify-end space-x-4 mt-6">
                        <button
                            @click="closePackageForm"
                            type="button"
                            class="px-4 py-2 bg-gray-300 text-gray-700 rounded-lg shadow-sm hover:bg-gray-400 transition duration-300"
                        >
                            Cancel
                        </button>
                        <button
                            type="submit"
                            class="px-4 py-2 bg-blue-600 text-white font-semibold rounded-lg shadow-sm hover:bg-blue-700 transition duration-300"
                        >
                            Save
                        </button>
                    </div>
                </div>
            </form>

            <!-- Outfit Selection Modal -->
            <div v-if="showOutfitModal" class="fixed inset-0 bg-black bg-opacity-50 flex justify-center items-center z-50">
                <div class="bg-white w-full max-w-lg p-6 rounded-lg shadow-xl">
                    <h3 class="text-xl font-semibold text-gray-800 mb-4">Select Outfits</h3>
                    
                    <!-- Search Input -->
                    <div class="mb-4">
                        <input
                            type="text"
                            v-model="searchQuery"
                            placeholder="Search outfits..."
                            class="w-full px-4 py-2 border rounded-lg"
                        >
                    </div>

                    <!-- Combined Outfits Table -->
                    <div style="max-height: 300px; overflow-y: auto;">
                    <table class="w-full text-sm">
                        <thead class="bg-gray-50 sticky top-0 z-10">
                            <tr>
                                <th class="px-4 py-2">Name</th>
                                <th class="px-4 py-2">Type</th>
                                <th class="px-4 py-2">Price</th>
                                <th class="px-4 py-2">Action</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-for="outfit in filteredOutfits" :key="outfit.outfit_id">
                            <td class="px-4 py-2">{{ outfit.outfit_name }}</td>
                            <td class="px-4 py-2 capitalize">{{ outfit.outfit_type }}</td>
                            <td class="px-4 py-2">₱{{ formatPrice(outfit.rent_price) }}</td>
                            <td class="px-4 py-2">
                                <button
                                    @click="toggleOutfitSelection(outfit)"
                                    class="rounded p-1"
                                >
                                    <img 
                                        :src="isOutfitSelected(outfit.outfit_id) ? '/img/delete.png' : '/img/inlcude.png'" 
                                        :alt="isOutfitSelected(outfit.outfit_id) ? 'Remove' : 'Add'"
                                        class="w-6 h-6"
                                    />
                                </button>
                            </td>
                        </tr>
                        </tbody>
                    </table>
                    </div>

                    <div class="mt-4 flex justify-end">
                        <button @click="closeOutfitModal" class="text-gray-600 hover:text-gray-800">
                            Close
                        </button>
                    </div>
                </div>
            </div>



            
            
            <!-- Edit Outfit Package Form -->
                <form v-if="editGownPackageForm" @submit.prevent="updateGownPackage" class="fixed inset-0 bg-black bg-opacity-30 flex justify-center items-center overflow-y-auto z-50">
                <div class="bg-white w-full max-w-md p-6 rounded-lg shadow-xl transform transition duration-300">
                    <!-- Header -->
                    <div class="flex justify-between items-center mb-4">
                    <h2 class="text-2xl font-bold text-gray-800">Edit Gown Package</h2>
                    <button @click="closeEditGownPackageForm" class="text-red-500 hover:text-red-700 transition duration-300">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
                        </svg>
                    </button>
                    </div>

                    <!-- Error Message -->
                    <div v-if="errorMessage" class="text-sm text-red-500 mb-4">
                    {{ errorMessage }}
                    </div>

                    <!-- Gown Package Name -->
                    <div class="mb-4">
                    <input
                        id="gown-package-name"
                        type="text"
                        v-model="selectedGownPackage.gown_package_name"
                        class="mt-2 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring focus:ring-blue-200"
                        placeholder="Enter package name"
                        required
                    />
                    </div>

                    <!-- Description -->
                    <div class="mb-4">
                    <input
                        id="description"
                        type="text"
                        v-model="selectedGownPackage.description"
                        class="mt-2 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring focus:ring-blue-200"
                        placeholder="Enter description"
                    />
                    </div>

                   <!-- Gowns Section -->
                    <div class="mb-6">
                        <h3 class="text-lg font-semibold text-gray-800 mb-2">Select Gowns</h3>
                        <div class="max-h-48 overflow-y-auto border border-gray-300 rounded-lg">
                        <table class="w-full">
                            <thead class="bg-gray-200">
                            <tr>
                                <th class="p-2 text-left">Select</th>
                                <th class="p-2 text-left">Gown Name</th>
                                <th class="p-2 text-left">Price</th>
                            </tr>
                            </thead>
                            <tbody>
                            <tr 
                                v-for="outfit in gowns" 
                                :key="outfit.outfit_id" 
                                class="hover:bg-gray-100"
                            >
                                <td class="p-2 text-center">
                                    <input 
                                        type="checkbox" 
                                        :value="outfit.outfit_id"
                                        :checked="selectedGownPackage.selectedGowns.includes(outfit.outfit_id)"
                                        @change="toggleSelection(outfit.outfit_id, 'gown')"
                                        class="form-checkbox h-5 w-5 text-blue-600"
                                    >
                                </td>
                                <td class="p-2 text-sm">{{ outfit.outfit_name }}</td>
                                <td class="p-2 text-sm">{{ formatPrice(outfit.rent_price) }} php</td>
                            </tr>
                            </tbody>
                        </table>
                        </div>
                    </div>

                    <!-- Tuxedos Section -->
                    <div class="mb-6">
                        <h3 class="text-lg font-semibold text-gray-800 mb-2">Select Tuxedos</h3>
                        <div class="max-h-48 overflow-y-auto border border-gray-300 rounded-lg">
                        <table class="w-full">
                            <thead class="bg-gray-200">
                            <tr>
                                <th class="p-2 text-left">Select</th>
                                <th class="p-2 text-left">Tuxedo Name</th>
                                <th class="p-2 text-left">Price</th>
                            </tr>
                            </thead>
                            <tbody>
                            <tr 
                                v-for="outfit in tuxedos" 
                                :key="outfit.outfit_id" 
                                class="hover:bg-gray-100"
                            >
                                <td class="p-2 text-center">
                                    <input 
                                        type="checkbox" 
                                        :value="outfit.outfit_id"
                                        :checked="selectedGownPackage.selectedTuxedos.includes(outfit.outfit_id)"
                                        @change="toggleSelection(outfit.outfit_id, 'tuxedo')"
                                        class="form-checkbox h-5 w-5 text-blue-600"
                                    >
                                </td>
                                <td class="p-1 text-sm">{{ outfit.outfit_name }}</td>
                                <td class="p-1 text-sm">{{ formatPrice(outfit.rent_price) }} php</td>
                            </tr>
                            </tbody>
                        </table>
                        </div>
                    </div>

                    <!-- Actions -->
                    <div class="flex justify-end space-x-4">
                    <button
                        @click="closeEditGownPackageForm"
                        type="button"
                        class="px-4 py-2 bg-red-300 text-gray-700 rounded-lg shadow-sm hover:bg-red-500 transition duration-300"
                    >
                        Delete
                    </button>
                    <button
                        type="submit"
                        class="px-4 py-2 bg-blue-500 text-white font-semibold rounded-lg shadow-sm hover:bg-blue-600 transition duration-300"
                    >
                        Save Changes
                    </button>
                    </div>
                </div>
            </form>


    <!-- Add Outfit Form -->
    <form v-if="addOutfitForm" @submit.prevent="handleSubmit" class="flex justify-center items-center fixed inset-0 bg-gray-800 bg-opacity-50 overflow-y-auto" @click.self="closeAddOutfitForm">
        <div class="bg-white w-[600px] p-5 rounded-lg shadow-lg overflow-y-auto">
            <div class="flex justify-between items-center m-3">
                <h1 class="font-semibold text-xl font-raleway text-gray-800">Add Outfit</h1>
            </div>
            <div class="border border-gray-500 mt-5 items-center"></div>
            <div class="m-5">
                <span>{{ errorMessage }}</span>

        <!-- Outfit Name -->
            <div class="flex flex-row mt-5">
                <input type="text" 
                    class="mt-2 ml-2 p-2 w-full h-10 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:border-blue-700" 
                    v-model="newOutfit.outfit_name" 
                    placeholder="Outfit Name" 
                    required>
                        <!-- Outfit Type -->
                        <select class="mt-2 ml-2 p-2 w-full h-10 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:border-blue-700" 
                                v-model="newOutfit.outfit_type" 
                                required>
                            <option value="" disabled selected>Outfit Type</option>
                            <option value="Wedding Gown">Wedding Gown</option>
                            <option value="Saree">Saree</option>
                            <option value="Lehenga">Lehenga</option>
                            <option value="Suit">Suit</option>
                            <option value="Jumpsuit">Jumpsuit</option>
                            <option value="Reception Dress">Reception Dress</option>
                            <option value="Bridal Robe">Bridal Robe</option>
                            <option value="Tuxedo">Tuxedo</option>
                            <option value="Sherwani">Sherwani</option>
                            <option value="Kurta Pajama">Kurta Pajama</option>
                            <option value="Bespoke Tailored Outfit">Bespoke Tailored Outfit</option>
                            <option value="Barong Tagalog">Barong Tagalog</option>
                            <option value="Morning Coat">Morning Coat</option>
                            <option value="Bridesmaid Dress">Bridesmaid Dress</option>
                            <option value="Cultural Attire">Cultural Attire</option>
                            <option value="Mix-and-Match Dress">Mix-and-Match Dress</option>
                            <option value="Flower Girl Dress">Flower Girl Dress</option>
                            <option value="Ring Bearer Suit">Ring Bearer Suit</option>
                            <option value="Formal Attire">Formal Attire</option>
                            <option value="Semi-Formal Attire">Semi-Formal Attire</option>
                            <option value="Traditional/Tribal Wear">Traditional/Tribal Wear</option>
                            <option value="Engagement Outfit">Engagement Outfit</option>
                            <option value="Rehearsal Dinner Attire">Rehearsal Dinner Attire</option>
                            <option value="Haldi Ceremony Outfit">Haldi Ceremony Outfit</option>
                            <option value="Mehndi Ceremony Outfit">Mehndi Ceremony Outfit</option>
                            <option value="Cocktail Party Wear">Cocktail Party Wear</option>
                            <option value="Destination Wedding Attire">Destination Wedding Attire</option>
                            <option value="Seasonal Attire">Seasonal Attire</option>
                        </select>
                    </div>

                <!-- Outfit Color -->
                <div class="flex flex-row mt-5">
                    <input type="text" class="mt-2 ml-2 p-2 w-full h-10 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:border-blue-700" v-model="newOutfit.outfit_color" placeholder="Outfit Color" required>
                    <!-- Rent Price -->
                    <input type="number" step="0.01" class="mt-2 ml-2 p-2 w-full h-10 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:border-blue-700" v-model="newOutfit.rent_price" placeholder="Rent Price" required>
                </div>

                <!-- Size -->
                <div class="flex flex-row mt-5">
                    <select class="mt-2 ml-2 p-2 w-full h-10 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:border-blue-700" v-model="newOutfit.size" required>
                        <option value="" disabled selected>Size</option>
                        <option value="XS">XS</option>
                        <option value="S">S</option>
                        <option value="M">M</option>
                        <option value="L">L</option>
                        <option value="XL">XL</option>
                        <option value="2XL">2XL</option>
                        <option value="3XL">3XL</option>
                        <option value="4XL">4XL</option>
                        <option value="5XL">5XL</option>
                        </select>
                    <!-- Weight -->
                    <input type="number" step="0.01" class="mt-2 ml-2 p-2 w-full h-10 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:border-blue-700" v-model="newOutfit.weight" placeholder="Weight" required>
                </div>
                  
                <!-- Outfit From -->
                <div class="mt-5">
                    <input type="text" class="mt-2 ml-2 p-2 w-full h-10 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:border-blue-700" v-model="outfitArchive.creation_address" placeholder="Outfit Origin" required>
                </div>

                <!-- Outfit Owner -->
                <div class="mt-5">
                    <input type="text" class="mt-2 ml-2 p-2 w-full h-10 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:border-blue-700" v-model="outfitArchive.owner" placeholder="Outfit Owner" required>
                </div>

                <!-- Outfit Description -->
                <div class="mt-5">
                    <textarea class="mt-2 ml-2 p-2 w-full h-20 rounded-lg shadow-md border border-gray-500 focus:outline-none focus:border-blue-700" v-model="newOutfit.outfit_desc" placeholder="Outfit Description" required></textarea>
                </div>

                <!-- Outfit Image Upload -->
                <div class="mt-3 flex flex-col items-center">
                    <div class="h-[150px] w-[500px] rounded-lg shadow-md flex flex-col items-center justify-between p-2 gap-1 bg-blue-50">
                        <div class="flex-1 w-full border-2 border-dashed border-royalblue rounded-lg flex items-center justify-center flex-col">
                            <svg class="h-[50px]" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <path d="M7 10V9C7 6.23858 9.23858 4 12 4C14.7614 4 17 6.23858 17 9V10C19.2091 10 21 11.7909 21 14C21 15.4806 20.1956 16.8084 19 17.5M7 10C4.79086 10 3 11.7909 3 14C3 15.4806 3.8044 16.8084 5 17.5M7 10C7.43285 10 7.84965 10.0688 8.24006 10.1959M12 12V21M12 12L15 15M12 12L9 15" stroke="#000000" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
                            </svg>
                            <p class="text-center text-black text-sm">Browse File to upload!</p>
                        </div>
                        <label for="file" class="bg-blue-50 w-full h-[45px] p-2 rounded-lg cursor-pointer flex items-center justify-end text-black border-none">
                            <svg class="h-[100%] bg-gray-100 rounded-full p-1 shadow-md" fill="#000000" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg">
                                <path d="M15.331 6H8.5v20h15V14.154h-8.169z"></path>
                                <path d="M18.153 6h-.009v5.342H23.5v-.002z"></path>
                            </svg>
                            <p id="displayFileName" class="flex-1 text-center text-sm">No file selected</p>
                            <svg class="h-[100%] bg-gray-100 rounded-full p-1 shadow-md" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <path d="M5.16565 10.1534C5.07629 8.99181 5.99473 8 7.15975 8H16.8402C18.0053 8 18.9237 8.9918 18.8344 10.1534L18.142 19.1534C18.0619 20.1954 17.193 21 16.1479 21H7.85206C6.80699 21 5.93811 20.1954 5.85795 19.1534L5.16565 10.1534Z" stroke="#000000" stroke-width="2"></path>
                                <path d="M19.5 5H4.5" stroke="#000000" stroke-width="2" stroke-linecap="round"></path>
                                <path d="M10 3C10 2.44772 10.4477 2 11 2H13C13.5523 2 14 2.44772 14 3V5H10V3Z" stroke="#000000" stroke-width="2"></path>
                            </svg>
                        </label>
                        <input id="file" type="file" class="hidden" @change="updateFileName" accept="image/*">
                      
                          
                    </div>
                </div>

                <!-- Confirm and Cancel Buttons -->
                <div class="flex justify-center items-center mt-5 space-x-2">
                    <button class="w-20 h-10 bg-gray-300 text-white px-3 py-1 rounded transform transition duration-300 transform hover:scale-105 hover:bg-gray-400" @click="closeAddOutfitForm">
                        Cancel
                    </button>
                    <button type="submit" class="w-20 h-10 bg-blue-500 text-gray-100 font-semibold rounded-lg shadow-md transform transition duration-300 transform hover:scale-105">
                        Save
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
        name: 'AddOutfitPackage',
        data() {
            return {
            showTable: 'GownPackages',
            currentGownPackagePage: 1,
            rowsPerGownPackagePage: 5,
            editGownPackageForm: false,
			addOutfitForm: false,
			searchTerm: '',
            newGownPackage: {
                gown_package_name: '',
                description: '',
                outfits: []
            },
            gownPackages: [],
            addOutfitsPackageForm: false,
            gowns: [],
            tuxedos: [],
            errorMessage: '',
            selectedGowns: [],
            selectedTuxedos: [],
            selectedGownPackage: {
                gown_package_id: null,
                gown_package_name: '',
                description: '',
                selectedGowns: [],
                selectedTuxedos: []
            },

            newOutfit: {
                outfit_name: '',
                outfit_type: '',
                outfit_color: '',
                outfit_desc: '',
                rent_price: '',
                status: 'Available',
                outfit_img: '',
                size: '',
                weight: ''
            },
            outfitArchive: {
                creation_address: '',
                creation_date: '',
                owner: '',
                retail_price: ''
            },
          
            previewSrc: null,
            previewImage: "",

            showOutfitModal: false,
                currentOutfitType: '', // 'gown' or 'tuxedo'
                packageDetails: {
                    name: '',
                    description: ''
                },
            selectedOutfits: [],

            showModal: false,
                modalType: null,
                inclusions: [],
                packageDetails: {
                    name: '',
                    description: '',
                    outfits: [],
                    discount: 0,
                },

            showOutfitPackageForm: false,
            outfitSearchTerm: '',
            showOutfitModal: false,
            searchQuery: '',
            outfits: [],

            packageInclusions: [],
            packageDetails: {
                name: '',
                description: '',
                discount: 0
            }
        
                

        };
    },

     computed: {
        totalOutfitPackages() {
            return this.gownPackages.length;
        },
        paginatedGownPackages() {
            const start = (this.currentGownPackagePage - 1) * this.rowsPerGownPackagePage;
            const end = start + this.rowsPerGownPackagePage;
            return this.gownPackages.slice(start, end);
        },
        totalGownPackagePages() {
            return Math.ceil(this.gownPackages.length / this.rowsPerGownPackagePage);
        },
        filteredOutfits() {
            if (!this.searchQuery) return this.outfits;
            const query = this.searchQuery.toLowerCase();
            return this.outfits.filter(outfit => 
                outfit.outfit_name.toLowerCase().includes(query) || 
                outfit.outfit_type.toLowerCase().includes(query)
            );
        },
    },
    methods: {
        async fetchGownPackages() {
            try {
                const token = localStorage.getItem('access_token');
                if (!token) {
                    alert('You are not logged in. Please log in to view gown packages.');
                    return;
                }

                const response = await axios.get('http://127.0.0.1:5000/gown-packages', {
                    headers: {
                        'Content-Type': 'application/json',
                        'Authorization': `Bearer ${token}`,
                    },
                    withCredentials: true,calculateSubtotal() {
                            return this.inclusions.reduce((total, item) => total + item.price, 0);
                        },
                    
                        calculateDiscount() {
                            const subtotal = this.calculateSubtotal();
                            return (subtotal * this.packageDetails.discount) / 100;
                        },
                    
                        calculateTotal() {
                            return this.calculateSubtotal() - this.calculateDiscount();
                        },
                    
                        formatPrice(price) {
                            return Number(price).toFixed(2);
                        }
                });

                // Populate gownPackages array with data from API
                this.gownPackages = response.data.map((item, index) => ({
                    gown_package_id: item.gown_package_id,
                    gown_package_name: item.gown_package_name,
                    gown_package_price: item.gown_package_price,
                    description: item.description,
                    dummyIndex: index + 1,
                }));

            } catch (error) {
                console.error('Error fetching gown packages:', error.response?.data || error.message);
            }
        },


    async fetchOutfits() {
            try {
            const token = localStorage.getItem('access_token');
            if (!token) {
                alert('You are not logged in. Please log in to view outfits.');
                return;
            }

            const response = await axios.get('http://127.0.0.1:5000/outfits', {
                headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${token}`,
                },
                withCredentials: true,
            });

            // Populate outfits array with data from API
            this.outfits = response.data.map((item, index) => ({
                outfit_id: item.outfit_id,
                outfit_name: item.outfit_name,
                outfit_type: item.outfit_type,
                outfit_color: item.outfit_color,
                outfit_desc: item.outfit_desc,
                rent_price: item.rent_price,
                status: item.status,
                outfit_img: item.outfit_img,
                size: item.size,
                weight: item.weight,
                dummyIndex: index + 1,
            }));

            // Separate outfits by type
            this.gowns = this.outfits.filter(outfit => outfit.outfit_type === 'Gown');
            this.tuxedos = this.outfits.filter(outfit => outfit.outfit_type === 'Tuxedo');

            } catch (error) {
            console.error('Error fetching outfits:', error.response?.data || error.message);
            }
        },
        addGownOutfits(event) {
            const selectedOptions = Array.from(event.target.selectedOptions).map(option => option.value);
            this.newGownPackage.outfits = [...new Set([...this.newGownPackage.outfits, ...selectedOptions])];
        },
        addTuxedoOutfits(event) {
            const selectedOptions = Array.from(event.target.selectedOptions).map(option => option.value);
            this.newGownPackage.outfits = [...new Set([...this.newGownPackage.outfits, ...selectedOptions])];
        },

    
        async submitPackage() {
                try {
                    const token = localStorage.getItem('access_token');
                    if (!token) {
                        alert('You are not logged in. Please log in to add a package.');
                        return;
                    }

                    // Check if package has a name
                    if (!this.packageDetails.name) {
                        this.errorMessage = "Please enter a package name";
                        return;
                    }

                    // Check if at least one outfit is included
                    if (this.packageInclusions.length === 0) {
                        this.errorMessage = "Please add at least one outfit to the package";
                        return;
                    }

                    // Prepare the package data
                    const packageData = {
                        gown_package_name: this.packageDetails.name,
                        description: this.packageDetails.description || '',
                        outfits: this.packageInclusions.map(item => item.outfit_id),  // Changed from item.id
                        discount: this.packageDetails.discount || 0
                    };

                    console.log('Sending data:', packageData);

                    const response = await axios.post('http://127.0.0.1:5000/add-gown-package', packageData, {
                        headers: {
                            'Content-Type': 'application/json',
                            'Authorization': `Bearer ${token}`,
                        },
                        withCredentials: true,
                    });

                    alert('Package added successfully');
                    
                    // Reset form
                    this.packageDetails = {
                        name: '',
                        description: '',
                        discount: 0
                    };
                    this.packageInclusions = [];  // Changed from inclusions
                    this.selectedOutfits = [];    // Added this to clear selected outfits
                    this.showOutfitPackageForm = false;
                    this.errorMessage = '';
                    
                    await this.fetchGownPackages();
                } catch (error) {
                    console.error('Error details:', {
                        message: error.message,
                        response: error.response?.data,
                        status: error.response?.status
                    });
                    this.errorMessage = error.response?.data?.message || 'An error occurred. Please try again.';
                }
            },
        updateFileName(event) {
            const fileInput = event.target;
            const fileName = fileInput.files.length > 0 ? fileInput.files[0].name : "No file selected";
            document.getElementById("displayFileName").textContent = fileName;
        },



            
        // Pagination methods
        prevGownPackagePage() {
            if (this.currentGownPackagePage > 1) {
                this.currentGownPackagePage--;
            }
        },
        nextGownPackagePage() {
            if (this.currentGownPackagePage < this.totalGownPackagePages) {
                this.currentGownPackagePage++;
            }
        },
        changeGownPackagePage(page) {
            this.currentGownPackagePage = page;
        },
        editVenueBtn(index) {
            // Handle edit action for venue
            console.log(`Edit venue at index: ${index}`);
        },
    
        addOutfitsPackageBtn() {
            this.showOutfitPackageForm = true;  // Show the form
            this.packageDetails = {
                name: '',
                description: ''
            };
            this.inclusions = [];
        },
        closeAddGownPackageForm()
        {
            this.addOutfitsPackageForm = false;
            this.newGownPackage = {};
        },
       
        formatPrice(price) {
            if (price === null || price === undefined || typeof price === 'object' || isNaN(price)) {
                return 'N/A'; // Return a fallback if price is invalid
            }
            // Ensure price is treated as a number, round to 2 decimal places, and format with commas
            return parseFloat(price).toFixed(2).replace(/\d(?=(\d{3})+\.)/g, '$&,');
            },
            
            editGownPackageBtn(index) {
                const gownPackage = this.gownPackages[index];
                this.selectedGownPackage = {
                    gown_package_id: gownPackage.gown_package_id,
                    gown_package_name: gownPackage.gown_package_name,
                    description: gownPackage.description,
                    selectedGowns: [], // You'll need to fetch the actual selected gowns from backend
                    selectedTuxedos: [] // You'll need to fetch the actual selected tuxedos from backend
                };
                this.editGownPackageForm = true;
            },

            closeEditGownPackageForm() {
                this.editGownPackageForm = false;
                this.selectedGownPackage = {
                    gown_package_name: '',
                    description: '',
                    gown_ids: [],
                    tuxedo_ids: []
                }; // Reset form fields to default
                this.errorMessage = ''; // Clear error messages
                },

			addOutfitsBtn() {
				this.addOutfitForm = true;
			},
            closeAddOutfitForm() {
                this.addOutfitForm = false;
            },

            async handleSubmit() {
                try {
                    const token = localStorage.getItem('access_token');
                    if (!token) {
                        this.errorMessage = 'Authentication required';
                        return;
                    }

                    // Create FormData object
                    const outfitData = {
                        ...this.newOutfit,
                        status: 'Available',  // Set default status
                        archive: {
                            ...this.outfitArchive,
                            creation_date: new Date().toISOString().split('T')[0],  // Set current date
                            usage: 0  // Set initial usage
                        }
                    };

                    // Make API request
                    const response = await axios.post('http://127.0.0.1:5000/outfits', outfitData, {
                        headers: {
                            'Authorization': `Bearer ${token}`,
                            'Content-Type': 'application/json'
                        }
                    });

                    if (response.data) {
                        alert('Outfit added successfully');
                        this.resetForm();
                        this.closeAddOutfitForm();
                        // You might want to refresh the outfits list here
                        // await this.fetchOutfits();
                    }
                } catch (error) {
                    console.error('Error adding outfit:', error);
                    this.errorMessage = error.response?.data?.message || 'Failed to add outfit';
                }
            },

            resetForm() {
                this.newOutfit = {
                    outfit_name: '',
                    outfit_type: '',
                    outfit_color: '',
                    outfit_desc: '',
                    rent_price: '',
                    status: 'Available',
                    outfit_img: '',
                    size: '',
                    weight: ''
                };
                this.outfitArchive = {
                    creation_address: '',
                    creation_date: new Date().toISOString().split('T')[0],
                    owner: '',
                    retail_price: '',
                    usage: 0
                };
                this.selectedFile = null;
                this.previewSrc = null;
                this.errorMessage = '';
                document.getElementById('displayFileName').textContent = 'No file selected';
            },

            openOutfitSelection(type) {
                this.currentOutfitType = type;
                this.showOutfitModal = true;
            },
            closeOutfitModal() {
                this.showOutfitModal = false;
            },
            getOutfits() {
                return this.currentOutfitType === 'gown' ? this.gowns : this.tuxedos;
            },
      
            addOutfitToPackage() {
                // Logic to push selected outfits into the inclusion table
                console.log('Selected Outfits:', this.selectedOutfits);
                this.closeOutfitModal();
            },

            openModal(type) {
                this.modalType = type;
                this.showModal = true;
            },

            closeModal() {
                this.showModal = false;
                this.modalType = null;
            },

            getOutfits(type) {
                // Map the outfits to have a consistent structure
                const outfits = type === 'gown' ? this.gowns : this.tuxedos;
                return outfits.map(outfit => ({
                    id: outfit.outfit_id,
                    name: outfit.outfit_name,
                    price: outfit.rent_price,
                    type: type
                }));
            },

            addInclusion(outfit) {
                // Check if outfit is already included
                const exists = this.inclusions.some(item => item.id === outfit.id);
                if (!exists) {
                    this.inclusions.push({
                        id: outfit.id,
                        name: outfit.name,
                        price: Number(outfit.price), // Convert to number
                        type: this.modalType
                    });
                }
                this.closeModal();
            },
            removeInclusion(outfitId) {
                // Remove from packageInclusions
                const index = this.packageInclusions.findIndex(item => item.outfit_id === outfitId);
                if (index !== -1) {
                    this.packageInclusions.splice(index, 1);
                }
                
                // Remove from selectedOutfits
                const selectedIndex = this.selectedOutfits.findIndex(item => item.outfit_id === outfitId);
                if (selectedIndex !== -1) {
                    this.selectedOutfits.splice(selectedIndex, 1);
                }
                
                // Update total
                this.calculateTotal();
            },

            closePackageForm() {
                this.showOutfitPackageForm = false;
                this.packageDetails = {
                    name: '',
                    description: '',
                    discount: 0
                };
                this.packageInclusions = [];
                this.selectedOutfits = [];
            },

            calculateSubtotal() {
                return this.packageInclusions.reduce((total, item) => total + Number(item.rent_price), 0);
            },

            calculateDiscount() {
                const subtotal = this.calculateSubtotal();
                return (subtotal * (this.packageDetails.discount || 0)) / 100;
            },

            calculateTotal() {
                return this.calculateSubtotal() - this.calculateDiscount();
            },
                    

            formatPrice(price) {
                return Number(price).toFixed(2);
            },


        formatPrice(price) {
            if (price === null || price === undefined || typeof price === 'object' || isNaN(price)) {
                return 'N/A'; // Return a fallback if price is invalid
            }
            // Ensure price is treated as a number, round to 2 decimal places, and format with commas
            return parseFloat(price).toFixed(2).replace(/\d(?=(\d{3})+\.)/g, '$&,');
        },

        openOutfitSelection() {
        this.showOutfitModal = true;
        this.fetchOutfits();
    },
    closeOutfitModal() {
        this.showOutfitModal = false;
        this.searchQuery = '';
    },
   
 
    isOutfitSelected(outfitId) {
        return this.selectedOutfits.some(outfit => outfit.outfit_id === outfitId);
    },
    toggleOutfitSelection(outfit) {
        const index = this.selectedOutfits.findIndex(item => item.outfit_id === outfit.outfit_id);
        if (index === -1) {
            // Add to selectedOutfits array
            this.selectedOutfits.push(outfit);
            
            // Add to package inclusions
            this.packageInclusions.push({
                outfit_id: outfit.outfit_id,
                outfit_name: outfit.outfit_name,
                outfit_type: outfit.outfit_type,
                rent_price: outfit.rent_price,
                quantity: 1
            });
            
            // Update total
            this.calculateTotal();
            
            // Close the modal
            this.closeOutfitModal();
        } else {
            // Remove from selectedOutfits array
            this.selectedOutfits.splice(index, 1);
            
            // Remove from package inclusions
            const inclusionIndex = this.packageInclusions.findIndex(item => item.outfit_id === outfit.outfit_id);
            if (inclusionIndex !== -1) {
                this.packageInclusions.splice(inclusionIndex, 1);
            }
            
            // Update total
            this.calculateTotal();
        }
    },

 
                        

    
    
    },
    
        mounted() {
            this.fetchGownPackages();
            this.fetchOutfits();
        },
    
    
    
    }
    
    
    </script>
    
    <style scoped>

    </style>