# coding: utf-8

# flake8: noqa

"""
Telegram Bot API - REST API Client
The Bot API is an HTTP-based interface created for developers keen on building bots for Telegram. To learn how to create and set up a bot, please consult our Introduction to Bots and Bot FAQ.

## Metadata

- **Copyright**: Copyright (c) 2025 Qntx
- **Author**: ΣX <gitctrlx@gmail.com>
- **Version**: 9.0.0
- **Modified**: 2025-07-01T14:36:24.755929598Z[Etc/UTC]
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
    "AnswerCallbackQueryPostRequest",
    "AnswerInlineQueryPostRequest",
    "AnswerPreCheckoutQueryPostRequest",
    "AnswerShippingQueryPostRequest",
    "AnswerWebAppQueryPost200Response",
    "AnswerWebAppQueryPostRequest",
    "ApproveChatJoinRequestPostRequest",
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
    "BanChatMemberPostRequest",
    "BanChatMemberPostRequestChatId",
    "BanChatSenderChatPostRequest",
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
    "CloseForumTopicPostRequest",
    "Contact",
    "ConvertGiftToStarsPostRequest",
    "CopyMessagePost200Response",
    "CopyMessagePostRequest",
    "CopyMessagesPostRequest",
    "CopyTextButton",
    "CreateChatInviteLinkPost200Response",
    "CreateChatInviteLinkPostRequest",
    "CreateChatSubscriptionInviteLinkPostRequest",
    "CreateChatSubscriptionInviteLinkPostRequestChatId",
    "CreateForumTopicPost200Response",
    "CreateForumTopicPostRequest",
    "CreateInvoiceLinkPostRequest",
    "DeleteBusinessMessagesPostRequest",
    "DeleteChatStickerSetPostRequest",
    "DeleteMessagePostRequest",
    "DeleteMessagesPostRequest",
    "DeleteMyCommandsPostRequest",
    "DeleteStickerFromSetPostRequest",
    "DeleteStickerSetPostRequest",
    "DeleteStoryPostRequest",
    "DeleteWebhookPostRequest",
    "Dice",
    "Document",
    "EditChatInviteLinkPostRequest",
    "EditChatSubscriptionInviteLinkPostRequest",
    "EditForumTopicPostRequest",
    "EditGeneralForumTopicPostRequest",
    "EditMessageCaptionPostRequest",
    "EditMessageLiveLocationPostRequest",
    "EditMessageReplyMarkupPostRequest",
    "EditMessageTextPost200Response",
    "EditMessageTextPost200ResponseResult",
    "EditMessageTextPostRequest",
    "EditMessageTextPostRequestChatId",
    "EditUserStarSubscriptionPostRequest",
    "EncryptedCredentials",
    "EncryptedPassportElement",
    "Error",
    "ExportChatInviteLinkPost200Response",
    "ExportChatInviteLinkPostRequest",
    "ExternalReplyInfo",
    "File",
    "ForceReply",
    "ForumTopic",
    "ForumTopicCreated",
    "ForumTopicEdited",
    "ForwardMessagePostRequest",
    "ForwardMessagePostRequestFromChatId",
    "ForwardMessagesPost200Response",
    "ForwardMessagesPostRequest",
    "ForwardMessagesPostRequestFromChatId",
    "Game",
    "GameHighScore",
    "GetAvailableGiftsPost200Response",
    "GetBusinessAccountGiftsPost200Response",
    "GetBusinessAccountGiftsPostRequest",
    "GetBusinessAccountStarBalancePost200Response",
    "GetBusinessConnectionPost200Response",
    "GetBusinessConnectionPostRequest",
    "GetChatAdministratorsPost200Response",
    "GetChatMemberCountPost200Response",
    "GetChatMemberPost200Response",
    "GetChatMemberPostRequest",
    "GetChatMenuButtonPost200Response",
    "GetChatMenuButtonPostRequest",
    "GetChatPost200Response",
    "GetCustomEmojiStickersPostRequest",
    "GetFilePost200Response",
    "GetFilePostRequest",
    "GetForumTopicIconStickersPost200Response",
    "GetGameHighScoresPost200Response",
    "GetGameHighScoresPostRequest",
    "GetMePost200Response",
    "GetMyCommandsPost200Response",
    "GetMyCommandsPostRequest",
    "GetMyDefaultAdministratorRightsPost200Response",
    "GetMyDefaultAdministratorRightsPostRequest",
    "GetMyDescriptionPost200Response",
    "GetMyNamePost200Response",
    "GetMyNamePostRequest",
    "GetMyShortDescriptionPost200Response",
    "GetStarTransactionsPost200Response",
    "GetStarTransactionsPostRequest",
    "GetStickerSetPost200Response",
    "GetStickerSetPostRequest",
    "GetUpdatesPost200Response",
    "GetUpdatesPostRequest",
    "GetUserChatBoostsPost200Response",
    "GetUserChatBoostsPostRequest",
    "GetUserChatBoostsPostRequestChatId",
    "GetUserProfilePhotosPost200Response",
    "GetUserProfilePhotosPostRequest",
    "GetWebhookInfoPost200Response",
    "Gift",
    "GiftInfo",
    "GiftPremiumSubscriptionPostRequest",
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
    "LeaveChatPostRequest",
    "LeaveChatPostRequestChatId",
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
    "PinChatMessagePostRequest",
    "Poll",
    "PollAnswer",
    "PollOption",
    "PostStoryPost200Response",
    "PreCheckoutQuery",
    "PreparedInlineMessage",
    "PromoteChatMemberPostRequest",
    "ProximityAlertTriggered",
    "ReactionCount",
    "ReactionType",
    "ReactionTypeCustomEmoji",
    "ReactionTypeEmoji",
    "ReactionTypePaid",
    "ReadBusinessMessagePostRequest",
    "RefundStarPaymentPostRequest",
    "RefundedPayment",
    "RemoveBusinessAccountProfilePhotoPostRequest",
    "RemoveUserVerificationPostRequest",
    "ReplyKeyboardMarkup",
    "ReplyKeyboardRemove",
    "ReplyParameters",
    "ReplyParametersChatId",
    "ResponseParameters",
    "RestrictChatMemberPostRequest",
    "RestrictChatMemberPostRequestChatId",
    "RevenueWithdrawalState",
    "RevenueWithdrawalStateFailed",
    "RevenueWithdrawalStatePending",
    "RevenueWithdrawalStateSucceeded",
    "RevokeChatInviteLinkPostRequest",
    "RevokeChatInviteLinkPostRequestChatId",
    "SavePreparedInlineMessagePost200Response",
    "SavePreparedInlineMessagePostRequest",
    "SendAnimationPostRequestAnimation",
    "SendAudioPostRequestAudio",
    "SendAudioPostRequestThumbnail",
    "SendChatActionPostRequest",
    "SendContactPostRequest",
    "SendDicePostRequest",
    "SendDocumentPostRequestDocument",
    "SendGamePostRequest",
    "SendGiftPostRequest",
    "SendGiftPostRequestChatId",
    "SendInvoicePostRequest",
    "SendLocationPostRequest",
    "SendMediaGroupPost200Response",
    "SendMediaGroupPostRequestMediaInner",
    "SendMessagePost200Response",
    "SendMessagePostRequest",
    "SendMessagePostRequestChatId",
    "SendMessagePostRequestReplyMarkup",
    "SendPaidMediaPostRequestChatId",
    "SendPhotoPostRequestPhoto",
    "SendPollPostRequest",
    "SendStickerPostRequestSticker",
    "SendVenuePostRequest",
    "SendVideoNotePostRequestVideoNote",
    "SendVideoPostRequestCover",
    "SendVideoPostRequestVideo",
    "SendVoicePostRequestVoice",
    "SentWebAppMessage",
    "SetBusinessAccountBioPostRequest",
    "SetBusinessAccountGiftSettingsPostRequest",
    "SetBusinessAccountNamePostRequest",
    "SetBusinessAccountUsernamePostRequest",
    "SetChatAdministratorCustomTitlePostRequest",
    "SetChatDescriptionPostRequest",
    "SetChatMenuButtonPostRequest",
    "SetChatPermissionsPostRequest",
    "SetChatStickerSetPostRequest",
    "SetChatTitlePostRequest",
    "SetCustomEmojiStickerSetThumbnailPostRequest",
    "SetGameScorePostRequest",
    "SetMessageReactionPostRequest",
    "SetMyCommandsPostRequest",
    "SetMyDefaultAdministratorRightsPostRequest",
    "SetMyDescriptionPostRequest",
    "SetMyNamePostRequest",
    "SetMyShortDescriptionPostRequest",
    "SetPassportDataErrorsPostRequest",
    "SetStickerEmojiListPostRequest",
    "SetStickerKeywordsPostRequest",
    "SetStickerMaskPositionPostRequest",
    "SetStickerPositionInSetPostRequest",
    "SetStickerSetThumbnailPostRequestThumbnail",
    "SetStickerSetTitlePostRequest",
    "SetUserEmojiStatusPostRequest",
    "SetWebhookPost200Response",
    "SharedUser",
    "ShippingAddress",
    "ShippingOption",
    "ShippingQuery",
    "StarAmount",
    "StarTransaction",
    "StarTransactions",
    "Sticker",
    "StickerSet",
    "StopMessageLiveLocationPostRequest",
    "StopPollPost200Response",
    "StopPollPostRequest",
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
    "TransferBusinessAccountStarsPostRequest",
    "TransferGiftPostRequest",
    "UnbanChatMemberPostRequest",
    "UniqueGift",
    "UniqueGiftBackdrop",
    "UniqueGiftBackdropColors",
    "UniqueGiftInfo",
    "UniqueGiftModel",
    "UniqueGiftSymbol",
    "UnpinChatMessagePostRequest",
    "Update",
    "UpgradeGiftPostRequest",
    "User",
    "UserChatBoosts",
    "UserProfilePhotos",
    "UsersShared",
    "Venue",
    "VerifyChatPostRequest",
    "VerifyUserPostRequest",
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
from tele_rest.models.answer_callback_query_post_request import AnswerCallbackQueryPostRequest as AnswerCallbackQueryPostRequest
from tele_rest.models.answer_inline_query_post_request import AnswerInlineQueryPostRequest as AnswerInlineQueryPostRequest
from tele_rest.models.answer_pre_checkout_query_post_request import AnswerPreCheckoutQueryPostRequest as AnswerPreCheckoutQueryPostRequest
from tele_rest.models.answer_shipping_query_post_request import AnswerShippingQueryPostRequest as AnswerShippingQueryPostRequest
from tele_rest.models.answer_web_app_query_post200_response import AnswerWebAppQueryPost200Response as AnswerWebAppQueryPost200Response
from tele_rest.models.answer_web_app_query_post_request import AnswerWebAppQueryPostRequest as AnswerWebAppQueryPostRequest
from tele_rest.models.approve_chat_join_request_post_request import ApproveChatJoinRequestPostRequest as ApproveChatJoinRequestPostRequest
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
from tele_rest.models.ban_chat_member_post_request import BanChatMemberPostRequest as BanChatMemberPostRequest
from tele_rest.models.ban_chat_member_post_request_chat_id import BanChatMemberPostRequestChatId as BanChatMemberPostRequestChatId
from tele_rest.models.ban_chat_sender_chat_post_request import BanChatSenderChatPostRequest as BanChatSenderChatPostRequest
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
from tele_rest.models.close_forum_topic_post_request import CloseForumTopicPostRequest as CloseForumTopicPostRequest
from tele_rest.models.contact import Contact as Contact
from tele_rest.models.convert_gift_to_stars_post_request import ConvertGiftToStarsPostRequest as ConvertGiftToStarsPostRequest
from tele_rest.models.copy_message_post200_response import CopyMessagePost200Response as CopyMessagePost200Response
from tele_rest.models.copy_message_post_request import CopyMessagePostRequest as CopyMessagePostRequest
from tele_rest.models.copy_messages_post_request import CopyMessagesPostRequest as CopyMessagesPostRequest
from tele_rest.models.copy_text_button import CopyTextButton as CopyTextButton
from tele_rest.models.create_chat_invite_link_post200_response import CreateChatInviteLinkPost200Response as CreateChatInviteLinkPost200Response
from tele_rest.models.create_chat_invite_link_post_request import CreateChatInviteLinkPostRequest as CreateChatInviteLinkPostRequest
from tele_rest.models.create_chat_subscription_invite_link_post_request import CreateChatSubscriptionInviteLinkPostRequest as CreateChatSubscriptionInviteLinkPostRequest
from tele_rest.models.create_chat_subscription_invite_link_post_request_chat_id import CreateChatSubscriptionInviteLinkPostRequestChatId as CreateChatSubscriptionInviteLinkPostRequestChatId
from tele_rest.models.create_forum_topic_post200_response import CreateForumTopicPost200Response as CreateForumTopicPost200Response
from tele_rest.models.create_forum_topic_post_request import CreateForumTopicPostRequest as CreateForumTopicPostRequest
from tele_rest.models.create_invoice_link_post_request import CreateInvoiceLinkPostRequest as CreateInvoiceLinkPostRequest
from tele_rest.models.delete_business_messages_post_request import DeleteBusinessMessagesPostRequest as DeleteBusinessMessagesPostRequest
from tele_rest.models.delete_chat_sticker_set_post_request import DeleteChatStickerSetPostRequest as DeleteChatStickerSetPostRequest
from tele_rest.models.delete_message_post_request import DeleteMessagePostRequest as DeleteMessagePostRequest
from tele_rest.models.delete_messages_post_request import DeleteMessagesPostRequest as DeleteMessagesPostRequest
from tele_rest.models.delete_my_commands_post_request import DeleteMyCommandsPostRequest as DeleteMyCommandsPostRequest
from tele_rest.models.delete_sticker_from_set_post_request import DeleteStickerFromSetPostRequest as DeleteStickerFromSetPostRequest
from tele_rest.models.delete_sticker_set_post_request import DeleteStickerSetPostRequest as DeleteStickerSetPostRequest
from tele_rest.models.delete_story_post_request import DeleteStoryPostRequest as DeleteStoryPostRequest
from tele_rest.models.delete_webhook_post_request import DeleteWebhookPostRequest as DeleteWebhookPostRequest
from tele_rest.models.dice import Dice as Dice
from tele_rest.models.document import Document as Document
from tele_rest.models.edit_chat_invite_link_post_request import EditChatInviteLinkPostRequest as EditChatInviteLinkPostRequest
from tele_rest.models.edit_chat_subscription_invite_link_post_request import EditChatSubscriptionInviteLinkPostRequest as EditChatSubscriptionInviteLinkPostRequest
from tele_rest.models.edit_forum_topic_post_request import EditForumTopicPostRequest as EditForumTopicPostRequest
from tele_rest.models.edit_general_forum_topic_post_request import EditGeneralForumTopicPostRequest as EditGeneralForumTopicPostRequest
from tele_rest.models.edit_message_caption_post_request import EditMessageCaptionPostRequest as EditMessageCaptionPostRequest
from tele_rest.models.edit_message_live_location_post_request import EditMessageLiveLocationPostRequest as EditMessageLiveLocationPostRequest
from tele_rest.models.edit_message_reply_markup_post_request import EditMessageReplyMarkupPostRequest as EditMessageReplyMarkupPostRequest
from tele_rest.models.edit_message_text_post200_response import EditMessageTextPost200Response as EditMessageTextPost200Response
from tele_rest.models.edit_message_text_post200_response_result import EditMessageTextPost200ResponseResult as EditMessageTextPost200ResponseResult
from tele_rest.models.edit_message_text_post_request import EditMessageTextPostRequest as EditMessageTextPostRequest
from tele_rest.models.edit_message_text_post_request_chat_id import EditMessageTextPostRequestChatId as EditMessageTextPostRequestChatId
from tele_rest.models.edit_user_star_subscription_post_request import EditUserStarSubscriptionPostRequest as EditUserStarSubscriptionPostRequest
from tele_rest.models.encrypted_credentials import EncryptedCredentials as EncryptedCredentials
from tele_rest.models.encrypted_passport_element import EncryptedPassportElement as EncryptedPassportElement
from tele_rest.models.error import Error as Error
from tele_rest.models.export_chat_invite_link_post200_response import ExportChatInviteLinkPost200Response as ExportChatInviteLinkPost200Response
from tele_rest.models.export_chat_invite_link_post_request import ExportChatInviteLinkPostRequest as ExportChatInviteLinkPostRequest
from tele_rest.models.external_reply_info import ExternalReplyInfo as ExternalReplyInfo
from tele_rest.models.file import File as File
from tele_rest.models.force_reply import ForceReply as ForceReply
from tele_rest.models.forum_topic import ForumTopic as ForumTopic
from tele_rest.models.forum_topic_created import ForumTopicCreated as ForumTopicCreated
from tele_rest.models.forum_topic_edited import ForumTopicEdited as ForumTopicEdited
from tele_rest.models.forward_message_post_request import ForwardMessagePostRequest as ForwardMessagePostRequest
from tele_rest.models.forward_message_post_request_from_chat_id import ForwardMessagePostRequestFromChatId as ForwardMessagePostRequestFromChatId
from tele_rest.models.forward_messages_post200_response import ForwardMessagesPost200Response as ForwardMessagesPost200Response
from tele_rest.models.forward_messages_post_request import ForwardMessagesPostRequest as ForwardMessagesPostRequest
from tele_rest.models.forward_messages_post_request_from_chat_id import ForwardMessagesPostRequestFromChatId as ForwardMessagesPostRequestFromChatId
from tele_rest.models.game import Game as Game
from tele_rest.models.game_high_score import GameHighScore as GameHighScore
from tele_rest.models.get_available_gifts_post200_response import GetAvailableGiftsPost200Response as GetAvailableGiftsPost200Response
from tele_rest.models.get_business_account_gifts_post200_response import GetBusinessAccountGiftsPost200Response as GetBusinessAccountGiftsPost200Response
from tele_rest.models.get_business_account_gifts_post_request import GetBusinessAccountGiftsPostRequest as GetBusinessAccountGiftsPostRequest
from tele_rest.models.get_business_account_star_balance_post200_response import GetBusinessAccountStarBalancePost200Response as GetBusinessAccountStarBalancePost200Response
from tele_rest.models.get_business_connection_post200_response import GetBusinessConnectionPost200Response as GetBusinessConnectionPost200Response
from tele_rest.models.get_business_connection_post_request import GetBusinessConnectionPostRequest as GetBusinessConnectionPostRequest
from tele_rest.models.get_chat_administrators_post200_response import GetChatAdministratorsPost200Response as GetChatAdministratorsPost200Response
from tele_rest.models.get_chat_member_count_post200_response import GetChatMemberCountPost200Response as GetChatMemberCountPost200Response
from tele_rest.models.get_chat_member_post200_response import GetChatMemberPost200Response as GetChatMemberPost200Response
from tele_rest.models.get_chat_member_post_request import GetChatMemberPostRequest as GetChatMemberPostRequest
from tele_rest.models.get_chat_menu_button_post200_response import GetChatMenuButtonPost200Response as GetChatMenuButtonPost200Response
from tele_rest.models.get_chat_menu_button_post_request import GetChatMenuButtonPostRequest as GetChatMenuButtonPostRequest
from tele_rest.models.get_chat_post200_response import GetChatPost200Response as GetChatPost200Response
from tele_rest.models.get_custom_emoji_stickers_post_request import GetCustomEmojiStickersPostRequest as GetCustomEmojiStickersPostRequest
from tele_rest.models.get_file_post200_response import GetFilePost200Response as GetFilePost200Response
from tele_rest.models.get_file_post_request import GetFilePostRequest as GetFilePostRequest
from tele_rest.models.get_forum_topic_icon_stickers_post200_response import GetForumTopicIconStickersPost200Response as GetForumTopicIconStickersPost200Response
from tele_rest.models.get_game_high_scores_post200_response import GetGameHighScoresPost200Response as GetGameHighScoresPost200Response
from tele_rest.models.get_game_high_scores_post_request import GetGameHighScoresPostRequest as GetGameHighScoresPostRequest
from tele_rest.models.get_me_post200_response import GetMePost200Response as GetMePost200Response
from tele_rest.models.get_my_commands_post200_response import GetMyCommandsPost200Response as GetMyCommandsPost200Response
from tele_rest.models.get_my_commands_post_request import GetMyCommandsPostRequest as GetMyCommandsPostRequest
from tele_rest.models.get_my_default_administrator_rights_post200_response import GetMyDefaultAdministratorRightsPost200Response as GetMyDefaultAdministratorRightsPost200Response
from tele_rest.models.get_my_default_administrator_rights_post_request import GetMyDefaultAdministratorRightsPostRequest as GetMyDefaultAdministratorRightsPostRequest
from tele_rest.models.get_my_description_post200_response import GetMyDescriptionPost200Response as GetMyDescriptionPost200Response
from tele_rest.models.get_my_name_post200_response import GetMyNamePost200Response as GetMyNamePost200Response
from tele_rest.models.get_my_name_post_request import GetMyNamePostRequest as GetMyNamePostRequest
from tele_rest.models.get_my_short_description_post200_response import GetMyShortDescriptionPost200Response as GetMyShortDescriptionPost200Response
from tele_rest.models.get_star_transactions_post200_response import GetStarTransactionsPost200Response as GetStarTransactionsPost200Response
from tele_rest.models.get_star_transactions_post_request import GetStarTransactionsPostRequest as GetStarTransactionsPostRequest
from tele_rest.models.get_sticker_set_post200_response import GetStickerSetPost200Response as GetStickerSetPost200Response
from tele_rest.models.get_sticker_set_post_request import GetStickerSetPostRequest as GetStickerSetPostRequest
from tele_rest.models.get_updates_post200_response import GetUpdatesPost200Response as GetUpdatesPost200Response
from tele_rest.models.get_updates_post_request import GetUpdatesPostRequest as GetUpdatesPostRequest
from tele_rest.models.get_user_chat_boosts_post200_response import GetUserChatBoostsPost200Response as GetUserChatBoostsPost200Response
from tele_rest.models.get_user_chat_boosts_post_request import GetUserChatBoostsPostRequest as GetUserChatBoostsPostRequest
from tele_rest.models.get_user_chat_boosts_post_request_chat_id import GetUserChatBoostsPostRequestChatId as GetUserChatBoostsPostRequestChatId
from tele_rest.models.get_user_profile_photos_post200_response import GetUserProfilePhotosPost200Response as GetUserProfilePhotosPost200Response
from tele_rest.models.get_user_profile_photos_post_request import GetUserProfilePhotosPostRequest as GetUserProfilePhotosPostRequest
from tele_rest.models.get_webhook_info_post200_response import GetWebhookInfoPost200Response as GetWebhookInfoPost200Response
from tele_rest.models.gift import Gift as Gift
from tele_rest.models.gift_info import GiftInfo as GiftInfo
from tele_rest.models.gift_premium_subscription_post_request import GiftPremiumSubscriptionPostRequest as GiftPremiumSubscriptionPostRequest
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
from tele_rest.models.leave_chat_post_request import LeaveChatPostRequest as LeaveChatPostRequest
from tele_rest.models.leave_chat_post_request_chat_id import LeaveChatPostRequestChatId as LeaveChatPostRequestChatId
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
from tele_rest.models.pin_chat_message_post_request import PinChatMessagePostRequest as PinChatMessagePostRequest
from tele_rest.models.poll import Poll as Poll
from tele_rest.models.poll_answer import PollAnswer as PollAnswer
from tele_rest.models.poll_option import PollOption as PollOption
from tele_rest.models.post_story_post200_response import PostStoryPost200Response as PostStoryPost200Response
from tele_rest.models.pre_checkout_query import PreCheckoutQuery as PreCheckoutQuery
from tele_rest.models.prepared_inline_message import PreparedInlineMessage as PreparedInlineMessage
from tele_rest.models.promote_chat_member_post_request import PromoteChatMemberPostRequest as PromoteChatMemberPostRequest
from tele_rest.models.proximity_alert_triggered import ProximityAlertTriggered as ProximityAlertTriggered
from tele_rest.models.reaction_count import ReactionCount as ReactionCount
from tele_rest.models.reaction_type import ReactionType as ReactionType
from tele_rest.models.reaction_type_custom_emoji import ReactionTypeCustomEmoji as ReactionTypeCustomEmoji
from tele_rest.models.reaction_type_emoji import ReactionTypeEmoji as ReactionTypeEmoji
from tele_rest.models.reaction_type_paid import ReactionTypePaid as ReactionTypePaid
from tele_rest.models.read_business_message_post_request import ReadBusinessMessagePostRequest as ReadBusinessMessagePostRequest
from tele_rest.models.refund_star_payment_post_request import RefundStarPaymentPostRequest as RefundStarPaymentPostRequest
from tele_rest.models.refunded_payment import RefundedPayment as RefundedPayment
from tele_rest.models.remove_business_account_profile_photo_post_request import RemoveBusinessAccountProfilePhotoPostRequest as RemoveBusinessAccountProfilePhotoPostRequest
from tele_rest.models.remove_user_verification_post_request import RemoveUserVerificationPostRequest as RemoveUserVerificationPostRequest
from tele_rest.models.reply_keyboard_markup import ReplyKeyboardMarkup as ReplyKeyboardMarkup
from tele_rest.models.reply_keyboard_remove import ReplyKeyboardRemove as ReplyKeyboardRemove
from tele_rest.models.reply_parameters import ReplyParameters as ReplyParameters
from tele_rest.models.reply_parameters_chat_id import ReplyParametersChatId as ReplyParametersChatId
from tele_rest.models.response_parameters import ResponseParameters as ResponseParameters
from tele_rest.models.restrict_chat_member_post_request import RestrictChatMemberPostRequest as RestrictChatMemberPostRequest
from tele_rest.models.restrict_chat_member_post_request_chat_id import RestrictChatMemberPostRequestChatId as RestrictChatMemberPostRequestChatId
from tele_rest.models.revenue_withdrawal_state import RevenueWithdrawalState as RevenueWithdrawalState
from tele_rest.models.revenue_withdrawal_state_failed import RevenueWithdrawalStateFailed as RevenueWithdrawalStateFailed
from tele_rest.models.revenue_withdrawal_state_pending import RevenueWithdrawalStatePending as RevenueWithdrawalStatePending
from tele_rest.models.revenue_withdrawal_state_succeeded import RevenueWithdrawalStateSucceeded as RevenueWithdrawalStateSucceeded
from tele_rest.models.revoke_chat_invite_link_post_request import RevokeChatInviteLinkPostRequest as RevokeChatInviteLinkPostRequest
from tele_rest.models.revoke_chat_invite_link_post_request_chat_id import RevokeChatInviteLinkPostRequestChatId as RevokeChatInviteLinkPostRequestChatId
from tele_rest.models.save_prepared_inline_message_post200_response import SavePreparedInlineMessagePost200Response as SavePreparedInlineMessagePost200Response
from tele_rest.models.save_prepared_inline_message_post_request import SavePreparedInlineMessagePostRequest as SavePreparedInlineMessagePostRequest
from tele_rest.models.send_animation_post_request_animation import SendAnimationPostRequestAnimation as SendAnimationPostRequestAnimation
from tele_rest.models.send_audio_post_request_audio import SendAudioPostRequestAudio as SendAudioPostRequestAudio
from tele_rest.models.send_audio_post_request_thumbnail import SendAudioPostRequestThumbnail as SendAudioPostRequestThumbnail
from tele_rest.models.send_chat_action_post_request import SendChatActionPostRequest as SendChatActionPostRequest
from tele_rest.models.send_contact_post_request import SendContactPostRequest as SendContactPostRequest
from tele_rest.models.send_dice_post_request import SendDicePostRequest as SendDicePostRequest
from tele_rest.models.send_document_post_request_document import SendDocumentPostRequestDocument as SendDocumentPostRequestDocument
from tele_rest.models.send_game_post_request import SendGamePostRequest as SendGamePostRequest
from tele_rest.models.send_gift_post_request import SendGiftPostRequest as SendGiftPostRequest
from tele_rest.models.send_gift_post_request_chat_id import SendGiftPostRequestChatId as SendGiftPostRequestChatId
from tele_rest.models.send_invoice_post_request import SendInvoicePostRequest as SendInvoicePostRequest
from tele_rest.models.send_location_post_request import SendLocationPostRequest as SendLocationPostRequest
from tele_rest.models.send_media_group_post200_response import SendMediaGroupPost200Response as SendMediaGroupPost200Response
from tele_rest.models.send_media_group_post_request_media_inner import SendMediaGroupPostRequestMediaInner as SendMediaGroupPostRequestMediaInner
from tele_rest.models.send_message_post200_response import SendMessagePost200Response as SendMessagePost200Response
from tele_rest.models.send_message_post_request import SendMessagePostRequest as SendMessagePostRequest
from tele_rest.models.send_message_post_request_chat_id import SendMessagePostRequestChatId as SendMessagePostRequestChatId
from tele_rest.models.send_message_post_request_reply_markup import SendMessagePostRequestReplyMarkup as SendMessagePostRequestReplyMarkup
from tele_rest.models.send_paid_media_post_request_chat_id import SendPaidMediaPostRequestChatId as SendPaidMediaPostRequestChatId
from tele_rest.models.send_photo_post_request_photo import SendPhotoPostRequestPhoto as SendPhotoPostRequestPhoto
from tele_rest.models.send_poll_post_request import SendPollPostRequest as SendPollPostRequest
from tele_rest.models.send_sticker_post_request_sticker import SendStickerPostRequestSticker as SendStickerPostRequestSticker
from tele_rest.models.send_venue_post_request import SendVenuePostRequest as SendVenuePostRequest
from tele_rest.models.send_video_note_post_request_video_note import SendVideoNotePostRequestVideoNote as SendVideoNotePostRequestVideoNote
from tele_rest.models.send_video_post_request_cover import SendVideoPostRequestCover as SendVideoPostRequestCover
from tele_rest.models.send_video_post_request_video import SendVideoPostRequestVideo as SendVideoPostRequestVideo
from tele_rest.models.send_voice_post_request_voice import SendVoicePostRequestVoice as SendVoicePostRequestVoice
from tele_rest.models.sent_web_app_message import SentWebAppMessage as SentWebAppMessage
from tele_rest.models.set_business_account_bio_post_request import SetBusinessAccountBioPostRequest as SetBusinessAccountBioPostRequest
from tele_rest.models.set_business_account_gift_settings_post_request import SetBusinessAccountGiftSettingsPostRequest as SetBusinessAccountGiftSettingsPostRequest
from tele_rest.models.set_business_account_name_post_request import SetBusinessAccountNamePostRequest as SetBusinessAccountNamePostRequest
from tele_rest.models.set_business_account_username_post_request import SetBusinessAccountUsernamePostRequest as SetBusinessAccountUsernamePostRequest
from tele_rest.models.set_chat_administrator_custom_title_post_request import SetChatAdministratorCustomTitlePostRequest as SetChatAdministratorCustomTitlePostRequest
from tele_rest.models.set_chat_description_post_request import SetChatDescriptionPostRequest as SetChatDescriptionPostRequest
from tele_rest.models.set_chat_menu_button_post_request import SetChatMenuButtonPostRequest as SetChatMenuButtonPostRequest
from tele_rest.models.set_chat_permissions_post_request import SetChatPermissionsPostRequest as SetChatPermissionsPostRequest
from tele_rest.models.set_chat_sticker_set_post_request import SetChatStickerSetPostRequest as SetChatStickerSetPostRequest
from tele_rest.models.set_chat_title_post_request import SetChatTitlePostRequest as SetChatTitlePostRequest
from tele_rest.models.set_custom_emoji_sticker_set_thumbnail_post_request import SetCustomEmojiStickerSetThumbnailPostRequest as SetCustomEmojiStickerSetThumbnailPostRequest
from tele_rest.models.set_game_score_post_request import SetGameScorePostRequest as SetGameScorePostRequest
from tele_rest.models.set_message_reaction_post_request import SetMessageReactionPostRequest as SetMessageReactionPostRequest
from tele_rest.models.set_my_commands_post_request import SetMyCommandsPostRequest as SetMyCommandsPostRequest
from tele_rest.models.set_my_default_administrator_rights_post_request import SetMyDefaultAdministratorRightsPostRequest as SetMyDefaultAdministratorRightsPostRequest
from tele_rest.models.set_my_description_post_request import SetMyDescriptionPostRequest as SetMyDescriptionPostRequest
from tele_rest.models.set_my_name_post_request import SetMyNamePostRequest as SetMyNamePostRequest
from tele_rest.models.set_my_short_description_post_request import SetMyShortDescriptionPostRequest as SetMyShortDescriptionPostRequest
from tele_rest.models.set_passport_data_errors_post_request import SetPassportDataErrorsPostRequest as SetPassportDataErrorsPostRequest
from tele_rest.models.set_sticker_emoji_list_post_request import SetStickerEmojiListPostRequest as SetStickerEmojiListPostRequest
from tele_rest.models.set_sticker_keywords_post_request import SetStickerKeywordsPostRequest as SetStickerKeywordsPostRequest
from tele_rest.models.set_sticker_mask_position_post_request import SetStickerMaskPositionPostRequest as SetStickerMaskPositionPostRequest
from tele_rest.models.set_sticker_position_in_set_post_request import SetStickerPositionInSetPostRequest as SetStickerPositionInSetPostRequest
from tele_rest.models.set_sticker_set_thumbnail_post_request_thumbnail import SetStickerSetThumbnailPostRequestThumbnail as SetStickerSetThumbnailPostRequestThumbnail
from tele_rest.models.set_sticker_set_title_post_request import SetStickerSetTitlePostRequest as SetStickerSetTitlePostRequest
from tele_rest.models.set_user_emoji_status_post_request import SetUserEmojiStatusPostRequest as SetUserEmojiStatusPostRequest
from tele_rest.models.set_webhook_post200_response import SetWebhookPost200Response as SetWebhookPost200Response
from tele_rest.models.shared_user import SharedUser as SharedUser
from tele_rest.models.shipping_address import ShippingAddress as ShippingAddress
from tele_rest.models.shipping_option import ShippingOption as ShippingOption
from tele_rest.models.shipping_query import ShippingQuery as ShippingQuery
from tele_rest.models.star_amount import StarAmount as StarAmount
from tele_rest.models.star_transaction import StarTransaction as StarTransaction
from tele_rest.models.star_transactions import StarTransactions as StarTransactions
from tele_rest.models.sticker import Sticker as Sticker
from tele_rest.models.sticker_set import StickerSet as StickerSet
from tele_rest.models.stop_message_live_location_post_request import StopMessageLiveLocationPostRequest as StopMessageLiveLocationPostRequest
from tele_rest.models.stop_poll_post200_response import StopPollPost200Response as StopPollPost200Response
from tele_rest.models.stop_poll_post_request import StopPollPostRequest as StopPollPostRequest
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
from tele_rest.models.transfer_business_account_stars_post_request import TransferBusinessAccountStarsPostRequest as TransferBusinessAccountStarsPostRequest
from tele_rest.models.transfer_gift_post_request import TransferGiftPostRequest as TransferGiftPostRequest
from tele_rest.models.unban_chat_member_post_request import UnbanChatMemberPostRequest as UnbanChatMemberPostRequest
from tele_rest.models.unique_gift import UniqueGift as UniqueGift
from tele_rest.models.unique_gift_backdrop import UniqueGiftBackdrop as UniqueGiftBackdrop
from tele_rest.models.unique_gift_backdrop_colors import UniqueGiftBackdropColors as UniqueGiftBackdropColors
from tele_rest.models.unique_gift_info import UniqueGiftInfo as UniqueGiftInfo
from tele_rest.models.unique_gift_model import UniqueGiftModel as UniqueGiftModel
from tele_rest.models.unique_gift_symbol import UniqueGiftSymbol as UniqueGiftSymbol
from tele_rest.models.unpin_chat_message_post_request import UnpinChatMessagePostRequest as UnpinChatMessagePostRequest
from tele_rest.models.update import Update as Update
from tele_rest.models.upgrade_gift_post_request import UpgradeGiftPostRequest as UpgradeGiftPostRequest
from tele_rest.models.user import User as User
from tele_rest.models.user_chat_boosts import UserChatBoosts as UserChatBoosts
from tele_rest.models.user_profile_photos import UserProfilePhotos as UserProfilePhotos
from tele_rest.models.users_shared import UsersShared as UsersShared
from tele_rest.models.venue import Venue as Venue
from tele_rest.models.verify_chat_post_request import VerifyChatPostRequest as VerifyChatPostRequest
from tele_rest.models.verify_user_post_request import VerifyUserPostRequest as VerifyUserPostRequest
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
