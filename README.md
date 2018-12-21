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