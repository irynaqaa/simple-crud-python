<?php

namespace Application\src\Form;

use Drupal\Core\Form\FormBase;
use Drupal\Core\Form\FormStateInterface;

class CustomConfigForm extends FormBase {

    /**
     * {@inheritdoc}
     */
    public function getFormId() {
        return 'custom_config_form';
    }

    /**
     * {@inheritdoc}
     */
    public function buildForm(array $form, FormStateInterface $form_state) {
        $form['api_key'] = [
            '#type' => 'textfield',
            '#title' => $this->t('API Key'),
            '#required' => TRUE,
        ];

        $form['api_secret'] = [
            '#type' => 'textfield',
            '#title' => $this->t('API Secret'),
            '#required' => TRUE,
        ];

        $form['api_url'] = [
            '#type' => 'url',
            '#title' => $this->t('API URL'),
            '#required' => TRUE,
        ];

        $form['actions']['#type'] = 'actions';
        $form['actions']['submit'] = [
            '#type' => 'submit',
            '#value' => $this->t('Save Configuration'),
        ];

        return $form;
    }

    /**
     * {@inheritdoc}
     */
    public function submitForm(array &$form, FormStateInterface $form_state) {
        // Save the configuration.
        
        
        drupal_set_message($this->t('Configuration saved successfully.'));
    }
}