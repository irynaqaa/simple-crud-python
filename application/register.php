<?php

require __DIR__ . '/vendor/autoload.php';
require __DIR__ . '/User.php';

$app = new \Slim\App();

$app->post('/register', function (\Slim\Http\Request $request, \Slim\Http\Response $response) {
    $data = $request->getParsedBody();
    $user = new User($conn);
    $result = $user->registerUser($data['name'], $data['email'], $data['password']);
    if ($result === "User registered successfully") {
        $user->sendVerificationEmail($data['email']);
        return $response->withJson(['message' => $result], 201);
    } else {
        return $response->withJson(['message' => $result], 400);
    }
});

$app->run();
