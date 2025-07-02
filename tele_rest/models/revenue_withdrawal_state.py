# coding: utf-8

"""
Telegram Bot API - REST API Client
The Bot API is an HTTP-based interface created for developers keen on building bots for Telegram. To learn how to create and set up a bot, please consult our Introduction to Bots and Bot FAQ.

## Metadata

- **Copyright**: Copyright (c) 2025 Qntx
- **Author**: ΣX <gitctrlx@gmail.com>
- **Version**: 9.0.0
- **Modified**: 2025-07-02T07:03:17.088738557Z[Etc/UTC]
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
from tele_rest.models.revenue_withdrawal_state_failed import RevenueWithdrawalStateFailed
from tele_rest.models.revenue_withdrawal_state_pending import RevenueWithdrawalStatePending
from tele_rest.models.revenue_withdrawal_state_succeeded import RevenueWithdrawalStateSucceeded
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

REVENUEWITHDRAWALSTATE_ONE_OF_SCHEMAS = ["RevenueWithdrawalStateFailed", "RevenueWithdrawalStatePending", "RevenueWithdrawalStateSucceeded"]

class RevenueWithdrawalState(BaseModel):
    """
    This object describes the state of a revenue withdrawal operation. Currently, it can be one of  * [RevenueWithdrawalStatePending](https://core.telegram.org/bots/api/#revenuewithdrawalstatepending) * [RevenueWithdrawalStateSucceeded](https://core.telegram.org/bots/api/#revenuewithdrawalstatesucceeded) * [RevenueWithdrawalStateFailed](https://core.telegram.org/bots/api/#revenuewithdrawalstatefailed)
    """
    # data type: RevenueWithdrawalStatePending
    oneof_schema_1_validator: Optional[RevenueWithdrawalStatePending] = None
    # data type: RevenueWithdrawalStateSucceeded
    oneof_schema_2_validator: Optional[RevenueWithdrawalStateSucceeded] = None
    # data type: RevenueWithdrawalStateFailed
    oneof_schema_3_validator: Optional[RevenueWithdrawalStateFailed] = None
    actual_instance: Optional[Union[RevenueWithdrawalStateFailed, RevenueWithdrawalStatePending, RevenueWithdrawalStateSucceeded]] = None
    one_of_schemas: Set[str] = { "RevenueWithdrawalStateFailed", "RevenueWithdrawalStatePending", "RevenueWithdrawalStateSucceeded" }

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
        instance = RevenueWithdrawalState.model_construct()
        error_messages = []
        match = 0
        # validate data type: RevenueWithdrawalStatePending
        if not isinstance(v, RevenueWithdrawalStatePending):
            error_messages.append(f"Error! Input type `{type(v)}` is not `RevenueWithdrawalStatePending`")
        else:
            match += 1
        # validate data type: RevenueWithdrawalStateSucceeded
        if not isinstance(v, RevenueWithdrawalStateSucceeded):
            error_messages.append(f"Error! Input type `{type(v)}` is not `RevenueWithdrawalStateSucceeded`")
        else:
            match += 1
        # validate data type: RevenueWithdrawalStateFailed
        if not isinstance(v, RevenueWithdrawalStateFailed):
            error_messages.append(f"Error! Input type `{type(v)}` is not `RevenueWithdrawalStateFailed`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in RevenueWithdrawalState with oneOf schemas: RevenueWithdrawalStateFailed, RevenueWithdrawalStatePending, RevenueWithdrawalStateSucceeded. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in RevenueWithdrawalState with oneOf schemas: RevenueWithdrawalStateFailed, RevenueWithdrawalStatePending, RevenueWithdrawalStateSucceeded. Details: " + ", ".join(error_messages))
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

        # deserialize data into RevenueWithdrawalStatePending
        try:
            instance.actual_instance = RevenueWithdrawalStatePending.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into RevenueWithdrawalStateSucceeded
        try:
            instance.actual_instance = RevenueWithdrawalStateSucceeded.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into RevenueWithdrawalStateFailed
        try:
            instance.actual_instance = RevenueWithdrawalStateFailed.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into RevenueWithdrawalState with oneOf schemas: RevenueWithdrawalStateFailed, RevenueWithdrawalStatePending, RevenueWithdrawalStateSucceeded. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into RevenueWithdrawalState with oneOf schemas: RevenueWithdrawalStateFailed, RevenueWithdrawalStatePending, RevenueWithdrawalStateSucceeded. Details: " + ", ".join(error_messages))
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

    def to_dict(self) -> Optional[Union[Dict[str, Any], RevenueWithdrawalStateFailed, RevenueWithdrawalStatePending, RevenueWithdrawalStateSucceeded]]:
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


