"""MIT License

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





from flask import current_app
from abc import ABCMeta, abstractmethod
import typing

class DiscordModelsMeta(ABCMeta):

    ROUTE = str()

    def __init__(cls, name, *args, **kwargs):
        if not cls.ROUTE and name != "DiscordModelsBase":
            raise NotImplementedError(f"ROUTE must be specified in a Discord model: {name}.")
        super().__init__(name, *args, **kwargs)


class DiscordModelsBase(metaclass=DiscordModelsMeta):

    BOT = False
    MANY = False

    @abstractmethod
    def __init__(self, payload):
        self._payload:dict = payload

    @staticmethod
    def _request(*args, **kwargs):
        """A shorthand to :py:func:discord_flask.request`. It uses Flask current_app local proxy to get the
        discord_flask client.

        """
        return current_app.discord.request(*args, **kwargs)

    @staticmethod
    def _bot_request(route: str, method="GET", **kwargs) -> typing.Union[dict, str]:
        """A shorthand to :py:func:discord_flask.bot_request`."""
        return current_app.discord.bot_request(route, method, **kwargs)

    @classmethod
    def fetch_from_api(cls):
        """A class method which returns an instance or list of instances of this model by implicitly making an
        API call to Discord.

        Returns
        -------
        cls
            An instance of this model itself.
        [cls, ...]
            List of instances of this model when many of these models exist.

        """
        request_method = cls._bot_request if cls.BOT else cls._request
        payload = request_method(cls.ROUTE)
        if cls.MANY:
            return [cls(_) for _ in payload]
        return cls(payload)

    def to_json(self):
        """A utility method which returns raw payload object as it was received from discord.

        Returns
        -------
        dict
            A dict representing raw payload object received from discord.

        """
        return self._payload
