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
        copyPrimary: "rgb(var(--copy-primary))",
        copySecondary: "rgb(var(--copy-secondary))",
        cta: "rgb(var(--cta))",
        ctaActive: "rgb(var(--cta-active))",
        ctaText: "rgb(var(--cta-text))",
        accent: "rgb(var(--accent))",
      },
    },
  },
  plugins: [],
};
