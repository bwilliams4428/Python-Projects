import socket
import re
import requests
import config


class IpLookUp:

    def __init__(self, domain_name_or_ip):
        self.domain_name_or_ip = domain_name_or_ip

    def isValidDomain(self):
        # Regex to check valid
        # domain name.
        regex = "^((?!-)[A-Za-z0-9-]" + "{1,63}(?<!-)\\.)" + "+[A-Za-z]{2,24}"

        # Compile the ReGex
        p = re.compile(regex)

        # If the string is empty
        # return false
        if self.domain_name_or_ip is None:
            return False

        # Return if the string
        # matched the ReGex
        if re.search(p, self.domain_name_or_ip):
            return True
        else:
            return False

    # Checks if IP is valid
    def isValidIP(self):

        regex = "^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
        p = re.compile(regex)

        if self.domain_name_or_ip is None:
            return False
        if re.search(p, self.domain_name_or_ip):
            return True
        else:
            return False

    # This functions generates an IP whois report by using sockets to connect to ARIN's whois server and generate the
    # record data. It also calls another function which uses abuseipdb.com's API to check if the IP has any abuse
    # reports and provides its abuse confidence score.

    def ipWhoisReport(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        if self.isValidDomain():
            hostip = socket.gethostbyname(self.domain_name_or_ip)
            print("The IP for {} is {}".format(self.domain_name_or_ip, hostip))
            s.connect(("whois.arin.net", 43))
            s.send((hostip + "\r\n").encode())
            printWhois(s)
            abuseIP(hostip)
        if self.isValidIP():
            s.connect(("whois.arin.net", 43))
            s.send((self.domain_name_or_ip + "\r\n").encode())
            printWhois(s)
            abuseIP(self.domain_name_or_ip)


# This function uses abuseipdb.com's API to check if the IP has any abuse reports and provides its abuse confidence
# score.
def abuseIP(ip):
    url = 'https://api.abuseipdb.com/api/v2/check'

    headers = {
        'Accept': 'application/json',
        'Key': config.abip_api_key  # input your personal API key from your abuseipdb.com account
    }
    querystring = {
        'ipAddress': ip,
        'verbose': ''
    }
    response = requests.request(method='GET', url=url, headers=headers, params=querystring)

    abusedip_data = response.json()['data']
    if abusedip_data["totalReports"] >= 1:
        print("{} was listed by Abusedb with an abuse confidence score of {} and a total of {} reports".format(
            ip, abusedip_data[
                "abuseConfidenceScore"], abusedip_data["totalReports"]))
        print("For more detail data please visit https://www.abuseipdb.com/check/{} \n".format(ip))
    else:
        print("Hooray. There are no reports for your IP at abuseipdb.com. \n")


# This function prints the whois report
def printWhois(Socket):
    response = b""
    while True:
        data = Socket.recv(4096)
        response += data
        if not data:
            break
    Socket.close()
    print(response.decode())
