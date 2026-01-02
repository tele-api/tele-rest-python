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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from tele_rest.models.chat import Chat
from typing import Optional, Set
from typing_extensions import Self

class Giveaway(BaseModel):
    """
    This object represents a message about a scheduled giveaway.
    """ # noqa: E501
    chats: List[Chat] = Field(description="The list of chats which the user must join to participate in the giveaway")
    winners_selection_date: StrictInt = Field(description="Point in time (Unix timestamp) when winners of the giveaway will be selected")
    winner_count: StrictInt = Field(description="The number of users which are supposed to be selected as winners of the giveaway")
    only_new_members: Optional[StrictBool] = Field(default=True, description="*Optional*. *True*, if only users who join the chats after the giveaway started should be eligible to win")
    has_public_winners: Optional[StrictBool] = Field(default=True, description="*Optional*. *True*, if the list of giveaway winners will be visible to everyone")
    prize_description: Optional[StrictStr] = Field(default=None, description="*Optional*. Description of additional giveaway prize")
    country_codes: Optional[List[StrictStr]] = Field(default=None, description="*Optional*. A list of two-letter [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes indicating the countries from which eligible users for the giveaway must come. If empty, then all users can participate in the giveaway. Users with a phone number that was bought on Fragment can always participate in giveaways.")
    prize_star_count: Optional[StrictInt] = Field(default=None, description="*Optional*. The number of Telegram Stars to be split between giveaway winners; for Telegram Star giveaways only")
    premium_subscription_month_count: Optional[StrictInt] = Field(default=None, description="*Optional*. The number of months the Telegram Premium subscription won from the giveaway will be active for; for Telegram Premium giveaways only")
    __properties: ClassVar[List[str]] = ["chats", "winners_selection_date", "winner_count", "only_new_members", "has_public_winners", "prize_description", "country_codes", "prize_star_count", "premium_subscription_month_count"]

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
        """Create an instance of Giveaway from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in chats (list)
        _items = []
        if self.chats:
            for _item_chats in self.chats:
                if _item_chats:
                    _items.append(_item_chats.to_dict())
            _dict['chats'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Giveaway from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in Giveaway) in the input: " + _key)

        _obj = cls.model_validate({
            "chats": [Chat.from_dict(_item) for _item in obj["chats"]] if obj.get("chats") is not None else None,
            "winners_selection_date": obj.get("winners_selection_date"),
            "winner_count": obj.get("winner_count"),
            "only_new_members": obj.get("only_new_members") if obj.get("only_new_members") is not None else True,
            "has_public_winners": obj.get("has_public_winners") if obj.get("has_public_winners") is not None else True,
            "prize_description": obj.get("prize_description"),
            "country_codes": obj.get("country_codes"),
            "prize_star_count": obj.get("prize_star_count"),
            "premium_subscription_month_count": obj.get("premium_subscription_month_count")
        })
        return _obj


