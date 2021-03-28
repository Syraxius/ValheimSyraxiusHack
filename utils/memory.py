import pymem


# Adapted from: pymem.pattern.scan_pattern_module.
# This allows scanning of the entire process memory rather than by modules
def pattern_scan_process(handle, pattern):
    curr_address = handle
    while True:
        next_address, found = pymem.pattern.scan_pattern_page(handle, curr_address, pattern)
        if found:
            break
        if next_address <= handle:  # Not found
            break
        curr_address = next_address
    return found
