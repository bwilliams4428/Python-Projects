import subprocess
import re

def display_interfance_menu(list):
    print("Input the numerical value for the network interface to modify its MAC Address:")
    for interface_choice, interface in enumerate(interface_list):
        print("{}. {}".format(interface_choice+1,interface))
    print("Type 'X' to exit ")

def change_mac(interface, new_mac):
    print("[+] Chaning Mac address for {} to {}".format(interface, new_mac))
    # prevent user from executing other commands on the system
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_result))
    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
       print("[-] Could not read Mac address")

def user_selection(choice, nic):
        choice = int(input())-1
        return choice

def check_for_no_mac(interface):
    if re.search(r"(None)", str(get_current_mac(interface))):
        print("Please select a different interface")

user_interface_choice = '-'

system_interfaces = subprocess.check_output(["ls", "/sys/class/net"]).decode('utf-8')
interface_list = list(system_interfaces.split("\n"))
interface_list.pop(len(interface_list) - 1)
display_interfance_menu(interface_list)

while user_interface_choice != 'X':


    user_interface_choice = input()
    if user_interface_choice == 'X':
        print("Exiting script")
    else:
        user_nic = int(user_interface_choice) - 1
        if re.search(r"(None)", str(get_current_mac(interface_list[user_nic]))):
            print("Please select a different interface")
            display_interfance_menu(interface_list)

        else:
            print("Current Mac address for {} interface: {}".format(interface_list[user_nic],get_current_mac(interface_list[user_nic])))
            user_custom_mac = input("Input your custom MAC address for the selected interface(Note: First octet must be an even value):")
            change_mac(interface_list[user_nic],user_custom_mac)
            display_interfance_menu(interface_list)
