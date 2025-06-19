<?php

namespace Application\src\Controller;

use Drupal\Core\Controller\ControllerBase;

class ArticleResultsController extends ControllerBase {

    /**
     * Builds the article results page.
     *
     * @return array
     *   A render array for the article results page.
     */
    public function results() {
        return [
            '#markup' => $this->t('Article results will be displayed here.'),
        ];
    }
}