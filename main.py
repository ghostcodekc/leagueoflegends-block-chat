import yaml
import socket
import subprocess, ctypes, os, sys
from subprocess import Popen, DEVNULL

def read_yaml(file_path):
    with open(file_path, "r") as f:
        return yaml.safe_load(f)

def check_admin():
    """ Force to start application with admin rights """
    try:
        isAdmin = ctypes.windll.shell32.IsUserAnAdmin()
    except AttributeError:
        isAdmin = False
    if not isAdmin:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)

def check_for_firewall_rule(firewall_rule_name):
    """ Check for existing rule in Windows Firewall """
    print("Checking to see if firewall rule exists")
    x = subprocess.call(
        f"netsh advfirewall firewall show rule {firewall_rule_name}",
        shell=True, 
        stdout=DEVNULL, 
        stderr=DEVNULL
    )
    if x == 0:
        print(F"Rule exists.")
        return True
    else: 
        print(F"Rule does not exist.")
        return False

def add_or_modify_rule(firewall_rule_name, state, firewall_exists, ip):
    """ Add Rule if the rule doesn't already exist. Delete the rule if the rule exists. """
    if firewall_exists and state == 1:
        delete_rule(firewall_rule_name)
        add_rule(firewall_rule_name, ip)
    if firewall_exists and state == 0:
        delete_rule(firewall_rule_name)
    if not firewall_exists and state == 1:
        add_rule(firewall_rule_name, ip)
    if not firewall_exists and state == 0:
        print("Firewall rule does not exist, and `block chat` is set to disabled")

def delete_rule(firewall_rule_name):
    subprocess.call(
        f"netsh advfirewall firewall delete rule name={firewall_rule_name}", 
        shell=True, 
        stdout=DEVNULL, 
        stderr=DEVNULL
    )
    print(f"Rule '{firewall_rule_name}' deleted")

def add_rule(firewall_rule_name, ip):
    """ Add rule to Windows Firewall """
    subprocess.call(
        f"netsh advfirewall firewall add rule name={firewall_rule_name} dir=out action=block remoteip={ip} protocol=TCP",
        shell=True, 
        stdout=DEVNULL, 
        stderr=DEVNULL
    )
    print(f"Current League of Legends Chat IP Address: {ip}. \nRule {firewall_rule_name} added. ")

if __name__ == '__main__':
    config = read_yaml(".\config.yaml")
    state = config['config']['block_chat']
    firewall_rule_name = config['config']['firewall_rule_name']
    lol_config_file = config['config']['dir']
    region = config['config']['region']
    lol_config = read_yaml(lol_config_file)
    host = lol_config['region_data'][region]['servers']['chat']['chat_host']
    ip = socket.gethostbyname(host)
    check_admin()
    firewall_exists = check_for_firewall_rule(firewall_rule_name)
    add_or_modify_rule(firewall_rule_name, state, firewall_exists, ip)