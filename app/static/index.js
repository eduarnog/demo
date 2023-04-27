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
    window.location.href = "/dashboard";
  });
}

function editNote(noteId, noteData) {
  document.getElementById("note").value = noteData;
  document.getElementById("note-id").value = noteId;
  document.getElementById("add-note-button").style.display = "none";
  document.getElementById("update-note-button").style.display = "block";
}

function deleteNote(noteId) {
  fetch("/delete-note", {
    method: "POST",
    body: JSON.stringify({ noteId: noteId }),
  }).then((_res) => {
    window.location.href = "/dashboard";
  });
}

document.getElementById("update-note-button").addEventListener("click", function() {
  var noteId = document.getElementById("note-id").value;
  var noteData = document.getElementById("note").value;
  fetch("/update-note", {
    method: "POST",
    body: JSON.stringify({ noteId: noteId, noteData: noteData }),
  }).then((_res) => {
    window.location.href = "/dashboard";
  });
});