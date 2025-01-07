<template>
  <div class= "ml-10 mt-5 text-start">
    <h1 class="font-amaticBold font-bold text-4xl pb-1">Welcome, Admin</h1>
    <p class="font-amaticRegular font-bold text-gray-400">Check your latest updates</p>
    <hr class="w-[1100px] mt-2">
  </div>
  
    <!--Information Cards-->
      <div class="py-10 pl-10 flex flex-row space-x-10">
        <div class = "flex">
          <VCalendar 
            :attributes="attrs"
                />
          
      </div>
      <div class=""> <!-- Add padding to the dashboard -->
      <div class="border border-gray-300 rounded-lg shadow-lg p-4" style="height: 280px; width: 450px;">
        <apexchart 
          type="bar" 
          :options="barChartOptions" 
          :series="barChartSeries" 
        />
      </div>
    </div>
      <div class = "flex flex-col space-y-2">
      <router-link to = "/manage-events">
    <div class="border border-gray-300 w-80 h-32 rounded-lg bg-blue-100 flex flex-col justify-start items-start pt-2 pl-4 shadow-lg">
      <img class="w-[48px] h-[48px] mb-0" src="/img/events-booked-w.png">
      <h2 class="font-quicksand text-3xl font-bold">7</h2>
      <p class="font-quicksand text-sm text-gray-500 font-bold">No. Wishlist </p>
    </div>
      </router-link>
      <router-link to = "/manage-users">
    <div class="border border-gray-300 w-80 h-32 rounded-lg bg-blue-100 flex flex-col justify-start items-start pt-2 pl-4 shadow-md">
      <img class="w-[48px] h-[48px] mb-0" src="/img/vendor.png">
      <h2 class="font-quicksand text-3xl font-bold">45</h2>
      <p class="font-quicksand text-sm text-gray-500 font-bold">No. Suppliers </p>
    </div>
    </router-link>
  </div>
  
  
  </div>
  
  
  
  <!--Team's Progress -->
  <div class="flex space-x-10">
  <div class="max-w-sm w-full bg-white-200 border border-gray-300 rounded-lg shadow-xl dark:bg-blue-200 p-4 md:p-6 ml-10 mb-5">
    <div class="flex justify-between mb-5 ml-5">
      <div class="flex items-center">
        <div class="flex justify-center items-center">
          <h5 class="text-xl font-bold leading-none text-gray-900 dark:text-white pe-1">Your team's progress</h5>
          <svg data-popover-target="chart-info" data-popover-placement="bottom" class="w-3.5 h-3.5 text-gray-500 dark:text-gray-400 hover:text-gray-900 dark:hover:text-white cursor-pointer ms-1" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 20">
            <path d="M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5Zm0 16a1.5 1.5 0 1 1 0-3 1.5 1.5 0 0 1 0 3Zm1-5.034V12a1 1 0 0 1-2 0v-1.418a1 1 0 0 1 1.038-.999 1.436 1.436 0 0 0 1.488-1.441 1.501 1.501 0 1 0-3-.116.986.986 0 0 1-1.037.961 1 1 0 0 1-.96-1.037A3.5 3.5 0 1 1 11 11.466Z"/>
          </svg>
        </div>
      </div>
    </div>
  
    <div class="bg-gray-50 dark:bg-gray-700 p-3 rounded-lg">
      <div class="grid grid-cols-3 gap-3 mb-2">
        <dl class="bg-orange-50 dark:bg-gray-600 rounded-lg flex flex-col items-center justify-center h-[78px]">
          <dt class="w-8 h-8 rounded-full bg-orange-100 dark:bg-gray-500 text-orange-600 dark:text-orange-300 text-sm font-medium flex items-center justify-center mb-1">12</dt>
          <dd class="text-orange-600 dark:text-orange-300 text-sm font-medium">Pending</dd>
        </dl>
        <dl class="bg-teal-50 dark:bg-gray-600 rounded-lg flex flex-col items-center justify-center h-[78px]">
          <dt class="w-8 h-8 rounded-full bg-teal-100 dark:bg-gray-500 text-teal-600 dark:text-teal-300 text-sm font-medium flex items-center justify-center mb-1">23</dt>
          <dd class="text-teal-600 dark:text-teal-300 text-sm font-medium">In progress</dd>
        </dl>
        <dl class="bg-blue-50 dark:bg-gray-600 rounded-lg flex flex-col items-center justify-center h-[78px]">
          <dt class="w-8 h-8 rounded-full bg-blue-100 dark:bg-gray-500 text-blue-600 dark:text-blue-300 text-sm font-medium flex items-center justify-center mb-1">64</dt>
          <dd class="text-blue-600 dark:text-blue-300 text-sm font-medium">Done</dd>
        </dl>
      </div>
      <div>
      <button @click="toggleDetails" type="button" class="hover:underline text-xs text-gray-500 dark:text-gray-400 font-medium inline-flex items-center">
        Show more details
        <svg class="w-2 h-2 ms-1" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 10 6">
          <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m1 1 4 4 4-4"/>
        </svg>
      </button>
      <div v-if="isDetailsVisible" class="border-gray-200 border-t dark:border-gray-600 pt-3 mt-3 space-y-2">
        <dl class="flex items-center justify-between">
          <dt class="text-gray-500 dark:text-gray-400 text-sm font-normal">Average task completion rate:</dt>
          <dd class="bg-green-100 text-green-800 text-xs font-medium inline-flex items-center px-2.5 py-1 rounded-md dark:bg-green-900 dark:text-green-300">
            <svg class="w-2.5 h-2.5 me-1.5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 10 14">
              <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13V1m0 0L1 5m4-4 4 4"/>
            </svg> 57%
          </dd>
        </dl>
        <dl class="flex items-center justify-between">
          <dt class="text-gray-500 dark:text-gray-400 text-sm font-normal">Days until sprint ends:</dt>
          <dd class="bg-gray-100 text-gray-800 text-xs font-medium inline-flex items-center px-2.5 py-1 rounded-md dark:bg-gray-600 dark:text-gray-300">13 days</dd>
        </dl>
        <dl class="flex items-center justify-between">
          <dt class="text-gray-500 dark:text-gray-400 text-sm font-normal">Next meeting:</dt>
          <dd class="bg-gray-100 text-gray-800 text-xs font-medium inline-flex items-center px-2.5 py-1 rounded-md dark:bg-gray-600 dark:text-gray-300">Thursday</dd>
        </dl>
      </div>
    </div>
    </div>
  
    <!-- Radial Chart -->
    <div class="py-6" id="radial-chart"></div>
    <div class="grid grid-cols-1 items-center border-gray-200 border-t dark:border-gray-700 justify-between">
      <div class="flex justify-between items-center pt-5">
        <!-- Button -->
        <a
          href="#"
          class="uppercase text-sm font-semibold inline-flex items-center rounded-lg text-blue-600 hover:text-blue-700 dark:hover:text-blue-500  hover:bg-gray-100 dark:hover:bg-gray-700 dark:focus:ring-gray-700 dark:border-gray-700 px-3 py-2">
          Progress report
          <svg class="w-2.5 h-2.5 ms-1.5 rtl:rotate-180" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 6 10">
            <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m1 9 4-4 4-4"/>
          </svg>
        </a>
      </div>
    </div>
  </div>
  
    
  <!---Events per Month Line Graph-->
  
  <div class="relative flex flex-col rounded-xl bg-white bg-clip-border text-gray-700 shadow-lg border border-gray-300 h-[330px] w-[680px]">
      <div class="relative mx-48 mt-4 flex flex-col gap-1 overflow-hidden rounded-none bg-transparent bg-clip-border text-gray-700 shadow-none md:flex-row md:items-center">
        <div>
          <h6 class="block font-sans text-base font-semibold leading-relaxed tracking-normal text-blue-gray-900 antialiased">
            Events Booked in 2024
          </h6>
          <p class="block max-w-sm font-sans text-sm font-normal leading-normal text-gray-700 antialiased">
          This are the successful events per Month
          </p>
        </div>
      </div>
      <div class="pt-0 px-2 pb-0 h-full">
        <div ref="lineChart"></div>
      </div>
    </div>
  
  
  </div>

   <div class="flex justify-center items-center w-full px-10 py-8">
    <div class="card w-full bg-white shadow-lg rounded-lg p-6">
        <h2 class="text-2xl font-bold mb-4 text-gray-800">Event Statistics</h2>
        <Chart type="line" :data="areaChartData" :options="areaChartOptions" class="h-[38rem] w-full" />
    </div>
   </div>
  
  
  
  
  
    </template>
    
    <script>
  import ApexCharts from 'apexcharts';
  import { defineComponent, onMounted, onUnmounted, ref } from 'vue';
  import VueApexCharts from "vue3-apexcharts";
  import axios from 'axios';
  
  export default defineComponent({
    name: 'Dashboard',
    components: {
      apexchart: VueApexCharts,
    },
    data() {
      return {
        isDetailsVisible: false,
        attrs: [
          {
            key: 'today',
            highlight: 'red',
            dates: new Date(),
          },
        ],
  
        //Line chart configs
        barChartOptions: {
          chart: {
            type: 'bar',
             toolbar: {
                show: false,
                  },
          },
          plotOptions: {
              bar: {
                  columnWidth: '40%',
                  borderRadius: 2,
               },
           },
    dataLabels: {
      enabled: false, // Disable data labels
    },
          xaxis: {
            categories: [1, 2, 3, 4, 5], // Ratings
          },
          yaxis: {
            title: {
              text: 'No of users',
              style: {
              fontSize: '12px',
              fontWeight: 'bold',
              fontFamily: 'inherit',
            },
            },
          },
          title: {
            text: 'Feedback Ratings',
            align: 'center',
            style: {
              fontSize: '18px',
              fontWeight: 'bold',
              fontFamily: 'inherit',
        
            },
          },
        },
        barChartSeries: [
          {
            name: 'Number of People',
            data: [2, 6, 14, 21, 24], // Number of people for each rating
          },
        ],
      };
    },
    methods: {
      toggleDetails() {
        this.isDetailsVisible = !this.isDetailsVisible;
      },
      
    },
    setup() {
      const date = ref(new Date());
      const isDatePickerDisabled = ref(false);
      const isDetailsVisible = ref(false);
      const selectedMonth = ref(null);
      const pollingInterval = ref(null);
      
      // Area Chart Data
      const areaChartData = ref({
        labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
        datasets: []
      });

      const colors = {
        'Wedding': { border: '#42A5F5', background: 'rgba(66, 165, 245, 0.2)' },
        'Birthday': { border: '#66BB6A', background: 'rgba(102, 187, 106, 0.2)' },
        'Christening': { border: '#FFA726', background: 'rgba(255, 167, 38, 0.2)' },
        'Anniversary': { border: '#EC407A', background: 'rgba(236, 64, 122, 0.2)' },
        'Corporate': { border: '#AB47BC', background: 'rgba(171, 71, 188, 0.2)' }
      };

      const getRandomColor = () => {
        const letters = '0123456789ABCDEF';
        let color = '#';
        for (let i = 0; i < 6; i++) {
          color += letters[Math.floor(Math.random() * 16)];
        }
        return {
          border: color,
          background: color.replace(')', ', 0.2)')
        };
      };

      const fetchEventsByMonth = async () => {
        try {
          const response = await axios.get('http://localhost:5000/api/events-by-month');
          const { eventTypes, data } = response.data;
          
          // Create a dataset for each event type
          const newDatasets = eventTypes.map(type => {
            // Use existing color if available, otherwise generate new one
            const color = colors[type] || getRandomColor();
            return {
              label: type,
              data: data[type],
              fill: true,
              borderColor: color.border,
              tension: 0.4,
              backgroundColor: color.background,
              hidden: false
            };
          });

          // Update datasets while preserving animations
          areaChartData.value.datasets = newDatasets;
        } catch (error) {
          console.error('Error fetching events by month:', error);
        }
      };

      const startPolling = () => {
        // Poll every 30 seconds
        pollingInterval.value = setInterval(fetchEventsByMonth, 30000);
      };

      const stopPolling = () => {
        if (pollingInterval.value) {
          clearInterval(pollingInterval.value);
          pollingInterval.value = null;
        }
      };

      onMounted(() => {
        fetchEventsByMonth();
        startPolling();
        const chartConfig = {
          series: [
            {
              name: "Sales",
              data: [50, 40, 65, 29, 89, 53, 23, 70, 67],
            },
          ],
          chart: {
            type: "line",
            height: 240,
            toolbar: {
              show: false,
            },
          },
          title: {
            show: "",
          },
          dataLabels: {
            enabled: false,
          },
          colors: ["#020617"],
          plotOptions: {
            bar: {
              columnWidth: "40%",
              borderRadius: 2,
            },
          },
          xaxis: {
            axisTicks: {
              show: false,
            },
            axisBorder: {
              show: false,
            },
            labels: {
              style: {
                colors: "#616161",
                fontSize: "12px",
                fontFamily: "inherit",
                fontWeight: 400,
              },
            },
            categories: [
              "Apr",
              "May",
              "Jun",
              "Jul",
              "Aug",
              "Sep",
              "Oct",
              "Nov",
              "Dec",
            ],
          },
          yaxis: {
            labels: {
              style: {
                colors: "#616161",
                fontSize: "12px",
                fontFamily: "inherit",
                fontWeight: 400,
              },
            },
          },
          grid: {
            show: true,
            borderColor: "#dddddd",
            strokeDashArray: 5,
            xaxis: {
              lines: {
                show: true,
              },
            },
            padding: {
              top: 5,
              right: 20,
            },
          },
          fill: {
            opacity: 0.8,
          },
          tooltip: {
            theme: "dark",
          },
        };
  
        const chart = new ApexCharts(lineChart.value, chartConfig);
        chart.render();
      });

      onUnmounted(() => {
        stopPolling();
      });

      const lineChart = ref(null);

      // Line Chart Options with click interaction
      const areaChartOptions = ref({
        plugins: {
          legend: {
            labels: {
              color: '#495057'
            }
          },
          tooltip: {
            mode: 'index',
            intersect: false
          }
        },
        scales: {
          x: {
            ticks: {
              color: '#495057',
              callback: function(value, index) {
                const month = areaChartData.value.labels[index];
                const isSelected = selectedMonth.value === index;
                return isSelected ? ' ' + month : month;
              }
            },
            grid: {
              color: '#ebedef'
            }
          },
          y: {
            ticks: {
              color: '#495057'
            },
            grid: {
              color: '#ebedef'
            }
          }
        },
        onClick: (event, elements) => {
          if (elements.length > 0) {
            const clickedIndex = elements[0].index;
            selectedMonth.value = selectedMonth.value === clickedIndex ? null : clickedIndex;
            updateChartData(clickedIndex);
          }
        },
        hover: {
          mode: 'index',
          intersect: false
        }
      });

      const updateChartData = (monthIndex) => {
        if (selectedMonth.value === null) {
          // Show all months
          areaChartData.value.datasets.forEach(dataset => {
            dataset.hidden = false;
          });
        } else {
          // Show only selected month's data
          const selectedData = {};
          areaChartData.value.datasets.forEach(dataset => {
            selectedData[dataset.label] = dataset.data[monthIndex];
          });

          // Update datasets to show only selected month
          areaChartData.value.datasets.forEach(dataset => {
            const value = selectedData[dataset.label];
            dataset.data = Array(12).fill(null);
            dataset.data[monthIndex] = value;
          });
        }
      };

      return {
        date,
        isDatePickerDisabled,
        isDetailsVisible,
        areaChartData,
        areaChartOptions,
        selectedMonth,
        lineChart
      };
    }
  });
  
    </script>
    
    <style scoped>
     html {
      scroll-behavior: smooth;
    }
  
  
    </style>