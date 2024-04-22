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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from swagger_client.models.item_base import ItemBase
from swagger_client.models.size_base import SizeBase
from swagger_client.models.user_bot_base import UserBotBase
from typing import Optional, Set
from typing_extensions import Self

class BasketBaseDb(BaseModel):
    """
    BasketBaseDb
    """ # noqa: E501
    id: Optional[StrictInt] = None
    created: datetime
    item_code: StrictStr
    price: StrictInt
    user_bot_id: StrictInt
    size_id: StrictInt
    user_bot: Optional[UserBotBase] = None
    size: Optional[SizeBase] = None
    item: Optional[ItemBase] = None
    __properties: ClassVar[List[str]] = ["id", "created", "item_code", "price", "user_bot_id", "size_id", "user_bot", "size", "item"]

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
        """Create an instance of BasketBaseDb from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of user_bot
        if self.user_bot:
            _dict['user_bot'] = self.user_bot.to_dict()
        # override the default output from pydantic by calling `to_dict()` of size
        if self.size:
            _dict['size'] = self.size.to_dict()
        # override the default output from pydantic by calling `to_dict()` of item
        if self.item:
            _dict['item'] = self.item.to_dict()
        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if user_bot (nullable) is None
        # and model_fields_set contains the field
        if self.user_bot is None and "user_bot" in self.model_fields_set:
            _dict['user_bot'] = None

        # set to None if size (nullable) is None
        # and model_fields_set contains the field
        if self.size is None and "size" in self.model_fields_set:
            _dict['size'] = None

        # set to None if item (nullable) is None
        # and model_fields_set contains the field
        if self.item is None and "item" in self.model_fields_set:
            _dict['item'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of BasketBaseDb from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "created": obj.get("created"),
            "item_code": obj.get("item_code"),
            "price": obj.get("price"),
            "user_bot_id": obj.get("user_bot_id"),
            "size_id": obj.get("size_id"),
            "user_bot": UserBotBase.from_dict(obj["user_bot"]) if obj.get("user_bot") is not None else None,
            "size": SizeBase.from_dict(obj["size"]) if obj.get("size") is not None else None,
            "item": ItemBase.from_dict(obj["item"]) if obj.get("item") is not None else None
        })
        return _obj


