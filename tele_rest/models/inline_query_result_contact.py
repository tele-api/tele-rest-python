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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from tele_rest.models.inline_keyboard_markup import InlineKeyboardMarkup
from tele_rest.models.input_message_content import InputMessageContent
from typing import Optional, Set
from typing_extensions import Self

class InlineQueryResultContact(BaseModel):
    """
    Represents a contact with a phone number. By default, this contact will be sent by the user. Alternatively, you can use *input\\_message\\_content* to send a message with the specified content instead of the contact.
    """ # noqa: E501
    type: StrictStr = Field(description="Type of the result, must be *contact*")
    id: StrictStr = Field(description="Unique identifier for this result, 1-64 Bytes")
    phone_number: StrictStr = Field(description="Contact's phone number")
    first_name: StrictStr = Field(description="Contact's first name")
    last_name: Optional[StrictStr] = Field(default=None, description="*Optional*. Contact's last name")
    vcard: Optional[StrictStr] = Field(default=None, description="*Optional*. Additional data about the contact in the form of a [vCard](https://en.wikipedia.org/wiki/VCard), 0-2048 bytes")
    reply_markup: Optional[InlineKeyboardMarkup] = None
    input_message_content: Optional[InputMessageContent] = None
    thumbnail_url: Optional[StrictStr] = Field(default=None, description="*Optional*. Url of the thumbnail for the result")
    thumbnail_width: Optional[StrictInt] = Field(default=None, description="*Optional*. Thumbnail width")
    thumbnail_height: Optional[StrictInt] = Field(default=None, description="*Optional*. Thumbnail height")
    __properties: ClassVar[List[str]] = ["type", "id", "phone_number", "first_name", "last_name", "vcard", "reply_markup", "input_message_content", "thumbnail_url", "thumbnail_width", "thumbnail_height"]

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
        """Create an instance of InlineQueryResultContact from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of reply_markup
        if self.reply_markup:
            _dict['reply_markup'] = self.reply_markup.to_dict()
        # override the default output from pydantic by calling `to_dict()` of input_message_content
        if self.input_message_content:
            _dict['input_message_content'] = self.input_message_content.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of InlineQueryResultContact from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in InlineQueryResultContact) in the input: " + _key)

        _obj = cls.model_validate({
            "type": obj.get("type") if obj.get("type") is not None else 'contact',
            "id": obj.get("id"),
            "phone_number": obj.get("phone_number"),
            "first_name": obj.get("first_name"),
            "last_name": obj.get("last_name"),
            "vcard": obj.get("vcard"),
            "reply_markup": InlineKeyboardMarkup.from_dict(obj["reply_markup"]) if obj.get("reply_markup") is not None else None,
            "input_message_content": InputMessageContent.from_dict(obj["input_message_content"]) if obj.get("input_message_content") is not None else None,
            "thumbnail_url": obj.get("thumbnail_url"),
            "thumbnail_width": obj.get("thumbnail_width"),
            "thumbnail_height": obj.get("thumbnail_height")
        })
        return _obj


