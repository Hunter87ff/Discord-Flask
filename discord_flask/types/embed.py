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

from typing import List, Tuple

class Embed:
    """Class representing an embed object."""
    def __init__(self, title:str=None, description:str=None, color:int=None, fields:List[Tuple[str, str]]=None, footer:Tuple[str, str]=None):
        self.title:str = title
        self.description:str = description
        self.color:int = color
        self.fields:List = fields
        self.footer:Tuple[str, str] = footer
        self.image:str = None
        self.thumbnail:str = None

    def __repr__(self):
        return f"<Embed title={self.title} description={self.description} color={self.color} fields={self.fields}>"
    
    def __str__(self):
        return self.title
    
    def __eq__(self, other):
        return self.title == other.title
    
    def __ne__(self, other):
        return not self.__eq__(other)
    
    def add_field(self, name:str, value:str):
        self.fields.append((name, value))


    def set_footer(self, text:str, icon:str):
        self.footer = (text, icon)


    def set_image(self, url:str):
        self.image = url

    def to_dict(self):
        return {
            "title":self.title,
            "description":self.description,
            "color":self.color,
            "fields":self.fields,
            "footer":self.footer,
            "image":self.image,
            "thumbnail":self.thumbnail
        }
    

