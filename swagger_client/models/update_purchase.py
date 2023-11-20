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

from pydantic import BaseModel, StrictInt, StrictStr

try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class UpdatePurchase(BaseModel):
    """
    UpdatePurchase
    """ # noqa: E501
    purchase_id: StrictInt
    add_info: Optional[StrictStr] = None
    add_photo: Optional[StrictStr] = None
    status: Optional[StrictInt] = None
    __properties: ClassVar[List[str]] = ["purchase_id", "add_info", "add_photo", "status"]

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
        """Create an instance of UpdatePurchase from a JSON string"""
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
        # set to None if add_info (nullable) is None
        # and model_fields_set contains the field
        if self.add_info is None and "add_info" in self.model_fields_set:
            _dict['add_info'] = None

        # set to None if add_photo (nullable) is None
        # and model_fields_set contains the field
        if self.add_photo is None and "add_photo" in self.model_fields_set:
            _dict['add_photo'] = None

        # set to None if status (nullable) is None
        # and model_fields_set contains the field
        if self.status is None and "status" in self.model_fields_set:
            _dict['status'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of UpdatePurchase from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "purchase_id": obj.get("purchase_id"),
            "add_info": obj.get("add_info"),
            "add_photo": obj.get("add_photo"),
            "status": obj.get("status")
        })
        return _obj
