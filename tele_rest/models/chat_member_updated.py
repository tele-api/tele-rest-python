# coding: utf-8

"""
Telegram Bot API - REST API Client
The Bot API is an HTTP-based interface created for developers keen on building bots for Telegram. To learn how to create and set up a bot, please consult our Introduction to Bots and Bot FAQ.

## Metadata

- **Copyright**: Copyright (c) 2025 Qntx
- **Author**: ΣX <gitctrlx@gmail.com>
- **Version**: 9.1.0
- **Modified**: 2025-07-19T09:30:11.405683802Z[Etc/UTC]
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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from tele_rest.models.chat import Chat
from tele_rest.models.chat_invite_link import ChatInviteLink
from tele_rest.models.chat_member import ChatMember
from tele_rest.models.user import User
from typing import Optional, Set
from typing_extensions import Self

class ChatMemberUpdated(BaseModel):
    """
    This object represents changes in the status of a chat member.
    """ # noqa: E501
    chat: Chat
    var_from: User = Field(alias="from")
    var_date: StrictInt = Field(description="Date the change was done in Unix time", alias="date")
    old_chat_member: ChatMember
    new_chat_member: ChatMember
    invite_link: Optional[ChatInviteLink] = None
    via_join_request: Optional[StrictBool] = Field(default=None, description="*Optional*. *True*, if the user joined the chat after sending a direct join request without using an invite link and being approved by an administrator")
    via_chat_folder_invite_link: Optional[StrictBool] = Field(default=None, description="*Optional*. *True*, if the user joined the chat via a chat folder invite link")
    __properties: ClassVar[List[str]] = ["chat", "from", "date", "old_chat_member", "new_chat_member", "invite_link", "via_join_request", "via_chat_folder_invite_link"]

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
        """Create an instance of ChatMemberUpdated from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of chat
        if self.chat:
            _dict['chat'] = self.chat.to_dict()
        # override the default output from pydantic by calling `to_dict()` of var_from
        if self.var_from:
            _dict['from'] = self.var_from.to_dict()
        # override the default output from pydantic by calling `to_dict()` of old_chat_member
        if self.old_chat_member:
            _dict['old_chat_member'] = self.old_chat_member.to_dict()
        # override the default output from pydantic by calling `to_dict()` of new_chat_member
        if self.new_chat_member:
            _dict['new_chat_member'] = self.new_chat_member.to_dict()
        # override the default output from pydantic by calling `to_dict()` of invite_link
        if self.invite_link:
            _dict['invite_link'] = self.invite_link.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ChatMemberUpdated from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in ChatMemberUpdated) in the input: " + _key)

        _obj = cls.model_validate({
            "chat": Chat.from_dict(obj["chat"]) if obj.get("chat") is not None else None,
            "from": User.from_dict(obj["from"]) if obj.get("from") is not None else None,
            "date": obj.get("date"),
            "old_chat_member": ChatMember.from_dict(obj["old_chat_member"]) if obj.get("old_chat_member") is not None else None,
            "new_chat_member": ChatMember.from_dict(obj["new_chat_member"]) if obj.get("new_chat_member") is not None else None,
            "invite_link": ChatInviteLink.from_dict(obj["invite_link"]) if obj.get("invite_link") is not None else None,
            "via_join_request": obj.get("via_join_request"),
            "via_chat_folder_invite_link": obj.get("via_chat_folder_invite_link")
        })
        return _obj


