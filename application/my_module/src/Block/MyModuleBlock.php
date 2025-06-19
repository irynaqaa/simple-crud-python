<?php

namespace Drupal\my_module\src\Block;

use Drupal\Core\Block\BlockBase;

/**
 * Provides a 'MyModule' Block.
 *
 * @Block(
 *   id = "my_module_block",
 *   admin_label = @Translation("My Module Block"),
 * )
 */
class MyModuleBlock extends BlockBase {

    /**
     * {@inheritdoc}
     */
    public function build() {
        return [
            '#markup' => t('This is my custom block content.'),
        ];
    }
}
