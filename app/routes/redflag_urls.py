from app.views.red_flag_view import RedFlagView

class Routes:
    
    @staticmethod
    def fetch_urls(app):
        redflag_views  = RedFlagView.as_view('ireporter')
        app.add_url_rule('/api/v1/red-flags', defaults={'id': None},
                         view_func=redflag_views, methods=['GET',])
        app.add_url_rule('/api/v1/red-flags', view_func=redflag_views, methods=['POST',])
        app.add_url_rule('/api/v1/red-flags/<id>', view_func=redflag_views,  methods=['GET', 'PUT', 'DELETE'])
        
       