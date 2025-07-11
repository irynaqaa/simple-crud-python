<?php

class Token {
    private $conn;
    
    public function __construct($conn) {
        $this->conn = $conn;
    }
    
    public function generateToken($user_id) {
        $token = bin2hex(random_bytes(16));
        $stmt = $this->conn->prepare('INSERT INTO tokens (user_id, token) VALUES (:user_id, :token)');
        $stmt->bindParam(':user_id', $user_id);
        $stmt->bindParam(':token', $token);
        $stmt->execute();
        return $token;
    }
    
    public function verifyToken($token) {
        $stmt = $this->conn->prepare('SELECT * FROM tokens WHERE token = :token');
        $stmt->bindParam(':token', $token);
        $stmt->execute();
        $token_data = $stmt->fetch();
        if ($token_data) {
            return $token_data['user_id'];
        } else {
            return null;
        }
    }
}
