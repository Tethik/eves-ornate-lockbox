from eve.auth import BasicAuth

class DummyAuth(BasicAuth):
	users = {
		"bob": "password",
		"jimmy": "password1",
		"testing": "password",
		# etc..		
	}
	def check_auth(self, username, password, allowed_roles, resource, method):
		return username in self.users.keys() and self.users[username] == password;
