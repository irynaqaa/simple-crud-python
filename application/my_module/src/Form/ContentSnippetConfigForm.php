<?php

namespace Drupal\\my_module\\src\\Form;

use Drupal\\Core\\Form\\FormBase;
use Drupal\\Core\\Form\\FormStateInterface;

/**
 * Class ContentSnippetConfigForm.
 *
 * Provides a configuration form for HTML snippets.
 */
class ContentSnippetConfigForm extends FormBase {

    /**
     * {@inheritdoc}
     */
    public function getFormId() {
        return 'content_snippet_config_form';
    }

    /**
     * {@inheritdoc}
     */
    public function buildForm(array $form, FormStateInterface $form_state) {
        $config = $this->config('my_module.settings');

        $form['snippet_1'] = [
            '#type' => 'textarea',
            '#title' => t('HTML Snippet 1'),
            '#required' => TRUE,
        ];

        $form['snippet_2'] = [
            '#type' => 'textarea',
            '#title' => t('HTML Snippet 2'),
            '#required' => TRUE,
        ];

        $form['snippet_3'] = [
            '#type' => 'textarea',
            '#title' => t('HTML Snippet 3'),
            '#required' => FALSE,
        ];

        $form['actions']['#type'] = 'actions';
        $form['actions']['submit'] = [
            '#type' => 'submit',
            '#value' => t('Save'),
        ];

        return $form;
    }

    /**
     * {@inheritdoc}
     */
    public function submitForm(array &$form, FormStateInterface $form_state) {
        $this->config('my_module.settings')
            ->set('snippet_1', $form_state->getValue('snippet_1'))
            ->set('snippet_2', $form_state->getValue('snippet_2'))
            ->set('snippet_3', $form_state->getValue('snippet_3'))
            ->save();
    }
}
