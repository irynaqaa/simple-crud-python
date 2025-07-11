<?php

class Logging {
    private $logger;
    
    public function __construct() {
        $this->logger = new \Monolog\Logger('app');
        $this->logger->pushHandler(new \Monolog\Handler\StreamHandler('logs/app.log', \Monolog\Logger::DEBUG));
    }
    
    public function log($message, $level = \Monolog\Logger::INFO) {
        $this->logger->log($level, $message);
    }
}
