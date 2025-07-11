<?php
class Database {
    private $db_host;
    private $db_username;
    private $db_password;
    private $db_name;
    private $conn;
    
    public function __construct() {
        $this->db_host = 'localhost';
        $this->db_username = 'root';
        $this->db_password = '';
        $this->db_name = 'user_registration';
        $this->conn = new mysqli($this->db_host, $this->db_username, $this->db_password, $this->db_name);
    }
    
    public function getConnection() {
        return $this->conn;
    }
}
