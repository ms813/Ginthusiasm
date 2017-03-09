// magic.js
$(document).ready(function() {

  $('#add_review').on('submit', function(event){
    event.preventDefault();
    console.log("form submitted!")
    create_review();

  });

  // AJAX for posting
  function create_review() {
      console.log("create post is working!")

      var formData = $("#add_review").serializeArray()

      $.ajax({
          url : '', // the endpoint
          type : "POST", // http method
          data : formData, // data sent with the post request

          // handle a successful response
          success : function(json) {
              console.log(json); // log the returned json to the console
              console.log("success"); // another sanity check
              $("#add_review").slideUp(function(){
                $("#thanks").slideDown();
              });

          },

          // handle a non-successful response
          error : function(xhr,errmsg,err) {
              $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                  " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
              console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
          }
      });
  };

  var x = document.getElementById("demo");
  function getLocation() {
      if (navigator.geolocation) {
          navigator.geolocation.getCurrentPosition(showPosition);
      } else {
          x.innerHTML = "Geolocation is not supported by this browser.";
      }
  }
  function showPosition(position) {
      x.innerHTML = "Latitude: " + position.coords.latitude +
      "<br>Longitude: " + position.coords.longitude;
  }

});
