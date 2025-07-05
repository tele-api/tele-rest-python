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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from tele_rest.models.affiliate_info import AffiliateInfo
from tele_rest.models.gift import Gift
from tele_rest.models.paid_media import PaidMedia
from tele_rest.models.user import User
from typing import Optional, Set
from typing_extensions import Self

class TransactionPartnerUser(BaseModel):
    """
    Describes a transaction with a user.
    """ # noqa: E501
    type: StrictStr = Field(description="Type of the transaction partner, always “user”")
    transaction_type: StrictStr = Field(description="Type of the transaction, currently one of “invoice\\_payment” for payments via invoices, “paid\\_media\\_payment” for payments for paid media, “gift\\_purchase” for gifts sent by the bot, “premium\\_purchase” for Telegram Premium subscriptions gifted by the bot, “business\\_account\\_transfer” for direct transfers from managed business accounts")
    user: User
    affiliate: Optional[AffiliateInfo] = None
    invoice_payload: Optional[StrictStr] = Field(default=None, description="*Optional*. Bot-specified invoice payload. Can be available only for “invoice\\_payment” transactions.")
    subscription_period: Optional[StrictInt] = Field(default=None, description="*Optional*. The duration of the paid subscription. Can be available only for “invoice\\_payment” transactions.")
    paid_media: Optional[List[PaidMedia]] = Field(default=None, description="*Optional*. Information about the paid media bought by the user; for “paid\\_media\\_payment” transactions only")
    paid_media_payload: Optional[StrictStr] = Field(default=None, description="*Optional*. Bot-specified paid media payload. Can be available only for “paid\\_media\\_payment” transactions.")
    gift: Optional[Gift] = None
    premium_subscription_duration: Optional[StrictInt] = Field(default=None, description="*Optional*. Number of months the gifted Telegram Premium subscription will be active for; for “premium\\_purchase” transactions only")
    __properties: ClassVar[List[str]] = ["type", "transaction_type", "user", "affiliate", "invoice_payload", "subscription_period", "paid_media", "paid_media_payload", "gift", "premium_subscription_duration"]

    @field_validator('transaction_type')
    def transaction_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['invoice_payment', 'paid_media_payment', 'gift_purchase', 'premium_purchase', 'business_account_transfer']):
            raise ValueError("must be one of enum values ('invoice_payment', 'paid_media_payment', 'gift_purchase', 'premium_purchase', 'business_account_transfer')")
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
        """Create an instance of TransactionPartnerUser from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of affiliate
        if self.affiliate:
            _dict['affiliate'] = self.affiliate.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in paid_media (list)
        _items = []
        if self.paid_media:
            for _item_paid_media in self.paid_media:
                if _item_paid_media:
                    _items.append(_item_paid_media.to_dict())
            _dict['paid_media'] = _items
        # override the default output from pydantic by calling `to_dict()` of gift
        if self.gift:
            _dict['gift'] = self.gift.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TransactionPartnerUser from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in TransactionPartnerUser) in the input: " + _key)

        _obj = cls.model_validate({
            "type": obj.get("type") if obj.get("type") is not None else 'user',
            "transaction_type": obj.get("transaction_type"),
            "user": User.from_dict(obj["user"]) if obj.get("user") is not None else None,
            "affiliate": AffiliateInfo.from_dict(obj["affiliate"]) if obj.get("affiliate") is not None else None,
            "invoice_payload": obj.get("invoice_payload"),
            "subscription_period": obj.get("subscription_period"),
            "paid_media": [PaidMedia.from_dict(_item) for _item in obj["paid_media"]] if obj.get("paid_media") is not None else None,
            "paid_media_payload": obj.get("paid_media_payload"),
            "gift": Gift.from_dict(obj["gift"]) if obj.get("gift") is not None else None,
            "premium_subscription_duration": obj.get("premium_subscription_duration")
        })
        return _obj


