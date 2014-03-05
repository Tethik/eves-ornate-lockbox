from eve.auth import TokenAuth

adminsecretkey = "secret"

class UserTokenAuth(TokenAuth):
    def check_auth(self, token, allowed_roles, resource, method): 
		if method == "GET":
			return True		
		return token == adminsecretkey
