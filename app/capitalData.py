
import json
import urllib2
import urllib
import argparse
import sys


testkey = "779198b647652d0c1ff6836c713703ff"
url = "http://api.reimaginebanking.com/customers/55e94a6af8d8770528e60de3/accounts?key="+ testkey

response = urllib.urlopen(url)
data = json.loads(response.read())

def get_Balance():	
  return data[0]["balance"]

def get_Name():
  return data[0]["nickname"]

def get_account_type():
  return data[0][""]

