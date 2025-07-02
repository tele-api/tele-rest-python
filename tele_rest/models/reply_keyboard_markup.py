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

from pydantic import BaseModel, ConfigDict, Field, StrictBool
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from tele_rest.models.keyboard_button import KeyboardButton
from typing import Optional, Set
from typing_extensions import Self

class ReplyKeyboardMarkup(BaseModel):
    """
    This object represents a [custom keyboard](https://core.telegram.org/bots/features#keyboards) with reply options (see [Introduction to bots](https://core.telegram.org/bots/features#keyboards) for details and examples). Not supported in channels and for messages sent on behalf of a Telegram Business account.
    """ # noqa: E501
    keyboard: List[List[KeyboardButton]] = Field(description="Array of button rows, each represented by an Array of [KeyboardButton](https://core.telegram.org/bots/api/#keyboardbutton) objects")
    is_persistent: Optional[StrictBool] = Field(default=False, description="*Optional*. Requests clients to always show the keyboard when the regular keyboard is hidden. Defaults to *false*, in which case the custom keyboard can be hidden and opened with a keyboard icon.")
    resize_keyboard: Optional[StrictBool] = Field(default=False, description="*Optional*. Requests clients to resize the keyboard vertically for optimal fit (e.g., make the keyboard smaller if there are just two rows of buttons). Defaults to *false*, in which case the custom keyboard is always of the same height as the app's standard keyboard.")
    one_time_keyboard: Optional[StrictBool] = Field(default=False, description="*Optional*. Requests clients to hide the keyboard as soon as it's been used. The keyboard will still be available, but clients will automatically display the usual letter-keyboard in the chat - the user can press a special button in the input field to see the custom keyboard again. Defaults to *false*.")
    input_field_placeholder: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=64)]] = Field(default=None, description="*Optional*. The placeholder to be shown in the input field when the keyboard is active; 1-64 characters")
    selective: Optional[StrictBool] = Field(default=None, description="*Optional*. Use this parameter if you want to show the keyboard to specific users only. Targets: 1) users that are @mentioned in the *text* of the [Message](https://core.telegram.org/bots/api/#message) object; 2) if the bot's message is a reply to a message in the same chat and forum topic, sender of the original message.    *Example:* A user requests to change the bot's language, bot replies to the request with a keyboard to select the new language. Other users in the group don't see the keyboard.")
    __properties: ClassVar[List[str]] = ["keyboard", "is_persistent", "resize_keyboard", "one_time_keyboard", "input_field_placeholder", "selective"]

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
        """Create an instance of ReplyKeyboardMarkup from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in keyboard (list of list)
        _items = []
        if self.keyboard:
            for _item_keyboard in self.keyboard:
                if _item_keyboard:
                    _items.append(
                         [_inner_item.to_dict() for _inner_item in _item_keyboard if _inner_item is not None]
                    )
            _dict['keyboard'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ReplyKeyboardMarkup from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in ReplyKeyboardMarkup) in the input: " + _key)

        _obj = cls.model_validate({
            "keyboard": [
                    [KeyboardButton.from_dict(_inner_item) for _inner_item in _item]
                    for _item in obj["keyboard"]
                ] if obj.get("keyboard") is not None else None,
            "is_persistent": obj.get("is_persistent") if obj.get("is_persistent") is not None else False,
            "resize_keyboard": obj.get("resize_keyboard") if obj.get("resize_keyboard") is not None else False,
            "one_time_keyboard": obj.get("one_time_keyboard") if obj.get("one_time_keyboard") is not None else False,
            "input_field_placeholder": obj.get("input_field_placeholder"),
            "selective": obj.get("selective")
        })
        return _obj


