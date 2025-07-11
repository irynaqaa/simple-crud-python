<?php

require __DIR__ . '/vendor/autoload.php';
require __DIR__ . '/User.php';

$app = new \Slim\App();

$app->post('/login', function (\Slim\Http\Request $request, \Slim\Http\Response $response) {
    $data = $request->getParsedBody();
    $user = new User($conn);
    $result = $user->loginUser($data['email'], $data['password']);
    if ($result === "Login successful") {
        return $response->withJson(['message' => $result], 200);
    } else {
        return $response->withJson(['message' => $result], 400);
    }
});

$app->run();
