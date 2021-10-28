from dnsqueries import Dnsqueries
from subdomainenum import SubDomainEnum
from whoislookup import WhoisClass
from ipwhoislookup import IpLookUp

"""
This application performs DNS queries for a user provided domain, sub domain enumeration for a user provided domain,
whois lookups for TLDs and CCTLD and whois lookup for a user provided IPv4 or the IPv4 for domain's web server. 
"""

print("Simple OSINT App v1.0")

while True:
    # Command Line Interface
    print("Please select an option from the following menu: \n"
          "Input 1 to perform a DNS Query  \n"
          "Input 2 to perform a Subdomain Enumeration \n"
          "Input 3 to perform a Whois Lookup \n"
          "Input 4 to perform an IP Whois Lookup \n"
          "Input Stop to quit app \n")

    user_selection = input(str("Please input your selection: "))

    if user_selection.lower() == 'stop':
        print("Exiting....Goodbye.")
        break

    if user_selection == '1':
        user_domain = input(
            str("Please input a valid domain name or sub domain (format: domain.com or my.domain.com) : "))
        # Creates an object of the Dnsqueries class
        dns_query = Dnsqueries(domain_name=user_domain.lower())
        # Checks if a user provided a valid domain name or sub domain
        if dns_query.isValidDomain():
            # Calls function to perform a DNS query for the domain or sub domain provided by the user
            dns_query.query_records()
        if not dns_query.isValidDomain():
            print("Not a valid domain or sub domain. \n")

    if user_selection == '2':
        user_domain = input(
            str("Please input a valid domain name for sub domain enumeration (format: domain.com or my.domain.com) : "))
        # Creates an object of the SubDomainEnum class
        enum_lookup = SubDomainEnum(domain_name=user_domain.lower())
        # Checks if a user provided a valid domain name or sub domain
        if enum_lookup.isValidDomain():
            # Calls function to perform sub domain enumeration for the domain or sub domain provided by the user
            enum_lookup.subDomEnum()
        if not enum_lookup.isValidDomain():
            print("Not a valid domain. \n")

    if user_selection == '3':
        user_domain = input(str("Please input a valid domain (format: domain.com) : "))
        # Creates an object of the WhoisClass class
        whois_lookup = WhoisClass(domain_name=user_domain)
        # Checks if a user provided a valid domain name
        if whois_lookup.isValidDomain():
            # The following 3 lines of code reads a text file that contains all country code TLDs and saves
            # those to a list
            cc_tlds = open("cctlds.txt", "r")
            cc_tlds_list = cc_tlds.read()
            cc_tlds.close()
            # Calls function to perform whois lookup using the domain name provided by the user
            WhoisClass.getWhoisReport(user_domain, cc_tlds_list)
        if not whois_lookup.isValidDomain():
            print("Not a valid domain. \n")

    if user_selection == '4':
        user_domain = input(str("Please input a valid domain name or IP address (If a domain is inputted then the"
                                "script will obtain the domain's IP automatically. Format: domain.com)): "))
        # Creates an object of the IpLookUp  class
        ipwhois_lookup = IpLookUp(user_domain)
        # Since the user can input an IP or domain name, the if statements validates if a valid IP or domain name was
        # inputted
        if ipwhois_lookup.isValidDomain() or ipwhois_lookup.isValidIP():
            # Calls function to perform ip whois lookup
            ipwhois_lookup.ipWhoisReport()
        else:
            print("Invalid domain or IP. Please input a valid domain name or IP: ")
