# coding: utf-8

"""
Telegram Bot API - REST API Client
The Bot API is an HTTP-based interface created for developers keen on building bots for Telegram. To learn how to create and set up a bot, please consult our Introduction to Bots and Bot FAQ.

## Metadata

- **Copyright**: Copyright (c) 2025 Qntx
- **Author**: ΣX <gitctrlx@gmail.com>
- **Version**: 9.2.0
- **Modified**: 2025-09-06T05:32:06.285336202Z[Etc/UTC]
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
from tele_rest.models.chat import Chat
from tele_rest.models.unique_gift_backdrop import UniqueGiftBackdrop
from tele_rest.models.unique_gift_model import UniqueGiftModel
from tele_rest.models.unique_gift_symbol import UniqueGiftSymbol
from typing import Optional, Set
from typing_extensions import Self

class UniqueGift(BaseModel):
    """
    This object describes a unique gift that was upgraded from a regular gift.
    """ # noqa: E501
    base_name: StrictStr = Field(description="Human-readable name of the regular gift from which this unique gift was upgraded")
    name: StrictStr = Field(description="Unique name of the gift. This name can be used in `https://t.me/nft/...` links and story areas")
    number: StrictInt = Field(description="Unique number of the upgraded gift among gifts upgraded from the same regular gift")
    model: UniqueGiftModel
    symbol: UniqueGiftSymbol
    backdrop: UniqueGiftBackdrop
    publisher_chat: Optional[Chat] = None
    __properties: ClassVar[List[str]] = ["base_name", "name", "number", "model", "symbol", "backdrop", "publisher_chat"]

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
        """Create an instance of UniqueGift from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of model
        if self.model:
            _dict['model'] = self.model.to_dict()
        # override the default output from pydantic by calling `to_dict()` of symbol
        if self.symbol:
            _dict['symbol'] = self.symbol.to_dict()
        # override the default output from pydantic by calling `to_dict()` of backdrop
        if self.backdrop:
            _dict['backdrop'] = self.backdrop.to_dict()
        # override the default output from pydantic by calling `to_dict()` of publisher_chat
        if self.publisher_chat:
            _dict['publisher_chat'] = self.publisher_chat.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UniqueGift from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in UniqueGift) in the input: " + _key)

        _obj = cls.model_validate({
            "base_name": obj.get("base_name"),
            "name": obj.get("name"),
            "number": obj.get("number"),
            "model": UniqueGiftModel.from_dict(obj["model"]) if obj.get("model") is not None else None,
            "symbol": UniqueGiftSymbol.from_dict(obj["symbol"]) if obj.get("symbol") is not None else None,
            "backdrop": UniqueGiftBackdrop.from_dict(obj["backdrop"]) if obj.get("backdrop") is not None else None,
            "publisher_chat": Chat.from_dict(obj["publisher_chat"]) if obj.get("publisher_chat") is not None else None
        })
        return _obj


