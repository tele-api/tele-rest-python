# coding: utf-8

"""
Telegram Bot API - REST API Client
The Bot API is an HTTP-based interface created for developers keen on building bots for Telegram. To learn how to create and set up a bot, please consult our Introduction to Bots and Bot FAQ.

## Metadata

- **Copyright**: Copyright (c) 2025 Qntx
- **Author**: ΣX <gitctrlx@gmail.com>
- **Version**: 9.1.0
- **Modified**: 2025-07-05T02:41:43.458230827Z[Etc/UTC]
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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from tele_rest.models.message_entity import MessageEntity
from tele_rest.models.poll_option import PollOption
from typing import Optional, Set
from typing_extensions import Self

class Poll(BaseModel):
    """
    This object contains information about a poll.
    """ # noqa: E501
    id: StrictStr = Field(description="Unique poll identifier")
    question: Annotated[str, Field(min_length=1, strict=True, max_length=300)] = Field(description="Poll question, 1-300 characters")
    question_entities: Optional[List[MessageEntity]] = Field(default=None, description="*Optional*. Special entities that appear in the *question*. Currently, only custom emoji entities are allowed in poll questions")
    options: List[PollOption] = Field(description="List of poll options")
    total_voter_count: StrictInt = Field(description="Total number of users that voted in the poll")
    is_closed: StrictBool = Field(description="*True*, if the poll is closed")
    is_anonymous: StrictBool = Field(description="*True*, if the poll is anonymous")
    type: StrictStr = Field(description="Poll type, currently can be “regular” or “quiz”")
    allows_multiple_answers: StrictBool = Field(description="*True*, if the poll allows multiple answers")
    correct_option_id: Optional[StrictInt] = Field(default=None, description="*Optional*. 0-based identifier of the correct answer option. Available only for polls in the quiz mode, which are closed, or was sent (not forwarded) by the bot or to the private chat with the bot.")
    explanation: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=200)]] = Field(default=None, description="*Optional*. Text that is shown when a user chooses an incorrect answer or taps on the lamp icon in a quiz-style poll, 0-200 characters")
    explanation_entities: Optional[List[MessageEntity]] = Field(default=None, description="*Optional*. Special entities like usernames, URLs, bot commands, etc. that appear in the *explanation*")
    open_period: Optional[StrictInt] = Field(default=None, description="*Optional*. Amount of time in seconds the poll will be active after creation")
    close_date: Optional[StrictInt] = Field(default=None, description="*Optional*. Point in time (Unix timestamp) when the poll will be automatically closed")
    __properties: ClassVar[List[str]] = ["id", "question", "question_entities", "options", "total_voter_count", "is_closed", "is_anonymous", "type", "allows_multiple_answers", "correct_option_id", "explanation", "explanation_entities", "open_period", "close_date"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['regular', 'quiz']):
            raise ValueError("must be one of enum values ('regular', 'quiz')")
        return value

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
        """Create an instance of Poll from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in question_entities (list)
        _items = []
        if self.question_entities:
            for _item_question_entities in self.question_entities:
                if _item_question_entities:
                    _items.append(_item_question_entities.to_dict())
            _dict['question_entities'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in options (list)
        _items = []
        if self.options:
            for _item_options in self.options:
                if _item_options:
                    _items.append(_item_options.to_dict())
            _dict['options'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in explanation_entities (list)
        _items = []
        if self.explanation_entities:
            for _item_explanation_entities in self.explanation_entities:
                if _item_explanation_entities:
                    _items.append(_item_explanation_entities.to_dict())
            _dict['explanation_entities'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Poll from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in Poll) in the input: " + _key)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "question": obj.get("question"),
            "question_entities": [MessageEntity.from_dict(_item) for _item in obj["question_entities"]] if obj.get("question_entities") is not None else None,
            "options": [PollOption.from_dict(_item) for _item in obj["options"]] if obj.get("options") is not None else None,
            "total_voter_count": obj.get("total_voter_count"),
            "is_closed": obj.get("is_closed"),
            "is_anonymous": obj.get("is_anonymous"),
            "type": obj.get("type"),
            "allows_multiple_answers": obj.get("allows_multiple_answers"),
            "correct_option_id": obj.get("correct_option_id"),
            "explanation": obj.get("explanation"),
            "explanation_entities": [MessageEntity.from_dict(_item) for _item in obj["explanation_entities"]] if obj.get("explanation_entities") is not None else None,
            "open_period": obj.get("open_period"),
            "close_date": obj.get("close_date")
        })
        return _obj


