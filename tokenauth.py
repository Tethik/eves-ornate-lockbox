from eve.auth import BasicAuth
from dummyauth import DummyAuth

adminsecretkey = "secret"

class TokenOverrideAuth(BasicAuth):
	normal_auth = DummyAuth()
	
	def check_auth(self, username, password, allowed_roles, resource, method):
		if username == adminsecretkey:
			return True	
		return method == "GET" and self.normal_auth.check_auth(username, password, allowed_roles, resource, method)		
		
