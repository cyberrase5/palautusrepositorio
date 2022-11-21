*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***

Register With Valid Username And Password
    Input Credentials  moi123  asd666661
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  kalle1235
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  a  sadasde5t645
    Output Should Contain  Username too short

Register With Valid Username And Too Short Password
    Input Credentials  sadasde5t645  a
    Output Should Contain  Password too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  sadasde5t645  aaaaaaaaaaaaaaaaaaa
    Output Should Contain  Password can't be only letters

*** Keywords ***
Input New Command And Create User
    Create User  kalle  kalle1235
    Input New Command