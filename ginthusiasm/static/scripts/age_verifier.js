
function verify_age() {

    var legalDrinkingAge = 18;
    var latestValidDOB = new Date(); //defaults to today
    latestValidDOB.setYear(latestValidDOB.getYear() - legalDrinkingAge)

    // Get the user's inputted DOB
    var dob = new Date($('#dob').val());
    if((latestValidDOB - dob) > 0) {
        // Allow user to use site if of legal drinking age
        setCookie('verified', 'True', 365);
        $('#age-overlay').remove()
    }
    else {
        // User is under the legal drinking age, so redirect
        window.location = 'http://www.google.com'
        return false
    }
}

// Based on https://www.w3schools.com/js/js_cookies.asp
function setCookie(cookieName, cookieValue, expiryDays) {
    var date = new Date();
    var millisecondsInSingleDay = 24 * 60 * 60 * 1000;
    // Ensure cookie is valid for specified number of days
    date.setTime(date.getTime() + (expiryDays * millisecondsInSingleDay))
    // Converts date time to a string
    var expires = "expires="+date.toUTCString();
    document.cookie = cookieName + "=" + cookieValue + ";" + expires + ";path=/";
}
