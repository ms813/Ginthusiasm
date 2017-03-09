$(document).ready(function() {
    $('.rating_widget').each(function(i, e){

        var average_rating = $(e).find('.average_rating');
        var user_rating = $(e).find('.user_rating');
        var form_rating = $(e).find('.form_rating');

        // Initialise the star rating widgets
        average_rating.barrating({
            theme: 'fontawesome-stars-o',
            initialRating: average_rating.data('rating'),
            readonly: true,
        });

        user_rating.barrating({
            theme: 'fontawesome-stars-o',
            initialRating: user_rating.data('rating'),
            onSelect: instantRatingClicked,
        });

        form_rating.barrating({
            theme: 'fontawesome-stars-o',
            initialRating: form_rating.data('rating'),
            onSelect: formRatingClicked,
        })
    });
});

// Submit a rating when clicking on the instant rating widget
var instantRatingClicked = function(value, text, event) {
    if (value === "") {
        value = 0;
    }

    var data = $(event.target).closest('.rating_widget').data()
    var request = $.post('/gin/' + data.gin + '/rate/', {rating: value});
    var message = $(event.target).closest('.rating').children('.message')

    request.done(function(data, status, jqXHR) {
        if (data === 'unauthenticated') {
            window.location = '/login/';
        } else if (data === 'rated') {
            displayMessage(message, "Thank you for rating!");

        } else if (data === 'not rated') {
            displayMessage(message, "An error occurred while rating this gin.")
        }
    });

    request.fail(function(data, status, jqXHR){});
}

var displayMessage = function(destination, message) {
    destination.fadeIn(1000);
    destination.html(message);

    window.setTimeout(function() {
        destination.fadeOut(1000);
    },3000);
}

// Set the value of the rating input on the form when clicking a form rating widget
var formRatingClicked = function(value, text, event) {
    if (value === "") {
        value = 0;
    }

    $(event.target).closest('.rating_widget').siblings('#id_rating').val(value);
}
