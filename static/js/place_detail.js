document.querySelectorAll('.thumbnail-image').forEach((thumbnail) => {
    thumbnail.addEventListener('click', function () {
        const imageUrl = this.getAttribute('data-image-url');
        fetch(imageUrl)
            .then(response => response.json())
            .then(data => {
                const largeImageUrl = data.image_url;
                $('#largeImageModal .modal-body').html(
                    `<img src="${largeImageUrl}" alt="Large Image">`);
                $('#largeImageModal').modal('show');
            })
            .catch(error => {
                console.error('Error:', error);
            });
    });
});