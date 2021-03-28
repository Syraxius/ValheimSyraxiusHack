import time
import logging
import pymem
from config import hack_table
from utils.helpers import toggle_hack, check_hack_state

logger = logging.getLogger('pymem')
logger.setLevel(logging.ERROR)


def main():
    print('Initializing...')
    process_name = 'valheim.exe'
    while True:
        print('Searching for %s' % process_name)
        try:
            pm = pymem.Pymem(process_name)
            break
        except pymem.exception.ProcessNotFound:
            print('%s process not found, have you started it? Retrying in 5 seconds')
            time.sleep(5)

    hacks = sorted(hack_table.keys())

    print('Checking state of all hacks...')
    for hack in hacks:
        hack_table[hack]['state'] = check_hack_state(pm, hack_table, hack)

    print('---------------------')
    print('Valheim Syraxius Hack')
    print('---------------------')
    while True:
        print('==========')
        print('Hack Menu:')
        print('==========')
        print('0. Exit')
        id = 1
        for hack in hacks:
            print('%s. %s: %s' % (id, hack_table[hack]['name'], hack_table[hack]['state'].capitalize()))
            if hack_table[hack]['state'] == 'undefined':
                print('   Note: %s' % hack_table[hack]['undefined_help'])
            id += 1
        print('Toggle:')
        try:
            choice = int(input())
            if choice == 0:
                break
            if hack_table[hack]['state'] == 'on':
                toggle_hack(pm, hack_table, hack, toggle_on=False)
            else:
                success = toggle_hack(pm, hack_table, hack, toggle_on=True)
                if not success:
                    print('There was an issue toggling this hack, try again.')
        except:
            print('Invalid input, try again.')


if __name__ == '__main__':
    main()
