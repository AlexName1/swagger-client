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
from swagger_client.models.category_base import CategoryBase
from swagger_client.models.dimension_base import DimensionBase
from swagger_client.models.quantity_base_db import QuantityBaseDb
from typing import Optional, Set
from typing_extensions import Self

class ItemBaseDb(BaseModel):
    """
    ItemBaseDb
    """ # noqa: E501
    id: StrictInt
    code: StrictStr
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
    code_hash: StrictStr
    category_id: StrictStr
    manufacturer_country: Optional[StrictStr] = None
    material: Optional[StrictStr] = None
    dimension_id: Optional[StrictStr] = None
    is_original: StrictBool
    quantities: Optional[List[QuantityBaseDb]] = None
    category: Optional[CategoryBase] = None
    dimension: Optional[DimensionBase] = None
    __properties: ClassVar[List[str]] = ["id", "code", "changed", "active", "brand", "model", "title", "retail_price", "drop_price", "link", "photos", "season", "color", "discount_price", "new", "code_hash", "category_id", "manufacturer_country", "material", "dimension_id", "is_original", "quantities", "category", "dimension"]

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
        """Create an instance of ItemBaseDb from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in quantities (list)
        _items = []
        if self.quantities:
            for _item in self.quantities:
                if _item:
                    _items.append(_item.to_dict())
            _dict['quantities'] = _items
        # override the default output from pydantic by calling `to_dict()` of category
        if self.category:
            _dict['category'] = self.category.to_dict()
        # override the default output from pydantic by calling `to_dict()` of dimension
        if self.dimension:
            _dict['dimension'] = self.dimension.to_dict()
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

        # set to None if quantities (nullable) is None
        # and model_fields_set contains the field
        if self.quantities is None and "quantities" in self.model_fields_set:
            _dict['quantities'] = None

        # set to None if category (nullable) is None
        # and model_fields_set contains the field
        if self.category is None and "category" in self.model_fields_set:
            _dict['category'] = None

        # set to None if dimension (nullable) is None
        # and model_fields_set contains the field
        if self.dimension is None and "dimension" in self.model_fields_set:
            _dict['dimension'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ItemBaseDb from a dict"""
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
            "is_original": obj.get("is_original"),
            "quantities": [QuantityBaseDb.from_dict(_item) for _item in obj["quantities"]] if obj.get("quantities") is not None else None,
            "category": CategoryBase.from_dict(obj["category"]) if obj.get("category") is not None else None,
            "dimension": DimensionBase.from_dict(obj["dimension"]) if obj.get("dimension") is not None else None
        })
        return _obj


