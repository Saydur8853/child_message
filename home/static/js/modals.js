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
  $('#childForm').submit(function(event) {
    event.preventDefault(); // Prevent default form submission
    var formData = $(this).serialize(); // Serialize form data
    
    $.ajax({
        url: '{% url "home" %}',  // URL to send the form data to
        method: 'POST',
        data: formData,
        success: function(response) {
            if (response.success) {
                alert('Form submitted successfully!');
            } else {
                alert('Form submission failed!');
            }
        },
        error: function() {
            alert('An error occurred.');
        }
    });
});
