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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from tele_rest.models.edit_message_text_request_chat_id import EditMessageTextRequestChatId
from tele_rest.models.inline_keyboard_markup import InlineKeyboardMarkup
from tele_rest.models.message_entity import MessageEntity
from typing import Optional, Set
from typing_extensions import Self

class EditMessageCaptionRequest(BaseModel):
    """
    Request parameters for editMessageCaption
    """ # noqa: E501
    business_connection_id: Optional[StrictStr] = Field(default=None, description="Unique identifier of the business connection on behalf of which the message to be edited was sent")
    chat_id: Optional[EditMessageTextRequestChatId] = None
    message_id: Optional[StrictInt] = Field(default=None, description="Required if *inline\\_message\\_id* is not specified. Identifier of the message to edit")
    inline_message_id: Optional[StrictStr] = Field(default=None, description="Required if *chat\\_id* and *message\\_id* are not specified. Identifier of the inline message")
    caption: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=1024)]] = Field(default=None, description="New caption of the message, 0-1024 characters after entities parsing")
    parse_mode: Optional[StrictStr] = Field(default=None, description="Mode for parsing entities in the message caption. See [formatting options](https://core.telegram.org/bots/api/#formatting-options) for more details.")
    caption_entities: Optional[List[MessageEntity]] = Field(default=None, description="A JSON-serialized list of special entities that appear in the caption, which can be specified instead of *parse\\_mode*")
    show_caption_above_media: Optional[StrictBool] = Field(default=None, description="Pass *True*, if the caption must be shown above the message media. Supported only for animation, photo and video messages.")
    reply_markup: Optional[InlineKeyboardMarkup] = None
    __properties: ClassVar[List[str]] = ["business_connection_id", "chat_id", "message_id", "inline_message_id", "caption", "parse_mode", "caption_entities", "show_caption_above_media", "reply_markup"]

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
        """Create an instance of EditMessageCaptionRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of chat_id
        if self.chat_id:
            _dict['chat_id'] = self.chat_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in caption_entities (list)
        _items = []
        if self.caption_entities:
            for _item_caption_entities in self.caption_entities:
                if _item_caption_entities:
                    _items.append(_item_caption_entities.to_dict())
            _dict['caption_entities'] = _items
        # override the default output from pydantic by calling `to_dict()` of reply_markup
        if self.reply_markup:
            _dict['reply_markup'] = self.reply_markup.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EditMessageCaptionRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in EditMessageCaptionRequest) in the input: " + _key)

        _obj = cls.model_validate({
            "business_connection_id": obj.get("business_connection_id"),
            "chat_id": EditMessageTextRequestChatId.from_dict(obj["chat_id"]) if obj.get("chat_id") is not None else None,
            "message_id": obj.get("message_id"),
            "inline_message_id": obj.get("inline_message_id"),
            "caption": obj.get("caption"),
            "parse_mode": obj.get("parse_mode"),
            "caption_entities": [MessageEntity.from_dict(_item) for _item in obj["caption_entities"]] if obj.get("caption_entities") is not None else None,
            "show_caption_above_media": obj.get("show_caption_above_media"),
            "reply_markup": InlineKeyboardMarkup.from_dict(obj["reply_markup"]) if obj.get("reply_markup") is not None else None
        })
        return _obj


