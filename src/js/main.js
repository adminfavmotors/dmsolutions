import '../styles/main.css';

import { initCurrentYear } from './modules/current-year.js';
import { initHeroCarousel } from './modules/hero-carousel.js';
import { initMobileNav } from './modules/mobile-nav.js';

function initApp() {
  initCurrentYear();
  initMobileNav();
  initHeroCarousel();
}

initApp();
