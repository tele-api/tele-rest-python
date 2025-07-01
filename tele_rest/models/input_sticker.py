# coding: utf-8

"""
Telegram Bot API - REST API Client
The Bot API is an HTTP-based interface created for developers keen on building bots for Telegram. To learn how to create and set up a bot, please consult our Introduction to Bots and Bot FAQ.

## Metadata

- **Copyright**: Copyright (c) 2025 Qntx
- **Author**: ΣX <gitctrlx@gmail.com>
- **Version**: 9.0.0
- **Modified**: 2025-07-01T14:36:24.755929598Z[Etc/UTC]
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

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from tele_rest.models.mask_position import MaskPosition
from typing import Optional, Set
from typing_extensions import Self

class InputSticker(BaseModel):
    """
    This object describes a sticker to be added to a sticker set.
    """ # noqa: E501
    sticker: StrictStr = Field(description="The added sticker. Pass a *file\\_id* as a String to send a file that already exists on the Telegram servers, pass an HTTP URL as a String for Telegram to get a file from the Internet, or pass “attach://\\<file\\_attach\\_name\\>” to upload a new file using multipart/form-data under \\<file\\_attach\\_name\\> name. Animated and video stickers can't be uploaded via HTTP URL. [More information on Sending Files »](https://core.telegram.org/bots/api/#sending-files)")
    format: StrictStr = Field(description="Format of the added sticker, must be one of “static” for a **.WEBP** or **.PNG** image, “animated” for a **.TGS** animation, “video” for a **.WEBM** video")
    emoji_list: List[StrictStr] = Field(description="List of 1-20 emoji associated with the sticker")
    mask_position: Optional[MaskPosition] = None
    keywords: Optional[List[StrictStr]] = Field(default=None, description="*Optional*. List of 0-20 search keywords for the sticker with total length of up to 64 characters. For “regular” and “custom\\_emoji” stickers only.")
    __properties: ClassVar[List[str]] = ["sticker", "format", "emoji_list", "mask_position", "keywords"]

    @field_validator('format')
    def format_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['static', 'animated', 'video']):
            raise ValueError("must be one of enum values ('static', 'animated', 'video')")
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
        """Create an instance of InputSticker from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of mask_position
        if self.mask_position:
            _dict['mask_position'] = self.mask_position.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of InputSticker from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in InputSticker) in the input: " + _key)

        _obj = cls.model_validate({
            "sticker": obj.get("sticker"),
            "format": obj.get("format"),
            "emoji_list": obj.get("emoji_list"),
            "mask_position": MaskPosition.from_dict(obj["mask_position"]) if obj.get("mask_position") is not None else None,
            "keywords": obj.get("keywords")
        })
        return _obj


