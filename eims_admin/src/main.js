import { createApp } from 'vue';
import './style.css'
import App from './App.vue'
import router from './router';
import { setupCalendar, Calendar, DatePicker } from 'v-calendar';
import PrimeVue from 'primevue/config';
import Chart from 'primevue/chart';
import 'primeicons/primeicons.css';

import 'v-calendar/style.css';

const app = createApp(App);
app.use(router);
app.use(PrimeVue);
app.use(setupCalendar, {});
app.component('Chart', Chart);

app.component('VCalendar', Calendar);
app.component('VDatePicker', DatePicker);

app.mount('#app');
