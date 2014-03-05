from eve.auth import BasicAuth
import pyrad.packet

from pyrad.client import Client
from pyrad.dictionary import Dictionary

class RadiusAuth(BasicAuth):
	def check_auth(self, username, password, allowed_roles, resource, method):
		srv=Client(server="192.168.137.200", secret="wowsuchsecret",
			  dict=Dictionary("/usr/share/freeradius/dictionary"))

		req=srv.CreateAuthPacket(code=pyrad.packet.AccessRequest,
					  User_Name=username, NAS_Identifier="")
		#~ req["Username"]="testing"
		req["Password"]=req.PwCrypt(password)

		reply=srv.SendPacket(req)
		if reply.code==pyrad.packet.AccessAccept:
			return True
		else:
			return False
