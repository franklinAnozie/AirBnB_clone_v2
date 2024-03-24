#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy import Column, DATETIME, String
from sqlalchemy.ext.declarative import declarative_base
import models
from os import getenv

if getenv("HBNB_TYPE_STORAGE") == 'db':
    Base = declarative_base()
else:
    Base = object


class BaseModel:
    """A base class for all hbnb models"""

    if getenv("HBNB_TYPE_STORAGE") == 'db':
        __table_args__ = {'mysql_engine': 'InnoDB', 'mysql_charset': 'latin1'}
        id = Column(String(60), primary_key=True)
        created_at = Column(DATETIME, default=datetime.utcnow, nullable=False)
        updated_at = Column(DATETIME, default=datetime.utcnow, nullable=False)

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            tf = "%Y-%m-%dT%H:%M:%S.%f"
            if "updated_at" in kwargs:
                kwargs["updated_at"] = datetime.strptime(kwargs["updated_at"],
                                                         tf)
            else:
                self.updated_at = datetime.now()
            if "created_at" in kwargs:
                kwargs["created_at"] = datetime.strptime(kwargs["created_at"],
                                                         tf)
            else:
                self.created_at = datetime.now()
            if "id" not in kwargs:
                self.id = str(uuid.uuid4())
            for key in kwargs:
                if key != "__class__":
                    setattr(self, key, kwargs[key])

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        dic = self.__dict__.copy()
        if "_sa_instance_state" in dic:
            del dic["_sa_instance_state"]
        return '[{}] ({}) {}'.format(cls, self.id, dic)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        if "_sa_instance_state" in dictionary:
            del dictionary["_sa_instance_state"]
        return dictionary

    def delete(self):
        """ deletes the instance"""
        models.storage.delete(self)
