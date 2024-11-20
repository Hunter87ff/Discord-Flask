"""
MIT License

Copyright (c) 2019 thecosmos
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

from .base import DiscordModelsBase
from flask import current_app
from .channel import Channel
from ..role import Role
from .member import Member
from ..emoji import Emoji
from .. import types
from .. import configs
import json
from typing import (
    Any,
    List,
    Dict,
    Sequence
)

class Guild(DiscordModelsBase):
    MANY = True
    ROUTE = "/guilds/{guild_id}"

    def __init__(self, payload:dict):
        super().__init__(payload)
        self.id:int = int(self._payload["id"])
        self.name:str = self._payload["name"]
        self.icon_hash:str = self._payload.get("icon")
        self.is_owner = self._payload.get("owner")
        self.permissions = self.__get_permissions(self._payload.get("permissions"))
        self._roles:dict= self._add_roles()
        self._members:dict = {}
        self._channels:dict = self._add_channels()
        self._owner_id:int = int(self._payload.get("owner_id"))

    def _add_channels(self):
        fetched_channels = self._bot_request(f"/guilds/{self.id}/channels")
        return {channel['id']:Channel(channel, self) for channel in fetched_channels}
    
    def _add_members(self):
        fetched_members = self._bot_request(f"/guilds/{self.id}/members?limit=1000")
        self._members = {member["user"]["id"]: Member(member, self) for member in fetched_members}

    def _add_roles(self):
        fetched_roles = self._payload.get("roles")
        return {role["id"] : Role(role, self) for role in fetched_roles}

    @staticmethod
    def __get_permissions(permissions_value):
        if permissions_value is None:return
        return types.Permissions(int(permissions_value))

    def __str__(self):
        return self.name

    def __eq__(self, guild):
        return isinstance(guild, Guild) and guild.id == self.id

    def __ne__(self, guild):
        return not self.__eq__(guild)

    @property
    def icon_url(self)->str:
        if not self.icon_hash:return
        return configs.DISCORD_GUILD_ICON_BASE_URL.format(guild_id=self.id, icon_hash=self.icon_hash)
    
    def get_channel(self, channel_id:int)->Channel:
        return self._channels.get(channel_id)
    
    def get_member(self, user_id:int)->Member:
        if self._members and user_id in self._members:return self._members[user_id]
        fetched_member = self._bot_request(f"/guilds/{self.id}/members/{user_id}")
        member_obj = Member(fetched_member, self)
        if not self._members: self._members[member_obj.id] = member_obj
        return member_obj
    
    def get_role(self, role_id:int)->Role:
        return self._roles.get(role_id)    
    
    @property
    def channels(self) -> List[Channel]:
        return self._channels.values()
    
    @property
    def emojies(self)->List[str]:
        return [Emoji(emoji) for emoji in self._payload.get("emojis", [])]
    
    @property
    def features(self)->List[str]:
        return self._payload.get("features", [])
    
    @property
    def members(self)->List[Member]:
        return self._members.values()
    
    @property
    def roles(self)->List[Role]:
        return self._roles.values() 

    @property
    def owner_id(self)->int:
        return self._owner_id

    

class CGuild(DiscordModelsBase):
    """CGuild Class representing discord Guild the user is part of.

    Operations
    ----------
    x == y
        Checks if two guild's are the same.
    x != y
        Checks if two guild's are not the same.
    str(x)
        Returns the guild's name.

    Attributes
    ----------
    id : int
        Discord ID of the guild.
    name : str
        Name of the guild.
    icon_hash : str
        Hash of guild's icon.
    is_owner : bool
        Boolean determining if current user is owner of the guild or not.
    permissions : discord.Permissions
        An instance of discord.Permissions representing permissions of current user in the guild.

    """

    MANY = True
    ROUTE = "/users/@me/guilds"

    def __init__(self, payload):
        super().__init__(payload)
        self.id = int(self._payload["id"])
        self.name = self._payload["name"]
        self.icon_hash = self._payload.get("icon")
        self.is_owner = self._payload.get("owner")
        self.permissions = self.__get_permissions(self._payload.get("permissions"))

    @staticmethod
    def __get_permissions(permissions_value):
        if permissions_value is None:
            return
        return types.Permissions(int(permissions_value))

    def __str__(self):
        return self.name

    def __eq__(self, guild):
        return isinstance(guild, Guild) and guild.id == self.id

    def __ne__(self, guild):
        return not self.__eq__(guild)

    @property
    def icon_url(self):
        """A property returning direct URL to the guild's icon. Returns None if guild has no icon set."""
        if not self.icon_hash:
            return
        return configs.DISCORD_GUILD_ICON_BASE_URL.format(guild_id=self.id, icon_hash=self.icon_hash)

    @classmethod
    def fetch_from_api(cls, cache=True):
        """A class method which returns an instance or list of instances of this model by implicitly making an
        API call to Discord. If an instance of :py:class:`discord_flask.User` exists in the users internal cache
        who belongs to these guilds then, the cached property :py:attr:`discord_flask.User.guilds` is updated.

        Parameters
        ----------
        cache : bool
            Determines if the :py:attr:`discord_flask.User.guilds` cache should be updated with the new guilds.

        Returns
        -------
        list[discord_flask.Guild, ...]
            List of instances of :py:class:`discord_flask.Guild` to which this user belongs.

        """
        guilds = super().fetch_from_api()

        if cache:
            user = current_app.discord.users_cache.get(current_app.discord.user_id)
            try:
                user.guilds = {guild.id: guild for guild in guilds}
            except AttributeError:
                pass

        return guilds
    
    def get_member(self, user_id:int)->Member:
        try:
            fetched_member = self._bot_request(f"/guilds/{self.id}/members/{user_id}")
            print(fetched_member)
            return Member(fetched_member, self)
        except:
            return None