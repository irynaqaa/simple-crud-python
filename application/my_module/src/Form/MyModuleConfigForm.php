<?php

namespace Drupal\my_module\src\Form;

use Drupal\Core\Form\FormBase;
use Drupal\Core\Form\FormStateInterface;

/**
 * Class MyModuleConfigForm.
 *
 * Provides a configuration form for API credentials.
 */
class MyModuleConfigForm extends FormBase {

    /**
     * {@inheritdoc}
     */
    public function getFormId() {
        return 'my_module_config_form';
    }

    /**
     * {@inheritdoc}
     */
    public function buildForm(array $form, FormStateInterface $form_state) {
        $config = $this->config('my_module.settings');

        $form['api_key'] = [
            '#type' => 'textfield',
            '#title' => t('API Key'),
            '#required' => TRUE,
        ];

        $form['api_secret'] = [
            '#type' => 'textfield',
            '#title' => t('API Secret'),
            '#required' => TRUE,
        ];

        $form['api_url'] = [
            '#type' => 'url',
            '#title' => t('API URL'),
            '#required' => TRUE,
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
            ->set('api_key', $form_state->getValue('api_key'))
            ->set('api_secret', $form_state->getValue('api_secret'))
            ->set('api_url', $form_state->getValue('api_url'))
            ->save();
    }
}
