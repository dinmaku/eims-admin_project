/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
    "./node_modules/flowbite/**/*.js",
  ],
  theme: {
    extend: {
      fontFamily: {
        raleway: ["Raleway", "sans-serif"],
        dancing: ["DancingScript", "cursive"],
        amaticBold: ["AmaticSC-Bold", "sans-serif"],
        amaticRegular: ["AmaticSC-Regular", "sans-serif"],
        merriweatherRegular: ["Merriweather-Regular", "serif"],
        merriweatherBoldItalic: ["Merriweather-BoldItalic", "serif"],
        quicksand: ["Quicksand", "sans-serif"],
        gothic: ["GothicA1", "sans-serif"],
      },
      scrollBehavior: {
        smooth: 'smooth',
      },
    
    },
  },
  plugins: [
    require("flowbite/plugin"),
],
};
