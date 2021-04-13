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

def add_rule(rule_name, ip):
    """ Add rule to Windows Firewall """
    subprocess.call(
        f"netsh advfirewall firewall add rule name={rule_name} dir=out action=block remoteip={ip} protocol=TCP",
        shell=True, 
        stdout=DEVNULL, 
        stderr=DEVNULL
    )
    print(f"Rule {rule_name} added")

def modify_rule(rule_name, state):
    """ Enable/Disable specific rule, 0 = Disable / 1 = Enable """
    state, message = ("yes", "Enabled") if state else ("no", "Disabled")
    subprocess.call(
        f"netsh advfirewall firewall set rule name={rule_name} new enable={state}", 
        shell=True, 
        stdout=DEVNULL, 
        stderr=DEVNULL
    )
    print(f"Rule {rule_name} {message}")

if __name__ == '__main__':
    config = read_yaml(".\config.yaml")
    lol_config_file = config['config']['dir']
    region = config['config']['region']
    lol_config = read_yaml(lol_config_file)
    host = lol_config['region_data'][region]['servers']['chat']['chat_host']
    ip = socket.gethostbyname(host)
    check_admin()
    add_rule("lolchat", ip)
    modify_rule("lolchat", 1)