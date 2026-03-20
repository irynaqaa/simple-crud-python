$(document).ready(function() {
    $('#editForm').on('submit', function(event) {
        event.preventDefault();
        
        const userId = $('#user_id').val();
        const email = $('#email').val();
        
        $.ajax({
            type: 'POST',
            url: '/editAction',
            data: JSON.stringify({ user_id: userId, email: email }),
            contentType: 'application/json',
            success: function(response) {
                $('#message').text('Success: ' + response.message).css('color', 'green');
            },
            error: function(xhr) {
                const errorMessage = xhr.responseJSON ? xhr.responseJSON.message : 'An error occurred';
                $('#message').text('Error: ' + errorMessage).css('color', 'red');
            }
        });
    });
});