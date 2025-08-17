# coding: utf-8

"""
Telegram Bot API - REST API Client
The Bot API is an HTTP-based interface created for developers keen on building bots for Telegram. To learn how to create and set up a bot, please consult our Introduction to Bots and Bot FAQ.

## Metadata

- **Copyright**: Copyright (c) 2025 Qntx
- **Author**: ΣX <gitctrlx@gmail.com>
- **Version**: 9.2.0
- **Modified**: 2025-08-17T02:10:52.303427632Z[Etc/UTC]
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

from pydantic import BaseModel, ConfigDict, Field, StrictBool
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class BusinessBotRights(BaseModel):
    """
    Represents the rights of a business bot.
    """ # noqa: E501
    can_reply: Optional[StrictBool] = Field(default=True, description="*Optional*. *True*, if the bot can send and edit messages in the private chats that had incoming messages in the last 24 hours")
    can_read_messages: Optional[StrictBool] = Field(default=True, description="*Optional*. *True*, if the bot can mark incoming private messages as read")
    can_delete_sent_messages: Optional[StrictBool] = Field(default=True, description="*Optional*. *True*, if the bot can delete messages sent by the bot")
    can_delete_all_messages: Optional[StrictBool] = Field(default=True, description="*Optional*. *True*, if the bot can delete all private messages in managed chats")
    can_edit_name: Optional[StrictBool] = Field(default=True, description="*Optional*. *True*, if the bot can edit the first and last name of the business account")
    can_edit_bio: Optional[StrictBool] = Field(default=True, description="*Optional*. *True*, if the bot can edit the bio of the business account")
    can_edit_profile_photo: Optional[StrictBool] = Field(default=True, description="*Optional*. *True*, if the bot can edit the profile photo of the business account")
    can_edit_username: Optional[StrictBool] = Field(default=True, description="*Optional*. *True*, if the bot can edit the username of the business account")
    can_change_gift_settings: Optional[StrictBool] = Field(default=True, description="*Optional*. *True*, if the bot can change the privacy settings pertaining to gifts for the business account")
    can_view_gifts_and_stars: Optional[StrictBool] = Field(default=True, description="*Optional*. *True*, if the bot can view gifts and the amount of Telegram Stars owned by the business account")
    can_convert_gifts_to_stars: Optional[StrictBool] = Field(default=True, description="*Optional*. *True*, if the bot can convert regular gifts owned by the business account to Telegram Stars")
    can_transfer_and_upgrade_gifts: Optional[StrictBool] = Field(default=True, description="*Optional*. *True*, if the bot can transfer and upgrade gifts owned by the business account")
    can_transfer_stars: Optional[StrictBool] = Field(default=True, description="*Optional*. *True*, if the bot can transfer Telegram Stars received by the business account to its own account, or use them to upgrade and transfer gifts")
    can_manage_stories: Optional[StrictBool] = Field(default=True, description="*Optional*. *True*, if the bot can post, edit and delete stories on behalf of the business account")
    __properties: ClassVar[List[str]] = ["can_reply", "can_read_messages", "can_delete_sent_messages", "can_delete_all_messages", "can_edit_name", "can_edit_bio", "can_edit_profile_photo", "can_edit_username", "can_change_gift_settings", "can_view_gifts_and_stars", "can_convert_gifts_to_stars", "can_transfer_and_upgrade_gifts", "can_transfer_stars", "can_manage_stories"]

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
        """Create an instance of BusinessBotRights from a JSON string"""
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
        """Create an instance of BusinessBotRights from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in BusinessBotRights) in the input: " + _key)

        _obj = cls.model_validate({
            "can_reply": obj.get("can_reply") if obj.get("can_reply") is not None else True,
            "can_read_messages": obj.get("can_read_messages") if obj.get("can_read_messages") is not None else True,
            "can_delete_sent_messages": obj.get("can_delete_sent_messages") if obj.get("can_delete_sent_messages") is not None else True,
            "can_delete_all_messages": obj.get("can_delete_all_messages") if obj.get("can_delete_all_messages") is not None else True,
            "can_edit_name": obj.get("can_edit_name") if obj.get("can_edit_name") is not None else True,
            "can_edit_bio": obj.get("can_edit_bio") if obj.get("can_edit_bio") is not None else True,
            "can_edit_profile_photo": obj.get("can_edit_profile_photo") if obj.get("can_edit_profile_photo") is not None else True,
            "can_edit_username": obj.get("can_edit_username") if obj.get("can_edit_username") is not None else True,
            "can_change_gift_settings": obj.get("can_change_gift_settings") if obj.get("can_change_gift_settings") is not None else True,
            "can_view_gifts_and_stars": obj.get("can_view_gifts_and_stars") if obj.get("can_view_gifts_and_stars") is not None else True,
            "can_convert_gifts_to_stars": obj.get("can_convert_gifts_to_stars") if obj.get("can_convert_gifts_to_stars") is not None else True,
            "can_transfer_and_upgrade_gifts": obj.get("can_transfer_and_upgrade_gifts") if obj.get("can_transfer_and_upgrade_gifts") is not None else True,
            "can_transfer_stars": obj.get("can_transfer_stars") if obj.get("can_transfer_stars") is not None else True,
            "can_manage_stories": obj.get("can_manage_stories") if obj.get("can_manage_stories") is not None else True
        })
        return _obj


