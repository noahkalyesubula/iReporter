import pytest
from flask import json
from app import app
client_tester = app.test_client


############################# Tests for getting all red-flags with an empty data structure ######################################
def test_when_there_are_no_redflags():
    result = client_tester().get('/api/v1/red-flags')
    assert result.status_code == 200
    json_data = json.loads(result.data)
    assert json_data['data'][0]['message'] == "There are no red-flags yet"

############################# Tests for addng a new red-flag ###########################################################
def test_to_create_a_new_redflag():
    """
    Method for addng a new red-flag
    """
    result = client_tester().post('/api/v1/red-flags', content_type='application/json',
                           data=json.dumps({"createdBy" : "Noah",
                                            "title":"Judicial corruption",
                                            "location" : [0.8789, 9.5672],
                                            "comment" : "Bribery"}))
    assert result.status_code == 201

    json_data = json.loads(result.data)
    assert "data" in json_data
    assert json_data['data'][0]['id'] == 1
    assert json_data['status'] == 201
    assert json_data['data'][0]['message'] == "Created red-flag record"

############################## Tests for addng a new red-flag with wrong content type ######################################
def test_to_create_a_new_redflag_with_wrong_content_type():
    """
    Method for addng a new red-flag with wrong content type 
    """
    result = client_tester().post('/api/v1/red-flags', content_type='text',
                           data=json.dumps({"createdBy" : "Noah",
                                            "title":"Judicial corruption",
                                            "location" : [0.8789, 9.5672],
                                            "comment" : "Bribery"}))
    assert result.status_code == 400

    json_data = json.loads(result.data)
    assert "error" in json_data
    assert json_data['error'] == "Content-type must be json"
    assert json_data['status'] == 400
    
############################# Tests for addng a new red-flag with wrong body format ######################################
def test_to_create_a_new_redflag_with_wrong_body_format():
    """
    Method for addng a new red-flag with wrong body format
    """
    result = client_tester().post('/api/v1/red-flags', content_type='application/json',
                           data=json.dumps({}))
    assert result.status_code == 400

    json_data = json.loads(result.data)
    assert "error" in json_data
    assert json_data['error'] == "Wrong body format. refer to this example -> {'createdBy': 'Noah', 'title': 'Judicial Corruption, \
                                                                 'location':[6.2134,3.5677], 'comment':'Bribery'}"
    assert json_data['status'] == 400

############################# Tests for addng a new red-flag with wrong values ######################################
def test_to_create_a_new_redflag_with_wrong_values():
    """
    Method for addng a new red-flag with wrong values
    """
    result = client_tester().post('/api/v1/red-flags', content_type='application/json',
                           data=json.dumps({"createdBy" : "12",
                                            "title":2,
                                            "location" : "kampala",
                                            "comment" : "2"}))
    assert result.status_code == 400

    json_data = json.loads(result.data)
    assert "error" in json_data
    assert json_data['error'] ==  [
                                    "createdBy must be a string with no digits or special characters",
                                    "The comment must be between 5 and 50 characters",
                                    "Comment cannot contain numbers or special characters",
                                    "wrong location format. follow this example ->> {'location':[12.3453,9.6589]}",
                                    "location expects only two parameters in the list",
                                    "The location should contain only integers or floats"
                                ]
    assert json_data['status'] == 400

############################# Tests for getting all red-flags ######################################

def test_to_get_all_redflags():
    """
    Method for fetching all red-flags.
    """
    result = client_tester().get('/api/v1/red-flags')
    assert result.status_code == 200
    json_data = json.loads(result.data)
    assert json_data['data'][0]['id'] == 1
    assert json_data['data'][0]['title'] == "Judicial corruption"
    assert json_data['data'][0]['location'] == [0.8789,9.5672]
    assert json_data['data'][0]['createdBy'] == "Noah"
    assert json_data['data'][0]['comment'] == "Bribery"
    assert json_data['data'][0]['status'] == "draft"