<p align="center">
<br><br><br>
<a https://api.c99.nl/"><img src="https://api.c99.nl/assets/images/logo.png" width="100px"></a>
<br><br><br>
</p>

<p align="center">
<b>Seamlessly integrate the c99.nl API into your Python projects</b>
</p>

<p align=center>
<a href="https://pypi.org/project/c99api/"><img src="https://badgen.net/pypi/v/c99api/"></a>
<a href="https://github.com/Haste171/c99-api/releases"><img src="https://badgen.net/github/release/Haste171/c99-api">
<a href="https://gitHub.com/Haste171/c99-api/graphs/commit-activity"><img src="https://img.shields.io/badge/Maintained%3F-yes-green.svg">
<a href="https://github.com/Haste171/c99-api/blob/master/LICENSE"><img src="https://img.shields.io/github/license/Haste171/c99-api">
<a href="http://makeapullrequest.com"><img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square">

</a>

# Installation

```
pip install c99api
```

**Initiator**
```python
# Import the package
from c99api import EndpointClient

api = EndpointClient

# Define your API key
api.key = 'your_key'
```

# Usage

```python 
# Access list of different methods available
response = api.list_methods()
print(response)
```
```python
[
    'phonelookup',
    'emailvalidator',
    'disposablemailchecker',
    'portscanner',
    'portscanner_port',
    'ping',
    'gethostname',
    'dnschecker',
    'dnsresolver',
    'ipvalidator',
    'torchecker',
    'iplogger',
    'proxydetector',
    'subdomainfinder',
    'firewalldetector',
    'ip2domains',
    'alexarank',
    'whois',
    'createscreenshot',
    'geoip',
    'upordown',
    'reputationchecker',
    'getheaders',
    'linkbackup',
    'urlshortener',
    'bitcoinbalance',
    'ethereumbalance',
    'currency',
    'currencyrates',
    'randomstringpicker',
    'dictionary',
    'definepicture',
    'synonym',
    'translate',
    'randomperson',
    'youtubedetails',
    'youtubemp3',
    'weather',
    'qrgenerator',
    'textparser',
    'passwordgenerator',
    'randomnumber',
    'licensekeygenerator',
    'eitheror',
    'gif'
]
```

## Use Cases
```python
# With JSON
response = api.emailvalidator(email='example@example.com', json=True)
print(response)
```
```json
{
    "success": True, 
    "exists": False,
    "error": "E-mail doesn't exist."
}
```


```python
# Without JSON
response = api.emailvalidator(email='example@example.com', json=False)
print(response)
```
```md
Email doesn't exist
```

# Other

## To-Do
Add dynamic parser for JSON responses


## Docs

[API Overview](https://api.c99.nl/dashboard/api_overview)

## Warning

**To use the c99.nl API you need to [purchase](https://api.c99.nl/dashboard/shop) an API key**

