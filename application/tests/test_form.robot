*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}    http://example.com/form

*** Test Cases ***
Valid Form Submission
    [Documentation]    Test valid form submission
    Open Browser    ${URL}    chrome
    Input Text    name_field_locator    Test User
    Input Text    email_field_locator    test@example.com
    Input Text    message_field_locator    Hello!
    Click Button    submit_button_locator
    Page Should Contain    Form submitted successfully!
    Close Browser

Invalid Form Submission
    [Documentation]    Test invalid form submission
    Open Browser    ${URL}    chrome
    Input Text    name_field_locator    
    Input Text    email_field_locator    invalid_email
    Input Text    message_field_locator    
    Click Button    submit_button_locator
    Page Should Contain    Please fill out this field.
    Close Browser
