*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}    http://example.com/login

*** Test Cases ***
Successful Login
    [Documentation]    Test successful login
    Open Browser    ${URL}    chrome
    Input Text    username_field_locator    valid_user
    Input Text    password_field_locator    valid_password
    Click Button    login_button_locator
    Page Should Contain    Expected content after login
    Close Browser

Unsuccessful Login
    [Documentation]    Test unsuccessful login
    Open Browser    ${URL}    chrome
    Input Text    username_field_locator    invalid_user
    Input Text    password_field_locator    invalid_password
    Click Button    login_button_locator
    Page Should Contain    Expected error message
    Close Browser
