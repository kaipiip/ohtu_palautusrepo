*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  kissa  kissa123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  kalle123
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  ki  kissa123
    Output Should Contain  Username length must be at least 3 letters

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  ki$$a  kissa123
    Output Should Contain  Valid username charachters are within range \"a\" to \"z\"

Register With Valid Username And Too Short Password
    Input Credentials  kissa  kissa
    Output Should Contain  Password length must be at least 8 charachters


Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  kissa  kissakissa
    Output Should Contain  Password cannot contain only letters

*** Keywords ***
Input New Command And Create User
    Create User  kalle  kalle123
    Input New Command
    