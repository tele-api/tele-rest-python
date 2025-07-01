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
from inspect import getfullargspec
import json
import pprint
import re  # noqa: F401
from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Optional
from tele_rest.models.message_origin_channel import MessageOriginChannel
from tele_rest.models.message_origin_chat import MessageOriginChat
from tele_rest.models.message_origin_hidden_user import MessageOriginHiddenUser
from tele_rest.models.message_origin_user import MessageOriginUser
from typing import Union, Any, List, Set, TYPE_CHECKING, Optional, Dict
from typing_extensions import Literal, Self
from pydantic import Field

MESSAGEORIGIN_ANY_OF_SCHEMAS = ["MessageOriginChannel", "MessageOriginChat", "MessageOriginHiddenUser", "MessageOriginUser"]

class MessageOrigin(BaseModel):
    """
    This object describes the origin of a message. It can be one of  * [MessageOriginUser](https://core.telegram.org/bots/api/#messageoriginuser) * [MessageOriginHiddenUser](https://core.telegram.org/bots/api/#messageoriginhiddenuser) * [MessageOriginChat](https://core.telegram.org/bots/api/#messageoriginchat) * [MessageOriginChannel](https://core.telegram.org/bots/api/#messageoriginchannel)
    """

    # data type: MessageOriginUser
    anyof_schema_1_validator: Optional[MessageOriginUser] = None
    # data type: MessageOriginHiddenUser
    anyof_schema_2_validator: Optional[MessageOriginHiddenUser] = None
    # data type: MessageOriginChat
    anyof_schema_3_validator: Optional[MessageOriginChat] = None
    # data type: MessageOriginChannel
    anyof_schema_4_validator: Optional[MessageOriginChannel] = None
    if TYPE_CHECKING:
        actual_instance: Optional[Union[MessageOriginChannel, MessageOriginChat, MessageOriginHiddenUser, MessageOriginUser]] = None
    else:
        actual_instance: Any = None
    any_of_schemas: Set[str] = { "MessageOriginChannel", "MessageOriginChat", "MessageOriginHiddenUser", "MessageOriginUser" }

    model_config = {
        "validate_assignment": True,
        "protected_namespaces": (),
    }

    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator('actual_instance')
    def actual_instance_must_validate_anyof(cls, v):
        instance = MessageOrigin.model_construct()
        error_messages = []
        # validate data type: MessageOriginUser
        if not isinstance(v, MessageOriginUser):
            error_messages.append(f"Error! Input type `{type(v)}` is not `MessageOriginUser`")
        else:
            return v

        # validate data type: MessageOriginHiddenUser
        if not isinstance(v, MessageOriginHiddenUser):
            error_messages.append(f"Error! Input type `{type(v)}` is not `MessageOriginHiddenUser`")
        else:
            return v

        # validate data type: MessageOriginChat
        if not isinstance(v, MessageOriginChat):
            error_messages.append(f"Error! Input type `{type(v)}` is not `MessageOriginChat`")
        else:
            return v

        # validate data type: MessageOriginChannel
        if not isinstance(v, MessageOriginChannel):
            error_messages.append(f"Error! Input type `{type(v)}` is not `MessageOriginChannel`")
        else:
            return v

        if error_messages:
            # no match
            raise ValueError("No match found when setting the actual_instance in MessageOrigin with anyOf schemas: MessageOriginChannel, MessageOriginChat, MessageOriginHiddenUser, MessageOriginUser. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: Dict[str, Any]) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        error_messages = []
        # anyof_schema_1_validator: Optional[MessageOriginUser] = None
        try:
            instance.actual_instance = MessageOriginUser.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_2_validator: Optional[MessageOriginHiddenUser] = None
        try:
            instance.actual_instance = MessageOriginHiddenUser.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_3_validator: Optional[MessageOriginChat] = None
        try:
            instance.actual_instance = MessageOriginChat.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_4_validator: Optional[MessageOriginChannel] = None
        try:
            instance.actual_instance = MessageOriginChannel.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))

        if error_messages:
            # no match
            raise ValueError("No match found when deserializing the JSON string into MessageOrigin with anyOf schemas: MessageOriginChannel, MessageOriginChat, MessageOriginHiddenUser, MessageOriginUser. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        if hasattr(self.actual_instance, "to_json") and callable(self.actual_instance.to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> Optional[Union[Dict[str, Any], MessageOriginChannel, MessageOriginChat, MessageOriginHiddenUser, MessageOriginUser]]:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        if hasattr(self.actual_instance, "to_dict") and callable(self.actual_instance.to_dict):
            return self.actual_instance.to_dict()
        else:
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())


