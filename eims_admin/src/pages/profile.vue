<template>
  <div class="max-w-4xl mx-auto p-6 bg-white shadow-md rounded-lg">
    <!-- Profile Header -->
    <div class="flex items-center justify-between mb-6">
      <div class="flex items-center">
        <img
          v-if="user.user_img"
          :src="user.user_img"
          alt="User Image"
          class="w-24 h-24 rounded-full border-2 border-gray-300"
        />
        <div v-else class="w-24 h-24 bg-gray-300 rounded-full flex items-center justify-center text-white font-bold">
          {{ user.firstname[0] }}{{ user.lastname[0] }}
        </div>
        <div class="ml-6">
          <h2 class="text-2xl font-semibold text-gray-800">{{ user.firstname }} {{ user.lastname }}</h2>
          <p class="text-gray-500">{{ user.email }}</p>
        </div>
      </div>
      <button
        @click="editProfile"
        class="bg-blue-500 text-white px-4 py-2 rounded-lg hover:bg-blue-700"
      >
        Edit Profile
      </button>
    </div>

    <!-- Profile Information -->
    <div v-if="editing" class="space-y-4">
      <div>
        <label for="firstname" class="block text-sm font-medium text-gray-700">First Name</label>
        <input
          v-model="user.firstname"
          id="firstname"
          type="text"
          class="mt-1 p-2 w-full border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500"
        />
      </div>
      <div>
        <label for="lastname" class="block text-sm font-medium text-gray-700">Last Name</label>
        <input
          v-model="user.lastname"
          id="lastname"
          type="text"
          class="mt-1 p-2 w-full border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500"
        />
      </div>
      <div>
        <label for="contactnumber" class="block text-sm font-medium text-gray-700">Contact Number</label>
        <input
          v-model="user.contactnumber"
          id="contactnumber"
          type="text"
          class="mt-1 p-2 w-full border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500"
        />
      </div>
      <div>
        <label for="address" class="block text-sm font-medium text-gray-700">Address</label>
        <input
          v-model="user.address"
          id="address"
          type="text"
          class="mt-1 p-2 w-full border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500"
        />
      </div>
      <div>
        <label for="username" class="block text-sm font-medium text-gray-700">Username</label>
        <input
          v-model="user.username"
          id="username"
          type="text"
          class="mt-1 p-2 w-full border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500"
        />
      </div>
      <div>
        <label for="password" class="block text-sm font-medium text-gray-700">Password</label>
        <input
          v-model="user.password"
          id="password"
          type="password"
          class="mt-1 p-2 w-full border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500"
        />
      </div>
      <div class="flex justify-end space-x-4 mt-4">
        <button
          @click="cancelEdit"
          class="bg-gray-500 text-white px-4 py-2 rounded-lg hover:bg-gray-700"
        >
          Cancel
        </button>
        <button
          @click="saveProfile"
          class="bg-blue-500 text-white px-4 py-2 rounded-lg hover:bg-blue-700"
        >
          Save Changes
        </button>
      </div>
    </div>

    <!-- Profile Display (non-editing mode) -->
    <div v-else class="space-y-4">
      <div class="flex items-center space-x-4">
        <div class="flex-shrink-0 w-24 h-24 bg-gray-300 rounded-full"></div>
        <div>
          <h2 class="text-xl font-semibold">{{ user.firstname }} {{ user.lastname }}</h2>
          <p class="text-gray-500">{{ user.email }}</p>
        </div>
      </div>
      <div>
        <h3 class="font-semibold text-gray-800">Contact Information</h3>
        <p class="text-gray-500">{{ user.contactnumber }}</p>
        <p class="text-gray-500">{{ user.address }}</p>
      </div>
      <div>
        <h3 class="font-semibold text-gray-800">Username</h3>
        <p class="text-gray-500">{{ user.username }}</p>
      </div>
      <div>
        <h3 class="font-semibold text-gray-800">Password</h3>
        <p class="text-gray-500">******</p>
      </div>
    </div>
  </div>
</template>

  
<script>
export default {
  name: 'Profile',
  data() {
    return {
      editing: false,
      user: {
        firstname: 'John',
        lastname: 'Doe',
        email: 'john.doe@example.com',
        contactnumber: '123-456-7890',
        address: '123 Main St, City, Country',
        username: 'johndoe',
        password: '******',
        user_img: '', // You can bind to a URL here
      },
    };
  },
  methods: {
    editProfile() {
      this.editing = true;
    },
    cancelEdit() {
      this.editing = false;
    },
    saveProfile() {
      // Make API call to save changes
      this.editing = false;
      alert('Profile updated!');
    },
  },
};
</script>
  
  <style scoped>
  /* Add component-specific styles here */
  </style>