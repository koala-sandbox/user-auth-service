class Config(object):
	"""
	Configuration base, for all environments.
	"""
	ENV = "production"
	SHARED_SECRET_KEY = "1234567890"
	SERVICE_NAME = "koala"
	VERSION = "0.0.1"

class ProductionConfig(Config):
	pass

class DevConfig(Config):
	ENV = "development"

class TestingConfig(Config):
	ENV = "testing"
