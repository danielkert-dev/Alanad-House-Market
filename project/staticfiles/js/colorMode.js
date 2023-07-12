function applyTheme() {
    const theme = localStorage.getItem('theme');
    const bodyElement = document.querySelector('body');
  
    if (theme === 'dark') {
      bodyElement.classList.remove('light-theme');
      bodyElement.classList.add('dark-theme');
    } else if (theme === 'light') {
      bodyElement.classList.remove('dark-theme');
      bodyElement.classList.add('light-theme');
    }
  }
  
  function toggleTheme() {
    const theme = localStorage.getItem('theme');
    const updatedTheme = theme === 'dark' ? 'light' : 'dark';
    localStorage.setItem('theme', updatedTheme);
    applyTheme();
  }
  
  // Set initial theme
  document.addEventListener('DOMContentLoaded', applyTheme);

