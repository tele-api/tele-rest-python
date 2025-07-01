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
from tele_rest.models.transaction_partner_affiliate_program import TransactionPartnerAffiliateProgram
from tele_rest.models.transaction_partner_chat import TransactionPartnerChat
from tele_rest.models.transaction_partner_fragment import TransactionPartnerFragment
from tele_rest.models.transaction_partner_other import TransactionPartnerOther
from tele_rest.models.transaction_partner_telegram_ads import TransactionPartnerTelegramAds
from tele_rest.models.transaction_partner_telegram_api import TransactionPartnerTelegramApi
from tele_rest.models.transaction_partner_user import TransactionPartnerUser
from typing import Union, Any, List, Set, TYPE_CHECKING, Optional, Dict
from typing_extensions import Literal, Self
from pydantic import Field

TRANSACTIONPARTNER_ANY_OF_SCHEMAS = ["TransactionPartnerAffiliateProgram", "TransactionPartnerChat", "TransactionPartnerFragment", "TransactionPartnerOther", "TransactionPartnerTelegramAds", "TransactionPartnerTelegramApi", "TransactionPartnerUser"]

class TransactionPartner(BaseModel):
    """
    This object describes the source of a transaction, or its recipient for outgoing transactions. Currently, it can be one of  * [TransactionPartnerUser](https://core.telegram.org/bots/api/#transactionpartneruser) * [TransactionPartnerChat](https://core.telegram.org/bots/api/#transactionpartnerchat) * [TransactionPartnerAffiliateProgram](https://core.telegram.org/bots/api/#transactionpartneraffiliateprogram) * [TransactionPartnerFragment](https://core.telegram.org/bots/api/#transactionpartnerfragment) * [TransactionPartnerTelegramAds](https://core.telegram.org/bots/api/#transactionpartnertelegramads) * [TransactionPartnerTelegramApi](https://core.telegram.org/bots/api/#transactionpartnertelegramapi) * [TransactionPartnerOther](https://core.telegram.org/bots/api/#transactionpartnerother)
    """

    # data type: TransactionPartnerUser
    anyof_schema_1_validator: Optional[TransactionPartnerUser] = None
    # data type: TransactionPartnerChat
    anyof_schema_2_validator: Optional[TransactionPartnerChat] = None
    # data type: TransactionPartnerAffiliateProgram
    anyof_schema_3_validator: Optional[TransactionPartnerAffiliateProgram] = None
    # data type: TransactionPartnerFragment
    anyof_schema_4_validator: Optional[TransactionPartnerFragment] = None
    # data type: TransactionPartnerTelegramAds
    anyof_schema_5_validator: Optional[TransactionPartnerTelegramAds] = None
    # data type: TransactionPartnerTelegramApi
    anyof_schema_6_validator: Optional[TransactionPartnerTelegramApi] = None
    # data type: TransactionPartnerOther
    anyof_schema_7_validator: Optional[TransactionPartnerOther] = None
    if TYPE_CHECKING:
        actual_instance: Optional[Union[TransactionPartnerAffiliateProgram, TransactionPartnerChat, TransactionPartnerFragment, TransactionPartnerOther, TransactionPartnerTelegramAds, TransactionPartnerTelegramApi, TransactionPartnerUser]] = None
    else:
        actual_instance: Any = None
    any_of_schemas: Set[str] = { "TransactionPartnerAffiliateProgram", "TransactionPartnerChat", "TransactionPartnerFragment", "TransactionPartnerOther", "TransactionPartnerTelegramAds", "TransactionPartnerTelegramApi", "TransactionPartnerUser" }

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
        instance = TransactionPartner.model_construct()
        error_messages = []
        # validate data type: TransactionPartnerUser
        if not isinstance(v, TransactionPartnerUser):
            error_messages.append(f"Error! Input type `{type(v)}` is not `TransactionPartnerUser`")
        else:
            return v

        # validate data type: TransactionPartnerChat
        if not isinstance(v, TransactionPartnerChat):
            error_messages.append(f"Error! Input type `{type(v)}` is not `TransactionPartnerChat`")
        else:
            return v

        # validate data type: TransactionPartnerAffiliateProgram
        if not isinstance(v, TransactionPartnerAffiliateProgram):
            error_messages.append(f"Error! Input type `{type(v)}` is not `TransactionPartnerAffiliateProgram`")
        else:
            return v

        # validate data type: TransactionPartnerFragment
        if not isinstance(v, TransactionPartnerFragment):
            error_messages.append(f"Error! Input type `{type(v)}` is not `TransactionPartnerFragment`")
        else:
            return v

        # validate data type: TransactionPartnerTelegramAds
        if not isinstance(v, TransactionPartnerTelegramAds):
            error_messages.append(f"Error! Input type `{type(v)}` is not `TransactionPartnerTelegramAds`")
        else:
            return v

        # validate data type: TransactionPartnerTelegramApi
        if not isinstance(v, TransactionPartnerTelegramApi):
            error_messages.append(f"Error! Input type `{type(v)}` is not `TransactionPartnerTelegramApi`")
        else:
            return v

        # validate data type: TransactionPartnerOther
        if not isinstance(v, TransactionPartnerOther):
            error_messages.append(f"Error! Input type `{type(v)}` is not `TransactionPartnerOther`")
        else:
            return v

        if error_messages:
            # no match
            raise ValueError("No match found when setting the actual_instance in TransactionPartner with anyOf schemas: TransactionPartnerAffiliateProgram, TransactionPartnerChat, TransactionPartnerFragment, TransactionPartnerOther, TransactionPartnerTelegramAds, TransactionPartnerTelegramApi, TransactionPartnerUser. Details: " + ", ".join(error_messages))
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
        # anyof_schema_1_validator: Optional[TransactionPartnerUser] = None
        try:
            instance.actual_instance = TransactionPartnerUser.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_2_validator: Optional[TransactionPartnerChat] = None
        try:
            instance.actual_instance = TransactionPartnerChat.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_3_validator: Optional[TransactionPartnerAffiliateProgram] = None
        try:
            instance.actual_instance = TransactionPartnerAffiliateProgram.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_4_validator: Optional[TransactionPartnerFragment] = None
        try:
            instance.actual_instance = TransactionPartnerFragment.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_5_validator: Optional[TransactionPartnerTelegramAds] = None
        try:
            instance.actual_instance = TransactionPartnerTelegramAds.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_6_validator: Optional[TransactionPartnerTelegramApi] = None
        try:
            instance.actual_instance = TransactionPartnerTelegramApi.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_7_validator: Optional[TransactionPartnerOther] = None
        try:
            instance.actual_instance = TransactionPartnerOther.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))

        if error_messages:
            # no match
            raise ValueError("No match found when deserializing the JSON string into TransactionPartner with anyOf schemas: TransactionPartnerAffiliateProgram, TransactionPartnerChat, TransactionPartnerFragment, TransactionPartnerOther, TransactionPartnerTelegramAds, TransactionPartnerTelegramApi, TransactionPartnerUser. Details: " + ", ".join(error_messages))
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

    def to_dict(self) -> Optional[Union[Dict[str, Any], TransactionPartnerAffiliateProgram, TransactionPartnerChat, TransactionPartnerFragment, TransactionPartnerOther, TransactionPartnerTelegramAds, TransactionPartnerTelegramApi, TransactionPartnerUser]]:
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


