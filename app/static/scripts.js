const menuButton = document.getElementById('menu-navbar');
const menuSection = document.getElementById('nav-menu-open');

menuButton.addEventListener('click', function() {
  menuSection.classList.toggle('open');
});