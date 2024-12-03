#!/usr/bin/env python

import subprocess
import optparse
import re

def get_arguments():
    parser = optparse.OptionParser()

    parser.add_option("-i", "--interface", dest="interface", help="Interface tp change its MAC Address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")

    (options, arguments) =  parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify an interface, use --help for more info.")        
    elif not options.new_mac:
        parser.error("[-] Please specify an new mac, use --help for more info.")
    return options

def change_mac(interface, new_mac):
    # interface = raw_input("interface > ")
    # new_mac = raw_input("New MAC >")

    print("[+] Changing MAC Address for " + interface + " to " + new_mac)

    # subprocess.call("ifconfig " + interface + " down", shell=True)
    # subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
    # subprocess.call("ifconfig " + interface + " up", shell=True)

    subprocess.call(["ifconfig" , interface , "down"])
    subprocess.call(["ifconfig" , interface , "hw", "ether" , new_mac])
    subprocess.call(["ifconfig" , interface , "up"])

def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    # print(ifconfig_result)
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_result))
    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[-] Could not read MAC Address")
    
# interface = options.interface
# new_mac = options.new_mac

options = get_arguments()

current_mac = get_current_mac(options.interface)
print("Current MAC = " + str(current_mac))

change_mac(options.interface, options.change_mac)

current_mac = get_current_mac(options.interface)
if current_mac == options.new_mac:
    print("[+] MAC address was sucessfully changed to " + current_mac)
else:
    print("[-] MAC address did not get chaged.")