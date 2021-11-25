var slideout;
window.addEventListener("resize", function () {
  if (window.innerWidth >= 769) {
    document.querySelector(".main").classList.add("remove-push-content");
    if (slideout) slideout.destroy();
  }
  if (window.innerWidth <= 768) {
    document.querySelector(".main").classList.remove("remove-push-content");
    slideout = new Slideout({
      panel: document.querySelector(".main"),
      menu: document.querySelector(".mobileMenu"),
      padding: 250,
      tolerance: 70,
    });
  }
});

if (window.innerWidth <= 768) {
  slideout = new Slideout({
    panel: document.querySelector(".main"),
    menu: document.querySelector(".mobileMenu"),
    padding: 250,
    tolerance: 70,
  });
}

toggleMenu = () => {
  slideout.toggle();
};

// Confirm Delete
confirmDelete = (title) => {
  var agree = confirm(`Are you sure you want to delete ${title}?`);
  if (agree) return true;
  else return false;
};
