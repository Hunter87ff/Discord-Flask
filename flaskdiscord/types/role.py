# from ..models.base import DiscordModelsBase
# from ..models import Guild


class Role():
    ROUTE = "/guilds/{guild_id}/roles"
    def __init__(self, _payload:dict, guild) -> None:
        self.guild = guild
        self.name = _payload.get("name")
        self.id = int(_payload.get("id"))
        self.color = _payload.get("color")
        self.hoist = _payload.get("hoist")
        self.tags = _payload.get("tags")
        self.icon_hash = _payload.get("icon")
        self.members = _payload.get("members")
        self.managed = _payload.get("managed")
        self.position = _payload.get("position")
        self.description = _payload.get("description")
        self.permissions = _payload.get("permissions")
        self.mentionable = _payload.get("mentionable")
        self.accent_color = _payload.get("accent_color")
        self.integration_id = _payload.get("integration_id")
        self.permissions_new = _payload.get("permissions_new")

