$(document).ready(function() {
    $('.rating_widget').each(function(i, e){

        var average_rating = $(e).find('.average_rating');
        var user_rating = $(e).find('.user_rating');
        var form_rating = $(e).find('.form_rating');

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

var instantRatingClicked = function(value, text, event) {
    if (value === "") {
        value = 0;
    }

    var data = $(event.target).closest('.rating_widget').data()
    var request = $.post('/gin/' + data.gin + '/rate/', {rating: value});

    request.done(function(data, status, jqXHR) {
        if (data === 'unauthenticated') {
            window.location = '/login/';
        } else if (data === 'not rated') {
            alert('An error occurred while rating this gin.')
        }
    });

    request.fail(function(data, status, jqXHR){});
}

var formRatingClicked = function(value, text, event) {
    if (value === "") {
        value = 0;
    }

    $(event.target).closest('.rating_widget').siblings('#id_rating').val(value);
}
