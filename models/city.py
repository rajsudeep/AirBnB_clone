#!/usr/bin/python3
"""City Module for AirbnB clone"""


from models.base_model import BaseModel


class City(BaseModel):
    """User inherits from BaseModel"""

    state_id = ""
    name = ""
