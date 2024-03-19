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
from typing import Optional, Set
from typing_extensions import Self

class DeliveryCdekUpdate(BaseModel):
    """
    DeliveryCdekUpdate
    """ # noqa: E501
    delivery_cdek_id: StrictInt
    status_delivery: Optional[StrictStr] = None
    photo_tg_file_id: Optional[StrictStr] = None
    invoice_tg_file_id: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["delivery_cdek_id", "status_delivery", "photo_tg_file_id", "invoice_tg_file_id"]

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
        """Create an instance of DeliveryCdekUpdate from a JSON string"""
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
        # set to None if status_delivery (nullable) is None
        # and model_fields_set contains the field
        if self.status_delivery is None and "status_delivery" in self.model_fields_set:
            _dict['status_delivery'] = None

        # set to None if photo_tg_file_id (nullable) is None
        # and model_fields_set contains the field
        if self.photo_tg_file_id is None and "photo_tg_file_id" in self.model_fields_set:
            _dict['photo_tg_file_id'] = None

        # set to None if invoice_tg_file_id (nullable) is None
        # and model_fields_set contains the field
        if self.invoice_tg_file_id is None and "invoice_tg_file_id" in self.model_fields_set:
            _dict['invoice_tg_file_id'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DeliveryCdekUpdate from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "delivery_cdek_id": obj.get("delivery_cdek_id"),
            "status_delivery": obj.get("status_delivery"),
            "photo_tg_file_id": obj.get("photo_tg_file_id"),
            "invoice_tg_file_id": obj.get("invoice_tg_file_id")
        })
        return _obj


