var gin_search_url = "/gin/?keywords=";
var distillery_search_url = "/distillery/?distillery_name=";
var destination_url = gin_search_url;

$(document).ready(() => {
    openTab(null, "Gin");

    // if the cursor is in the header search bar, bind the enter key to search
    $('#feature-search-field').keyup(e => {
        if(e.which === 13){
            featureSearch(e);
        } else {
            autocomplete();
            //gin_autocomplete();
        }
    });
});

var featureSearch = function(e) {
    // grab the string from the search box
    var inputString = $('#feature-search-field').val();

    // remove punctuation and whitespace, replace spaces with +
    var keywords = inputString.replace(/[^\w\s]/g, "").replace(/\s+/g, "+");

    // make a GET request for the search url
    window.location = destination_url + keywords;

    return false;
}

var gin_autocomplete = function() {
    if ($('#feature-search-field').val().length > 0) {
        var request = $.post('/gin-search/', {
                search_text : $('#feature-search-field').val(),
                csrfmiddlewaretoken : $("input[name=csrfmiddlewaretoken]").val()
            }
        )

        request.done(function(data, textStatus, jqXHR) {
            console.log(data)
            $('#feature-search-results').html(data);
        });
    } else {
        $('#feature-search-results').html();
    }
}

var distillery_autocomplete = function() {

}

var autocomplete = gin_autocomplete;

function openTab(evt, tabName) {
    // Declare all variables
    if (tabName === "Gin") {
        destination_url = gin_search_url;
        $('#Gin.tablinks').css("background-color", "#aaa");
        $('#Distillery.tablinks').css("background-color", $('.tab').css("background-color"));
        autocomplete = gin_autocomplete;
    } else if (tabName === "Distillery") {
        destination_url = distillery_search_url;
        $('#Distillery.tablinks').css("background-color", "#aaa");
        $('#Gin.tablinks').css("background-color", $('.tab').css("background-color"));
        autocomplete = distillery_autocomplete;
    }
}
