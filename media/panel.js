(function () {
  const vscode = acquireVsCodeApi();
  const results = document.getElementById('results');
  const buttons = {
    run: document.getElementById('run'),
    submit: document.getElementById('submit'),
    open: document.getElementById('open'),
    reset: document.getElementById('reset'),
    support: document.getElementById('support'),
  };
  const language = document.getElementById('language');

  buttons.run.addEventListener('click', () => vscode.postMessage({ type: 'run', mode: 'sample' }));
  buttons.submit.addEventListener('click', () => vscode.postMessage({ type: 'run', mode: 'submit' }));
  buttons.open.addEventListener('click', () => vscode.postMessage({ type: 'open' }));
  buttons.reset.addEventListener('click', () => vscode.postMessage({ type: 'reset' }));
  if (buttons.support) {
    buttons.support.addEventListener('click', () => vscode.postMessage({ type: 'support' }));
  }
  language.addEventListener('change', () => vscode.postMessage({ type: 'language', language: language.value }));

  // The panel HTML is replaced wholesale on every render, so results posted
  // before this script ran would be lost. Ask for them on load instead.
  vscode.postMessage({ type: 'ready' });

  window.addEventListener('message', (event) => {
    const message = event.data;
    if (message.type === 'results') {
      results.innerHTML = message.html;
      results.classList.remove('running');
      results.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    } else if (message.type === 'editorial') {
      const details = document.getElementById('editorial-details');
      if (details) {
        details.open = true;
        details.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    } else if (message.type === 'running') {
      buttons.run.disabled = message.running;
      buttons.submit.disabled = message.running;
      if (message.running) {
        results.classList.add('running');
        results.innerHTML = '<div class="empty">Running tests…</div>';
      }
    }
  });
})();
