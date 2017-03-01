$(document).ready(() => {
    $('#header-search-button').click(headerSearch);

    // if the cursor is in the header search bar, bind the enter key to search
    $('#header-search-field').keypress(e => {
        if(e.which === 13){
            headerSearch(e);
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
