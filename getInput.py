from os import mkdir
from os.path import isfile, isdir
from requests import get
from sys import argv


def get_input(day: int) -> None:
    data = _download_input(day)
    _save_input(day, data)


def _download_input(day: int) -> str:
    url = f"https://adventofcode.com/2023/day/{day}/input"
    cookies = {'session': _get_session()}

    response = get(url, cookies=cookies)
    if response.status_code == 404:
        print(f'Day {day} is not available yet.')
        exit()
    response.raise_for_status()

    return response.text


def _get_session() -> str:
    file = 'session.txt'
    if not isfile(file):
        print(f'{file} does not seem to exist. Please create it in the project root directory and add your AoC session token.')
        exit()

    with open(file, 'r') as f:
        session = f.read()
    if session == '':
        print(f'session.txt appears to be empty. Please add your session token.')
        exit()
    return session


def _save_input(day: int, data: str) -> None:
    dir = f'./Days/Day{day:02d}'
    if not isdir(dir):
        mkdir(dir)
    file = f'{dir}/input.txt'
    with open(file, 'w') as f:
        f.write(data)
    return


if __name__ == '__main__':
    if len(argv) <= 1:
        print(f'Specify a Day to get the 2023 input for, or use the --all flag to get all available inputs.')
        exit()
    if len(argv) > 2:
        print(f'Too many arguments. Please only input the Day.')
        exit()

    if argv[1] == '--all':
        # Get all available inputs
        for day in range(1, 26):
            get_input(day)
        exit()

    if not argv[1].isdigit():
        print(f'Day must be a number.')
        exit()

    day = int(argv[1])

    if day not in range(1, 26):
        valid = False
        print(f'Day must be a value from 1-25.')
        exit()

    get_input(day)
