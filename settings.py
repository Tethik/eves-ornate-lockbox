from tokenauth import TokenOverrideAuth
	

#SERVER_NAME = '127.0.0.1:5000'
DEBUG = True

# Use these to connect to a specific mongo instance.
# Otherwise default localhost will be used.
#~ MONGO_HOST = 'localhost'
#~ MONGO_PORT = 27017
#~ MONGO_USERNAME = 'user'
#~ MONGO_PASSWORD = 'user'
#~ MONGO_DBNAME = 'apitest'

# Enable reads (GET), inserts (POST) and DELETE for resources/collections
# (if you omit this line, the API will default to ['GET'] and provide
# read-only access to the endpoint).
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']

# Enable reads (GET), edits (PATCH), replacements (PUT) and deletes of
# individual items  (defaults to read-only item access).
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']


user_schema = {
	'username': {
		'type': 'string',
		'required': True,
		'unique': True
	},
	'public_key': {
		'type': 'media'		
	}
}

users = {
	'schema': user_schema,
	'authentication': TokenOverrideAuth(),
	'query_objectid_as_string': True
}


files_schema = {
    # Schema definition, based on Cerberus grammar. Check the Cerberus project
    # (https://github.com/nicolaiarocci/cerberus) for details.   
	'name': {
		'type': 'string',
		'required': True,
	},
	'content': {
		'type': 'media'
	},		
	
	# username basis
	'uploaded_by': {
		'type': 'string',		
	},	
	'accessible_by': {
		'type': 'string',
		'required': True
		#~ 'type': 'list', 
		#~ 'items': [{'type': 'string'}]
	},
	'signature': {
		'type': 'string'
	},
	'session_key': {
		'type': 'string'
	}
}

files = {
	'schema': files_schema,
}

DOMAIN = {
    'users': users,
    'files': files,
}
