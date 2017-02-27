// see https://docs.djangoproject.com/en/dev/ref/csrf/
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        var csrftoken = Cookies.get('csrftoken');
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
