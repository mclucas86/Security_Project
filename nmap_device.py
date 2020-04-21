# These classes hold each device discovered by the NMAP scan


class NMAPDevice:
    def __init__(self, hostname, state):
        self.hostname = hostname
        self.state = state

    def printhostname(self):
        print("The hostname for the device is: " + self.hostname + " and it's state is....: " + self.state)

