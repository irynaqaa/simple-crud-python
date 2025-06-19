(function ($, Drupal) {
    'use strict';

    Drupal.behaviors.votingBehavior = {
        attach: function (context, settings) {
            $('.upvote-button', context).once('voting').on('click', function () {
                // AJAX call to send upvote.
                $.ajax({
                    url: '/voting/upvote',
                    type: 'POST',
                    success: function (response) {
                        alert(response.message);
                    }
                });
            });

            $('.downvote-button', context).once('voting').on('click', function () {
                // AJAX call to send downvote.
                $.ajax({
                    url: '/voting/downvote',
                    type: 'POST',
                    success: function (response) {
                        alert(response.message);
                    }
                });
            });
        }
    };
})(jQuery, Drupal);
