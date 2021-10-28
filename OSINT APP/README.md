## Open Source Intelligence (OSINT) Application v1.0

This is my implementation of a small scale OSINT application. It performs DNS querying, domain and IP whois looks, sub domain enumeration and checks if an IP has been reported for abuse. 

The purpose of this is application was to practice Python by creating something. It utilizes OOP, sockets, API calls to generate data.

This application was developed using Python 3.

The application requires the tldextract and dnspython libraries. If you do not have them installed use pip and the included requirements.txt file to install the libraries:
```
cd ../OSINT APP
pip install -r requirements.txt
```
This application does use APIs for Security Trails and AbuseIPDB. Please create free, developer accounts with those service providers, obtain your own API keys and input the API key parameters in the config.py file.

After those libraries have been installed, execute the main.py file to use the application:
```
python3 main.py
```

![](https://github.com/bwilliams4428/Python-Projects/blob/main/OSINT%20APP/gifs/Option%201.gif)

![](https://github.com/bwilliams4428/Python-Projects/blob/main/OSINT%20APP/gifs/Option2.gif)

![](https://github.com/bwilliams4428/Python-Projects/blob/main/OSINT%20APP/gifs/Option3.gif)

![](https://github.com/bwilliams4428/Python-Projects/blob/main/OSINT%20APP/gifs/option4.gif)

![](https://github.com/bwilliams4428/Python-Projects/blob/main/OSINT%20APP/gifs/option4ip.gif)

![](https://github.com/bwilliams4428/Python-Projects/blob/main/OSINT%20APP/gifs/quit.gif)

The application does run slow. Lots of room for improvement.
