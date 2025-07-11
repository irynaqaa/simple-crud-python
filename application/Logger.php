<?php

class Logger {
    private $logger;
    
    public function __construct() {
        $this->logger = new Logger('app');
        $this->logger->pushHandler(new StreamHandler('logs/app.log', Logger::DEBUG));
    }
    
    public function log($message, $level = Logger::INFO) {
        $this->logger->log($level, $message);
    }
}
