# coding: utf-8

"""
Telegram Bot API - REST API Client
The Bot API is an HTTP-based interface created for developers keen on building bots for Telegram. To learn how to create and set up a bot, please consult our Introduction to Bots and Bot FAQ.

## Metadata

- **Copyright**: Copyright (c) 2025 Qntx
- **Author**: ΣX <gitctrlx@gmail.com>
- **Version**: 9.2.0
- **Modified**: 2025-09-09T23:46:51.548881723Z[Etc/UTC]
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
from tele_rest.models.chat import Chat
from tele_rest.models.user import User
from typing import Optional, Set
from typing_extensions import Self

class GiveawayWinners(BaseModel):
    """
    This object represents a message about the completion of a giveaway with public winners.
    """ # noqa: E501
    chat: Chat
    giveaway_message_id: StrictInt = Field(description="Identifier of the message with the giveaway in the chat")
    winners_selection_date: StrictInt = Field(description="Point in time (Unix timestamp) when winners of the giveaway were selected")
    winner_count: StrictInt = Field(description="Total number of winners in the giveaway")
    winners: List[User] = Field(description="List of up to 100 winners of the giveaway")
    additional_chat_count: Optional[StrictInt] = Field(default=None, description="*Optional*. The number of other chats the user had to join in order to be eligible for the giveaway")
    prize_star_count: Optional[StrictInt] = Field(default=None, description="*Optional*. The number of Telegram Stars that were split between giveaway winners; for Telegram Star giveaways only")
    premium_subscription_month_count: Optional[StrictInt] = Field(default=None, description="*Optional*. The number of months the Telegram Premium subscription won from the giveaway will be active for; for Telegram Premium giveaways only")
    unclaimed_prize_count: Optional[StrictInt] = Field(default=None, description="*Optional*. Number of undistributed prizes")
    only_new_members: Optional[StrictBool] = Field(default=True, description="*Optional*. *True*, if only users who had joined the chats after the giveaway started were eligible to win")
    was_refunded: Optional[StrictBool] = Field(default=True, description="*Optional*. *True*, if the giveaway was canceled because the payment for it was refunded")
    prize_description: Optional[StrictStr] = Field(default=None, description="*Optional*. Description of additional giveaway prize")
    __properties: ClassVar[List[str]] = ["chat", "giveaway_message_id", "winners_selection_date", "winner_count", "winners", "additional_chat_count", "prize_star_count", "premium_subscription_month_count", "unclaimed_prize_count", "only_new_members", "was_refunded", "prize_description"]

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
        """Create an instance of GiveawayWinners from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in winners (list)
        _items = []
        if self.winners:
            for _item_winners in self.winners:
                if _item_winners:
                    _items.append(_item_winners.to_dict())
            _dict['winners'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GiveawayWinners from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in GiveawayWinners) in the input: " + _key)

        _obj = cls.model_validate({
            "chat": Chat.from_dict(obj["chat"]) if obj.get("chat") is not None else None,
            "giveaway_message_id": obj.get("giveaway_message_id"),
            "winners_selection_date": obj.get("winners_selection_date"),
            "winner_count": obj.get("winner_count"),
            "winners": [User.from_dict(_item) for _item in obj["winners"]] if obj.get("winners") is not None else None,
            "additional_chat_count": obj.get("additional_chat_count"),
            "prize_star_count": obj.get("prize_star_count"),
            "premium_subscription_month_count": obj.get("premium_subscription_month_count"),
            "unclaimed_prize_count": obj.get("unclaimed_prize_count"),
            "only_new_members": obj.get("only_new_members") if obj.get("only_new_members") is not None else True,
            "was_refunded": obj.get("was_refunded") if obj.get("was_refunded") is not None else True,
            "prize_description": obj.get("prize_description")
        })
        return _obj


