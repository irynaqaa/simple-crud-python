<?php

namespace Application\src\Block;

use Drupal\Core\Block\BlockBase;
use Drupal\Core\Cache\CacheableMetadata;
use GuzzleHttp\Client;
use GuzzleHttp\Exception\GuzzleException;

/**
 * Provides a 'Voting' Block.
 *
 * @Block(
 *   id = "voting_block",
 *   admin_label = @Translation("Voting Block"),
 * )
 */
class VotingBlock extends BlockBase {

    /**
     * {@inheritdoc}
     */
    public function build() {
        // Initialize Guzzle client.
        $client = new Client();

        // Retrieve API credentials from the configuration.
        $config = $this->getConfiguration();
        $api_key = $config['api_key'] ?? '';
        $api_secret = $config['api_secret'] ?? '';
        $api_url = $config['api_url'] ?? '';

        try {
            // Make the API call to fetch voting results.
            $response = $client->request('GET', $api_url, [
                'auth' => [$api_key, $api_secret],
            ]);

            // Check if the response is successful.
            if ($response->getStatusCode() === 200) {
                $data = json_decode($response->getBody(), TRUE);
                // Format the results for display.
                $formatted_results = $this->formatResults($data);
            } else {
                $formatted_results = [
                    'error' => 'Failed to fetch voting results. Status code: ' . $response->getStatusCode(),
                ];
            }
        } catch (GuzzleException $e) {
            // Handle any errors during the API call.
            $formatted_results = [
                'error' => 'API call failed: ' . $e->getMessage(),
            ];
        }

        // Build the render array for the block.
        return [
            '#theme' => 'voting_results',
            '#results' => $formatted_results ?? [],
            '#cache' => [
                'max-age' => 0,
            ],
        ];
    }

    /**
     * Format the voting results for display.
     */
    private function formatResults(array $data) {
        // TODO: Implement the logic to format the results.
        return $data;
    }
}