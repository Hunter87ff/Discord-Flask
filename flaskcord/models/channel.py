from flask import current_app
# from .guild import Guild
from .base import DiscordModelsBase
from .. import types


class Channel(DiscordModelsBase):
    MANY = True
    ROUTE = "/channels/{channel_id}"

    def __init__(self, payload, guild):
        super().__init__(payload)
        self._payload:dict = payload
        self.id:int = int(self._payload["id"])
        self.name:str = self._payload["name"]
        self.permissions = self.__get_permissions(self._payload.get("permissions"))
        self.mention:str = f"<#{self.id}>"
        # self.last_message_id = self._payload["last_message_id"]
        self._guild = guild

    @property
    def guild(self):
       return self._guild

    @staticmethod
    def __get_permissions(permissions_value) -> types.Permissions:
        if permissions_value is None:return
        return types.Permissions(int(permissions_value))
    
    async def send(self, content:str, embed:types.Embed = None):
        """Send a message to the channel.

        Parameters
        ----------
        content : str
            Content of the message.
        embed : discord.Embed, optional
            Embed to be sent with the message.

        Returns
        -------
        discord.Message
            Message object of the sent message.
        """
        return await current_app.http.send_message(self.id, content, embed)
    

