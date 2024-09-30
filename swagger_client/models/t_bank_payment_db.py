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
from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class TBankPaymentDb(BaseModel):
    """
    TBankPaymentDb
    """ # noqa: E501
    id: StrictInt
    tbank_kassa_id: Optional[StrictInt]
    order_id: Optional[StrictInt]
    tbank_payment_id: StrictStr
    tbank_status: StrictStr
    tbank_order_id: StrictStr
    tbank_amount: StrictInt
    tbank_payment_url: Optional[StrictStr]
    tbank_redirect_due_date: Optional[datetime]
    create_datetime: datetime
    __properties: ClassVar[List[str]] = ["id", "tbank_kassa_id", "order_id", "tbank_payment_id", "tbank_status", "tbank_order_id", "tbank_amount", "tbank_payment_url", "tbank_redirect_due_date", "create_datetime"]

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
        """Create an instance of TBankPaymentDb from a JSON string"""
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
        # set to None if tbank_kassa_id (nullable) is None
        # and model_fields_set contains the field
        if self.tbank_kassa_id is None and "tbank_kassa_id" in self.model_fields_set:
            _dict['tbank_kassa_id'] = None

        # set to None if order_id (nullable) is None
        # and model_fields_set contains the field
        if self.order_id is None and "order_id" in self.model_fields_set:
            _dict['order_id'] = None

        # set to None if tbank_payment_url (nullable) is None
        # and model_fields_set contains the field
        if self.tbank_payment_url is None and "tbank_payment_url" in self.model_fields_set:
            _dict['tbank_payment_url'] = None

        # set to None if tbank_redirect_due_date (nullable) is None
        # and model_fields_set contains the field
        if self.tbank_redirect_due_date is None and "tbank_redirect_due_date" in self.model_fields_set:
            _dict['tbank_redirect_due_date'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TBankPaymentDb from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "tbank_kassa_id": obj.get("tbank_kassa_id"),
            "order_id": obj.get("order_id"),
            "tbank_payment_id": obj.get("tbank_payment_id"),
            "tbank_status": obj.get("tbank_status"),
            "tbank_order_id": obj.get("tbank_order_id"),
            "tbank_amount": obj.get("tbank_amount"),
            "tbank_payment_url": obj.get("tbank_payment_url"),
            "tbank_redirect_due_date": obj.get("tbank_redirect_due_date"),
            "create_datetime": obj.get("create_datetime")
        })
        return _obj


