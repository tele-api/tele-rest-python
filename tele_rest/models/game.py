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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from tele_rest.models.animation import Animation
from tele_rest.models.message_entity import MessageEntity
from tele_rest.models.photo_size import PhotoSize
from typing import Optional, Set
from typing_extensions import Self

class Game(BaseModel):
    """
    This object represents a game. Use BotFather to create and edit games, their short names will act as unique identifiers.
    """ # noqa: E501
    title: StrictStr = Field(description="Title of the game")
    description: StrictStr = Field(description="Description of the game")
    photo: List[PhotoSize] = Field(description="Photo that will be displayed in the game message in chats.")
    text: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=4096)]] = Field(default=None, description="*Optional*. Brief description of the game or high scores included in the game message. Can be automatically edited to include current high scores for the game when the bot calls [setGameScore](https://core.telegram.org/bots/api/#setgamescore), or manually edited using [editMessageText](https://core.telegram.org/bots/api/#editmessagetext). 0-4096 characters.")
    text_entities: Optional[List[MessageEntity]] = Field(default=None, description="*Optional*. Special entities that appear in *text*, such as usernames, URLs, bot commands, etc.")
    animation: Optional[Animation] = None
    __properties: ClassVar[List[str]] = ["title", "description", "photo", "text", "text_entities", "animation"]

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
        """Create an instance of Game from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in photo (list)
        _items = []
        if self.photo:
            for _item_photo in self.photo:
                if _item_photo:
                    _items.append(_item_photo.to_dict())
            _dict['photo'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in text_entities (list)
        _items = []
        if self.text_entities:
            for _item_text_entities in self.text_entities:
                if _item_text_entities:
                    _items.append(_item_text_entities.to_dict())
            _dict['text_entities'] = _items
        # override the default output from pydantic by calling `to_dict()` of animation
        if self.animation:
            _dict['animation'] = self.animation.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Game from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in Game) in the input: " + _key)

        _obj = cls.model_validate({
            "title": obj.get("title"),
            "description": obj.get("description"),
            "photo": [PhotoSize.from_dict(_item) for _item in obj["photo"]] if obj.get("photo") is not None else None,
            "text": obj.get("text"),
            "text_entities": [MessageEntity.from_dict(_item) for _item in obj["text_entities"]] if obj.get("text_entities") is not None else None,
            "animation": Animation.from_dict(obj["animation"]) if obj.get("animation") is not None else None
        })
        return _obj


