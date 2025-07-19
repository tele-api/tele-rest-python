# coding: utf-8

"""
Telegram Bot API - REST API Client
The Bot API is an HTTP-based interface created for developers keen on building bots for Telegram. To learn how to create and set up a bot, please consult our Introduction to Bots and Bot FAQ.

## Metadata

- **Copyright**: Copyright (c) 2025 Qntx
- **Author**: ΣX <gitctrlx@gmail.com>
- **Version**: 9.1.0
- **Modified**: 2025-07-19T09:30:11.405683802Z[Etc/UTC]
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
from tele_rest.models.inline_query_result_article import InlineQueryResultArticle
from tele_rest.models.inline_query_result_audio import InlineQueryResultAudio
from tele_rest.models.inline_query_result_cached_audio import InlineQueryResultCachedAudio
from tele_rest.models.inline_query_result_cached_document import InlineQueryResultCachedDocument
from tele_rest.models.inline_query_result_cached_gif import InlineQueryResultCachedGif
from tele_rest.models.inline_query_result_cached_mpeg4_gif import InlineQueryResultCachedMpeg4Gif
from tele_rest.models.inline_query_result_cached_photo import InlineQueryResultCachedPhoto
from tele_rest.models.inline_query_result_cached_sticker import InlineQueryResultCachedSticker
from tele_rest.models.inline_query_result_cached_video import InlineQueryResultCachedVideo
from tele_rest.models.inline_query_result_cached_voice import InlineQueryResultCachedVoice
from tele_rest.models.inline_query_result_contact import InlineQueryResultContact
from tele_rest.models.inline_query_result_document import InlineQueryResultDocument
from tele_rest.models.inline_query_result_game import InlineQueryResultGame
from tele_rest.models.inline_query_result_gif import InlineQueryResultGif
from tele_rest.models.inline_query_result_location import InlineQueryResultLocation
from tele_rest.models.inline_query_result_mpeg4_gif import InlineQueryResultMpeg4Gif
from tele_rest.models.inline_query_result_photo import InlineQueryResultPhoto
from tele_rest.models.inline_query_result_venue import InlineQueryResultVenue
from tele_rest.models.inline_query_result_video import InlineQueryResultVideo
from tele_rest.models.inline_query_result_voice import InlineQueryResultVoice
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

INLINEQUERYRESULT_ONE_OF_SCHEMAS = ["InlineQueryResultArticle", "InlineQueryResultAudio", "InlineQueryResultCachedAudio", "InlineQueryResultCachedDocument", "InlineQueryResultCachedGif", "InlineQueryResultCachedMpeg4Gif", "InlineQueryResultCachedPhoto", "InlineQueryResultCachedSticker", "InlineQueryResultCachedVideo", "InlineQueryResultCachedVoice", "InlineQueryResultContact", "InlineQueryResultDocument", "InlineQueryResultGame", "InlineQueryResultGif", "InlineQueryResultLocation", "InlineQueryResultMpeg4Gif", "InlineQueryResultPhoto", "InlineQueryResultVenue", "InlineQueryResultVideo", "InlineQueryResultVoice"]

class InlineQueryResult(BaseModel):
    """
    This object represents one result of an inline query. Telegram clients currently support results of the following 20 types:  * [InlineQueryResultCachedAudio](https://core.telegram.org/bots/api/#inlinequeryresultcachedaudio) * [InlineQueryResultCachedDocument](https://core.telegram.org/bots/api/#inlinequeryresultcacheddocument) * [InlineQueryResultCachedGif](https://core.telegram.org/bots/api/#inlinequeryresultcachedgif) * [InlineQueryResultCachedMpeg4Gif](https://core.telegram.org/bots/api/#inlinequeryresultcachedmpeg4gif) * [InlineQueryResultCachedPhoto](https://core.telegram.org/bots/api/#inlinequeryresultcachedphoto) * [InlineQueryResultCachedSticker](https://core.telegram.org/bots/api/#inlinequeryresultcachedsticker) * [InlineQueryResultCachedVideo](https://core.telegram.org/bots/api/#inlinequeryresultcachedvideo) * [InlineQueryResultCachedVoice](https://core.telegram.org/bots/api/#inlinequeryresultcachedvoice) * [InlineQueryResultArticle](https://core.telegram.org/bots/api/#inlinequeryresultarticle) * [InlineQueryResultAudio](https://core.telegram.org/bots/api/#inlinequeryresultaudio) * [InlineQueryResultContact](https://core.telegram.org/bots/api/#inlinequeryresultcontact) * [InlineQueryResultGame](https://core.telegram.org/bots/api/#inlinequeryresultgame) * [InlineQueryResultDocument](https://core.telegram.org/bots/api/#inlinequeryresultdocument) * [InlineQueryResultGif](https://core.telegram.org/bots/api/#inlinequeryresultgif) * [InlineQueryResultLocation](https://core.telegram.org/bots/api/#inlinequeryresultlocation) * [InlineQueryResultMpeg4Gif](https://core.telegram.org/bots/api/#inlinequeryresultmpeg4gif) * [InlineQueryResultPhoto](https://core.telegram.org/bots/api/#inlinequeryresultphoto) * [InlineQueryResultVenue](https://core.telegram.org/bots/api/#inlinequeryresultvenue) * [InlineQueryResultVideo](https://core.telegram.org/bots/api/#inlinequeryresultvideo) * [InlineQueryResultVoice](https://core.telegram.org/bots/api/#inlinequeryresultvoice)
    """
    # data type: InlineQueryResultCachedAudio
    oneof_schema_1_validator: Optional[InlineQueryResultCachedAudio] = None
    # data type: InlineQueryResultCachedDocument
    oneof_schema_2_validator: Optional[InlineQueryResultCachedDocument] = None
    # data type: InlineQueryResultCachedGif
    oneof_schema_3_validator: Optional[InlineQueryResultCachedGif] = None
    # data type: InlineQueryResultCachedMpeg4Gif
    oneof_schema_4_validator: Optional[InlineQueryResultCachedMpeg4Gif] = None
    # data type: InlineQueryResultCachedPhoto
    oneof_schema_5_validator: Optional[InlineQueryResultCachedPhoto] = None
    # data type: InlineQueryResultCachedSticker
    oneof_schema_6_validator: Optional[InlineQueryResultCachedSticker] = None
    # data type: InlineQueryResultCachedVideo
    oneof_schema_7_validator: Optional[InlineQueryResultCachedVideo] = None
    # data type: InlineQueryResultCachedVoice
    oneof_schema_8_validator: Optional[InlineQueryResultCachedVoice] = None
    # data type: InlineQueryResultArticle
    oneof_schema_9_validator: Optional[InlineQueryResultArticle] = None
    # data type: InlineQueryResultAudio
    oneof_schema_10_validator: Optional[InlineQueryResultAudio] = None
    # data type: InlineQueryResultContact
    oneof_schema_11_validator: Optional[InlineQueryResultContact] = None
    # data type: InlineQueryResultGame
    oneof_schema_12_validator: Optional[InlineQueryResultGame] = None
    # data type: InlineQueryResultDocument
    oneof_schema_13_validator: Optional[InlineQueryResultDocument] = None
    # data type: InlineQueryResultGif
    oneof_schema_14_validator: Optional[InlineQueryResultGif] = None
    # data type: InlineQueryResultLocation
    oneof_schema_15_validator: Optional[InlineQueryResultLocation] = None
    # data type: InlineQueryResultMpeg4Gif
    oneof_schema_16_validator: Optional[InlineQueryResultMpeg4Gif] = None
    # data type: InlineQueryResultPhoto
    oneof_schema_17_validator: Optional[InlineQueryResultPhoto] = None
    # data type: InlineQueryResultVenue
    oneof_schema_18_validator: Optional[InlineQueryResultVenue] = None
    # data type: InlineQueryResultVideo
    oneof_schema_19_validator: Optional[InlineQueryResultVideo] = None
    # data type: InlineQueryResultVoice
    oneof_schema_20_validator: Optional[InlineQueryResultVoice] = None
    actual_instance: Optional[Union[InlineQueryResultArticle, InlineQueryResultAudio, InlineQueryResultCachedAudio, InlineQueryResultCachedDocument, InlineQueryResultCachedGif, InlineQueryResultCachedMpeg4Gif, InlineQueryResultCachedPhoto, InlineQueryResultCachedSticker, InlineQueryResultCachedVideo, InlineQueryResultCachedVoice, InlineQueryResultContact, InlineQueryResultDocument, InlineQueryResultGame, InlineQueryResultGif, InlineQueryResultLocation, InlineQueryResultMpeg4Gif, InlineQueryResultPhoto, InlineQueryResultVenue, InlineQueryResultVideo, InlineQueryResultVoice]] = None
    one_of_schemas: Set[str] = { "InlineQueryResultArticle", "InlineQueryResultAudio", "InlineQueryResultCachedAudio", "InlineQueryResultCachedDocument", "InlineQueryResultCachedGif", "InlineQueryResultCachedMpeg4Gif", "InlineQueryResultCachedPhoto", "InlineQueryResultCachedSticker", "InlineQueryResultCachedVideo", "InlineQueryResultCachedVoice", "InlineQueryResultContact", "InlineQueryResultDocument", "InlineQueryResultGame", "InlineQueryResultGif", "InlineQueryResultLocation", "InlineQueryResultMpeg4Gif", "InlineQueryResultPhoto", "InlineQueryResultVenue", "InlineQueryResultVideo", "InlineQueryResultVoice" }

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
        instance = InlineQueryResult.model_construct()
        error_messages = []
        match = 0
        # validate data type: InlineQueryResultCachedAudio
        if not isinstance(v, InlineQueryResultCachedAudio):
            error_messages.append(f"Error! Input type `{type(v)}` is not `InlineQueryResultCachedAudio`")
        else:
            match += 1
        # validate data type: InlineQueryResultCachedDocument
        if not isinstance(v, InlineQueryResultCachedDocument):
            error_messages.append(f"Error! Input type `{type(v)}` is not `InlineQueryResultCachedDocument`")
        else:
            match += 1
        # validate data type: InlineQueryResultCachedGif
        if not isinstance(v, InlineQueryResultCachedGif):
            error_messages.append(f"Error! Input type `{type(v)}` is not `InlineQueryResultCachedGif`")
        else:
            match += 1
        # validate data type: InlineQueryResultCachedMpeg4Gif
        if not isinstance(v, InlineQueryResultCachedMpeg4Gif):
            error_messages.append(f"Error! Input type `{type(v)}` is not `InlineQueryResultCachedMpeg4Gif`")
        else:
            match += 1
        # validate data type: InlineQueryResultCachedPhoto
        if not isinstance(v, InlineQueryResultCachedPhoto):
            error_messages.append(f"Error! Input type `{type(v)}` is not `InlineQueryResultCachedPhoto`")
        else:
            match += 1
        # validate data type: InlineQueryResultCachedSticker
        if not isinstance(v, InlineQueryResultCachedSticker):
            error_messages.append(f"Error! Input type `{type(v)}` is not `InlineQueryResultCachedSticker`")
        else:
            match += 1
        # validate data type: InlineQueryResultCachedVideo
        if not isinstance(v, InlineQueryResultCachedVideo):
            error_messages.append(f"Error! Input type `{type(v)}` is not `InlineQueryResultCachedVideo`")
        else:
            match += 1
        # validate data type: InlineQueryResultCachedVoice
        if not isinstance(v, InlineQueryResultCachedVoice):
            error_messages.append(f"Error! Input type `{type(v)}` is not `InlineQueryResultCachedVoice`")
        else:
            match += 1
        # validate data type: InlineQueryResultArticle
        if not isinstance(v, InlineQueryResultArticle):
            error_messages.append(f"Error! Input type `{type(v)}` is not `InlineQueryResultArticle`")
        else:
            match += 1
        # validate data type: InlineQueryResultAudio
        if not isinstance(v, InlineQueryResultAudio):
            error_messages.append(f"Error! Input type `{type(v)}` is not `InlineQueryResultAudio`")
        else:
            match += 1
        # validate data type: InlineQueryResultContact
        if not isinstance(v, InlineQueryResultContact):
            error_messages.append(f"Error! Input type `{type(v)}` is not `InlineQueryResultContact`")
        else:
            match += 1
        # validate data type: InlineQueryResultGame
        if not isinstance(v, InlineQueryResultGame):
            error_messages.append(f"Error! Input type `{type(v)}` is not `InlineQueryResultGame`")
        else:
            match += 1
        # validate data type: InlineQueryResultDocument
        if not isinstance(v, InlineQueryResultDocument):
            error_messages.append(f"Error! Input type `{type(v)}` is not `InlineQueryResultDocument`")
        else:
            match += 1
        # validate data type: InlineQueryResultGif
        if not isinstance(v, InlineQueryResultGif):
            error_messages.append(f"Error! Input type `{type(v)}` is not `InlineQueryResultGif`")
        else:
            match += 1
        # validate data type: InlineQueryResultLocation
        if not isinstance(v, InlineQueryResultLocation):
            error_messages.append(f"Error! Input type `{type(v)}` is not `InlineQueryResultLocation`")
        else:
            match += 1
        # validate data type: InlineQueryResultMpeg4Gif
        if not isinstance(v, InlineQueryResultMpeg4Gif):
            error_messages.append(f"Error! Input type `{type(v)}` is not `InlineQueryResultMpeg4Gif`")
        else:
            match += 1
        # validate data type: InlineQueryResultPhoto
        if not isinstance(v, InlineQueryResultPhoto):
            error_messages.append(f"Error! Input type `{type(v)}` is not `InlineQueryResultPhoto`")
        else:
            match += 1
        # validate data type: InlineQueryResultVenue
        if not isinstance(v, InlineQueryResultVenue):
            error_messages.append(f"Error! Input type `{type(v)}` is not `InlineQueryResultVenue`")
        else:
            match += 1
        # validate data type: InlineQueryResultVideo
        if not isinstance(v, InlineQueryResultVideo):
            error_messages.append(f"Error! Input type `{type(v)}` is not `InlineQueryResultVideo`")
        else:
            match += 1
        # validate data type: InlineQueryResultVoice
        if not isinstance(v, InlineQueryResultVoice):
            error_messages.append(f"Error! Input type `{type(v)}` is not `InlineQueryResultVoice`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in InlineQueryResult with oneOf schemas: InlineQueryResultArticle, InlineQueryResultAudio, InlineQueryResultCachedAudio, InlineQueryResultCachedDocument, InlineQueryResultCachedGif, InlineQueryResultCachedMpeg4Gif, InlineQueryResultCachedPhoto, InlineQueryResultCachedSticker, InlineQueryResultCachedVideo, InlineQueryResultCachedVoice, InlineQueryResultContact, InlineQueryResultDocument, InlineQueryResultGame, InlineQueryResultGif, InlineQueryResultLocation, InlineQueryResultMpeg4Gif, InlineQueryResultPhoto, InlineQueryResultVenue, InlineQueryResultVideo, InlineQueryResultVoice. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in InlineQueryResult with oneOf schemas: InlineQueryResultArticle, InlineQueryResultAudio, InlineQueryResultCachedAudio, InlineQueryResultCachedDocument, InlineQueryResultCachedGif, InlineQueryResultCachedMpeg4Gif, InlineQueryResultCachedPhoto, InlineQueryResultCachedSticker, InlineQueryResultCachedVideo, InlineQueryResultCachedVoice, InlineQueryResultContact, InlineQueryResultDocument, InlineQueryResultGame, InlineQueryResultGif, InlineQueryResultLocation, InlineQueryResultMpeg4Gif, InlineQueryResultPhoto, InlineQueryResultVenue, InlineQueryResultVideo, InlineQueryResultVoice. Details: " + ", ".join(error_messages))
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

        # deserialize data into InlineQueryResultCachedAudio
        try:
            instance.actual_instance = InlineQueryResultCachedAudio.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into InlineQueryResultCachedDocument
        try:
            instance.actual_instance = InlineQueryResultCachedDocument.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into InlineQueryResultCachedGif
        try:
            instance.actual_instance = InlineQueryResultCachedGif.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into InlineQueryResultCachedMpeg4Gif
        try:
            instance.actual_instance = InlineQueryResultCachedMpeg4Gif.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into InlineQueryResultCachedPhoto
        try:
            instance.actual_instance = InlineQueryResultCachedPhoto.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into InlineQueryResultCachedSticker
        try:
            instance.actual_instance = InlineQueryResultCachedSticker.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into InlineQueryResultCachedVideo
        try:
            instance.actual_instance = InlineQueryResultCachedVideo.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into InlineQueryResultCachedVoice
        try:
            instance.actual_instance = InlineQueryResultCachedVoice.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into InlineQueryResultArticle
        try:
            instance.actual_instance = InlineQueryResultArticle.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into InlineQueryResultAudio
        try:
            instance.actual_instance = InlineQueryResultAudio.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into InlineQueryResultContact
        try:
            instance.actual_instance = InlineQueryResultContact.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into InlineQueryResultGame
        try:
            instance.actual_instance = InlineQueryResultGame.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into InlineQueryResultDocument
        try:
            instance.actual_instance = InlineQueryResultDocument.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into InlineQueryResultGif
        try:
            instance.actual_instance = InlineQueryResultGif.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into InlineQueryResultLocation
        try:
            instance.actual_instance = InlineQueryResultLocation.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into InlineQueryResultMpeg4Gif
        try:
            instance.actual_instance = InlineQueryResultMpeg4Gif.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into InlineQueryResultPhoto
        try:
            instance.actual_instance = InlineQueryResultPhoto.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into InlineQueryResultVenue
        try:
            instance.actual_instance = InlineQueryResultVenue.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into InlineQueryResultVideo
        try:
            instance.actual_instance = InlineQueryResultVideo.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into InlineQueryResultVoice
        try:
            instance.actual_instance = InlineQueryResultVoice.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into InlineQueryResult with oneOf schemas: InlineQueryResultArticle, InlineQueryResultAudio, InlineQueryResultCachedAudio, InlineQueryResultCachedDocument, InlineQueryResultCachedGif, InlineQueryResultCachedMpeg4Gif, InlineQueryResultCachedPhoto, InlineQueryResultCachedSticker, InlineQueryResultCachedVideo, InlineQueryResultCachedVoice, InlineQueryResultContact, InlineQueryResultDocument, InlineQueryResultGame, InlineQueryResultGif, InlineQueryResultLocation, InlineQueryResultMpeg4Gif, InlineQueryResultPhoto, InlineQueryResultVenue, InlineQueryResultVideo, InlineQueryResultVoice. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into InlineQueryResult with oneOf schemas: InlineQueryResultArticle, InlineQueryResultAudio, InlineQueryResultCachedAudio, InlineQueryResultCachedDocument, InlineQueryResultCachedGif, InlineQueryResultCachedMpeg4Gif, InlineQueryResultCachedPhoto, InlineQueryResultCachedSticker, InlineQueryResultCachedVideo, InlineQueryResultCachedVoice, InlineQueryResultContact, InlineQueryResultDocument, InlineQueryResultGame, InlineQueryResultGif, InlineQueryResultLocation, InlineQueryResultMpeg4Gif, InlineQueryResultPhoto, InlineQueryResultVenue, InlineQueryResultVideo, InlineQueryResultVoice. Details: " + ", ".join(error_messages))
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

    def to_dict(self) -> Optional[Union[Dict[str, Any], InlineQueryResultArticle, InlineQueryResultAudio, InlineQueryResultCachedAudio, InlineQueryResultCachedDocument, InlineQueryResultCachedGif, InlineQueryResultCachedMpeg4Gif, InlineQueryResultCachedPhoto, InlineQueryResultCachedSticker, InlineQueryResultCachedVideo, InlineQueryResultCachedVoice, InlineQueryResultContact, InlineQueryResultDocument, InlineQueryResultGame, InlineQueryResultGif, InlineQueryResultLocation, InlineQueryResultMpeg4Gif, InlineQueryResultPhoto, InlineQueryResultVenue, InlineQueryResultVideo, InlineQueryResultVoice]]:
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


