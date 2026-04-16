import Splide from '@splidejs/splide';

export function initHeroCarousel() {
  const el = document.querySelector('.hero__carousel');
  if (!el) return;

  new Splide(el, {
    type: 'loop',
    autoplay: true,
    interval: 5000,
    pauseOnHover: true,
    resetProgress: false,
    speed: 600,
    reducedMotion: {
      speed: 0,
      rewindSpeed: 0,
      autoplay: 'pause',
    },
    i18n: {
      prev: 'Poprzedni slajd',
      next: 'Następny slajd',
      slideX: 'Slajd %s',
      pageX: 'Strona %s',
    },
  }).mount();
}
