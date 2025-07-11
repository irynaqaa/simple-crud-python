<?php

use Stripe\Stripe;
use Stripe\Charge;
use Stripe\Customer;
use Stripe\Token;
require __DIR__ . '/vendor/autoload.php';

Stripe::setApiKey('YOUR_STRIPE_SECRET_KEY');

$app = new \Slim\App();

$app->post('/payment', function ($request, $response) {
    $data = $request->getParsedBody();
    $customer = Customer::create([
        'email' => $data['email'],
        'source' => $data['token'],
    ]);
    $charge = Charge::create([
        'customer' => $customer->id,
        'amount' => $data['amount'],
        'currency' => 'usd',
    ]);
    return $response->withJson(['message' => 'Payment successful'], 200);
});

$app->run();
