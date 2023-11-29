from sys import argv
from os.path import isdir, isfile, dirname
from os import mkdir


def create_files(num):
    """Will only create folder/files if they don't exist."""
    day = str(num)
    if len(day) == 1:
        day = '0' + day
    project_dir = dirname(__file__)
    day_dir = project_dir + f'\\Day{day}'

    # Create Folder if it doesn't exist
    if not isdir(day_dir):
        mkdir(day_dir)

    # Create empty txt input files
    if not isfile(day_dir + f'\\input.txt'):
        f = open(day_dir + f'\\input.txt', 'w')
        f.close()
    if not isfile(day_dir + f'\\t_input.txt'):
        f = open(day_dir + f'\\t_input.txt', 'w')
        f.close()

    # Create the .py file
    if not isfile(day_dir + f'\\day_{day}.py'):
        with open(day_dir + f'\\day_{day}.py', 'w') as f:
            # Read data from Template .py file and replace ?? with 'day' variable
            with open(f'{project_dir}\\Template.py', 'r') as template:
                data = template.read()
            data = data.replace('??', day)
            f.write(data)


def main():
    if len(argv) <= 1:  # Too few args
        print("Please provide a day #")
        return
    if len(argv) > 2:  # Too many args
        print("Please provide only 1 argument")
        return
    if not argv[1].isdigit():  # Arg is not a number
        print("Invalid argument. Value must be a number.")
        return
    # Add another check to ensure it's within the 1-25 range?

    create_files(argv[1])


if __name__ == '__main__':
    main()
