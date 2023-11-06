/*
This is recycled code from PP1
*/
const mobileToggleOpen = document.getElementsByClassName("fa-bars")[0];
const mobileToggleClose = document.getElementsByClassName("fa-xmark")[0];
const navBar = document.getElementsByClassName("column-50-mobile")[0];

mobileToggleOpen.addEventListener("click", () => {
    navBar.classList.remove("closed");
  navBar.classList.add("open");
});

mobileToggleClose.addEventListener("click", () => {
    navBar.classList.remove("open");
    navBar.classList.add("closed");
});

/* This will remove the displayed messages after a certain time */
setTimeout(() => {
    const message = document.getElementById("messages");
    if ( message ) {
        message.style.display = 'none';
    }
}, 3000);