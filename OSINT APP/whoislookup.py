import socket
import re
import tldextract


class WhoisClass:

    def __init__(self, domain_name):
        self.domain_name = domain_name

    def isValidDomain(self):
        # Regex to check valid
        # domain name.
        regex = "^((?!-)[A-Za-z0-9-]" + "{1,63}(?<!-)\\.)" + "+[A-Za-z]{2,24}"

        # Compile the ReGex
        p = re.compile(regex)

        # If the string is empty
        # return false
        if self.domain_name is None:
            return False

        # Return if the string
        # matched the ReGex
        if re.search(p, self.domain_name):
            return True
        else:
            return False

    def getWhoisReport(self, cclist):
        # Python module to extract parts of the domain name and saves the TLD into a tld variable
        tld = tldextract.extract(self)
        # Creates a socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # If varaible tld is a country code TLD then access then query the IANA whois database for country code domains
        if tld[2] in cclist:
            s.connect(("whois.iana.org", 43))
            # convert string to bytes, socket need bytes
            s.send((self + "\r\n").encode())
        # If not a country code TLD then query Internic's whois database for the whois record data
        else:
            s.connect(("whois.internic.net", 43))
            # convert string to bytes, socket need bytes
            s.send((self + "\r\n").encode())
        # Function prints whois report
        printWhois(s)


# This function filters the whois data obatined by the socket and prints it
def printWhois(Socket):
    response = b""
    while True:
        data = Socket.recv(4096)
        response += data
        if not data:
            break
    Socket.close()
    print(response.decode())
