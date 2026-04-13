export function initHeroCarousel() {
  const track = document.getElementById('heroTrack');
  const prevButton = document.getElementById('heroPrev');
  const nextButton = document.getElementById('heroNext');
  const dots = Array.from(document.querySelectorAll('[data-hero]'));

  if (!track || !prevButton || !nextButton || dots.length === 0) {
    return;
  }

  const slideCount = dots.length;
  let currentIndex = 0;
  let autoPlayId = null;
  let touchStartX = 0;

  const setSlide = (index) => {
    currentIndex = (index + slideCount) % slideCount;
    track.style.transform = `translateX(-${currentIndex * 100}%)`;

    dots.forEach((dot, dotIndex) => {
      const isActive = dotIndex === currentIndex;
      dot.classList.toggle('is-active', isActive);
      dot.setAttribute('aria-selected', String(isActive));
    });
  };

  const stopAutoPlay = () => {
    if (autoPlayId) {
      window.clearInterval(autoPlayId);
      autoPlayId = null;
    }
  };

  const startAutoPlay = () => {
    stopAutoPlay();
    autoPlayId = window.setInterval(() => {
      setSlide(currentIndex + 1);
    }, 5000);
  };

  prevButton.addEventListener('click', () => {
    setSlide(currentIndex - 1);
    startAutoPlay();
  });

  nextButton.addEventListener('click', () => {
    setSlide(currentIndex + 1);
    startAutoPlay();
  });

  dots.forEach((dot) => {
    dot.addEventListener('click', () => {
      setSlide(Number(dot.dataset.hero));
      startAutoPlay();
    });
  });

  track.addEventListener(
    'touchstart',
    (event) => {
      touchStartX = event.touches[0].clientX;
    },
    { passive: true }
  );

  track.addEventListener(
    'touchend',
    (event) => {
      const deltaX = event.changedTouches[0].clientX - touchStartX;

      if (Math.abs(deltaX) > 50) {
        setSlide(deltaX < 0 ? currentIndex + 1 : currentIndex - 1);
        startAutoPlay();
      }
    },
    { passive: true }
  );

  track.addEventListener('mouseenter', stopAutoPlay);
  track.addEventListener('mouseleave', startAutoPlay);

  document.addEventListener('keydown', (event) => {
    if (event.key === 'ArrowLeft') {
      setSlide(currentIndex - 1);
      startAutoPlay();
    }

    if (event.key === 'ArrowRight') {
      setSlide(currentIndex + 1);
      startAutoPlay();
    }
  });

  setSlide(0);
  startAutoPlay();
}
