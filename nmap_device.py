# These classes hold each device discovered by the NMAP scan


class NMAPDevice:
    def __init__(self, hostname, state, ip, mac):
        self.hostname = hostname
        self.state = state
        self.ip = ip
        self.mac = mac
        #  self.protocols = protocols()

    def printhostname(self):
        print("The hostname for the device is: " + self.hostname + " and it's state is....: " + self.state)

    def print_information(self):
        print("***********************************")
        print("IP Address:- " + self.ip)
        print("Hostname:- " + self.hostname)
        print("Current State:- " + self.state)


