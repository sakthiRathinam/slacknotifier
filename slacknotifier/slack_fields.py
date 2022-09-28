import requests
import logging
from .constants import *


class SlackError(requests.exceptions.RequestException):
    pass

class DictConvertibleObject:

    def __init__(self, *args, **kwargs):
        pass

    def to_dict(self):
        raise NotImplementedError(
            'Object "{}" does not implemented "to_dict" method'.format(
                self.__class__.__name__),
        )
        

class BaseBlock(DictConvertibleObject):
    def __init__(self,text_type,text):
        self.type = text_type
        self.text = text
    def to_dict(self):
        assert if self.type or self.text is None \
            