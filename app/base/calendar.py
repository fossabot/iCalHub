# Simple wrapper for the calendar

import uuid
import copy
import json
from typing import List, Dict


import icalendar
from SecretColors.palette import Palette


class Calendar(object):
    def __init__(self, name: str):
        """
        Constructor
        :param name: The name of the calendar.
        """
        self.cal : Dict = {}
        self.events : List[Dict[str, str]] = []

        self.init_calendar(name)

        material = Palette("material")

        self.set_calendar_color(material.orange())
        self.set_calendar_timezone('Asia/Shanghai')

    def init_calendar(self, name: str) -> None:
        """
        Set initial attributes for the calendar.
        :param name: The name of the calendar.
        :return: None
        """
        self.cal['version'] = '2.0'
        self.cal['name'] = name
        self.cal['x-wr-calname'] = name

    def set_calendar_color(self, color: str):
        self.cal['x-outlook-color'] = color
        self.cal['x-funambol-color'] = color
        self.cal['x-apple-calendar-color'] = color

    def set_calendar_timezone(self, timezone: str):
        self.cal['timezone-id'] = timezone
        self.cal['x-wr-timezone'] = timezone

    def set_calendar_refresh_duration(self, duration):
        self.cal['refresh-interval;value=duration'] = duration

    def add_event(self, event: Dict[str, str]):
        event['uid'] = str(uuid.uuid4()).upper()
        self.events.append(event)

    def to_ical(self) -> str:
        cal: any = icalendar.Calendar()

        for prop in self.cal:
            cal[prop] = self.cal[prop]

        for event in self.events:
            evt: any = icalendar.Event()

            for prop in event:
                evt[prop] = event[prop]

            cal.add_component(evt)

        return cal.to_ical().decode('utf-8')

    def to_json(self) -> str:
        cal = copy.deepcopy(self.cal)
        events = copy.deepcopy(self.events)

        cal['events'] = events

        return json.dumps(cal).encode('utf8')
