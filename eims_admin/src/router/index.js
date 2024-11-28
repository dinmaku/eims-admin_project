import { createRouter, createWebHistory } from 'vue-router';
import AdminLogin from '@/components/admin-login.vue';
import AdminDashboard from '../pages/dashboard.vue';
import Home from '../pages/home.vue';
import Profile from '../pages/profile.vue';
import ManageEvents from '../pages/manage-events.vue';
import Settings from '../pages/settings.vue';
import ManageOutfits from '../pages/manage-outfits.vue';
import ManageUsers from '../pages/manage-users.vue';
import UploadGallery from '../pages/upload-gallery.vue';
import CreateEvent from '../pages/create-event.vue';
import WeddingForm from '../pages/wedding-form.vue';
import BirthdayForm from '../pages/birthday-form.vue';
import DebutForm from '../pages/debut-form.vue';
import EventCalendar from '../pages/event-calendar.vue';
import Invoice from '../pages/invoice.vue';
import AddServices from '../pages/add-services.vue'

const routes = [
  {
    name: 'AdminLogin',
    path: '/',
    component: AdminLogin
  },
  {
    path: '/dashboard',
    component: AdminDashboard, 
    children: [
      {
        path: '',
        component: Home
      },
      {
        name: 'Profile',
        path: '/profile',
        component: Profile
      },
      {
        name: 'ManageEvents',
        path: '/manage-events',
        component: ManageEvents
      },
      {
        name: 'EventCalendar',
        path: '/event-calendar',
        component: EventCalendar
      },
      {
        name: 'ManageOutfits',
        path: '/manage-outfits',
        component: ManageOutfits
      },
      {
        name: 'ManageUsers',
        path: '/manage-users', 
        component: ManageUsers
      },
      {
        name: 'UploadGallery',
        path: '/upload-gallery', 
        component: UploadGallery
      },
      {
        name: 'Settings',
        path: '/settings',
        component: Settings
      },
      {
        name: 'CreateEvent',
        path: '/create-event',
        component: CreateEvent,
        props: true,
        children: [
           {
             path: '/wedding-form',
             component: WeddingForm,
           },
           {
            path: '/birthday-form',
            component: BirthdayForm,
          },
          {
            path: '/debut-form',
            component: DebutForm,
          },
          

        ],
      },
      {
        name: 'Invoice',
        path: '/invoice',
        component: Invoice,
        props: true,     
      
      },
      {
        name: 'AddServices',
        path: '/add-services',
        component: AddServices,
        props: true,     
      
      },
    ],
  }
  // You can add additional routes here if needed
];


const router = Router();
export default router;
function Router() {
  const router = createRouter({
    history: createWebHistory(),
    routes,
  });
  return router;
}

router.beforeEach((to, from, next) => {
  document.title = to.meta.title || 'RedCarpet Admin';
  next();
});