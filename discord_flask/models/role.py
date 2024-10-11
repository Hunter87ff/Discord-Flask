from .. import types



class Role():
    MANY = True
    ROUTE = "/guilds/{guild_id}/roles"
    # print(json.dumps(_payload, indent=4))
    def __init__(self, _payload, guild):
        self.id = int(_payload["id"])
        self.name = _payload["name"]
        self.permissions = self.__get_permissions(_payload.get("permissions"))
        self.mention:str = f"<@{self.id}>"
        # self.last_message_id = payload["last_message_id"]
        self.guild = guild

        
    @staticmethod
    def __get_permissions(permissions_value):
        if permissions_value is None:
            return
        return types.Permissions(int(permissions_value))