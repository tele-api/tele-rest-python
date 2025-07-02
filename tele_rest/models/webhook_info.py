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
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class WebhookInfo(BaseModel):
    """
    Describes the current status of a webhook.
    """ # noqa: E501
    url: StrictStr = Field(description="Webhook URL, may be empty if webhook is not set up")
    has_custom_certificate: StrictBool = Field(description="*True*, if a custom certificate was provided for webhook certificate checks")
    pending_update_count: StrictInt = Field(description="Number of updates awaiting delivery")
    ip_address: Optional[StrictStr] = Field(default=None, description="*Optional*. Currently used webhook IP address")
    last_error_date: Optional[StrictInt] = Field(default=None, description="*Optional*. Unix time for the most recent error that happened when trying to deliver an update via webhook")
    last_error_message: Optional[StrictStr] = Field(default=None, description="*Optional*. Error message in human-readable format for the most recent error that happened when trying to deliver an update via webhook")
    last_synchronization_error_date: Optional[StrictInt] = Field(default=None, description="*Optional*. Unix time of the most recent error that happened when trying to synchronize available updates with Telegram datacenters")
    max_connections: Optional[StrictInt] = Field(default=None, description="*Optional*. The maximum allowed number of simultaneous HTTPS connections to the webhook for update delivery")
    allowed_updates: Optional[List[StrictStr]] = Field(default=None, description="*Optional*. A list of update types the bot is subscribed to. Defaults to all update types except *chat\\_member*")
    __properties: ClassVar[List[str]] = ["url", "has_custom_certificate", "pending_update_count", "ip_address", "last_error_date", "last_error_message", "last_synchronization_error_date", "max_connections", "allowed_updates"]

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
        """Create an instance of WebhookInfo from a JSON string"""
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
        """Create an instance of WebhookInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in WebhookInfo) in the input: " + _key)

        _obj = cls.model_validate({
            "url": obj.get("url"),
            "has_custom_certificate": obj.get("has_custom_certificate"),
            "pending_update_count": obj.get("pending_update_count"),
            "ip_address": obj.get("ip_address"),
            "last_error_date": obj.get("last_error_date"),
            "last_error_message": obj.get("last_error_message"),
            "last_synchronization_error_date": obj.get("last_synchronization_error_date"),
            "max_connections": obj.get("max_connections"),
            "allowed_updates": obj.get("allowed_updates")
        })
        return _obj


