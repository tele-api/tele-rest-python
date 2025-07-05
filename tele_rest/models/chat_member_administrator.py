# coding: utf-8

"""
Telegram Bot API - REST API Client
The Bot API is an HTTP-based interface created for developers keen on building bots for Telegram. To learn how to create and set up a bot, please consult our Introduction to Bots and Bot FAQ.

## Metadata

- **Copyright**: Copyright (c) 2025 Qntx
- **Author**: ΣX <gitctrlx@gmail.com>
- **Version**: 9.1.0
- **Modified**: 2025-07-05T02:41:43.458230827Z[Etc/UTC]
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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from tele_rest.models.user import User
from typing import Optional, Set
from typing_extensions import Self

class ChatMemberAdministrator(BaseModel):
    """
    Represents a [chat member](https://core.telegram.org/bots/api/#chatmember) that has some additional privileges.
    """ # noqa: E501
    status: StrictStr = Field(description="The member's status in the chat, always “administrator”")
    user: User
    can_be_edited: StrictBool = Field(description="*True*, if the bot is allowed to edit administrator privileges of that user")
    is_anonymous: StrictBool = Field(description="*True*, if the user's presence in the chat is hidden")
    can_manage_chat: StrictBool = Field(description="*True*, if the administrator can access the chat event log, get boost list, see hidden supergroup and channel members, report spam messages, ignore slow mode, and send messages to the chat without paying Telegram Stars. Implied by any other administrator privilege.")
    can_delete_messages: StrictBool = Field(description="*True*, if the administrator can delete messages of other users")
    can_manage_video_chats: StrictBool = Field(description="*True*, if the administrator can manage video chats")
    can_restrict_members: StrictBool = Field(description="*True*, if the administrator can restrict, ban or unban chat members, or access supergroup statistics")
    can_promote_members: StrictBool = Field(description="*True*, if the administrator can add new administrators with a subset of their own privileges or demote administrators that they have promoted, directly or indirectly (promoted by administrators that were appointed by the user)")
    can_change_info: StrictBool = Field(description="*True*, if the user is allowed to change the chat title, photo and other settings")
    can_invite_users: StrictBool = Field(description="*True*, if the user is allowed to invite new users to the chat")
    can_post_stories: StrictBool = Field(description="*True*, if the administrator can post stories to the chat")
    can_edit_stories: StrictBool = Field(description="*True*, if the administrator can edit stories posted by other users, post stories to the chat page, pin chat stories, and access the chat's story archive")
    can_delete_stories: StrictBool = Field(description="*True*, if the administrator can delete stories posted by other users")
    can_post_messages: Optional[StrictBool] = Field(default=None, description="*Optional*. *True*, if the administrator can post messages in the channel, approve suggested posts, or access channel statistics; for channels only")
    can_edit_messages: Optional[StrictBool] = Field(default=None, description="*Optional*. *True*, if the administrator can edit messages of other users and can pin messages; for channels only")
    can_pin_messages: Optional[StrictBool] = Field(default=None, description="*Optional*. *True*, if the user is allowed to pin messages; for groups and supergroups only")
    can_manage_topics: Optional[StrictBool] = Field(default=None, description="*Optional*. *True*, if the user is allowed to create, rename, close, and reopen forum topics; for supergroups only")
    custom_title: Optional[StrictStr] = Field(default=None, description="*Optional*. Custom title for this user")
    __properties: ClassVar[List[str]] = ["status", "user", "can_be_edited", "is_anonymous", "can_manage_chat", "can_delete_messages", "can_manage_video_chats", "can_restrict_members", "can_promote_members", "can_change_info", "can_invite_users", "can_post_stories", "can_edit_stories", "can_delete_stories", "can_post_messages", "can_edit_messages", "can_pin_messages", "can_manage_topics", "custom_title"]

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
        """Create an instance of ChatMemberAdministrator from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of user
        if self.user:
            _dict['user'] = self.user.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ChatMemberAdministrator from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in ChatMemberAdministrator) in the input: " + _key)

        _obj = cls.model_validate({
            "status": obj.get("status") if obj.get("status") is not None else 'administrator',
            "user": User.from_dict(obj["user"]) if obj.get("user") is not None else None,
            "can_be_edited": obj.get("can_be_edited"),
            "is_anonymous": obj.get("is_anonymous"),
            "can_manage_chat": obj.get("can_manage_chat"),
            "can_delete_messages": obj.get("can_delete_messages"),
            "can_manage_video_chats": obj.get("can_manage_video_chats"),
            "can_restrict_members": obj.get("can_restrict_members"),
            "can_promote_members": obj.get("can_promote_members"),
            "can_change_info": obj.get("can_change_info"),
            "can_invite_users": obj.get("can_invite_users"),
            "can_post_stories": obj.get("can_post_stories"),
            "can_edit_stories": obj.get("can_edit_stories"),
            "can_delete_stories": obj.get("can_delete_stories"),
            "can_post_messages": obj.get("can_post_messages"),
            "can_edit_messages": obj.get("can_edit_messages"),
            "can_pin_messages": obj.get("can_pin_messages"),
            "can_manage_topics": obj.get("can_manage_topics"),
            "custom_title": obj.get("custom_title")
        })
        return _obj


