<?php

namespace Drupal\my_module\Controller;

use Drupal\Core\Controller\ControllerBase;
use Symfony\Component\HttpFoundation\JsonResponse;

/**
 * Class VotingController.
 *
 * Provides a controller for handling voting actions.
 */
class VotingController extends ControllerBase {

    /**
     * Handles the voting action.
     *
     * @param string $vote
     *   The vote type (upvote or downvote).
     *
     * @return \Symfony\Component\HttpFoundation\JsonResponse
     *   Returns a JSON response with the result of the vote.
     */
    public function vote($vote) {
        // Logic to send the vote to the third-party API.
        // Example API call (replace with actual API logic).
        $response = [
            'status' => 'success',
            'message' => 'Vote recorded successfully.',
        ];

        return new JsonResponse($response);
    }
}
