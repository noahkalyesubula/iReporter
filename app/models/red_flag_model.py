import re
from flask import jsonify
"""
Red-flag modal for creating new red-flags
"""
class RedFlagModel:
    def __init__(self, **kwargs):
        self.id = kwargs['id']
        self.createdBy = kwargs['createdBy']
        self.title = kwargs['title']
        self.location = kwargs['location']
        self.comment = kwargs['comment']
        self.status = kwargs['status']
        self.createdOn = kwargs['createdOn']

    def validate_posted_data(createdBy, title, location, comment):
        errors = []
        if not createdBy or not title or not location or not comment:
            errors.append("createdBy, title, location, and comment must not be empty")
        if not isinstance(createdBy, str) or re.search("[0-9]", str(createdBy)) or re.search("[$#@]", str(createdBy)):                                                                
            errors.append("createdBy must be a string with no digits or special characters")
        if RedFlagModel.validate_comment(comment) is not True:
            errors += RedFlagModel.validate_comment(comment)
        if RedFlagModel.validate_location(location) is not True:
            errors += RedFlagModel.validate_location(location)
        if not errors:
            return True
        return errors

    def validate_location(location):
        get_errors = []
        if not type(location) is list:
            get_errors.append("wrong location format. follow this example ->> {'location':[12.3453,9.6589]}")
        
        try:
            if len(location) != 2:
                get_errors.append("location expects only two parameters in the list")
            if (type(location[0]) not in [int, float]) or (type(location[1]) not in [int, float]):
                get_errors.append("The location should contain only integers or floats")                                         
        except:
            get_errors.append("location should contain only integers or floats")
            get_errors.append("location expects only two parameters in the list")
        if not get_errors:
            return True
        return get_errors
    
    def validate_comment(comment):
        caught_errors = []
        if not isinstance(comment, str):
            caught_errors.append("The comment must be a string")
        
        if (len(str(comment)) < 5 or len(str(comment)) > 50):
                caught_errors.append("The comment must be between 5 and 50 characters")
        
        if re.search("[0-9]", str(comment)) or re.search("[$#@]", str(comment)):
            caught_errors.append("Comment cannot contain numbers or special characters")
        if not caught_errors:
            return True
        return caught_errors

    def validate_id(id):
        try:
            convert_id = int(id)
            
        except:
            return jsonify({"status": 400, "error":"The id must be a non negative integer"}),400

        if convert_id < 0:
            return jsonify({"status": 400, "error":"The id cannot be negative"}),400
        return True

    def edit_location_validation(location, redflags_list, id):
        
        # validate location
        if RedFlagModel.validate_location(location) is not True:
            return jsonify({"status":400, "error": RedFlagModel.validate_location(location)}),400
        
        #check if the id matches a particular red-flag in the list
        get_redflag_record = [r_record.__dict__ for r_record in redflags_list if r_record.__dict__['id'] == int(id) ]
        if not get_redflag_record:
            return jsonify({"status":404, "error":"Red-flag not found"}),404

        if get_redflag_record[0]['status'] in ['under investigation','rejected','resolved']:
            return jsonify({"status":400, "error": "You can no longer edit or delete this red-flag"}),400

        return True
    
    
    def validate_content_type(contentType):
        if contentType == 'application/json':
            return True
        return jsonify({"status":400, "error":"The content type must be json"}), 400