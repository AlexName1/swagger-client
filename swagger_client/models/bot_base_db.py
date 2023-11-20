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

class BotBaseDb(BaseModel):
    """
    BotBaseDb
    """ # noqa: E501
    id: Optional[StrictInt] = None
    token: Optional[StrictStr] = None
    full_name: Optional[StrictStr] = None
    username: Optional[StrictStr] = None
    id_bot: Optional[StrictInt] = None
    admin_list: Optional[List[StrictInt]] = None
    text_channel_url: Optional[StrictStr] = None
    support_url: Optional[StrictStr] = None
    channel_url: Optional[StrictStr] = None
    info_url: Optional[StrictStr] = None
    comments_url: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["id", "token", "full_name", "username", "id_bot", "admin_list", "text_channel_url", "support_url", "channel_url", "info_url", "comments_url"]

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
        """Create an instance of BotBaseDb from a JSON string"""
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

        # set to None if token (nullable) is None
        # and model_fields_set contains the field
        if self.token is None and "token" in self.model_fields_set:
            _dict['token'] = None

        # set to None if full_name (nullable) is None
        # and model_fields_set contains the field
        if self.full_name is None and "full_name" in self.model_fields_set:
            _dict['full_name'] = None

        # set to None if username (nullable) is None
        # and model_fields_set contains the field
        if self.username is None and "username" in self.model_fields_set:
            _dict['username'] = None

        # set to None if id_bot (nullable) is None
        # and model_fields_set contains the field
        if self.id_bot is None and "id_bot" in self.model_fields_set:
            _dict['id_bot'] = None

        # set to None if admin_list (nullable) is None
        # and model_fields_set contains the field
        if self.admin_list is None and "admin_list" in self.model_fields_set:
            _dict['admin_list'] = None

        # set to None if text_channel_url (nullable) is None
        # and model_fields_set contains the field
        if self.text_channel_url is None and "text_channel_url" in self.model_fields_set:
            _dict['text_channel_url'] = None

        # set to None if support_url (nullable) is None
        # and model_fields_set contains the field
        if self.support_url is None and "support_url" in self.model_fields_set:
            _dict['support_url'] = None

        # set to None if channel_url (nullable) is None
        # and model_fields_set contains the field
        if self.channel_url is None and "channel_url" in self.model_fields_set:
            _dict['channel_url'] = None

        # set to None if info_url (nullable) is None
        # and model_fields_set contains the field
        if self.info_url is None and "info_url" in self.model_fields_set:
            _dict['info_url'] = None

        # set to None if comments_url (nullable) is None
        # and model_fields_set contains the field
        if self.comments_url is None and "comments_url" in self.model_fields_set:
            _dict['comments_url'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of BotBaseDb from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "token": obj.get("token"),
            "full_name": obj.get("full_name"),
            "username": obj.get("username"),
            "id_bot": obj.get("id_bot"),
            "admin_list": obj.get("admin_list"),
            "text_channel_url": obj.get("text_channel_url"),
            "support_url": obj.get("support_url"),
            "channel_url": obj.get("channel_url"),
            "info_url": obj.get("info_url"),
            "comments_url": obj.get("comments_url")
        })
        return _obj
