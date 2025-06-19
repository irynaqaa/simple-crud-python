*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}    http://example.com/data

*** Test Cases ***
Data Driven Test
    [Documentation]    Test using data from external sources
    Open Browser    ${URL}    chrome
    ${data}=    Get Data From External Source
    :FOR    ${item}    IN    @{data}
    	Input Text    name_field_locator    ${item}[name]
    	Input Text    email_field_locator    ${item}[email]
    	Input Text    message_field_locator    ${item}[message]
    	Click Button    submit_button_locator
    	Page Should Contain    Form submitted successfully!
    Close Browser
