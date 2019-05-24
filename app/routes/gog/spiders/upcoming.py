from typing import List, Dict


import moment
import requests


def get_upcoming_games() -> List:
    url = 'https://www.gog.com/games/ajax/filtered?availability=coming&mediaType=game'
    response = requests.get(url)

    if response.status_code != 200:
        return []

    content = response.json()
    products = content['products']

    return products


def get_game_details() -> Dict[str, str]:
    games : List = get_upcoming_games()
    for game in games:
        try:
            date: str = moment.unix(game['globalReleaseDate']).strftime('%Y%m%d')
            name: str = game['title']
            stamp: str = '{}T000000Z'.format(date)

            yield {
                'date': date,
                'name': name,
                'stamp': stamp
            }
        except TypeError:
            continue
