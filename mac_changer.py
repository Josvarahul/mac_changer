#!/usr/bin/env python
import subprocess
import optparse
import re
print("      #############################################")
print("      #             MAC SPOOFER TOOL              #")
print("      #         ***********************           #")
print("      #############################################")
print("                                  -created by josva_rahul                  ")
print()
print("     ***this tool is only for educational purpose***"  )
print("                      ")
print()
print()
print("[+]lets start spoofing....")
def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="enter the interface for mac")
    parser.add_option("-m", "--mac", dest="new_mac", help="enter the new_mac address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] please specify the interface or --help for help")
    if not options.new_mac:
        parser.error("[-] please specify the new_mac address or --help for help")

    return options

def mac_changer(interface,new_mac):
    print("[+] spoofing mac address........")
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether",new_mac])
    subprocess.call(["ifconfig", interface, "up"])


def get_current_mac(interface):
    result = subprocess.check_output(["ifconfig", interface])
    result = str(result)
    mac_in_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", result, flags=0)
    if mac_in_search_result:
        return mac_in_search_result.group(0)
    else:
        print("[-] mac no found ")

options = get_arguments()
current_mac = get_current_mac(options.interface)
print("[+] THE CURRENT MAC ADDRESS IS ", current_mac)
print()
mac_changer(options.interface,options.new_mac)

current_mac = get_current_mac(options.interface)
if current_mac == options.new_mac:
    print("[+] The mac address is spoofed successfully to", current_mac)
    print()
else:
    print("[-] cannot spoof the mac address")
    print()

print(" ###############   happy hacking ........################")