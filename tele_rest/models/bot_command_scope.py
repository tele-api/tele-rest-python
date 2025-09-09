# coding: utf-8

"""
Telegram Bot API - REST API Client
The Bot API is an HTTP-based interface created for developers keen on building bots for Telegram. To learn how to create and set up a bot, please consult our Introduction to Bots and Bot FAQ.

## Metadata

- **Copyright**: Copyright (c) 2025 Qntx
- **Author**: ΣX <gitctrlx@gmail.com>
- **Version**: 9.2.0
- **Modified**: 2025-09-09T23:46:51.548881723Z[Etc/UTC]
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
import json
import pprint
from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Any, List, Optional
from tele_rest.models.bot_command_scope_all_chat_administrators import BotCommandScopeAllChatAdministrators
from tele_rest.models.bot_command_scope_all_group_chats import BotCommandScopeAllGroupChats
from tele_rest.models.bot_command_scope_all_private_chats import BotCommandScopeAllPrivateChats
from tele_rest.models.bot_command_scope_chat import BotCommandScopeChat
from tele_rest.models.bot_command_scope_chat_administrators import BotCommandScopeChatAdministrators
from tele_rest.models.bot_command_scope_chat_member import BotCommandScopeChatMember
from tele_rest.models.bot_command_scope_default import BotCommandScopeDefault
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

BOTCOMMANDSCOPE_ONE_OF_SCHEMAS = ["BotCommandScopeAllChatAdministrators", "BotCommandScopeAllGroupChats", "BotCommandScopeAllPrivateChats", "BotCommandScopeChat", "BotCommandScopeChatAdministrators", "BotCommandScopeChatMember", "BotCommandScopeDefault"]

class BotCommandScope(BaseModel):
    """
    This object represents the scope to which bot commands are applied. Currently, the following 7 scopes are supported:  * [BotCommandScopeDefault](https://core.telegram.org/bots/api/#botcommandscopedefault) * [BotCommandScopeAllPrivateChats](https://core.telegram.org/bots/api/#botcommandscopeallprivatechats) * [BotCommandScopeAllGroupChats](https://core.telegram.org/bots/api/#botcommandscopeallgroupchats) * [BotCommandScopeAllChatAdministrators](https://core.telegram.org/bots/api/#botcommandscopeallchatadministrators) * [BotCommandScopeChat](https://core.telegram.org/bots/api/#botcommandscopechat) * [BotCommandScopeChatAdministrators](https://core.telegram.org/bots/api/#botcommandscopechatadministrators) * [BotCommandScopeChatMember](https://core.telegram.org/bots/api/#botcommandscopechatmember)
    """
    # data type: BotCommandScopeDefault
    oneof_schema_1_validator: Optional[BotCommandScopeDefault] = None
    # data type: BotCommandScopeAllPrivateChats
    oneof_schema_2_validator: Optional[BotCommandScopeAllPrivateChats] = None
    # data type: BotCommandScopeAllGroupChats
    oneof_schema_3_validator: Optional[BotCommandScopeAllGroupChats] = None
    # data type: BotCommandScopeAllChatAdministrators
    oneof_schema_4_validator: Optional[BotCommandScopeAllChatAdministrators] = None
    # data type: BotCommandScopeChat
    oneof_schema_5_validator: Optional[BotCommandScopeChat] = None
    # data type: BotCommandScopeChatAdministrators
    oneof_schema_6_validator: Optional[BotCommandScopeChatAdministrators] = None
    # data type: BotCommandScopeChatMember
    oneof_schema_7_validator: Optional[BotCommandScopeChatMember] = None
    actual_instance: Optional[Union[BotCommandScopeAllChatAdministrators, BotCommandScopeAllGroupChats, BotCommandScopeAllPrivateChats, BotCommandScopeChat, BotCommandScopeChatAdministrators, BotCommandScopeChatMember, BotCommandScopeDefault]] = None
    one_of_schemas: Set[str] = { "BotCommandScopeAllChatAdministrators", "BotCommandScopeAllGroupChats", "BotCommandScopeAllPrivateChats", "BotCommandScopeChat", "BotCommandScopeChatAdministrators", "BotCommandScopeChatMember", "BotCommandScopeDefault" }

    model_config = ConfigDict(
        validate_assignment=True,
        protected_namespaces=(),
    )


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
    def actual_instance_must_validate_oneof(cls, v):
        instance = BotCommandScope.model_construct()
        error_messages = []
        match = 0
        # validate data type: BotCommandScopeDefault
        if not isinstance(v, BotCommandScopeDefault):
            error_messages.append(f"Error! Input type `{type(v)}` is not `BotCommandScopeDefault`")
        else:
            match += 1
        # validate data type: BotCommandScopeAllPrivateChats
        if not isinstance(v, BotCommandScopeAllPrivateChats):
            error_messages.append(f"Error! Input type `{type(v)}` is not `BotCommandScopeAllPrivateChats`")
        else:
            match += 1
        # validate data type: BotCommandScopeAllGroupChats
        if not isinstance(v, BotCommandScopeAllGroupChats):
            error_messages.append(f"Error! Input type `{type(v)}` is not `BotCommandScopeAllGroupChats`")
        else:
            match += 1
        # validate data type: BotCommandScopeAllChatAdministrators
        if not isinstance(v, BotCommandScopeAllChatAdministrators):
            error_messages.append(f"Error! Input type `{type(v)}` is not `BotCommandScopeAllChatAdministrators`")
        else:
            match += 1
        # validate data type: BotCommandScopeChat
        if not isinstance(v, BotCommandScopeChat):
            error_messages.append(f"Error! Input type `{type(v)}` is not `BotCommandScopeChat`")
        else:
            match += 1
        # validate data type: BotCommandScopeChatAdministrators
        if not isinstance(v, BotCommandScopeChatAdministrators):
            error_messages.append(f"Error! Input type `{type(v)}` is not `BotCommandScopeChatAdministrators`")
        else:
            match += 1
        # validate data type: BotCommandScopeChatMember
        if not isinstance(v, BotCommandScopeChatMember):
            error_messages.append(f"Error! Input type `{type(v)}` is not `BotCommandScopeChatMember`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in BotCommandScope with oneOf schemas: BotCommandScopeAllChatAdministrators, BotCommandScopeAllGroupChats, BotCommandScopeAllPrivateChats, BotCommandScopeChat, BotCommandScopeChatAdministrators, BotCommandScopeChatMember, BotCommandScopeDefault. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in BotCommandScope with oneOf schemas: BotCommandScopeAllChatAdministrators, BotCommandScopeAllGroupChats, BotCommandScopeAllPrivateChats, BotCommandScopeChat, BotCommandScopeChatAdministrators, BotCommandScopeChatMember, BotCommandScopeDefault. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: Union[str, Dict[str, Any]]) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        error_messages = []
        match = 0

        # deserialize data into BotCommandScopeDefault
        try:
            instance.actual_instance = BotCommandScopeDefault.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into BotCommandScopeAllPrivateChats
        try:
            instance.actual_instance = BotCommandScopeAllPrivateChats.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into BotCommandScopeAllGroupChats
        try:
            instance.actual_instance = BotCommandScopeAllGroupChats.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into BotCommandScopeAllChatAdministrators
        try:
            instance.actual_instance = BotCommandScopeAllChatAdministrators.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into BotCommandScopeChat
        try:
            instance.actual_instance = BotCommandScopeChat.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into BotCommandScopeChatAdministrators
        try:
            instance.actual_instance = BotCommandScopeChatAdministrators.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into BotCommandScopeChatMember
        try:
            instance.actual_instance = BotCommandScopeChatMember.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into BotCommandScope with oneOf schemas: BotCommandScopeAllChatAdministrators, BotCommandScopeAllGroupChats, BotCommandScopeAllPrivateChats, BotCommandScopeChat, BotCommandScopeChatAdministrators, BotCommandScopeChatMember, BotCommandScopeDefault. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into BotCommandScope with oneOf schemas: BotCommandScopeAllChatAdministrators, BotCommandScopeAllGroupChats, BotCommandScopeAllPrivateChats, BotCommandScopeChat, BotCommandScopeChatAdministrators, BotCommandScopeChatMember, BotCommandScopeDefault. Details: " + ", ".join(error_messages))
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

    def to_dict(self) -> Optional[Union[Dict[str, Any], BotCommandScopeAllChatAdministrators, BotCommandScopeAllGroupChats, BotCommandScopeAllPrivateChats, BotCommandScopeChat, BotCommandScopeChatAdministrators, BotCommandScopeChatMember, BotCommandScopeDefault]]:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        if hasattr(self.actual_instance, "to_dict") and callable(self.actual_instance.to_dict):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())


