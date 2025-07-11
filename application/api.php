<?php
require __DIR__ . '/vendor/autoload.php';
require 'validation.php';
require 'sanitization.php';
require 'CRUD.php';
require 'logging.php';

use Psr\Http\Message\ServerRequestInterface;
use Psr\Http\Message\ResponseInterface;

$app = new \Slim\App();

// Create a RESTful API endpoint for user registration
$app->post('/register', function (ServerRequestInterface $request, ResponseInterface $response) {
    $data = $request->getParsedBody();
    $validation = new Validation();
    $sanitization = new Sanitization();
    $validatedData = $validation->validate($data);
    $sanitizedData = $sanitization->sanitize($data);
    $crud = new CRUD($db, $logger);
    $result = $crud->create($sanitizedData);
    return $response->withJson($result);
});

// Create a RESTful API endpoint for user login
$app->post('/login', function (ServerRequestInterface $request, ResponseInterface $response) {
    $data = $request->getParsedBody();
    $validation = new Validation();
    $validatedData = $validation->validate($data);
    // Check if the user exists and the password is correct
    $db = new PDO('mysql:host=localhost;dbname=your_database', 'your_username', 'your_password');
    $stmt = $db->prepare('SELECT * FROM users WHERE email = :email');
    $stmt->bindParam(':email', $data['email']);
    $stmt->execute();
    $user = $stmt->fetch();
    if ($user && password_verify($data['password'], $user['password'])) {
        // Generate a JWT token
        $token = JWT::encode([
            'iss' => 'your_issuer',
            'aud' => 'your_audience',
            'iat' => time(),
            'exp' => time() + 3600, // Token expires in 1 hour
            'sub' => $user['id'],
        ], 'your_secret_key', 'HS256');
        return $response->withJson(['token' => $token], 200);
    } else {
        return $response->withJson(['message' => 'Invalid email or password'], 401);
    }
});

$app->run();
