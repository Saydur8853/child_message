// Initialize Swiper after all sections are loaded
let swiper;
function initSwiper() {
    swiper = new Swiper('.swiper-container', {
        slidesPerView: 3, // Show 3 items per view
        spaceBetween: 20, // Space between slides
        navigation: {
            nextEl: '.swiper-button-next',
            prevEl: '.swiper-button-prev',
        },
        pagination: {
            el: '.swiper-pagination',
            clickable: true,
        },
        autoplay: {
            delay: 2500, // Delay between slides in milliseconds (2.5 seconds)
            disableOnInteraction: false, // Allow autoplay to continue even if the user interacts with the slider
        },
        breakpoints: {
            // When window width is >= 640px
            640: {
                slidesPerView: 2,
                spaceBetween: 10,
            },
            // When window width is >= 768px
            768: {
                slidesPerView: 3,
                spaceBetween: 20,
            },
            // When window width is >= 1024px
            1024: {
                slidesPerView: 4,
                spaceBetween: 20,
            },
        },
    });
}

let player;
// Initialize YouTube API player
function onYouTubeIframeAPIReady() {
    document.querySelectorAll('.swiper-slide iframe').forEach((iframe, index) => {
        player = new YT.Player(iframe, {
            events: {
                'onStateChange': onPlayerStateChange, // Listen for state changes
            }
        });
    });
}

// Handle video state changes
function onPlayerStateChange(event) {
    if (event.data == YT.PlayerState.PLAYING) {
        // Pause Swiper autoplay when the video starts playing
        swiper.autoplay.stop();
    } else if (event.data == YT.PlayerState.PAUSED || event.data == YT.PlayerState.ENDED) {
        // Resume Swiper autoplay when the video is paused or ended
        swiper.autoplay.start();
    }
}

// Show popup logic
document.addEventListener("DOMContentLoaded", () => {
    const popup = document.getElementById("popup");
    const closePopup = document.getElementById("closePopup");

    // Flag to track if popup has been shown
    let popupShown = false;

    // Display popup only if it hasn't been shown yet
    const showPopup = () => {
        if (!popupShown) {
            popup.classList.remove("hidden");
            popupShown = true; // Mark that the popup has been shown

            // Auto-hide after 5 seconds
            setTimeout(() => {
                popup.classList.add("hidden");
            }, 5000);
        } else {
            popup.style.display = "none";
        }
    };

    // Close popup on button click
    closePopup.addEventListener("click", () => {
        popup.classList.add("hidden");
        popupShown = true; // Mark that the popup has been shown
    });

    // Show the popup initially
    showPopup();

    // Initialize Swiper after content is loaded
    window.addEventListener('load', () => {
        initSwiper();
    });
});
