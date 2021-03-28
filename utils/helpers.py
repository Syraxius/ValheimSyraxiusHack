from utils.memory import pattern_scan_process


def check_hack_state(pm, hack_table, hack):
    hack_table[hack]['state'] = 'undefined'
    pattern_bef = hack_table[hack]['pattern_bef']
    pattern_aft = hack_table[hack]['pattern_aft']
    address_bef = pattern_scan_process(pm.process_handle, pattern_bef)
    address_aft = pattern_scan_process(pm.process_handle, pattern_aft)
    if address_bef:
        hack_table[hack]['last_address'] = address_bef
        hack_table[hack]['state'] = 'off'
    elif address_aft:
        hack_table[hack]['last_address'] = address_aft
        hack_table[hack]['state'] = 'on'
    return hack_table[hack]['state']


def toggle_hack(pm, hack_table, hack, toggle_on=True):
    if toggle_on:
        pattern = hack_table[hack]['pattern_bef']
        value = hack_table[hack]['value_aft']
    else:
        pattern = hack_table[hack]['pattern_aft']
        value = hack_table[hack]['value_bef']

    address = hack_table[hack].get('last_address')
    if not address:
        address = pattern_scan_process(pm.process_handle, pattern)
        if address is None:
            print('%s: Could not find pattern %s' % (hack, pattern))
            return False
    hack_table[hack]['last_address'] = address

    pm.write_bytes(address, value, len(value))
    if toggle_on:
        hack_table[hack]['state'] = 'on'
    else:
        hack_table[hack]['state'] = 'off'
    return True
