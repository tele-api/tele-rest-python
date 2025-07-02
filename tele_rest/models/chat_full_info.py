# coding: utf-8

"""
Telegram Bot API - REST API Client
The Bot API is an HTTP-based interface created for developers keen on building bots for Telegram. To learn how to create and set up a bot, please consult our Introduction to Bots and Bot FAQ.

## Metadata

- **Copyright**: Copyright (c) 2025 Qntx
- **Author**: ΣX <gitctrlx@gmail.com>
- **Version**: 9.0.0
- **Modified**: 2025-07-02T07:03:17.088738557Z[Etc/UTC]
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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from tele_rest.models.accepted_gift_types import AcceptedGiftTypes
from tele_rest.models.birthdate import Birthdate
from tele_rest.models.business_intro import BusinessIntro
from tele_rest.models.business_location import BusinessLocation
from tele_rest.models.business_opening_hours import BusinessOpeningHours
from tele_rest.models.chat import Chat
from tele_rest.models.chat_location import ChatLocation
from tele_rest.models.chat_permissions import ChatPermissions
from tele_rest.models.chat_photo import ChatPhoto
from tele_rest.models.message import Message
from tele_rest.models.reaction_type import ReactionType
from typing import Optional, Set
from typing_extensions import Self

class ChatFullInfo(BaseModel):
    """
    This object contains full information about a chat.
    """ # noqa: E501
    id: StrictInt = Field(description="Unique identifier for this chat. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this identifier.")
    type: StrictStr = Field(description="Type of the chat, can be either “private”, “group”, “supergroup” or “channel”")
    title: Optional[StrictStr] = Field(default=None, description="*Optional*. Title, for supergroups, channels and group chats")
    username: Optional[StrictStr] = Field(default=None, description="*Optional*. Username, for private chats, supergroups and channels if available")
    first_name: Optional[StrictStr] = Field(default=None, description="*Optional*. First name of the other party in a private chat")
    last_name: Optional[StrictStr] = Field(default=None, description="*Optional*. Last name of the other party in a private chat")
    is_forum: Optional[StrictBool] = Field(default=True, description="*Optional*. *True*, if the supergroup chat is a forum (has [topics](https://telegram.org/blog/topics-in-groups-collectible-usernames#topics-in-groups) enabled)")
    accent_color_id: StrictInt = Field(description="Identifier of the accent color for the chat name and backgrounds of the chat photo, reply header, and link preview. See [accent colors](https://core.telegram.org/bots/api/#accent-colors) for more details.")
    max_reaction_count: StrictInt = Field(description="The maximum number of reactions that can be set on a message in the chat")
    photo: Optional[ChatPhoto] = None
    active_usernames: Optional[List[StrictStr]] = Field(default=None, description="*Optional*. If non-empty, the list of all [active chat usernames](https://telegram.org/blog/topics-in-groups-collectible-usernames#collectible-usernames); for private chats, supergroups and channels")
    birthdate: Optional[Birthdate] = None
    business_intro: Optional[BusinessIntro] = None
    business_location: Optional[BusinessLocation] = None
    business_opening_hours: Optional[BusinessOpeningHours] = None
    personal_chat: Optional[Chat] = None
    available_reactions: Optional[List[ReactionType]] = Field(default=None, description="*Optional*. List of available reactions allowed in the chat. If omitted, then all [emoji reactions](https://core.telegram.org/bots/api/#reactiontypeemoji) are allowed.")
    background_custom_emoji_id: Optional[StrictStr] = Field(default=None, description="*Optional*. Custom emoji identifier of the emoji chosen by the chat for the reply header and link preview background")
    profile_accent_color_id: Optional[StrictInt] = Field(default=None, description="*Optional*. Identifier of the accent color for the chat's profile background. See [profile accent colors](https://core.telegram.org/bots/api/#profile-accent-colors) for more details.")
    profile_background_custom_emoji_id: Optional[StrictStr] = Field(default=None, description="*Optional*. Custom emoji identifier of the emoji chosen by the chat for its profile background")
    emoji_status_custom_emoji_id: Optional[StrictStr] = Field(default=None, description="*Optional*. Custom emoji identifier of the emoji status of the chat or the other party in a private chat")
    emoji_status_expiration_date: Optional[StrictInt] = Field(default=None, description="*Optional*. Expiration date of the emoji status of the chat or the other party in a private chat, in Unix time, if any")
    bio: Optional[StrictStr] = Field(default=None, description="*Optional*. Bio of the other party in a private chat")
    has_private_forwards: Optional[StrictBool] = Field(default=True, description="*Optional*. *True*, if privacy settings of the other party in the private chat allows to use `tg://user?id=<user_id>` links only in chats with the user")
    has_restricted_voice_and_video_messages: Optional[StrictBool] = Field(default=True, description="*Optional*. *True*, if the privacy settings of the other party restrict sending voice and video note messages in the private chat")
    join_to_send_messages: Optional[StrictBool] = Field(default=True, description="*Optional*. *True*, if users need to join the supergroup before they can send messages")
    join_by_request: Optional[StrictBool] = Field(default=True, description="*Optional*. *True*, if all users directly joining the supergroup without using an invite link need to be approved by supergroup administrators")
    description: Optional[StrictStr] = Field(default=None, description="*Optional*. Description, for groups, supergroups and channel chats")
    invite_link: Optional[StrictStr] = Field(default=None, description="*Optional*. Primary invite link, for groups, supergroups and channel chats")
    pinned_message: Optional[Message] = None
    permissions: Optional[ChatPermissions] = None
    accepted_gift_types: AcceptedGiftTypes
    can_send_paid_media: Optional[StrictBool] = Field(default=True, description="*Optional*. *True*, if paid media messages can be sent or forwarded to the channel chat. The field is available only for channel chats.")
    slow_mode_delay: Optional[StrictInt] = Field(default=None, description="*Optional*. For supergroups, the minimum allowed delay between consecutive messages sent by each unprivileged user; in seconds")
    unrestrict_boost_count: Optional[StrictInt] = Field(default=None, description="*Optional*. For supergroups, the minimum number of boosts that a non-administrator user needs to add in order to ignore slow mode and chat permissions")
    message_auto_delete_time: Optional[StrictInt] = Field(default=None, description="*Optional*. The time after which all messages sent to the chat will be automatically deleted; in seconds")
    has_aggressive_anti_spam_enabled: Optional[StrictBool] = Field(default=True, description="*Optional*. *True*, if aggressive anti-spam checks are enabled in the supergroup. The field is only available to chat administrators.")
    has_hidden_members: Optional[StrictBool] = Field(default=True, description="*Optional*. *True*, if non-administrators can only get the list of bots and administrators in the chat")
    has_protected_content: Optional[StrictBool] = Field(default=True, description="*Optional*. *True*, if messages from the chat can't be forwarded to other chats")
    has_visible_history: Optional[StrictBool] = Field(default=True, description="*Optional*. *True*, if new chat members will have access to old messages; available only to chat administrators")
    sticker_set_name: Optional[StrictStr] = Field(default=None, description="*Optional*. For supergroups, name of the group sticker set")
    can_set_sticker_set: Optional[StrictBool] = Field(default=True, description="*Optional*. *True*, if the bot can change the group sticker set")
    custom_emoji_sticker_set_name: Optional[StrictStr] = Field(default=None, description="*Optional*. For supergroups, the name of the group's custom emoji sticker set. Custom emoji from this set can be used by all users and bots in the group.")
    linked_chat_id: Optional[StrictInt] = Field(default=None, description="*Optional*. Unique identifier for the linked chat, i.e. the discussion group identifier for a channel and vice versa; for supergroups and channel chats. This identifier may be greater than 32 bits and some programming languages may have difficulty/silent defects in interpreting it. But it is smaller than 52 bits, so a signed 64 bit integer or double-precision float type are safe for storing this identifier.")
    location: Optional[ChatLocation] = None
    __properties: ClassVar[List[str]] = ["id", "type", "title", "username", "first_name", "last_name", "is_forum", "accent_color_id", "max_reaction_count", "photo", "active_usernames", "birthdate", "business_intro", "business_location", "business_opening_hours", "personal_chat", "available_reactions", "background_custom_emoji_id", "profile_accent_color_id", "profile_background_custom_emoji_id", "emoji_status_custom_emoji_id", "emoji_status_expiration_date", "bio", "has_private_forwards", "has_restricted_voice_and_video_messages", "join_to_send_messages", "join_by_request", "description", "invite_link", "pinned_message", "permissions", "accepted_gift_types", "can_send_paid_media", "slow_mode_delay", "unrestrict_boost_count", "message_auto_delete_time", "has_aggressive_anti_spam_enabled", "has_hidden_members", "has_protected_content", "has_visible_history", "sticker_set_name", "can_set_sticker_set", "custom_emoji_sticker_set_name", "linked_chat_id", "location"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['private', 'group', 'supergroup', 'channel']):
            raise ValueError("must be one of enum values ('private', 'group', 'supergroup', 'channel')")
        return value

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
        """Create an instance of ChatFullInfo from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of photo
        if self.photo:
            _dict['photo'] = self.photo.to_dict()
        # override the default output from pydantic by calling `to_dict()` of birthdate
        if self.birthdate:
            _dict['birthdate'] = self.birthdate.to_dict()
        # override the default output from pydantic by calling `to_dict()` of business_intro
        if self.business_intro:
            _dict['business_intro'] = self.business_intro.to_dict()
        # override the default output from pydantic by calling `to_dict()` of business_location
        if self.business_location:
            _dict['business_location'] = self.business_location.to_dict()
        # override the default output from pydantic by calling `to_dict()` of business_opening_hours
        if self.business_opening_hours:
            _dict['business_opening_hours'] = self.business_opening_hours.to_dict()
        # override the default output from pydantic by calling `to_dict()` of personal_chat
        if self.personal_chat:
            _dict['personal_chat'] = self.personal_chat.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in available_reactions (list)
        _items = []
        if self.available_reactions:
            for _item_available_reactions in self.available_reactions:
                if _item_available_reactions:
                    _items.append(_item_available_reactions.to_dict())
            _dict['available_reactions'] = _items
        # override the default output from pydantic by calling `to_dict()` of pinned_message
        if self.pinned_message:
            _dict['pinned_message'] = self.pinned_message.to_dict()
        # override the default output from pydantic by calling `to_dict()` of permissions
        if self.permissions:
            _dict['permissions'] = self.permissions.to_dict()
        # override the default output from pydantic by calling `to_dict()` of accepted_gift_types
        if self.accepted_gift_types:
            _dict['accepted_gift_types'] = self.accepted_gift_types.to_dict()
        # override the default output from pydantic by calling `to_dict()` of location
        if self.location:
            _dict['location'] = self.location.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ChatFullInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in ChatFullInfo) in the input: " + _key)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "type": obj.get("type"),
            "title": obj.get("title"),
            "username": obj.get("username"),
            "first_name": obj.get("first_name"),
            "last_name": obj.get("last_name"),
            "is_forum": obj.get("is_forum") if obj.get("is_forum") is not None else True,
            "accent_color_id": obj.get("accent_color_id"),
            "max_reaction_count": obj.get("max_reaction_count"),
            "photo": ChatPhoto.from_dict(obj["photo"]) if obj.get("photo") is not None else None,
            "active_usernames": obj.get("active_usernames"),
            "birthdate": Birthdate.from_dict(obj["birthdate"]) if obj.get("birthdate") is not None else None,
            "business_intro": BusinessIntro.from_dict(obj["business_intro"]) if obj.get("business_intro") is not None else None,
            "business_location": BusinessLocation.from_dict(obj["business_location"]) if obj.get("business_location") is not None else None,
            "business_opening_hours": BusinessOpeningHours.from_dict(obj["business_opening_hours"]) if obj.get("business_opening_hours") is not None else None,
            "personal_chat": Chat.from_dict(obj["personal_chat"]) if obj.get("personal_chat") is not None else None,
            "available_reactions": [ReactionType.from_dict(_item) for _item in obj["available_reactions"]] if obj.get("available_reactions") is not None else None,
            "background_custom_emoji_id": obj.get("background_custom_emoji_id"),
            "profile_accent_color_id": obj.get("profile_accent_color_id"),
            "profile_background_custom_emoji_id": obj.get("profile_background_custom_emoji_id"),
            "emoji_status_custom_emoji_id": obj.get("emoji_status_custom_emoji_id"),
            "emoji_status_expiration_date": obj.get("emoji_status_expiration_date"),
            "bio": obj.get("bio"),
            "has_private_forwards": obj.get("has_private_forwards") if obj.get("has_private_forwards") is not None else True,
            "has_restricted_voice_and_video_messages": obj.get("has_restricted_voice_and_video_messages") if obj.get("has_restricted_voice_and_video_messages") is not None else True,
            "join_to_send_messages": obj.get("join_to_send_messages") if obj.get("join_to_send_messages") is not None else True,
            "join_by_request": obj.get("join_by_request") if obj.get("join_by_request") is not None else True,
            "description": obj.get("description"),
            "invite_link": obj.get("invite_link"),
            "pinned_message": Message.from_dict(obj["pinned_message"]) if obj.get("pinned_message") is not None else None,
            "permissions": ChatPermissions.from_dict(obj["permissions"]) if obj.get("permissions") is not None else None,
            "accepted_gift_types": AcceptedGiftTypes.from_dict(obj["accepted_gift_types"]) if obj.get("accepted_gift_types") is not None else None,
            "can_send_paid_media": obj.get("can_send_paid_media") if obj.get("can_send_paid_media") is not None else True,
            "slow_mode_delay": obj.get("slow_mode_delay"),
            "unrestrict_boost_count": obj.get("unrestrict_boost_count"),
            "message_auto_delete_time": obj.get("message_auto_delete_time"),
            "has_aggressive_anti_spam_enabled": obj.get("has_aggressive_anti_spam_enabled") if obj.get("has_aggressive_anti_spam_enabled") is not None else True,
            "has_hidden_members": obj.get("has_hidden_members") if obj.get("has_hidden_members") is not None else True,
            "has_protected_content": obj.get("has_protected_content") if obj.get("has_protected_content") is not None else True,
            "has_visible_history": obj.get("has_visible_history") if obj.get("has_visible_history") is not None else True,
            "sticker_set_name": obj.get("sticker_set_name"),
            "can_set_sticker_set": obj.get("can_set_sticker_set") if obj.get("can_set_sticker_set") is not None else True,
            "custom_emoji_sticker_set_name": obj.get("custom_emoji_sticker_set_name"),
            "linked_chat_id": obj.get("linked_chat_id"),
            "location": ChatLocation.from_dict(obj["location"]) if obj.get("location") is not None else None
        })
        return _obj


