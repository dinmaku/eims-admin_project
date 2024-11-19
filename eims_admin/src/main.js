import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import router from './router';
import { setupCalendar, Calendar, DatePicker } from 'v-calendar';

import 'v-calendar/style.css';


const app = createApp(App)
app.use(router)
app.mount('#app');

app.use(setupCalendar, {})

app.component('VCalendar', Calendar)
app.component('VDatepicker', DatePicker)
