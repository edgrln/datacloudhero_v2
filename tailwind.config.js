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
  // Styles raw markdown-rendered HTML (article/page content - see
  // CLAUDE.md) that has no classes of its own to hook utilities onto.
  // Scoped via the `prose`/`prose-lg` utility classes in article.html/
  // page.html specifically, not applied globally - everything else
  // (category/tag/author/archives/index) is hand-authored template
  // markup with its own component classes already, not raw content.
  plugins: [require('@tailwindcss/typography')],
};
