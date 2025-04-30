document.addEventListener('DOMContentLoaded', () => {
    const burger = document.querySelector('.burger');
    const navWrapper = document.querySelector('.nav-wrapper');

    burger.addEventListener('click', () => {
      burger.classList.toggle('active');
      navWrapper.classList.toggle('active');
    });

    // Для удобства - закрываем меню при клике на ссылку
    document.querySelectorAll('.nav-link').forEach(link => {
      link.addEventListener('click', () => {
        burger.classList.remove('active');
        navWrapper.classList.remove('active');
      });
    });
  });

  // Эффект шапки при скролле
  window.addEventListener('scroll', () => {
    const header = document.querySelector('.header');
    if (window.scrollY > 50) {
      header.style.backgroundColor = 'rgba(255, 255, 255, 0.95)';
      header.style.boxShadow = 'var(--shadow-md)';
    } else {
      header.style.backgroundColor = 'var(--white)';
      header.style.boxShadow = 'var(--shadow-sm)';
    }
  });