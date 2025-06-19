<?php

namespace Application\src\Controller;

use Drupal\Core\Controller\ControllerBase;
use Drupal\Core\Access\AccessResult;
use Symfony\Component\DependencyInjection\ContainerInterface;
use GuzzleHttp\Client;
use GuzzleHttp\Exception\GuzzleException;

class VotingResultsController extends ControllerBase {

    /**
     * Returns a renderable array for the voting results page.
     */
    public function results() {
        // Fetch voting results from the third-party API.
        $results = $this->getVotingResults();

        return [
            '#theme' => 'voting_results',
            '#results' => $results,
        ];
    }

    /**
     * Checks access for the voting results page.
     */
    public function access() {
        return AccessResult::allowedIfHasPermission(
            $this->currentUser()->getRoles(),
            'administer site configuration'
        );
    }

    /**
     * Fetch voting results from the third-party API.
     */
    private function getVotingResults() {
        // Retrieve API credentials from the configuration.
        $config = \Drupal::config('custom_voting_module.settings');
        $api_key = $config->get('api_key');
        $api_secret = $config->get('api_secret');
        $api_url = $config->get('api_url');

        // Initialize Guzzle client.
        $client = new Client();

        try {
            // Make the API call to fetch voting results.
            $response = $client->request('GET', $api_url, [
                'auth' => [$api_key, $api_secret],
            ]);

            // Check if the response is successful.
            if ($response->getStatusCode() === 200) {
                $data = json_decode($response->getBody(), TRUE);
                // Format the results for display.
                return $this->formatResults($data);
            } else {
                return [
                    'error' => 'Failed to fetch voting results. Status code: ' . $response->getStatusCode(),
                ];
            }
        } catch (GuzzleException $e) {
            // Handle any errors during the API call.
            return [
                'error' => 'API call failed: ' . $e->getMessage(),
            ];
        }
    }

    /**
     * Format the voting results for display.
     *
     * @param array $data
     *   The raw data from the API.
     *
     * @return array
     *   The formatted results.
     */
    private function formatResults(array $data) {
        $formatted_results = [];

        // Loop through the data and format it.
        foreach ($data as $item) {
            $formatted_results[] = [
                'candidate' => $item['candidate_name'] ?? 'Unknown',
                'votes' => $item['vote_count'] ?? 0,
            ];
        }

        return $formatted_results;
    }
}