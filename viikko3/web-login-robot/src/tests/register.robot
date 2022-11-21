*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set RUsername  moi123
    Set RPassword  asf123ghj
    Set RPassword Again  asf123ghj
    Submit Credentials
    Registration Should Succeed


Register With Too Short Username And Valid Password
    Set RUsername  a
    Set RPassword  asf123ghj
    Set RPassword Again  asf123ghj
    Submit Credentials
    Registration Should Fail With Message  Username too short

Register With Valid Username And Too Short Password
    Set RUsername  moi123
    Set RPassword  asf123
    Set RPassword Again  asf123
    Submit Credentials
    Registration Should Fail With Message  Password too short

Register With Nonmatching Password And Password Confirmation
    Set RUsername  moi123
    Set RPassword  asf1234567
    Set RPassword Again  asf123456
    Submit Credentials
    Registration Should Fail With Message  Passwords don't match


Login After Successful Registration
    Set RUsername  moi123
    Set RPassword  asf123ghj
    Set RPassword Again  asf123ghj
    Submit Credentials
    Go To Login Page
    Set Username  moi123
    Set Password  asf123ghj
    Submit LCredentials
    Login Should Succeed

Login After Failed Registration
    Set RUsername  as
    Set RPassword  asf123ghj
    Set RPassword Again  asf123ghj
    Submit Credentials
    Go To Login Page
    Set Username  as
    Set Password  asf123ghj
    Submit LCredentials
    Login Should Fail With Message  Invalid username or password


*** Keywords ***
Go To Register Page
    Go To  ${REGISTER URL}

Set RUsername
    [Arguments]  ${username}
    Input Text  username  ${username}

Set RPassword
    [Arguments]  ${password}
    Input Password  password  ${password}

Set RPassword Again
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

Registration Should Succeed
    Title Should Be  Welcome to Ohtu Application!

Submit Credentials
    Click Button  Register

Registration Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit LCredentials
    Click Button  Login

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Login Should Succeed
    Main Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}