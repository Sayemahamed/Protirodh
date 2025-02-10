module.exports = {
  darkMode: 'class', // Use the "class" strategy for dark mode
  content: [
    "./templates/**/*.html",
    "./static/**/*.js",
  ],
  theme: {
    extend: {
      colors: {
        background: "rgb(var(--background))",
        card: "rgb(var(--card))",
        border: "rgb(var(--border))",
        'copy-primary': "rgb(var(--copy-primary))",
        'copy-secondary': "rgb(var(--copy-secondary))",
        cta: "rgb(var(--cta))",
        'cta-active': "rgb(var(--cta-active))",
        'cta-text': "rgb(var(--cta-text))",
        accent: "rgb(var(--accent))",
      },
    },
  },
  plugins: [],
};
