from app.base.calendar import Calendar
from .spiders.upcoming import get_movie_item


def generate_upcoming_calendar():
    calendar = Calendar('即将上映电影')
    calendar.set_calendar_color('#1C88CB')
    calendar.set_calendar_refresh_duration('PT6H0M0S')

    for movie in get_movie_item():
        event = dict()
        event['summary'] = movie['name']
        event['dtstart;value=date'] = movie['date']
        event['dtstamp'] = movie['stamp']

        calendar.add_event(event)

    return calendar.to_ical()
