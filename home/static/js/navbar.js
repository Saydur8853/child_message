// Get references to elements
const topAd = document.getElementById('top-advertisement');
const navbar = document.getElementById('navbar');
const menuToggle = document.getElementById('menu-toggle');
const menuClose = document.getElementById('menu-close');
const menuDrawer = document.getElementById('menu-drawer');
const menuOverlay = document.getElementById('menu-overlay');

// Function to handle scroll events
function handleScroll() {
    const scrollY = window.scrollY; // Get the current scroll position
    if (scrollY > topAd.offsetHeight) {
        navbar.classList.add('fixed');
        topAd.style.display = 'none justify-center'; // Hide top advertisement
    } else {
        navbar.classList.remove('fixed');
        topAd.style.display = 'block justify-center'; // Show top advertisement
    }
}

// Function to adjust drawer position
function adjustDrawerPosition() {
    const navbarHeight = navbar.offsetHeight;
    menuDrawer.style.top = `${navbarHeight}px`;
}

// Close drawer
const closeDrawer = () => {
    menuDrawer.classList.add('translate-x-full');
    menuOverlay.classList.add('hidden');
};

// Event listener for opening the drawer
menuToggle?.addEventListener('click', (e) => {
    e.stopPropagation(); // Prevent triggering closeDrawer on menuToggle click
    menuDrawer.classList.remove('translate-x-full');
    menuOverlay.classList.remove('hidden');
});

// Event listener for closing the drawer
menuClose?.addEventListener('click', closeDrawer);
menuOverlay?.addEventListener('click', closeDrawer);

// Close drawer when clicking anywhere outside the drawer
document.addEventListener('click', (e) => {
    const isClickInsideDrawer = menuDrawer.contains(e.target) || menuToggle.contains(e.target);
    if (!isClickInsideDrawer) {
        closeDrawer();
    }
});

// Close drawer when resizing screen to a larger size
window.addEventListener('resize', () => {
    adjustDrawerPosition();
    if (window.innerWidth > 768) { // Replace 768 with your breakpoint
        closeDrawer();
    }
});

// Initial setup on load and scroll
window.addEventListener('load', () => {
    handleScroll();
    adjustDrawerPosition();
});
window.addEventListener('scroll', () => {
    handleScroll();
    adjustDrawerPosition();
});
