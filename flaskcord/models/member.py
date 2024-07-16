# from ..models.base import DiscordModelsBase
# from ..models import Guild
from ..types.role import Role

class Member():
    def __init__(self, _payload:dict, guild) -> None:
        
        self.guild = guild
        self.name = _payload["user"]["global_name"]
        self.id = int(_payload.get("user").get("id"))
        self.discriminator = _payload.get("discriminator")
        self.avatar_hash = _payload["user"]["avatar"]
        self.roles = _payload.get("roles")
        self.joined_at = _payload.get("joined_at")
        self.user = _payload.get("user")
        self.deaf = _payload.get("deaf")
        self.mute = _payload.get("mute")
        self.nick = _payload.get("nick")

    def __str__(self) -> str:
        return self.name
    
    async def add_role(self, role:Role):
        return await self._bot_request(f"/guilds/{self.guild.id}/members/{self.id}/roles/{role.id}", method="PUT")

