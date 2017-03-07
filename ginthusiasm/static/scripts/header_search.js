$(document).ready(() => {
    $('#header-search-button').click(headerSearch);

    /*$('.header-search').focusout(e => {
        $('#header-search-results').hide()
    });
    $('.header-search').focusin(e => {
        $('#header-search-results').show()
    });*/

    // if the cursor is in the header search bar, bind the enter key to search
    $('#header-search-field').keyup(e => {
        if(e.which === 13){
            headerSearch(e);
        } else {
            var request = $.post('/gin-search/', {
                    search_text : $('#header-search-field').val(),
                    csrfmiddlewaretoken : $("input[name=csrfmiddlewaretoken]").val()
                }
            )

            request.done(function(data, textStatus, jqXHR) {
                console.log(data)
                $('#header-search-results').html(data);

            });
        }
    });
});

var headerSearch = function(e) {
    // grab the string from the search box
    var inputString = $('#header-search-field').val();

    // remove punctuation and whitespace, replace spaces with +
    var keywords = inputString.replace(/[^\w\s]/g, "").replace(/\s+/g, "+");

    // make a GET request for the search url
    window.location = "/gin/?keywords=" + keywords;

    return false;
}
