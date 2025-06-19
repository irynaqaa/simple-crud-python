<?php

namespace Application\src\Controller;

use Drupal\Core\Controller\ControllerBase;
use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;

class ArticleController extends ControllerBase {

    /**
     * Handles the saving of article content.
     *
     * @param Request $request
     *   The request object containing the article content.
     *
     * @return JsonResponse
     *   A JSON response indicating the result of the save operation.
     */
    public function saveArticle(Request $request) {
        $article_content = $request->get('content');

        // Replace tokens with HTML snippets securely.
        $replaced_content = $this->replaceTokensWithSnippets($article_content);

        // Here you would typically save the $replaced_content to the database.
        // For demonstration, we will just return a success message.

        return new JsonResponse(['message' => 'Article saved successfully.', 'content' => $replaced_content]);
    }

    /**
     * Replaces specific tokens in the article body with defined HTML snippets.
     *
     * @param string $content
     *   The article content with tokens.
     *
     * @return string
     *   The content with tokens replaced by HTML snippets.
     */
    private function replaceTokensWithSnippets($content) {
        // Retrieve HTML snippets from configuration.
        $config = \Drupal::config('custom_voting_module.settings');
        $snippet_1 = $config->get('snippet_1');
        $snippet_2 = $config->get('snippet_2');
        $snippet_3 = $config->get('snippet_3');

        // Replace tokens with corresponding HTML snippets.
        $content = str_replace('[snippet_1]', $snippet_1, $content);
        $content = str_replace('[snippet_2]', $snippet_2, $content);
        $content = str_replace('[snippet_3]', $snippet_3, $content);

        return $content;
    }
}
