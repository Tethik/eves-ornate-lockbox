from eve.auth import BasicAuth

class DummyAuth(BasicAuth):
	users = {
		"bob": "password",
		"jimmy": "password1",
		# etc..		
	}
	def check_auth(self, username, password, allowed_roles, resource, method):
		return self.users[username] == password;
