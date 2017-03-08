// magic.js
$(document).ready(function() {

  $('#add_review').on('submit', function(event){
    event.preventDefault();
    console.log("form submitted!")  // sanity check
    create_review();

  });

  // AJAX for posting
  function create_review() {
      console.log("create post is working!") // sanity check

      var formData = $("#add_review").serializeArray()

      $.ajax({
          url : '', // the endpoint
          type : "POST", // http method
          data : formData, // data sent with the post request

          // handle a successful response
          success : function(json) {
              console.log(json); // log the returned json to the console
              console.log("success"); // another sanity check
          },

          // handle a non-successful response
          error : function(xhr,errmsg,err) {
              $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                  " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
              console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
          }
      });
  };

});
