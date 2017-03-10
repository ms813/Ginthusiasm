$(document).ready(() => {

    let input = $('#header-search-field');
    let results = $('#header-search-results');

    //do the search when the search button is pressed
    $('#header-search-button').click(e => {
        headerSearch(e, input.val());
    });

    //if the search box is un-focused, hide the autocomplete results after a short delay
    input.blur(e => {
        setTimeout(() => {
            results.hide()
        }, 2000);
    });

    //show the autocomplete results when the search box is focused
    input.focus(e => {
        results.show();
    });

    // if the cursor is in the header search bar, bind the enter key to search
    input.keyup(e => {
        if (e.which === 13) {
            // 13 is the keycode for enter
            headerSearch(e);
        } else {
            let request = $.post('/gin-search/', {
                    search_text: input.val(),
                    //csrfmiddlewaretoken : $("input[name=csrfmiddlewaretoken]").val()
                }
            );

            request.done((data, textStatus, jqXHR) => {
                results.html(data);
            });
        }
    });
});

const headerSearch = function (e, inputString) {

    // remove punctuation and whitespace, replace spaces with +
    let keywords = inputString.replace(/[^\w\s]/g, "").replace(/\s+/g, "+");

    // make a GET request for the search url
    window.location = "/gin/?keywords=" + keywords;

    //prevent the <a> tag from being followed
    return false;
};
