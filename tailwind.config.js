/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templales/**/*.html", //templales at the project level
    "./**/templates/**/*.html" // templales inside apps level
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}

