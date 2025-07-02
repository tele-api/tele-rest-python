# coding: utf-8

"""
Telegram Bot API - REST API Client
The Bot API is an HTTP-based interface created for developers keen on building bots for Telegram. To learn how to create and set up a bot, please consult our Introduction to Bots and Bot FAQ.

## Metadata

- **Copyright**: Copyright (c) 2025 Qntx
- **Author**: ΣX <gitctrlx@gmail.com>
- **Version**: 9.0.0
- **Modified**: 2025-07-02T09:16:58.218987030Z[Etc/UTC]
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
from tele_rest.models.order_info import OrderInfo
from typing import Optional, Set
from typing_extensions import Self

class SuccessfulPayment(BaseModel):
    """
    This object contains basic information about a successful payment. Note that if the buyer initiates a chargeback with the relevant payment provider following this transaction, the funds may be debited from your balance. This is outside of Telegram's control.
    """ # noqa: E501
    currency: StrictStr = Field(description="Three-letter ISO 4217 [currency](https://core.telegram.org/bots/payments#supported-currencies) code, or “XTR” for payments in [Telegram Stars](https://t.me/BotNews/90)")
    total_amount: StrictInt = Field(description="Total price in the *smallest units* of the currency (integer, **not** float/double). For example, for a price of `US$ 1.45` pass `amount = 145`. See the *exp* parameter in [currencies.json](https://core.telegram.org/bots/payments/currencies.json), it shows the number of digits past the decimal point for each currency (2 for the majority of currencies).")
    invoice_payload: StrictStr = Field(description="Bot-specified invoice payload")
    subscription_expiration_date: Optional[StrictInt] = Field(default=None, description="*Optional*. Expiration date of the subscription, in Unix time; for recurring payments only")
    is_recurring: Optional[StrictBool] = Field(default=True, description="*Optional*. True, if the payment is a recurring payment for a subscription")
    is_first_recurring: Optional[StrictBool] = Field(default=True, description="*Optional*. True, if the payment is the first payment for a subscription")
    shipping_option_id: Optional[StrictStr] = Field(default=None, description="*Optional*. Identifier of the shipping option chosen by the user")
    order_info: Optional[OrderInfo] = None
    telegram_payment_charge_id: StrictStr = Field(description="Telegram payment identifier")
    provider_payment_charge_id: StrictStr = Field(description="Provider payment identifier")
    __properties: ClassVar[List[str]] = ["currency", "total_amount", "invoice_payload", "subscription_expiration_date", "is_recurring", "is_first_recurring", "shipping_option_id", "order_info", "telegram_payment_charge_id", "provider_payment_charge_id"]

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
        """Create an instance of SuccessfulPayment from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of order_info
        if self.order_info:
            _dict['order_info'] = self.order_info.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SuccessfulPayment from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in SuccessfulPayment) in the input: " + _key)

        _obj = cls.model_validate({
            "currency": obj.get("currency"),
            "total_amount": obj.get("total_amount"),
            "invoice_payload": obj.get("invoice_payload"),
            "subscription_expiration_date": obj.get("subscription_expiration_date"),
            "is_recurring": obj.get("is_recurring") if obj.get("is_recurring") is not None else True,
            "is_first_recurring": obj.get("is_first_recurring") if obj.get("is_first_recurring") is not None else True,
            "shipping_option_id": obj.get("shipping_option_id"),
            "order_info": OrderInfo.from_dict(obj["order_info"]) if obj.get("order_info") is not None else None,
            "telegram_payment_charge_id": obj.get("telegram_payment_charge_id"),
            "provider_payment_charge_id": obj.get("provider_payment_charge_id")
        })
        return _obj


