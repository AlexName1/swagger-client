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


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictInt, StrictStr
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class InfoItemUpdateNew(BaseModel):
    """
    InfoItemUpdateNew
    """ # noqa: E501
    code: StrictStr
    retail_price: Optional[StrictInt] = None
    link: Optional[StrictStr] = None
    discount_price: Optional[StrictInt] = None
    __properties: ClassVar[List[str]] = ["code", "retail_price", "link", "discount_price"]

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
        """Create an instance of InfoItemUpdateNew from a JSON string"""
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
        # set to None if retail_price (nullable) is None
        # and model_fields_set contains the field
        if self.retail_price is None and "retail_price" in self.model_fields_set:
            _dict['retail_price'] = None

        # set to None if link (nullable) is None
        # and model_fields_set contains the field
        if self.link is None and "link" in self.model_fields_set:
            _dict['link'] = None

        # set to None if discount_price (nullable) is None
        # and model_fields_set contains the field
        if self.discount_price is None and "discount_price" in self.model_fields_set:
            _dict['discount_price'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of InfoItemUpdateNew from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "code": obj.get("code"),
            "retail_price": obj.get("retail_price"),
            "link": obj.get("link"),
            "discount_price": obj.get("discount_price")
        })
        return _obj


