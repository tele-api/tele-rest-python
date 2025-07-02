# coding: utf-8

# flake8: noqa

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


__version__ = "9.0.0"

# Define package exports
__all__ = [
    "DefaultApi",
    "ApiResponse",
    "ApiClient",
    "Configuration",
    "OpenApiException",
    "ApiTypeError",
    "ApiValueError",
    "ApiKeyError",
    "ApiAttributeError",
    "ApiException",
    "AcceptedGiftTypes",
    "AffiliateInfo",
    "Animation",
    "Audio",
    "BackgroundFill",
    "BackgroundFillFreeformGradient",
    "BackgroundFillGradient",
    "BackgroundFillSolid",
    "BackgroundType",
    "BackgroundTypeChatTheme",
    "BackgroundTypeFill",
    "BackgroundTypePattern",
    "BackgroundTypeWallpaper",
    "Birthdate",
    "BotCommand",
    "BotCommandScope",
    "BotCommandScopeAllChatAdministrators",
    "BotCommandScopeAllGroupChats",
    "BotCommandScopeAllPrivateChats",
    "BotCommandScopeChat",
    "BotCommandScopeChatAdministrators",
    "BotCommandScopeChatMember",
    "BotCommandScopeDefault",
    "BotDescription",
    "BotName",
    "BotShortDescription",
    "BusinessBotRights",
    "BusinessConnection",
    "BusinessIntro",
    "BusinessLocation",
    "BusinessMessagesDeleted",
    "BusinessOpeningHours",
    "BusinessOpeningHoursInterval",
    "CallbackQuery",
    "Chat",
    "ChatAdministratorRights",
    "ChatBackground",
    "ChatBoost",
    "ChatBoostAdded",
    "ChatBoostRemoved",
    "ChatBoostSource",
    "ChatBoostSourceGiftCode",
    "ChatBoostSourceGiveaway",
    "ChatBoostSourcePremium",
    "ChatBoostUpdated",
    "ChatFullInfo",
    "ChatInviteLink",
    "ChatJoinRequest",
    "ChatLocation",
    "ChatMember",
    "ChatMemberAdministrator",
    "ChatMemberBanned",
    "ChatMemberLeft",
    "ChatMemberMember",
    "ChatMemberOwner",
    "ChatMemberRestricted",
    "ChatMemberUpdated",
    "ChatPermissions",
    "ChatPhoto",
    "ChatShared",
    "ChosenInlineResult",
    "Contact",
    "CopyTextButton",
    "Dice",
    "Document",
    "EncryptedCredentials",
    "EncryptedPassportElement",
    "Error",
    "ExternalReplyInfo",
    "File",
    "ForceReply",
    "ForumTopic",
    "ForumTopicCreated",
    "ForumTopicEdited",
    "Game",
    "GameHighScore",
    "Gift",
    "GiftInfo",
    "Gifts",
    "Giveaway",
    "GiveawayCompleted",
    "GiveawayCreated",
    "GiveawayWinners",
    "InaccessibleMessage",
    "InlineKeyboardButton",
    "InlineKeyboardMarkup",
    "InlineQuery",
    "InlineQueryResult",
    "InlineQueryResultArticle",
    "InlineQueryResultAudio",
    "InlineQueryResultCachedAudio",
    "InlineQueryResultCachedDocument",
    "InlineQueryResultCachedGif",
    "InlineQueryResultCachedMpeg4Gif",
    "InlineQueryResultCachedPhoto",
    "InlineQueryResultCachedSticker",
    "InlineQueryResultCachedVideo",
    "InlineQueryResultCachedVoice",
    "InlineQueryResultContact",
    "InlineQueryResultDocument",
    "InlineQueryResultGame",
    "InlineQueryResultGif",
    "InlineQueryResultLocation",
    "InlineQueryResultMpeg4Gif",
    "InlineQueryResultPhoto",
    "InlineQueryResultVenue",
    "InlineQueryResultVideo",
    "InlineQueryResultVoice",
    "InlineQueryResultsButton",
    "InputContactMessageContent",
    "InputInvoiceMessageContent",
    "InputLocationMessageContent",
    "InputMedia",
    "InputMediaAnimation",
    "InputMediaAudio",
    "InputMediaDocument",
    "InputMediaPhoto",
    "InputMediaVideo",
    "InputMessageContent",
    "InputPaidMedia",
    "InputPaidMediaPhoto",
    "InputPaidMediaVideo",
    "InputPollOption",
    "InputProfilePhoto",
    "InputProfilePhotoAnimated",
    "InputProfilePhotoStatic",
    "InputSticker",
    "InputStoryContent",
    "InputStoryContentPhoto",
    "InputStoryContentVideo",
    "InputTextMessageContent",
    "InputVenueMessageContent",
    "Invoice",
    "KeyboardButton",
    "KeyboardButtonPollType",
    "KeyboardButtonRequestChat",
    "KeyboardButtonRequestUsers",
    "LabeledPrice",
    "LinkPreviewOptions",
    "Location",
    "LocationAddress",
    "LoginUrl",
    "MaskPosition",
    "MaybeInaccessibleMessage",
    "MenuButton",
    "MenuButtonCommands",
    "MenuButtonDefault",
    "MenuButtonWebApp",
    "Message",
    "MessageAutoDeleteTimerChanged",
    "MessageEntity",
    "MessageId",
    "MessageOrigin",
    "MessageOriginChannel",
    "MessageOriginChat",
    "MessageOriginHiddenUser",
    "MessageOriginUser",
    "MessageReactionCountUpdated",
    "MessageReactionUpdated",
    "OrderInfo",
    "OwnedGift",
    "OwnedGiftRegular",
    "OwnedGiftUnique",
    "OwnedGifts",
    "PaidMedia",
    "PaidMediaInfo",
    "PaidMediaPhoto",
    "PaidMediaPreview",
    "PaidMediaPurchased",
    "PaidMediaVideo",
    "PaidMessagePriceChanged",
    "PassportData",
    "PassportElementError",
    "PassportElementErrorDataField",
    "PassportElementErrorFile",
    "PassportElementErrorFiles",
    "PassportElementErrorFrontSide",
    "PassportElementErrorReverseSide",
    "PassportElementErrorSelfie",
    "PassportElementErrorTranslationFile",
    "PassportElementErrorTranslationFiles",
    "PassportElementErrorUnspecified",
    "PassportFile",
    "PhotoSize",
    "Poll",
    "PollAnswer",
    "PollOption",
    "PostAnswerCallbackQueryRequest",
    "PostAnswerInlineQueryRequest",
    "PostAnswerPreCheckoutQueryRequest",
    "PostAnswerShippingQueryRequest",
    "PostAnswerWebAppQuery200Response",
    "PostAnswerWebAppQueryRequest",
    "PostApproveChatJoinRequestRequest",
    "PostBanChatMemberRequest",
    "PostBanChatMemberRequestChatId",
    "PostBanChatSenderChatRequest",
    "PostCloseForumTopicRequest",
    "PostConvertGiftToStarsRequest",
    "PostCopyMessage200Response",
    "PostCopyMessageRequest",
    "PostCopyMessagesRequest",
    "PostCreateChatInviteLink200Response",
    "PostCreateChatInviteLinkRequest",
    "PostCreateChatSubscriptionInviteLinkRequest",
    "PostCreateChatSubscriptionInviteLinkRequestChatId",
    "PostCreateForumTopic200Response",
    "PostCreateForumTopicRequest",
    "PostCreateInvoiceLinkRequest",
    "PostDeleteBusinessMessagesRequest",
    "PostDeleteChatStickerSetRequest",
    "PostDeleteMessageRequest",
    "PostDeleteMessagesRequest",
    "PostDeleteMyCommandsRequest",
    "PostDeleteStickerFromSetRequest",
    "PostDeleteStickerSetRequest",
    "PostDeleteStoryRequest",
    "PostDeleteWebhookRequest",
    "PostEditChatInviteLinkRequest",
    "PostEditChatSubscriptionInviteLinkRequest",
    "PostEditForumTopicRequest",
    "PostEditGeneralForumTopicRequest",
    "PostEditMessageCaptionRequest",
    "PostEditMessageLiveLocationRequest",
    "PostEditMessageReplyMarkupRequest",
    "PostEditMessageText200Response",
    "PostEditMessageText200ResponseResult",
    "PostEditMessageTextRequest",
    "PostEditMessageTextRequestChatId",
    "PostEditUserStarSubscriptionRequest",
    "PostExportChatInviteLink200Response",
    "PostExportChatInviteLinkRequest",
    "PostForwardMessageRequest",
    "PostForwardMessageRequestFromChatId",
    "PostForwardMessages200Response",
    "PostForwardMessagesRequest",
    "PostForwardMessagesRequestFromChatId",
    "PostGetAvailableGifts200Response",
    "PostGetBusinessAccountGifts200Response",
    "PostGetBusinessAccountGiftsRequest",
    "PostGetBusinessAccountStarBalance200Response",
    "PostGetBusinessConnection200Response",
    "PostGetBusinessConnectionRequest",
    "PostGetChat200Response",
    "PostGetChatAdministrators200Response",
    "PostGetChatMember200Response",
    "PostGetChatMemberCount200Response",
    "PostGetChatMemberRequest",
    "PostGetChatMenuButton200Response",
    "PostGetChatMenuButtonRequest",
    "PostGetCustomEmojiStickersRequest",
    "PostGetFile200Response",
    "PostGetFileRequest",
    "PostGetForumTopicIconStickers200Response",
    "PostGetGameHighScores200Response",
    "PostGetGameHighScoresRequest",
    "PostGetMe200Response",
    "PostGetMyCommands200Response",
    "PostGetMyCommandsRequest",
    "PostGetMyDefaultAdministratorRights200Response",
    "PostGetMyDefaultAdministratorRightsRequest",
    "PostGetMyDescription200Response",
    "PostGetMyName200Response",
    "PostGetMyNameRequest",
    "PostGetMyShortDescription200Response",
    "PostGetStarTransactions200Response",
    "PostGetStarTransactionsRequest",
    "PostGetStickerSet200Response",
    "PostGetStickerSetRequest",
    "PostGetUpdates200Response",
    "PostGetUpdatesRequest",
    "PostGetUserChatBoosts200Response",
    "PostGetUserChatBoostsRequest",
    "PostGetUserChatBoostsRequestChatId",
    "PostGetUserProfilePhotos200Response",
    "PostGetUserProfilePhotosRequest",
    "PostGetWebhookInfo200Response",
    "PostGiftPremiumSubscriptionRequest",
    "PostLeaveChatRequest",
    "PostLeaveChatRequestChatId",
    "PostPinChatMessageRequest",
    "PostPostStory200Response",
    "PostPromoteChatMemberRequest",
    "PostReadBusinessMessageRequest",
    "PostRefundStarPaymentRequest",
    "PostRemoveBusinessAccountProfilePhotoRequest",
    "PostRemoveUserVerificationRequest",
    "PostRestrictChatMemberRequest",
    "PostRestrictChatMemberRequestChatId",
    "PostRevokeChatInviteLinkRequest",
    "PostRevokeChatInviteLinkRequestChatId",
    "PostSavePreparedInlineMessage200Response",
    "PostSavePreparedInlineMessageRequest",
    "PostSendAnimationRequestAnimation",
    "PostSendAudioRequestAudio",
    "PostSendAudioRequestThumbnail",
    "PostSendChatActionRequest",
    "PostSendContactRequest",
    "PostSendDiceRequest",
    "PostSendDocumentRequestDocument",
    "PostSendGameRequest",
    "PostSendGiftRequest",
    "PostSendGiftRequestChatId",
    "PostSendInvoiceRequest",
    "PostSendLocationRequest",
    "PostSendMediaGroup200Response",
    "PostSendMediaGroupRequestMediaInner",
    "PostSendMessage200Response",
    "PostSendMessageRequest",
    "PostSendMessageRequestChatId",
    "PostSendMessageRequestReplyMarkup",
    "PostSendPaidMediaRequestChatId",
    "PostSendPhotoRequestPhoto",
    "PostSendPollRequest",
    "PostSendStickerRequestSticker",
    "PostSendVenueRequest",
    "PostSendVideoNoteRequestVideoNote",
    "PostSendVideoRequestCover",
    "PostSendVideoRequestVideo",
    "PostSendVoiceRequestVoice",
    "PostSetBusinessAccountBioRequest",
    "PostSetBusinessAccountGiftSettingsRequest",
    "PostSetBusinessAccountNameRequest",
    "PostSetBusinessAccountUsernameRequest",
    "PostSetChatAdministratorCustomTitleRequest",
    "PostSetChatDescriptionRequest",
    "PostSetChatMenuButtonRequest",
    "PostSetChatPermissionsRequest",
    "PostSetChatStickerSetRequest",
    "PostSetChatTitleRequest",
    "PostSetCustomEmojiStickerSetThumbnailRequest",
    "PostSetGameScoreRequest",
    "PostSetMessageReactionRequest",
    "PostSetMyCommandsRequest",
    "PostSetMyDefaultAdministratorRightsRequest",
    "PostSetMyDescriptionRequest",
    "PostSetMyNameRequest",
    "PostSetMyShortDescriptionRequest",
    "PostSetPassportDataErrorsRequest",
    "PostSetStickerEmojiListRequest",
    "PostSetStickerKeywordsRequest",
    "PostSetStickerMaskPositionRequest",
    "PostSetStickerPositionInSetRequest",
    "PostSetStickerSetThumbnailRequestThumbnail",
    "PostSetStickerSetTitleRequest",
    "PostSetUserEmojiStatusRequest",
    "PostSetWebhook200Response",
    "PostStopMessageLiveLocationRequest",
    "PostStopPoll200Response",
    "PostStopPollRequest",
    "PostTransferBusinessAccountStarsRequest",
    "PostTransferGiftRequest",
    "PostUnbanChatMemberRequest",
    "PostUnpinChatMessageRequest",
    "PostUpgradeGiftRequest",
    "PostVerifyChatRequest",
    "PostVerifyUserRequest",
    "PreCheckoutQuery",
    "PreparedInlineMessage",
    "ProximityAlertTriggered",
    "ReactionCount",
    "ReactionType",
    "ReactionTypeCustomEmoji",
    "ReactionTypeEmoji",
    "ReactionTypePaid",
    "RefundedPayment",
    "ReplyKeyboardMarkup",
    "ReplyKeyboardRemove",
    "ReplyParameters",
    "ReplyParametersChatId",
    "ResponseParameters",
    "RevenueWithdrawalState",
    "RevenueWithdrawalStateFailed",
    "RevenueWithdrawalStatePending",
    "RevenueWithdrawalStateSucceeded",
    "SentWebAppMessage",
    "SharedUser",
    "ShippingAddress",
    "ShippingOption",
    "ShippingQuery",
    "StarAmount",
    "StarTransaction",
    "StarTransactions",
    "Sticker",
    "StickerSet",
    "Story",
    "StoryArea",
    "StoryAreaPosition",
    "StoryAreaType",
    "StoryAreaTypeLink",
    "StoryAreaTypeLocation",
    "StoryAreaTypeSuggestedReaction",
    "StoryAreaTypeUniqueGift",
    "StoryAreaTypeWeather",
    "SuccessfulPayment",
    "SwitchInlineQueryChosenChat",
    "TextQuote",
    "TransactionPartner",
    "TransactionPartnerAffiliateProgram",
    "TransactionPartnerChat",
    "TransactionPartnerFragment",
    "TransactionPartnerOther",
    "TransactionPartnerTelegramAds",
    "TransactionPartnerTelegramApi",
    "TransactionPartnerUser",
    "UniqueGift",
    "UniqueGiftBackdrop",
    "UniqueGiftBackdropColors",
    "UniqueGiftInfo",
    "UniqueGiftModel",
    "UniqueGiftSymbol",
    "Update",
    "User",
    "UserChatBoosts",
    "UserProfilePhotos",
    "UsersShared",
    "Venue",
    "Video",
    "VideoChatEnded",
    "VideoChatParticipantsInvited",
    "VideoChatScheduled",
    "VideoNote",
    "Voice",
    "WebAppData",
    "WebAppInfo",
    "WebhookInfo",
    "WriteAccessAllowed",
]

# import apis into sdk package
from tele_rest.api.default_api import DefaultApi as DefaultApi

# import ApiClient
from tele_rest.api_response import ApiResponse as ApiResponse
from tele_rest.api_client import ApiClient as ApiClient
from tele_rest.configuration import Configuration as Configuration
from tele_rest.exceptions import OpenApiException as OpenApiException
from tele_rest.exceptions import ApiTypeError as ApiTypeError
from tele_rest.exceptions import ApiValueError as ApiValueError
from tele_rest.exceptions import ApiKeyError as ApiKeyError
from tele_rest.exceptions import ApiAttributeError as ApiAttributeError
from tele_rest.exceptions import ApiException as ApiException

# import models into sdk package
from tele_rest.models.accepted_gift_types import AcceptedGiftTypes as AcceptedGiftTypes
from tele_rest.models.affiliate_info import AffiliateInfo as AffiliateInfo
from tele_rest.models.animation import Animation as Animation
from tele_rest.models.audio import Audio as Audio
from tele_rest.models.background_fill import BackgroundFill as BackgroundFill
from tele_rest.models.background_fill_freeform_gradient import BackgroundFillFreeformGradient as BackgroundFillFreeformGradient
from tele_rest.models.background_fill_gradient import BackgroundFillGradient as BackgroundFillGradient
from tele_rest.models.background_fill_solid import BackgroundFillSolid as BackgroundFillSolid
from tele_rest.models.background_type import BackgroundType as BackgroundType
from tele_rest.models.background_type_chat_theme import BackgroundTypeChatTheme as BackgroundTypeChatTheme
from tele_rest.models.background_type_fill import BackgroundTypeFill as BackgroundTypeFill
from tele_rest.models.background_type_pattern import BackgroundTypePattern as BackgroundTypePattern
from tele_rest.models.background_type_wallpaper import BackgroundTypeWallpaper as BackgroundTypeWallpaper
from tele_rest.models.birthdate import Birthdate as Birthdate
from tele_rest.models.bot_command import BotCommand as BotCommand
from tele_rest.models.bot_command_scope import BotCommandScope as BotCommandScope
from tele_rest.models.bot_command_scope_all_chat_administrators import BotCommandScopeAllChatAdministrators as BotCommandScopeAllChatAdministrators
from tele_rest.models.bot_command_scope_all_group_chats import BotCommandScopeAllGroupChats as BotCommandScopeAllGroupChats
from tele_rest.models.bot_command_scope_all_private_chats import BotCommandScopeAllPrivateChats as BotCommandScopeAllPrivateChats
from tele_rest.models.bot_command_scope_chat import BotCommandScopeChat as BotCommandScopeChat
from tele_rest.models.bot_command_scope_chat_administrators import BotCommandScopeChatAdministrators as BotCommandScopeChatAdministrators
from tele_rest.models.bot_command_scope_chat_member import BotCommandScopeChatMember as BotCommandScopeChatMember
from tele_rest.models.bot_command_scope_default import BotCommandScopeDefault as BotCommandScopeDefault
from tele_rest.models.bot_description import BotDescription as BotDescription
from tele_rest.models.bot_name import BotName as BotName
from tele_rest.models.bot_short_description import BotShortDescription as BotShortDescription
from tele_rest.models.business_bot_rights import BusinessBotRights as BusinessBotRights
from tele_rest.models.business_connection import BusinessConnection as BusinessConnection
from tele_rest.models.business_intro import BusinessIntro as BusinessIntro
from tele_rest.models.business_location import BusinessLocation as BusinessLocation
from tele_rest.models.business_messages_deleted import BusinessMessagesDeleted as BusinessMessagesDeleted
from tele_rest.models.business_opening_hours import BusinessOpeningHours as BusinessOpeningHours
from tele_rest.models.business_opening_hours_interval import BusinessOpeningHoursInterval as BusinessOpeningHoursInterval
from tele_rest.models.callback_query import CallbackQuery as CallbackQuery
from tele_rest.models.chat import Chat as Chat
from tele_rest.models.chat_administrator_rights import ChatAdministratorRights as ChatAdministratorRights
from tele_rest.models.chat_background import ChatBackground as ChatBackground
from tele_rest.models.chat_boost import ChatBoost as ChatBoost
from tele_rest.models.chat_boost_added import ChatBoostAdded as ChatBoostAdded
from tele_rest.models.chat_boost_removed import ChatBoostRemoved as ChatBoostRemoved
from tele_rest.models.chat_boost_source import ChatBoostSource as ChatBoostSource
from tele_rest.models.chat_boost_source_gift_code import ChatBoostSourceGiftCode as ChatBoostSourceGiftCode
from tele_rest.models.chat_boost_source_giveaway import ChatBoostSourceGiveaway as ChatBoostSourceGiveaway
from tele_rest.models.chat_boost_source_premium import ChatBoostSourcePremium as ChatBoostSourcePremium
from tele_rest.models.chat_boost_updated import ChatBoostUpdated as ChatBoostUpdated
from tele_rest.models.chat_full_info import ChatFullInfo as ChatFullInfo
from tele_rest.models.chat_invite_link import ChatInviteLink as ChatInviteLink
from tele_rest.models.chat_join_request import ChatJoinRequest as ChatJoinRequest
from tele_rest.models.chat_location import ChatLocation as ChatLocation
from tele_rest.models.chat_member import ChatMember as ChatMember
from tele_rest.models.chat_member_administrator import ChatMemberAdministrator as ChatMemberAdministrator
from tele_rest.models.chat_member_banned import ChatMemberBanned as ChatMemberBanned
from tele_rest.models.chat_member_left import ChatMemberLeft as ChatMemberLeft
from tele_rest.models.chat_member_member import ChatMemberMember as ChatMemberMember
from tele_rest.models.chat_member_owner import ChatMemberOwner as ChatMemberOwner
from tele_rest.models.chat_member_restricted import ChatMemberRestricted as ChatMemberRestricted
from tele_rest.models.chat_member_updated import ChatMemberUpdated as ChatMemberUpdated
from tele_rest.models.chat_permissions import ChatPermissions as ChatPermissions
from tele_rest.models.chat_photo import ChatPhoto as ChatPhoto
from tele_rest.models.chat_shared import ChatShared as ChatShared
from tele_rest.models.chosen_inline_result import ChosenInlineResult as ChosenInlineResult
from tele_rest.models.contact import Contact as Contact
from tele_rest.models.copy_text_button import CopyTextButton as CopyTextButton
from tele_rest.models.dice import Dice as Dice
from tele_rest.models.document import Document as Document
from tele_rest.models.encrypted_credentials import EncryptedCredentials as EncryptedCredentials
from tele_rest.models.encrypted_passport_element import EncryptedPassportElement as EncryptedPassportElement
from tele_rest.models.error import Error as Error
from tele_rest.models.external_reply_info import ExternalReplyInfo as ExternalReplyInfo
from tele_rest.models.file import File as File
from tele_rest.models.force_reply import ForceReply as ForceReply
from tele_rest.models.forum_topic import ForumTopic as ForumTopic
from tele_rest.models.forum_topic_created import ForumTopicCreated as ForumTopicCreated
from tele_rest.models.forum_topic_edited import ForumTopicEdited as ForumTopicEdited
from tele_rest.models.game import Game as Game
from tele_rest.models.game_high_score import GameHighScore as GameHighScore
from tele_rest.models.gift import Gift as Gift
from tele_rest.models.gift_info import GiftInfo as GiftInfo
from tele_rest.models.gifts import Gifts as Gifts
from tele_rest.models.giveaway import Giveaway as Giveaway
from tele_rest.models.giveaway_completed import GiveawayCompleted as GiveawayCompleted
from tele_rest.models.giveaway_created import GiveawayCreated as GiveawayCreated
from tele_rest.models.giveaway_winners import GiveawayWinners as GiveawayWinners
from tele_rest.models.inaccessible_message import InaccessibleMessage as InaccessibleMessage
from tele_rest.models.inline_keyboard_button import InlineKeyboardButton as InlineKeyboardButton
from tele_rest.models.inline_keyboard_markup import InlineKeyboardMarkup as InlineKeyboardMarkup
from tele_rest.models.inline_query import InlineQuery as InlineQuery
from tele_rest.models.inline_query_result import InlineQueryResult as InlineQueryResult
from tele_rest.models.inline_query_result_article import InlineQueryResultArticle as InlineQueryResultArticle
from tele_rest.models.inline_query_result_audio import InlineQueryResultAudio as InlineQueryResultAudio
from tele_rest.models.inline_query_result_cached_audio import InlineQueryResultCachedAudio as InlineQueryResultCachedAudio
from tele_rest.models.inline_query_result_cached_document import InlineQueryResultCachedDocument as InlineQueryResultCachedDocument
from tele_rest.models.inline_query_result_cached_gif import InlineQueryResultCachedGif as InlineQueryResultCachedGif
from tele_rest.models.inline_query_result_cached_mpeg4_gif import InlineQueryResultCachedMpeg4Gif as InlineQueryResultCachedMpeg4Gif
from tele_rest.models.inline_query_result_cached_photo import InlineQueryResultCachedPhoto as InlineQueryResultCachedPhoto
from tele_rest.models.inline_query_result_cached_sticker import InlineQueryResultCachedSticker as InlineQueryResultCachedSticker
from tele_rest.models.inline_query_result_cached_video import InlineQueryResultCachedVideo as InlineQueryResultCachedVideo
from tele_rest.models.inline_query_result_cached_voice import InlineQueryResultCachedVoice as InlineQueryResultCachedVoice
from tele_rest.models.inline_query_result_contact import InlineQueryResultContact as InlineQueryResultContact
from tele_rest.models.inline_query_result_document import InlineQueryResultDocument as InlineQueryResultDocument
from tele_rest.models.inline_query_result_game import InlineQueryResultGame as InlineQueryResultGame
from tele_rest.models.inline_query_result_gif import InlineQueryResultGif as InlineQueryResultGif
from tele_rest.models.inline_query_result_location import InlineQueryResultLocation as InlineQueryResultLocation
from tele_rest.models.inline_query_result_mpeg4_gif import InlineQueryResultMpeg4Gif as InlineQueryResultMpeg4Gif
from tele_rest.models.inline_query_result_photo import InlineQueryResultPhoto as InlineQueryResultPhoto
from tele_rest.models.inline_query_result_venue import InlineQueryResultVenue as InlineQueryResultVenue
from tele_rest.models.inline_query_result_video import InlineQueryResultVideo as InlineQueryResultVideo
from tele_rest.models.inline_query_result_voice import InlineQueryResultVoice as InlineQueryResultVoice
from tele_rest.models.inline_query_results_button import InlineQueryResultsButton as InlineQueryResultsButton
from tele_rest.models.input_contact_message_content import InputContactMessageContent as InputContactMessageContent
from tele_rest.models.input_invoice_message_content import InputInvoiceMessageContent as InputInvoiceMessageContent
from tele_rest.models.input_location_message_content import InputLocationMessageContent as InputLocationMessageContent
from tele_rest.models.input_media import InputMedia as InputMedia
from tele_rest.models.input_media_animation import InputMediaAnimation as InputMediaAnimation
from tele_rest.models.input_media_audio import InputMediaAudio as InputMediaAudio
from tele_rest.models.input_media_document import InputMediaDocument as InputMediaDocument
from tele_rest.models.input_media_photo import InputMediaPhoto as InputMediaPhoto
from tele_rest.models.input_media_video import InputMediaVideo as InputMediaVideo
from tele_rest.models.input_message_content import InputMessageContent as InputMessageContent
from tele_rest.models.input_paid_media import InputPaidMedia as InputPaidMedia
from tele_rest.models.input_paid_media_photo import InputPaidMediaPhoto as InputPaidMediaPhoto
from tele_rest.models.input_paid_media_video import InputPaidMediaVideo as InputPaidMediaVideo
from tele_rest.models.input_poll_option import InputPollOption as InputPollOption
from tele_rest.models.input_profile_photo import InputProfilePhoto as InputProfilePhoto
from tele_rest.models.input_profile_photo_animated import InputProfilePhotoAnimated as InputProfilePhotoAnimated
from tele_rest.models.input_profile_photo_static import InputProfilePhotoStatic as InputProfilePhotoStatic
from tele_rest.models.input_sticker import InputSticker as InputSticker
from tele_rest.models.input_story_content import InputStoryContent as InputStoryContent
from tele_rest.models.input_story_content_photo import InputStoryContentPhoto as InputStoryContentPhoto
from tele_rest.models.input_story_content_video import InputStoryContentVideo as InputStoryContentVideo
from tele_rest.models.input_text_message_content import InputTextMessageContent as InputTextMessageContent
from tele_rest.models.input_venue_message_content import InputVenueMessageContent as InputVenueMessageContent
from tele_rest.models.invoice import Invoice as Invoice
from tele_rest.models.keyboard_button import KeyboardButton as KeyboardButton
from tele_rest.models.keyboard_button_poll_type import KeyboardButtonPollType as KeyboardButtonPollType
from tele_rest.models.keyboard_button_request_chat import KeyboardButtonRequestChat as KeyboardButtonRequestChat
from tele_rest.models.keyboard_button_request_users import KeyboardButtonRequestUsers as KeyboardButtonRequestUsers
from tele_rest.models.labeled_price import LabeledPrice as LabeledPrice
from tele_rest.models.link_preview_options import LinkPreviewOptions as LinkPreviewOptions
from tele_rest.models.location import Location as Location
from tele_rest.models.location_address import LocationAddress as LocationAddress
from tele_rest.models.login_url import LoginUrl as LoginUrl
from tele_rest.models.mask_position import MaskPosition as MaskPosition
from tele_rest.models.maybe_inaccessible_message import MaybeInaccessibleMessage as MaybeInaccessibleMessage
from tele_rest.models.menu_button import MenuButton as MenuButton
from tele_rest.models.menu_button_commands import MenuButtonCommands as MenuButtonCommands
from tele_rest.models.menu_button_default import MenuButtonDefault as MenuButtonDefault
from tele_rest.models.menu_button_web_app import MenuButtonWebApp as MenuButtonWebApp
from tele_rest.models.message import Message as Message
from tele_rest.models.message_auto_delete_timer_changed import MessageAutoDeleteTimerChanged as MessageAutoDeleteTimerChanged
from tele_rest.models.message_entity import MessageEntity as MessageEntity
from tele_rest.models.message_id import MessageId as MessageId
from tele_rest.models.message_origin import MessageOrigin as MessageOrigin
from tele_rest.models.message_origin_channel import MessageOriginChannel as MessageOriginChannel
from tele_rest.models.message_origin_chat import MessageOriginChat as MessageOriginChat
from tele_rest.models.message_origin_hidden_user import MessageOriginHiddenUser as MessageOriginHiddenUser
from tele_rest.models.message_origin_user import MessageOriginUser as MessageOriginUser
from tele_rest.models.message_reaction_count_updated import MessageReactionCountUpdated as MessageReactionCountUpdated
from tele_rest.models.message_reaction_updated import MessageReactionUpdated as MessageReactionUpdated
from tele_rest.models.order_info import OrderInfo as OrderInfo
from tele_rest.models.owned_gift import OwnedGift as OwnedGift
from tele_rest.models.owned_gift_regular import OwnedGiftRegular as OwnedGiftRegular
from tele_rest.models.owned_gift_unique import OwnedGiftUnique as OwnedGiftUnique
from tele_rest.models.owned_gifts import OwnedGifts as OwnedGifts
from tele_rest.models.paid_media import PaidMedia as PaidMedia
from tele_rest.models.paid_media_info import PaidMediaInfo as PaidMediaInfo
from tele_rest.models.paid_media_photo import PaidMediaPhoto as PaidMediaPhoto
from tele_rest.models.paid_media_preview import PaidMediaPreview as PaidMediaPreview
from tele_rest.models.paid_media_purchased import PaidMediaPurchased as PaidMediaPurchased
from tele_rest.models.paid_media_video import PaidMediaVideo as PaidMediaVideo
from tele_rest.models.paid_message_price_changed import PaidMessagePriceChanged as PaidMessagePriceChanged
from tele_rest.models.passport_data import PassportData as PassportData
from tele_rest.models.passport_element_error import PassportElementError as PassportElementError
from tele_rest.models.passport_element_error_data_field import PassportElementErrorDataField as PassportElementErrorDataField
from tele_rest.models.passport_element_error_file import PassportElementErrorFile as PassportElementErrorFile
from tele_rest.models.passport_element_error_files import PassportElementErrorFiles as PassportElementErrorFiles
from tele_rest.models.passport_element_error_front_side import PassportElementErrorFrontSide as PassportElementErrorFrontSide
from tele_rest.models.passport_element_error_reverse_side import PassportElementErrorReverseSide as PassportElementErrorReverseSide
from tele_rest.models.passport_element_error_selfie import PassportElementErrorSelfie as PassportElementErrorSelfie
from tele_rest.models.passport_element_error_translation_file import PassportElementErrorTranslationFile as PassportElementErrorTranslationFile
from tele_rest.models.passport_element_error_translation_files import PassportElementErrorTranslationFiles as PassportElementErrorTranslationFiles
from tele_rest.models.passport_element_error_unspecified import PassportElementErrorUnspecified as PassportElementErrorUnspecified
from tele_rest.models.passport_file import PassportFile as PassportFile
from tele_rest.models.photo_size import PhotoSize as PhotoSize
from tele_rest.models.poll import Poll as Poll
from tele_rest.models.poll_answer import PollAnswer as PollAnswer
from tele_rest.models.poll_option import PollOption as PollOption
from tele_rest.models.post_answer_callback_query_request import PostAnswerCallbackQueryRequest as PostAnswerCallbackQueryRequest
from tele_rest.models.post_answer_inline_query_request import PostAnswerInlineQueryRequest as PostAnswerInlineQueryRequest
from tele_rest.models.post_answer_pre_checkout_query_request import PostAnswerPreCheckoutQueryRequest as PostAnswerPreCheckoutQueryRequest
from tele_rest.models.post_answer_shipping_query_request import PostAnswerShippingQueryRequest as PostAnswerShippingQueryRequest
from tele_rest.models.post_answer_web_app_query200_response import PostAnswerWebAppQuery200Response as PostAnswerWebAppQuery200Response
from tele_rest.models.post_answer_web_app_query_request import PostAnswerWebAppQueryRequest as PostAnswerWebAppQueryRequest
from tele_rest.models.post_approve_chat_join_request_request import PostApproveChatJoinRequestRequest as PostApproveChatJoinRequestRequest
from tele_rest.models.post_ban_chat_member_request import PostBanChatMemberRequest as PostBanChatMemberRequest
from tele_rest.models.post_ban_chat_member_request_chat_id import PostBanChatMemberRequestChatId as PostBanChatMemberRequestChatId
from tele_rest.models.post_ban_chat_sender_chat_request import PostBanChatSenderChatRequest as PostBanChatSenderChatRequest
from tele_rest.models.post_close_forum_topic_request import PostCloseForumTopicRequest as PostCloseForumTopicRequest
from tele_rest.models.post_convert_gift_to_stars_request import PostConvertGiftToStarsRequest as PostConvertGiftToStarsRequest
from tele_rest.models.post_copy_message200_response import PostCopyMessage200Response as PostCopyMessage200Response
from tele_rest.models.post_copy_message_request import PostCopyMessageRequest as PostCopyMessageRequest
from tele_rest.models.post_copy_messages_request import PostCopyMessagesRequest as PostCopyMessagesRequest
from tele_rest.models.post_create_chat_invite_link200_response import PostCreateChatInviteLink200Response as PostCreateChatInviteLink200Response
from tele_rest.models.post_create_chat_invite_link_request import PostCreateChatInviteLinkRequest as PostCreateChatInviteLinkRequest
from tele_rest.models.post_create_chat_subscription_invite_link_request import PostCreateChatSubscriptionInviteLinkRequest as PostCreateChatSubscriptionInviteLinkRequest
from tele_rest.models.post_create_chat_subscription_invite_link_request_chat_id import PostCreateChatSubscriptionInviteLinkRequestChatId as PostCreateChatSubscriptionInviteLinkRequestChatId
from tele_rest.models.post_create_forum_topic200_response import PostCreateForumTopic200Response as PostCreateForumTopic200Response
from tele_rest.models.post_create_forum_topic_request import PostCreateForumTopicRequest as PostCreateForumTopicRequest
from tele_rest.models.post_create_invoice_link_request import PostCreateInvoiceLinkRequest as PostCreateInvoiceLinkRequest
from tele_rest.models.post_delete_business_messages_request import PostDeleteBusinessMessagesRequest as PostDeleteBusinessMessagesRequest
from tele_rest.models.post_delete_chat_sticker_set_request import PostDeleteChatStickerSetRequest as PostDeleteChatStickerSetRequest
from tele_rest.models.post_delete_message_request import PostDeleteMessageRequest as PostDeleteMessageRequest
from tele_rest.models.post_delete_messages_request import PostDeleteMessagesRequest as PostDeleteMessagesRequest
from tele_rest.models.post_delete_my_commands_request import PostDeleteMyCommandsRequest as PostDeleteMyCommandsRequest
from tele_rest.models.post_delete_sticker_from_set_request import PostDeleteStickerFromSetRequest as PostDeleteStickerFromSetRequest
from tele_rest.models.post_delete_sticker_set_request import PostDeleteStickerSetRequest as PostDeleteStickerSetRequest
from tele_rest.models.post_delete_story_request import PostDeleteStoryRequest as PostDeleteStoryRequest
from tele_rest.models.post_delete_webhook_request import PostDeleteWebhookRequest as PostDeleteWebhookRequest
from tele_rest.models.post_edit_chat_invite_link_request import PostEditChatInviteLinkRequest as PostEditChatInviteLinkRequest
from tele_rest.models.post_edit_chat_subscription_invite_link_request import PostEditChatSubscriptionInviteLinkRequest as PostEditChatSubscriptionInviteLinkRequest
from tele_rest.models.post_edit_forum_topic_request import PostEditForumTopicRequest as PostEditForumTopicRequest
from tele_rest.models.post_edit_general_forum_topic_request import PostEditGeneralForumTopicRequest as PostEditGeneralForumTopicRequest
from tele_rest.models.post_edit_message_caption_request import PostEditMessageCaptionRequest as PostEditMessageCaptionRequest
from tele_rest.models.post_edit_message_live_location_request import PostEditMessageLiveLocationRequest as PostEditMessageLiveLocationRequest
from tele_rest.models.post_edit_message_reply_markup_request import PostEditMessageReplyMarkupRequest as PostEditMessageReplyMarkupRequest
from tele_rest.models.post_edit_message_text200_response import PostEditMessageText200Response as PostEditMessageText200Response
from tele_rest.models.post_edit_message_text200_response_result import PostEditMessageText200ResponseResult as PostEditMessageText200ResponseResult
from tele_rest.models.post_edit_message_text_request import PostEditMessageTextRequest as PostEditMessageTextRequest
from tele_rest.models.post_edit_message_text_request_chat_id import PostEditMessageTextRequestChatId as PostEditMessageTextRequestChatId
from tele_rest.models.post_edit_user_star_subscription_request import PostEditUserStarSubscriptionRequest as PostEditUserStarSubscriptionRequest
from tele_rest.models.post_export_chat_invite_link200_response import PostExportChatInviteLink200Response as PostExportChatInviteLink200Response
from tele_rest.models.post_export_chat_invite_link_request import PostExportChatInviteLinkRequest as PostExportChatInviteLinkRequest
from tele_rest.models.post_forward_message_request import PostForwardMessageRequest as PostForwardMessageRequest
from tele_rest.models.post_forward_message_request_from_chat_id import PostForwardMessageRequestFromChatId as PostForwardMessageRequestFromChatId
from tele_rest.models.post_forward_messages200_response import PostForwardMessages200Response as PostForwardMessages200Response
from tele_rest.models.post_forward_messages_request import PostForwardMessagesRequest as PostForwardMessagesRequest
from tele_rest.models.post_forward_messages_request_from_chat_id import PostForwardMessagesRequestFromChatId as PostForwardMessagesRequestFromChatId
from tele_rest.models.post_get_available_gifts200_response import PostGetAvailableGifts200Response as PostGetAvailableGifts200Response
from tele_rest.models.post_get_business_account_gifts200_response import PostGetBusinessAccountGifts200Response as PostGetBusinessAccountGifts200Response
from tele_rest.models.post_get_business_account_gifts_request import PostGetBusinessAccountGiftsRequest as PostGetBusinessAccountGiftsRequest
from tele_rest.models.post_get_business_account_star_balance200_response import PostGetBusinessAccountStarBalance200Response as PostGetBusinessAccountStarBalance200Response
from tele_rest.models.post_get_business_connection200_response import PostGetBusinessConnection200Response as PostGetBusinessConnection200Response
from tele_rest.models.post_get_business_connection_request import PostGetBusinessConnectionRequest as PostGetBusinessConnectionRequest
from tele_rest.models.post_get_chat200_response import PostGetChat200Response as PostGetChat200Response
from tele_rest.models.post_get_chat_administrators200_response import PostGetChatAdministrators200Response as PostGetChatAdministrators200Response
from tele_rest.models.post_get_chat_member200_response import PostGetChatMember200Response as PostGetChatMember200Response
from tele_rest.models.post_get_chat_member_count200_response import PostGetChatMemberCount200Response as PostGetChatMemberCount200Response
from tele_rest.models.post_get_chat_member_request import PostGetChatMemberRequest as PostGetChatMemberRequest
from tele_rest.models.post_get_chat_menu_button200_response import PostGetChatMenuButton200Response as PostGetChatMenuButton200Response
from tele_rest.models.post_get_chat_menu_button_request import PostGetChatMenuButtonRequest as PostGetChatMenuButtonRequest
from tele_rest.models.post_get_custom_emoji_stickers_request import PostGetCustomEmojiStickersRequest as PostGetCustomEmojiStickersRequest
from tele_rest.models.post_get_file200_response import PostGetFile200Response as PostGetFile200Response
from tele_rest.models.post_get_file_request import PostGetFileRequest as PostGetFileRequest
from tele_rest.models.post_get_forum_topic_icon_stickers200_response import PostGetForumTopicIconStickers200Response as PostGetForumTopicIconStickers200Response
from tele_rest.models.post_get_game_high_scores200_response import PostGetGameHighScores200Response as PostGetGameHighScores200Response
from tele_rest.models.post_get_game_high_scores_request import PostGetGameHighScoresRequest as PostGetGameHighScoresRequest
from tele_rest.models.post_get_me200_response import PostGetMe200Response as PostGetMe200Response
from tele_rest.models.post_get_my_commands200_response import PostGetMyCommands200Response as PostGetMyCommands200Response
from tele_rest.models.post_get_my_commands_request import PostGetMyCommandsRequest as PostGetMyCommandsRequest
from tele_rest.models.post_get_my_default_administrator_rights200_response import PostGetMyDefaultAdministratorRights200Response as PostGetMyDefaultAdministratorRights200Response
from tele_rest.models.post_get_my_default_administrator_rights_request import PostGetMyDefaultAdministratorRightsRequest as PostGetMyDefaultAdministratorRightsRequest
from tele_rest.models.post_get_my_description200_response import PostGetMyDescription200Response as PostGetMyDescription200Response
from tele_rest.models.post_get_my_name200_response import PostGetMyName200Response as PostGetMyName200Response
from tele_rest.models.post_get_my_name_request import PostGetMyNameRequest as PostGetMyNameRequest
from tele_rest.models.post_get_my_short_description200_response import PostGetMyShortDescription200Response as PostGetMyShortDescription200Response
from tele_rest.models.post_get_star_transactions200_response import PostGetStarTransactions200Response as PostGetStarTransactions200Response
from tele_rest.models.post_get_star_transactions_request import PostGetStarTransactionsRequest as PostGetStarTransactionsRequest
from tele_rest.models.post_get_sticker_set200_response import PostGetStickerSet200Response as PostGetStickerSet200Response
from tele_rest.models.post_get_sticker_set_request import PostGetStickerSetRequest as PostGetStickerSetRequest
from tele_rest.models.post_get_updates200_response import PostGetUpdates200Response as PostGetUpdates200Response
from tele_rest.models.post_get_updates_request import PostGetUpdatesRequest as PostGetUpdatesRequest
from tele_rest.models.post_get_user_chat_boosts200_response import PostGetUserChatBoosts200Response as PostGetUserChatBoosts200Response
from tele_rest.models.post_get_user_chat_boosts_request import PostGetUserChatBoostsRequest as PostGetUserChatBoostsRequest
from tele_rest.models.post_get_user_chat_boosts_request_chat_id import PostGetUserChatBoostsRequestChatId as PostGetUserChatBoostsRequestChatId
from tele_rest.models.post_get_user_profile_photos200_response import PostGetUserProfilePhotos200Response as PostGetUserProfilePhotos200Response
from tele_rest.models.post_get_user_profile_photos_request import PostGetUserProfilePhotosRequest as PostGetUserProfilePhotosRequest
from tele_rest.models.post_get_webhook_info200_response import PostGetWebhookInfo200Response as PostGetWebhookInfo200Response
from tele_rest.models.post_gift_premium_subscription_request import PostGiftPremiumSubscriptionRequest as PostGiftPremiumSubscriptionRequest
from tele_rest.models.post_leave_chat_request import PostLeaveChatRequest as PostLeaveChatRequest
from tele_rest.models.post_leave_chat_request_chat_id import PostLeaveChatRequestChatId as PostLeaveChatRequestChatId
from tele_rest.models.post_pin_chat_message_request import PostPinChatMessageRequest as PostPinChatMessageRequest
from tele_rest.models.post_post_story200_response import PostPostStory200Response as PostPostStory200Response
from tele_rest.models.post_promote_chat_member_request import PostPromoteChatMemberRequest as PostPromoteChatMemberRequest
from tele_rest.models.post_read_business_message_request import PostReadBusinessMessageRequest as PostReadBusinessMessageRequest
from tele_rest.models.post_refund_star_payment_request import PostRefundStarPaymentRequest as PostRefundStarPaymentRequest
from tele_rest.models.post_remove_business_account_profile_photo_request import PostRemoveBusinessAccountProfilePhotoRequest as PostRemoveBusinessAccountProfilePhotoRequest
from tele_rest.models.post_remove_user_verification_request import PostRemoveUserVerificationRequest as PostRemoveUserVerificationRequest
from tele_rest.models.post_restrict_chat_member_request import PostRestrictChatMemberRequest as PostRestrictChatMemberRequest
from tele_rest.models.post_restrict_chat_member_request_chat_id import PostRestrictChatMemberRequestChatId as PostRestrictChatMemberRequestChatId
from tele_rest.models.post_revoke_chat_invite_link_request import PostRevokeChatInviteLinkRequest as PostRevokeChatInviteLinkRequest
from tele_rest.models.post_revoke_chat_invite_link_request_chat_id import PostRevokeChatInviteLinkRequestChatId as PostRevokeChatInviteLinkRequestChatId
from tele_rest.models.post_save_prepared_inline_message200_response import PostSavePreparedInlineMessage200Response as PostSavePreparedInlineMessage200Response
from tele_rest.models.post_save_prepared_inline_message_request import PostSavePreparedInlineMessageRequest as PostSavePreparedInlineMessageRequest
from tele_rest.models.post_send_animation_request_animation import PostSendAnimationRequestAnimation as PostSendAnimationRequestAnimation
from tele_rest.models.post_send_audio_request_audio import PostSendAudioRequestAudio as PostSendAudioRequestAudio
from tele_rest.models.post_send_audio_request_thumbnail import PostSendAudioRequestThumbnail as PostSendAudioRequestThumbnail
from tele_rest.models.post_send_chat_action_request import PostSendChatActionRequest as PostSendChatActionRequest
from tele_rest.models.post_send_contact_request import PostSendContactRequest as PostSendContactRequest
from tele_rest.models.post_send_dice_request import PostSendDiceRequest as PostSendDiceRequest
from tele_rest.models.post_send_document_request_document import PostSendDocumentRequestDocument as PostSendDocumentRequestDocument
from tele_rest.models.post_send_game_request import PostSendGameRequest as PostSendGameRequest
from tele_rest.models.post_send_gift_request import PostSendGiftRequest as PostSendGiftRequest
from tele_rest.models.post_send_gift_request_chat_id import PostSendGiftRequestChatId as PostSendGiftRequestChatId
from tele_rest.models.post_send_invoice_request import PostSendInvoiceRequest as PostSendInvoiceRequest
from tele_rest.models.post_send_location_request import PostSendLocationRequest as PostSendLocationRequest
from tele_rest.models.post_send_media_group200_response import PostSendMediaGroup200Response as PostSendMediaGroup200Response
from tele_rest.models.post_send_media_group_request_media_inner import PostSendMediaGroupRequestMediaInner as PostSendMediaGroupRequestMediaInner
from tele_rest.models.post_send_message200_response import PostSendMessage200Response as PostSendMessage200Response
from tele_rest.models.post_send_message_request import PostSendMessageRequest as PostSendMessageRequest
from tele_rest.models.post_send_message_request_chat_id import PostSendMessageRequestChatId as PostSendMessageRequestChatId
from tele_rest.models.post_send_message_request_reply_markup import PostSendMessageRequestReplyMarkup as PostSendMessageRequestReplyMarkup
from tele_rest.models.post_send_paid_media_request_chat_id import PostSendPaidMediaRequestChatId as PostSendPaidMediaRequestChatId
from tele_rest.models.post_send_photo_request_photo import PostSendPhotoRequestPhoto as PostSendPhotoRequestPhoto
from tele_rest.models.post_send_poll_request import PostSendPollRequest as PostSendPollRequest
from tele_rest.models.post_send_sticker_request_sticker import PostSendStickerRequestSticker as PostSendStickerRequestSticker
from tele_rest.models.post_send_venue_request import PostSendVenueRequest as PostSendVenueRequest
from tele_rest.models.post_send_video_note_request_video_note import PostSendVideoNoteRequestVideoNote as PostSendVideoNoteRequestVideoNote
from tele_rest.models.post_send_video_request_cover import PostSendVideoRequestCover as PostSendVideoRequestCover
from tele_rest.models.post_send_video_request_video import PostSendVideoRequestVideo as PostSendVideoRequestVideo
from tele_rest.models.post_send_voice_request_voice import PostSendVoiceRequestVoice as PostSendVoiceRequestVoice
from tele_rest.models.post_set_business_account_bio_request import PostSetBusinessAccountBioRequest as PostSetBusinessAccountBioRequest
from tele_rest.models.post_set_business_account_gift_settings_request import PostSetBusinessAccountGiftSettingsRequest as PostSetBusinessAccountGiftSettingsRequest
from tele_rest.models.post_set_business_account_name_request import PostSetBusinessAccountNameRequest as PostSetBusinessAccountNameRequest
from tele_rest.models.post_set_business_account_username_request import PostSetBusinessAccountUsernameRequest as PostSetBusinessAccountUsernameRequest
from tele_rest.models.post_set_chat_administrator_custom_title_request import PostSetChatAdministratorCustomTitleRequest as PostSetChatAdministratorCustomTitleRequest
from tele_rest.models.post_set_chat_description_request import PostSetChatDescriptionRequest as PostSetChatDescriptionRequest
from tele_rest.models.post_set_chat_menu_button_request import PostSetChatMenuButtonRequest as PostSetChatMenuButtonRequest
from tele_rest.models.post_set_chat_permissions_request import PostSetChatPermissionsRequest as PostSetChatPermissionsRequest
from tele_rest.models.post_set_chat_sticker_set_request import PostSetChatStickerSetRequest as PostSetChatStickerSetRequest
from tele_rest.models.post_set_chat_title_request import PostSetChatTitleRequest as PostSetChatTitleRequest
from tele_rest.models.post_set_custom_emoji_sticker_set_thumbnail_request import PostSetCustomEmojiStickerSetThumbnailRequest as PostSetCustomEmojiStickerSetThumbnailRequest
from tele_rest.models.post_set_game_score_request import PostSetGameScoreRequest as PostSetGameScoreRequest
from tele_rest.models.post_set_message_reaction_request import PostSetMessageReactionRequest as PostSetMessageReactionRequest
from tele_rest.models.post_set_my_commands_request import PostSetMyCommandsRequest as PostSetMyCommandsRequest
from tele_rest.models.post_set_my_default_administrator_rights_request import PostSetMyDefaultAdministratorRightsRequest as PostSetMyDefaultAdministratorRightsRequest
from tele_rest.models.post_set_my_description_request import PostSetMyDescriptionRequest as PostSetMyDescriptionRequest
from tele_rest.models.post_set_my_name_request import PostSetMyNameRequest as PostSetMyNameRequest
from tele_rest.models.post_set_my_short_description_request import PostSetMyShortDescriptionRequest as PostSetMyShortDescriptionRequest
from tele_rest.models.post_set_passport_data_errors_request import PostSetPassportDataErrorsRequest as PostSetPassportDataErrorsRequest
from tele_rest.models.post_set_sticker_emoji_list_request import PostSetStickerEmojiListRequest as PostSetStickerEmojiListRequest
from tele_rest.models.post_set_sticker_keywords_request import PostSetStickerKeywordsRequest as PostSetStickerKeywordsRequest
from tele_rest.models.post_set_sticker_mask_position_request import PostSetStickerMaskPositionRequest as PostSetStickerMaskPositionRequest
from tele_rest.models.post_set_sticker_position_in_set_request import PostSetStickerPositionInSetRequest as PostSetStickerPositionInSetRequest
from tele_rest.models.post_set_sticker_set_thumbnail_request_thumbnail import PostSetStickerSetThumbnailRequestThumbnail as PostSetStickerSetThumbnailRequestThumbnail
from tele_rest.models.post_set_sticker_set_title_request import PostSetStickerSetTitleRequest as PostSetStickerSetTitleRequest
from tele_rest.models.post_set_user_emoji_status_request import PostSetUserEmojiStatusRequest as PostSetUserEmojiStatusRequest
from tele_rest.models.post_set_webhook200_response import PostSetWebhook200Response as PostSetWebhook200Response
from tele_rest.models.post_stop_message_live_location_request import PostStopMessageLiveLocationRequest as PostStopMessageLiveLocationRequest
from tele_rest.models.post_stop_poll200_response import PostStopPoll200Response as PostStopPoll200Response
from tele_rest.models.post_stop_poll_request import PostStopPollRequest as PostStopPollRequest
from tele_rest.models.post_transfer_business_account_stars_request import PostTransferBusinessAccountStarsRequest as PostTransferBusinessAccountStarsRequest
from tele_rest.models.post_transfer_gift_request import PostTransferGiftRequest as PostTransferGiftRequest
from tele_rest.models.post_unban_chat_member_request import PostUnbanChatMemberRequest as PostUnbanChatMemberRequest
from tele_rest.models.post_unpin_chat_message_request import PostUnpinChatMessageRequest as PostUnpinChatMessageRequest
from tele_rest.models.post_upgrade_gift_request import PostUpgradeGiftRequest as PostUpgradeGiftRequest
from tele_rest.models.post_verify_chat_request import PostVerifyChatRequest as PostVerifyChatRequest
from tele_rest.models.post_verify_user_request import PostVerifyUserRequest as PostVerifyUserRequest
from tele_rest.models.pre_checkout_query import PreCheckoutQuery as PreCheckoutQuery
from tele_rest.models.prepared_inline_message import PreparedInlineMessage as PreparedInlineMessage
from tele_rest.models.proximity_alert_triggered import ProximityAlertTriggered as ProximityAlertTriggered
from tele_rest.models.reaction_count import ReactionCount as ReactionCount
from tele_rest.models.reaction_type import ReactionType as ReactionType
from tele_rest.models.reaction_type_custom_emoji import ReactionTypeCustomEmoji as ReactionTypeCustomEmoji
from tele_rest.models.reaction_type_emoji import ReactionTypeEmoji as ReactionTypeEmoji
from tele_rest.models.reaction_type_paid import ReactionTypePaid as ReactionTypePaid
from tele_rest.models.refunded_payment import RefundedPayment as RefundedPayment
from tele_rest.models.reply_keyboard_markup import ReplyKeyboardMarkup as ReplyKeyboardMarkup
from tele_rest.models.reply_keyboard_remove import ReplyKeyboardRemove as ReplyKeyboardRemove
from tele_rest.models.reply_parameters import ReplyParameters as ReplyParameters
from tele_rest.models.reply_parameters_chat_id import ReplyParametersChatId as ReplyParametersChatId
from tele_rest.models.response_parameters import ResponseParameters as ResponseParameters
from tele_rest.models.revenue_withdrawal_state import RevenueWithdrawalState as RevenueWithdrawalState
from tele_rest.models.revenue_withdrawal_state_failed import RevenueWithdrawalStateFailed as RevenueWithdrawalStateFailed
from tele_rest.models.revenue_withdrawal_state_pending import RevenueWithdrawalStatePending as RevenueWithdrawalStatePending
from tele_rest.models.revenue_withdrawal_state_succeeded import RevenueWithdrawalStateSucceeded as RevenueWithdrawalStateSucceeded
from tele_rest.models.sent_web_app_message import SentWebAppMessage as SentWebAppMessage
from tele_rest.models.shared_user import SharedUser as SharedUser
from tele_rest.models.shipping_address import ShippingAddress as ShippingAddress
from tele_rest.models.shipping_option import ShippingOption as ShippingOption
from tele_rest.models.shipping_query import ShippingQuery as ShippingQuery
from tele_rest.models.star_amount import StarAmount as StarAmount
from tele_rest.models.star_transaction import StarTransaction as StarTransaction
from tele_rest.models.star_transactions import StarTransactions as StarTransactions
from tele_rest.models.sticker import Sticker as Sticker
from tele_rest.models.sticker_set import StickerSet as StickerSet
from tele_rest.models.story import Story as Story
from tele_rest.models.story_area import StoryArea as StoryArea
from tele_rest.models.story_area_position import StoryAreaPosition as StoryAreaPosition
from tele_rest.models.story_area_type import StoryAreaType as StoryAreaType
from tele_rest.models.story_area_type_link import StoryAreaTypeLink as StoryAreaTypeLink
from tele_rest.models.story_area_type_location import StoryAreaTypeLocation as StoryAreaTypeLocation
from tele_rest.models.story_area_type_suggested_reaction import StoryAreaTypeSuggestedReaction as StoryAreaTypeSuggestedReaction
from tele_rest.models.story_area_type_unique_gift import StoryAreaTypeUniqueGift as StoryAreaTypeUniqueGift
from tele_rest.models.story_area_type_weather import StoryAreaTypeWeather as StoryAreaTypeWeather
from tele_rest.models.successful_payment import SuccessfulPayment as SuccessfulPayment
from tele_rest.models.switch_inline_query_chosen_chat import SwitchInlineQueryChosenChat as SwitchInlineQueryChosenChat
from tele_rest.models.text_quote import TextQuote as TextQuote
from tele_rest.models.transaction_partner import TransactionPartner as TransactionPartner
from tele_rest.models.transaction_partner_affiliate_program import TransactionPartnerAffiliateProgram as TransactionPartnerAffiliateProgram
from tele_rest.models.transaction_partner_chat import TransactionPartnerChat as TransactionPartnerChat
from tele_rest.models.transaction_partner_fragment import TransactionPartnerFragment as TransactionPartnerFragment
from tele_rest.models.transaction_partner_other import TransactionPartnerOther as TransactionPartnerOther
from tele_rest.models.transaction_partner_telegram_ads import TransactionPartnerTelegramAds as TransactionPartnerTelegramAds
from tele_rest.models.transaction_partner_telegram_api import TransactionPartnerTelegramApi as TransactionPartnerTelegramApi
from tele_rest.models.transaction_partner_user import TransactionPartnerUser as TransactionPartnerUser
from tele_rest.models.unique_gift import UniqueGift as UniqueGift
from tele_rest.models.unique_gift_backdrop import UniqueGiftBackdrop as UniqueGiftBackdrop
from tele_rest.models.unique_gift_backdrop_colors import UniqueGiftBackdropColors as UniqueGiftBackdropColors
from tele_rest.models.unique_gift_info import UniqueGiftInfo as UniqueGiftInfo
from tele_rest.models.unique_gift_model import UniqueGiftModel as UniqueGiftModel
from tele_rest.models.unique_gift_symbol import UniqueGiftSymbol as UniqueGiftSymbol
from tele_rest.models.update import Update as Update
from tele_rest.models.user import User as User
from tele_rest.models.user_chat_boosts import UserChatBoosts as UserChatBoosts
from tele_rest.models.user_profile_photos import UserProfilePhotos as UserProfilePhotos
from tele_rest.models.users_shared import UsersShared as UsersShared
from tele_rest.models.venue import Venue as Venue
from tele_rest.models.video import Video as Video
from tele_rest.models.video_chat_ended import VideoChatEnded as VideoChatEnded
from tele_rest.models.video_chat_participants_invited import VideoChatParticipantsInvited as VideoChatParticipantsInvited
from tele_rest.models.video_chat_scheduled import VideoChatScheduled as VideoChatScheduled
from tele_rest.models.video_note import VideoNote as VideoNote
from tele_rest.models.voice import Voice as Voice
from tele_rest.models.web_app_data import WebAppData as WebAppData
from tele_rest.models.web_app_info import WebAppInfo as WebAppInfo
from tele_rest.models.webhook_info import WebhookInfo as WebhookInfo
from tele_rest.models.write_access_allowed import WriteAccessAllowed as WriteAccessAllowed
