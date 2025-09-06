# coding: utf-8

"""
Telegram Bot API - REST API Client
The Bot API is an HTTP-based interface created for developers keen on building bots for Telegram. To learn how to create and set up a bot, please consult our Introduction to Bots and Bot FAQ.

## Metadata

- **Copyright**: Copyright (c) 2025 Qntx
- **Author**: ΣX <gitctrlx@gmail.com>
- **Version**: 9.2.0
- **Modified**: 2025-09-06T05:32:06.285336202Z[Etc/UTC]
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
from tele_rest.models.user import User
from typing import Optional, Set
from typing_extensions import Self

class ChatInviteLink(BaseModel):
    """
    Represents an invite link for a chat.
    """ # noqa: E501
    invite_link: StrictStr = Field(description="The invite link. If the link was created by another chat administrator, then the second part of the link will be replaced with “…”.")
    creator: User
    creates_join_request: StrictBool = Field(description="*True*, if users joining the chat via the link need to be approved by chat administrators")
    is_primary: StrictBool = Field(description="*True*, if the link is primary")
    is_revoked: StrictBool = Field(description="*True*, if the link is revoked")
    name: Optional[StrictStr] = Field(default=None, description="*Optional*. Invite link name")
    expire_date: Optional[StrictInt] = Field(default=None, description="*Optional*. Point in time (Unix timestamp) when the link will expire or has been expired")
    member_limit: Optional[StrictInt] = Field(default=None, description="*Optional*. The maximum number of users that can be members of the chat simultaneously after joining the chat via this invite link; 1-99999")
    pending_join_request_count: Optional[StrictInt] = Field(default=None, description="*Optional*. Number of pending join requests created using this link")
    subscription_period: Optional[StrictInt] = Field(default=None, description="*Optional*. The number of seconds the subscription will be active for before the next payment")
    subscription_price: Optional[StrictInt] = Field(default=None, description="*Optional*. The amount of Telegram Stars a user must pay initially and after each subsequent subscription period to be a member of the chat using the link")
    __properties: ClassVar[List[str]] = ["invite_link", "creator", "creates_join_request", "is_primary", "is_revoked", "name", "expire_date", "member_limit", "pending_join_request_count", "subscription_period", "subscription_price"]

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
        """Create an instance of ChatInviteLink from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of creator
        if self.creator:
            _dict['creator'] = self.creator.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ChatInviteLink from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in ChatInviteLink) in the input: " + _key)

        _obj = cls.model_validate({
            "invite_link": obj.get("invite_link"),
            "creator": User.from_dict(obj["creator"]) if obj.get("creator") is not None else None,
            "creates_join_request": obj.get("creates_join_request"),
            "is_primary": obj.get("is_primary"),
            "is_revoked": obj.get("is_revoked"),
            "name": obj.get("name"),
            "expire_date": obj.get("expire_date"),
            "member_limit": obj.get("member_limit"),
            "pending_join_request_count": obj.get("pending_join_request_count"),
            "subscription_period": obj.get("subscription_period"),
            "subscription_price": obj.get("subscription_price")
        })
        return _obj


