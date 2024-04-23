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
from pydantic import BaseModel, ConfigDict, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from swagger_client.models.bot_base import BotBase
from swagger_client.models.order_base import OrderBase
from swagger_client.models.partner_base import PartnerBase
from swagger_client.models.user_base_db import UserBaseDb
from swagger_client.models.utm_mark_base import UtmMarkBase
from typing import Optional, Set
from typing_extensions import Self

class UserBotBaseDb(BaseModel):
    """
    UserBotBaseDb
    """ # noqa: E501
    id: StrictInt
    user_id: StrictInt
    bot_token: StrictStr
    last_mess: StrictInt
    items: Optional[StrictStr] = None
    new_user: StrictBool
    subscribe_channel: StrictBool
    utm_mark_id: Optional[StrictInt] = None
    date_added: Optional[datetime] = None
    user: Optional[UserBaseDb] = None
    bot: Optional[BotBase] = None
    partner: Optional[PartnerBase] = None
    utm_mark: Optional[UtmMarkBase] = None
    orders: Optional[List[OrderBase]] = None
    __properties: ClassVar[List[str]] = ["id", "user_id", "bot_token", "last_mess", "items", "new_user", "subscribe_channel", "utm_mark_id", "date_added", "user", "bot", "partner", "utm_mark", "orders"]

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
        """Create an instance of UserBotBaseDb from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of user
        if self.user:
            _dict['user'] = self.user.to_dict()
        # override the default output from pydantic by calling `to_dict()` of bot
        if self.bot:
            _dict['bot'] = self.bot.to_dict()
        # override the default output from pydantic by calling `to_dict()` of partner
        if self.partner:
            _dict['partner'] = self.partner.to_dict()
        # override the default output from pydantic by calling `to_dict()` of utm_mark
        if self.utm_mark:
            _dict['utm_mark'] = self.utm_mark.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in orders (list)
        _items = []
        if self.orders:
            for _item in self.orders:
                if _item:
                    _items.append(_item.to_dict())
            _dict['orders'] = _items
        # set to None if items (nullable) is None
        # and model_fields_set contains the field
        if self.items is None and "items" in self.model_fields_set:
            _dict['items'] = None

        # set to None if utm_mark_id (nullable) is None
        # and model_fields_set contains the field
        if self.utm_mark_id is None and "utm_mark_id" in self.model_fields_set:
            _dict['utm_mark_id'] = None

        # set to None if date_added (nullable) is None
        # and model_fields_set contains the field
        if self.date_added is None and "date_added" in self.model_fields_set:
            _dict['date_added'] = None

        # set to None if user (nullable) is None
        # and model_fields_set contains the field
        if self.user is None and "user" in self.model_fields_set:
            _dict['user'] = None

        # set to None if bot (nullable) is None
        # and model_fields_set contains the field
        if self.bot is None and "bot" in self.model_fields_set:
            _dict['bot'] = None

        # set to None if partner (nullable) is None
        # and model_fields_set contains the field
        if self.partner is None and "partner" in self.model_fields_set:
            _dict['partner'] = None

        # set to None if utm_mark (nullable) is None
        # and model_fields_set contains the field
        if self.utm_mark is None and "utm_mark" in self.model_fields_set:
            _dict['utm_mark'] = None

        # set to None if orders (nullable) is None
        # and model_fields_set contains the field
        if self.orders is None and "orders" in self.model_fields_set:
            _dict['orders'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UserBotBaseDb from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "user_id": obj.get("user_id"),
            "bot_token": obj.get("bot_token"),
            "last_mess": obj.get("last_mess"),
            "items": obj.get("items"),
            "new_user": obj.get("new_user"),
            "subscribe_channel": obj.get("subscribe_channel"),
            "utm_mark_id": obj.get("utm_mark_id"),
            "date_added": obj.get("date_added"),
            "user": UserBaseDb.from_dict(obj["user"]) if obj.get("user") is not None else None,
            "bot": BotBase.from_dict(obj["bot"]) if obj.get("bot") is not None else None,
            "partner": PartnerBase.from_dict(obj["partner"]) if obj.get("partner") is not None else None,
            "utm_mark": UtmMarkBase.from_dict(obj["utm_mark"]) if obj.get("utm_mark") is not None else None,
            "orders": [OrderBase.from_dict(_item) for _item in obj["orders"]] if obj.get("orders") is not None else None
        })
        return _obj


