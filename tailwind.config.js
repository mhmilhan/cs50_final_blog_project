/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.html',
    './static/css/**/*.css',  // For general public-facing CSS
    // Add paths to other apps or locations if necessary
  ],
  theme: {
    extend: {
        colors: {
        primary: '#007BFF',
        secondary: '#6C757D',
      },
    },
  },
  plugins: [],
}
