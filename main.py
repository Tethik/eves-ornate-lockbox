from eve import Eve
from radiusauth import RadiusAuth
from dummyauth import DummyAuth
import base64 
from flask import g, abort
	
def pre_get_callback(resource, request):
	auth = request.headers['Authorization'].split(" ")[1]
	g.username = base64.standard_b64decode(auth).split(":")[0]		
	#~ session["username"] = base64.standard_b64decode(auth).split(":")[0]	
	
def before_returning_files(documents):
	documents[:] = [doc for doc in documents if ("uploaded_by" in doc.keys() and doc["uploaded_by"] == g.username) or ("accessible_by" in doc.keys() and g.username == doc["accessible_by"])]		
	
def before_insert_files(documents):
	for doc in documents:
		doc["uploaded_by"] = g.username	
	
def before_fetch_item_file(_id, document):
	if not ("accessible_by" in document.keys() and g.username == document["accessible_by"]) and not g.username == document["uploaded_by"]:
		abort(401, "You don't have access to this file.") 

#~ app = Eve(auth=RadiusAuth)
app = Eve(auth=DummyAuth)
app.on_pre_GET += pre_get_callback
app.on_pre_POST += pre_get_callback
app.on_pre_PUT += pre_get_callback
app.on_pre_DELETE += pre_get_callback
app.on_pre_PATCH += pre_get_callback

app.on_fetch_resource_files += before_returning_files
app.on_insert_files += before_insert_files
app.on_replace_files += before_insert_files
app.on_update_files += before_insert_files

app.on_fetch_item_file += before_fetch_item_file

if __name__ == '__main__':
	app.run()
