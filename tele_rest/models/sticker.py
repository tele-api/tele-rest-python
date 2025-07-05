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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from tele_rest.models.file import File
from tele_rest.models.mask_position import MaskPosition
from tele_rest.models.photo_size import PhotoSize
from typing import Optional, Set
from typing_extensions import Self

class Sticker(BaseModel):
    """
    This object represents a sticker.
    """ # noqa: E501
    file_id: StrictStr = Field(description="Identifier for this file, which can be used to download or reuse the file")
    file_unique_id: StrictStr = Field(description="Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.")
    type: StrictStr = Field(description="Type of the sticker, currently one of “regular”, “mask”, “custom\\_emoji”. The type of the sticker is independent from its format, which is determined by the fields *is\\_animated* and *is\\_video*.")
    width: StrictInt = Field(description="Sticker width")
    height: StrictInt = Field(description="Sticker height")
    is_animated: StrictBool = Field(description="*True*, if the sticker is [animated](https://telegram.org/blog/animated-stickers)")
    is_video: StrictBool = Field(description="*True*, if the sticker is a [video sticker](https://telegram.org/blog/video-stickers-better-reactions)")
    thumbnail: Optional[PhotoSize] = None
    emoji: Optional[StrictStr] = Field(default=None, description="*Optional*. Emoji associated with the sticker")
    set_name: Optional[StrictStr] = Field(default=None, description="*Optional*. Name of the sticker set to which the sticker belongs")
    premium_animation: Optional[File] = None
    mask_position: Optional[MaskPosition] = None
    custom_emoji_id: Optional[StrictStr] = Field(default=None, description="*Optional*. For custom emoji stickers, unique identifier of the custom emoji")
    needs_repainting: Optional[StrictBool] = Field(default=True, description="*Optional*. *True*, if the sticker must be repainted to a text color in messages, the color of the Telegram Premium badge in emoji status, white color on chat photos, or another appropriate color in other places")
    file_size: Optional[StrictInt] = Field(default=None, description="*Optional*. File size in bytes")
    __properties: ClassVar[List[str]] = ["file_id", "file_unique_id", "type", "width", "height", "is_animated", "is_video", "thumbnail", "emoji", "set_name", "premium_animation", "mask_position", "custom_emoji_id", "needs_repainting", "file_size"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['regular', 'mask', 'custom_emoji']):
            raise ValueError("must be one of enum values ('regular', 'mask', 'custom_emoji')")
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
        """Create an instance of Sticker from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of thumbnail
        if self.thumbnail:
            _dict['thumbnail'] = self.thumbnail.to_dict()
        # override the default output from pydantic by calling `to_dict()` of premium_animation
        if self.premium_animation:
            _dict['premium_animation'] = self.premium_animation.to_dict()
        # override the default output from pydantic by calling `to_dict()` of mask_position
        if self.mask_position:
            _dict['mask_position'] = self.mask_position.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Sticker from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in Sticker) in the input: " + _key)

        _obj = cls.model_validate({
            "file_id": obj.get("file_id"),
            "file_unique_id": obj.get("file_unique_id"),
            "type": obj.get("type"),
            "width": obj.get("width"),
            "height": obj.get("height"),
            "is_animated": obj.get("is_animated"),
            "is_video": obj.get("is_video"),
            "thumbnail": PhotoSize.from_dict(obj["thumbnail"]) if obj.get("thumbnail") is not None else None,
            "emoji": obj.get("emoji"),
            "set_name": obj.get("set_name"),
            "premium_animation": File.from_dict(obj["premium_animation"]) if obj.get("premium_animation") is not None else None,
            "mask_position": MaskPosition.from_dict(obj["mask_position"]) if obj.get("mask_position") is not None else None,
            "custom_emoji_id": obj.get("custom_emoji_id"),
            "needs_repainting": obj.get("needs_repainting") if obj.get("needs_repainting") is not None else True,
            "file_size": obj.get("file_size")
        })
        return _obj


