import requests

class SupportToolRESTDriver:
    def __init__(self, resource, url, auth_token=None):
        self.resource = resource
        self.url = url.rstrip("/")
        self.auth_token = auth_token
        self.session = requests.Session()
        if auth_token:
            self.session.headers.update({"Authorization": f"Bearer {auth_token}"})

    def on_activate(self):
        res = self.session.get(f"{self.url}/health")
        if not res.ok:
            raise RuntimeError("Support tool server unreachable")

    def on_deactivate(self):
        try:
            self.session.post(f"{self.url}/shutdown")
        except Exception:
            pass

    def upgrade(self, payload: dict):
        res = self.session.post(f"{self.url}/upgrade", json=payload)
        if not res.ok:
            raise RuntimeError(f"Upgrade failed: {res.text}")
        return res.json()

    def downgrade(self, payload: dict):
        res = self.session.post(f"{self.url}/downgrade", json=payload)
        if not res.ok:
            raise RuntimeError(f"Downgrade failed: {res.text}")
        return res.json()
