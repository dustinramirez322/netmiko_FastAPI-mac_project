from netmiko import ConnectHandler
import dotenv
import os
import ast
import re

# Load switch information from .env
dotenv.load_dotenv()
switch = ast.literal_eval(os.environ.get("MAC_LOC"))

# Get a list of mac addresses in list form from a ddwrt device
def get_wrt_macs():
    # Connect to access points and run command
    device = ConnectHandler(**switch)
    device_info = device.send_command('wl_atheros assoclist')

    # Strip out macs into a list
    mac_format = re.compile(r'(?:[0-9a-fA-F]:?){12}')
    mac_list = re.findall(mac_format, device_info)

    return mac_list
