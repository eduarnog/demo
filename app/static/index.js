const menuButton = document.getElementById('menu-navbar');
const menuSection = document.getElementById('nav-menu-open');

menuButton.addEventListener('click', function() {
  menuSection.classList.toggle('open');
});

function deleteNote(noteId) {
  fetch("/delete-note", {
    method: "POST",
    body: JSON.stringify({ noteId: noteId }),
  }).then((_res) => {
    window.location.href = "/";
  });
}
