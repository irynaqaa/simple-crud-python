(function ($, Drupal) {
    'use strict';

    Drupal.behaviors.votingBehavior = {
        attach: function (context, settings) {
            // Add your JavaScript logic for voting here.
            $('form.voting-form', context).once('votingBehavior').on('submit', function (e) {
                e.preventDefault();
                // Handle the voting submission.
                var selectedOption = $(this).find('input[name="vote_option"]:checked').val();
                if (selectedOption) {
                    // Make an AJAX call to submit the vote.
                    $.ajax({
                        url: '/voting/submit',
                        type: 'POST',
                        data: { option: selectedOption },
                        success: function (response) {
                            // Handle success response.
                            alert(response.message);
                        },
                        error: function (xhr) {
                            // Handle error response.
                            alert('Error: ' + xhr.responseText);
                        }
                    });
                } else {
                    alert('Please select an option to vote.');
                }
            });
        }
    };
})(jQuery, Drupal);