"""
MIT License

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


from .types import Permissions


class Role:
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
        self.mention:str = f"<@{self.id}>"
        self.position = _payload.get("position")
        self.description = _payload.get("description")
        self.permissions = self.__get_permissions(_payload.get("permissions"))
        self.mentionable = _payload.get("mentionable")
        self.accent_color = _payload.get("accent_color")
        self.integration_id = _payload.get("integration_id")
        self.permissions_new = _payload.get("permissions_new")

    def __repr__(self):
        return f"<Role id={self.id} name={self.name}>"

    @staticmethod
    def __get_permissions(permissions_value):
        if permissions_value is None:
            return
        return Permissions(int(permissions_value))
    
