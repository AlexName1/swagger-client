# coding: utf-8

"""
    Rest DB

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations

import json
import pprint
import re  # noqa: F401
from typing import Any, ClassVar, Dict, List, Optional

from pydantic import BaseModel, StrictBool, StrictInt, StrictStr

from swagger_client.models.basket_base_db import BasketBaseDb

try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class InsertOrder(BaseModel):
    """
    InsertOrder
    """  # noqa: E501

    buyer: StrictStr
    delivery: Optional[StrictStr] = None
    address: Optional[StrictStr] = None
    phone: Optional[StrictStr] = None
    checking: StrictBool
    comment: Optional[StrictStr] = None
    partner: Optional[StrictBool] = None
    user_id: StrictInt
    pod: Optional[StrictInt] = None
    basket: List[BasketBaseDb]
    __properties: ClassVar[List[str]] = [
        "buyer",
        "delivery",
        "address",
        "phone",
        "checking",
        "comment",
        "partner",
        "user_id",
        "pod",
        "basket",
    ]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
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
        """Create an instance of InsertOrder from a JSON string"""
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
            exclude={},
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in basket (list)
        _items = []
        if self.basket:
            for _item in self.basket:
                if _item:
                    _items.append(_item.to_dict())
            _dict["basket"] = _items
        # set to None if delivery (nullable) is None
        # and model_fields_set contains the field
        if self.delivery is None and "delivery" in self.model_fields_set:
            _dict["delivery"] = None

        # set to None if address (nullable) is None
        # and model_fields_set contains the field
        if self.address is None and "address" in self.model_fields_set:
            _dict["address"] = None

        # set to None if phone (nullable) is None
        # and model_fields_set contains the field
        if self.phone is None and "phone" in self.model_fields_set:
            _dict["phone"] = None

        # set to None if comment (nullable) is None
        # and model_fields_set contains the field
        if self.comment is None and "comment" in self.model_fields_set:
            _dict["comment"] = None

        # set to None if partner (nullable) is None
        # and model_fields_set contains the field
        if self.partner is None and "partner" in self.model_fields_set:
            _dict["partner"] = None

        # set to None if pod (nullable) is None
        # and model_fields_set contains the field
        if self.pod is None and "pod" in self.model_fields_set:
            _dict["pod"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of InsertOrder from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "buyer": obj.get("buyer"),
                "delivery": obj.get("delivery"),
                "address": obj.get("address"),
                "phone": obj.get("phone"),
                "checking": obj.get("checking"),
                "comment": obj.get("comment"),
                "partner": obj.get("partner"),
                "user_id": obj.get("user_id"),
                "pod": obj.get("pod"),
                "basket": [BasketBaseDb.from_dict(_item) for _item in obj.get("basket")]
                if obj.get("basket") is not None
                else None,
            }
        )
        return _obj
