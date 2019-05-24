from typing import List, Dict


from app.base.calendar import Calendar
from .spiders.upcoming import get_game_details


def generate_upcoming_calendar() -> str:
    calendar = Calendar(name='GOG.com Upcoming')
    calendar.set_calendar_color('#1C88CB')
    calendar.set_calendar_refresh_duration('PT6H0M0S')

    for game in get_game_details():
        event = dict()
        event['summary'] = game['name']
        event['dtstart;value=date'] = game['date']
        event['dtstamp'] = game['stamp']

        calendar.add_event(event)

    return calendar.to_ical()
