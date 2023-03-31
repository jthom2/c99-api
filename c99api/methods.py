# methods.py

def register_methods(cls):
    method_names = [func.__name__ for func in globals().values() if callable(func) and func.__name__ != 'register_methods']
    for method_name in method_names:
        method_func = globals()[method_name]
        setattr(cls, method_name, classmethod(method_func))
    return cls

"""
Communication Tools
"""
def phonelookup(cls, number, json=True):
    return cls.perform_request(endpoint_name='phonelookup', number=number, json=json)

def emailvalidator(cls, email, json=True):
    return cls.perform_request(endpoint_name='emailvalidator', email=email, json=json)

def disposablemailchecker(cls, email, json=True):
    return cls.perform_request(endpoint_name='disposablemailchecker', email=email, json=json)


"""
Network Tools
"""
def portscanner(cls, host, json=True):
    return cls.perform_request(endpoint_name='portscanner', host=host, json=json)

def portscanner_port(cls, host, port, json=True):
    return cls.perform_request(endpoint_name='portscanner_port', host=host, port=port, json=json)

def ping(cls, host, json=True):
    return cls.perform_request(endpoint_name='ping', host=host, json=json)

def gethostname(cls, host, json=True):
    return cls.perform_request(endpoint_name='gethostname', host=host, json=json)

def dnschecker(cls, url, type, json=True):
    return cls.perform_request(endpoint_name='dnschecker', url=url, type=type, json=json)

def dnsresolver(cls, host, server, json=True):
    return cls.perform_request(endpoint_name='dnsresolver', host=host, server=server, json=json)

def ipvalidator(cls, ip, json=True):
    return cls.perform_request(endpoint_name='ipvalidator', ip=ip, json=json)

def torchecker(cls, ip, json=True):
    return cls.perform_request(endpoint_name='torchecker', ip=ip, json=json)

def iplogger(cls, action, json=True):
    return cls.perform_request(endpoint_name='iplogger', action=action, json=json)

def proxydetector(cls, ip, json=True):
    return cls.perform_request(endpoint_name='proxydetector', ip=ip, json=json)


"""
Web Tools
"""
def subdomainfinder(cls, domain, json=True):
    return cls.perform_request(endpoint_name='subdomainfinder', domain=domain, json=json)

def firewalldetector(cls, url, json=True):
    return cls.perform_request(endpoint_name='firewalldetector', url=url, json=json)

def ip2domains(cls, ip, json=True):
    return cls.perform_request(endpoint_name='ip2domains', ip=ip, json=json)

def alexarank(cls, url, json=True):
    return cls.perform_request(endpoint_name='alexarank', url=url, json=json)

def whois(cls, domain, json=True):
    return cls.perform_request(endpoint_name='whois', domain=domain, json=json)

def createscreenshot(cls, url, json=True):
    return cls.perform_request(endpoint_name='createscreenshot', url=url, json=json)

def geoip(cls, host, json=True):
    return cls.perform_request(endpoint_name='geoip', host=host, json=json)

def upordown(cls, host, json=True):
    return cls.perform_request(endpoint_name='upordown', host=host, json=json)

def reputationchecker(cls, url, json=True):
    return cls.perform_request(endpoint_name='reputationchecker', url=url, json=json)

def getheaders(cls, host, json=True):
    return cls.perform_request(endpoint_name='getheaders', host=host, json=json)

def linkbackup(cls, url, json=True):
    return cls.perform_request(endpoint_name='linkbackup', url=url, json=json)

def urlshortener(cls, url, json=True):
    return cls.perform_request(endpoint_name='urlshortener', url=url, json=json)


"""
Finance Tools
"""
def bitcoinbalance(cls, address, json=True):
    return cls.perform_request(endpoint_name='bitcoinbalance', address=address, json=json)

def ethereumbalance(cls, address, json=True):
    return cls.perform_request(endpoint_name='ethereumbalance', address=address, json=json)

def currency(cls, amount, from_currency, to_currency, json=True):
    return cls.perform_request(endpoint_name='currency', amount=amount, from_currency=from_currency, to_currency=to_currency, json=json)

def currencyrates(cls, source, json=True):
    return cls.perform_request(endpoint_name='currencyrates', source=source, json=json)


"""
Miscellaneous 
"""
def randomstringpicker(cls, textfile, json=True):
    return cls.perform_request(endpoint_name='randomstringpicker', textfile=textfile, json=json)

def dictionary(cls, word, json=True):
    return cls.perform_request(endpoint_name='dictionary', word=word, json=json)

def definepicture(cls, url, json=True):
    return cls.perform_request(endpoint_name='definepicture', url=url, json=json)

def synonym(cls, word, json=True):
    return cls.perform_request(endpoint_name='synonym', word=word, json=json)

def translate(cls, text, tolanguage, json=True):
    return cls.perform_request(endpoint_name='translate', text=text, tolanguage=tolanguage, json=json)

def randomperson(cls, gender, json=True):
    return cls.perform_request(endpoint_name='randomperson', gender=gender, json=json)

def youtubedetails(cls, videoid, json=True):
    return cls.perform_request(endpoint_name='youtubedetails', videoid=videoid, json=json)

def youtubemp3(cls, videoid, json=True):
    return cls.perform_request(endpoint_name='youtubemp3', videoid=videoid, json=json)

def weather(cls, location, json=True):
    return cls.perform_request(endpoint_name='weather', location=location, json=json)

def qrgenerator(cls, string, size, json=True):
    return cls.perform_request(endpoint_name='qrgenerator', string=string, size=size, json=json)

def textparser(cls, url, json=True):
    return cls.perform_request(endpoint_name='textparser', url=url, json=json)

def passwordgenerator(cls, length, include, customlist, json=True):
    return cls.perform_request(endpoint_name='passwordgenerator', length=length, include=include, customlist=customlist, json=json)

def randomnumber(cls, length, between, json=True):
    return cls.perform_request(endpoint_name='randomnumber', length=length, between=between, json=json)

def licensekeygenerator(cls, template, amount, json=True):
    return cls.perform_request(endpoint_name='licensekeygenerator', template=template, amount=amount, json=json)


"""
Fun and Games
"""
def eitheror(cls, json=True):
    return cls.perform_request(endpoint_name='eitheror', json=json)

def gif(cls, keyword, json=True):
    return cls.perform_request(endpoint_name='gif', keyword=keyword, json=json)

