<?php

namespace Application\src\Form;

use Drupal\Core\Form\FormBase;
use Drupal\Core\Form\FormStateInterface;

class ArticleForm extends FormBase {

    /**
     * {@inheritdoc}
     */
    public function getFormId() {
        return 'article_form';
    }

    /**
     * {@inheritdoc}
     */
    public function buildForm(array $form, FormStateInterface $form_state) {
        $form['content'] = [
            '#type' => 'textarea',
            '#title' => $this->t('Article Content'),
            '#description' => $this->t('Enter the article content with tokens.'),
            '#required' => TRUE,
        ];

        $form['actions']['#type'] = 'actions';
        $form['actions']['submit'] = [
            '#type' => 'submit',
            '#value' => $this->t('Save Article'),
            '#ajax' => [
                'callback' => '::ajaxSubmit',
                'wrapper' => 'article-form-messages',
            ],
        ];

        $form['messages'] = [
            '#type' => 'markup',
            '#markup' => '<div id="article-form-messages"></div>',
        ];

        return $form;
    }

    /**
     * AJAX callback for the form submission.
     */
    public function ajaxSubmit(array &$form, FormStateInterface $form_state) {
        $this->submitForm($form, $form_state);
        $response = [
            '#type' => 'markup',
            '#markup' => $this->t('Article saved successfully.'),
        ];
        return $response;
    }

    /**
     * {@inheritdoc}
     */
    public function submitForm(array &$form, FormStateInterface $form_state) {
        // Here you would typically handle the form submission.
        // For demonstration, we will just return a success message.
        drupal_set_message($this->t('Article saved successfully.'));
    }
}
