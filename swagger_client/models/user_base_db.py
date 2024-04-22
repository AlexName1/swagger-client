# coding: utf-8

"""
    Rest DB

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from swagger_client.models.stock_base import StockBase
from swagger_client.models.user_bot_base import UserBotBase
from typing import Optional, Set
from typing_extensions import Self

class UserBaseDb(BaseModel):
    """
    UserBaseDb
    """ # noqa: E501
    id: Optional[StrictInt] = None
    user_id: StrictInt
    first_name: StrictStr
    username: Optional[StrictStr] = None
    stock: Optional[StockBase] = None
    users_bots: Optional[List[UserBotBase]] = None
    __properties: ClassVar[List[str]] = ["id", "user_id", "first_name", "username", "stock", "users_bots"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of UserBaseDb from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of stock
        if self.stock:
            _dict['stock'] = self.stock.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in users_bots (list)
        _items = []
        if self.users_bots:
            for _item in self.users_bots:
                if _item:
                    _items.append(_item.to_dict())
            _dict['users_bots'] = _items
        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if username (nullable) is None
        # and model_fields_set contains the field
        if self.username is None and "username" in self.model_fields_set:
            _dict['username'] = None

        # set to None if stock (nullable) is None
        # and model_fields_set contains the field
        if self.stock is None and "stock" in self.model_fields_set:
            _dict['stock'] = None

        # set to None if users_bots (nullable) is None
        # and model_fields_set contains the field
        if self.users_bots is None and "users_bots" in self.model_fields_set:
            _dict['users_bots'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UserBaseDb from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "user_id": obj.get("user_id"),
            "first_name": obj.get("first_name"),
            "username": obj.get("username"),
            "stock": StockBase.from_dict(obj["stock"]) if obj.get("stock") is not None else None,
            "users_bots": [UserBotBase.from_dict(_item) for _item in obj["users_bots"]] if obj.get("users_bots") is not None else None
        })
        return _obj


