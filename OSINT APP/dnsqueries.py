import socket
import dns.resolver
import re


class Dnsqueries:

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

    # This function performs the DNS querying for the domain provided by the user.
    # The DNS record types are stored in a list.
    # The dns.resolver library is used to
    def query_records(self):
        output_file = self.domain_name + "-DNS_Queries.txt"
        # This list contains various dns record types to query against the domain
        record_list = [
            'NONE',
            'A',
            'NS',
            'MD',
            'MF',
            'CNAME',
            'SOA',
            'MB',
            'MG',
            'MR',
            'NULL',
            'WKS',
            'HINFO',
            'MINFO',
            'MX',
            'TXT',
            'RP',
            'AFSDB',
            'X25',
            'ISDN',
            'RT',
            'NSAP',
            'NSAP-PTR',
            'SIG',
            'KEY',
            'PX',
            'GPOS',
            'AAAA',
            'LOC',
            'NXT',
            'SRV',
            'NAPTR',
            'KX',
            'CERT',
            'A6',
            'DNAME',
            'OPT',
            'APL',
            'DS',
            'SSHFP',
            'IPSECKEY',
            'RRSIG',
            'NSEC',
            'DNSKEY',
            'DHCID',
            'NSEC3',
            'NSEC3PARAM',
            'TLSA',
            'HIP',
            'CDS',
            'CDNSKEY',
            'CSYNC',
            'SPF',
            'UNSPEC',
            'EUI48',
            'EUI64',
            'TKEY',
            'TSIG',
            'IXFR',
            'AXFR',
            'MAILB',
            'MAILA',
            'ANY',
            'URI',
            'CAA',
            'TA',
            'DLV',
        ]

        print("Processing queries. Please wait.")
        for record_type in record_list:
            try:
                answers = dns.resolver.resolve(self.domain_name, record_type)
                for rdata in answers:
                    print("\n" + record_type + ' record: ' + rdata.to_text() + "\n")
            except Exception as e:
                print("\n" + str(e))

        result = dns.resolver.resolve(self.domain_name, 'A')
        try:
            for arecords in result:
                print("\n" + "PTR record for {}: {}".format(self.domain_name,
                                                            socket.gethostbyaddr(arecords.to_text())[0]))
        except Exception as e:
            print('\nNo PTR records found for ' + self.domain_name + " " + str(e))

        print("The DNS querying complete \n")
