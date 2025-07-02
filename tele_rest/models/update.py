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

from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from tele_rest.models.business_connection import BusinessConnection
from tele_rest.models.business_messages_deleted import BusinessMessagesDeleted
from tele_rest.models.callback_query import CallbackQuery
from tele_rest.models.chat_boost_removed import ChatBoostRemoved
from tele_rest.models.chat_boost_updated import ChatBoostUpdated
from tele_rest.models.chat_join_request import ChatJoinRequest
from tele_rest.models.chat_member_updated import ChatMemberUpdated
from tele_rest.models.chosen_inline_result import ChosenInlineResult
from tele_rest.models.inline_query import InlineQuery
from tele_rest.models.message import Message
from tele_rest.models.message_reaction_count_updated import MessageReactionCountUpdated
from tele_rest.models.message_reaction_updated import MessageReactionUpdated
from tele_rest.models.paid_media_purchased import PaidMediaPurchased
from tele_rest.models.poll import Poll
from tele_rest.models.poll_answer import PollAnswer
from tele_rest.models.pre_checkout_query import PreCheckoutQuery
from tele_rest.models.shipping_query import ShippingQuery
from typing import Optional, Set
from typing_extensions import Self

class Update(BaseModel):
    """
    This [object](https://core.telegram.org/bots/api/#available-types) represents an incoming update.   At most **one** of the optional parameters can be present in any given update.
    """ # noqa: E501
    update_id: StrictInt = Field(description="The update's unique identifier. Update identifiers start from a certain positive number and increase sequentially. This identifier becomes especially handy if you're using [webhooks](https://core.telegram.org/bots/api/#setwebhook), since it allows you to ignore repeated updates or to restore the correct update sequence, should they get out of order. If there are no new updates for at least a week, then identifier of the next update will be chosen randomly instead of sequentially.")
    message: Optional[Message] = None
    edited_message: Optional[Message] = None
    channel_post: Optional[Message] = None
    edited_channel_post: Optional[Message] = None
    business_connection: Optional[BusinessConnection] = None
    business_message: Optional[Message] = None
    edited_business_message: Optional[Message] = None
    deleted_business_messages: Optional[BusinessMessagesDeleted] = None
    message_reaction: Optional[MessageReactionUpdated] = None
    message_reaction_count: Optional[MessageReactionCountUpdated] = None
    inline_query: Optional[InlineQuery] = None
    chosen_inline_result: Optional[ChosenInlineResult] = None
    callback_query: Optional[CallbackQuery] = None
    shipping_query: Optional[ShippingQuery] = None
    pre_checkout_query: Optional[PreCheckoutQuery] = None
    purchased_paid_media: Optional[PaidMediaPurchased] = None
    poll: Optional[Poll] = None
    poll_answer: Optional[PollAnswer] = None
    my_chat_member: Optional[ChatMemberUpdated] = None
    chat_member: Optional[ChatMemberUpdated] = None
    chat_join_request: Optional[ChatJoinRequest] = None
    chat_boost: Optional[ChatBoostUpdated] = None
    removed_chat_boost: Optional[ChatBoostRemoved] = None
    __properties: ClassVar[List[str]] = ["update_id", "message", "edited_message", "channel_post", "edited_channel_post", "business_connection", "business_message", "edited_business_message", "deleted_business_messages", "message_reaction", "message_reaction_count", "inline_query", "chosen_inline_result", "callback_query", "shipping_query", "pre_checkout_query", "purchased_paid_media", "poll", "poll_answer", "my_chat_member", "chat_member", "chat_join_request", "chat_boost", "removed_chat_boost"]

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
        """Create an instance of Update from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of message
        if self.message:
            _dict['message'] = self.message.to_dict()
        # override the default output from pydantic by calling `to_dict()` of edited_message
        if self.edited_message:
            _dict['edited_message'] = self.edited_message.to_dict()
        # override the default output from pydantic by calling `to_dict()` of channel_post
        if self.channel_post:
            _dict['channel_post'] = self.channel_post.to_dict()
        # override the default output from pydantic by calling `to_dict()` of edited_channel_post
        if self.edited_channel_post:
            _dict['edited_channel_post'] = self.edited_channel_post.to_dict()
        # override the default output from pydantic by calling `to_dict()` of business_connection
        if self.business_connection:
            _dict['business_connection'] = self.business_connection.to_dict()
        # override the default output from pydantic by calling `to_dict()` of business_message
        if self.business_message:
            _dict['business_message'] = self.business_message.to_dict()
        # override the default output from pydantic by calling `to_dict()` of edited_business_message
        if self.edited_business_message:
            _dict['edited_business_message'] = self.edited_business_message.to_dict()
        # override the default output from pydantic by calling `to_dict()` of deleted_business_messages
        if self.deleted_business_messages:
            _dict['deleted_business_messages'] = self.deleted_business_messages.to_dict()
        # override the default output from pydantic by calling `to_dict()` of message_reaction
        if self.message_reaction:
            _dict['message_reaction'] = self.message_reaction.to_dict()
        # override the default output from pydantic by calling `to_dict()` of message_reaction_count
        if self.message_reaction_count:
            _dict['message_reaction_count'] = self.message_reaction_count.to_dict()
        # override the default output from pydantic by calling `to_dict()` of inline_query
        if self.inline_query:
            _dict['inline_query'] = self.inline_query.to_dict()
        # override the default output from pydantic by calling `to_dict()` of chosen_inline_result
        if self.chosen_inline_result:
            _dict['chosen_inline_result'] = self.chosen_inline_result.to_dict()
        # override the default output from pydantic by calling `to_dict()` of callback_query
        if self.callback_query:
            _dict['callback_query'] = self.callback_query.to_dict()
        # override the default output from pydantic by calling `to_dict()` of shipping_query
        if self.shipping_query:
            _dict['shipping_query'] = self.shipping_query.to_dict()
        # override the default output from pydantic by calling `to_dict()` of pre_checkout_query
        if self.pre_checkout_query:
            _dict['pre_checkout_query'] = self.pre_checkout_query.to_dict()
        # override the default output from pydantic by calling `to_dict()` of purchased_paid_media
        if self.purchased_paid_media:
            _dict['purchased_paid_media'] = self.purchased_paid_media.to_dict()
        # override the default output from pydantic by calling `to_dict()` of poll
        if self.poll:
            _dict['poll'] = self.poll.to_dict()
        # override the default output from pydantic by calling `to_dict()` of poll_answer
        if self.poll_answer:
            _dict['poll_answer'] = self.poll_answer.to_dict()
        # override the default output from pydantic by calling `to_dict()` of my_chat_member
        if self.my_chat_member:
            _dict['my_chat_member'] = self.my_chat_member.to_dict()
        # override the default output from pydantic by calling `to_dict()` of chat_member
        if self.chat_member:
            _dict['chat_member'] = self.chat_member.to_dict()
        # override the default output from pydantic by calling `to_dict()` of chat_join_request
        if self.chat_join_request:
            _dict['chat_join_request'] = self.chat_join_request.to_dict()
        # override the default output from pydantic by calling `to_dict()` of chat_boost
        if self.chat_boost:
            _dict['chat_boost'] = self.chat_boost.to_dict()
        # override the default output from pydantic by calling `to_dict()` of removed_chat_boost
        if self.removed_chat_boost:
            _dict['removed_chat_boost'] = self.removed_chat_boost.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Update from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in Update) in the input: " + _key)

        _obj = cls.model_validate({
            "update_id": obj.get("update_id"),
            "message": Message.from_dict(obj["message"]) if obj.get("message") is not None else None,
            "edited_message": Message.from_dict(obj["edited_message"]) if obj.get("edited_message") is not None else None,
            "channel_post": Message.from_dict(obj["channel_post"]) if obj.get("channel_post") is not None else None,
            "edited_channel_post": Message.from_dict(obj["edited_channel_post"]) if obj.get("edited_channel_post") is not None else None,
            "business_connection": BusinessConnection.from_dict(obj["business_connection"]) if obj.get("business_connection") is not None else None,
            "business_message": Message.from_dict(obj["business_message"]) if obj.get("business_message") is not None else None,
            "edited_business_message": Message.from_dict(obj["edited_business_message"]) if obj.get("edited_business_message") is not None else None,
            "deleted_business_messages": BusinessMessagesDeleted.from_dict(obj["deleted_business_messages"]) if obj.get("deleted_business_messages") is not None else None,
            "message_reaction": MessageReactionUpdated.from_dict(obj["message_reaction"]) if obj.get("message_reaction") is not None else None,
            "message_reaction_count": MessageReactionCountUpdated.from_dict(obj["message_reaction_count"]) if obj.get("message_reaction_count") is not None else None,
            "inline_query": InlineQuery.from_dict(obj["inline_query"]) if obj.get("inline_query") is not None else None,
            "chosen_inline_result": ChosenInlineResult.from_dict(obj["chosen_inline_result"]) if obj.get("chosen_inline_result") is not None else None,
            "callback_query": CallbackQuery.from_dict(obj["callback_query"]) if obj.get("callback_query") is not None else None,
            "shipping_query": ShippingQuery.from_dict(obj["shipping_query"]) if obj.get("shipping_query") is not None else None,
            "pre_checkout_query": PreCheckoutQuery.from_dict(obj["pre_checkout_query"]) if obj.get("pre_checkout_query") is not None else None,
            "purchased_paid_media": PaidMediaPurchased.from_dict(obj["purchased_paid_media"]) if obj.get("purchased_paid_media") is not None else None,
            "poll": Poll.from_dict(obj["poll"]) if obj.get("poll") is not None else None,
            "poll_answer": PollAnswer.from_dict(obj["poll_answer"]) if obj.get("poll_answer") is not None else None,
            "my_chat_member": ChatMemberUpdated.from_dict(obj["my_chat_member"]) if obj.get("my_chat_member") is not None else None,
            "chat_member": ChatMemberUpdated.from_dict(obj["chat_member"]) if obj.get("chat_member") is not None else None,
            "chat_join_request": ChatJoinRequest.from_dict(obj["chat_join_request"]) if obj.get("chat_join_request") is not None else None,
            "chat_boost": ChatBoostUpdated.from_dict(obj["chat_boost"]) if obj.get("chat_boost") is not None else None,
            "removed_chat_boost": ChatBoostRemoved.from_dict(obj["removed_chat_boost"]) if obj.get("removed_chat_boost") is not None else None
        })
        return _obj


