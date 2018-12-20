from app.views.red_flag_view import RedFlagView, EditComment

class Routes:
    
    @staticmethod
    def fetch_urls(app):
        redflag_views = RedFlagView.as_view('ireporter')
        edit_comment  = EditComment.as_view('update_comment')
        app.add_url_rule('/api/v1/red-flags', defaults={'id': None},
                         view_func=redflag_views, methods=['GET',])
        app.add_url_rule('/api/v1/red-flags', view_func=redflag_views, methods=['POST',])
        app.add_url_rule('/api/v1/red-flags/<id>/location', view_func=redflag_views,  methods=['PUT',])
        app.add_url_rule('/api/v1/red-flags/<id>/comment', view_func=edit_comment,  methods=['PUT',])
        app.add_url_rule('/api/v1/red-flags/<id>', view_func=redflag_views,  methods=['GET','DELETE'])
        
        
       