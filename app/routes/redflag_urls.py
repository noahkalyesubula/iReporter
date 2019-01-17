"""this file contains url patterns for the api endpoints"""
from app.views.red_flag_view import RedFlagView, EditComment

class Routes:
    """API Routes class"""
    @staticmethod
    def fetch_urls(app):
        """API endpoints urls"""
        redflag_views = RedFlagView.as_view('ireporter')
        edit_comment  = EditComment.as_view('update_comment')
        app.add_url_rule('/api/v1/red-flags', defaults={'id': None},
                         view_func=redflag_views, methods=['GET',])
        app.add_url_rule('/api/v1/red-flags', view_func=redflag_views, methods=['POST',])
        app.add_url_rule('/api/v1/red-flags/<id>/location', view_func=redflag_views, methods=['PUT',])
        app.add_url_rule('/api/v1/red-flags/<id>/comment', view_func=edit_comment, methods=['PUT',])
        app.add_url_rule('/api/v1/red-flags/<id>', view_func=redflag_views, methods=['GET', 'DELETE'])
             