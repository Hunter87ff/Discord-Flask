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
    

