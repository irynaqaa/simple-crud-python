<?php

/**
 * Implements hook_preprocess_HOOK() for article templates.
 *
 * @param array &$variables
 *   An associative array containing the variables for the template.
 */
function template_preprocess_article(array &$variables) {
    // Add specific classes based on certain conditions.
    if (!empty($variables['content']['#node'])) {
        $node = $variables['content']['#node'];

        // Example condition: Add a class if the article is published.
        if ($node->isPublished()) {
            $variables['attributes']['class'][] = 'article-published';
        }

        // Example condition: Add a class based on the article's type.
        if ($node->getType() == 'article') {
            $variables['attributes']['class'][] = 'article-type';
        }

        // Additional conditions can be added here based on content properties.
    }
}