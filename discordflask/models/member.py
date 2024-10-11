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
from ..role import Role

class Member:
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
    
    
    def add_role(self, role:Role):
        return current_app.discord.bot_request(f"/guilds/{self.guild.id}/members/{self.id}/roles/{role.id}", method="PUT")

