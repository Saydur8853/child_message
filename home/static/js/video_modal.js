// Function to open the video modal with the provided video URL
function openVideoModal(videoUrl) {
    var modal = document.getElementById('videoModal');
    var videoSource = document.getElementById('modalVideoSource');
    var modalVideo = document.getElementById('modalVideo');
    
    // Set the video URL in the modal
    videoSource.src = videoUrl;
    modalVideo.load(); // Reload the video to apply the new source

    // Show the modal
    modal.classList.remove('hidden');
}

// Function to close the video modal
function closeVideoModal() {
    var modal = document.getElementById('videoModal');
    modal.classList.add('hidden');

    // Stop the video when closing the modal
    var modalVideo = document.getElementById('modalVideo');
    modalVideo.pause();
    modalVideo.currentTime = 0; // Reset video to the beginning
}
