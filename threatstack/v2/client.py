"""
v2 Client
"""

from threatstack.errors import ThreatStackClientError
from threatstack.base import BaseClient

from threatstack.v2 import resources

class Client(BaseClient):

    BASE_URL = "https://api.threatstack.com/v2/"

    def __init__(self, api_key=None, org_id=None, timeout=None, user_id=None):
        BaseClient.__init__(self, api_key=api_key, timeout=timeout)
        self.API_VERSION = 2
        self.org_id = org_id
        self.user_id = user_id
        self.org_id_header = "Organization-Id"
        self.agents = resources.Agents(self)
        self.alerts = resources.Alerts(self)
        self.vulnerabilities= resources.Vulnerabilities(self)
        self.rulesets = resources.Rulesets(self)
        self.servers = resources.Servers(self)

    @property
    def org_id(self):
        return self._org_id

    @org_id.setter
    def org_id(self, k):
        if not k:
            raise ThreatStackClientError("org_id is required.")
        self._org_id = k
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, k):
        if not k:
            raise ThreatStackClientError("user_id is required.")
        self._user_id = k
