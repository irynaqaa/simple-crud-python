<?php
// User class for handling user registration and email verification

class User {
    private $conn;
    private $mail;
    
    public function __construct($conn) {
        $this->conn = $conn;
        $this->mail = new PHPMailer(true);
    }
    
    public function registerUser($name, $email, $password) {
        // Validate and sanitize user input data
        $name = filter_var($name, FILTER_SANITIZE_STRING);
        $email = filter_var($email, FILTER_SANITIZE_EMAIL);
        $password = password_hash($password, PASSWORD_DEFAULT);
        
        // Check if user already exists
        $query = "SELECT * FROM users WHERE email = '$email'";
        $result = $this->conn->query($query);
        if ($result->num_rows > 0) {
            return "User already exists";
        }
        
        // Insert user data into database
        $query = "INSERT INTO users (name, email, password) VALUES ('$name', '$email', '$password')";
        if ($this->conn->query($query) === TRUE) {
            return "User registered successfully";
        } else {
            return "Error registering user: " . $this->conn->error;
        }
    }
    
    public function sendVerificationEmail($email) {
        // Set up PHPMailer
        $this->mail->isSMTP();
        $this->mail->Host = 'smtp.gmail.com';
        $this->mail->SMTPAuth = true;
        $this->mail->Username = 'your_email@gmail.com';
        $this->mail->Password = 'your_email_password';
        $this->mail->SMTPSecure = 'tls';
        $this->mail->Port = 587;
        
        // Set up email content
        $this->mail->setFrom('your_email@gmail.com', 'User Registration');
        $this->mail->addAddress($email);
        $this->mail->isHTML(true);
        $this->mail->Subject = 'Verify your email address';
        $this->mail->Body = 'Click <a href="http://localhost/verify.php?email=' . $email . '">here</a> to verify your email address.';
        
        // Send email
        if ($this->mail->send()) {
            return "Email sent successfully";
        } else {
            return "Error sending email: " . $this->mail->ErrorInfo;
        }
    }
}
