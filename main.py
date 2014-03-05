from eve import Eve
from radiusauth import RadiusAuth

app = Eve(auth=RadiusAuth)
app.run()
