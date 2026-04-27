export function initHeroCarousel() {
  const carousel = document.querySelector('.hero__carousel');
  const track = document.getElementById('heroTrack');
  const prevBtn = document.getElementById('heroPrev');
  const nextBtn = document.getElementById('heroNext');
  const dots = Array.from(document.querySelectorAll('[data-hero]'));

  if (!carousel || !track || !prevBtn || !nextBtn || dots.length === 0) return;

  const slideCount = dots.length;

  // --- Infinite loop: clone last slide before first, clone first slide after last ---
  // Track layout: [clone-last | slide-1 | slide-2 | slide-3 | clone-first]
  // Real slides sit at track indices 1..slideCount (OFFSET = 1)

  const realSlides = Array.from(track.children);

  const lastClone = realSlides[slideCount - 1].cloneNode(true);
  const firstClone = realSlides[0].cloneNode(true);
  lastClone.setAttribute('aria-hidden', 'true');
  firstClone.setAttribute('aria-hidden', 'true');

  track.insertBefore(lastClone, realSlides[0]);
  track.appendChild(firstClone);

  const OFFSET = 1; // real slides start at track index OFFSET

  let current = 0; // real index 0‥slideCount-1
  let autoPlayId = null;
  let debounceTimer = null;
  let isProgrammaticScroll = false;

  // --- Helpers ---

  const prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)');
  const supportsScrollEnd = 'onscrollend' in window;
  const scrollBehavior = () => (prefersReduced.matches ? 'instant' : 'smooth');

  const updateDots = () => {
    dots.forEach((dot, i) => {
      const active = i === current;
      dot.classList.toggle('is-active', active);
      dot.setAttribute('aria-selected', String(active));
    });
  };

  // --- Navigation ---

  const goTo = (realIndex) => {
    const next = ((realIndex % slideCount) + slideCount) % slideCount;
    const behavior = scrollBehavior();

    // For wrap-around with animation: scroll through the clone so the
    // transition looks continuous. With instant behavior go directly to
    // the real slide — there is no animation to smooth anyway.
    let trackIndex = next + OFFSET;
    if (behavior !== 'instant') {
      if (current === slideCount - 1 && next === 0) {
        trackIndex = slideCount + OFFSET; // animate into clone-first at end
      } else if (current === 0 && next === slideCount - 1) {
        trackIndex = 0; // animate into clone-last at beginning
      }
    }

    current = next;
    updateDots();
    isProgrammaticScroll = true;
    track.scrollTo({ left: trackIndex * track.offsetWidth, behavior });
  };

  // --- Sync after scroll settles (native swipe or end of programmatic scroll) ---

  const syncAfterScroll = () => {
    const slideWidth = track.offsetWidth;
    const trackIndex = Math.round(track.scrollLeft / slideWidth);

    // Arrived at clone-last (index 0) → silently jump to real last slide
    if (trackIndex === 0) {
      track.scrollTo({ left: slideCount * slideWidth, behavior: 'instant' });
      isProgrammaticScroll = false;
      return;
    }

    // Arrived at clone-first (index slideCount + OFFSET) → silently jump to real first
    if (trackIndex === slideCount + OFFSET) {
      track.scrollTo({ left: OFFSET * slideWidth, behavior: 'instant' });
      isProgrammaticScroll = false;
      return;
    }

    // Programmatic scroll to a real slide — already handled by goTo
    if (isProgrammaticScroll) {
      isProgrammaticScroll = false;
      return;
    }

    // Native swipe landed on a real slide
    const realIndex = trackIndex - OFFSET;
    if (realIndex >= 0 && realIndex < slideCount && realIndex !== current) {
      current = realIndex;
      updateDots();
      startAutoPlay();
    }
  };

  if (supportsScrollEnd) {
    track.addEventListener('scrollend', syncAfterScroll, { passive: true });
  } else {
    // Fallback for Safari < 16.4
    track.addEventListener('scroll', () => {
      clearTimeout(debounceTimer);
      debounceTimer = setTimeout(syncAfterScroll, 80);
    }, { passive: true });
  }

  // --- Autoplay ---

  const stopAutoPlay = () => {
    if (autoPlayId) { clearInterval(autoPlayId); autoPlayId = null; }
  };

  const startAutoPlay = () => {
    stopAutoPlay();
    autoPlayId = setInterval(() => goTo(current + 1), 5000);
  };

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
    if (e.key === 'ArrowLeft') goTo(current - 1);
    else goTo(current + 1);
    startAutoPlay();
  });

  // --- Resize: re-snap current real slide without animation ---

  const resizeObserver = new ResizeObserver(() => {
    isProgrammaticScroll = false;
    track.scrollTo({ left: (current + OFFSET) * track.offsetWidth, behavior: 'instant' });
  });
  resizeObserver.observe(track);

  // --- Init ---

  track.scrollTo({ left: OFFSET * track.offsetWidth, behavior: 'instant' });
  updateDots();
  if (!prefersReduced.matches) startAutoPlay();
}
