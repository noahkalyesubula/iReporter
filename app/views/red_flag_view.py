import datetime
from flask import request, jsonify
from flask.views import MethodView
from app.models.red_flag_model import RedFlagModel

class RedFlagView(MethodView):
    redflags_list = []

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
        
        redflag_id = len(self.redflags_list) + 1
        # Add a new red-flag record
        new_redflag_record = RedFlagModel(id = redflag_id, createdBy = request.json['createdBy'], title = request.json['title'], \
                createdOn = str(datetime.datetime.now()), location = request.json['location'], status= 'draft', comment = request.json['comment'])
        
        self.redflags_list.append(new_redflag_record)
        return jsonify({"status":201, "data":[{"id":redflag_id, "message":"Created red-flag record"}]}),201


