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

from swagger_client.models.delivery_cdek_base import DeliveryCdekBase
from swagger_client.models.item_base import ItemBase
from swagger_client.models.order_base import OrderBase
from swagger_client.models.size_base import SizeBase
from swagger_client.models.yookassa_payment_base import YookassaPaymentBase

try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class PurchaseBaseDb(BaseModel):
    """
    PurchaseBaseDb
    """ # noqa: E501
    id: Optional[StrictInt] = None
    created: Optional[datetime] = None
    buyer: Optional[StrictStr] = None
    code: Optional[StrictStr] = None
    price: Optional[StrictInt] = None
    delivery: Optional[StrictStr] = None
    address: Optional[StrictStr] = None
    phone: Optional[StrictStr] = None
    checking: Optional[StrictBool] = None
    pod: Optional[StrictInt] = None
    invoice: Optional[StrictStr] = None
    comment: Optional[StrictStr] = None
    status: Optional[StrictInt] = None
    add_info: Optional[StrictStr] = None
    user_id: Optional[StrictInt] = None
    add_photo: Optional[StrictStr] = None
    partner: Optional[StrictBool] = None
    paid: Optional[StrictBool] = None
    delivery_cdek_id: Optional[StrictInt] = None
    approve_size: Optional[StrictBool] = None
    size_id: Optional[StrictInt] = None
    bot_id: Optional[StrictInt] = None
    order_id: Optional[StrictInt] = None
    delivery_cdek_photo_tg_file_id: Optional[StrictStr] = None
    item: Optional[ItemBase] = None
    order: Optional[OrderBase] = None
    delivery_cdek: Optional[DeliveryCdekBase] = None
    size: Optional[SizeBase] = None
    yookassa_payment: Optional[YookassaPaymentBase] = None
    __properties: ClassVar[List[str]] = ["id", "created", "buyer", "code", "price", "delivery", "address", "phone", "checking", "pod", "invoice", "comment", "status", "add_info", "user_id", "add_photo", "partner", "paid", "delivery_cdek_id", "approve_size", "size_id", "bot_id", "order_id", "delivery_cdek_photo_tg_file_id", "item", "order", "delivery_cdek", "size", "yookassa_payment"]

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
        """Create an instance of PurchaseBaseDb from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of item
        if self.item:
            _dict['item'] = self.item.to_dict()
        # override the default output from pydantic by calling `to_dict()` of order
        if self.order:
            _dict['order'] = self.order.to_dict()
        # override the default output from pydantic by calling `to_dict()` of delivery_cdek
        if self.delivery_cdek:
            _dict['delivery_cdek'] = self.delivery_cdek.to_dict()
        # override the default output from pydantic by calling `to_dict()` of size
        if self.size:
            _dict['size'] = self.size.to_dict()
        # override the default output from pydantic by calling `to_dict()` of yookassa_payment
        if self.yookassa_payment:
            _dict['yookassa_payment'] = self.yookassa_payment.to_dict()
        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if created (nullable) is None
        # and model_fields_set contains the field
        if self.created is None and "created" in self.model_fields_set:
            _dict['created'] = None

        # set to None if buyer (nullable) is None
        # and model_fields_set contains the field
        if self.buyer is None and "buyer" in self.model_fields_set:
            _dict['buyer'] = None

        # set to None if code (nullable) is None
        # and model_fields_set contains the field
        if self.code is None and "code" in self.model_fields_set:
            _dict['code'] = None

        # set to None if price (nullable) is None
        # and model_fields_set contains the field
        if self.price is None and "price" in self.model_fields_set:
            _dict['price'] = None

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

        # set to None if pod (nullable) is None
        # and model_fields_set contains the field
        if self.pod is None and "pod" in self.model_fields_set:
            _dict['pod'] = None

        # set to None if invoice (nullable) is None
        # and model_fields_set contains the field
        if self.invoice is None and "invoice" in self.model_fields_set:
            _dict['invoice'] = None

        # set to None if comment (nullable) is None
        # and model_fields_set contains the field
        if self.comment is None and "comment" in self.model_fields_set:
            _dict['comment'] = None

        # set to None if status (nullable) is None
        # and model_fields_set contains the field
        if self.status is None and "status" in self.model_fields_set:
            _dict['status'] = None

        # set to None if add_info (nullable) is None
        # and model_fields_set contains the field
        if self.add_info is None and "add_info" in self.model_fields_set:
            _dict['add_info'] = None

        # set to None if user_id (nullable) is None
        # and model_fields_set contains the field
        if self.user_id is None and "user_id" in self.model_fields_set:
            _dict['user_id'] = None

        # set to None if add_photo (nullable) is None
        # and model_fields_set contains the field
        if self.add_photo is None and "add_photo" in self.model_fields_set:
            _dict['add_photo'] = None

        # set to None if partner (nullable) is None
        # and model_fields_set contains the field
        if self.partner is None and "partner" in self.model_fields_set:
            _dict['partner'] = None

        # set to None if paid (nullable) is None
        # and model_fields_set contains the field
        if self.paid is None and "paid" in self.model_fields_set:
            _dict['paid'] = None

        # set to None if delivery_cdek_id (nullable) is None
        # and model_fields_set contains the field
        if self.delivery_cdek_id is None and "delivery_cdek_id" in self.model_fields_set:
            _dict['delivery_cdek_id'] = None

        # set to None if approve_size (nullable) is None
        # and model_fields_set contains the field
        if self.approve_size is None and "approve_size" in self.model_fields_set:
            _dict['approve_size'] = None

        # set to None if size_id (nullable) is None
        # and model_fields_set contains the field
        if self.size_id is None and "size_id" in self.model_fields_set:
            _dict['size_id'] = None

        # set to None if bot_id (nullable) is None
        # and model_fields_set contains the field
        if self.bot_id is None and "bot_id" in self.model_fields_set:
            _dict['bot_id'] = None

        # set to None if order_id (nullable) is None
        # and model_fields_set contains the field
        if self.order_id is None and "order_id" in self.model_fields_set:
            _dict['order_id'] = None

        # set to None if delivery_cdek_photo_tg_file_id (nullable) is None
        # and model_fields_set contains the field
        if self.delivery_cdek_photo_tg_file_id is None and "delivery_cdek_photo_tg_file_id" in self.model_fields_set:
            _dict['delivery_cdek_photo_tg_file_id'] = None

        # set to None if item (nullable) is None
        # and model_fields_set contains the field
        if self.item is None and "item" in self.model_fields_set:
            _dict['item'] = None

        # set to None if order (nullable) is None
        # and model_fields_set contains the field
        if self.order is None and "order" in self.model_fields_set:
            _dict['order'] = None

        # set to None if delivery_cdek (nullable) is None
        # and model_fields_set contains the field
        if self.delivery_cdek is None and "delivery_cdek" in self.model_fields_set:
            _dict['delivery_cdek'] = None

        # set to None if size (nullable) is None
        # and model_fields_set contains the field
        if self.size is None and "size" in self.model_fields_set:
            _dict['size'] = None

        # set to None if yookassa_payment (nullable) is None
        # and model_fields_set contains the field
        if self.yookassa_payment is None and "yookassa_payment" in self.model_fields_set:
            _dict['yookassa_payment'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of PurchaseBaseDb from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "created": obj.get("created"),
            "buyer": obj.get("buyer"),
            "code": obj.get("code"),
            "price": obj.get("price"),
            "delivery": obj.get("delivery"),
            "address": obj.get("address"),
            "phone": obj.get("phone"),
            "checking": obj.get("checking"),
            "pod": obj.get("pod"),
            "invoice": obj.get("invoice"),
            "comment": obj.get("comment"),
            "status": obj.get("status"),
            "add_info": obj.get("add_info"),
            "user_id": obj.get("user_id"),
            "add_photo": obj.get("add_photo"),
            "partner": obj.get("partner"),
            "paid": obj.get("paid"),
            "delivery_cdek_id": obj.get("delivery_cdek_id"),
            "approve_size": obj.get("approve_size"),
            "size_id": obj.get("size_id"),
            "bot_id": obj.get("bot_id"),
            "order_id": obj.get("order_id"),
            "delivery_cdek_photo_tg_file_id": obj.get("delivery_cdek_photo_tg_file_id"),
            "item": ItemBase.from_dict(obj.get("item")) if obj.get("item") is not None else None,
            "order": OrderBase.from_dict(obj.get("order")) if obj.get("order") is not None else None,
            "delivery_cdek": DeliveryCdekBase.from_dict(obj.get("delivery_cdek")) if obj.get("delivery_cdek") is not None else None,
            "size": SizeBase.from_dict(obj.get("size")) if obj.get("size") is not None else None,
            "yookassa_payment": YookassaPaymentBase.from_dict(obj.get("yookassa_payment")) if obj.get("yookassa_payment") is not None else None
        })
        return _obj
