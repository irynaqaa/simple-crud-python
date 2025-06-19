<?php

namespace Application\src\Controller;

use Drupal\Core\Controller\ControllerBase;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\HttpFoundation\Request;

/**
 * Provides a controller for handling voting submissions.
 */
class VotingController extends ControllerBase {

    /**
     * Handles the vote submission.
     *
     * @param string $option
     *   The option that was voted for.
     *
     * @return \Symfony\Component\HttpFoundation\JsonResponse
     *   A JSON response indicating the result of the vote.
     */
    public function submitVote($option) {
        // Here you would typically send the vote to a third-party API.
        // For demonstration, we will just return a success message.

        // Validate the option.
        if (!in_array($option, ['option1', 'option2'])) {
            return new JsonResponse(['message' => 'Invalid option.'], 400);
        }

        // Simulate sending the vote to a third-party API.
        // $response = $this->sendVoteToApi($option);

        // Return a success message.
        return new JsonResponse(['message' => 'Vote submitted successfully for ' . $option . '.']);
    }

    /**
     * Simulates sending the vote to a third-party API.
     *
     * @param string $option
     *   The option that was voted for.
     *
     * @return array
     *   The response from the API.
     */
    private function sendVoteToApi($option) {
        // This function would contain the logic to send the vote to the API.
        // For now, we will return a mock response.
        return ['status' => 'success', 'option' => $option];
    }
}