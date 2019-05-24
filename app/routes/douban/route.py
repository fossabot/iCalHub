from flask import Blueprint, Response


from .service import generate_upcoming_calendar


douban = Blueprint('douban', __name__)


@douban.route('/upcoming')
def upcoming():
    calendar = generate_upcoming_calendar()
    return Response(calendar, mimetype='text/calendar; charset=UTF-8')
