<?php

class Auth {
    private $secretKey;
    
    public function __construct($secretKey) {
        $this->secretKey = $secretKey;
    }
    
    public function generateToken($userId) {
        $token = \Firebase\JWT\JWT::encode([
            'iss' => 'your_issuer',
            'aud' => 'your_audience',
            'iat' => time(),
            'exp' => time() + 3600, // Token expires in 1 hour
            'sub' => $userId,
        ], $this->secretKey, 'HS256');
        
        return $token;
    }
    
    public function validateToken($token) {
        try {
            $decoded = \Firebase\JWT\JWT::decode($token, $this->secretKey, ['HS256']);
            return $decoded->sub;
        } catch (\Exception $e) {
            return null;
        }
    }
}
