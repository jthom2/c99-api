# handler.py

import requests
from methods import register_methods

@register_methods

class c99_api:
    key = None
    base_url = 'https://api.c99.nl'

    @classmethod
    def fetch_endpoint(cls, endpoint_name, json=True, **kwargs):
        if not cls.key:
            raise ValueError("API key not set. Use c99_api.key = 'your_api_key'")
        
        # Add &json to the URLs only if json parameter is set to True
        json_query = '&json' if json else ''
        
        endpoint_list = {
        'phonelookup': cls.base_url + f'/phonelookup?key={cls.key}&number={kwargs.get("number")}{json_query}',
        'emailvalidator': cls.base_url + f'/emailvalidator?key={cls.key}&email={kwargs.get("email")}{json_query}',
        'disposablemailchecker': cls.base_url + f'/disposablemailchecker?key={cls.key}&email={kwargs.get("email")}{json_query}',
        'portscanner': cls.base_url + f'/portscanner?key={cls.key}&host={kwargs.get("host")}{json_query}',
        'portscanner_port': cls.base_url + f'/portscanner?key={cls.key}&host={kwargs.get("host")}&port={kwargs.get("port")}{json_query}',
        'ping': cls.base_url + f'/ping?key={cls.key}&host={kwargs.get("host")}{json_query}',
        'gethostname': cls.base_url + f'/gethostname?key={cls.key}&host={kwargs.get("host")}{json_query}',
        'dnschecker': cls.base_url + f'/dnschecker?key={cls.key}&url={kwargs.get("url")}&type={kwargs.get("type")}{json_query}',
        'dnsresolver': cls.base_url + f'/dnsresolver?key={cls.key}&host={kwargs.get("host")}&server={kwargs.get("server")}{json_query}',
        'ipvalidator': cls.base_url + f'/ipvalidator?key={cls.key}&ip={kwargs.get("ip")}{json_query}',
        'torchecker': cls.base_url + f'/torchecker?key={cls.key}&ip={kwargs.get("ip")}{json_query}',
        'iplogger': cls.base_url + f'/iplogger?key={cls.key}&action={kwargs.get("action")}{json_query}',
        'proxydetector': cls.base_url + f'/proxydetector?key={cls.key}&ip={kwargs.get("ip")}{json_query}',
        'subdomainfinder': cls.base_url + f'/subdomainfinder?key={cls.key}&domain={kwargs.get("domain")}{json_query}',
        'firewalldetector': cls.base_url + f'/firewalldetector?key={cls.key}&url={kwargs.get("url")}{json_query}',
        'ip2domains': cls.base_url + f'/ip2domains?key={cls.key}&ip={kwargs.get("ip")}{json_query}',
        'alexarank': cls.base_url + f'/alexarank?key={cls.key}&url={kwargs.get("url")}{json_query}',
        'whois': cls.base_url + f'/whois?key={cls.key}&domain={kwargs.get("domain")}{json_query}',
        'createscreenshot': cls.base_url + f'/createscreenshot?key={cls.key}&url={kwargs.get("url")}{json_query}',
        'geoip': cls.base_url + f'/geoip?key={cls.key}&host={kwargs.get("host")}{json_query}',
        'upordown': cls.base_url + f'/upordown?key={cls.key}&host={kwargs.get("host")}{json_query}',
        'reputationchecker': cls.base_url + f'/reputationchecker?key={cls.key}&url={kwargs.get("url")}{json_query}',
        'getheaders': cls.base_url + f'/getheaders?key={cls.key}&host={kwargs.get("host")}{json_query}',
        'linkbackup': cls.base_url + f'/linkbackup?key={cls.key}&url={kwargs.get("url")}{json_query}',
        'urlshortener': cls.base_url + f'/urlshortener?key={cls.key}&url={kwargs.get("url")}{json_query}',
        'bitcoinbalance': cls.base_url + f'/bitcoinbalance?key={cls.key}&address={kwargs.get("address")}{json_query}',
        'ethereumbalance': cls.base_url + f'/ethereumbalance?key={cls.key}&address={kwargs.get("address")}{json_query}',
        'currency': cls.base_url + f'/currency?key={cls.key}&amount={kwargs.get("amount")}&from={kwargs.get("from")}&to={kwargs.get("to")}{json_query}',
        'currencyrates': cls.base_url + f'/currencyrates?key={cls.key}&source={kwargs.get("source")}{json_query}',
        'randomstringpicker': cls.base_url + f'/randomstringpicker?key={cls.key}&textfile={kwargs.get("textfile")}{json_query}',
        'dictionary': cls.base_url + f'/dictionary?key={cls.key}&word={kwargs.get("word")}{json_query}',
        'definepicture': cls.base_url + f'/definepicture?key={cls.key}&url={kwargs.get("url")}{json_query}',
        'synonym': cls.base_url + f'/synonym?key={cls.key}&word={kwargs.get("word")}{json_query}',
        'translate': cls.base_url + f'/translate?key={cls.key}&text={kwargs.get("text")}&tolanguage={kwargs.get("tolanguage")}{json_query}',
        'randomperson': cls.base_url + f'/randomperson?key={cls.key}&gender={kwargs.get("gender")}{json_query}',
        'youtubedetails': cls.base_url + f'/youtubedetails?key={cls.key}&videoid={kwargs.get("videoid")}{json_query}',
        'youtubemp3': cls.base_url + f'/youtubemp3?key={cls.key}&videoid={kwargs.get("videoid")}{json_query}',
        'weather': cls.base_url + f'/weather?key={cls.key}&location={kwargs.get("location")}{json_query}',
        'qrgenerator': cls.base_url + f'/qrgenerator?key={cls.key}&string={kwargs.get("string")}&size={kwargs.get("size")}{json_query}',
        'textparser': cls.base_url + f'/textparser?key={cls.key}&url={kwargs.get("url")}{json_query}',
        'passwordgenerator': cls.base_url + f'/passwordgenerator?key={cls.key}&length={kwargs.get("length")}&include={kwargs.get("include")}&customlist={kwargs.get("customlist")}{json_query}',
        'randomnumber': cls.base_url + f'/randomnumber?key={cls.key}&length={kwargs.get("length")}&between={kwargs.get("between")}{json_query}',
        'licensekeygenerator': cls.base_url + f'/licensekeygenerator?key={cls.key}&template={kwargs.get("template")}&amount={kwargs.get("amount")}{json_query}',
        'eitheror': cls.base_url + f'/eitheror?key={cls.key}{json_query}',
        'gif': cls.base_url + f'/gif?key={cls.key}&keyword={kwargs.get("keyword")}{json_query}'
        }

        url_template = endpoint_list[endpoint_name]
        result_endpoint = url_template.format(**kwargs)
        return result_endpoint

    @classmethod
    def perform_request(cls, endpoint_name, json=True, **kwargs):
        url = cls.fetch_endpoint(endpoint_name=endpoint_name, json=json, **kwargs)
        response = requests.get(url)
        return response.json() if json else response.text
    
    @classmethod
    def list_methods(cls):

        methods_list = [
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

        return methods_list