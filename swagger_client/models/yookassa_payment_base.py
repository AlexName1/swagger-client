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


class YookassaPaymentBase(BaseModel):
    """
    YookassaPaymentBase
    """  # noqa: E501

    id: Optional[StrictInt] = None
    purchase_id: Optional[StrictInt] = None
    payment_id: Optional[StrictStr] = None
    status: Optional[StrictStr] = None
    captured_at: Optional[StrictStr] = None
    email: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = [
        "id",
        "purchase_id",
        "payment_id",
        "status",
        "captured_at",
        "email",
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
        """Create an instance of YookassaPaymentBase from a JSON string"""
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
        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict["id"] = None

        # set to None if purchase_id (nullable) is None
        # and model_fields_set contains the field
        if self.purchase_id is None and "purchase_id" in self.model_fields_set:
            _dict["purchase_id"] = None

        # set to None if payment_id (nullable) is None
        # and model_fields_set contains the field
        if self.payment_id is None and "payment_id" in self.model_fields_set:
            _dict["payment_id"] = None

        # set to None if status (nullable) is None
        # and model_fields_set contains the field
        if self.status is None and "status" in self.model_fields_set:
            _dict["status"] = None

        # set to None if captured_at (nullable) is None
        # and model_fields_set contains the field
        if self.captured_at is None and "captured_at" in self.model_fields_set:
            _dict["captured_at"] = None

        # set to None if email (nullable) is None
        # and model_fields_set contains the field
        if self.email is None and "email" in self.model_fields_set:
            _dict["email"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of YookassaPaymentBase from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "id": obj.get("id"),
                "purchase_id": obj.get("purchase_id"),
                "payment_id": obj.get("payment_id"),
                "status": obj.get("status"),
                "captured_at": obj.get("captured_at"),
                "email": obj.get("email"),
            }
        )
        return _obj
