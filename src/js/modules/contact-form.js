// Web3Forms — получить ключ на https://web3forms.com (бесплатно)
const ACCESS_KEY = 'TUTAJ_WSTAW_KLUCZ_WEB3FORMS';

export function initContactForm() {
  const form = document.querySelector('.contact-form');
  if (!form) return;

  const submitBtn = form.querySelector('.contact-form__submit');
  const statusEl = document.getElementById('form-status');

  const setState = (state) => {
    form.dataset.state = state;
    submitBtn.disabled = state === 'loading';

    if (state === 'loading') {
      submitBtn.textContent = 'Wysyłanie…';
    } else if (state === 'success') {
      submitBtn.textContent = 'Wyślij zapytanie';
    } else {
      submitBtn.textContent = 'Wyślij zapytanie';
    }
  };

  form.addEventListener('submit', async (e) => {
    e.preventDefault();

    setState('loading');
    statusEl.hidden = true;
    statusEl.className = 'form-status';

    const data = new FormData(form);
    data.append('access_key', ACCESS_KEY);
    data.append('subject', 'Nowe zapytanie — DMSolutions');
    data.append('from_name', 'DMSolutions strona');

    try {
      const res = await fetch('https://api.web3forms.com/submit', {
        method: 'POST',
        body: data,
      });
      const json = await res.json();

      if (json.success) {
        setState('success');
        statusEl.textContent = 'Dziękujemy! Odezwiemy się wkrótce.';
        statusEl.className = 'form-status form-status--success';
        statusEl.hidden = false;
        form.reset();
      } else {
        throw new Error(json.message || 'Błąd serwera');
      }
    } catch {
      setState('error');
      statusEl.textContent = 'Coś poszło nie tak. Zadzwoń do nas lub napisz bezpośrednio na e-mail.';
      statusEl.className = 'form-status form-status--error';
      statusEl.hidden = false;
    }
  });
}
