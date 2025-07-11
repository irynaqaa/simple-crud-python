<?php

require __DIR__ . '/vendor/autoload.php';
require __DIR__ . '/User.php';

$app = new \Slim\App();

$app->get('/verify/{email}', function (\Slim\Http\Request $request, \Slim\Http\Response $response, $args) {
    $email = $args['email'];
    $user = new User($conn);
    $result = $user->verifyEmail($email);
    if ($result === "Email verified successfully") {
        return $response->withJson(['message' => $result], 200);
    } else {
        return $response->withJson(['message' => $result], 400);
    }
});

$app->run();
