<?php

class Validation {
    public function validateUsername($username) {
        return filter_var($username, FILTER_SANITIZE_STRING);
    }
    
    public function validateEmail($email) {
        return filter_var($email, FILTER_SANITIZE_EMAIL);
    }
    
    public function validatePassword($password) {
        return filter_var($password, FILTER_SANITIZE_STRING);
    }
}
