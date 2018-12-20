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

############################# Tests for getting a specific red-flag record ######################################
def test_to_get_a_specific_redflag_record():
    """
    Method for fetching a specific red-flag
    """
    result = client_tester().get('/api/v1/red-flags/1')
    assert result.status_code == 200
    json_data = json.loads(result.data)
    assert json_data['data'][0]['id'] == 1
    assert json_data['data'][0]['title'] == "Judicial corruption"
    assert json_data['data'][0]['location'] == [0.8789,9.5672]
    assert json_data['data'][0]['createdBy'] == "Noah"
    assert json_data['data'][0]['comment'] == "Bribery"
    assert json_data['data'][0]['status'] == "draft"

############################# Tests for getting a specific red-flag record with wrong id ######################################
def test_for_getting_a_record_wrong_id():
    """
    Method for fetching a specific red-flag
    """
    #passing a negative id
    result1 = client_tester().get('/api/v1/red-flags/-9')

    #passing a string as an id 
    result2 = client_tester().get('/api/v1/red-flags/dndnd')
    
    #passing an id that doesn't exist
    result3 = client_tester().get('/api/v1/red-flags/10')

    # checking the status codes
    assert result1.status_code == 400
    assert result2.status_code == 400
    assert result3.status_code == 404

    # converting our results into json
    json_data1 = json.loads(result1.data)
    json_data2 = json.loads(result2.data)
    json_data3 = json.loads(result3.data)

    assert json_data1['error'] == "The id cannot be negative"
    assert json_data2['error'] == "The id must be a non negative integer"
    assert json_data3['error'] == "Red-flag not found"
    
############################# Tests for changing geolocation ######################################
def test_to_change_geolocation_of_a_redflag():
    """
    Method for changing geolocation
    """
    result = client_tester().put('api/v1/red-flags/1/location',content_type='application/json',
                           data=json.dumps({"location" : [10.1010,20.2020]}))
    
    assert result.status_code == 200

    json_data = json.loads(result.data)
    assert "data" in json_data
    assert json_data['data'][0]['id'] == 1
    assert json_data['data'][0]['message'] == "Updated red-flag record’s location"

    #make a put request to check whether the red-flag has been updated
    check_redflag = client_tester().get('/api/v1/red-flags/1')
    assert check_redflag.status_code == 200
    json_data = json.loads(check_redflag.data)
    assert json_data['data'][0]['id'] == 1
    assert json_data['data'][0]['title'] == "Judicial corruption"
    assert json_data['data'][0]['location'] == [10.1010,20.2020]
    assert json_data['data'][0]['createdBy'] == "Noah"
    assert json_data['data'][0]['comment'] == "Bribery"
    assert json_data['data'][0]['status'] == "draft"

    ############################## Tests for updating a red-flag with wrong content type ######################################
def test_for_updating_a_redflag_with_wrong_content_type():
    """
    Method for addng a new red-flag with wrong content type 
    """
    result = client_tester().put('api/v1/red-flags/1/location', content_type='text',
                           data=json.dumps({"location" : [10.1010,20.2020]}))
    
    assert result.status_code == 400

    json_data = json.loads(result.data)
    assert "error" in json_data
    assert json_data['error'] == "The content type must be json"
    assert json_data['status'] == 400

############################# Tests for updating a location with wrong id ######################################
def test_for_updating_a_record_with_wrong_id():
    """
    Method for fetching a specific red-flag
    """
    #passing a negative id
    result1 = client_tester().put('api/v1/red-flags/-9/location', content_type='application/json')

    #passing a string as an id 
    result2 = client_tester().put('api/v1/red-flags/vhgjf/location', content_type='application/json')
    

    # checking the status codes
    assert result1.status_code == 400
    assert result2.status_code == 400
  
    # converting our results into json
    json_data1 = json.loads(result1.data)
    json_data2 = json.loads(result2.data)
    
    assert json_data1['error'] == "The id cannot be negative"
    assert json_data2['error'] == "The id must be a non negative integer"
    
############################# Tests for updating a specific red-flag record with wrong body format ######################################
def test_for_updating_location_with_wrong_body_format():
    """
    Method for addng a new red-flag with wrong body format
    """
    result = client_tester().put('api/v1/red-flags/1/location', content_type='application/json',
                           data=json.dumps({}))
    assert result.status_code == 400

    json_data = json.loads(result.data)
    assert "error" in json_data
    assert json_data['error'] == "wrong location format. follow this example ->> {'location':[12.3453,9.6589]}"
    assert json_data['status'] == 400

############################# Tests for updating location with wrong values ######################################
def test_to_update_a_new_redflag_with_wrong_values():
    """
    Method for addng a new red-flag with wrong values
    """
    result = client_tester().put('api/v1/red-flags/1/location', content_type='application/json',
                           data=json.dumps({"location": 2}))
    assert result.status_code == 400

    json_data = json.loads(result.data)
    assert "error" in json_data
    assert json_data['error'] == [
                                    "wrong location format. follow this example ->> {'location':[12.3453,9.6589]}",
                                    "location should contain only integers or floats",
                                    "location expects only two parameters in the list"
                                ]
    assert json_data['status'] == 400


############################# Tests for changing the comment ######################################
def test_to_change_the_comment_of_a_redflag():
    """
    Method for changing comment
    """
    result = client_tester().put('api/v1/red-flags/1/comment',content_type='application/json',
                           data=json.dumps({"comment" : "Deceit"}))
    
    assert result.status_code == 200

    json_data = json.loads(result.data)
    assert "data" in json_data
    assert json_data['data'][0]['id'] == 1
    assert json_data['data'][0]['message'] == "Updated red-flag record’s comment"

    #make a put request to check whether the red-flag has been updated
    check_redflag = client_tester().get('/api/v1/red-flags/1')
    assert check_redflag.status_code == 200
    json_data = json.loads(check_redflag.data)
    assert json_data['data'][0]['id'] == 1
    assert json_data['data'][0]['title'] == "Judicial corruption"
    assert json_data['data'][0]['location'] == [10.1010,20.2020]
    assert json_data['data'][0]['createdBy'] == "Noah"
    assert json_data['data'][0]['comment'] == "Deceit"
    assert json_data['data'][0]['status'] == "draft"

def test_for_editing_comment_with_wrong_content_type():
    """
    Method for addng a new red-flag with wrong content type 
    """
    result = client_tester().put('api/v1/red-flags/1/comment', content_type='text',
                           data=json.dumps({"comment" : "Deceit"}))
    
    assert result.status_code == 400

    json_data = json.loads(result.data)
    assert "error" in json_data
    assert json_data['error'] == "The content type must be json"
    assert json_data['status'] == 400

############################# Tests for updating location with wrong values ######################################
def test_for_editting_comment_with_wrong_values():
    """
    Method for editting comment with wrong values
    """
    result = client_tester().put('api/v1/red-flags/1/comment', content_type='application/json',
                           data=json.dumps({"comment": 2}))
    result2 = client_tester().put('api/v1/red-flags/sxff/comment', content_type='application/json',
                           data=json.dumps({"comment": 2}))
    assert result.status_code == 400
    assert result2.status_code == 400
    
    json_data = json.loads(result.data)
    json_data2 = json.loads(result2.data)
    assert "error" in json_data
    assert "error" in json_data2
    assert json_data['error'] == [
                                    "The comment must be a string",
                                    "The comment must be between 5 and 50 characters",
                                    "Comment cannot contain numbers or special characters"
                                    ]
    assert json_data2['error'] == "The id must be a non negative integer"
    
    assert json_data['status'] == 400

############################# Tests for updating a specific red-flag record with wrong body format ######################################
def test_for_updating_comment_with_wrong_body_format():
    """
    Method for updating comment with wrong body format
    """
    result = client_tester().put('api/v1/red-flags/1/comment', content_type='application/json',
                           data=json.dumps({}))
    assert result.status_code == 400

    json_data = json.loads(result.data)
    assert "error" in json_data
    assert json_data['error'] == "wrong location format. follow this example ->> {'comment':'Bribery'}"
    assert json_data['status'] == 400

############################# Tests for deleting a red flag ######################################
def test_to_delete_a_redflag():
    result = client_tester().delete('api/v1/red-flags/1')
    
    assert result.status_code == 200

    json_data = json.loads(result.data)
    assert "data" in json_data
    assert json_data['data'][0]['id'] == 1
    assert json_data['data'][0]['message'] == "red-flag record has been deleted"

    # check to verify whether the red-flag has been deleted
    result = client_tester().get('api/v1/red-flags')
    assert result.status_code == 200
    json_data = json.loads(result.data)
    assert json_data['data'][0]['message'] == "There are no red-flags yet"


# ######################### tests for deleting a red-flag using a wrong id ##################################
def test_to_delete_a_redflag_using_a_wrong_id():
    result1 = client_tester().delete('api/v1/red-flags/-2')
    result2 = client_tester().delete('api/v1/red-flags/wee')

    assert result1.status_code == 400
    assert result2.status_code == 400
    json_data1 = json.loads(result1.data)
    json_data2 = json.loads(result2.data)
    assert "error" in json_data1
    assert "error" in json_data2

    assert json_data1['error'] == "The id cannot be negative"
    assert json_data2['error'] == "The id must be a non negative integer"
    assert json_data1['status'] == 400
    assert json_data2['status'] == 400

#########################tests for deleting a red-flag that doesn't exist####################################
def test_to_delete_a_redflag_which_doesnt_exist():
    result = client_tester().delete('api/v1/red-flags/2')

    assert result.status_code == 404
    json_data = json.loads(result.data)
    assert "error" in json_data
    assert json_data['error'] == "Red-flag not found"
    assert json_data['status'] == 404
