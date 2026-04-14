export function initHeroCarousel() {
  const track = document.getElementById('heroTrack');
  const prevBtn = document.getElementById('heroPrev');
  const nextBtn = document.getElementById('heroNext');
  const dots = Array.from(document.querySelectorAll('[data-hero]'));

  if (!track || !prevBtn || !nextBtn || dots.length === 0) return;

  const slideCount = dots.length;
  let current = 0;
  let autoPlayId = null;
  let isScrolling = false;

  // --- Navigation ---

  const goTo = (index) => {
    current = (index + slideCount) % slideCount;
    const slideWidth = track.offsetWidth;

    isScrolling = true;
    track.scrollTo({ left: current * slideWidth, behavior: 'smooth' });

    dots.forEach((dot, i) => {
      const active = i === current;
      dot.classList.toggle('is-active', active);
      dot.setAttribute('aria-selected', String(active));
    });
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
    const slideWidth = track.offsetWidth;
    const snapped = Math.round(track.scrollLeft / slideWidth);
    if (snapped !== current) {
      current = snapped;
      dots.forEach((dot, i) => {
        const active = i === current;
        dot.classList.toggle('is-active', active);
        dot.setAttribute('aria-selected', String(active));
      });
      startAutoPlay();
    }
    isScrolling = false;
  };

  track.addEventListener('scrollend', syncDots, { passive: true });

  // Fallback for browsers without scrollend (Safari < 16.4)
  let scrollTimer = null;
  track.addEventListener('scroll', () => {
    clearTimeout(scrollTimer);
    scrollTimer = setTimeout(syncDots, 80);
  }, { passive: true });

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

  document.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowLeft')  { goTo(current - 1); startAutoPlay(); }
    if (e.key === 'ArrowRight') { goTo(current + 1); startAutoPlay(); }
  });

  // --- Resize: re-snap to current slide without animation ---

  const resizeObserver = new ResizeObserver(() => {
    track.scrollTo({ left: current * track.offsetWidth, behavior: 'instant' });
  });
  resizeObserver.observe(track);

  // --- Init ---

  track.scrollTo({ left: 0, behavior: 'instant' });
  startAutoPlay();
}
