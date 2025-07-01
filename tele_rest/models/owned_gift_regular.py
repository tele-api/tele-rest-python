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
from tele_rest.models.gift import Gift
from tele_rest.models.message_entity import MessageEntity
from tele_rest.models.user import User
from typing import Optional, Set
from typing_extensions import Self

class OwnedGiftRegular(BaseModel):
    """
    Describes a regular gift owned by a user or a chat.
    """ # noqa: E501
    type: StrictStr = Field(description="Type of the gift, always “regular”")
    gift: Gift
    owned_gift_id: Optional[StrictStr] = Field(default=None, description="*Optional*. Unique identifier of the gift for the bot; for gifts received on behalf of business accounts only")
    sender_user: Optional[User] = None
    send_date: StrictInt = Field(description="Date the gift was sent in Unix time")
    text: Optional[StrictStr] = Field(default=None, description="*Optional*. Text of the message that was added to the gift")
    entities: Optional[List[MessageEntity]] = Field(default=None, description="*Optional*. Special entities that appear in the text")
    is_private: Optional[StrictBool] = Field(default=True, description="*Optional*. True, if the sender and gift text are shown only to the gift receiver; otherwise, everyone will be able to see them")
    is_saved: Optional[StrictBool] = Field(default=True, description="*Optional*. True, if the gift is displayed on the account's profile page; for gifts received on behalf of business accounts only")
    can_be_upgraded: Optional[StrictBool] = Field(default=True, description="*Optional*. True, if the gift can be upgraded to a unique gift; for gifts received on behalf of business accounts only")
    was_refunded: Optional[StrictBool] = Field(default=True, description="*Optional*. True, if the gift was refunded and isn't available anymore")
    convert_star_count: Optional[StrictInt] = Field(default=None, description="*Optional*. Number of Telegram Stars that can be claimed by the receiver instead of the gift; omitted if the gift cannot be converted to Telegram Stars")
    prepaid_upgrade_star_count: Optional[StrictInt] = Field(default=None, description="*Optional*. Number of Telegram Stars that were paid by the sender for the ability to upgrade the gift")
    __properties: ClassVar[List[str]] = ["type", "gift", "owned_gift_id", "sender_user", "send_date", "text", "entities", "is_private", "is_saved", "can_be_upgraded", "was_refunded", "convert_star_count", "prepaid_upgrade_star_count"]

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
        """Create an instance of OwnedGiftRegular from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of gift
        if self.gift:
            _dict['gift'] = self.gift.to_dict()
        # override the default output from pydantic by calling `to_dict()` of sender_user
        if self.sender_user:
            _dict['sender_user'] = self.sender_user.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in entities (list)
        _items = []
        if self.entities:
            for _item_entities in self.entities:
                if _item_entities:
                    _items.append(_item_entities.to_dict())
            _dict['entities'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OwnedGiftRegular from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in OwnedGiftRegular) in the input: " + _key)

        _obj = cls.model_validate({
            "type": obj.get("type") if obj.get("type") is not None else 'regular',
            "gift": Gift.from_dict(obj["gift"]) if obj.get("gift") is not None else None,
            "owned_gift_id": obj.get("owned_gift_id"),
            "sender_user": User.from_dict(obj["sender_user"]) if obj.get("sender_user") is not None else None,
            "send_date": obj.get("send_date"),
            "text": obj.get("text"),
            "entities": [MessageEntity.from_dict(_item) for _item in obj["entities"]] if obj.get("entities") is not None else None,
            "is_private": obj.get("is_private") if obj.get("is_private") is not None else True,
            "is_saved": obj.get("is_saved") if obj.get("is_saved") is not None else True,
            "can_be_upgraded": obj.get("can_be_upgraded") if obj.get("can_be_upgraded") is not None else True,
            "was_refunded": obj.get("was_refunded") if obj.get("was_refunded") is not None else True,
            "convert_star_count": obj.get("convert_star_count"),
            "prepaid_upgrade_star_count": obj.get("prepaid_upgrade_star_count")
        })
        return _obj


