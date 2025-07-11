<?php

class ErrorHandling {
    private $logger;
    
    public function __construct($logger) {
        $this->logger = $logger;
    }
    
    public function handleError($e) {
        $this->logger->addError('Error: ' . $e->getMessage());
        return ['message' => 'An error occurred'];
    }
}
