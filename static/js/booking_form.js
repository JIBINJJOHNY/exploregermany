document.addEventListener("DOMContentLoaded", function () {
    const noOfGuestsField = document.querySelector("#id_no_of_guests");
    const maxGuests = 6;

    noOfGuestsField.addEventListener("input", function () {
        const enteredGuests = parseInt(noOfGuestsField.value);
        if (enteredGuests > maxGuests) {
            noOfGuestsField.value = maxGuests;
            alert("Maximum number of guests is 6");
        }
    });
});