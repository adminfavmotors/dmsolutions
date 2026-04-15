import '../styles/main.css';

import { initCurrentYear } from './modules/current-year.js';
import { initHeroCarousel } from './modules/hero-carousel.js';
import { initMobileNav } from './modules/mobile-nav.js';
import { initContactForm } from './modules/contact-form.js';

function initApp() {
  initCurrentYear();
  initMobileNav();
  initHeroCarousel();
  initContactForm();
}

initApp();
