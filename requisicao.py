import requests

user = "admin"
password = "996057295"
r = requests.get("http://%s:%s@127.0.0.1:5984/myemails/_design/view2/_view/getName?include_docs=true" % (user, password))
print(r.json())