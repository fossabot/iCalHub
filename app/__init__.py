from flask import Flask


def register_routes(app):
    from .routes.gog import route as gog_route
    from .routes.douban import route as douban_route

    app.register_blueprint(gog_route, url_prefix='/game/gog')
    app.register_blueprint(douban_route, url_prefix='/movie/douban')


def create_app() -> object:
    app = Flask(__name__)

    register_routes(app)

    return app
