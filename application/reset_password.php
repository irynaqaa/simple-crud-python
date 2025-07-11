<?php
use Psr\Http\Message\ServerRequestInterface;
use Psr\Http\Message\ResponseInterface;
use PHPMailer\PHPMailer\PHPMailer;

require __DIR__ . '/vendor/autoload.php';

$app = new \Slim\App();

$app->post('/reset_password/{token}', function (ServerRequestInterface $request, ResponseInterface $response, $args) {
    $token = $args['token'];
    $data = $request->getParsedBody();
    
    // Validate and sanitize user input data
    $password = filter_var($data['password'], FILTER_SANITIZE_STRING);
    
    // Check if the token is valid
    $db = new PDO('mysql:host=localhost;dbname=your_database', 'your_username', 'your_password');
    $stmt = $db->prepare('SELECT * FROM users WHERE password_reset_token = :token');
    $stmt->bindParam(':token', $token);
    $stmt->execute();
    $user = $stmt->fetch();
    
    if ($user) {
        // Update the user's password
        $passwordHash = password_hash($password, PASSWORD_DEFAULT);
        $stmt = $db->prepare('UPDATE users SET password = :password, password_reset_token = NULL WHERE id = :id');
        $stmt->bindParam(':password', $passwordHash);
        $stmt->bindParam(':id', $user['id']);
        $stmt->execute();
        
        return $response->withJson(['message' => 'Password reset successfully'], 200);
    } else {
        return $response->withJson(['message' => 'Invalid token'], 400);
    }
});

$app->run();
