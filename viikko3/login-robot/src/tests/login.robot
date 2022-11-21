*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input Login Command

*** Test Cases ***
Login With Correct Credentials
    Input Credentials  kalle  kalle12366666
    Output Should Contain  Logged in

Login With Incorrect Password
    Create User  asdf  moi12366666
    Input Credentials  asdf  123moi66666
    Output Should Contain  Invalid username or password

Login With Nonexistent Username
    Input Credentials  asd  123moi
    Output Should Contain  Invalid username or password


*** Keywords ***
Create User And Input Login Command
    Create User  kalle  kalle12366666
    Input Login Command
