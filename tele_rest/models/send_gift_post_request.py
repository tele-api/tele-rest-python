# coding: utf-8

"""
Telegram Bot API - REST API Client
Auto-generated OpenAPI schema

## Metadata

- **Copyright**: Copyright (c) 2025 Qntx
- **Author**: ΣX <gitctrlx@gmail.com>
- **Version**: 9.0.0
- **Modified**: 2025-07-01T14:15:10.340422036Z[Etc/UTC]
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
from tele_rest.models.message_entity import MessageEntity
from tele_rest.models.send_gift_post_request_chat_id import SendGiftPostRequestChatId
from typing import Optional, Set
from typing_extensions import Self

class SendGiftPostRequest(BaseModel):
    """
    SendGiftPostRequest
    """ # noqa: E501
    user_id: Optional[StrictInt] = Field(default=None, description="Required if *chat\\_id* is not specified. Unique identifier of the target user who will receive the gift.")
    chat_id: Optional[SendGiftPostRequestChatId] = None
    gift_id: StrictStr = Field(description="Identifier of the gift")
    pay_for_upgrade: Optional[StrictBool] = Field(default=None, description="Pass *True* to pay for the gift upgrade from the bot's balance, thereby making the upgrade free for the receiver")
    text: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=128)]] = Field(default=None, description="Text that will be shown along with the gift; 0-128 characters")
    text_parse_mode: Optional[StrictStr] = Field(default=None, description="Mode for parsing entities in the text. See [formatting options](https://core.telegram.org/bots/api/#formatting-options) for more details. Entities other than “bold”, “italic”, “underline”, “strikethrough”, “spoiler”, and “custom\\_emoji” are ignored.")
    text_entities: Optional[List[MessageEntity]] = Field(default=None, description="A JSON-serialized list of special entities that appear in the gift text. It can be specified instead of *text\\_parse\\_mode*. Entities other than “bold”, “italic”, “underline”, “strikethrough”, “spoiler”, and “custom\\_emoji” are ignored.")
    __properties: ClassVar[List[str]] = ["user_id", "chat_id", "gift_id", "pay_for_upgrade", "text", "text_parse_mode", "text_entities"]

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
        """Create an instance of SendGiftPostRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in text_entities (list)
        _items = []
        if self.text_entities:
            for _item_text_entities in self.text_entities:
                if _item_text_entities:
                    _items.append(_item_text_entities.to_dict())
            _dict['text_entities'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SendGiftPostRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in SendGiftPostRequest) in the input: " + _key)

        _obj = cls.model_validate({
            "user_id": obj.get("user_id"),
            "chat_id": SendGiftPostRequestChatId.from_dict(obj["chat_id"]) if obj.get("chat_id") is not None else None,
            "gift_id": obj.get("gift_id"),
            "pay_for_upgrade": obj.get("pay_for_upgrade"),
            "text": obj.get("text"),
            "text_parse_mode": obj.get("text_parse_mode"),
            "text_entities": [MessageEntity.from_dict(_item) for _item in obj["text_entities"]] if obj.get("text_entities") is not None else None
        })
        return _obj


