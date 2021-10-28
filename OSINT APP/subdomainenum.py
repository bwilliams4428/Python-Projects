import requests
import json
import re
import config


class SubDomainEnum:

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

    # This function uses the securitytrails.com API to obtain a list of domains for the user provided domain
    def subDomEnum(self):
        domain = self.domain_name
        print("Enumerating.....Please wait.")
        url = "https://api.securitytrails.com/v1/domain/" + domain + "/subdomains"
        querystring = {"children_only": "true"}
        headers = {
            'accept': "application/json",
            'apikey': config.api_key}  # Use your own API key from your own account with securitytrails.com
        response = requests.request("GET", url, headers=headers, params=querystring)
        result_json = json.loads(response.text)
        sub_domains = [i + '.' + domain for i in result_json['subdomains']]
        for i in sub_domains:
            print(i)

        print("Sub domain enumeration complete. \n")
