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
from tele_rest.models.story_area_type_link import StoryAreaTypeLink
from tele_rest.models.story_area_type_location import StoryAreaTypeLocation
from tele_rest.models.story_area_type_suggested_reaction import StoryAreaTypeSuggestedReaction
from tele_rest.models.story_area_type_unique_gift import StoryAreaTypeUniqueGift
from tele_rest.models.story_area_type_weather import StoryAreaTypeWeather
from typing import Union, Any, List, Set, TYPE_CHECKING, Optional, Dict
from typing_extensions import Literal, Self
from pydantic import Field

STORYAREATYPE_ANY_OF_SCHEMAS = ["StoryAreaTypeLink", "StoryAreaTypeLocation", "StoryAreaTypeSuggestedReaction", "StoryAreaTypeUniqueGift", "StoryAreaTypeWeather"]

class StoryAreaType(BaseModel):
    """
    Describes the type of a clickable area on a story. Currently, it can be one of  * [StoryAreaTypeLocation](https://core.telegram.org/bots/api/#storyareatypelocation) * [StoryAreaTypeSuggestedReaction](https://core.telegram.org/bots/api/#storyareatypesuggestedreaction) * [StoryAreaTypeLink](https://core.telegram.org/bots/api/#storyareatypelink) * [StoryAreaTypeWeather](https://core.telegram.org/bots/api/#storyareatypeweather) * [StoryAreaTypeUniqueGift](https://core.telegram.org/bots/api/#storyareatypeuniquegift)
    """

    # data type: StoryAreaTypeLocation
    anyof_schema_1_validator: Optional[StoryAreaTypeLocation] = None
    # data type: StoryAreaTypeSuggestedReaction
    anyof_schema_2_validator: Optional[StoryAreaTypeSuggestedReaction] = None
    # data type: StoryAreaTypeLink
    anyof_schema_3_validator: Optional[StoryAreaTypeLink] = None
    # data type: StoryAreaTypeWeather
    anyof_schema_4_validator: Optional[StoryAreaTypeWeather] = None
    # data type: StoryAreaTypeUniqueGift
    anyof_schema_5_validator: Optional[StoryAreaTypeUniqueGift] = None
    if TYPE_CHECKING:
        actual_instance: Optional[Union[StoryAreaTypeLink, StoryAreaTypeLocation, StoryAreaTypeSuggestedReaction, StoryAreaTypeUniqueGift, StoryAreaTypeWeather]] = None
    else:
        actual_instance: Any = None
    any_of_schemas: Set[str] = { "StoryAreaTypeLink", "StoryAreaTypeLocation", "StoryAreaTypeSuggestedReaction", "StoryAreaTypeUniqueGift", "StoryAreaTypeWeather" }

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
        instance = StoryAreaType.model_construct()
        error_messages = []
        # validate data type: StoryAreaTypeLocation
        if not isinstance(v, StoryAreaTypeLocation):
            error_messages.append(f"Error! Input type `{type(v)}` is not `StoryAreaTypeLocation`")
        else:
            return v

        # validate data type: StoryAreaTypeSuggestedReaction
        if not isinstance(v, StoryAreaTypeSuggestedReaction):
            error_messages.append(f"Error! Input type `{type(v)}` is not `StoryAreaTypeSuggestedReaction`")
        else:
            return v

        # validate data type: StoryAreaTypeLink
        if not isinstance(v, StoryAreaTypeLink):
            error_messages.append(f"Error! Input type `{type(v)}` is not `StoryAreaTypeLink`")
        else:
            return v

        # validate data type: StoryAreaTypeWeather
        if not isinstance(v, StoryAreaTypeWeather):
            error_messages.append(f"Error! Input type `{type(v)}` is not `StoryAreaTypeWeather`")
        else:
            return v

        # validate data type: StoryAreaTypeUniqueGift
        if not isinstance(v, StoryAreaTypeUniqueGift):
            error_messages.append(f"Error! Input type `{type(v)}` is not `StoryAreaTypeUniqueGift`")
        else:
            return v

        if error_messages:
            # no match
            raise ValueError("No match found when setting the actual_instance in StoryAreaType with anyOf schemas: StoryAreaTypeLink, StoryAreaTypeLocation, StoryAreaTypeSuggestedReaction, StoryAreaTypeUniqueGift, StoryAreaTypeWeather. Details: " + ", ".join(error_messages))
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
        # anyof_schema_1_validator: Optional[StoryAreaTypeLocation] = None
        try:
            instance.actual_instance = StoryAreaTypeLocation.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_2_validator: Optional[StoryAreaTypeSuggestedReaction] = None
        try:
            instance.actual_instance = StoryAreaTypeSuggestedReaction.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_3_validator: Optional[StoryAreaTypeLink] = None
        try:
            instance.actual_instance = StoryAreaTypeLink.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_4_validator: Optional[StoryAreaTypeWeather] = None
        try:
            instance.actual_instance = StoryAreaTypeWeather.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_5_validator: Optional[StoryAreaTypeUniqueGift] = None
        try:
            instance.actual_instance = StoryAreaTypeUniqueGift.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))

        if error_messages:
            # no match
            raise ValueError("No match found when deserializing the JSON string into StoryAreaType with anyOf schemas: StoryAreaTypeLink, StoryAreaTypeLocation, StoryAreaTypeSuggestedReaction, StoryAreaTypeUniqueGift, StoryAreaTypeWeather. Details: " + ", ".join(error_messages))
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

    def to_dict(self) -> Optional[Union[Dict[str, Any], StoryAreaTypeLink, StoryAreaTypeLocation, StoryAreaTypeSuggestedReaction, StoryAreaTypeUniqueGift, StoryAreaTypeWeather]]:
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


