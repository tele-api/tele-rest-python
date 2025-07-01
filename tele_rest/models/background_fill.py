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
import json
import pprint
from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Any, List, Optional
from tele_rest.models.background_fill_freeform_gradient import BackgroundFillFreeformGradient
from tele_rest.models.background_fill_gradient import BackgroundFillGradient
from tele_rest.models.background_fill_solid import BackgroundFillSolid
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

BACKGROUNDFILL_ONE_OF_SCHEMAS = ["BackgroundFillFreeformGradient", "BackgroundFillGradient", "BackgroundFillSolid"]

class BackgroundFill(BaseModel):
    """
    This object describes the way a background is filled based on the selected colors. Currently, it can be one of  * [BackgroundFillSolid](https://core.telegram.org/bots/api/#backgroundfillsolid) * [BackgroundFillGradient](https://core.telegram.org/bots/api/#backgroundfillgradient) * [BackgroundFillFreeformGradient](https://core.telegram.org/bots/api/#backgroundfillfreeformgradient)
    """
    # data type: BackgroundFillSolid
    oneof_schema_1_validator: Optional[BackgroundFillSolid] = None
    # data type: BackgroundFillGradient
    oneof_schema_2_validator: Optional[BackgroundFillGradient] = None
    # data type: BackgroundFillFreeformGradient
    oneof_schema_3_validator: Optional[BackgroundFillFreeformGradient] = None
    actual_instance: Optional[Union[BackgroundFillFreeformGradient, BackgroundFillGradient, BackgroundFillSolid]] = None
    one_of_schemas: Set[str] = { "BackgroundFillFreeformGradient", "BackgroundFillGradient", "BackgroundFillSolid" }

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
        instance = BackgroundFill.model_construct()
        error_messages = []
        match = 0
        # validate data type: BackgroundFillSolid
        if not isinstance(v, BackgroundFillSolid):
            error_messages.append(f"Error! Input type `{type(v)}` is not `BackgroundFillSolid`")
        else:
            match += 1
        # validate data type: BackgroundFillGradient
        if not isinstance(v, BackgroundFillGradient):
            error_messages.append(f"Error! Input type `{type(v)}` is not `BackgroundFillGradient`")
        else:
            match += 1
        # validate data type: BackgroundFillFreeformGradient
        if not isinstance(v, BackgroundFillFreeformGradient):
            error_messages.append(f"Error! Input type `{type(v)}` is not `BackgroundFillFreeformGradient`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in BackgroundFill with oneOf schemas: BackgroundFillFreeformGradient, BackgroundFillGradient, BackgroundFillSolid. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in BackgroundFill with oneOf schemas: BackgroundFillFreeformGradient, BackgroundFillGradient, BackgroundFillSolid. Details: " + ", ".join(error_messages))
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

        # deserialize data into BackgroundFillSolid
        try:
            instance.actual_instance = BackgroundFillSolid.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into BackgroundFillGradient
        try:
            instance.actual_instance = BackgroundFillGradient.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into BackgroundFillFreeformGradient
        try:
            instance.actual_instance = BackgroundFillFreeformGradient.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into BackgroundFill with oneOf schemas: BackgroundFillFreeformGradient, BackgroundFillGradient, BackgroundFillSolid. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into BackgroundFill with oneOf schemas: BackgroundFillFreeformGradient, BackgroundFillGradient, BackgroundFillSolid. Details: " + ", ".join(error_messages))
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

    def to_dict(self) -> Optional[Union[Dict[str, Any], BackgroundFillFreeformGradient, BackgroundFillGradient, BackgroundFillSolid]]:
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


