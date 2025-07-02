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
from tele_rest.models.animation import Animation
from tele_rest.models.audio import Audio
from tele_rest.models.chat import Chat
from tele_rest.models.chat_background import ChatBackground
from tele_rest.models.chat_boost_added import ChatBoostAdded
from tele_rest.models.chat_shared import ChatShared
from tele_rest.models.contact import Contact
from tele_rest.models.dice import Dice
from tele_rest.models.document import Document
from tele_rest.models.external_reply_info import ExternalReplyInfo
from tele_rest.models.forum_topic_created import ForumTopicCreated
from tele_rest.models.forum_topic_edited import ForumTopicEdited
from tele_rest.models.game import Game
from tele_rest.models.gift_info import GiftInfo
from tele_rest.models.giveaway import Giveaway
from tele_rest.models.giveaway_created import GiveawayCreated
from tele_rest.models.giveaway_winners import GiveawayWinners
from tele_rest.models.inline_keyboard_markup import InlineKeyboardMarkup
from tele_rest.models.invoice import Invoice
from tele_rest.models.link_preview_options import LinkPreviewOptions
from tele_rest.models.location import Location
from tele_rest.models.message_auto_delete_timer_changed import MessageAutoDeleteTimerChanged
from tele_rest.models.message_entity import MessageEntity
from tele_rest.models.message_origin import MessageOrigin
from tele_rest.models.paid_media_info import PaidMediaInfo
from tele_rest.models.paid_message_price_changed import PaidMessagePriceChanged
from tele_rest.models.passport_data import PassportData
from tele_rest.models.photo_size import PhotoSize
from tele_rest.models.poll import Poll
from tele_rest.models.proximity_alert_triggered import ProximityAlertTriggered
from tele_rest.models.refunded_payment import RefundedPayment
from tele_rest.models.sticker import Sticker
from tele_rest.models.story import Story
from tele_rest.models.successful_payment import SuccessfulPayment
from tele_rest.models.text_quote import TextQuote
from tele_rest.models.unique_gift_info import UniqueGiftInfo
from tele_rest.models.user import User
from tele_rest.models.users_shared import UsersShared
from tele_rest.models.venue import Venue
from tele_rest.models.video import Video
from tele_rest.models.video_chat_ended import VideoChatEnded
from tele_rest.models.video_chat_participants_invited import VideoChatParticipantsInvited
from tele_rest.models.video_chat_scheduled import VideoChatScheduled
from tele_rest.models.video_note import VideoNote
from tele_rest.models.voice import Voice
from tele_rest.models.web_app_data import WebAppData
from tele_rest.models.write_access_allowed import WriteAccessAllowed
from typing import Optional, Set
from typing_extensions import Self

class Message(BaseModel):
    """
    This object represents a message.
    """ # noqa: E501
    message_id: StrictInt = Field(description="Unique message identifier inside this chat. In specific instances (e.g., message containing a video sent to a big chat), the server might automatically schedule a message instead of sending it immediately. In such cases, this field will be 0 and the relevant message will be unusable until it is actually sent")
    message_thread_id: Optional[StrictInt] = Field(default=None, description="*Optional*. Unique identifier of a message thread to which the message belongs; for supergroups only")
    var_from: Optional[User] = Field(default=None, alias="from")
    sender_chat: Optional[Chat] = None
    sender_boost_count: Optional[StrictInt] = Field(default=None, description="*Optional*. If the sender of the message boosted the chat, the number of boosts added by the user")
    sender_business_bot: Optional[User] = None
    var_date: StrictInt = Field(description="Date the message was sent in Unix time. It is always a positive number, representing a valid date.", alias="date")
    business_connection_id: Optional[StrictStr] = Field(default=None, description="*Optional*. Unique identifier of the business connection from which the message was received. If non-empty, the message belongs to a chat of the corresponding business account that is independent from any potential bot chat which might share the same identifier.")
    chat: Chat
    forward_origin: Optional[MessageOrigin] = None
    is_topic_message: Optional[StrictBool] = Field(default=True, description="*Optional*. *True*, if the message is sent to a forum topic")
    is_automatic_forward: Optional[StrictBool] = Field(default=True, description="*Optional*. *True*, if the message is a channel post that was automatically forwarded to the connected discussion group")
    reply_to_message: Optional[Message] = None
    external_reply: Optional[ExternalReplyInfo] = None
    quote: Optional[TextQuote] = None
    reply_to_story: Optional[Story] = None
    via_bot: Optional[User] = None
    edit_date: Optional[StrictInt] = Field(default=None, description="*Optional*. Date the message was last edited in Unix time")
    has_protected_content: Optional[StrictBool] = Field(default=True, description="*Optional*. *True*, if the message can't be forwarded")
    is_from_offline: Optional[StrictBool] = Field(default=True, description="*Optional*. True, if the message was sent by an implicit action, for example, as an away or a greeting business message, or as a scheduled message")
    media_group_id: Optional[StrictStr] = Field(default=None, description="*Optional*. The unique identifier of a media message group this message belongs to")
    author_signature: Optional[StrictStr] = Field(default=None, description="*Optional*. Signature of the post author for messages in channels, or the custom title of an anonymous group administrator")
    paid_star_count: Optional[StrictInt] = Field(default=None, description="*Optional*. The number of Telegram Stars that were paid by the sender of the message to send it")
    text: Optional[StrictStr] = Field(default=None, description="*Optional*. For text messages, the actual UTF-8 text of the message")
    entities: Optional[List[MessageEntity]] = Field(default=None, description="*Optional*. For text messages, special entities like usernames, URLs, bot commands, etc. that appear in the text")
    link_preview_options: Optional[LinkPreviewOptions] = None
    effect_id: Optional[StrictStr] = Field(default=None, description="*Optional*. Unique identifier of the message effect added to the message")
    animation: Optional[Animation] = None
    audio: Optional[Audio] = None
    document: Optional[Document] = None
    paid_media: Optional[PaidMediaInfo] = None
    photo: Optional[List[PhotoSize]] = Field(default=None, description="*Optional*. Message is a photo, available sizes of the photo")
    sticker: Optional[Sticker] = None
    story: Optional[Story] = None
    video: Optional[Video] = None
    video_note: Optional[VideoNote] = None
    voice: Optional[Voice] = None
    caption: Optional[StrictStr] = Field(default=None, description="*Optional*. Caption for the animation, audio, document, paid media, photo, video or voice")
    caption_entities: Optional[List[MessageEntity]] = Field(default=None, description="*Optional*. For messages with a caption, special entities like usernames, URLs, bot commands, etc. that appear in the caption")
    show_caption_above_media: Optional[StrictBool] = Field(default=True, description="*Optional*. True, if the caption must be shown above the message media")
    has_media_spoiler: Optional[StrictBool] = Field(default=True, description="*Optional*. *True*, if the message media is covered by a spoiler animation")
    contact: Optional[Contact] = None
    dice: Optional[Dice] = None
    game: Optional[Game] = None
    poll: Optional[Poll] = None
    venue: Optional[Venue] = None
    location: Optional[Location] = None
    new_chat_members: Optional[List[User]] = Field(default=None, description="*Optional*. New members that were added to the group or supergroup and information about them (the bot itself may be one of these members)")
    left_chat_member: Optional[User] = None
    new_chat_title: Optional[StrictStr] = Field(default=None, description="*Optional*. A chat title was changed to this value")
    new_chat_photo: Optional[List[PhotoSize]] = Field(default=None, description="*Optional*. A chat photo was change to this value")
    delete_chat_photo: Optional[StrictBool] = Field(default=True, description="*Optional*. Service message: the chat photo was deleted")
    group_chat_created: Optional[StrictBool] = Field(default=True, description="*Optional*. Service message: the group has been created")
    supergroup_chat_created: Optional[StrictBool] = Field(default=True, description="*Optional*. Service message: the supergroup has been created. This field can't be received in a message coming through updates, because bot can't be a member of a supergroup when it is created. It can only be found in reply\\_to\\_message if someone replies to a very first message in a directly created supergroup.")
    channel_chat_created: Optional[StrictBool] = Field(default=True, description="*Optional*. Service message: the channel has been created. This field can't be received in a message coming through updates, because bot can't be a member of a channel when it is created. It can only be found in reply\\_to\\_message if someone replies to a very first message in a channel.")
    message_auto_delete_timer_changed: Optional[MessageAutoDeleteTimerChanged] = None
    migrate_to_chat_id: Optional[StrictInt] = Field(default=None, description="*Optional*. The group has been migrated to a supergroup with the specified identifier. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this identifier.")
    migrate_from_chat_id: Optional[StrictInt] = Field(default=None, description="*Optional*. The supergroup has been migrated from a group with the specified identifier. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this identifier.")
    pinned_message: Optional[MaybeInaccessibleMessage] = None
    invoice: Optional[Invoice] = None
    successful_payment: Optional[SuccessfulPayment] = None
    refunded_payment: Optional[RefundedPayment] = None
    users_shared: Optional[UsersShared] = None
    chat_shared: Optional[ChatShared] = None
    gift: Optional[GiftInfo] = None
    unique_gift: Optional[UniqueGiftInfo] = None
    connected_website: Optional[StrictStr] = Field(default=None, description="*Optional*. The domain name of the website on which the user has logged in. [More about Telegram Login »](https://core.telegram.org/widgets/login)")
    write_access_allowed: Optional[WriteAccessAllowed] = None
    passport_data: Optional[PassportData] = None
    proximity_alert_triggered: Optional[ProximityAlertTriggered] = None
    boost_added: Optional[ChatBoostAdded] = None
    chat_background_set: Optional[ChatBackground] = None
    forum_topic_created: Optional[ForumTopicCreated] = None
    forum_topic_edited: Optional[ForumTopicEdited] = None
    forum_topic_closed: Optional[Any] = None
    forum_topic_reopened: Optional[Any] = None
    general_forum_topic_hidden: Optional[Any] = None
    general_forum_topic_unhidden: Optional[Any] = None
    giveaway_created: Optional[GiveawayCreated] = None
    giveaway: Optional[Giveaway] = None
    giveaway_winners: Optional[GiveawayWinners] = None
    giveaway_completed: Optional[GiveawayCompleted] = None
    paid_message_price_changed: Optional[PaidMessagePriceChanged] = None
    video_chat_scheduled: Optional[VideoChatScheduled] = None
    video_chat_started: Optional[Any] = None
    video_chat_ended: Optional[VideoChatEnded] = None
    video_chat_participants_invited: Optional[VideoChatParticipantsInvited] = None
    web_app_data: Optional[WebAppData] = None
    reply_markup: Optional[InlineKeyboardMarkup] = None
    __properties: ClassVar[List[str]] = ["message_id", "message_thread_id", "from", "sender_chat", "sender_boost_count", "sender_business_bot", "date", "business_connection_id", "chat", "forward_origin", "is_topic_message", "is_automatic_forward", "reply_to_message", "external_reply", "quote", "reply_to_story", "via_bot", "edit_date", "has_protected_content", "is_from_offline", "media_group_id", "author_signature", "paid_star_count", "text", "entities", "link_preview_options", "effect_id", "animation", "audio", "document", "paid_media", "photo", "sticker", "story", "video", "video_note", "voice", "caption", "caption_entities", "show_caption_above_media", "has_media_spoiler", "contact", "dice", "game", "poll", "venue", "location", "new_chat_members", "left_chat_member", "new_chat_title", "new_chat_photo", "delete_chat_photo", "group_chat_created", "supergroup_chat_created", "channel_chat_created", "message_auto_delete_timer_changed", "migrate_to_chat_id", "migrate_from_chat_id", "pinned_message", "invoice", "successful_payment", "refunded_payment", "users_shared", "chat_shared", "gift", "unique_gift", "connected_website", "write_access_allowed", "passport_data", "proximity_alert_triggered", "boost_added", "chat_background_set", "forum_topic_created", "forum_topic_edited", "forum_topic_closed", "forum_topic_reopened", "general_forum_topic_hidden", "general_forum_topic_unhidden", "giveaway_created", "giveaway", "giveaway_winners", "giveaway_completed", "paid_message_price_changed", "video_chat_scheduled", "video_chat_started", "video_chat_ended", "video_chat_participants_invited", "web_app_data", "reply_markup"]

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
        """Create an instance of Message from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of var_from
        if self.var_from:
            _dict['from'] = self.var_from.to_dict()
        # override the default output from pydantic by calling `to_dict()` of sender_chat
        if self.sender_chat:
            _dict['sender_chat'] = self.sender_chat.to_dict()
        # override the default output from pydantic by calling `to_dict()` of sender_business_bot
        if self.sender_business_bot:
            _dict['sender_business_bot'] = self.sender_business_bot.to_dict()
        # override the default output from pydantic by calling `to_dict()` of chat
        if self.chat:
            _dict['chat'] = self.chat.to_dict()
        # override the default output from pydantic by calling `to_dict()` of forward_origin
        if self.forward_origin:
            _dict['forward_origin'] = self.forward_origin.to_dict()
        # override the default output from pydantic by calling `to_dict()` of reply_to_message
        if self.reply_to_message:
            _dict['reply_to_message'] = self.reply_to_message.to_dict()
        # override the default output from pydantic by calling `to_dict()` of external_reply
        if self.external_reply:
            _dict['external_reply'] = self.external_reply.to_dict()
        # override the default output from pydantic by calling `to_dict()` of quote
        if self.quote:
            _dict['quote'] = self.quote.to_dict()
        # override the default output from pydantic by calling `to_dict()` of reply_to_story
        if self.reply_to_story:
            _dict['reply_to_story'] = self.reply_to_story.to_dict()
        # override the default output from pydantic by calling `to_dict()` of via_bot
        if self.via_bot:
            _dict['via_bot'] = self.via_bot.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in entities (list)
        _items = []
        if self.entities:
            for _item_entities in self.entities:
                if _item_entities:
                    _items.append(_item_entities.to_dict())
            _dict['entities'] = _items
        # override the default output from pydantic by calling `to_dict()` of link_preview_options
        if self.link_preview_options:
            _dict['link_preview_options'] = self.link_preview_options.to_dict()
        # override the default output from pydantic by calling `to_dict()` of animation
        if self.animation:
            _dict['animation'] = self.animation.to_dict()
        # override the default output from pydantic by calling `to_dict()` of audio
        if self.audio:
            _dict['audio'] = self.audio.to_dict()
        # override the default output from pydantic by calling `to_dict()` of document
        if self.document:
            _dict['document'] = self.document.to_dict()
        # override the default output from pydantic by calling `to_dict()` of paid_media
        if self.paid_media:
            _dict['paid_media'] = self.paid_media.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in photo (list)
        _items = []
        if self.photo:
            for _item_photo in self.photo:
                if _item_photo:
                    _items.append(_item_photo.to_dict())
            _dict['photo'] = _items
        # override the default output from pydantic by calling `to_dict()` of sticker
        if self.sticker:
            _dict['sticker'] = self.sticker.to_dict()
        # override the default output from pydantic by calling `to_dict()` of story
        if self.story:
            _dict['story'] = self.story.to_dict()
        # override the default output from pydantic by calling `to_dict()` of video
        if self.video:
            _dict['video'] = self.video.to_dict()
        # override the default output from pydantic by calling `to_dict()` of video_note
        if self.video_note:
            _dict['video_note'] = self.video_note.to_dict()
        # override the default output from pydantic by calling `to_dict()` of voice
        if self.voice:
            _dict['voice'] = self.voice.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in caption_entities (list)
        _items = []
        if self.caption_entities:
            for _item_caption_entities in self.caption_entities:
                if _item_caption_entities:
                    _items.append(_item_caption_entities.to_dict())
            _dict['caption_entities'] = _items
        # override the default output from pydantic by calling `to_dict()` of contact
        if self.contact:
            _dict['contact'] = self.contact.to_dict()
        # override the default output from pydantic by calling `to_dict()` of dice
        if self.dice:
            _dict['dice'] = self.dice.to_dict()
        # override the default output from pydantic by calling `to_dict()` of game
        if self.game:
            _dict['game'] = self.game.to_dict()
        # override the default output from pydantic by calling `to_dict()` of poll
        if self.poll:
            _dict['poll'] = self.poll.to_dict()
        # override the default output from pydantic by calling `to_dict()` of venue
        if self.venue:
            _dict['venue'] = self.venue.to_dict()
        # override the default output from pydantic by calling `to_dict()` of location
        if self.location:
            _dict['location'] = self.location.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in new_chat_members (list)
        _items = []
        if self.new_chat_members:
            for _item_new_chat_members in self.new_chat_members:
                if _item_new_chat_members:
                    _items.append(_item_new_chat_members.to_dict())
            _dict['new_chat_members'] = _items
        # override the default output from pydantic by calling `to_dict()` of left_chat_member
        if self.left_chat_member:
            _dict['left_chat_member'] = self.left_chat_member.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in new_chat_photo (list)
        _items = []
        if self.new_chat_photo:
            for _item_new_chat_photo in self.new_chat_photo:
                if _item_new_chat_photo:
                    _items.append(_item_new_chat_photo.to_dict())
            _dict['new_chat_photo'] = _items
        # override the default output from pydantic by calling `to_dict()` of message_auto_delete_timer_changed
        if self.message_auto_delete_timer_changed:
            _dict['message_auto_delete_timer_changed'] = self.message_auto_delete_timer_changed.to_dict()
        # override the default output from pydantic by calling `to_dict()` of pinned_message
        if self.pinned_message:
            _dict['pinned_message'] = self.pinned_message.to_dict()
        # override the default output from pydantic by calling `to_dict()` of invoice
        if self.invoice:
            _dict['invoice'] = self.invoice.to_dict()
        # override the default output from pydantic by calling `to_dict()` of successful_payment
        if self.successful_payment:
            _dict['successful_payment'] = self.successful_payment.to_dict()
        # override the default output from pydantic by calling `to_dict()` of refunded_payment
        if self.refunded_payment:
            _dict['refunded_payment'] = self.refunded_payment.to_dict()
        # override the default output from pydantic by calling `to_dict()` of users_shared
        if self.users_shared:
            _dict['users_shared'] = self.users_shared.to_dict()
        # override the default output from pydantic by calling `to_dict()` of chat_shared
        if self.chat_shared:
            _dict['chat_shared'] = self.chat_shared.to_dict()
        # override the default output from pydantic by calling `to_dict()` of gift
        if self.gift:
            _dict['gift'] = self.gift.to_dict()
        # override the default output from pydantic by calling `to_dict()` of unique_gift
        if self.unique_gift:
            _dict['unique_gift'] = self.unique_gift.to_dict()
        # override the default output from pydantic by calling `to_dict()` of write_access_allowed
        if self.write_access_allowed:
            _dict['write_access_allowed'] = self.write_access_allowed.to_dict()
        # override the default output from pydantic by calling `to_dict()` of passport_data
        if self.passport_data:
            _dict['passport_data'] = self.passport_data.to_dict()
        # override the default output from pydantic by calling `to_dict()` of proximity_alert_triggered
        if self.proximity_alert_triggered:
            _dict['proximity_alert_triggered'] = self.proximity_alert_triggered.to_dict()
        # override the default output from pydantic by calling `to_dict()` of boost_added
        if self.boost_added:
            _dict['boost_added'] = self.boost_added.to_dict()
        # override the default output from pydantic by calling `to_dict()` of chat_background_set
        if self.chat_background_set:
            _dict['chat_background_set'] = self.chat_background_set.to_dict()
        # override the default output from pydantic by calling `to_dict()` of forum_topic_created
        if self.forum_topic_created:
            _dict['forum_topic_created'] = self.forum_topic_created.to_dict()
        # override the default output from pydantic by calling `to_dict()` of forum_topic_edited
        if self.forum_topic_edited:
            _dict['forum_topic_edited'] = self.forum_topic_edited.to_dict()
        # override the default output from pydantic by calling `to_dict()` of giveaway_created
        if self.giveaway_created:
            _dict['giveaway_created'] = self.giveaway_created.to_dict()
        # override the default output from pydantic by calling `to_dict()` of giveaway
        if self.giveaway:
            _dict['giveaway'] = self.giveaway.to_dict()
        # override the default output from pydantic by calling `to_dict()` of giveaway_winners
        if self.giveaway_winners:
            _dict['giveaway_winners'] = self.giveaway_winners.to_dict()
        # override the default output from pydantic by calling `to_dict()` of giveaway_completed
        if self.giveaway_completed:
            _dict['giveaway_completed'] = self.giveaway_completed.to_dict()
        # override the default output from pydantic by calling `to_dict()` of paid_message_price_changed
        if self.paid_message_price_changed:
            _dict['paid_message_price_changed'] = self.paid_message_price_changed.to_dict()
        # override the default output from pydantic by calling `to_dict()` of video_chat_scheduled
        if self.video_chat_scheduled:
            _dict['video_chat_scheduled'] = self.video_chat_scheduled.to_dict()
        # override the default output from pydantic by calling `to_dict()` of video_chat_ended
        if self.video_chat_ended:
            _dict['video_chat_ended'] = self.video_chat_ended.to_dict()
        # override the default output from pydantic by calling `to_dict()` of video_chat_participants_invited
        if self.video_chat_participants_invited:
            _dict['video_chat_participants_invited'] = self.video_chat_participants_invited.to_dict()
        # override the default output from pydantic by calling `to_dict()` of web_app_data
        if self.web_app_data:
            _dict['web_app_data'] = self.web_app_data.to_dict()
        # override the default output from pydantic by calling `to_dict()` of reply_markup
        if self.reply_markup:
            _dict['reply_markup'] = self.reply_markup.to_dict()
        # set to None if forum_topic_closed (nullable) is None
        # and model_fields_set contains the field
        if self.forum_topic_closed is None and "forum_topic_closed" in self.model_fields_set:
            _dict['forum_topic_closed'] = None

        # set to None if forum_topic_reopened (nullable) is None
        # and model_fields_set contains the field
        if self.forum_topic_reopened is None and "forum_topic_reopened" in self.model_fields_set:
            _dict['forum_topic_reopened'] = None

        # set to None if general_forum_topic_hidden (nullable) is None
        # and model_fields_set contains the field
        if self.general_forum_topic_hidden is None and "general_forum_topic_hidden" in self.model_fields_set:
            _dict['general_forum_topic_hidden'] = None

        # set to None if general_forum_topic_unhidden (nullable) is None
        # and model_fields_set contains the field
        if self.general_forum_topic_unhidden is None and "general_forum_topic_unhidden" in self.model_fields_set:
            _dict['general_forum_topic_unhidden'] = None

        # set to None if video_chat_started (nullable) is None
        # and model_fields_set contains the field
        if self.video_chat_started is None and "video_chat_started" in self.model_fields_set:
            _dict['video_chat_started'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Message from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in Message) in the input: " + _key)

        _obj = cls.model_validate({
            "message_id": obj.get("message_id"),
            "message_thread_id": obj.get("message_thread_id"),
            "from": User.from_dict(obj["from"]) if obj.get("from") is not None else None,
            "sender_chat": Chat.from_dict(obj["sender_chat"]) if obj.get("sender_chat") is not None else None,
            "sender_boost_count": obj.get("sender_boost_count"),
            "sender_business_bot": User.from_dict(obj["sender_business_bot"]) if obj.get("sender_business_bot") is not None else None,
            "date": obj.get("date"),
            "business_connection_id": obj.get("business_connection_id"),
            "chat": Chat.from_dict(obj["chat"]) if obj.get("chat") is not None else None,
            "forward_origin": MessageOrigin.from_dict(obj["forward_origin"]) if obj.get("forward_origin") is not None else None,
            "is_topic_message": obj.get("is_topic_message") if obj.get("is_topic_message") is not None else True,
            "is_automatic_forward": obj.get("is_automatic_forward") if obj.get("is_automatic_forward") is not None else True,
            "reply_to_message": Message.from_dict(obj["reply_to_message"]) if obj.get("reply_to_message") is not None else None,
            "external_reply": ExternalReplyInfo.from_dict(obj["external_reply"]) if obj.get("external_reply") is not None else None,
            "quote": TextQuote.from_dict(obj["quote"]) if obj.get("quote") is not None else None,
            "reply_to_story": Story.from_dict(obj["reply_to_story"]) if obj.get("reply_to_story") is not None else None,
            "via_bot": User.from_dict(obj["via_bot"]) if obj.get("via_bot") is not None else None,
            "edit_date": obj.get("edit_date"),
            "has_protected_content": obj.get("has_protected_content") if obj.get("has_protected_content") is not None else True,
            "is_from_offline": obj.get("is_from_offline") if obj.get("is_from_offline") is not None else True,
            "media_group_id": obj.get("media_group_id"),
            "author_signature": obj.get("author_signature"),
            "paid_star_count": obj.get("paid_star_count"),
            "text": obj.get("text"),
            "entities": [MessageEntity.from_dict(_item) for _item in obj["entities"]] if obj.get("entities") is not None else None,
            "link_preview_options": LinkPreviewOptions.from_dict(obj["link_preview_options"]) if obj.get("link_preview_options") is not None else None,
            "effect_id": obj.get("effect_id"),
            "animation": Animation.from_dict(obj["animation"]) if obj.get("animation") is not None else None,
            "audio": Audio.from_dict(obj["audio"]) if obj.get("audio") is not None else None,
            "document": Document.from_dict(obj["document"]) if obj.get("document") is not None else None,
            "paid_media": PaidMediaInfo.from_dict(obj["paid_media"]) if obj.get("paid_media") is not None else None,
            "photo": [PhotoSize.from_dict(_item) for _item in obj["photo"]] if obj.get("photo") is not None else None,
            "sticker": Sticker.from_dict(obj["sticker"]) if obj.get("sticker") is not None else None,
            "story": Story.from_dict(obj["story"]) if obj.get("story") is not None else None,
            "video": Video.from_dict(obj["video"]) if obj.get("video") is not None else None,
            "video_note": VideoNote.from_dict(obj["video_note"]) if obj.get("video_note") is not None else None,
            "voice": Voice.from_dict(obj["voice"]) if obj.get("voice") is not None else None,
            "caption": obj.get("caption"),
            "caption_entities": [MessageEntity.from_dict(_item) for _item in obj["caption_entities"]] if obj.get("caption_entities") is not None else None,
            "show_caption_above_media": obj.get("show_caption_above_media") if obj.get("show_caption_above_media") is not None else True,
            "has_media_spoiler": obj.get("has_media_spoiler") if obj.get("has_media_spoiler") is not None else True,
            "contact": Contact.from_dict(obj["contact"]) if obj.get("contact") is not None else None,
            "dice": Dice.from_dict(obj["dice"]) if obj.get("dice") is not None else None,
            "game": Game.from_dict(obj["game"]) if obj.get("game") is not None else None,
            "poll": Poll.from_dict(obj["poll"]) if obj.get("poll") is not None else None,
            "venue": Venue.from_dict(obj["venue"]) if obj.get("venue") is not None else None,
            "location": Location.from_dict(obj["location"]) if obj.get("location") is not None else None,
            "new_chat_members": [User.from_dict(_item) for _item in obj["new_chat_members"]] if obj.get("new_chat_members") is not None else None,
            "left_chat_member": User.from_dict(obj["left_chat_member"]) if obj.get("left_chat_member") is not None else None,
            "new_chat_title": obj.get("new_chat_title"),
            "new_chat_photo": [PhotoSize.from_dict(_item) for _item in obj["new_chat_photo"]] if obj.get("new_chat_photo") is not None else None,
            "delete_chat_photo": obj.get("delete_chat_photo") if obj.get("delete_chat_photo") is not None else True,
            "group_chat_created": obj.get("group_chat_created") if obj.get("group_chat_created") is not None else True,
            "supergroup_chat_created": obj.get("supergroup_chat_created") if obj.get("supergroup_chat_created") is not None else True,
            "channel_chat_created": obj.get("channel_chat_created") if obj.get("channel_chat_created") is not None else True,
            "message_auto_delete_timer_changed": MessageAutoDeleteTimerChanged.from_dict(obj["message_auto_delete_timer_changed"]) if obj.get("message_auto_delete_timer_changed") is not None else None,
            "migrate_to_chat_id": obj.get("migrate_to_chat_id"),
            "migrate_from_chat_id": obj.get("migrate_from_chat_id"),
            "pinned_message": MaybeInaccessibleMessage.from_dict(obj["pinned_message"]) if obj.get("pinned_message") is not None else None,
            "invoice": Invoice.from_dict(obj["invoice"]) if obj.get("invoice") is not None else None,
            "successful_payment": SuccessfulPayment.from_dict(obj["successful_payment"]) if obj.get("successful_payment") is not None else None,
            "refunded_payment": RefundedPayment.from_dict(obj["refunded_payment"]) if obj.get("refunded_payment") is not None else None,
            "users_shared": UsersShared.from_dict(obj["users_shared"]) if obj.get("users_shared") is not None else None,
            "chat_shared": ChatShared.from_dict(obj["chat_shared"]) if obj.get("chat_shared") is not None else None,
            "gift": GiftInfo.from_dict(obj["gift"]) if obj.get("gift") is not None else None,
            "unique_gift": UniqueGiftInfo.from_dict(obj["unique_gift"]) if obj.get("unique_gift") is not None else None,
            "connected_website": obj.get("connected_website"),
            "write_access_allowed": WriteAccessAllowed.from_dict(obj["write_access_allowed"]) if obj.get("write_access_allowed") is not None else None,
            "passport_data": PassportData.from_dict(obj["passport_data"]) if obj.get("passport_data") is not None else None,
            "proximity_alert_triggered": ProximityAlertTriggered.from_dict(obj["proximity_alert_triggered"]) if obj.get("proximity_alert_triggered") is not None else None,
            "boost_added": ChatBoostAdded.from_dict(obj["boost_added"]) if obj.get("boost_added") is not None else None,
            "chat_background_set": ChatBackground.from_dict(obj["chat_background_set"]) if obj.get("chat_background_set") is not None else None,
            "forum_topic_created": ForumTopicCreated.from_dict(obj["forum_topic_created"]) if obj.get("forum_topic_created") is not None else None,
            "forum_topic_edited": ForumTopicEdited.from_dict(obj["forum_topic_edited"]) if obj.get("forum_topic_edited") is not None else None,
            "forum_topic_closed": obj.get("forum_topic_closed"),
            "forum_topic_reopened": obj.get("forum_topic_reopened"),
            "general_forum_topic_hidden": obj.get("general_forum_topic_hidden"),
            "general_forum_topic_unhidden": obj.get("general_forum_topic_unhidden"),
            "giveaway_created": GiveawayCreated.from_dict(obj["giveaway_created"]) if obj.get("giveaway_created") is not None else None,
            "giveaway": Giveaway.from_dict(obj["giveaway"]) if obj.get("giveaway") is not None else None,
            "giveaway_winners": GiveawayWinners.from_dict(obj["giveaway_winners"]) if obj.get("giveaway_winners") is not None else None,
            "giveaway_completed": GiveawayCompleted.from_dict(obj["giveaway_completed"]) if obj.get("giveaway_completed") is not None else None,
            "paid_message_price_changed": PaidMessagePriceChanged.from_dict(obj["paid_message_price_changed"]) if obj.get("paid_message_price_changed") is not None else None,
            "video_chat_scheduled": VideoChatScheduled.from_dict(obj["video_chat_scheduled"]) if obj.get("video_chat_scheduled") is not None else None,
            "video_chat_started": obj.get("video_chat_started"),
            "video_chat_ended": VideoChatEnded.from_dict(obj["video_chat_ended"]) if obj.get("video_chat_ended") is not None else None,
            "video_chat_participants_invited": VideoChatParticipantsInvited.from_dict(obj["video_chat_participants_invited"]) if obj.get("video_chat_participants_invited") is not None else None,
            "web_app_data": WebAppData.from_dict(obj["web_app_data"]) if obj.get("web_app_data") is not None else None,
            "reply_markup": InlineKeyboardMarkup.from_dict(obj["reply_markup"]) if obj.get("reply_markup") is not None else None
        })
        return _obj

from tele_rest.models.giveaway_completed import GiveawayCompleted
from tele_rest.models.maybe_inaccessible_message import MaybeInaccessibleMessage
# TODO: Rewrite to not use raise_errors
Message.model_rebuild(raise_errors=False)

