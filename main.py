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

    hacks_names = sorted(hack_table.keys())

    print('Checking state of all hacks...')
    for hack_name in hacks_names:
        hack_table[hack_name]['state'] = check_hack_state(pm, hack_table, hack_name)

    print()
    print('---------------------')
    print('Valheim Syraxius Hack')
    print('---------------------')
    print()
    while True:
        print('==========')
        print('Hack Menu:')
        print('==========')
        hack_id = 1
        for hack_name in hacks_names:
            print('%s. %s: %s' % (hack_id, hack_table[hack_name]['name'], hack_table[hack_name]['state'].capitalize()))
            if hack_table[hack_name]['state'] == 'undefined':
                print('   Note: %s' % hack_table[hack_name]['undefined_help'])
            hack_id += 1
        print('Choice (0 to exit):')
        try:
            choice = int(input())
            if choice == 0:
                break
            hack_name = hacks_names[choice - 1]
            if hack_table[hack_name]['state'] == 'on':
                toggle_hack(pm, hack_table, hack_name, toggle_on=False)
            else:
                success = toggle_hack(pm, hack_table, hack_name, toggle_on=True)
                if not success:
                    print('There was an issue toggling this hack_name, try again.')
        except:
            print('Invalid input, try again.')


if __name__ == '__main__':
    main()
