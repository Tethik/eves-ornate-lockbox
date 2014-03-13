#!/usr/bin/python

import httplib
import base64
import json

addr = "127.0.0.1:5000"
endpoint = "/users"
auth = "secret:"
use_ssl = False

headers = {"Content-type": "application/json", "Accept": "text/plain", "Authorization": "Basic " + base64.b64encode(auth)}

h1 = httplib.HTTPConnection(addr)
if use_ssl:
	h1 = httplib.HTTPSConnection(addr)
h1.request("GET", endpoint, headers=headers)


resp = h1.getresponse().read()
decoded_resp = json.loads(resp)
print decoded_resp
h1.close()

