# Mock Resource class
class Resource:
    def __init__(self, name):
        self.name = name

# Mock decorator
def target_factory_decorator(cls):
    return cls

target_factory = type('factory', (), {'reg_resource': target_factory_decorator})

@target_factory.reg_resource
class SupportToolRESTDevice(Resource):
    def __init__(self, name, url, auth_token=None):
        super().__init__(name)
        self.url = url
        self.auth_token = auth_token
