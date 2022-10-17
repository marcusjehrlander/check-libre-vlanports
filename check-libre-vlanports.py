#!/usr/bin/python3


from email import header
import requests
import json
import signal
import sys
from libreapi import librenms_get_devices, librenms_net_one_arp, librenms_net_two_arp, librenms_find_port, librenms_net_three_arp

signal.signal(signal.SIGPIPE, signal.SIG_DFL) # IOError: Broken pipe
signal.signal(signal.SIGINT, signal.SIG_DFL) #Keyboardinterrupt: Ctrl-C

def main():
    # Gather all device IDs
    text_api_get_devices = librenms_get_devices()

    # IP-range 1
    print("-----")
    print("Checking IP-range 1.")
    json_api_search_one = librenms_net_one_arp()
    check_one = librenms_find_port(json_api_search_one, text_api_get_devices)

    # IP-range 2
    print("-----")
    print("Checking IP-range 2.")
    json_api_search_two = librenms_net_two_arp()
    check_two = librenms_find_port(json_api_search_two, text_api_get_devices)

    # IP-range 3
    print("-----")
    print("Checking IP-range 3.")
    json_api_search_three = librenms_net_three_arp()
    check_three = librenms_find_port(json_api_search_three, text_api_get_devices)

    sys.exit()

if __name__ == '__main__':
    main()