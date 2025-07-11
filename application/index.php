<?php
// Include configuration file
require_once 'config.php';

// Include User class
require_once 'User.php';

// Create a new User object
$user = new User($conn);

// Check if form is submitted
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $name = $_POST['name'];
    $email = $_POST['email'];
    $password = $_POST['password'];
    
    // Register user
    $result = $user->registerUser($name, $email, $password);
    if ($result == 'User registered successfully') {
        // Send verification email
        $result = $user->sendVerificationEmail($email);
        if ($result == 'Email sent successfully') {
            echo 'User registered and email sent successfully.';
        } else {
            echo 'Error sending email: ' . $result;
        }
    } else {
        echo 'Error registering user: ' . $result;
    }
}

// Close database connection
$conn->close();
?>
