//JavaScript for handling the clicks and making the Ajax request
document.querySelectorAll('.thumbnail-image').forEach((thumbnail) => {
    thumbnail.addEventListener('click', function () {
        // Get the data-image-url attribute (URL to fetch the large image)
        const imageUrl = this.getAttribute('data-image-url');

        // Make an Ajax request to get the large image
        fetch(imageUrl)
            .then(response => response.json()) // Parse the response as JSON
            .then(data => {
                const largeImageUrl = data.image_url; // Extract the URL from the response
                // Display the large image in the Bootstrap modal
                $('#largeImageModal .modal-body').html(
                    `<img src="${largeImageUrl}" alt="Large Image">`);
                $('#largeImageModal').modal('show');
            })
            .catch(error => {
                console.error('Error:', error);
            });
    });
});