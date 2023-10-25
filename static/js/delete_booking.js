$(".delete-booking").click(function () {
    if (confirm("Are you sure you want to delete this booking?")) {
        // User clicked OK, proceed with the deletion
        const bookingId = $(this).data("id");
        console.log(`Deleting booking with ID: ${bookingId}`);

        // Send the DELETE request via AJAX and handle the response
        $.ajax({
            url: `/delete-booking/${bookingId}/`, // Make sure the URL is correct
            type: "DELETE",
            success: function (data) {
                if (data.message === "Booking deleted successfully") {
                    // Remove the deleted booking from the UI
                    listItem.remove();

                    // Check if there are no more bookings and display a message
                    if ($("ul").find("li").length === 0) {
                        $("ul").append("<li>No bookings available.</li>");
                    }
                }
            },
        });
    }
});