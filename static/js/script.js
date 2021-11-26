// Sliding menu bar
var slideout;
window.addEventListener("resize", function () {
  if (window.innerWidth >= 769) {
    //destory slideout menu when windows is greater than 769px
    document.querySelector(".main").classList.add("remove-push-content");
    if (slideout) slideout.destroy();
  }
  if (window.innerWidth <= 768) {
    //re-init slideout menu when windows is smaller than 769px
    document.querySelector(".main").classList.remove("remove-push-content");
    slideout = new Slideout({
      panel: document.querySelector(".main"),
      menu: document.querySelector(".mobileMenu"),
      padding: 250,
      tolerance: 70,
      touch: false,
    });
  }
});
//init slideout menu when it is smaller than 768px when website is loaded in.
if (window.innerWidth <= 768) {
  slideout = new Slideout({
    panel: document.querySelector(".main"),
    menu: document.querySelector(".mobileMenu"),
    padding: 250,
    tolerance: 70,
    touch: false,
  });
}
// toggle menu click
toggleMenu = () => {
  slideout.toggle();
};

// Confirm Delete
confirmDelete = (title) => {
  var agree = confirm(`Are you sure you want to delete ${title}?`);
  if (agree) return true;
  else return false;
};
//remove message after certain time
var alertBox = document.getElementById("alertBox");
setTimeout(function () {
  alertBox.style.display = "none";
}, 5000);
