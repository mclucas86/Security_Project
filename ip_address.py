import socket
import os
import re
import subprocess

ip_check = re.compile(r'(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.('
                      r'25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.('
                      r'25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.('
                      r'25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)')


# get_IP uses the socket import and connects to the IP 10.255.255.255. The IP which is used to connect
# to this socket is the IP address of the local machine. This is then returned to the user for further
# use in the application.
def get_ip():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        sock.connect(('10.255.255.255', 1))
        ip = sock.getsockname()[0]
        return ip
    except:
        print("Sorry, unable to detect the IP address from the host")
        return '127.0.0.1'
    finally:
        sock.close()


# get_Hostname acquires the hostname of the computer running the application. This is used in the final
# report of the results.
def get_hostname():
    try:
        hostname = socket.gethostname()
        return hostname
    except:
        print("Unable to retrieve hostname")


# Pings an IP which is presented by the user. Calls the OS.System, and uses the command line utility ping,
# alongside -n 4 (4 packets) and also -4 (IPv4)
def ping_ip():
    os.system('clear')
    print("Please enter an IP address to ping (In the format aaa.bbb.ccc.ddd)")
    ip = input("IP: ")

    if check_ip(ip):
        iterations = input("No. of iterations. Leave blank for default [4]")
        if iterations == "":
            iterations = 4
        os.system(f'ping -c {iterations} {ip}')
        print("")
        input("Please press the enter key to return to the main menu")
    else:
        print("")
        input("Incorrect IP. Please press enter to try again.")
        ping_ip()


# Using the module OS, the name of the operating system is devised as either: nt (Windows), posix (Linux) or other.
# This method discovers this and returns it to the user.
def get_os(option):
    switcher = {
        "win32": "Windows",
        "linux": "Linux",
        "darwin": "Mac OS",
        "aix": "AIX",
        "cygwin": "Windows / Cygwin"
    }
    return switcher.get(option, "Unknown OS")


def check_ip(ip):
    if re.search(ip_check, ip):
        return True
    else:
        return False


def get_netmask(ip):
    cidr = subprocess.check_output(["ip", "-o", "addr", "show"], stderr=subprocess.STDOUT).decode()
    netmask_output = re.findall(str(ip) + "\/[0-9][0-9]", cidr)
    temp_ip = "".join(netmask_output)
    netmask = re.sub(ip_check, "", temp_ip)
    return netmask


def get_default_gateway():
    gw_output = ""
    ps = subprocess.Popen(("ip", "r"), stdout=subprocess.PIPE)
    gw = subprocess.check_output(["grep", "default"], stdin=ps.stdout).decode()
    temp_output = re.findall(ip_check, gw)
    for x in temp_output:
        gw_output = ".".join(x)
    return gw_output
