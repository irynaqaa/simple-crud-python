<?php

class Sanitization {
    public function sanitize($data) {
        // Sanitize the data using filter_var
        $sanitizedData = [];
        foreach ($data as $key => $value) {
            $sanitizedData[$key] = filter_var($value, FILTER_SANITIZE_STRING);
        }
        return $sanitizedData;
    }
}
