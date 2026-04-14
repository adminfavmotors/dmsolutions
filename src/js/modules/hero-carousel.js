export function initHeroCarousel() {
  const track = document.getElementById('heroTrack');
  const prevBtn = document.getElementById('heroPrev');
  const nextBtn = document.getElementById('heroNext');
  const dots = Array.from(document.querySelectorAll('[data-hero]'));

  if (!track || !prevBtn || !nextBtn || dots.length === 0) return;

  const slideCount = dots.length;
  let current = 0;
  let autoPlayId = null;

  // Touch drag state
  let dragStartX = 0;
  let dragDelta = 0;
  let isDragging = false;

  // --- Core ---

  const goTo = (index) => {
    current = (index + slideCount) % slideCount;
    track.style.transition = 'transform 500ms cubic-bezier(0.4, 0, 0.2, 1)';
    track.style.transform = `translateX(-${current * 100}%)`;
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

  // --- Controls ---

  prevBtn.addEventListener('click', () => { goTo(current - 1); startAutoPlay(); });
  nextBtn.addEventListener('click', () => { goTo(current + 1); startAutoPlay(); });
  dots.forEach((dot) => {
    dot.addEventListener('click', () => { goTo(Number(dot.dataset.hero)); startAutoPlay(); });
  });

  // --- Touch drag (live feedback while swiping) ---

  track.addEventListener('touchstart', (e) => {
    dragStartX = e.touches[0].clientX;
    dragDelta = 0;
    isDragging = true;
    track.style.transition = 'none';
  }, { passive: true });

  track.addEventListener('touchmove', (e) => {
    if (!isDragging) return;
    dragDelta = e.touches[0].clientX - dragStartX;
    const base = -(current * 100);
    const offset = (dragDelta / track.offsetWidth) * 100;
    track.style.transform = `translateX(calc(${base}% + ${dragDelta}px))`;
  }, { passive: true });

  track.addEventListener('touchend', () => {
    if (!isDragging) return;
    isDragging = false;
    const threshold = track.offsetWidth * 0.2;
    if (dragDelta < -threshold) goTo(current + 1);
    else if (dragDelta > threshold) goTo(current - 1);
    else goTo(current); // snap back
    startAutoPlay();
  }, { passive: true });

  // --- Pause on hover ---

  track.addEventListener('mouseenter', stopAutoPlay);
  track.addEventListener('mouseleave', startAutoPlay);

  // --- Keyboard ---

  document.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowLeft')  { goTo(current - 1); startAutoPlay(); }
    if (e.key === 'ArrowRight') { goTo(current + 1); startAutoPlay(); }
  });

  // --- Init ---

  goTo(0);
  startAutoPlay();
}
