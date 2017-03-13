$(document).ready(function () {
    $('#add-review-btn').on('click', create_review);
    $('#location-btn').on('click', getLocation);
});

var create_review = function (event) {
    //console.log("create post is working!") // sanity check
    event.preventDefault();

    var formData = $("#add_review").serializeArray()

    //check that the rating is set to either the default value or the clicked value
    var rating = -1;
    var ratingIndex = -1;
    for (var i = 0; i < formData.length; i++) {
        if (formData[i].name === "rating") {
            rating = formData[i].value;
            ratingIndex = i;
        }
    }

    //get the number of stars in the widget when the page was loaded
    var initialRating = $('.rating_widget').find('.form_rating').data('rating')

    //if the current rating is 0, set the rating to the default
    if (rating == 0) {
        formData[ratingIndex].value = initialRating;
    }

    var request = $.post('review/', formData);

    request.done(function (data, status, jqXHR) {
        console.log(data);
        $("#add_review").slideUp(function () {
            $("#thanks").slideDown();
        });
    });

    request.fail(function (data, status, jqXHR) {
        // add the error to the dom
        $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: " + data +
            " <a href='#' class='close'>&times;</a></div>");

        // provide a bit more info about the error to the console
        console.log(data.status + ": " + data.responseText);
    });
};

var getLocation = function (e) {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function (pos) {
            $('#id_lat').val(pos.coords.latitude);
            $('#id_lng').val(pos.coords.longitude);
            $('#id_postcode').val("");
        });
    } else {
        console.log("Geolocation is not supported by this browser.");
    }
};
