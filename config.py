hack_table = {
    # To find the stamina value, search for 75.0 when you are completely starved
    'unlimited_stamina': {
        'name': 'Unlimited Stamina',
        'undefined_help': 'You will need to invoke an in-game action that reduces stamina before the hack can be toggled',
        'pattern_bef': rb'\xF3\x0F\x11\xAE\x5C\x05\x00\x00\xF3\x0F\x10\x86\x5C\x05\x00\x00',
        'pattern_aft': rb'\x90\x90\x90\x90\x90\x90\x90\x90\xF3\x0F\x10\x86\x5C\x05\x00\x00',
        'value_bef': b'\xF3\x0F\x11\xAE\x5C\x05\x00\x00\xF3\x0F\x10\x86\x5C\x05\x00\x00',
        'value_aft': b'\x90\x90\x90\x90\x90\x90\x90\x90\xF3\x0F\x10\x86\x5C\x05\x00\x00',
    },
    # To find the health value, repeatedly range search your current health value in float when full
    'unlimited_health': {
        'name': 'Unlimited Health',
        'undefined_help': 'You will need to invoke an in-game action that reduces health before the hack can be toggled',
        'pattern_bef': rb'\xF3\x0F\x11\x68\x0C\x49\x63\x47\x44',
        'pattern_aft': rb'\x90\x90\x90\x90\x90\x49\x63\x47\x44',
        'value_bef': b'\xF3\x0F\x11\x68\x0C\x49\x63\x47\x44',
        'value_aft': b'\x90\x90\x90\x90\x90\x49\x63\x47\x44',
    },
}
