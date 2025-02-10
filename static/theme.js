/* ===================================== */
/*         Theme Management              */
/* ===================================== */

/**
 * Applies the given theme by toggling the 'dark' class on the root element.
 * @param {string} theme - Either "light" or "dark".
 */
function applyTheme(theme) {
  if (theme === 'dark') {
    document.documentElement.classList.add('dark');
  } else {
    document.documentElement.classList.remove('dark');
  }
}

/**
 * Synchronizes the value of theme selectors (if present) with the current theme.
 * @param {string} theme - The theme value ("light" or "dark").
 */
function syncThemeSelectors(theme) {
  const selectors = ['theme-selector', 'mobile-theme-selector'];
  selectors.forEach(id => {
    const selector = document.getElementById(id);
    if (selector) {
      selector.value = theme;
    }
  });
}

/**
 * Initializes the theme on page load using localStorage (defaults to "light" if not set).
 */
function initializeTheme() {
  const savedTheme = localStorage.getItem('theme') || 'light';
  applyTheme(savedTheme);
  syncThemeSelectors(savedTheme);
}

/**
 * Handles theme changes from the selectors.
 * @param {Event} event - The change event from the theme selector.
 */
function handleThemeChange(event) {
  const theme = event.target.value;
  if (!theme) return; // Do nothing if theme is empty

  applyTheme(theme);
  localStorage.setItem('theme', theme);

  // Sync the other theme selector (if it exists)
  const otherSelectorId = event.target.id === 'theme-selector' ? 'mobile-theme-selector' : 'theme-selector';
  const otherSelector = document.getElementById(otherSelectorId);
  if (otherSelector) {
    otherSelector.value = theme;
  }
}

/* ===================================== */
/*          DOMContentLoaded             */
/* ===================================== */
document.addEventListener('DOMContentLoaded', () => {
  // Initialize theme on page load
  initializeTheme();

  // Setup theme selectors
  const themeSelector = document.getElementById('theme-selector');
  const mobileThemeSelector = document.getElementById('mobile-theme-selector');

  if (themeSelector) {
    themeSelector.addEventListener('change', handleThemeChange);
  }
  if (mobileThemeSelector) {
    mobileThemeSelector.addEventListener('change', handleThemeChange);
  }
});
