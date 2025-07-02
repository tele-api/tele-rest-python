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
from typing_extensions import Annotated
from tele_rest.models.message_entity import MessageEntity
from tele_rest.models.reply_parameters_chat_id import ReplyParametersChatId
from typing import Optional, Set
from typing_extensions import Self

class ReplyParameters(BaseModel):
    """
    Describes reply parameters for the message that is being sent.
    """ # noqa: E501
    message_id: StrictInt = Field(description="Identifier of the message that will be replied to in the current chat, or in the chat *chat\\_id* if it is specified")
    chat_id: Optional[ReplyParametersChatId] = None
    allow_sending_without_reply: Optional[StrictBool] = Field(default=None, description="*Optional*. Pass *True* if the message should be sent even if the specified message to be replied to is not found. Always *False* for replies in another chat or forum topic. Always *True* for messages sent on behalf of a business account.")
    quote: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=1024)]] = Field(default=None, description="*Optional*. Quoted part of the message to be replied to; 0-1024 characters after entities parsing. The quote must be an exact substring of the message to be replied to, including *bold*, *italic*, *underline*, *strikethrough*, *spoiler*, and *custom\\_emoji* entities. The message will fail to send if the quote isn't found in the original message.")
    quote_parse_mode: Optional[StrictStr] = Field(default=None, description="*Optional*. Mode for parsing entities in the quote. See [formatting options](https://core.telegram.org/bots/api/#formatting-options) for more details.")
    quote_entities: Optional[List[MessageEntity]] = Field(default=None, description="*Optional*. A JSON-serialized list of special entities that appear in the quote. It can be specified instead of *quote\\_parse\\_mode*.")
    quote_position: Optional[StrictInt] = Field(default=None, description="*Optional*. Position of the quote in the original message in UTF-16 code units")
    __properties: ClassVar[List[str]] = ["message_id", "chat_id", "allow_sending_without_reply", "quote", "quote_parse_mode", "quote_entities", "quote_position"]

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
        """Create an instance of ReplyParameters from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in quote_entities (list)
        _items = []
        if self.quote_entities:
            for _item_quote_entities in self.quote_entities:
                if _item_quote_entities:
                    _items.append(_item_quote_entities.to_dict())
            _dict['quote_entities'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ReplyParameters from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in ReplyParameters) in the input: " + _key)

        _obj = cls.model_validate({
            "message_id": obj.get("message_id"),
            "chat_id": ReplyParametersChatId.from_dict(obj["chat_id"]) if obj.get("chat_id") is not None else None,
            "allow_sending_without_reply": obj.get("allow_sending_without_reply"),
            "quote": obj.get("quote"),
            "quote_parse_mode": obj.get("quote_parse_mode"),
            "quote_entities": [MessageEntity.from_dict(_item) for _item in obj["quote_entities"]] if obj.get("quote_entities") is not None else None,
            "quote_position": obj.get("quote_position")
        })
        return _obj


