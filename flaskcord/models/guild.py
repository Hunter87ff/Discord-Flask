from .base import DiscordModelsBase
from flask import current_app
from .channel import Channel
from .role import Role
from .member import Member
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
    ROUTE = "/users/@me/guilds"

    def __init__(self, payload:dict):
        super().__init__(payload)
        self.id:int = int(self._payload["id"])
        self.name:str = self._payload["name"]
        self.icon_hash:str = self._payload.get("icon")
        self.is_owner = self._payload.get("owner")
        self.permissions = self.__get_permissions(self._payload.get("permissions"))
        self._roles:dict= self._add_roles()
        self._members:dict = self._add_members()
        self._channels:dict = self._add_channels()
        self._owner_id:int = int(self._payload.get("owner_id"))
        # print(json.dumps(self._members.values()[0], indent=4))

    def _add_channels(self):
        # if self._channels:return self._channels
        fetched_channels = self._bot_request(f"/guilds/{self.id}/channels")
        # print("Channel:",json.dumps(list(fetched_channels)[0], indent=4))
        return {channel['id']:Channel(channel, self) for channel in fetched_channels}
    
    def _add_members(self):
        # if self._members:return self._members
        fetched_members = self._bot_request(f"/guilds/{self.id}/members?limit=1000")
        # print("Member:", json.dumps(list(fetched_members)[0], indent=4))
        return {member["user"]["id"]: Member(member, self) for member in fetched_members}

    def _add_roles(self):
        # if self._roles:return self._roles
        # fetched_roles:dict = self._bot_request(f"/guilds/{self.id}/roles")
        fetched_roles = self._payload.get("roles")
        # print("Role:",json.dumps(list(fetched_roles)[0], indent=4))
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
    
    def get_member(self, user_id:int)->types.Member:
        return self._members.get(user_id)
    
    def get_role(self, role_id:int)->Role:
        return self._roles.get(role_id)    
    
    @property
    def channels(self) -> List[Channel]:
        return self._channels.values()
    
    @property
    def emojies(self)->List[str]:
        return [types.Emoji(emoji) for emoji in self._payload.get("emojis", [])]
    
    @property
    def features(self)->List[str]:
        return self._payload.get("features", [])
    
    @property
    def members(self)->List[types.Member]:
        return self._members.values()
    
    @property
    def roles(self)->List[Role]:
        return self._roles.values() 

    @property
    def owner_id(self)->int:
        return self._owner_id

    

class CGuild(DiscordModelsBase):
    """Class representing discord Guild the user is part of.

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
        API call to Discord. If an instance of :py:class:`flaskcord.User` exists in the users internal cache
        who belongs to these guilds then, the cached property :py:attr:`flaskcord.User.guilds` is updated.

        Parameters
        ----------
        cache : bool
            Determines if the :py:attr:`flaskcord.User.guilds` cache should be updated with the new guilds.

        Returns
        -------
        list[flaskcord.Guild, ...]
            List of instances of :py:class:`flaskcord.Guild` to which this user belongs.

        """
        guilds = super().fetch_from_api()

        if cache:
            user = current_app.discord.users_cache.get(current_app.discord.user_id)
            try:
                user.guilds = {guild.id: guild for guild in guilds}
            except AttributeError:
                pass

        return guilds
