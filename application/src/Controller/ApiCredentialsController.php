<?php

namespace Application\src\Controller;

use Drupal\Core\Controller\ControllerBase;

class ApiCredentialsController extends ControllerBase {

    /**
     * Builds the API Credentials page.
     *
     * @return array
     *   A render array for the API credentials page.
     */
    public function build() {
        return [
            '#theme' => 'api_credentials_block',
            '#user_data' => [], // This will be populated with actual data.
        ];
    }
}