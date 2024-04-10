import toml
from app import app

@app.route('/')
def index():
	return "hello world!"


@app.route('/koala')
def koala():
	service_name = ""
	description = ""
	version = ""
	with open(".koala.toml", "rb") as f:
		toml_str = f.read().decode("utf-8")
		parsed_toml = toml.loads(toml_str)
		service_name = parsed_toml["Name"]
		description = parsed_toml["Description"]
	
	with open("VERSION", "rb") as f:
		version = f.readline().decode("utf-8")

	return "Hello Koala! (%s v%s) - %s" % (service_name, version, description)