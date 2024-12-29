// Function to open the modal
function openModal(heading) {
    document.getElementById("modalHeading").innerText = heading; // Update the heading
    document.getElementById("myModal").classList.remove("hidden"); // Show the modal
  }
  
  // Function to close the modal
  function closeModal() {
    document.getElementById("myModal").classList.add("hidden"); // Hide the modal
  }
  
  // Close the modal if the user clicks outside the modal content
  document.getElementById("myModal").addEventListener("click", function(event) {
    if (event.target === this) {
      closeModal(); // Close the modal if the background (overlay) is clicked
    }
  });
  
  // Optional: Handle form submission
  document.getElementById("childJournalistForm").addEventListener("submit", function(event) {
    event.preventDefault();
    // Handle form submission logic here
    alert("Form submitted!");
    closeModal(); // Close the modal after submission
  });
  