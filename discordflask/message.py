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
SOFTWARE.
"""

class Message:
    def __init__(self, payload:dict) -> None:
        self.channel_id = payload.get("channel_id")
        self.author = payload.get("author")
        self.content = payload.get("content")
        self.id = payload.get("id")
        self.mentions = payload.get("mentions")
        self.embeds = payload.get("embeds")
        self.attachments = payload.get("attachments")
        self.webhook_id = payload.get("webhook_id")
        self.pinned = payload.get("pinned")
        self.mention_roles = payload.get("mention_roles")
        self.mention_everyone = payload.get("mention_everyone")
        self.reactios = payload.get("reactios")
        self.payload:dict = payload

    def __str__(self) -> str:
        return self.content
    
    def reply(self, *args) -> None:
        pass

    def delete(self) -> None:
        pass

    def edit(self, *args) -> None:
        pass
