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
    dir = f'./Day{day:02d}'
    if not isdir(dir):
        mkdir(dir)
    file = f'{dir}/input.txt'
    with open(file, 'w') as f:
        f.write(data)
    return


if __name__ == '__main__':
    if len(argv) <= 1:
        print(f'Please add the Day to get the 2023 input for.')
        exit()
    if len(argv) > 2:
        print(f'Too many arguments. Please only input the Day.')
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
