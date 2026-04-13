export function initCurrentYear() {
  const yearNodes = document.querySelectorAll('[data-current-year]');

  yearNodes.forEach((node) => {
    node.textContent = String(new Date().getFullYear());
  });
}
