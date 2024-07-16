from .. import configs

class Emoji:
    def init(self, payload:dict):
        self.id = payload.get("id")
        self.name = payload.get("name")
        self.roles = payload.get("roles")
        self.user = payload.get("user")
        self.require_colons = payload.get("require_colons")
        self.managed = payload.get("managed")
        self.animated = payload.get("animated")
        self.available = payload.get("available")

    def __str__(self):
        return self.name
    

    def url(self):
        return f"{configs.DISCORD_EMOJI_URL}{self.id}"