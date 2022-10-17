import requests
from email import header
import json


token = "INSERT_HEADER"
headers = {'Authorization': "Bearer {}".format(token)}


def librenms_port_mac(macadd):
    return (f'''https://librenms.domain.com/api/v0/ports/mac/{macadd}''')


def librenms_get_devices():
    api_get_devices = requests.get("https://librenms.domain.com/api/v0/devices", headers=headers)
    text_api_get_devices = json.loads(api_get_devices.text)
    return(text_api_get_devices)

def librenms_net_one_arp():
    api_search_one = requests.get("https://librenms.domain.com/api/v0/resources/ip/arp/10.10.10.0/24", headers=headers)
    json_api_search_one = api_search_one.json() 
    return(json_api_search_one)

def librenms_net_two_arp():
    api_search_two = requests.get("https://librenms.domain.com/api/v0/resources/ip/arp/10.20.20.0/24", headers=headers)
    json_api_search_two = api_search_two.json() 
    return(json_api_search_two)

def librenms_net_three_arp():
    api_search_three = requests.get("https://librenms.domain.com/api/v0/resources/ip/arp/10.30.30.0/24", headers=headers)
    json_api_search_three = api_search_three.json() 
    return(json_api_search_three)

def librenms_find_port(search_for_mac, text_api_get_devices):
    print("{: <30} {: <30} {: <30}".format("Switch", "Interface", "Description"))
    for macaddresses in search_for_mac["arp"]:
        search_mac = librenms_port_mac(macaddresses["mac_address"])
        api_search_mac = requests.get(search_mac, headers=headers)
        text_search_mac = json.loads(api_search_mac.text)
        for results in text_search_mac["ports"]:
            if results["ifTrunk"] != "dot1Q":            
                devicename = get_devicename_from_id(results["device_id"],text_api_get_devices)
                print("{: <30} {: <30} {: <30}".format(devicename, results["ifDescr"], results["ifAlias"]))

def get_devicename_from_id(device_id, device_id_list):
    for device in device_id_list["devices"]:
        if device["device_id"] == int(device_id):
            return(device["hostname"])