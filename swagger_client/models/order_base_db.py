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
from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from swagger_client.models.purchase_base_db import PurchaseBaseDb
from swagger_client.models.user_bot_base_db import UserBotBaseDb
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class OrderBaseDb(BaseModel):
    """
    OrderBaseDb
    """ # noqa: E501
    id: Optional[StrictInt] = None
    created: Optional[datetime] = None
    user_bot_id: Optional[StrictInt] = None
    buyer: Optional[StrictStr] = None
    delivery: Optional[StrictStr] = None
    address: Optional[StrictStr] = None
    phone: Optional[StrictStr] = None
    checking: Optional[StrictBool] = None
    payment_receipt: Optional[StrictStr] = None
    comment: Optional[StrictStr] = None
    partner: Optional[StrictBool] = None
    paid: Optional[StrictBool] = None
    purchases: Optional[List[PurchaseBaseDb]] = None
    user_bot: Optional[UserBotBaseDb] = None
    __properties: ClassVar[List[str]] = ["id", "created", "user_bot_id", "buyer", "delivery", "address", "phone", "checking", "payment_receipt", "comment", "partner", "paid", "purchases", "user_bot"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of OrderBaseDb from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in purchases (list)
        _items = []
        if self.purchases:
            for _item in self.purchases:
                if _item:
                    _items.append(_item.to_dict())
            _dict['purchases'] = _items
        # override the default output from pydantic by calling `to_dict()` of user_bot
        if self.user_bot:
            _dict['user_bot'] = self.user_bot.to_dict()
        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if created (nullable) is None
        # and model_fields_set contains the field
        if self.created is None and "created" in self.model_fields_set:
            _dict['created'] = None

        # set to None if user_bot_id (nullable) is None
        # and model_fields_set contains the field
        if self.user_bot_id is None and "user_bot_id" in self.model_fields_set:
            _dict['user_bot_id'] = None

        # set to None if buyer (nullable) is None
        # and model_fields_set contains the field
        if self.buyer is None and "buyer" in self.model_fields_set:
            _dict['buyer'] = None

        # set to None if delivery (nullable) is None
        # and model_fields_set contains the field
        if self.delivery is None and "delivery" in self.model_fields_set:
            _dict['delivery'] = None

        # set to None if address (nullable) is None
        # and model_fields_set contains the field
        if self.address is None and "address" in self.model_fields_set:
            _dict['address'] = None

        # set to None if phone (nullable) is None
        # and model_fields_set contains the field
        if self.phone is None and "phone" in self.model_fields_set:
            _dict['phone'] = None

        # set to None if checking (nullable) is None
        # and model_fields_set contains the field
        if self.checking is None and "checking" in self.model_fields_set:
            _dict['checking'] = None

        # set to None if payment_receipt (nullable) is None
        # and model_fields_set contains the field
        if self.payment_receipt is None and "payment_receipt" in self.model_fields_set:
            _dict['payment_receipt'] = None

        # set to None if comment (nullable) is None
        # and model_fields_set contains the field
        if self.comment is None and "comment" in self.model_fields_set:
            _dict['comment'] = None

        # set to None if partner (nullable) is None
        # and model_fields_set contains the field
        if self.partner is None and "partner" in self.model_fields_set:
            _dict['partner'] = None

        # set to None if paid (nullable) is None
        # and model_fields_set contains the field
        if self.paid is None and "paid" in self.model_fields_set:
            _dict['paid'] = None

        # set to None if purchases (nullable) is None
        # and model_fields_set contains the field
        if self.purchases is None and "purchases" in self.model_fields_set:
            _dict['purchases'] = None

        # set to None if user_bot (nullable) is None
        # and model_fields_set contains the field
        if self.user_bot is None and "user_bot" in self.model_fields_set:
            _dict['user_bot'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of OrderBaseDb from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "created": obj.get("created"),
            "user_bot_id": obj.get("user_bot_id"),
            "buyer": obj.get("buyer"),
            "delivery": obj.get("delivery"),
            "address": obj.get("address"),
            "phone": obj.get("phone"),
            "checking": obj.get("checking"),
            "payment_receipt": obj.get("payment_receipt"),
            "comment": obj.get("comment"),
            "partner": obj.get("partner"),
            "paid": obj.get("paid"),
            "purchases": [PurchaseBaseDb.from_dict(_item) for _item in obj.get("purchases")] if obj.get("purchases") is not None else None,
            "user_bot": UserBotBaseDb.from_dict(obj.get("user_bot")) if obj.get("user_bot") is not None else None
        })
        return _obj


