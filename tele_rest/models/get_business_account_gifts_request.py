# coding: utf-8

"""
Telegram Bot API - REST API Client
The Bot API is an HTTP-based interface created for developers keen on building bots for Telegram. To learn how to create and set up a bot, please consult our Introduction to Bots and Bot FAQ.

## Metadata

- **Copyright**: Copyright (c) 2026 Qntx
- **Author**: ΣX <gitctrlx@gmail.com>
- **Version**: 9.3.0
- **Modified**: 2026-01-01T02:06:09.762570119Z[Etc/UTC]
- **Generator Version**: 7.18.0

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
from typing import Optional, Set
from typing_extensions import Self

class GetBusinessAccountGiftsRequest(BaseModel):
    """
    Request parameters for getBusinessAccountGifts
    """ # noqa: E501
    business_connection_id: StrictStr = Field(description="Unique identifier of the business connection")
    exclude_unsaved: Optional[StrictBool] = Field(default=None, description="Pass *True* to exclude gifts that aren't saved to the account's profile page")
    exclude_saved: Optional[StrictBool] = Field(default=None, description="Pass *True* to exclude gifts that are saved to the account's profile page")
    exclude_unlimited: Optional[StrictBool] = Field(default=None, description="Pass *True* to exclude gifts that can be purchased an unlimited number of times")
    exclude_limited_upgradable: Optional[StrictBool] = Field(default=None, description="Pass *True* to exclude gifts that can be purchased a limited number of times and can be upgraded to unique")
    exclude_limited_non_upgradable: Optional[StrictBool] = Field(default=None, description="Pass *True* to exclude gifts that can be purchased a limited number of times and can't be upgraded to unique")
    exclude_unique: Optional[StrictBool] = Field(default=None, description="Pass *True* to exclude unique gifts")
    exclude_from_blockchain: Optional[StrictBool] = Field(default=None, description="Pass *True* to exclude gifts that were assigned from the TON blockchain and can't be resold or transferred in Telegram")
    sort_by_price: Optional[StrictBool] = Field(default=None, description="Pass *True* to sort results by gift price instead of send date. Sorting is applied before pagination.")
    offset: Optional[StrictStr] = Field(default=None, description="Offset of the first entry to return as received from the previous request; use empty string to get the first chunk of results")
    limit: Optional[StrictInt] = Field(default=100, description="The maximum number of gifts to be returned; 1-100. Defaults to 100")
    __properties: ClassVar[List[str]] = ["business_connection_id", "exclude_unsaved", "exclude_saved", "exclude_unlimited", "exclude_limited_upgradable", "exclude_limited_non_upgradable", "exclude_unique", "exclude_from_blockchain", "sort_by_price", "offset", "limit"]

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
        """Create an instance of GetBusinessAccountGiftsRequest from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetBusinessAccountGiftsRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in GetBusinessAccountGiftsRequest) in the input: " + _key)

        _obj = cls.model_validate({
            "business_connection_id": obj.get("business_connection_id"),
            "exclude_unsaved": obj.get("exclude_unsaved"),
            "exclude_saved": obj.get("exclude_saved"),
            "exclude_unlimited": obj.get("exclude_unlimited"),
            "exclude_limited_upgradable": obj.get("exclude_limited_upgradable"),
            "exclude_limited_non_upgradable": obj.get("exclude_limited_non_upgradable"),
            "exclude_unique": obj.get("exclude_unique"),
            "exclude_from_blockchain": obj.get("exclude_from_blockchain"),
            "sort_by_price": obj.get("sort_by_price"),
            "offset": obj.get("offset"),
            "limit": obj.get("limit") if obj.get("limit") is not None else 100
        })
        return _obj


