class Integration(object):

    def __init__(self, payload:dict):
        self._payload = payload
        self.id = int(self._payload.get("id", 0))
        self.name = self._payload.get("name")
        self.type = self._payload.get("type")
        self.enabled = self._payload.get("enabled")
        self.syncing = self._payload.get("syncing")
        self.role_id = int(self._payload.get("role_id", 0))
        self.expire_behaviour = self._payload.get("expire_behaviour")
        self.expire_grace_period = self._payload.get("expire_grace_period")
        # self.user = User(self._payload.get("user", dict()))
        self.account = self._payload.get("account")
        self.synced_at = self._payload.get("synced_at")
