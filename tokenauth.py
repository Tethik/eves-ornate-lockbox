from eve.auth import BasicAuth
from dummyauth import DummyAuth
from radiusauth import RadiusAuth

adminsecretkey = "secret"

class TokenOverrideAuth(BasicAuth):
	normal_auth = DummyAuth()
	#normal_auth = RadiusAuth()
	
	def check_auth(self, username, password, allowed_roles, resource, method):
		if username == adminsecretkey:
			return True	
		return method == "GET" and self.normal_auth.check_auth(username, password, allowed_roles, resource, method)		
		
