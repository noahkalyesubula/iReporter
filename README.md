# iReporter

[![Build Status](https://travis-ci.org/noahkalyesubula/iReporter.svg?branch=develop)](https://travis-ci.org/noahkalyesubula/iReporter)
[![Maintainability](https://api.codeclimate.com/v1/badges/686f37edfc20a7c0d374/maintainability)](https://codeclimate.com/github/noahkalyesubula/iReporter/maintainability)
[![Coverage Status](https://coveralls.io/repos/github/noahkalyesubula/iReporter/badge.svg?branch=develop)](https://coveralls.io/github/noahkalyesubula/iReporter?branch=develop)


## Project overview:

Corruption is a huge bane to Africa’s development. African countries must develop novel and
localised solutions that will curb this menace, hence the birth of iReporter. iReporter enables
any/every citizen to bring any form of corruption to the notice of appropriate authorities and the
general public. Users can also report on things that needs government intervention.

## Functionality
- Create a red-flag record
- Get all red-flag records
- Get a specific red-flag record
- Edit a specific red-flag record
- Delete a red-flag record

The live demo for this project can be found at: 
https://noahkalyesubula.github.io/iReporter/

Github repository can be found at:
https://github.com/noahkalyesubula/iReporter

PivotalTracker link: https://www.pivotaltracker.com/n/projects/2231656



## Project usage:
The project has an admin and users.

### Admin
The admin is able to log into the system and view a list of all red-flag/intervention records created by all users.
The admin can also change the status of a record to either under investigation, rejected (in the
event of a false claim) or resolved (in the event that the claim has been investigated and
resolved) .
<!--admin login credentials-->
#### Admin credentials
email:admin@admin.com
password:admin1234


### Users
The user is able to log into the system with the right credentials. 
The user is also able to create/edit/delete their red-flag or intervention records.
<!--user login credentials-->
#### User credentials
email:user@user.com
password:user1234

## Configuration instructions:
For one to use this application, the person needs to have a computer with a browser and a steady internet connection.

These are the endpoints:

| Method  | Endpoint          | Description                      | Body                  |
| --------|:-----------------:| -------------------------------: |----------------------:|
| GET     | /api/v1/red-flags | Get all red-flag records |                  |                       |
| GET     | /api/v1/red-flags/id | Get a specific red-flag record  |                       |   
|POST     | /api/v1/red-flags | Create a red-flag record         | e.g  {"createdBy" : "Noah", "title":"Judicial corruption", "location" : [0.8789, 9.5672], "comment" : "Bribery"}  |
|PUT      | /api/v1/red-flags/id/location | Edit geolocation   | e.g  {"location" : [0.8789, 9.5672]} |
|PUT      | /api/v1/red-flags/id/comment | Edit comment        | e.g  {"comment" : "Bribery"} |
|DELETE   | /api/v1/red-flags/id | Delete a red-flag record|   |                       |


APIs are Hosted at https://ireporter-system.herokuapp.com/
