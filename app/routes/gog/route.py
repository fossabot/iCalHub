from flask import Blueprint, Response


from .service import generate_upcoming_calendar


gog = Blueprint('gog', __name__)


@gog.route('/upcoming')
def upcoming():
    calendar = generate_upcoming_calendar()
    return Response(calendar, mimetype='text/calendar; charset=UTF-8')