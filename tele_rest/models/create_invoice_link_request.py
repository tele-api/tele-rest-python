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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from tele_rest.models.labeled_price import LabeledPrice
from typing import Optional, Set
from typing_extensions import Self

class CreateInvoiceLinkRequest(BaseModel):
    """
    Request parameters for createInvoiceLink
    """ # noqa: E501
    business_connection_id: Optional[StrictStr] = Field(default=None, description="Unique identifier of the business connection on behalf of which the link will be created. For payments in [Telegram Stars](https://t.me/BotNews/90) only.")
    title: Annotated[str, Field(min_length=1, strict=True, max_length=32)] = Field(description="Product name, 1-32 characters")
    description: Annotated[str, Field(min_length=1, strict=True, max_length=255)] = Field(description="Product description, 1-255 characters")
    payload: StrictStr = Field(description="Bot-defined invoice payload, 1-128 bytes. This will not be displayed to the user, use it for your internal processes.")
    provider_token: Optional[StrictStr] = Field(default=None, description="Payment provider token, obtained via [@BotFather](https://t.me/botfather). Pass an empty string for payments in [Telegram Stars](https://t.me/BotNews/90).")
    currency: StrictStr = Field(description="Three-letter ISO 4217 currency code, see [more on currencies](https://core.telegram.org/bots/payments#supported-currencies). Pass “XTR” for payments in [Telegram Stars](https://t.me/BotNews/90).")
    prices: List[LabeledPrice] = Field(description="Price breakdown, a JSON-serialized list of components (e.g. product price, tax, discount, delivery cost, delivery tax, bonus, etc.). Must contain exactly one item for payments in [Telegram Stars](https://t.me/BotNews/90).")
    subscription_period: Optional[StrictInt] = Field(default=None, description="The number of seconds the subscription will be active for before the next payment. The currency must be set to “XTR” (Telegram Stars) if the parameter is used. Currently, it must always be 2592000 (30 days) if specified. Any number of subscriptions can be active for a given bot at the same time, including multiple concurrent subscriptions from the same user. Subscription price must no exceed 10000 Telegram Stars.")
    max_tip_amount: Optional[StrictInt] = Field(default=0, description="The maximum accepted amount for tips in the *smallest units* of the currency (integer, **not** float/double). For example, for a maximum tip of `US$ 1.45` pass `max_tip_amount = 145`. See the *exp* parameter in [currencies.json](https://core.telegram.org/bots/payments/currencies.json), it shows the number of digits past the decimal point for each currency (2 for the majority of currencies). Defaults to 0. Not supported for payments in [Telegram Stars](https://t.me/BotNews/90).")
    suggested_tip_amounts: Optional[List[StrictInt]] = Field(default=None, description="A JSON-serialized array of suggested amounts of tips in the *smallest units* of the currency (integer, **not** float/double). At most 4 suggested tip amounts can be specified. The suggested tip amounts must be positive, passed in a strictly increased order and must not exceed *max\\_tip\\_amount*.")
    provider_data: Optional[StrictStr] = Field(default=None, description="JSON-serialized data about the invoice, which will be shared with the payment provider. A detailed description of required fields should be provided by the payment provider.")
    photo_url: Optional[StrictStr] = Field(default=None, description="URL of the product photo for the invoice. Can be a photo of the goods or a marketing image for a service.")
    photo_size: Optional[StrictInt] = Field(default=None, description="Photo size in bytes")
    photo_width: Optional[StrictInt] = Field(default=None, description="Photo width")
    photo_height: Optional[StrictInt] = Field(default=None, description="Photo height")
    need_name: Optional[StrictBool] = Field(default=None, description="Pass *True* if you require the user's full name to complete the order. Ignored for payments in [Telegram Stars](https://t.me/BotNews/90).")
    need_phone_number: Optional[StrictBool] = Field(default=None, description="Pass *True* if you require the user's phone number to complete the order. Ignored for payments in [Telegram Stars](https://t.me/BotNews/90).")
    need_email: Optional[StrictBool] = Field(default=None, description="Pass *True* if you require the user's email address to complete the order. Ignored for payments in [Telegram Stars](https://t.me/BotNews/90).")
    need_shipping_address: Optional[StrictBool] = Field(default=None, description="Pass *True* if you require the user's shipping address to complete the order. Ignored for payments in [Telegram Stars](https://t.me/BotNews/90).")
    send_phone_number_to_provider: Optional[StrictBool] = Field(default=None, description="Pass *True* if the user's phone number should be sent to the provider. Ignored for payments in [Telegram Stars](https://t.me/BotNews/90).")
    send_email_to_provider: Optional[StrictBool] = Field(default=None, description="Pass *True* if the user's email address should be sent to the provider. Ignored for payments in [Telegram Stars](https://t.me/BotNews/90).")
    is_flexible: Optional[StrictBool] = Field(default=None, description="Pass *True* if the final price depends on the shipping method. Ignored for payments in [Telegram Stars](https://t.me/BotNews/90).")
    __properties: ClassVar[List[str]] = ["business_connection_id", "title", "description", "payload", "provider_token", "currency", "prices", "subscription_period", "max_tip_amount", "suggested_tip_amounts", "provider_data", "photo_url", "photo_size", "photo_width", "photo_height", "need_name", "need_phone_number", "need_email", "need_shipping_address", "send_phone_number_to_provider", "send_email_to_provider", "is_flexible"]

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
        """Create an instance of CreateInvoiceLinkRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in prices (list)
        _items = []
        if self.prices:
            for _item_prices in self.prices:
                if _item_prices:
                    _items.append(_item_prices.to_dict())
            _dict['prices'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CreateInvoiceLinkRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in CreateInvoiceLinkRequest) in the input: " + _key)

        _obj = cls.model_validate({
            "business_connection_id": obj.get("business_connection_id"),
            "title": obj.get("title"),
            "description": obj.get("description"),
            "payload": obj.get("payload"),
            "provider_token": obj.get("provider_token"),
            "currency": obj.get("currency"),
            "prices": [LabeledPrice.from_dict(_item) for _item in obj["prices"]] if obj.get("prices") is not None else None,
            "subscription_period": obj.get("subscription_period"),
            "max_tip_amount": obj.get("max_tip_amount") if obj.get("max_tip_amount") is not None else 0,
            "suggested_tip_amounts": obj.get("suggested_tip_amounts"),
            "provider_data": obj.get("provider_data"),
            "photo_url": obj.get("photo_url"),
            "photo_size": obj.get("photo_size"),
            "photo_width": obj.get("photo_width"),
            "photo_height": obj.get("photo_height"),
            "need_name": obj.get("need_name"),
            "need_phone_number": obj.get("need_phone_number"),
            "need_email": obj.get("need_email"),
            "need_shipping_address": obj.get("need_shipping_address"),
            "send_phone_number_to_provider": obj.get("send_phone_number_to_provider"),
            "send_email_to_provider": obj.get("send_email_to_provider"),
            "is_flexible": obj.get("is_flexible")
        })
        return _obj


