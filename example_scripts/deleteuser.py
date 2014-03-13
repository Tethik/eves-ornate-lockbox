#!/usr/bin/python

import httplib
import base64
import json
import sys
import urllib

if len(sys.argv) < 2:
	print "USAGE: deleteuser.py username"
	exit(1)

addr = "127.0.0.1:5000"
endpoint = "/users?where={\"username\":\"" + sys.argv[1] + "\"}"
auth = "secret:"
use_ssl = False

headers = {"Accept": "text/plain", "Authorization": "Basic " + base64.b64encode(auth)}

h1 = httplib.HTTPConnection(addr)
if use_ssl:
	h1 = httplib.HTTPSConnection(addr)
h1.request("GET", endpoint, headers=headers)


resp = h1.getresponse().read()
#~ print resp
decoded_resp = json.loads(resp)
print decoded_resp
if len(decoded_resp["_items"]) < 1:
	print "Found no user with name", sys.argv[1]
	exit(1)

user_url = decoded_resp["_items"][0]["_links"]["self"]["href"]
headers["If-Match"] = decoded_resp["_items"][0]["_etag"]

h1.request("DELETE", user_url, headers=headers)
print h1.getresponse().read()
h1.close()

