# coding: utf-8

# flake8: noqa

"""
Telegram Bot API - REST API Client
The Bot API is an HTTP-based interface created for developers keen on building bots for Telegram. To learn how to create and set up a bot, please consult our Introduction to Bots and Bot FAQ.

## Metadata

- **Copyright**: Copyright (c) 2025 Qntx
- **Author**: ΣX <gitctrlx@gmail.com>
- **Version**: 9.0.0
- **Modified**: 2025-07-02T09:16:58.218987030Z[Etc/UTC]
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
    "AddStickerToSetRequest",
    "AddStickerToSetResponse",
    "AffiliateInfo",
    "Animation",
    "AnswerCallbackQueryRequest",
    "AnswerCallbackQueryResponse",
    "AnswerInlineQueryRequest",
    "AnswerInlineQueryResponse",
    "AnswerPreCheckoutQueryRequest",
    "AnswerPreCheckoutQueryResponse",
    "AnswerShippingQueryRequest",
    "AnswerShippingQueryResponse",
    "AnswerWebAppQueryRequest",
    "AnswerWebAppQueryResponse",
    "ApproveChatJoinRequestRequest",
    "ApproveChatJoinRequestResponse",
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
    "BanChatMemberRequest",
    "BanChatMemberRequestChatId",
    "BanChatMemberResponse",
    "BanChatSenderChatRequest",
    "BanChatSenderChatResponse",
    "Birthdate",
    "BotCommand",
    "BotCommandScope",
    "BotCommandScopeAllChatAdministrators",
    "BotCommandScopeAllGroupChats",
    "BotCommandScopeAllPrivateChats",
    "BotCommandScopeChat",
    "BotCommandScopeChatAdministrators",
    "BotCommandScopeChatChatId",
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
    "CloseForumTopicRequest",
    "CloseForumTopicResponse",
    "CloseGeneralForumTopicRequest",
    "CloseGeneralForumTopicResponse",
    "CloseResponse",
    "Contact",
    "ConvertGiftToStarsRequest",
    "ConvertGiftToStarsResponse",
    "CopyMessageRequest",
    "CopyMessageResponse",
    "CopyMessagesRequest",
    "CopyMessagesResponse",
    "CopyTextButton",
    "CreateChatInviteLinkRequest",
    "CreateChatInviteLinkResponse",
    "CreateChatSubscriptionInviteLinkRequest",
    "CreateChatSubscriptionInviteLinkRequestChatId",
    "CreateChatSubscriptionInviteLinkResponse",
    "CreateForumTopicRequest",
    "CreateForumTopicResponse",
    "CreateInvoiceLinkRequest",
    "CreateInvoiceLinkResponse",
    "CreateNewStickerSetRequest",
    "CreateNewStickerSetResponse",
    "DeclineChatJoinRequestRequest",
    "DeclineChatJoinRequestResponse",
    "DeleteBusinessMessagesRequest",
    "DeleteBusinessMessagesResponse",
    "DeleteChatPhotoRequest",
    "DeleteChatPhotoResponse",
    "DeleteChatStickerSetRequest",
    "DeleteChatStickerSetResponse",
    "DeleteForumTopicRequest",
    "DeleteForumTopicResponse",
    "DeleteMessageRequest",
    "DeleteMessageResponse",
    "DeleteMessagesRequest",
    "DeleteMessagesResponse",
    "DeleteMyCommandsRequest",
    "DeleteMyCommandsResponse",
    "DeleteStickerFromSetRequest",
    "DeleteStickerFromSetResponse",
    "DeleteStickerSetRequest",
    "DeleteStickerSetResponse",
    "DeleteStoryRequest",
    "DeleteStoryResponse",
    "DeleteWebhookRequest",
    "DeleteWebhookResponse",
    "Dice",
    "Document",
    "EditChatInviteLinkRequest",
    "EditChatInviteLinkResponse",
    "EditChatSubscriptionInviteLinkRequest",
    "EditChatSubscriptionInviteLinkResponse",
    "EditForumTopicRequest",
    "EditForumTopicResponse",
    "EditGeneralForumTopicRequest",
    "EditGeneralForumTopicResponse",
    "EditMessageCaptionRequest",
    "EditMessageCaptionResponse",
    "EditMessageLiveLocationRequest",
    "EditMessageLiveLocationResponse",
    "EditMessageMediaRequest",
    "EditMessageMediaResponse",
    "EditMessageReplyMarkupRequest",
    "EditMessageReplyMarkupResponse",
    "EditMessageTextRequest",
    "EditMessageTextRequestChatId",
    "EditMessageTextResponse",
    "EditMessageTextResponseResult",
    "EditStoryRequest",
    "EditStoryResponse",
    "EditUserStarSubscriptionRequest",
    "EditUserStarSubscriptionResponse",
    "EncryptedCredentials",
    "EncryptedPassportElement",
    "Error",
    "ExportChatInviteLinkRequest",
    "ExportChatInviteLinkResponse",
    "ExternalReplyInfo",
    "File",
    "ForceReply",
    "ForumTopic",
    "ForumTopicCreated",
    "ForumTopicEdited",
    "ForwardMessageRequest",
    "ForwardMessageRequestFromChatId",
    "ForwardMessageResponse",
    "ForwardMessagesRequest",
    "ForwardMessagesRequestFromChatId",
    "ForwardMessagesResponse",
    "Game",
    "GameHighScore",
    "GetAvailableGiftsResponse",
    "GetBusinessAccountGiftsRequest",
    "GetBusinessAccountGiftsResponse",
    "GetBusinessAccountStarBalanceRequest",
    "GetBusinessAccountStarBalanceResponse",
    "GetBusinessConnectionRequest",
    "GetBusinessConnectionResponse",
    "GetChatAdministratorsRequest",
    "GetChatAdministratorsResponse",
    "GetChatMemberCountRequest",
    "GetChatMemberCountResponse",
    "GetChatMemberRequest",
    "GetChatMemberResponse",
    "GetChatMenuButtonRequest",
    "GetChatMenuButtonResponse",
    "GetChatRequest",
    "GetChatResponse",
    "GetCustomEmojiStickersRequest",
    "GetCustomEmojiStickersResponse",
    "GetFileRequest",
    "GetFileResponse",
    "GetForumTopicIconStickersResponse",
    "GetGameHighScoresRequest",
    "GetGameHighScoresResponse",
    "GetMeResponse",
    "GetMyCommandsRequest",
    "GetMyCommandsResponse",
    "GetMyDefaultAdministratorRightsRequest",
    "GetMyDefaultAdministratorRightsResponse",
    "GetMyDescriptionRequest",
    "GetMyDescriptionResponse",
    "GetMyNameRequest",
    "GetMyNameResponse",
    "GetMyShortDescriptionRequest",
    "GetMyShortDescriptionResponse",
    "GetStarTransactionsRequest",
    "GetStarTransactionsResponse",
    "GetStickerSetRequest",
    "GetStickerSetResponse",
    "GetUpdatesRequest",
    "GetUpdatesResponse",
    "GetUserChatBoostsRequest",
    "GetUserChatBoostsRequestChatId",
    "GetUserChatBoostsResponse",
    "GetUserProfilePhotosRequest",
    "GetUserProfilePhotosResponse",
    "GetWebhookInfoResponse",
    "Gift",
    "GiftInfo",
    "GiftPremiumSubscriptionRequest",
    "GiftPremiumSubscriptionResponse",
    "Gifts",
    "Giveaway",
    "GiveawayCompleted",
    "GiveawayCreated",
    "GiveawayWinners",
    "HideGeneralForumTopicRequest",
    "HideGeneralForumTopicResponse",
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
    "LeaveChatRequest",
    "LeaveChatRequestChatId",
    "LeaveChatResponse",
    "LinkPreviewOptions",
    "Location",
    "LocationAddress",
    "LogOutResponse",
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
    "PinChatMessageRequest",
    "PinChatMessageResponse",
    "Poll",
    "PollAnswer",
    "PollOption",
    "PostStoryRequest",
    "PostStoryResponse",
    "PreCheckoutQuery",
    "PreparedInlineMessage",
    "PromoteChatMemberRequest",
    "PromoteChatMemberResponse",
    "ProximityAlertTriggered",
    "ReactionCount",
    "ReactionType",
    "ReactionTypeCustomEmoji",
    "ReactionTypeEmoji",
    "ReactionTypePaid",
    "ReadBusinessMessageRequest",
    "ReadBusinessMessageResponse",
    "RefundStarPaymentRequest",
    "RefundStarPaymentResponse",
    "RefundedPayment",
    "RemoveBusinessAccountProfilePhotoRequest",
    "RemoveBusinessAccountProfilePhotoResponse",
    "RemoveChatVerificationRequest",
    "RemoveChatVerificationResponse",
    "RemoveUserVerificationRequest",
    "RemoveUserVerificationResponse",
    "ReopenForumTopicRequest",
    "ReopenForumTopicResponse",
    "ReopenGeneralForumTopicRequest",
    "ReopenGeneralForumTopicResponse",
    "ReplaceStickerInSetRequest",
    "ReplaceStickerInSetResponse",
    "ReplyKeyboardMarkup",
    "ReplyKeyboardRemove",
    "ReplyParameters",
    "ReplyParametersChatId",
    "ResponseParameters",
    "RestrictChatMemberRequest",
    "RestrictChatMemberResponse",
    "RevenueWithdrawalState",
    "RevenueWithdrawalStateFailed",
    "RevenueWithdrawalStatePending",
    "RevenueWithdrawalStateSucceeded",
    "RevokeChatInviteLinkRequest",
    "RevokeChatInviteLinkRequestChatId",
    "RevokeChatInviteLinkResponse",
    "SavePreparedInlineMessageRequest",
    "SavePreparedInlineMessageResponse",
    "SendAnimationRequest",
    "SendAnimationResponse",
    "SendAudioRequest",
    "SendAudioResponse",
    "SendChatActionRequest",
    "SendChatActionResponse",
    "SendContactRequest",
    "SendContactResponse",
    "SendDiceRequest",
    "SendDiceResponse",
    "SendDocumentRequest",
    "SendDocumentResponse",
    "SendGameRequest",
    "SendGameResponse",
    "SendGiftRequest",
    "SendGiftRequestChatId",
    "SendGiftResponse",
    "SendInvoiceRequest",
    "SendInvoiceResponse",
    "SendLocationRequest",
    "SendLocationResponse",
    "SendMediaGroupRequest",
    "SendMediaGroupRequestMediaInner",
    "SendMediaGroupResponse",
    "SendMessageRequest",
    "SendMessageRequestChatId",
    "SendMessageRequestReplyMarkup",
    "SendMessageResponse",
    "SendPaidMediaRequest",
    "SendPaidMediaRequestChatId",
    "SendPaidMediaResponse",
    "SendPhotoRequest",
    "SendPhotoResponse",
    "SendPollRequest",
    "SendPollResponse",
    "SendStickerRequest",
    "SendStickerResponse",
    "SendVenueRequest",
    "SendVenueResponse",
    "SendVideoNoteRequest",
    "SendVideoNoteResponse",
    "SendVideoRequest",
    "SendVideoResponse",
    "SendVoiceRequest",
    "SendVoiceResponse",
    "SentWebAppMessage",
    "SetBusinessAccountBioRequest",
    "SetBusinessAccountBioResponse",
    "SetBusinessAccountGiftSettingsRequest",
    "SetBusinessAccountGiftSettingsResponse",
    "SetBusinessAccountNameRequest",
    "SetBusinessAccountNameResponse",
    "SetBusinessAccountProfilePhotoRequest",
    "SetBusinessAccountProfilePhotoResponse",
    "SetBusinessAccountUsernameRequest",
    "SetBusinessAccountUsernameResponse",
    "SetChatAdministratorCustomTitleRequest",
    "SetChatAdministratorCustomTitleResponse",
    "SetChatDescriptionRequest",
    "SetChatDescriptionResponse",
    "SetChatMenuButtonRequest",
    "SetChatMenuButtonResponse",
    "SetChatPermissionsRequest",
    "SetChatPermissionsResponse",
    "SetChatPhotoRequest",
    "SetChatPhotoResponse",
    "SetChatStickerSetRequest",
    "SetChatStickerSetResponse",
    "SetChatTitleRequest",
    "SetChatTitleResponse",
    "SetCustomEmojiStickerSetThumbnailRequest",
    "SetCustomEmojiStickerSetThumbnailResponse",
    "SetGameScoreRequest",
    "SetGameScoreResponse",
    "SetMessageReactionRequest",
    "SetMessageReactionResponse",
    "SetMyCommandsRequest",
    "SetMyCommandsResponse",
    "SetMyDefaultAdministratorRightsRequest",
    "SetMyDefaultAdministratorRightsResponse",
    "SetMyDescriptionRequest",
    "SetMyDescriptionResponse",
    "SetMyNameRequest",
    "SetMyNameResponse",
    "SetMyShortDescriptionRequest",
    "SetMyShortDescriptionResponse",
    "SetPassportDataErrorsRequest",
    "SetPassportDataErrorsResponse",
    "SetStickerEmojiListRequest",
    "SetStickerEmojiListResponse",
    "SetStickerKeywordsRequest",
    "SetStickerKeywordsResponse",
    "SetStickerMaskPositionRequest",
    "SetStickerMaskPositionResponse",
    "SetStickerPositionInSetRequest",
    "SetStickerPositionInSetResponse",
    "SetStickerSetThumbnailRequest",
    "SetStickerSetThumbnailResponse",
    "SetStickerSetTitleRequest",
    "SetStickerSetTitleResponse",
    "SetUserEmojiStatusRequest",
    "SetUserEmojiStatusResponse",
    "SetWebhookRequest",
    "SetWebhookResponse",
    "SharedUser",
    "ShippingAddress",
    "ShippingOption",
    "ShippingQuery",
    "StarAmount",
    "StarTransaction",
    "StarTransactions",
    "Sticker",
    "StickerSet",
    "StopMessageLiveLocationRequest",
    "StopMessageLiveLocationResponse",
    "StopPollRequest",
    "StopPollResponse",
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
    "TransferBusinessAccountStarsRequest",
    "TransferBusinessAccountStarsResponse",
    "TransferGiftRequest",
    "TransferGiftResponse",
    "UnbanChatMemberRequest",
    "UnbanChatMemberResponse",
    "UnbanChatSenderChatRequest",
    "UnbanChatSenderChatResponse",
    "UnhideGeneralForumTopicRequest",
    "UnhideGeneralForumTopicResponse",
    "UniqueGift",
    "UniqueGiftBackdrop",
    "UniqueGiftBackdropColors",
    "UniqueGiftInfo",
    "UniqueGiftModel",
    "UniqueGiftSymbol",
    "UnpinAllChatMessagesRequest",
    "UnpinAllChatMessagesResponse",
    "UnpinAllForumTopicMessagesRequest",
    "UnpinAllForumTopicMessagesResponse",
    "UnpinAllGeneralForumTopicMessagesRequest",
    "UnpinAllGeneralForumTopicMessagesResponse",
    "UnpinChatMessageRequest",
    "UnpinChatMessageResponse",
    "Update",
    "UpgradeGiftRequest",
    "UpgradeGiftResponse",
    "UploadStickerFileRequest",
    "UploadStickerFileResponse",
    "User",
    "UserChatBoosts",
    "UserProfilePhotos",
    "UsersShared",
    "Venue",
    "VerifyChatRequest",
    "VerifyChatResponse",
    "VerifyUserRequest",
    "VerifyUserResponse",
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
from tele_rest.models.add_sticker_to_set_request import AddStickerToSetRequest as AddStickerToSetRequest
from tele_rest.models.add_sticker_to_set_response import AddStickerToSetResponse as AddStickerToSetResponse
from tele_rest.models.affiliate_info import AffiliateInfo as AffiliateInfo
from tele_rest.models.animation import Animation as Animation
from tele_rest.models.answer_callback_query_request import AnswerCallbackQueryRequest as AnswerCallbackQueryRequest
from tele_rest.models.answer_callback_query_response import AnswerCallbackQueryResponse as AnswerCallbackQueryResponse
from tele_rest.models.answer_inline_query_request import AnswerInlineQueryRequest as AnswerInlineQueryRequest
from tele_rest.models.answer_inline_query_response import AnswerInlineQueryResponse as AnswerInlineQueryResponse
from tele_rest.models.answer_pre_checkout_query_request import AnswerPreCheckoutQueryRequest as AnswerPreCheckoutQueryRequest
from tele_rest.models.answer_pre_checkout_query_response import AnswerPreCheckoutQueryResponse as AnswerPreCheckoutQueryResponse
from tele_rest.models.answer_shipping_query_request import AnswerShippingQueryRequest as AnswerShippingQueryRequest
from tele_rest.models.answer_shipping_query_response import AnswerShippingQueryResponse as AnswerShippingQueryResponse
from tele_rest.models.answer_web_app_query_request import AnswerWebAppQueryRequest as AnswerWebAppQueryRequest
from tele_rest.models.answer_web_app_query_response import AnswerWebAppQueryResponse as AnswerWebAppQueryResponse
from tele_rest.models.approve_chat_join_request_request import ApproveChatJoinRequestRequest as ApproveChatJoinRequestRequest
from tele_rest.models.approve_chat_join_request_response import ApproveChatJoinRequestResponse as ApproveChatJoinRequestResponse
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
from tele_rest.models.ban_chat_member_request import BanChatMemberRequest as BanChatMemberRequest
from tele_rest.models.ban_chat_member_request_chat_id import BanChatMemberRequestChatId as BanChatMemberRequestChatId
from tele_rest.models.ban_chat_member_response import BanChatMemberResponse as BanChatMemberResponse
from tele_rest.models.ban_chat_sender_chat_request import BanChatSenderChatRequest as BanChatSenderChatRequest
from tele_rest.models.ban_chat_sender_chat_response import BanChatSenderChatResponse as BanChatSenderChatResponse
from tele_rest.models.birthdate import Birthdate as Birthdate
from tele_rest.models.bot_command import BotCommand as BotCommand
from tele_rest.models.bot_command_scope import BotCommandScope as BotCommandScope
from tele_rest.models.bot_command_scope_all_chat_administrators import BotCommandScopeAllChatAdministrators as BotCommandScopeAllChatAdministrators
from tele_rest.models.bot_command_scope_all_group_chats import BotCommandScopeAllGroupChats as BotCommandScopeAllGroupChats
from tele_rest.models.bot_command_scope_all_private_chats import BotCommandScopeAllPrivateChats as BotCommandScopeAllPrivateChats
from tele_rest.models.bot_command_scope_chat import BotCommandScopeChat as BotCommandScopeChat
from tele_rest.models.bot_command_scope_chat_administrators import BotCommandScopeChatAdministrators as BotCommandScopeChatAdministrators
from tele_rest.models.bot_command_scope_chat_chat_id import BotCommandScopeChatChatId as BotCommandScopeChatChatId
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
from tele_rest.models.close_forum_topic_request import CloseForumTopicRequest as CloseForumTopicRequest
from tele_rest.models.close_forum_topic_response import CloseForumTopicResponse as CloseForumTopicResponse
from tele_rest.models.close_general_forum_topic_request import CloseGeneralForumTopicRequest as CloseGeneralForumTopicRequest
from tele_rest.models.close_general_forum_topic_response import CloseGeneralForumTopicResponse as CloseGeneralForumTopicResponse
from tele_rest.models.close_response import CloseResponse as CloseResponse
from tele_rest.models.contact import Contact as Contact
from tele_rest.models.convert_gift_to_stars_request import ConvertGiftToStarsRequest as ConvertGiftToStarsRequest
from tele_rest.models.convert_gift_to_stars_response import ConvertGiftToStarsResponse as ConvertGiftToStarsResponse
from tele_rest.models.copy_message_request import CopyMessageRequest as CopyMessageRequest
from tele_rest.models.copy_message_response import CopyMessageResponse as CopyMessageResponse
from tele_rest.models.copy_messages_request import CopyMessagesRequest as CopyMessagesRequest
from tele_rest.models.copy_messages_response import CopyMessagesResponse as CopyMessagesResponse
from tele_rest.models.copy_text_button import CopyTextButton as CopyTextButton
from tele_rest.models.create_chat_invite_link_request import CreateChatInviteLinkRequest as CreateChatInviteLinkRequest
from tele_rest.models.create_chat_invite_link_response import CreateChatInviteLinkResponse as CreateChatInviteLinkResponse
from tele_rest.models.create_chat_subscription_invite_link_request import CreateChatSubscriptionInviteLinkRequest as CreateChatSubscriptionInviteLinkRequest
from tele_rest.models.create_chat_subscription_invite_link_request_chat_id import CreateChatSubscriptionInviteLinkRequestChatId as CreateChatSubscriptionInviteLinkRequestChatId
from tele_rest.models.create_chat_subscription_invite_link_response import CreateChatSubscriptionInviteLinkResponse as CreateChatSubscriptionInviteLinkResponse
from tele_rest.models.create_forum_topic_request import CreateForumTopicRequest as CreateForumTopicRequest
from tele_rest.models.create_forum_topic_response import CreateForumTopicResponse as CreateForumTopicResponse
from tele_rest.models.create_invoice_link_request import CreateInvoiceLinkRequest as CreateInvoiceLinkRequest
from tele_rest.models.create_invoice_link_response import CreateInvoiceLinkResponse as CreateInvoiceLinkResponse
from tele_rest.models.create_new_sticker_set_request import CreateNewStickerSetRequest as CreateNewStickerSetRequest
from tele_rest.models.create_new_sticker_set_response import CreateNewStickerSetResponse as CreateNewStickerSetResponse
from tele_rest.models.decline_chat_join_request_request import DeclineChatJoinRequestRequest as DeclineChatJoinRequestRequest
from tele_rest.models.decline_chat_join_request_response import DeclineChatJoinRequestResponse as DeclineChatJoinRequestResponse
from tele_rest.models.delete_business_messages_request import DeleteBusinessMessagesRequest as DeleteBusinessMessagesRequest
from tele_rest.models.delete_business_messages_response import DeleteBusinessMessagesResponse as DeleteBusinessMessagesResponse
from tele_rest.models.delete_chat_photo_request import DeleteChatPhotoRequest as DeleteChatPhotoRequest
from tele_rest.models.delete_chat_photo_response import DeleteChatPhotoResponse as DeleteChatPhotoResponse
from tele_rest.models.delete_chat_sticker_set_request import DeleteChatStickerSetRequest as DeleteChatStickerSetRequest
from tele_rest.models.delete_chat_sticker_set_response import DeleteChatStickerSetResponse as DeleteChatStickerSetResponse
from tele_rest.models.delete_forum_topic_request import DeleteForumTopicRequest as DeleteForumTopicRequest
from tele_rest.models.delete_forum_topic_response import DeleteForumTopicResponse as DeleteForumTopicResponse
from tele_rest.models.delete_message_request import DeleteMessageRequest as DeleteMessageRequest
from tele_rest.models.delete_message_response import DeleteMessageResponse as DeleteMessageResponse
from tele_rest.models.delete_messages_request import DeleteMessagesRequest as DeleteMessagesRequest
from tele_rest.models.delete_messages_response import DeleteMessagesResponse as DeleteMessagesResponse
from tele_rest.models.delete_my_commands_request import DeleteMyCommandsRequest as DeleteMyCommandsRequest
from tele_rest.models.delete_my_commands_response import DeleteMyCommandsResponse as DeleteMyCommandsResponse
from tele_rest.models.delete_sticker_from_set_request import DeleteStickerFromSetRequest as DeleteStickerFromSetRequest
from tele_rest.models.delete_sticker_from_set_response import DeleteStickerFromSetResponse as DeleteStickerFromSetResponse
from tele_rest.models.delete_sticker_set_request import DeleteStickerSetRequest as DeleteStickerSetRequest
from tele_rest.models.delete_sticker_set_response import DeleteStickerSetResponse as DeleteStickerSetResponse
from tele_rest.models.delete_story_request import DeleteStoryRequest as DeleteStoryRequest
from tele_rest.models.delete_story_response import DeleteStoryResponse as DeleteStoryResponse
from tele_rest.models.delete_webhook_request import DeleteWebhookRequest as DeleteWebhookRequest
from tele_rest.models.delete_webhook_response import DeleteWebhookResponse as DeleteWebhookResponse
from tele_rest.models.dice import Dice as Dice
from tele_rest.models.document import Document as Document
from tele_rest.models.edit_chat_invite_link_request import EditChatInviteLinkRequest as EditChatInviteLinkRequest
from tele_rest.models.edit_chat_invite_link_response import EditChatInviteLinkResponse as EditChatInviteLinkResponse
from tele_rest.models.edit_chat_subscription_invite_link_request import EditChatSubscriptionInviteLinkRequest as EditChatSubscriptionInviteLinkRequest
from tele_rest.models.edit_chat_subscription_invite_link_response import EditChatSubscriptionInviteLinkResponse as EditChatSubscriptionInviteLinkResponse
from tele_rest.models.edit_forum_topic_request import EditForumTopicRequest as EditForumTopicRequest
from tele_rest.models.edit_forum_topic_response import EditForumTopicResponse as EditForumTopicResponse
from tele_rest.models.edit_general_forum_topic_request import EditGeneralForumTopicRequest as EditGeneralForumTopicRequest
from tele_rest.models.edit_general_forum_topic_response import EditGeneralForumTopicResponse as EditGeneralForumTopicResponse
from tele_rest.models.edit_message_caption_request import EditMessageCaptionRequest as EditMessageCaptionRequest
from tele_rest.models.edit_message_caption_response import EditMessageCaptionResponse as EditMessageCaptionResponse
from tele_rest.models.edit_message_live_location_request import EditMessageLiveLocationRequest as EditMessageLiveLocationRequest
from tele_rest.models.edit_message_live_location_response import EditMessageLiveLocationResponse as EditMessageLiveLocationResponse
from tele_rest.models.edit_message_media_request import EditMessageMediaRequest as EditMessageMediaRequest
from tele_rest.models.edit_message_media_response import EditMessageMediaResponse as EditMessageMediaResponse
from tele_rest.models.edit_message_reply_markup_request import EditMessageReplyMarkupRequest as EditMessageReplyMarkupRequest
from tele_rest.models.edit_message_reply_markup_response import EditMessageReplyMarkupResponse as EditMessageReplyMarkupResponse
from tele_rest.models.edit_message_text_request import EditMessageTextRequest as EditMessageTextRequest
from tele_rest.models.edit_message_text_request_chat_id import EditMessageTextRequestChatId as EditMessageTextRequestChatId
from tele_rest.models.edit_message_text_response import EditMessageTextResponse as EditMessageTextResponse
from tele_rest.models.edit_message_text_response_result import EditMessageTextResponseResult as EditMessageTextResponseResult
from tele_rest.models.edit_story_request import EditStoryRequest as EditStoryRequest
from tele_rest.models.edit_story_response import EditStoryResponse as EditStoryResponse
from tele_rest.models.edit_user_star_subscription_request import EditUserStarSubscriptionRequest as EditUserStarSubscriptionRequest
from tele_rest.models.edit_user_star_subscription_response import EditUserStarSubscriptionResponse as EditUserStarSubscriptionResponse
from tele_rest.models.encrypted_credentials import EncryptedCredentials as EncryptedCredentials
from tele_rest.models.encrypted_passport_element import EncryptedPassportElement as EncryptedPassportElement
from tele_rest.models.error import Error as Error
from tele_rest.models.export_chat_invite_link_request import ExportChatInviteLinkRequest as ExportChatInviteLinkRequest
from tele_rest.models.export_chat_invite_link_response import ExportChatInviteLinkResponse as ExportChatInviteLinkResponse
from tele_rest.models.external_reply_info import ExternalReplyInfo as ExternalReplyInfo
from tele_rest.models.file import File as File
from tele_rest.models.force_reply import ForceReply as ForceReply
from tele_rest.models.forum_topic import ForumTopic as ForumTopic
from tele_rest.models.forum_topic_created import ForumTopicCreated as ForumTopicCreated
from tele_rest.models.forum_topic_edited import ForumTopicEdited as ForumTopicEdited
from tele_rest.models.forward_message_request import ForwardMessageRequest as ForwardMessageRequest
from tele_rest.models.forward_message_request_from_chat_id import ForwardMessageRequestFromChatId as ForwardMessageRequestFromChatId
from tele_rest.models.forward_message_response import ForwardMessageResponse as ForwardMessageResponse
from tele_rest.models.forward_messages_request import ForwardMessagesRequest as ForwardMessagesRequest
from tele_rest.models.forward_messages_request_from_chat_id import ForwardMessagesRequestFromChatId as ForwardMessagesRequestFromChatId
from tele_rest.models.forward_messages_response import ForwardMessagesResponse as ForwardMessagesResponse
from tele_rest.models.game import Game as Game
from tele_rest.models.game_high_score import GameHighScore as GameHighScore
from tele_rest.models.get_available_gifts_response import GetAvailableGiftsResponse as GetAvailableGiftsResponse
from tele_rest.models.get_business_account_gifts_request import GetBusinessAccountGiftsRequest as GetBusinessAccountGiftsRequest
from tele_rest.models.get_business_account_gifts_response import GetBusinessAccountGiftsResponse as GetBusinessAccountGiftsResponse
from tele_rest.models.get_business_account_star_balance_request import GetBusinessAccountStarBalanceRequest as GetBusinessAccountStarBalanceRequest
from tele_rest.models.get_business_account_star_balance_response import GetBusinessAccountStarBalanceResponse as GetBusinessAccountStarBalanceResponse
from tele_rest.models.get_business_connection_request import GetBusinessConnectionRequest as GetBusinessConnectionRequest
from tele_rest.models.get_business_connection_response import GetBusinessConnectionResponse as GetBusinessConnectionResponse
from tele_rest.models.get_chat_administrators_request import GetChatAdministratorsRequest as GetChatAdministratorsRequest
from tele_rest.models.get_chat_administrators_response import GetChatAdministratorsResponse as GetChatAdministratorsResponse
from tele_rest.models.get_chat_member_count_request import GetChatMemberCountRequest as GetChatMemberCountRequest
from tele_rest.models.get_chat_member_count_response import GetChatMemberCountResponse as GetChatMemberCountResponse
from tele_rest.models.get_chat_member_request import GetChatMemberRequest as GetChatMemberRequest
from tele_rest.models.get_chat_member_response import GetChatMemberResponse as GetChatMemberResponse
from tele_rest.models.get_chat_menu_button_request import GetChatMenuButtonRequest as GetChatMenuButtonRequest
from tele_rest.models.get_chat_menu_button_response import GetChatMenuButtonResponse as GetChatMenuButtonResponse
from tele_rest.models.get_chat_request import GetChatRequest as GetChatRequest
from tele_rest.models.get_chat_response import GetChatResponse as GetChatResponse
from tele_rest.models.get_custom_emoji_stickers_request import GetCustomEmojiStickersRequest as GetCustomEmojiStickersRequest
from tele_rest.models.get_custom_emoji_stickers_response import GetCustomEmojiStickersResponse as GetCustomEmojiStickersResponse
from tele_rest.models.get_file_request import GetFileRequest as GetFileRequest
from tele_rest.models.get_file_response import GetFileResponse as GetFileResponse
from tele_rest.models.get_forum_topic_icon_stickers_response import GetForumTopicIconStickersResponse as GetForumTopicIconStickersResponse
from tele_rest.models.get_game_high_scores_request import GetGameHighScoresRequest as GetGameHighScoresRequest
from tele_rest.models.get_game_high_scores_response import GetGameHighScoresResponse as GetGameHighScoresResponse
from tele_rest.models.get_me_response import GetMeResponse as GetMeResponse
from tele_rest.models.get_my_commands_request import GetMyCommandsRequest as GetMyCommandsRequest
from tele_rest.models.get_my_commands_response import GetMyCommandsResponse as GetMyCommandsResponse
from tele_rest.models.get_my_default_administrator_rights_request import GetMyDefaultAdministratorRightsRequest as GetMyDefaultAdministratorRightsRequest
from tele_rest.models.get_my_default_administrator_rights_response import GetMyDefaultAdministratorRightsResponse as GetMyDefaultAdministratorRightsResponse
from tele_rest.models.get_my_description_request import GetMyDescriptionRequest as GetMyDescriptionRequest
from tele_rest.models.get_my_description_response import GetMyDescriptionResponse as GetMyDescriptionResponse
from tele_rest.models.get_my_name_request import GetMyNameRequest as GetMyNameRequest
from tele_rest.models.get_my_name_response import GetMyNameResponse as GetMyNameResponse
from tele_rest.models.get_my_short_description_request import GetMyShortDescriptionRequest as GetMyShortDescriptionRequest
from tele_rest.models.get_my_short_description_response import GetMyShortDescriptionResponse as GetMyShortDescriptionResponse
from tele_rest.models.get_star_transactions_request import GetStarTransactionsRequest as GetStarTransactionsRequest
from tele_rest.models.get_star_transactions_response import GetStarTransactionsResponse as GetStarTransactionsResponse
from tele_rest.models.get_sticker_set_request import GetStickerSetRequest as GetStickerSetRequest
from tele_rest.models.get_sticker_set_response import GetStickerSetResponse as GetStickerSetResponse
from tele_rest.models.get_updates_request import GetUpdatesRequest as GetUpdatesRequest
from tele_rest.models.get_updates_response import GetUpdatesResponse as GetUpdatesResponse
from tele_rest.models.get_user_chat_boosts_request import GetUserChatBoostsRequest as GetUserChatBoostsRequest
from tele_rest.models.get_user_chat_boosts_request_chat_id import GetUserChatBoostsRequestChatId as GetUserChatBoostsRequestChatId
from tele_rest.models.get_user_chat_boosts_response import GetUserChatBoostsResponse as GetUserChatBoostsResponse
from tele_rest.models.get_user_profile_photos_request import GetUserProfilePhotosRequest as GetUserProfilePhotosRequest
from tele_rest.models.get_user_profile_photos_response import GetUserProfilePhotosResponse as GetUserProfilePhotosResponse
from tele_rest.models.get_webhook_info_response import GetWebhookInfoResponse as GetWebhookInfoResponse
from tele_rest.models.gift import Gift as Gift
from tele_rest.models.gift_info import GiftInfo as GiftInfo
from tele_rest.models.gift_premium_subscription_request import GiftPremiumSubscriptionRequest as GiftPremiumSubscriptionRequest
from tele_rest.models.gift_premium_subscription_response import GiftPremiumSubscriptionResponse as GiftPremiumSubscriptionResponse
from tele_rest.models.gifts import Gifts as Gifts
from tele_rest.models.giveaway import Giveaway as Giveaway
from tele_rest.models.giveaway_completed import GiveawayCompleted as GiveawayCompleted
from tele_rest.models.giveaway_created import GiveawayCreated as GiveawayCreated
from tele_rest.models.giveaway_winners import GiveawayWinners as GiveawayWinners
from tele_rest.models.hide_general_forum_topic_request import HideGeneralForumTopicRequest as HideGeneralForumTopicRequest
from tele_rest.models.hide_general_forum_topic_response import HideGeneralForumTopicResponse as HideGeneralForumTopicResponse
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
from tele_rest.models.leave_chat_request import LeaveChatRequest as LeaveChatRequest
from tele_rest.models.leave_chat_request_chat_id import LeaveChatRequestChatId as LeaveChatRequestChatId
from tele_rest.models.leave_chat_response import LeaveChatResponse as LeaveChatResponse
from tele_rest.models.link_preview_options import LinkPreviewOptions as LinkPreviewOptions
from tele_rest.models.location import Location as Location
from tele_rest.models.location_address import LocationAddress as LocationAddress
from tele_rest.models.log_out_response import LogOutResponse as LogOutResponse
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
from tele_rest.models.pin_chat_message_request import PinChatMessageRequest as PinChatMessageRequest
from tele_rest.models.pin_chat_message_response import PinChatMessageResponse as PinChatMessageResponse
from tele_rest.models.poll import Poll as Poll
from tele_rest.models.poll_answer import PollAnswer as PollAnswer
from tele_rest.models.poll_option import PollOption as PollOption
from tele_rest.models.post_story_request import PostStoryRequest as PostStoryRequest
from tele_rest.models.post_story_response import PostStoryResponse as PostStoryResponse
from tele_rest.models.pre_checkout_query import PreCheckoutQuery as PreCheckoutQuery
from tele_rest.models.prepared_inline_message import PreparedInlineMessage as PreparedInlineMessage
from tele_rest.models.promote_chat_member_request import PromoteChatMemberRequest as PromoteChatMemberRequest
from tele_rest.models.promote_chat_member_response import PromoteChatMemberResponse as PromoteChatMemberResponse
from tele_rest.models.proximity_alert_triggered import ProximityAlertTriggered as ProximityAlertTriggered
from tele_rest.models.reaction_count import ReactionCount as ReactionCount
from tele_rest.models.reaction_type import ReactionType as ReactionType
from tele_rest.models.reaction_type_custom_emoji import ReactionTypeCustomEmoji as ReactionTypeCustomEmoji
from tele_rest.models.reaction_type_emoji import ReactionTypeEmoji as ReactionTypeEmoji
from tele_rest.models.reaction_type_paid import ReactionTypePaid as ReactionTypePaid
from tele_rest.models.read_business_message_request import ReadBusinessMessageRequest as ReadBusinessMessageRequest
from tele_rest.models.read_business_message_response import ReadBusinessMessageResponse as ReadBusinessMessageResponse
from tele_rest.models.refund_star_payment_request import RefundStarPaymentRequest as RefundStarPaymentRequest
from tele_rest.models.refund_star_payment_response import RefundStarPaymentResponse as RefundStarPaymentResponse
from tele_rest.models.refunded_payment import RefundedPayment as RefundedPayment
from tele_rest.models.remove_business_account_profile_photo_request import RemoveBusinessAccountProfilePhotoRequest as RemoveBusinessAccountProfilePhotoRequest
from tele_rest.models.remove_business_account_profile_photo_response import RemoveBusinessAccountProfilePhotoResponse as RemoveBusinessAccountProfilePhotoResponse
from tele_rest.models.remove_chat_verification_request import RemoveChatVerificationRequest as RemoveChatVerificationRequest
from tele_rest.models.remove_chat_verification_response import RemoveChatVerificationResponse as RemoveChatVerificationResponse
from tele_rest.models.remove_user_verification_request import RemoveUserVerificationRequest as RemoveUserVerificationRequest
from tele_rest.models.remove_user_verification_response import RemoveUserVerificationResponse as RemoveUserVerificationResponse
from tele_rest.models.reopen_forum_topic_request import ReopenForumTopicRequest as ReopenForumTopicRequest
from tele_rest.models.reopen_forum_topic_response import ReopenForumTopicResponse as ReopenForumTopicResponse
from tele_rest.models.reopen_general_forum_topic_request import ReopenGeneralForumTopicRequest as ReopenGeneralForumTopicRequest
from tele_rest.models.reopen_general_forum_topic_response import ReopenGeneralForumTopicResponse as ReopenGeneralForumTopicResponse
from tele_rest.models.replace_sticker_in_set_request import ReplaceStickerInSetRequest as ReplaceStickerInSetRequest
from tele_rest.models.replace_sticker_in_set_response import ReplaceStickerInSetResponse as ReplaceStickerInSetResponse
from tele_rest.models.reply_keyboard_markup import ReplyKeyboardMarkup as ReplyKeyboardMarkup
from tele_rest.models.reply_keyboard_remove import ReplyKeyboardRemove as ReplyKeyboardRemove
from tele_rest.models.reply_parameters import ReplyParameters as ReplyParameters
from tele_rest.models.reply_parameters_chat_id import ReplyParametersChatId as ReplyParametersChatId
from tele_rest.models.response_parameters import ResponseParameters as ResponseParameters
from tele_rest.models.restrict_chat_member_request import RestrictChatMemberRequest as RestrictChatMemberRequest
from tele_rest.models.restrict_chat_member_response import RestrictChatMemberResponse as RestrictChatMemberResponse
from tele_rest.models.revenue_withdrawal_state import RevenueWithdrawalState as RevenueWithdrawalState
from tele_rest.models.revenue_withdrawal_state_failed import RevenueWithdrawalStateFailed as RevenueWithdrawalStateFailed
from tele_rest.models.revenue_withdrawal_state_pending import RevenueWithdrawalStatePending as RevenueWithdrawalStatePending
from tele_rest.models.revenue_withdrawal_state_succeeded import RevenueWithdrawalStateSucceeded as RevenueWithdrawalStateSucceeded
from tele_rest.models.revoke_chat_invite_link_request import RevokeChatInviteLinkRequest as RevokeChatInviteLinkRequest
from tele_rest.models.revoke_chat_invite_link_request_chat_id import RevokeChatInviteLinkRequestChatId as RevokeChatInviteLinkRequestChatId
from tele_rest.models.revoke_chat_invite_link_response import RevokeChatInviteLinkResponse as RevokeChatInviteLinkResponse
from tele_rest.models.save_prepared_inline_message_request import SavePreparedInlineMessageRequest as SavePreparedInlineMessageRequest
from tele_rest.models.save_prepared_inline_message_response import SavePreparedInlineMessageResponse as SavePreparedInlineMessageResponse
from tele_rest.models.send_animation_request import SendAnimationRequest as SendAnimationRequest
from tele_rest.models.send_animation_response import SendAnimationResponse as SendAnimationResponse
from tele_rest.models.send_audio_request import SendAudioRequest as SendAudioRequest
from tele_rest.models.send_audio_response import SendAudioResponse as SendAudioResponse
from tele_rest.models.send_chat_action_request import SendChatActionRequest as SendChatActionRequest
from tele_rest.models.send_chat_action_response import SendChatActionResponse as SendChatActionResponse
from tele_rest.models.send_contact_request import SendContactRequest as SendContactRequest
from tele_rest.models.send_contact_response import SendContactResponse as SendContactResponse
from tele_rest.models.send_dice_request import SendDiceRequest as SendDiceRequest
from tele_rest.models.send_dice_response import SendDiceResponse as SendDiceResponse
from tele_rest.models.send_document_request import SendDocumentRequest as SendDocumentRequest
from tele_rest.models.send_document_response import SendDocumentResponse as SendDocumentResponse
from tele_rest.models.send_game_request import SendGameRequest as SendGameRequest
from tele_rest.models.send_game_response import SendGameResponse as SendGameResponse
from tele_rest.models.send_gift_request import SendGiftRequest as SendGiftRequest
from tele_rest.models.send_gift_request_chat_id import SendGiftRequestChatId as SendGiftRequestChatId
from tele_rest.models.send_gift_response import SendGiftResponse as SendGiftResponse
from tele_rest.models.send_invoice_request import SendInvoiceRequest as SendInvoiceRequest
from tele_rest.models.send_invoice_response import SendInvoiceResponse as SendInvoiceResponse
from tele_rest.models.send_location_request import SendLocationRequest as SendLocationRequest
from tele_rest.models.send_location_response import SendLocationResponse as SendLocationResponse
from tele_rest.models.send_media_group_request import SendMediaGroupRequest as SendMediaGroupRequest
from tele_rest.models.send_media_group_request_media_inner import SendMediaGroupRequestMediaInner as SendMediaGroupRequestMediaInner
from tele_rest.models.send_media_group_response import SendMediaGroupResponse as SendMediaGroupResponse
from tele_rest.models.send_message_request import SendMessageRequest as SendMessageRequest
from tele_rest.models.send_message_request_chat_id import SendMessageRequestChatId as SendMessageRequestChatId
from tele_rest.models.send_message_request_reply_markup import SendMessageRequestReplyMarkup as SendMessageRequestReplyMarkup
from tele_rest.models.send_message_response import SendMessageResponse as SendMessageResponse
from tele_rest.models.send_paid_media_request import SendPaidMediaRequest as SendPaidMediaRequest
from tele_rest.models.send_paid_media_request_chat_id import SendPaidMediaRequestChatId as SendPaidMediaRequestChatId
from tele_rest.models.send_paid_media_response import SendPaidMediaResponse as SendPaidMediaResponse
from tele_rest.models.send_photo_request import SendPhotoRequest as SendPhotoRequest
from tele_rest.models.send_photo_response import SendPhotoResponse as SendPhotoResponse
from tele_rest.models.send_poll_request import SendPollRequest as SendPollRequest
from tele_rest.models.send_poll_response import SendPollResponse as SendPollResponse
from tele_rest.models.send_sticker_request import SendStickerRequest as SendStickerRequest
from tele_rest.models.send_sticker_response import SendStickerResponse as SendStickerResponse
from tele_rest.models.send_venue_request import SendVenueRequest as SendVenueRequest
from tele_rest.models.send_venue_response import SendVenueResponse as SendVenueResponse
from tele_rest.models.send_video_note_request import SendVideoNoteRequest as SendVideoNoteRequest
from tele_rest.models.send_video_note_response import SendVideoNoteResponse as SendVideoNoteResponse
from tele_rest.models.send_video_request import SendVideoRequest as SendVideoRequest
from tele_rest.models.send_video_response import SendVideoResponse as SendVideoResponse
from tele_rest.models.send_voice_request import SendVoiceRequest as SendVoiceRequest
from tele_rest.models.send_voice_response import SendVoiceResponse as SendVoiceResponse
from tele_rest.models.sent_web_app_message import SentWebAppMessage as SentWebAppMessage
from tele_rest.models.set_business_account_bio_request import SetBusinessAccountBioRequest as SetBusinessAccountBioRequest
from tele_rest.models.set_business_account_bio_response import SetBusinessAccountBioResponse as SetBusinessAccountBioResponse
from tele_rest.models.set_business_account_gift_settings_request import SetBusinessAccountGiftSettingsRequest as SetBusinessAccountGiftSettingsRequest
from tele_rest.models.set_business_account_gift_settings_response import SetBusinessAccountGiftSettingsResponse as SetBusinessAccountGiftSettingsResponse
from tele_rest.models.set_business_account_name_request import SetBusinessAccountNameRequest as SetBusinessAccountNameRequest
from tele_rest.models.set_business_account_name_response import SetBusinessAccountNameResponse as SetBusinessAccountNameResponse
from tele_rest.models.set_business_account_profile_photo_request import SetBusinessAccountProfilePhotoRequest as SetBusinessAccountProfilePhotoRequest
from tele_rest.models.set_business_account_profile_photo_response import SetBusinessAccountProfilePhotoResponse as SetBusinessAccountProfilePhotoResponse
from tele_rest.models.set_business_account_username_request import SetBusinessAccountUsernameRequest as SetBusinessAccountUsernameRequest
from tele_rest.models.set_business_account_username_response import SetBusinessAccountUsernameResponse as SetBusinessAccountUsernameResponse
from tele_rest.models.set_chat_administrator_custom_title_request import SetChatAdministratorCustomTitleRequest as SetChatAdministratorCustomTitleRequest
from tele_rest.models.set_chat_administrator_custom_title_response import SetChatAdministratorCustomTitleResponse as SetChatAdministratorCustomTitleResponse
from tele_rest.models.set_chat_description_request import SetChatDescriptionRequest as SetChatDescriptionRequest
from tele_rest.models.set_chat_description_response import SetChatDescriptionResponse as SetChatDescriptionResponse
from tele_rest.models.set_chat_menu_button_request import SetChatMenuButtonRequest as SetChatMenuButtonRequest
from tele_rest.models.set_chat_menu_button_response import SetChatMenuButtonResponse as SetChatMenuButtonResponse
from tele_rest.models.set_chat_permissions_request import SetChatPermissionsRequest as SetChatPermissionsRequest
from tele_rest.models.set_chat_permissions_response import SetChatPermissionsResponse as SetChatPermissionsResponse
from tele_rest.models.set_chat_photo_request import SetChatPhotoRequest as SetChatPhotoRequest
from tele_rest.models.set_chat_photo_response import SetChatPhotoResponse as SetChatPhotoResponse
from tele_rest.models.set_chat_sticker_set_request import SetChatStickerSetRequest as SetChatStickerSetRequest
from tele_rest.models.set_chat_sticker_set_response import SetChatStickerSetResponse as SetChatStickerSetResponse
from tele_rest.models.set_chat_title_request import SetChatTitleRequest as SetChatTitleRequest
from tele_rest.models.set_chat_title_response import SetChatTitleResponse as SetChatTitleResponse
from tele_rest.models.set_custom_emoji_sticker_set_thumbnail_request import SetCustomEmojiStickerSetThumbnailRequest as SetCustomEmojiStickerSetThumbnailRequest
from tele_rest.models.set_custom_emoji_sticker_set_thumbnail_response import SetCustomEmojiStickerSetThumbnailResponse as SetCustomEmojiStickerSetThumbnailResponse
from tele_rest.models.set_game_score_request import SetGameScoreRequest as SetGameScoreRequest
from tele_rest.models.set_game_score_response import SetGameScoreResponse as SetGameScoreResponse
from tele_rest.models.set_message_reaction_request import SetMessageReactionRequest as SetMessageReactionRequest
from tele_rest.models.set_message_reaction_response import SetMessageReactionResponse as SetMessageReactionResponse
from tele_rest.models.set_my_commands_request import SetMyCommandsRequest as SetMyCommandsRequest
from tele_rest.models.set_my_commands_response import SetMyCommandsResponse as SetMyCommandsResponse
from tele_rest.models.set_my_default_administrator_rights_request import SetMyDefaultAdministratorRightsRequest as SetMyDefaultAdministratorRightsRequest
from tele_rest.models.set_my_default_administrator_rights_response import SetMyDefaultAdministratorRightsResponse as SetMyDefaultAdministratorRightsResponse
from tele_rest.models.set_my_description_request import SetMyDescriptionRequest as SetMyDescriptionRequest
from tele_rest.models.set_my_description_response import SetMyDescriptionResponse as SetMyDescriptionResponse
from tele_rest.models.set_my_name_request import SetMyNameRequest as SetMyNameRequest
from tele_rest.models.set_my_name_response import SetMyNameResponse as SetMyNameResponse
from tele_rest.models.set_my_short_description_request import SetMyShortDescriptionRequest as SetMyShortDescriptionRequest
from tele_rest.models.set_my_short_description_response import SetMyShortDescriptionResponse as SetMyShortDescriptionResponse
from tele_rest.models.set_passport_data_errors_request import SetPassportDataErrorsRequest as SetPassportDataErrorsRequest
from tele_rest.models.set_passport_data_errors_response import SetPassportDataErrorsResponse as SetPassportDataErrorsResponse
from tele_rest.models.set_sticker_emoji_list_request import SetStickerEmojiListRequest as SetStickerEmojiListRequest
from tele_rest.models.set_sticker_emoji_list_response import SetStickerEmojiListResponse as SetStickerEmojiListResponse
from tele_rest.models.set_sticker_keywords_request import SetStickerKeywordsRequest as SetStickerKeywordsRequest
from tele_rest.models.set_sticker_keywords_response import SetStickerKeywordsResponse as SetStickerKeywordsResponse
from tele_rest.models.set_sticker_mask_position_request import SetStickerMaskPositionRequest as SetStickerMaskPositionRequest
from tele_rest.models.set_sticker_mask_position_response import SetStickerMaskPositionResponse as SetStickerMaskPositionResponse
from tele_rest.models.set_sticker_position_in_set_request import SetStickerPositionInSetRequest as SetStickerPositionInSetRequest
from tele_rest.models.set_sticker_position_in_set_response import SetStickerPositionInSetResponse as SetStickerPositionInSetResponse
from tele_rest.models.set_sticker_set_thumbnail_request import SetStickerSetThumbnailRequest as SetStickerSetThumbnailRequest
from tele_rest.models.set_sticker_set_thumbnail_response import SetStickerSetThumbnailResponse as SetStickerSetThumbnailResponse
from tele_rest.models.set_sticker_set_title_request import SetStickerSetTitleRequest as SetStickerSetTitleRequest
from tele_rest.models.set_sticker_set_title_response import SetStickerSetTitleResponse as SetStickerSetTitleResponse
from tele_rest.models.set_user_emoji_status_request import SetUserEmojiStatusRequest as SetUserEmojiStatusRequest
from tele_rest.models.set_user_emoji_status_response import SetUserEmojiStatusResponse as SetUserEmojiStatusResponse
from tele_rest.models.set_webhook_request import SetWebhookRequest as SetWebhookRequest
from tele_rest.models.set_webhook_response import SetWebhookResponse as SetWebhookResponse
from tele_rest.models.shared_user import SharedUser as SharedUser
from tele_rest.models.shipping_address import ShippingAddress as ShippingAddress
from tele_rest.models.shipping_option import ShippingOption as ShippingOption
from tele_rest.models.shipping_query import ShippingQuery as ShippingQuery
from tele_rest.models.star_amount import StarAmount as StarAmount
from tele_rest.models.star_transaction import StarTransaction as StarTransaction
from tele_rest.models.star_transactions import StarTransactions as StarTransactions
from tele_rest.models.sticker import Sticker as Sticker
from tele_rest.models.sticker_set import StickerSet as StickerSet
from tele_rest.models.stop_message_live_location_request import StopMessageLiveLocationRequest as StopMessageLiveLocationRequest
from tele_rest.models.stop_message_live_location_response import StopMessageLiveLocationResponse as StopMessageLiveLocationResponse
from tele_rest.models.stop_poll_request import StopPollRequest as StopPollRequest
from tele_rest.models.stop_poll_response import StopPollResponse as StopPollResponse
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
from tele_rest.models.transfer_business_account_stars_request import TransferBusinessAccountStarsRequest as TransferBusinessAccountStarsRequest
from tele_rest.models.transfer_business_account_stars_response import TransferBusinessAccountStarsResponse as TransferBusinessAccountStarsResponse
from tele_rest.models.transfer_gift_request import TransferGiftRequest as TransferGiftRequest
from tele_rest.models.transfer_gift_response import TransferGiftResponse as TransferGiftResponse
from tele_rest.models.unban_chat_member_request import UnbanChatMemberRequest as UnbanChatMemberRequest
from tele_rest.models.unban_chat_member_response import UnbanChatMemberResponse as UnbanChatMemberResponse
from tele_rest.models.unban_chat_sender_chat_request import UnbanChatSenderChatRequest as UnbanChatSenderChatRequest
from tele_rest.models.unban_chat_sender_chat_response import UnbanChatSenderChatResponse as UnbanChatSenderChatResponse
from tele_rest.models.unhide_general_forum_topic_request import UnhideGeneralForumTopicRequest as UnhideGeneralForumTopicRequest
from tele_rest.models.unhide_general_forum_topic_response import UnhideGeneralForumTopicResponse as UnhideGeneralForumTopicResponse
from tele_rest.models.unique_gift import UniqueGift as UniqueGift
from tele_rest.models.unique_gift_backdrop import UniqueGiftBackdrop as UniqueGiftBackdrop
from tele_rest.models.unique_gift_backdrop_colors import UniqueGiftBackdropColors as UniqueGiftBackdropColors
from tele_rest.models.unique_gift_info import UniqueGiftInfo as UniqueGiftInfo
from tele_rest.models.unique_gift_model import UniqueGiftModel as UniqueGiftModel
from tele_rest.models.unique_gift_symbol import UniqueGiftSymbol as UniqueGiftSymbol
from tele_rest.models.unpin_all_chat_messages_request import UnpinAllChatMessagesRequest as UnpinAllChatMessagesRequest
from tele_rest.models.unpin_all_chat_messages_response import UnpinAllChatMessagesResponse as UnpinAllChatMessagesResponse
from tele_rest.models.unpin_all_forum_topic_messages_request import UnpinAllForumTopicMessagesRequest as UnpinAllForumTopicMessagesRequest
from tele_rest.models.unpin_all_forum_topic_messages_response import UnpinAllForumTopicMessagesResponse as UnpinAllForumTopicMessagesResponse
from tele_rest.models.unpin_all_general_forum_topic_messages_request import UnpinAllGeneralForumTopicMessagesRequest as UnpinAllGeneralForumTopicMessagesRequest
from tele_rest.models.unpin_all_general_forum_topic_messages_response import UnpinAllGeneralForumTopicMessagesResponse as UnpinAllGeneralForumTopicMessagesResponse
from tele_rest.models.unpin_chat_message_request import UnpinChatMessageRequest as UnpinChatMessageRequest
from tele_rest.models.unpin_chat_message_response import UnpinChatMessageResponse as UnpinChatMessageResponse
from tele_rest.models.update import Update as Update
from tele_rest.models.upgrade_gift_request import UpgradeGiftRequest as UpgradeGiftRequest
from tele_rest.models.upgrade_gift_response import UpgradeGiftResponse as UpgradeGiftResponse
from tele_rest.models.upload_sticker_file_request import UploadStickerFileRequest as UploadStickerFileRequest
from tele_rest.models.upload_sticker_file_response import UploadStickerFileResponse as UploadStickerFileResponse
from tele_rest.models.user import User as User
from tele_rest.models.user_chat_boosts import UserChatBoosts as UserChatBoosts
from tele_rest.models.user_profile_photos import UserProfilePhotos as UserProfilePhotos
from tele_rest.models.users_shared import UsersShared as UsersShared
from tele_rest.models.venue import Venue as Venue
from tele_rest.models.verify_chat_request import VerifyChatRequest as VerifyChatRequest
from tele_rest.models.verify_chat_response import VerifyChatResponse as VerifyChatResponse
from tele_rest.models.verify_user_request import VerifyUserRequest as VerifyUserRequest
from tele_rest.models.verify_user_response import VerifyUserResponse as VerifyUserResponse
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
