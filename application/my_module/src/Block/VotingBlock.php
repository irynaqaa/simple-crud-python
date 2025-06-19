<?php

namespace Drupal\my_module\src\Block;

use Drupal\Core\Block\BlockBase;
use Drupal\Core\Cache\Cache;

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
        // Render the voting buttons with AJAX functionality.
        $build = [
            '#markup' => '<div class="voting-component">
                <button class="upvote-button" aria-label="Upvote">Upvote</button>
                <button class="downvote-button" aria-label="Downvote">Downvote</button>
            </div>',
            '#attached' => [
                'library' => [
                    'my_module/voting_library',
                ],
            ],
        ];

        return $build;
    }

    /**
     * {@inheritdoc}
     */
    public function getCacheContexts() {
        return [Cache::PERMANENT];
    }
}
