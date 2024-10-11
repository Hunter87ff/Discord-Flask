"""MIT License

Copyright (c) 2024 hunter87ff

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE."""



from flask import current_app
from .. import types
from ..embed import Embed
from ..message import Message

class Channel():
    MANY = True
    ROUTE = "/channels/{channel_id}"

    def __init__(self, payload, guild):
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
    
    def send(self, content:str=None, embed:Embed = None) -> Message:
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
        return current_app.discord.send_message(channel_id=self.id, content=content, embeds=[embed])  
    

