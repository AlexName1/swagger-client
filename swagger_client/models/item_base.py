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
from datetime import datetime
from typing import Any, ClassVar, Dict, List, Optional

from pydantic import BaseModel, StrictBool, StrictInt, StrictStr

try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ItemBase(BaseModel):
    """
    ItemBase
    """ # noqa: E501
    id: Optional[StrictInt] = None
    code: Optional[StrictStr] = None
    changed: Optional[datetime] = None
    active: Optional[StrictBool] = None
    brand: Optional[StrictStr] = None
    model: Optional[StrictStr] = None
    title: Optional[StrictStr] = None
    retail_price: Optional[StrictInt] = None
    drop_price: Optional[StrictInt] = None
    link: Optional[StrictStr] = None
    photos: Optional[StrictStr] = None
    season: Optional[StrictStr] = None
    color: Optional[StrictStr] = None
    discount_price: Optional[StrictInt] = None
    new: Optional[StrictBool] = None
    code_hash: Optional[StrictStr] = None
    category_id: Optional[StrictStr] = None
    manufacturer_country: Optional[StrictStr] = None
    material: Optional[StrictStr] = None
    dimension_id: Optional[StrictInt] = None
    photo_path_tg: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["id", "code", "changed", "active", "brand", "model", "title", "retail_price", "drop_price", "link", "photos", "season", "color", "discount_price", "new", "code_hash", "category_id", "manufacturer_country", "material", "dimension_id", "photo_path_tg"]

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
        """Create an instance of ItemBase from a JSON string"""
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
        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if code (nullable) is None
        # and model_fields_set contains the field
        if self.code is None and "code" in self.model_fields_set:
            _dict['code'] = None

        # set to None if changed (nullable) is None
        # and model_fields_set contains the field
        if self.changed is None and "changed" in self.model_fields_set:
            _dict['changed'] = None

        # set to None if active (nullable) is None
        # and model_fields_set contains the field
        if self.active is None and "active" in self.model_fields_set:
            _dict['active'] = None

        # set to None if brand (nullable) is None
        # and model_fields_set contains the field
        if self.brand is None and "brand" in self.model_fields_set:
            _dict['brand'] = None

        # set to None if model (nullable) is None
        # and model_fields_set contains the field
        if self.model is None and "model" in self.model_fields_set:
            _dict['model'] = None

        # set to None if title (nullable) is None
        # and model_fields_set contains the field
        if self.title is None and "title" in self.model_fields_set:
            _dict['title'] = None

        # set to None if retail_price (nullable) is None
        # and model_fields_set contains the field
        if self.retail_price is None and "retail_price" in self.model_fields_set:
            _dict['retail_price'] = None

        # set to None if drop_price (nullable) is None
        # and model_fields_set contains the field
        if self.drop_price is None and "drop_price" in self.model_fields_set:
            _dict['drop_price'] = None

        # set to None if link (nullable) is None
        # and model_fields_set contains the field
        if self.link is None and "link" in self.model_fields_set:
            _dict['link'] = None

        # set to None if photos (nullable) is None
        # and model_fields_set contains the field
        if self.photos is None and "photos" in self.model_fields_set:
            _dict['photos'] = None

        # set to None if season (nullable) is None
        # and model_fields_set contains the field
        if self.season is None and "season" in self.model_fields_set:
            _dict['season'] = None

        # set to None if color (nullable) is None
        # and model_fields_set contains the field
        if self.color is None and "color" in self.model_fields_set:
            _dict['color'] = None

        # set to None if discount_price (nullable) is None
        # and model_fields_set contains the field
        if self.discount_price is None and "discount_price" in self.model_fields_set:
            _dict['discount_price'] = None

        # set to None if new (nullable) is None
        # and model_fields_set contains the field
        if self.new is None and "new" in self.model_fields_set:
            _dict['new'] = None

        # set to None if code_hash (nullable) is None
        # and model_fields_set contains the field
        if self.code_hash is None and "code_hash" in self.model_fields_set:
            _dict['code_hash'] = None

        # set to None if category_id (nullable) is None
        # and model_fields_set contains the field
        if self.category_id is None and "category_id" in self.model_fields_set:
            _dict['category_id'] = None

        # set to None if manufacturer_country (nullable) is None
        # and model_fields_set contains the field
        if self.manufacturer_country is None and "manufacturer_country" in self.model_fields_set:
            _dict['manufacturer_country'] = None

        # set to None if material (nullable) is None
        # and model_fields_set contains the field
        if self.material is None and "material" in self.model_fields_set:
            _dict['material'] = None

        # set to None if dimension_id (nullable) is None
        # and model_fields_set contains the field
        if self.dimension_id is None and "dimension_id" in self.model_fields_set:
            _dict['dimension_id'] = None

        # set to None if photo_path_tg (nullable) is None
        # and model_fields_set contains the field
        if self.photo_path_tg is None and "photo_path_tg" in self.model_fields_set:
            _dict['photo_path_tg'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ItemBase from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "code": obj.get("code"),
            "changed": obj.get("changed"),
            "active": obj.get("active"),
            "brand": obj.get("brand"),
            "model": obj.get("model"),
            "title": obj.get("title"),
            "retail_price": obj.get("retail_price"),
            "drop_price": obj.get("drop_price"),
            "link": obj.get("link"),
            "photos": obj.get("photos"),
            "season": obj.get("season"),
            "color": obj.get("color"),
            "discount_price": obj.get("discount_price"),
            "new": obj.get("new"),
            "code_hash": obj.get("code_hash"),
            "category_id": obj.get("category_id"),
            "manufacturer_country": obj.get("manufacturer_country"),
            "material": obj.get("material"),
            "dimension_id": obj.get("dimension_id"),
            "photo_path_tg": obj.get("photo_path_tg")
        })
        return _obj
