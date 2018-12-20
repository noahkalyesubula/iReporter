import datetime
from flask import request, jsonify
from flask.views import MethodView
from app.models.red_flag_model import RedFlagModel

redflags_list = []
class RedFlagView(MethodView):
    
    
    def get(self, id):
        if id is None:
            if not redflags_list:
                return jsonify({"status":200, "data":[{"message":"There are no red-flags yet"}]})
            return jsonify({"status":200,"data": [redflag_record.__dict__ for redflag_record in redflags_list]})

        validate_id_result = RedFlagModel.validate_id(id)
        if validate_id_result is not True:
            return validate_id_result
        single_redflag_record = [record.__dict__ for record in redflags_list if record.__dict__['id'] == int(id) ]
        if single_redflag_record:
            return jsonify({"status":200, "data": [single_redflag_record[0]]})
        return jsonify({"status":404, "error":"Red-flag not found"}),404
    
    
    def post(self):
        if request.content_type != 'application/json':
            return jsonify({"status":400, "error":"Content-type must be json"}),400
        if 'title' not in request.json or 'createdBy' not in request.json or 'location' not in request.json or 'comment' not in request.json:
            return jsonify({"status":400, "error":"Wrong body format. refer to this example -> {'createdBy': 'Noah', 'title': 'Judicial Corruption, \
                                                                 'location':[6.2134,3.5677], 'comment':'Bribery'}"}),400
        posted_data = request.get_json()
        validation_result = RedFlagModel.validate_posted_data(posted_data['createdBy'],posted_data['title'],posted_data['location'],posted_data['comment'])

        if validation_result is not True:
            return jsonify({"status":400, "error": validation_result}),400
        
        redflag_id = len(redflags_list) + 1
        # Add a new red-flag record
        new_redflag_record = RedFlagModel(id = redflag_id, createdBy = request.json['createdBy'], title = request.json['title'], \
                createdOn = str(datetime.datetime.now()), location = request.json['location'], status= 'draft', comment = request.json['comment'])
        
        redflags_list.append(new_redflag_record)
        return jsonify({"status":201, "data":[{"id":redflag_id, "message":"Created red-flag record"}]}),201

    # update geolocation
    def put(self, id):
        content_type = RedFlagModel.validate_content_type(request.content_type)
        if content_type is not True:
            return content_type
        
        redlag_id_validation = RedFlagModel.validate_id(id)
        
        if redlag_id_validation is not True:
            return redlag_id_validation

        if 'location' not in request.json:
            return jsonify({"status": 400, "error":"wrong location format. follow this example ->> {'location':[12.3453,9.6589]}"}),400

        get_location = request.get_json()
        validate_result = RedFlagModel.edit_location_validation(get_location['location'], redflags_list, int(id))
   
        if validate_result is not True:
            return validate_result

        get_record = [redflag.__dict__ for redflag in redflags_list if redflag.__dict__['id'] == int(id)]
        get_record[0]['location'] = get_location['location']

        return jsonify({"status":400, "data":[{"id":int(id), "message":"Updated red-flag record’s location"}]})

    # Delete a specific red flag record
    def delete(self, id):
        delete_id_validation = RedFlagModel.validate_id(id)
        if delete_id_validation is not True:
            return delete_id_validation
        get_redflag_record = [rf_record for rf_record in redflags_list if rf_record.__dict__['id'] == int(id) ]

        if not get_redflag_record:
            return jsonify({"status":404, "error":"Red-flag not found"}),404
        
        if get_redflag_record[0].__dict__['status'] in ['under investigation','rejected','resolved']:
            return jsonify({"status":400, "error": "You can no longer edit or delete this red-flag"}),400

        redflags_list.remove(get_redflag_record[0])

        return jsonify({"status":200, "data":[{"id":int(id), "message":"red-flag record has been deleted"}]})


class EditComment(MethodView):

    def put(self, id):
        if request.content_type != 'application/json':
            return jsonify({"status":400, "error":"The content type must be json"}), 400

        edit_id_validation = RedFlagModel.validate_id(id)
        
        if edit_id_validation is not True:
            return edit_id_validation

        if 'comment' not in request.json:
            return jsonify({"status": 400, "error":"wrong location format. follow this example ->> {'comment':'Bribery'}"}),400

        get_comment = request.get_json()
        edit_validation_result = EditComment.comment_validations(get_comment['comment'], redflags_list, int(id))

        if edit_validation_result is not True:
            return edit_validation_result

        redflag_record = [single_record.__dict__ for single_record in redflags_list if single_record.__dict__['id'] == int(id)]
        redflag_record[0]['comment'] = get_comment['comment']

        return jsonify({"status":400, "data":[{"id":int(id), "message":"Updated red-flag record’s comment"}]})

    def comment_validations(comment, redflags_list, redflag_id):
        
        # comment
        if RedFlagModel.validate_comment(comment) is not True:
            return jsonify({"status":400, "error": RedFlagModel.validate_comment(comment)}),400
        
        #check if the id matches a particular red-flag in the list
        redflag_record = [record.__dict__ for record in redflags_list if record.__dict__['id'] == int(redflag_id) ]
        if not redflag_record:
            return jsonify({"status":404, "error":"Red-flag not found"}),404

        if redflag_record[0]['status'] in ['under investigation','rejected','resolved']:
            return jsonify({"status":400, "error": "Sorry, you can no longer edit or delete this red-flag"}),400

        return True
    





