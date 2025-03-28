$(document).ready(function() {
    // Ensure the CSRF token is included in all AJAX requests
    $.ajaxSetup({
        headers: {
            'X-CSRFToken': $("input[name=csrfmiddlewaretoken]").val()  // Get CSRF token from the form
        }
    });

    $(document).on('click', '.pagination a', function(e) {
        e.preventDefault();  // Prevent default link behavior
        var page = $(this).attr('href').split('page=')[1];
        // alert(page)
        $.ajax({
            url: "/projects/paginate/",  // URL pointing to your Django view
            type: "POST",
            data: { page: page, csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val() },  
            success: function (response) {
                $("#project-container").html(response);  // Update content
            },
            error: function (xhr) {
                console.error(xhr.responseText);
            }
        });
    }); 
})
