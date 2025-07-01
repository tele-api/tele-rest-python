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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from tele_rest.models.photo_size import PhotoSize
from typing import Optional, Set
from typing_extensions import Self

class Video(BaseModel):
    """
    This object represents a video file.
    """ # noqa: E501
    file_id: StrictStr = Field(description="Identifier for this file, which can be used to download or reuse the file")
    file_unique_id: StrictStr = Field(description="Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.")
    width: StrictInt = Field(description="Video width as defined by the sender")
    height: StrictInt = Field(description="Video height as defined by the sender")
    duration: StrictInt = Field(description="Duration of the video in seconds as defined by the sender")
    thumbnail: Optional[PhotoSize] = None
    cover: Optional[List[PhotoSize]] = Field(default=None, description="*Optional*. Available sizes of the cover of the video in the message")
    start_timestamp: Optional[StrictInt] = Field(default=None, description="*Optional*. Timestamp in seconds from which the video will play in the message")
    file_name: Optional[StrictStr] = Field(default=None, description="*Optional*. Original filename as defined by the sender")
    mime_type: Optional[StrictStr] = Field(default=None, description="*Optional*. MIME type of the file as defined by the sender")
    file_size: Optional[StrictInt] = Field(default=None, description="*Optional*. File size in bytes. It can be bigger than 2^31 and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this value.")
    __properties: ClassVar[List[str]] = ["file_id", "file_unique_id", "width", "height", "duration", "thumbnail", "cover", "start_timestamp", "file_name", "mime_type", "file_size"]

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
        """Create an instance of Video from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in cover (list)
        _items = []
        if self.cover:
            for _item_cover in self.cover:
                if _item_cover:
                    _items.append(_item_cover.to_dict())
            _dict['cover'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Video from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in Video) in the input: " + _key)

        _obj = cls.model_validate({
            "file_id": obj.get("file_id"),
            "file_unique_id": obj.get("file_unique_id"),
            "width": obj.get("width"),
            "height": obj.get("height"),
            "duration": obj.get("duration"),
            "thumbnail": PhotoSize.from_dict(obj["thumbnail"]) if obj.get("thumbnail") is not None else None,
            "cover": [PhotoSize.from_dict(_item) for _item in obj["cover"]] if obj.get("cover") is not None else None,
            "start_timestamp": obj.get("start_timestamp"),
            "file_name": obj.get("file_name"),
            "mime_type": obj.get("mime_type"),
            "file_size": obj.get("file_size")
        })
        return _obj


