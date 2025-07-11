<?php
// CRUD operations
require 'config.php';
require 'logging.php';

class CRUD {
    private $db;
    private $logger;
    
    public function __construct($db, $logger) {
        $this->db = $db;
        $this->logger = $logger;
    }
    
    public function create($data) {
        try {
            $stmt = $this->db->prepare('INSERT INTO users (username, email, password) VALUES (:username, :email, :password)');
            $stmt->bindParam(':username', $data['username']);
            $stmt->bindParam(':email', $data['email']);
            $stmt->bindParam(':password', password_hash($data['password'], PASSWORD_DEFAULT));
            $stmt->execute();
            $this->logger->addInfo('User created successfully');
            return ['message' => 'User created successfully'];
        } catch (Exception $e) {
            $this->logger->addError('Error creating user: ' . $e->getMessage());
            return ['message' => 'Error creating user'];
        }
    }
    
    public function read($id) {
        try {
            $stmt = $this->db->prepare('SELECT * FROM users WHERE id = :id');
            $stmt->bindParam(':id', $id);
            $stmt->execute();
            $user = $stmt->fetch();
            $this->logger->addInfo('User retrieved successfully');
            return $user;
        } catch (Exception $e) {
            $this->logger->addError('Error retrieving user: ' . $e->getMessage());
            return null;
        }
    }
    
    public function update($id, $data) {
        try {
            $stmt = $this->db->prepare('UPDATE users SET username = :username, email = :email, password = :password WHERE id = :id');
            $stmt->bindParam(':username', $data['username']);
            $stmt->bindParam(':email', $data['email']);
            $stmt->bindParam(':password', password_hash($data['password'], PASSWORD_DEFAULT));
            $stmt->bindParam(':id', $id);
            $stmt->execute();
            $this->logger->addInfo('User updated successfully');
            return ['message' => 'User updated successfully'];
        } catch (Exception $e) {
            $this->logger->addError('Error updating user: ' . $e->getMessage());
            return ['message' => 'Error updating user'];
        }
    }
    
    public function delete($id) {
        try {
            $stmt = $this->db->prepare('DELETE FROM users WHERE id = :id');
            $stmt->bindParam(':id', $id);
            $stmt->execute();
            $this->logger->addInfo('User deleted successfully');
            return ['message' => 'User deleted successfully'];
        } catch (Exception $e) {
            $this->logger->addError('Error deleting user: ' . $e->getMessage());
            return ['message' => 'Error deleting user'];
        }
    }
}
