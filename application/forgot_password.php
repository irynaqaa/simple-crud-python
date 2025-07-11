<?php
use Psr\Http\Message\ServerRequestInterface;
use Psr\Http\Message\ResponseInterface;
use PHPMailer\PHPMailer\PHPMailer;

require __DIR__ . '/vendor/autoload.php';

$app = new \Slim\App();

$app->post('/forgot_password', function (ServerRequestInterface $request, ResponseInterface $response) {
    $data = $request->getParsedBody();
    
    // Validate and sanitize user input data
    $email = filter_var($data['email'], FILTER_SANITIZE_EMAIL);
    
    // Check if the user exists
    $db = new PDO('mysql:host=localhost;dbname=your_database', 'your_username', 'your_password');
    $stmt = $db->prepare('SELECT * FROM users WHERE email = :email');
    $stmt->bindParam(':email', $email);
    $stmt->execute();
    $user = $stmt->fetch();
    
    if ($user) {
        // Generate a password reset token
        $token = bin2hex(random_bytes(16));
        
        // Update the user's password reset token
        $stmt = $db->prepare('UPDATE users SET password_reset_token = :token WHERE id = :id');
        $stmt->bindParam(':token', $token);
        $stmt->bindParam(':id', $user['id']);
        $stmt->execute();
        
        // Send a password reset email to the user
        $mailer = new PHPMailer();
        $mailer->isSMTP();
        $mailer->Host = 'your_smtp_host';
        $mailer->SMTPAuth = true;
        $mailer->Username = 'your_smtp_username';
        $mailer->Password = 'your_smtp_password';
        $mailer->Subject = 'Reset your password';
        $mailer->Body = 'Click <a href="http://example.com/reset_password/' . $token . '">here</a> to reset your password';
        $mailer->setFrom('your_email_address', 'Your Name');
        $mailer->addAddress($email);
        $mailer->send();
        
        return $response->withJson(['message' => 'Password reset email sent successfully'], 200);
    } else {
        return $response->withJson(['message' => 'User not found'], 404);
    }
});

$app->run();
