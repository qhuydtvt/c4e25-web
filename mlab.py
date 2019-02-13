import mongoengine

# mongodb://<dbuser>:<dbpassword>@ds213665.mlab.com:13665/c4e25-web

host = "ds213665.mlab.com"
port = 13665
db_name = "c4e25-web"
user_name = "admin"
password = "admin1"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())