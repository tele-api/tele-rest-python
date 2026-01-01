# coding: utf-8

"""
Telegram Bot API - REST API Client
The Bot API is an HTTP-based interface created for developers keen on building bots for Telegram. To learn how to create and set up a bot, please consult our Introduction to Bots and Bot FAQ.

## Metadata

- **Copyright**: Copyright (c) 2026 Qntx
- **Author**: ΣX <gitctrlx@gmail.com>
- **Version**: 9.3.0
- **Modified**: 2026-01-01T02:06:09.762570119Z[Etc/UTC]
- **Generator Version**: 7.18.0

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

class ChatPermissions(BaseModel):
    """
    Describes actions that a non-administrator user is allowed to take in a chat.
    """ # noqa: E501
    can_send_messages: Optional[StrictBool] = Field(default=None, description="*Optional*. *True*, if the user is allowed to send text messages, contacts, giveaways, giveaway winners, invoices, locations and venues")
    can_send_audios: Optional[StrictBool] = Field(default=None, description="*Optional*. *True*, if the user is allowed to send audios")
    can_send_documents: Optional[StrictBool] = Field(default=None, description="*Optional*. *True*, if the user is allowed to send documents")
    can_send_photos: Optional[StrictBool] = Field(default=None, description="*Optional*. *True*, if the user is allowed to send photos")
    can_send_videos: Optional[StrictBool] = Field(default=None, description="*Optional*. *True*, if the user is allowed to send videos")
    can_send_video_notes: Optional[StrictBool] = Field(default=None, description="*Optional*. *True*, if the user is allowed to send video notes")
    can_send_voice_notes: Optional[StrictBool] = Field(default=None, description="*Optional*. *True*, if the user is allowed to send voice notes")
    can_send_polls: Optional[StrictBool] = Field(default=None, description="*Optional*. *True*, if the user is allowed to send polls and checklists")
    can_send_other_messages: Optional[StrictBool] = Field(default=None, description="*Optional*. *True*, if the user is allowed to send animations, games, stickers and use inline bots")
    can_add_web_page_previews: Optional[StrictBool] = Field(default=None, description="*Optional*. *True*, if the user is allowed to add web page previews to their messages")
    can_change_info: Optional[StrictBool] = Field(default=None, description="*Optional*. *True*, if the user is allowed to change the chat title, photo and other settings. Ignored in public supergroups")
    can_invite_users: Optional[StrictBool] = Field(default=None, description="*Optional*. *True*, if the user is allowed to invite new users to the chat")
    can_pin_messages: Optional[StrictBool] = Field(default=None, description="*Optional*. *True*, if the user is allowed to pin messages. Ignored in public supergroups")
    can_manage_topics: Optional[StrictBool] = Field(default=None, description="*Optional*. *True*, if the user is allowed to create forum topics. If omitted defaults to the value of can\\_pin\\_messages")
    __properties: ClassVar[List[str]] = ["can_send_messages", "can_send_audios", "can_send_documents", "can_send_photos", "can_send_videos", "can_send_video_notes", "can_send_voice_notes", "can_send_polls", "can_send_other_messages", "can_add_web_page_previews", "can_change_info", "can_invite_users", "can_pin_messages", "can_manage_topics"]

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
        """Create an instance of ChatPermissions from a JSON string"""
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
        """Create an instance of ChatPermissions from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in ChatPermissions) in the input: " + _key)

        _obj = cls.model_validate({
            "can_send_messages": obj.get("can_send_messages"),
            "can_send_audios": obj.get("can_send_audios"),
            "can_send_documents": obj.get("can_send_documents"),
            "can_send_photos": obj.get("can_send_photos"),
            "can_send_videos": obj.get("can_send_videos"),
            "can_send_video_notes": obj.get("can_send_video_notes"),
            "can_send_voice_notes": obj.get("can_send_voice_notes"),
            "can_send_polls": obj.get("can_send_polls"),
            "can_send_other_messages": obj.get("can_send_other_messages"),
            "can_add_web_page_previews": obj.get("can_add_web_page_previews"),
            "can_change_info": obj.get("can_change_info"),
            "can_invite_users": obj.get("can_invite_users"),
            "can_pin_messages": obj.get("can_pin_messages"),
            "can_manage_topics": obj.get("can_manage_topics")
        })
        return _obj


