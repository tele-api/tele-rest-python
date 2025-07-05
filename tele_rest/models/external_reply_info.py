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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from tele_rest.models.animation import Animation
from tele_rest.models.audio import Audio
from tele_rest.models.chat import Chat
from tele_rest.models.checklist import Checklist
from tele_rest.models.contact import Contact
from tele_rest.models.dice import Dice
from tele_rest.models.document import Document
from tele_rest.models.game import Game
from tele_rest.models.giveaway import Giveaway
from tele_rest.models.giveaway_winners import GiveawayWinners
from tele_rest.models.invoice import Invoice
from tele_rest.models.link_preview_options import LinkPreviewOptions
from tele_rest.models.location import Location
from tele_rest.models.message_origin import MessageOrigin
from tele_rest.models.paid_media_info import PaidMediaInfo
from tele_rest.models.photo_size import PhotoSize
from tele_rest.models.poll import Poll
from tele_rest.models.sticker import Sticker
from tele_rest.models.story import Story
from tele_rest.models.venue import Venue
from tele_rest.models.video import Video
from tele_rest.models.video_note import VideoNote
from tele_rest.models.voice import Voice
from typing import Optional, Set
from typing_extensions import Self

class ExternalReplyInfo(BaseModel):
    """
    This object contains information about a message that is being replied to, which may come from another chat or forum topic.
    """ # noqa: E501
    origin: MessageOrigin
    chat: Optional[Chat] = None
    message_id: Optional[StrictInt] = Field(default=None, description="*Optional*. Unique message identifier inside the original chat. Available only if the original chat is a supergroup or a channel.")
    link_preview_options: Optional[LinkPreviewOptions] = None
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
    has_media_spoiler: Optional[StrictBool] = Field(default=True, description="*Optional*. *True*, if the message media is covered by a spoiler animation")
    checklist: Optional[Checklist] = None
    contact: Optional[Contact] = None
    dice: Optional[Dice] = None
    game: Optional[Game] = None
    giveaway: Optional[Giveaway] = None
    giveaway_winners: Optional[GiveawayWinners] = None
    invoice: Optional[Invoice] = None
    location: Optional[Location] = None
    poll: Optional[Poll] = None
    venue: Optional[Venue] = None
    __properties: ClassVar[List[str]] = ["origin", "chat", "message_id", "link_preview_options", "animation", "audio", "document", "paid_media", "photo", "sticker", "story", "video", "video_note", "voice", "has_media_spoiler", "checklist", "contact", "dice", "game", "giveaway", "giveaway_winners", "invoice", "location", "poll", "venue"]

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
        """Create an instance of ExternalReplyInfo from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of origin
        if self.origin:
            _dict['origin'] = self.origin.to_dict()
        # override the default output from pydantic by calling `to_dict()` of chat
        if self.chat:
            _dict['chat'] = self.chat.to_dict()
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
        # override the default output from pydantic by calling `to_dict()` of checklist
        if self.checklist:
            _dict['checklist'] = self.checklist.to_dict()
        # override the default output from pydantic by calling `to_dict()` of contact
        if self.contact:
            _dict['contact'] = self.contact.to_dict()
        # override the default output from pydantic by calling `to_dict()` of dice
        if self.dice:
            _dict['dice'] = self.dice.to_dict()
        # override the default output from pydantic by calling `to_dict()` of game
        if self.game:
            _dict['game'] = self.game.to_dict()
        # override the default output from pydantic by calling `to_dict()` of giveaway
        if self.giveaway:
            _dict['giveaway'] = self.giveaway.to_dict()
        # override the default output from pydantic by calling `to_dict()` of giveaway_winners
        if self.giveaway_winners:
            _dict['giveaway_winners'] = self.giveaway_winners.to_dict()
        # override the default output from pydantic by calling `to_dict()` of invoice
        if self.invoice:
            _dict['invoice'] = self.invoice.to_dict()
        # override the default output from pydantic by calling `to_dict()` of location
        if self.location:
            _dict['location'] = self.location.to_dict()
        # override the default output from pydantic by calling `to_dict()` of poll
        if self.poll:
            _dict['poll'] = self.poll.to_dict()
        # override the default output from pydantic by calling `to_dict()` of venue
        if self.venue:
            _dict['venue'] = self.venue.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ExternalReplyInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in ExternalReplyInfo) in the input: " + _key)

        _obj = cls.model_validate({
            "origin": MessageOrigin.from_dict(obj["origin"]) if obj.get("origin") is not None else None,
            "chat": Chat.from_dict(obj["chat"]) if obj.get("chat") is not None else None,
            "message_id": obj.get("message_id"),
            "link_preview_options": LinkPreviewOptions.from_dict(obj["link_preview_options"]) if obj.get("link_preview_options") is not None else None,
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
            "has_media_spoiler": obj.get("has_media_spoiler") if obj.get("has_media_spoiler") is not None else True,
            "checklist": Checklist.from_dict(obj["checklist"]) if obj.get("checklist") is not None else None,
            "contact": Contact.from_dict(obj["contact"]) if obj.get("contact") is not None else None,
            "dice": Dice.from_dict(obj["dice"]) if obj.get("dice") is not None else None,
            "game": Game.from_dict(obj["game"]) if obj.get("game") is not None else None,
            "giveaway": Giveaway.from_dict(obj["giveaway"]) if obj.get("giveaway") is not None else None,
            "giveaway_winners": GiveawayWinners.from_dict(obj["giveaway_winners"]) if obj.get("giveaway_winners") is not None else None,
            "invoice": Invoice.from_dict(obj["invoice"]) if obj.get("invoice") is not None else None,
            "location": Location.from_dict(obj["location"]) if obj.get("location") is not None else None,
            "poll": Poll.from_dict(obj["poll"]) if obj.get("poll") is not None else None,
            "venue": Venue.from_dict(obj["venue"]) if obj.get("venue") is not None else None
        })
        return _obj


