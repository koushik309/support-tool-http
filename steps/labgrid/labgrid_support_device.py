
from labgrid.resource.common import Resource
from labgrid.factory import target_factory

@target_factory.reg_resource
class SupportToolRESTDevice(Resource):
    def __init__(self, name, url, auth_token=None):
        super().__init__(name)
        self.url = url
        self.auth_token = auth_token
