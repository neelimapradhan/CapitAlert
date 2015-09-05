import requests
import json
import urllib2
import urllib
import argparse
import sys
#import oauth2

url = "http://api.reimaginebanking.com/customers/55e94a6af8d8770528e60de3/accounts?key=779198b647652d0c1ff6836c713703ff"

response = urllib.urlopen(url)
data = json.loads(response.read())

print data
print data[0]["balance"]
