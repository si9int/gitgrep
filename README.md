# gitgrep
A simple Python-Wrapper for https://grep.app

#### Requirements
- Python 3
- `pip3 install requests`

#### Usage
```
python3 gitgrep.py <domain> <optional:-json>
```

#### Example

1. Get all repositories and files associated with a domain based (STDOUT)
```
python3 gitgrep.py target.com
---
[-] Printing repositories for target.com 

https://github.com/apparition47/MailTrackerBlocker
https://github.com/datenanfragen/data
https://github.com/MahApps/MahApps.Metro.IconPacks
...

[-] Printing raw-data target.com 

https://raw.githubusercontent.com/apparition47/MailTrackerBlocker/main/Source/MTBBlockedMessage.m
https://raw.githubusercontent.com/datenanfragen/data/master/companies/rewe-shop.json
...
```
2. Output results in JSON
```
python3 gitgrep.py target.com -json
---
{"repos": ["https://github.com/apparition47/MailTrackerBlocker", "https://github.com/datenanfragen/data", ... "files": ["https://raw.githubusercontent.com/apparition47/MailTrackerBlocker/main/Source/MTBBlockedMessage.m", "https://raw.githubusercontent.com/datenanfragen/data/master/companies/rewe-shop.json" ...}
```
