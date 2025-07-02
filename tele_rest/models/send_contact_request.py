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
from tele_rest.models.reply_parameters import ReplyParameters
from tele_rest.models.send_message_request_chat_id import SendMessageRequestChatId
from tele_rest.models.send_message_request_reply_markup import SendMessageRequestReplyMarkup
from typing import Optional, Set
from typing_extensions import Self

class SendContactRequest(BaseModel):
    """
    Request parameters for sendContact
    """ # noqa: E501
    business_connection_id: Optional[StrictStr] = Field(default=None, description="Unique identifier of the business connection on behalf of which the message will be sent")
    chat_id: SendMessageRequestChatId
    message_thread_id: Optional[StrictInt] = Field(default=None, description="Unique identifier for the target message thread (topic) of the forum; for forum supergroups only")
    phone_number: StrictStr = Field(description="Contact's phone number")
    first_name: StrictStr = Field(description="Contact's first name")
    last_name: Optional[StrictStr] = Field(default=None, description="Contact's last name")
    vcard: Optional[StrictStr] = Field(default=None, description="Additional data about the contact in the form of a [vCard](https://en.wikipedia.org/wiki/VCard), 0-2048 bytes")
    disable_notification: Optional[StrictBool] = Field(default=None, description="Sends the message [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound.")
    protect_content: Optional[StrictBool] = Field(default=None, description="Protects the contents of the sent message from forwarding and saving")
    allow_paid_broadcast: Optional[StrictBool] = Field(default=None, description="Pass *True* to allow up to 1000 messages per second, ignoring [broadcasting limits](https://core.telegram.org/bots/faq#how-can-i-message-all-of-my-bot-39s-subscribers-at-once) for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot's balance")
    message_effect_id: Optional[StrictStr] = Field(default=None, description="Unique identifier of the message effect to be added to the message; for private chats only")
    reply_parameters: Optional[ReplyParameters] = None
    reply_markup: Optional[SendMessageRequestReplyMarkup] = None
    __properties: ClassVar[List[str]] = ["business_connection_id", "chat_id", "message_thread_id", "phone_number", "first_name", "last_name", "vcard", "disable_notification", "protect_content", "allow_paid_broadcast", "message_effect_id", "reply_parameters", "reply_markup"]

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
        """Create an instance of SendContactRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of reply_parameters
        if self.reply_parameters:
            _dict['reply_parameters'] = self.reply_parameters.to_dict()
        # override the default output from pydantic by calling `to_dict()` of reply_markup
        if self.reply_markup:
            _dict['reply_markup'] = self.reply_markup.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SendContactRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in SendContactRequest) in the input: " + _key)

        _obj = cls.model_validate({
            "business_connection_id": obj.get("business_connection_id"),
            "chat_id": SendMessageRequestChatId.from_dict(obj["chat_id"]) if obj.get("chat_id") is not None else None,
            "message_thread_id": obj.get("message_thread_id"),
            "phone_number": obj.get("phone_number"),
            "first_name": obj.get("first_name"),
            "last_name": obj.get("last_name"),
            "vcard": obj.get("vcard"),
            "disable_notification": obj.get("disable_notification"),
            "protect_content": obj.get("protect_content"),
            "allow_paid_broadcast": obj.get("allow_paid_broadcast"),
            "message_effect_id": obj.get("message_effect_id"),
            "reply_parameters": ReplyParameters.from_dict(obj["reply_parameters"]) if obj.get("reply_parameters") is not None else None,
            "reply_markup": SendMessageRequestReplyMarkup.from_dict(obj["reply_markup"]) if obj.get("reply_markup") is not None else None
        })
        return _obj


