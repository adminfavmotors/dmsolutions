export function initHeroCarousel() {
  const carousel = document.querySelector('.hero__carousel');
  const track = document.getElementById('heroTrack');
  const prevBtn = document.getElementById('heroPrev');
  const nextBtn = document.getElementById('heroNext');
  const dots = Array.from(document.querySelectorAll('[data-hero]'));

  if (!carousel || !track || !prevBtn || !nextBtn || dots.length === 0) return;

  const slideCount = dots.length;
  let current = 0;
  let autoPlayId = null;
  let syncTimer = null;
  let isProgrammaticScroll = false;

  // --- Navigation ---

  const prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)');
  const supportsScrollEnd = 'onscrollend' in window;

  const scrollBehavior = () => prefersReduced.matches ? 'instant' : 'smooth';

  const updateDots = () => {
    dots.forEach((dot, i) => {
      const active = i === current;
      dot.classList.toggle('is-active', active);
      dot.setAttribute('aria-selected', String(active));
    });
  };

  const scheduleProgrammaticUnlock = () => {
    clearTimeout(syncTimer);
    syncTimer = setTimeout(() => {
      isProgrammaticScroll = false;
    }, prefersReduced.matches ? 0 : 450);
  };

  const goTo = (index) => {
    const next = (index + slideCount) % slideCount;
    const wrapsAcrossTrack = Math.abs(next - current) > 1;
    const slideWidth = track.offsetWidth;
    const behavior = wrapsAcrossTrack ? 'instant' : scrollBehavior();

    current = next;
    updateDots();
    isProgrammaticScroll = true;
    track.scrollTo({ left: current * slideWidth, behavior });

    if (behavior === 'instant') {
      isProgrammaticScroll = false;
      return;
    }

    scheduleProgrammaticUnlock();
  };

  // --- Autoplay ---

  const stopAutoPlay = () => {
    if (autoPlayId) { clearInterval(autoPlayId); autoPlayId = null; }
  };

  const startAutoPlay = () => {
    stopAutoPlay();
    autoPlayId = setInterval(() => goTo(current + 1), 5000);
  };

  // --- Sync dots after native scroll (swipe on mobile) ---

  const syncDots = () => {
    if (isProgrammaticScroll) return;

    const slideWidth = track.offsetWidth;
    const snapped = Math.round(track.scrollLeft / slideWidth);
    if (snapped !== current) {
      current = snapped;
      updateDots();
      startAutoPlay();
    }
  };

  if (supportsScrollEnd) {
    track.addEventListener('scrollend', syncDots, { passive: true });
  } else {
    // Fallback for browsers without scrollend (Safari < 16.4)
    track.addEventListener('scroll', () => {
      clearTimeout(syncTimer);
      syncTimer = setTimeout(syncDots, 80);
    }, { passive: true });
  }

  // --- Controls ---

  prevBtn.addEventListener('click', () => { goTo(current - 1); startAutoPlay(); });
  nextBtn.addEventListener('click', () => { goTo(current + 1); startAutoPlay(); });
  dots.forEach((dot) => {
    dot.addEventListener('click', () => { goTo(Number(dot.dataset.hero)); startAutoPlay(); });
  });

  // --- Pause on hover ---

  track.addEventListener('mouseenter', stopAutoPlay);
  track.addEventListener('mouseleave', startAutoPlay);

  // --- Keyboard ---

  carousel.addEventListener('keydown', (e) => {
    if (e.key !== 'ArrowLeft' && e.key !== 'ArrowRight') return;

    e.preventDefault();

    if (e.key === 'ArrowLeft') {
      goTo(current - 1);
    } else {
      goTo(current + 1);
    }

    startAutoPlay();
  });

  // --- Resize: re-snap to current slide without animation ---

  const resizeObserver = new ResizeObserver(() => {
    isProgrammaticScroll = false;
    track.scrollTo({ left: current * track.offsetWidth, behavior: 'instant' });
  });
  resizeObserver.observe(track);

  // --- Init ---

  track.scrollTo({ left: 0, behavior: 'instant' });
  updateDots();
  if (!prefersReduced.matches) startAutoPlay();
}
