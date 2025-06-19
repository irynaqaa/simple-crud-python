<?php

namespace Application\src\Block;

use Drupal\Core\Block\BlockBase;
use Drupal\Core\Cache\CacheableMetadata;
use GuzzleHttp\Client;
use GuzzleHttp\Exception\GuzzleException;

/**
 * Provides a 'API Credentials' Block.
 *
 * @Block(
 *   id = "api_credentials_block",
 *   admin_label = @Translation("API Credentials Block"),
 * )
 */
class ApiCredentialsBlock extends BlockBase {

    /**
     * {@inheritdoc}
     */
    public function build() {
        // Retrieve API credentials from the configuration.
        $config = \Drupal::config('custom_voting_module.settings');
        $api_key = $config->get('api_key');
        $api_secret = $config->get('api_secret');
        $api_url = $config->get('api_url');

        // Initialize Guzzle client.
        $client = new Client();

        try {
            // Make the API call to fetch user data.
            $response = $client->request('GET', $api_url, [
                'auth' => [$api_key, $api_secret],
            ]);

            // Check if the response is successful.
            if ($response->getStatusCode() === 200) {
                $data = json_decode($response->getBody(), TRUE);
                // Prepare user data for rendering.
                $user_data = [
                    'username' => $data['username'] ?? 'N/A',
                    'email' => $data['email'] ?? 'N/A',
                    'description' => $data['description'] ?? 'N/A',
                ];
            } else {
                $user_data = [
                    'error' => 'Failed to fetch user data. Status code: ' . $response->getStatusCode(),
                ];
            }
        } catch (GuzzleException $e) {
            // Handle any errors during the API call.
            $user_data = [
                'error' => 'API call failed: ' . $e->getMessage(),
            ];
        }

        // Build the render array for the block.
        return [
            '#theme' => 'api_credentials_block',
            '#user_data' => $user_data ?? [],
            '#cache' => [
                'max-age' => 0,
            ],
        ];
    }

    /**
     * {@inheritdoc}
     */
    public function getCacheTags() {
        return CacheableMetadata::createFromRenderArray($this->build())->getCacheTags();
    }

    /**
     * {@inheritdoc}
     */
    public function getCacheContexts() {
        return ['url'];
    }
}