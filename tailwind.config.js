/** @type {import('tailwindcss').Config} */
module.exports = {
  // landing.html is included too - harmless, Tailwind only scans for class
  // name strings here to decide what utilities to keep, it doesn't affect
  // landing's own separate Play-CDN runtime (see CLAUDE.md).
  content: ["./themes/mytheme/templates/**/*.html"],
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        accent: {
          DEFAULT: '#1bab53',
          hover: '#159647',
        },
      },
    },
  },
  plugins: [],
};
