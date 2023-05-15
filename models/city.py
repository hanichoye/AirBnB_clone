#!/usr/bin/python3
""" City class """

import uuid
from datetime import datetime
from models import storage
from models.base_model import BaseModel

class City(BaseModel):
    """Defines the blueprint of the City.

    Attributes:
        state_id: string - empty string: it will be the State.id
        name: string - empty string
    """
    state_id = ""
    name = ""
