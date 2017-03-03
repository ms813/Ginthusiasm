$(document).ready(function() {
    $('.rating_widget').each(function(i, e){

        var average_rating = $(e).find('.average_rating');
        var user_rating = $(e).find('.user_rating');

        average_rating.barrating({
            theme: 'fontawesome-stars-o',
            initialRating: average_rating.data('rating'),
            readonly: true,
        });

        user_rating.barrating({
            theme: 'fontawesome-stars-o',
            initialRating: user_rating.data('rating'),
            onSelect: ratingClicked,
        });
    });
});

var ratingClicked = function(value, text, event) {
    if (value === "") {
        value = 0;
    }

    var data = $(event.target).closest('.rating_widget').data()
    var request = $.post('/gin/' + data.gin + '/rate/', {rating: value});

    request.done(function(data, status, jqXHR) {
        if (data === 'unauthenticated') {
            window.location = '/login/';
        }
    });

    request.fail(function(data, status, jqXHR){});
}
