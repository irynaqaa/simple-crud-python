<?php

namespace Application\src\Form;

use Drupal\Core\Form\FormBase;
use Drupal\Core\Form\FormStateInterface;

class HtmlSnippetConfigForm extends FormBase {

    /**
     * {@inheritdoc}
     */
    public function getFormId() {
        return 'html_snippet_config_form';
    }

    /**
     * {@inheritdoc}
     */
    public function buildForm(array $form, FormStateInterface $form_state) {
        $form['snippet_1'] = [
            '#type' => 'textarea',
            '#title' => $this->t('Snippet 1'),
            '#required' => TRUE,
        ];

        $form['snippet_2'] = [
            '#type' => 'textarea',
            '#title' => $this->t('Snippet 2'),
            '#required' => TRUE,
        ];

        $form['snippet_3'] = [
            '#type' => 'textarea',
            '#title' => $this->t('Snippet 3'),
            '#required' => TRUE,
        ];

        $form['actions']['#type'] = 'actions';
        $form['actions']['submit'] = [
            '#type' => 'submit',
            '#value' => $this->t('Save Snippets'),
        ];

        return $form;
    }

    /**
     * {@inheritdoc}
     */
    public function submitForm(array &$form, FormStateInterface $form_state) {
        // Save the snippets to configuration.
        $config = \Drupal::configFactory()->getEditable('custom_voting_module.settings');
        $config->set('snippet_1', $form_state->getValue('snippet_1'))
            ->set('snippet_2', $form_state->getValue('snippet_2'))
            ->set('snippet_3', $form_state->getValue('snippet_3'))
            ->save();

        drupal_set_message($this->t('HTML snippets saved successfully.'));
    }
}