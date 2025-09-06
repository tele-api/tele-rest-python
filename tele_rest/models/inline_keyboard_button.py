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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from tele_rest.models.copy_text_button import CopyTextButton
from tele_rest.models.login_url import LoginUrl
from tele_rest.models.switch_inline_query_chosen_chat import SwitchInlineQueryChosenChat
from tele_rest.models.web_app_info import WebAppInfo
from typing import Optional, Set
from typing_extensions import Self

class InlineKeyboardButton(BaseModel):
    """
    This object represents one button of an inline keyboard. Exactly one of the optional fields must be used to specify type of the button.
    """ # noqa: E501
    text: StrictStr = Field(description="Label text on the button")
    url: Optional[StrictStr] = Field(default=None, description="*Optional*. HTTP or tg:// URL to be opened when the button is pressed. Links `tg://user?id=<user_id>` can be used to mention a user by their identifier without using a username, if this is allowed by their privacy settings.")
    callback_data: Optional[StrictStr] = Field(default=None, description="*Optional*. Data to be sent in a [callback query](https://core.telegram.org/bots/api/#callbackquery) to the bot when the button is pressed, 1-64 bytes")
    web_app: Optional[WebAppInfo] = None
    login_url: Optional[LoginUrl] = None
    switch_inline_query: Optional[StrictStr] = Field(default=None, description="*Optional*. If set, pressing the button will prompt the user to select one of their chats, open that chat and insert the bot's username and the specified inline query in the input field. May be empty, in which case just the bot's username will be inserted. Not supported for messages sent in channel direct messages chats and on behalf of a Telegram Business account.")
    switch_inline_query_current_chat: Optional[StrictStr] = Field(default=None, description="*Optional*. If set, pressing the button will insert the bot's username and the specified inline query in the current chat's input field. May be empty, in which case only the bot's username will be inserted.    This offers a quick way for the user to open your bot in inline mode in the same chat - good for selecting something from multiple options. Not supported in channels and for messages sent in channel direct messages chats and on behalf of a Telegram Business account.")
    switch_inline_query_chosen_chat: Optional[SwitchInlineQueryChosenChat] = None
    copy_text: Optional[CopyTextButton] = None
    callback_game: Optional[Any] = None
    pay: Optional[StrictBool] = Field(default=None, description="*Optional*. Specify *True*, to send a [Pay button](https://core.telegram.org/bots/api/#payments). Substrings “⭐” and “XTR” in the buttons's text will be replaced with a Telegram Star icon.    **NOTE:** This type of button **must** always be the first button in the first row and can only be used in invoice messages.")
    __properties: ClassVar[List[str]] = ["text", "url", "callback_data", "web_app", "login_url", "switch_inline_query", "switch_inline_query_current_chat", "switch_inline_query_chosen_chat", "copy_text", "callback_game", "pay"]

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
        """Create an instance of InlineKeyboardButton from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of web_app
        if self.web_app:
            _dict['web_app'] = self.web_app.to_dict()
        # override the default output from pydantic by calling `to_dict()` of login_url
        if self.login_url:
            _dict['login_url'] = self.login_url.to_dict()
        # override the default output from pydantic by calling `to_dict()` of switch_inline_query_chosen_chat
        if self.switch_inline_query_chosen_chat:
            _dict['switch_inline_query_chosen_chat'] = self.switch_inline_query_chosen_chat.to_dict()
        # override the default output from pydantic by calling `to_dict()` of copy_text
        if self.copy_text:
            _dict['copy_text'] = self.copy_text.to_dict()
        # set to None if callback_game (nullable) is None
        # and model_fields_set contains the field
        if self.callback_game is None and "callback_game" in self.model_fields_set:
            _dict['callback_game'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of InlineKeyboardButton from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in InlineKeyboardButton) in the input: " + _key)

        _obj = cls.model_validate({
            "text": obj.get("text"),
            "url": obj.get("url"),
            "callback_data": obj.get("callback_data"),
            "web_app": WebAppInfo.from_dict(obj["web_app"]) if obj.get("web_app") is not None else None,
            "login_url": LoginUrl.from_dict(obj["login_url"]) if obj.get("login_url") is not None else None,
            "switch_inline_query": obj.get("switch_inline_query"),
            "switch_inline_query_current_chat": obj.get("switch_inline_query_current_chat"),
            "switch_inline_query_chosen_chat": SwitchInlineQueryChosenChat.from_dict(obj["switch_inline_query_chosen_chat"]) if obj.get("switch_inline_query_chosen_chat") is not None else None,
            "copy_text": CopyTextButton.from_dict(obj["copy_text"]) if obj.get("copy_text") is not None else None,
            "callback_game": obj.get("callback_game"),
            "pay": obj.get("pay")
        })
        return _obj


