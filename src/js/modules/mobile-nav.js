export function initMobileNav() {
  const desktopNavMediaQuery = window.matchMedia('(min-width: 56.25rem)');
  const toggle = document.querySelector('.menu-toggle');
  const panel = document.querySelector('.nav-panel');
  const links = document.querySelectorAll('.nav-panel a');

  if (!toggle || !panel) {
    return;
  }

  const setExpanded = (value) => {
    toggle.setAttribute('aria-expanded', String(value));
    document.body.classList.toggle('menu-open', value);
  };

  toggle.addEventListener('click', () => {
    const nextState = toggle.getAttribute('aria-expanded') !== 'true';
    setExpanded(nextState);
  });

  links.forEach((link) => {
    link.addEventListener('click', () => {
      setExpanded(false);
    });
  });

  const closeMenuOnDesktop = () => {
    if (desktopNavMediaQuery.matches) {
      setExpanded(false);
    }
  };

  if (typeof desktopNavMediaQuery.addEventListener === 'function') {
    desktopNavMediaQuery.addEventListener('change', closeMenuOnDesktop);
  } else {
    desktopNavMediaQuery.addListener(closeMenuOnDesktop);
  }

  closeMenuOnDesktop();
}
