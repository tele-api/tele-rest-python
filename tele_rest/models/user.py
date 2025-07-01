# coding: utf-8

"""
Telegram Bot API - REST API Client
The Bot API is an HTTP-based interface created for developers keen on building bots for Telegram. To learn how to create and set up a bot, please consult our Introduction to Bots and Bot FAQ.

## Metadata

- **Copyright**: Copyright (c) 2025 Qntx
- **Author**: ΣX <gitctrlx@gmail.com>
- **Version**: 9.0.0
- **Modified**: 2025-07-01T14:36:24.755929598Z[Etc/UTC]
- **Generator Version**: 7.14.0

<details>
<summary><strong>⚠️ Important Disclaimer & Limitation of Liability</strong></summary>
<br>
> **IMPORTANT**: This software is provided "as is" without any warranties, express or implied, including but not limited
> to warranties of merchantability, fitness for a particular purpose, or non-infringement. The developers, contributors,
> and licensors (collectively, "Developers") make no representations regarding the accuracy, completeness, or reliability
> of this software or its outputs.
>
> This client is not intended to provide financial, investment, tax, or legal advice. It facilitates interaction with the
> Telegram Bot API service but does not endorse or recommend any financial actions, including the purchase, sale, or holding of
> financial instruments (e.g., stocks, bonds, derivatives, cryptocurrencies). Users must consult qualified financial or
> legal professionals before making decisions based on this software's outputs.
>
> Financial markets are inherently speculative and carry significant risks. Using this software in trading, analysis, or
> other financial activities may result in substantial losses, including total loss of capital. The Developers are not
> liable for any losses or damages arising from such use. Users assume full responsibility for validating the software's
> outputs and ensuring their suitability for intended purposes.
>
> This client may rely on third-party data or services (e.g., market feeds, APIs). The Developers do not control or verify
> the accuracy of these services and are not liable for any errors, delays, or losses resulting from their use. Users must
> comply with third-party terms and conditions.
>
> Users are solely responsible for ensuring compliance with all applicable financial, tax, and regulatory requirements in
> their jurisdiction. This includes obtaining necessary licenses or approvals for trading or investment activities. The
> Developers disclaim liability for any legal consequences arising from non-compliance.
>
> To the fullest extent permitted by law, the Developers shall not be liable for any direct, indirect, incidental,
> consequential, or punitive damages arising from the use or inability to use this software, including but not limited to
> loss of profits, data, or business opportunities.

</details>
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class User(BaseModel):
    """
    This object represents a Telegram user or bot.
    """ # noqa: E501
    id: StrictInt = Field(description="Unique identifier for this user or bot. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a 64-bit integer or double-precision float type are safe for storing this identifier.")
    is_bot: StrictBool = Field(description="*True*, if this user is a bot")
    first_name: StrictStr = Field(description="User's or bot's first name")
    last_name: Optional[StrictStr] = Field(default=None, description="*Optional*. User's or bot's last name")
    username: Optional[StrictStr] = Field(default=None, description="*Optional*. User's or bot's username")
    language_code: Optional[StrictStr] = Field(default=None, description="*Optional*. [IETF language tag](https://en.wikipedia.org/wiki/IETF_language_tag) of the user's language")
    is_premium: Optional[StrictBool] = Field(default=True, description="*Optional*. *True*, if this user is a Telegram Premium user")
    added_to_attachment_menu: Optional[StrictBool] = Field(default=True, description="*Optional*. *True*, if this user added the bot to the attachment menu")
    can_join_groups: Optional[StrictBool] = Field(default=None, description="*Optional*. *True*, if the bot can be invited to groups. Returned only in [getMe](https://core.telegram.org/bots/api/#getme).")
    can_read_all_group_messages: Optional[StrictBool] = Field(default=None, description="*Optional*. *True*, if [privacy mode](https://core.telegram.org/bots/features#privacy-mode) is disabled for the bot. Returned only in [getMe](https://core.telegram.org/bots/api/#getme).")
    supports_inline_queries: Optional[StrictBool] = Field(default=None, description="*Optional*. *True*, if the bot supports inline queries. Returned only in [getMe](https://core.telegram.org/bots/api/#getme).")
    can_connect_to_business: Optional[StrictBool] = Field(default=None, description="*Optional*. *True*, if the bot can be connected to a Telegram Business account to receive its messages. Returned only in [getMe](https://core.telegram.org/bots/api/#getme).")
    has_main_web_app: Optional[StrictBool] = Field(default=None, description="*Optional*. *True*, if the bot has a main Web App. Returned only in [getMe](https://core.telegram.org/bots/api/#getme).")
    __properties: ClassVar[List[str]] = ["id", "is_bot", "first_name", "last_name", "username", "language_code", "is_premium", "added_to_attachment_menu", "can_join_groups", "can_read_all_group_messages", "supports_inline_queries", "can_connect_to_business", "has_main_web_app"]

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
        """Create an instance of User from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of User from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in User) in the input: " + _key)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "is_bot": obj.get("is_bot"),
            "first_name": obj.get("first_name"),
            "last_name": obj.get("last_name"),
            "username": obj.get("username"),
            "language_code": obj.get("language_code"),
            "is_premium": obj.get("is_premium") if obj.get("is_premium") is not None else True,
            "added_to_attachment_menu": obj.get("added_to_attachment_menu") if obj.get("added_to_attachment_menu") is not None else True,
            "can_join_groups": obj.get("can_join_groups"),
            "can_read_all_group_messages": obj.get("can_read_all_group_messages"),
            "supports_inline_queries": obj.get("supports_inline_queries"),
            "can_connect_to_business": obj.get("can_connect_to_business"),
            "has_main_web_app": obj.get("has_main_web_app")
        })
        return _obj


