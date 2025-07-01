# Python API client for tele-rest
Auto-generated OpenAPI schema

- API version: 9.0.0
- Package version: 9.0.0
- Build date: 2025-07-01T14:15:10.340422036Z[Etc/UTC]

## Requirements.

Python 3.9+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/tele-api/tele-rest-python.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/tele-api/tele-rest-python.git`)

Then import the package:
```python
import tele_rest
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import tele_rest
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import tele_rest
from tele_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.telegram.org/bot123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11
# See configuration.py for a list of all supported configuration parameters.
configuration = tele_rest.Configuration(
    host = "https://api.telegram.org/bot123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11"
)



# Enter a context with an instance of the API client
async with tele_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tele_rest.DefaultApi(api_client)
    user_id = 56 # int | User identifier of sticker set owner
    name = 'name_example' # str | Sticker set name
    sticker = tele_rest.InputSticker() # InputSticker | 

    try:
        api_response = await api_instance.add_sticker_to_set_post(user_id, name, sticker)
        print("The response of DefaultApi->add_sticker_to_set_post:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->add_sticker_to_set_post: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.telegram.org/bot123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**add_sticker_to_set_post**](docs/DefaultApi.md#add_sticker_to_set_post) | **POST** /addStickerToSet | 
*DefaultApi* | [**answer_callback_query_post**](docs/DefaultApi.md#answer_callback_query_post) | **POST** /answerCallbackQuery | 
*DefaultApi* | [**answer_inline_query_post**](docs/DefaultApi.md#answer_inline_query_post) | **POST** /answerInlineQuery | 
*DefaultApi* | [**answer_pre_checkout_query_post**](docs/DefaultApi.md#answer_pre_checkout_query_post) | **POST** /answerPreCheckoutQuery | 
*DefaultApi* | [**answer_shipping_query_post**](docs/DefaultApi.md#answer_shipping_query_post) | **POST** /answerShippingQuery | 
*DefaultApi* | [**answer_web_app_query_post**](docs/DefaultApi.md#answer_web_app_query_post) | **POST** /answerWebAppQuery | 
*DefaultApi* | [**approve_chat_join_request_post**](docs/DefaultApi.md#approve_chat_join_request_post) | **POST** /approveChatJoinRequest | 
*DefaultApi* | [**ban_chat_member_post**](docs/DefaultApi.md#ban_chat_member_post) | **POST** /banChatMember | 
*DefaultApi* | [**ban_chat_sender_chat_post**](docs/DefaultApi.md#ban_chat_sender_chat_post) | **POST** /banChatSenderChat | 
*DefaultApi* | [**close_forum_topic_post**](docs/DefaultApi.md#close_forum_topic_post) | **POST** /closeForumTopic | 
*DefaultApi* | [**close_general_forum_topic_post**](docs/DefaultApi.md#close_general_forum_topic_post) | **POST** /closeGeneralForumTopic | 
*DefaultApi* | [**close_post**](docs/DefaultApi.md#close_post) | **POST** /close | 
*DefaultApi* | [**convert_gift_to_stars_post**](docs/DefaultApi.md#convert_gift_to_stars_post) | **POST** /convertGiftToStars | 
*DefaultApi* | [**copy_message_post**](docs/DefaultApi.md#copy_message_post) | **POST** /copyMessage | 
*DefaultApi* | [**copy_messages_post**](docs/DefaultApi.md#copy_messages_post) | **POST** /copyMessages | 
*DefaultApi* | [**create_chat_invite_link_post**](docs/DefaultApi.md#create_chat_invite_link_post) | **POST** /createChatInviteLink | 
*DefaultApi* | [**create_chat_subscription_invite_link_post**](docs/DefaultApi.md#create_chat_subscription_invite_link_post) | **POST** /createChatSubscriptionInviteLink | 
*DefaultApi* | [**create_forum_topic_post**](docs/DefaultApi.md#create_forum_topic_post) | **POST** /createForumTopic | 
*DefaultApi* | [**create_invoice_link_post**](docs/DefaultApi.md#create_invoice_link_post) | **POST** /createInvoiceLink | 
*DefaultApi* | [**create_new_sticker_set_post**](docs/DefaultApi.md#create_new_sticker_set_post) | **POST** /createNewStickerSet | 
*DefaultApi* | [**decline_chat_join_request_post**](docs/DefaultApi.md#decline_chat_join_request_post) | **POST** /declineChatJoinRequest | 
*DefaultApi* | [**delete_business_messages_post**](docs/DefaultApi.md#delete_business_messages_post) | **POST** /deleteBusinessMessages | 
*DefaultApi* | [**delete_chat_photo_post**](docs/DefaultApi.md#delete_chat_photo_post) | **POST** /deleteChatPhoto | 
*DefaultApi* | [**delete_chat_sticker_set_post**](docs/DefaultApi.md#delete_chat_sticker_set_post) | **POST** /deleteChatStickerSet | 
*DefaultApi* | [**delete_forum_topic_post**](docs/DefaultApi.md#delete_forum_topic_post) | **POST** /deleteForumTopic | 
*DefaultApi* | [**delete_message_post**](docs/DefaultApi.md#delete_message_post) | **POST** /deleteMessage | 
*DefaultApi* | [**delete_messages_post**](docs/DefaultApi.md#delete_messages_post) | **POST** /deleteMessages | 
*DefaultApi* | [**delete_my_commands_post**](docs/DefaultApi.md#delete_my_commands_post) | **POST** /deleteMyCommands | 
*DefaultApi* | [**delete_sticker_from_set_post**](docs/DefaultApi.md#delete_sticker_from_set_post) | **POST** /deleteStickerFromSet | 
*DefaultApi* | [**delete_sticker_set_post**](docs/DefaultApi.md#delete_sticker_set_post) | **POST** /deleteStickerSet | 
*DefaultApi* | [**delete_story_post**](docs/DefaultApi.md#delete_story_post) | **POST** /deleteStory | 
*DefaultApi* | [**delete_webhook_post**](docs/DefaultApi.md#delete_webhook_post) | **POST** /deleteWebhook | 
*DefaultApi* | [**edit_chat_invite_link_post**](docs/DefaultApi.md#edit_chat_invite_link_post) | **POST** /editChatInviteLink | 
*DefaultApi* | [**edit_chat_subscription_invite_link_post**](docs/DefaultApi.md#edit_chat_subscription_invite_link_post) | **POST** /editChatSubscriptionInviteLink | 
*DefaultApi* | [**edit_forum_topic_post**](docs/DefaultApi.md#edit_forum_topic_post) | **POST** /editForumTopic | 
*DefaultApi* | [**edit_general_forum_topic_post**](docs/DefaultApi.md#edit_general_forum_topic_post) | **POST** /editGeneralForumTopic | 
*DefaultApi* | [**edit_message_caption_post**](docs/DefaultApi.md#edit_message_caption_post) | **POST** /editMessageCaption | 
*DefaultApi* | [**edit_message_live_location_post**](docs/DefaultApi.md#edit_message_live_location_post) | **POST** /editMessageLiveLocation | 
*DefaultApi* | [**edit_message_media_post**](docs/DefaultApi.md#edit_message_media_post) | **POST** /editMessageMedia | 
*DefaultApi* | [**edit_message_reply_markup_post**](docs/DefaultApi.md#edit_message_reply_markup_post) | **POST** /editMessageReplyMarkup | 
*DefaultApi* | [**edit_message_text_post**](docs/DefaultApi.md#edit_message_text_post) | **POST** /editMessageText | 
*DefaultApi* | [**edit_story_post**](docs/DefaultApi.md#edit_story_post) | **POST** /editStory | 
*DefaultApi* | [**edit_user_star_subscription_post**](docs/DefaultApi.md#edit_user_star_subscription_post) | **POST** /editUserStarSubscription | 
*DefaultApi* | [**export_chat_invite_link_post**](docs/DefaultApi.md#export_chat_invite_link_post) | **POST** /exportChatInviteLink | 
*DefaultApi* | [**forward_message_post**](docs/DefaultApi.md#forward_message_post) | **POST** /forwardMessage | 
*DefaultApi* | [**forward_messages_post**](docs/DefaultApi.md#forward_messages_post) | **POST** /forwardMessages | 
*DefaultApi* | [**get_available_gifts_post**](docs/DefaultApi.md#get_available_gifts_post) | **POST** /getAvailableGifts | 
*DefaultApi* | [**get_business_account_gifts_post**](docs/DefaultApi.md#get_business_account_gifts_post) | **POST** /getBusinessAccountGifts | 
*DefaultApi* | [**get_business_account_star_balance_post**](docs/DefaultApi.md#get_business_account_star_balance_post) | **POST** /getBusinessAccountStarBalance | 
*DefaultApi* | [**get_business_connection_post**](docs/DefaultApi.md#get_business_connection_post) | **POST** /getBusinessConnection | 
*DefaultApi* | [**get_chat_administrators_post**](docs/DefaultApi.md#get_chat_administrators_post) | **POST** /getChatAdministrators | 
*DefaultApi* | [**get_chat_member_count_post**](docs/DefaultApi.md#get_chat_member_count_post) | **POST** /getChatMemberCount | 
*DefaultApi* | [**get_chat_member_post**](docs/DefaultApi.md#get_chat_member_post) | **POST** /getChatMember | 
*DefaultApi* | [**get_chat_menu_button_post**](docs/DefaultApi.md#get_chat_menu_button_post) | **POST** /getChatMenuButton | 
*DefaultApi* | [**get_chat_post**](docs/DefaultApi.md#get_chat_post) | **POST** /getChat | 
*DefaultApi* | [**get_custom_emoji_stickers_post**](docs/DefaultApi.md#get_custom_emoji_stickers_post) | **POST** /getCustomEmojiStickers | 
*DefaultApi* | [**get_file_post**](docs/DefaultApi.md#get_file_post) | **POST** /getFile | 
*DefaultApi* | [**get_forum_topic_icon_stickers_post**](docs/DefaultApi.md#get_forum_topic_icon_stickers_post) | **POST** /getForumTopicIconStickers | 
*DefaultApi* | [**get_game_high_scores_post**](docs/DefaultApi.md#get_game_high_scores_post) | **POST** /getGameHighScores | 
*DefaultApi* | [**get_me_post**](docs/DefaultApi.md#get_me_post) | **POST** /getMe | 
*DefaultApi* | [**get_my_commands_post**](docs/DefaultApi.md#get_my_commands_post) | **POST** /getMyCommands | 
*DefaultApi* | [**get_my_default_administrator_rights_post**](docs/DefaultApi.md#get_my_default_administrator_rights_post) | **POST** /getMyDefaultAdministratorRights | 
*DefaultApi* | [**get_my_description_post**](docs/DefaultApi.md#get_my_description_post) | **POST** /getMyDescription | 
*DefaultApi* | [**get_my_name_post**](docs/DefaultApi.md#get_my_name_post) | **POST** /getMyName | 
*DefaultApi* | [**get_my_short_description_post**](docs/DefaultApi.md#get_my_short_description_post) | **POST** /getMyShortDescription | 
*DefaultApi* | [**get_star_transactions_post**](docs/DefaultApi.md#get_star_transactions_post) | **POST** /getStarTransactions | 
*DefaultApi* | [**get_sticker_set_post**](docs/DefaultApi.md#get_sticker_set_post) | **POST** /getStickerSet | 
*DefaultApi* | [**get_updates_post**](docs/DefaultApi.md#get_updates_post) | **POST** /getUpdates | 
*DefaultApi* | [**get_user_chat_boosts_post**](docs/DefaultApi.md#get_user_chat_boosts_post) | **POST** /getUserChatBoosts | 
*DefaultApi* | [**get_user_profile_photos_post**](docs/DefaultApi.md#get_user_profile_photos_post) | **POST** /getUserProfilePhotos | 
*DefaultApi* | [**get_webhook_info_post**](docs/DefaultApi.md#get_webhook_info_post) | **POST** /getWebhookInfo | 
*DefaultApi* | [**gift_premium_subscription_post**](docs/DefaultApi.md#gift_premium_subscription_post) | **POST** /giftPremiumSubscription | 
*DefaultApi* | [**hide_general_forum_topic_post**](docs/DefaultApi.md#hide_general_forum_topic_post) | **POST** /hideGeneralForumTopic | 
*DefaultApi* | [**leave_chat_post**](docs/DefaultApi.md#leave_chat_post) | **POST** /leaveChat | 
*DefaultApi* | [**log_out_post**](docs/DefaultApi.md#log_out_post) | **POST** /logOut | 
*DefaultApi* | [**pin_chat_message_post**](docs/DefaultApi.md#pin_chat_message_post) | **POST** /pinChatMessage | 
*DefaultApi* | [**post_story_post**](docs/DefaultApi.md#post_story_post) | **POST** /postStory | 
*DefaultApi* | [**promote_chat_member_post**](docs/DefaultApi.md#promote_chat_member_post) | **POST** /promoteChatMember | 
*DefaultApi* | [**read_business_message_post**](docs/DefaultApi.md#read_business_message_post) | **POST** /readBusinessMessage | 
*DefaultApi* | [**refund_star_payment_post**](docs/DefaultApi.md#refund_star_payment_post) | **POST** /refundStarPayment | 
*DefaultApi* | [**remove_business_account_profile_photo_post**](docs/DefaultApi.md#remove_business_account_profile_photo_post) | **POST** /removeBusinessAccountProfilePhoto | 
*DefaultApi* | [**remove_chat_verification_post**](docs/DefaultApi.md#remove_chat_verification_post) | **POST** /removeChatVerification | 
*DefaultApi* | [**remove_user_verification_post**](docs/DefaultApi.md#remove_user_verification_post) | **POST** /removeUserVerification | 
*DefaultApi* | [**reopen_forum_topic_post**](docs/DefaultApi.md#reopen_forum_topic_post) | **POST** /reopenForumTopic | 
*DefaultApi* | [**reopen_general_forum_topic_post**](docs/DefaultApi.md#reopen_general_forum_topic_post) | **POST** /reopenGeneralForumTopic | 
*DefaultApi* | [**replace_sticker_in_set_post**](docs/DefaultApi.md#replace_sticker_in_set_post) | **POST** /replaceStickerInSet | 
*DefaultApi* | [**restrict_chat_member_post**](docs/DefaultApi.md#restrict_chat_member_post) | **POST** /restrictChatMember | 
*DefaultApi* | [**revoke_chat_invite_link_post**](docs/DefaultApi.md#revoke_chat_invite_link_post) | **POST** /revokeChatInviteLink | 
*DefaultApi* | [**save_prepared_inline_message_post**](docs/DefaultApi.md#save_prepared_inline_message_post) | **POST** /savePreparedInlineMessage | 
*DefaultApi* | [**send_animation_post**](docs/DefaultApi.md#send_animation_post) | **POST** /sendAnimation | 
*DefaultApi* | [**send_audio_post**](docs/DefaultApi.md#send_audio_post) | **POST** /sendAudio | 
*DefaultApi* | [**send_chat_action_post**](docs/DefaultApi.md#send_chat_action_post) | **POST** /sendChatAction | 
*DefaultApi* | [**send_contact_post**](docs/DefaultApi.md#send_contact_post) | **POST** /sendContact | 
*DefaultApi* | [**send_dice_post**](docs/DefaultApi.md#send_dice_post) | **POST** /sendDice | 
*DefaultApi* | [**send_document_post**](docs/DefaultApi.md#send_document_post) | **POST** /sendDocument | 
*DefaultApi* | [**send_game_post**](docs/DefaultApi.md#send_game_post) | **POST** /sendGame | 
*DefaultApi* | [**send_gift_post**](docs/DefaultApi.md#send_gift_post) | **POST** /sendGift | 
*DefaultApi* | [**send_invoice_post**](docs/DefaultApi.md#send_invoice_post) | **POST** /sendInvoice | 
*DefaultApi* | [**send_location_post**](docs/DefaultApi.md#send_location_post) | **POST** /sendLocation | 
*DefaultApi* | [**send_media_group_post**](docs/DefaultApi.md#send_media_group_post) | **POST** /sendMediaGroup | 
*DefaultApi* | [**send_message_post**](docs/DefaultApi.md#send_message_post) | **POST** /sendMessage | 
*DefaultApi* | [**send_paid_media_post**](docs/DefaultApi.md#send_paid_media_post) | **POST** /sendPaidMedia | 
*DefaultApi* | [**send_photo_post**](docs/DefaultApi.md#send_photo_post) | **POST** /sendPhoto | 
*DefaultApi* | [**send_poll_post**](docs/DefaultApi.md#send_poll_post) | **POST** /sendPoll | 
*DefaultApi* | [**send_sticker_post**](docs/DefaultApi.md#send_sticker_post) | **POST** /sendSticker | 
*DefaultApi* | [**send_venue_post**](docs/DefaultApi.md#send_venue_post) | **POST** /sendVenue | 
*DefaultApi* | [**send_video_note_post**](docs/DefaultApi.md#send_video_note_post) | **POST** /sendVideoNote | 
*DefaultApi* | [**send_video_post**](docs/DefaultApi.md#send_video_post) | **POST** /sendVideo | 
*DefaultApi* | [**send_voice_post**](docs/DefaultApi.md#send_voice_post) | **POST** /sendVoice | 
*DefaultApi* | [**set_business_account_bio_post**](docs/DefaultApi.md#set_business_account_bio_post) | **POST** /setBusinessAccountBio | 
*DefaultApi* | [**set_business_account_gift_settings_post**](docs/DefaultApi.md#set_business_account_gift_settings_post) | **POST** /setBusinessAccountGiftSettings | 
*DefaultApi* | [**set_business_account_name_post**](docs/DefaultApi.md#set_business_account_name_post) | **POST** /setBusinessAccountName | 
*DefaultApi* | [**set_business_account_profile_photo_post**](docs/DefaultApi.md#set_business_account_profile_photo_post) | **POST** /setBusinessAccountProfilePhoto | 
*DefaultApi* | [**set_business_account_username_post**](docs/DefaultApi.md#set_business_account_username_post) | **POST** /setBusinessAccountUsername | 
*DefaultApi* | [**set_chat_administrator_custom_title_post**](docs/DefaultApi.md#set_chat_administrator_custom_title_post) | **POST** /setChatAdministratorCustomTitle | 
*DefaultApi* | [**set_chat_description_post**](docs/DefaultApi.md#set_chat_description_post) | **POST** /setChatDescription | 
*DefaultApi* | [**set_chat_menu_button_post**](docs/DefaultApi.md#set_chat_menu_button_post) | **POST** /setChatMenuButton | 
*DefaultApi* | [**set_chat_permissions_post**](docs/DefaultApi.md#set_chat_permissions_post) | **POST** /setChatPermissions | 
*DefaultApi* | [**set_chat_photo_post**](docs/DefaultApi.md#set_chat_photo_post) | **POST** /setChatPhoto | 
*DefaultApi* | [**set_chat_sticker_set_post**](docs/DefaultApi.md#set_chat_sticker_set_post) | **POST** /setChatStickerSet | 
*DefaultApi* | [**set_chat_title_post**](docs/DefaultApi.md#set_chat_title_post) | **POST** /setChatTitle | 
*DefaultApi* | [**set_custom_emoji_sticker_set_thumbnail_post**](docs/DefaultApi.md#set_custom_emoji_sticker_set_thumbnail_post) | **POST** /setCustomEmojiStickerSetThumbnail | 
*DefaultApi* | [**set_game_score_post**](docs/DefaultApi.md#set_game_score_post) | **POST** /setGameScore | 
*DefaultApi* | [**set_message_reaction_post**](docs/DefaultApi.md#set_message_reaction_post) | **POST** /setMessageReaction | 
*DefaultApi* | [**set_my_commands_post**](docs/DefaultApi.md#set_my_commands_post) | **POST** /setMyCommands | 
*DefaultApi* | [**set_my_default_administrator_rights_post**](docs/DefaultApi.md#set_my_default_administrator_rights_post) | **POST** /setMyDefaultAdministratorRights | 
*DefaultApi* | [**set_my_description_post**](docs/DefaultApi.md#set_my_description_post) | **POST** /setMyDescription | 
*DefaultApi* | [**set_my_name_post**](docs/DefaultApi.md#set_my_name_post) | **POST** /setMyName | 
*DefaultApi* | [**set_my_short_description_post**](docs/DefaultApi.md#set_my_short_description_post) | **POST** /setMyShortDescription | 
*DefaultApi* | [**set_passport_data_errors_post**](docs/DefaultApi.md#set_passport_data_errors_post) | **POST** /setPassportDataErrors | 
*DefaultApi* | [**set_sticker_emoji_list_post**](docs/DefaultApi.md#set_sticker_emoji_list_post) | **POST** /setStickerEmojiList | 
*DefaultApi* | [**set_sticker_keywords_post**](docs/DefaultApi.md#set_sticker_keywords_post) | **POST** /setStickerKeywords | 
*DefaultApi* | [**set_sticker_mask_position_post**](docs/DefaultApi.md#set_sticker_mask_position_post) | **POST** /setStickerMaskPosition | 
*DefaultApi* | [**set_sticker_position_in_set_post**](docs/DefaultApi.md#set_sticker_position_in_set_post) | **POST** /setStickerPositionInSet | 
*DefaultApi* | [**set_sticker_set_thumbnail_post**](docs/DefaultApi.md#set_sticker_set_thumbnail_post) | **POST** /setStickerSetThumbnail | 
*DefaultApi* | [**set_sticker_set_title_post**](docs/DefaultApi.md#set_sticker_set_title_post) | **POST** /setStickerSetTitle | 
*DefaultApi* | [**set_user_emoji_status_post**](docs/DefaultApi.md#set_user_emoji_status_post) | **POST** /setUserEmojiStatus | 
*DefaultApi* | [**set_webhook_post**](docs/DefaultApi.md#set_webhook_post) | **POST** /setWebhook | 
*DefaultApi* | [**stop_message_live_location_post**](docs/DefaultApi.md#stop_message_live_location_post) | **POST** /stopMessageLiveLocation | 
*DefaultApi* | [**stop_poll_post**](docs/DefaultApi.md#stop_poll_post) | **POST** /stopPoll | 
*DefaultApi* | [**transfer_business_account_stars_post**](docs/DefaultApi.md#transfer_business_account_stars_post) | **POST** /transferBusinessAccountStars | 
*DefaultApi* | [**transfer_gift_post**](docs/DefaultApi.md#transfer_gift_post) | **POST** /transferGift | 
*DefaultApi* | [**unban_chat_member_post**](docs/DefaultApi.md#unban_chat_member_post) | **POST** /unbanChatMember | 
*DefaultApi* | [**unban_chat_sender_chat_post**](docs/DefaultApi.md#unban_chat_sender_chat_post) | **POST** /unbanChatSenderChat | 
*DefaultApi* | [**unhide_general_forum_topic_post**](docs/DefaultApi.md#unhide_general_forum_topic_post) | **POST** /unhideGeneralForumTopic | 
*DefaultApi* | [**unpin_all_chat_messages_post**](docs/DefaultApi.md#unpin_all_chat_messages_post) | **POST** /unpinAllChatMessages | 
*DefaultApi* | [**unpin_all_forum_topic_messages_post**](docs/DefaultApi.md#unpin_all_forum_topic_messages_post) | **POST** /unpinAllForumTopicMessages | 
*DefaultApi* | [**unpin_all_general_forum_topic_messages_post**](docs/DefaultApi.md#unpin_all_general_forum_topic_messages_post) | **POST** /unpinAllGeneralForumTopicMessages | 
*DefaultApi* | [**unpin_chat_message_post**](docs/DefaultApi.md#unpin_chat_message_post) | **POST** /unpinChatMessage | 
*DefaultApi* | [**upgrade_gift_post**](docs/DefaultApi.md#upgrade_gift_post) | **POST** /upgradeGift | 
*DefaultApi* | [**upload_sticker_file_post**](docs/DefaultApi.md#upload_sticker_file_post) | **POST** /uploadStickerFile | 
*DefaultApi* | [**verify_chat_post**](docs/DefaultApi.md#verify_chat_post) | **POST** /verifyChat | 
*DefaultApi* | [**verify_user_post**](docs/DefaultApi.md#verify_user_post) | **POST** /verifyUser | 


## Documentation For Models

 - [AcceptedGiftTypes](docs/AcceptedGiftTypes.md)
 - [AffiliateInfo](docs/AffiliateInfo.md)
 - [Animation](docs/Animation.md)
 - [AnswerCallbackQueryPostRequest](docs/AnswerCallbackQueryPostRequest.md)
 - [AnswerInlineQueryPostRequest](docs/AnswerInlineQueryPostRequest.md)
 - [AnswerPreCheckoutQueryPostRequest](docs/AnswerPreCheckoutQueryPostRequest.md)
 - [AnswerShippingQueryPostRequest](docs/AnswerShippingQueryPostRequest.md)
 - [AnswerWebAppQueryPost200Response](docs/AnswerWebAppQueryPost200Response.md)
 - [AnswerWebAppQueryPostRequest](docs/AnswerWebAppQueryPostRequest.md)
 - [ApproveChatJoinRequestPostRequest](docs/ApproveChatJoinRequestPostRequest.md)
 - [Audio](docs/Audio.md)
 - [BackgroundFill](docs/BackgroundFill.md)
 - [BackgroundFillFreeformGradient](docs/BackgroundFillFreeformGradient.md)
 - [BackgroundFillGradient](docs/BackgroundFillGradient.md)
 - [BackgroundFillSolid](docs/BackgroundFillSolid.md)
 - [BackgroundType](docs/BackgroundType.md)
 - [BackgroundTypeChatTheme](docs/BackgroundTypeChatTheme.md)
 - [BackgroundTypeFill](docs/BackgroundTypeFill.md)
 - [BackgroundTypePattern](docs/BackgroundTypePattern.md)
 - [BackgroundTypeWallpaper](docs/BackgroundTypeWallpaper.md)
 - [BanChatMemberPostRequest](docs/BanChatMemberPostRequest.md)
 - [BanChatMemberPostRequestChatId](docs/BanChatMemberPostRequestChatId.md)
 - [BanChatSenderChatPostRequest](docs/BanChatSenderChatPostRequest.md)
 - [Birthdate](docs/Birthdate.md)
 - [BotCommand](docs/BotCommand.md)
 - [BotCommandScope](docs/BotCommandScope.md)
 - [BotCommandScopeAllChatAdministrators](docs/BotCommandScopeAllChatAdministrators.md)
 - [BotCommandScopeAllGroupChats](docs/BotCommandScopeAllGroupChats.md)
 - [BotCommandScopeAllPrivateChats](docs/BotCommandScopeAllPrivateChats.md)
 - [BotCommandScopeChat](docs/BotCommandScopeChat.md)
 - [BotCommandScopeChatAdministrators](docs/BotCommandScopeChatAdministrators.md)
 - [BotCommandScopeChatMember](docs/BotCommandScopeChatMember.md)
 - [BotCommandScopeDefault](docs/BotCommandScopeDefault.md)
 - [BotDescription](docs/BotDescription.md)
 - [BotName](docs/BotName.md)
 - [BotShortDescription](docs/BotShortDescription.md)
 - [BusinessBotRights](docs/BusinessBotRights.md)
 - [BusinessConnection](docs/BusinessConnection.md)
 - [BusinessIntro](docs/BusinessIntro.md)
 - [BusinessLocation](docs/BusinessLocation.md)
 - [BusinessMessagesDeleted](docs/BusinessMessagesDeleted.md)
 - [BusinessOpeningHours](docs/BusinessOpeningHours.md)
 - [BusinessOpeningHoursInterval](docs/BusinessOpeningHoursInterval.md)
 - [CallbackQuery](docs/CallbackQuery.md)
 - [Chat](docs/Chat.md)
 - [ChatAdministratorRights](docs/ChatAdministratorRights.md)
 - [ChatBackground](docs/ChatBackground.md)
 - [ChatBoost](docs/ChatBoost.md)
 - [ChatBoostAdded](docs/ChatBoostAdded.md)
 - [ChatBoostRemoved](docs/ChatBoostRemoved.md)
 - [ChatBoostSource](docs/ChatBoostSource.md)
 - [ChatBoostSourceGiftCode](docs/ChatBoostSourceGiftCode.md)
 - [ChatBoostSourceGiveaway](docs/ChatBoostSourceGiveaway.md)
 - [ChatBoostSourcePremium](docs/ChatBoostSourcePremium.md)
 - [ChatBoostUpdated](docs/ChatBoostUpdated.md)
 - [ChatFullInfo](docs/ChatFullInfo.md)
 - [ChatInviteLink](docs/ChatInviteLink.md)
 - [ChatJoinRequest](docs/ChatJoinRequest.md)
 - [ChatLocation](docs/ChatLocation.md)
 - [ChatMember](docs/ChatMember.md)
 - [ChatMemberAdministrator](docs/ChatMemberAdministrator.md)
 - [ChatMemberBanned](docs/ChatMemberBanned.md)
 - [ChatMemberLeft](docs/ChatMemberLeft.md)
 - [ChatMemberMember](docs/ChatMemberMember.md)
 - [ChatMemberOwner](docs/ChatMemberOwner.md)
 - [ChatMemberRestricted](docs/ChatMemberRestricted.md)
 - [ChatMemberUpdated](docs/ChatMemberUpdated.md)
 - [ChatPermissions](docs/ChatPermissions.md)
 - [ChatPhoto](docs/ChatPhoto.md)
 - [ChatShared](docs/ChatShared.md)
 - [ChosenInlineResult](docs/ChosenInlineResult.md)
 - [CloseForumTopicPostRequest](docs/CloseForumTopicPostRequest.md)
 - [Contact](docs/Contact.md)
 - [ConvertGiftToStarsPostRequest](docs/ConvertGiftToStarsPostRequest.md)
 - [CopyMessagePost200Response](docs/CopyMessagePost200Response.md)
 - [CopyMessagePostRequest](docs/CopyMessagePostRequest.md)
 - [CopyMessagesPostRequest](docs/CopyMessagesPostRequest.md)
 - [CopyTextButton](docs/CopyTextButton.md)
 - [CreateChatInviteLinkPost200Response](docs/CreateChatInviteLinkPost200Response.md)
 - [CreateChatInviteLinkPostRequest](docs/CreateChatInviteLinkPostRequest.md)
 - [CreateChatSubscriptionInviteLinkPostRequest](docs/CreateChatSubscriptionInviteLinkPostRequest.md)
 - [CreateChatSubscriptionInviteLinkPostRequestChatId](docs/CreateChatSubscriptionInviteLinkPostRequestChatId.md)
 - [CreateForumTopicPost200Response](docs/CreateForumTopicPost200Response.md)
 - [CreateForumTopicPostRequest](docs/CreateForumTopicPostRequest.md)
 - [CreateInvoiceLinkPostRequest](docs/CreateInvoiceLinkPostRequest.md)
 - [DeleteBusinessMessagesPostRequest](docs/DeleteBusinessMessagesPostRequest.md)
 - [DeleteChatStickerSetPostRequest](docs/DeleteChatStickerSetPostRequest.md)
 - [DeleteMessagePostRequest](docs/DeleteMessagePostRequest.md)
 - [DeleteMessagesPostRequest](docs/DeleteMessagesPostRequest.md)
 - [DeleteMyCommandsPostRequest](docs/DeleteMyCommandsPostRequest.md)
 - [DeleteStickerFromSetPostRequest](docs/DeleteStickerFromSetPostRequest.md)
 - [DeleteStickerSetPostRequest](docs/DeleteStickerSetPostRequest.md)
 - [DeleteStoryPostRequest](docs/DeleteStoryPostRequest.md)
 - [DeleteWebhookPostRequest](docs/DeleteWebhookPostRequest.md)
 - [Dice](docs/Dice.md)
 - [Document](docs/Document.md)
 - [EditChatInviteLinkPostRequest](docs/EditChatInviteLinkPostRequest.md)
 - [EditChatSubscriptionInviteLinkPostRequest](docs/EditChatSubscriptionInviteLinkPostRequest.md)
 - [EditForumTopicPostRequest](docs/EditForumTopicPostRequest.md)
 - [EditGeneralForumTopicPostRequest](docs/EditGeneralForumTopicPostRequest.md)
 - [EditMessageCaptionPostRequest](docs/EditMessageCaptionPostRequest.md)
 - [EditMessageLiveLocationPostRequest](docs/EditMessageLiveLocationPostRequest.md)
 - [EditMessageReplyMarkupPostRequest](docs/EditMessageReplyMarkupPostRequest.md)
 - [EditMessageTextPost200Response](docs/EditMessageTextPost200Response.md)
 - [EditMessageTextPost200ResponseResult](docs/EditMessageTextPost200ResponseResult.md)
 - [EditMessageTextPostRequest](docs/EditMessageTextPostRequest.md)
 - [EditMessageTextPostRequestChatId](docs/EditMessageTextPostRequestChatId.md)
 - [EditUserStarSubscriptionPostRequest](docs/EditUserStarSubscriptionPostRequest.md)
 - [EncryptedCredentials](docs/EncryptedCredentials.md)
 - [EncryptedPassportElement](docs/EncryptedPassportElement.md)
 - [Error](docs/Error.md)
 - [ExportChatInviteLinkPost200Response](docs/ExportChatInviteLinkPost200Response.md)
 - [ExportChatInviteLinkPostRequest](docs/ExportChatInviteLinkPostRequest.md)
 - [ExternalReplyInfo](docs/ExternalReplyInfo.md)
 - [File](docs/File.md)
 - [ForceReply](docs/ForceReply.md)
 - [ForumTopic](docs/ForumTopic.md)
 - [ForumTopicCreated](docs/ForumTopicCreated.md)
 - [ForumTopicEdited](docs/ForumTopicEdited.md)
 - [ForwardMessagePostRequest](docs/ForwardMessagePostRequest.md)
 - [ForwardMessagePostRequestFromChatId](docs/ForwardMessagePostRequestFromChatId.md)
 - [ForwardMessagesPost200Response](docs/ForwardMessagesPost200Response.md)
 - [ForwardMessagesPostRequest](docs/ForwardMessagesPostRequest.md)
 - [ForwardMessagesPostRequestFromChatId](docs/ForwardMessagesPostRequestFromChatId.md)
 - [Game](docs/Game.md)
 - [GameHighScore](docs/GameHighScore.md)
 - [GetAvailableGiftsPost200Response](docs/GetAvailableGiftsPost200Response.md)
 - [GetBusinessAccountGiftsPost200Response](docs/GetBusinessAccountGiftsPost200Response.md)
 - [GetBusinessAccountGiftsPostRequest](docs/GetBusinessAccountGiftsPostRequest.md)
 - [GetBusinessAccountStarBalancePost200Response](docs/GetBusinessAccountStarBalancePost200Response.md)
 - [GetBusinessConnectionPost200Response](docs/GetBusinessConnectionPost200Response.md)
 - [GetBusinessConnectionPostRequest](docs/GetBusinessConnectionPostRequest.md)
 - [GetChatAdministratorsPost200Response](docs/GetChatAdministratorsPost200Response.md)
 - [GetChatMemberCountPost200Response](docs/GetChatMemberCountPost200Response.md)
 - [GetChatMemberPost200Response](docs/GetChatMemberPost200Response.md)
 - [GetChatMemberPostRequest](docs/GetChatMemberPostRequest.md)
 - [GetChatMenuButtonPost200Response](docs/GetChatMenuButtonPost200Response.md)
 - [GetChatMenuButtonPostRequest](docs/GetChatMenuButtonPostRequest.md)
 - [GetChatPost200Response](docs/GetChatPost200Response.md)
 - [GetCustomEmojiStickersPostRequest](docs/GetCustomEmojiStickersPostRequest.md)
 - [GetFilePost200Response](docs/GetFilePost200Response.md)
 - [GetFilePostRequest](docs/GetFilePostRequest.md)
 - [GetForumTopicIconStickersPost200Response](docs/GetForumTopicIconStickersPost200Response.md)
 - [GetGameHighScoresPost200Response](docs/GetGameHighScoresPost200Response.md)
 - [GetGameHighScoresPostRequest](docs/GetGameHighScoresPostRequest.md)
 - [GetMePost200Response](docs/GetMePost200Response.md)
 - [GetMyCommandsPost200Response](docs/GetMyCommandsPost200Response.md)
 - [GetMyCommandsPostRequest](docs/GetMyCommandsPostRequest.md)
 - [GetMyDefaultAdministratorRightsPost200Response](docs/GetMyDefaultAdministratorRightsPost200Response.md)
 - [GetMyDefaultAdministratorRightsPostRequest](docs/GetMyDefaultAdministratorRightsPostRequest.md)
 - [GetMyDescriptionPost200Response](docs/GetMyDescriptionPost200Response.md)
 - [GetMyNamePost200Response](docs/GetMyNamePost200Response.md)
 - [GetMyNamePostRequest](docs/GetMyNamePostRequest.md)
 - [GetMyShortDescriptionPost200Response](docs/GetMyShortDescriptionPost200Response.md)
 - [GetStarTransactionsPost200Response](docs/GetStarTransactionsPost200Response.md)
 - [GetStarTransactionsPostRequest](docs/GetStarTransactionsPostRequest.md)
 - [GetStickerSetPost200Response](docs/GetStickerSetPost200Response.md)
 - [GetStickerSetPostRequest](docs/GetStickerSetPostRequest.md)
 - [GetUpdatesPost200Response](docs/GetUpdatesPost200Response.md)
 - [GetUpdatesPostRequest](docs/GetUpdatesPostRequest.md)
 - [GetUserChatBoostsPost200Response](docs/GetUserChatBoostsPost200Response.md)
 - [GetUserChatBoostsPostRequest](docs/GetUserChatBoostsPostRequest.md)
 - [GetUserChatBoostsPostRequestChatId](docs/GetUserChatBoostsPostRequestChatId.md)
 - [GetUserProfilePhotosPost200Response](docs/GetUserProfilePhotosPost200Response.md)
 - [GetUserProfilePhotosPostRequest](docs/GetUserProfilePhotosPostRequest.md)
 - [GetWebhookInfoPost200Response](docs/GetWebhookInfoPost200Response.md)
 - [Gift](docs/Gift.md)
 - [GiftInfo](docs/GiftInfo.md)
 - [GiftPremiumSubscriptionPostRequest](docs/GiftPremiumSubscriptionPostRequest.md)
 - [Gifts](docs/Gifts.md)
 - [Giveaway](docs/Giveaway.md)
 - [GiveawayCompleted](docs/GiveawayCompleted.md)
 - [GiveawayCreated](docs/GiveawayCreated.md)
 - [GiveawayWinners](docs/GiveawayWinners.md)
 - [InaccessibleMessage](docs/InaccessibleMessage.md)
 - [InlineKeyboardButton](docs/InlineKeyboardButton.md)
 - [InlineKeyboardMarkup](docs/InlineKeyboardMarkup.md)
 - [InlineQuery](docs/InlineQuery.md)
 - [InlineQueryResult](docs/InlineQueryResult.md)
 - [InlineQueryResultArticle](docs/InlineQueryResultArticle.md)
 - [InlineQueryResultAudio](docs/InlineQueryResultAudio.md)
 - [InlineQueryResultCachedAudio](docs/InlineQueryResultCachedAudio.md)
 - [InlineQueryResultCachedDocument](docs/InlineQueryResultCachedDocument.md)
 - [InlineQueryResultCachedGif](docs/InlineQueryResultCachedGif.md)
 - [InlineQueryResultCachedMpeg4Gif](docs/InlineQueryResultCachedMpeg4Gif.md)
 - [InlineQueryResultCachedPhoto](docs/InlineQueryResultCachedPhoto.md)
 - [InlineQueryResultCachedSticker](docs/InlineQueryResultCachedSticker.md)
 - [InlineQueryResultCachedVideo](docs/InlineQueryResultCachedVideo.md)
 - [InlineQueryResultCachedVoice](docs/InlineQueryResultCachedVoice.md)
 - [InlineQueryResultContact](docs/InlineQueryResultContact.md)
 - [InlineQueryResultDocument](docs/InlineQueryResultDocument.md)
 - [InlineQueryResultGame](docs/InlineQueryResultGame.md)
 - [InlineQueryResultGif](docs/InlineQueryResultGif.md)
 - [InlineQueryResultLocation](docs/InlineQueryResultLocation.md)
 - [InlineQueryResultMpeg4Gif](docs/InlineQueryResultMpeg4Gif.md)
 - [InlineQueryResultPhoto](docs/InlineQueryResultPhoto.md)
 - [InlineQueryResultVenue](docs/InlineQueryResultVenue.md)
 - [InlineQueryResultVideo](docs/InlineQueryResultVideo.md)
 - [InlineQueryResultVoice](docs/InlineQueryResultVoice.md)
 - [InlineQueryResultsButton](docs/InlineQueryResultsButton.md)
 - [InputContactMessageContent](docs/InputContactMessageContent.md)
 - [InputInvoiceMessageContent](docs/InputInvoiceMessageContent.md)
 - [InputLocationMessageContent](docs/InputLocationMessageContent.md)
 - [InputMedia](docs/InputMedia.md)
 - [InputMediaAnimation](docs/InputMediaAnimation.md)
 - [InputMediaAudio](docs/InputMediaAudio.md)
 - [InputMediaDocument](docs/InputMediaDocument.md)
 - [InputMediaPhoto](docs/InputMediaPhoto.md)
 - [InputMediaVideo](docs/InputMediaVideo.md)
 - [InputMessageContent](docs/InputMessageContent.md)
 - [InputPaidMedia](docs/InputPaidMedia.md)
 - [InputPaidMediaPhoto](docs/InputPaidMediaPhoto.md)
 - [InputPaidMediaVideo](docs/InputPaidMediaVideo.md)
 - [InputPollOption](docs/InputPollOption.md)
 - [InputProfilePhoto](docs/InputProfilePhoto.md)
 - [InputProfilePhotoAnimated](docs/InputProfilePhotoAnimated.md)
 - [InputProfilePhotoStatic](docs/InputProfilePhotoStatic.md)
 - [InputSticker](docs/InputSticker.md)
 - [InputStoryContent](docs/InputStoryContent.md)
 - [InputStoryContentPhoto](docs/InputStoryContentPhoto.md)
 - [InputStoryContentVideo](docs/InputStoryContentVideo.md)
 - [InputTextMessageContent](docs/InputTextMessageContent.md)
 - [InputVenueMessageContent](docs/InputVenueMessageContent.md)
 - [Invoice](docs/Invoice.md)
 - [KeyboardButton](docs/KeyboardButton.md)
 - [KeyboardButtonPollType](docs/KeyboardButtonPollType.md)
 - [KeyboardButtonRequestChat](docs/KeyboardButtonRequestChat.md)
 - [KeyboardButtonRequestUsers](docs/KeyboardButtonRequestUsers.md)
 - [LabeledPrice](docs/LabeledPrice.md)
 - [LeaveChatPostRequest](docs/LeaveChatPostRequest.md)
 - [LeaveChatPostRequestChatId](docs/LeaveChatPostRequestChatId.md)
 - [LinkPreviewOptions](docs/LinkPreviewOptions.md)
 - [Location](docs/Location.md)
 - [LocationAddress](docs/LocationAddress.md)
 - [LoginUrl](docs/LoginUrl.md)
 - [MaskPosition](docs/MaskPosition.md)
 - [MaybeInaccessibleMessage](docs/MaybeInaccessibleMessage.md)
 - [MenuButton](docs/MenuButton.md)
 - [MenuButtonCommands](docs/MenuButtonCommands.md)
 - [MenuButtonDefault](docs/MenuButtonDefault.md)
 - [MenuButtonWebApp](docs/MenuButtonWebApp.md)
 - [Message](docs/Message.md)
 - [MessageAutoDeleteTimerChanged](docs/MessageAutoDeleteTimerChanged.md)
 - [MessageEntity](docs/MessageEntity.md)
 - [MessageId](docs/MessageId.md)
 - [MessageOrigin](docs/MessageOrigin.md)
 - [MessageOriginChannel](docs/MessageOriginChannel.md)
 - [MessageOriginChat](docs/MessageOriginChat.md)
 - [MessageOriginHiddenUser](docs/MessageOriginHiddenUser.md)
 - [MessageOriginUser](docs/MessageOriginUser.md)
 - [MessageReactionCountUpdated](docs/MessageReactionCountUpdated.md)
 - [MessageReactionUpdated](docs/MessageReactionUpdated.md)
 - [OrderInfo](docs/OrderInfo.md)
 - [OwnedGift](docs/OwnedGift.md)
 - [OwnedGiftRegular](docs/OwnedGiftRegular.md)
 - [OwnedGiftUnique](docs/OwnedGiftUnique.md)
 - [OwnedGifts](docs/OwnedGifts.md)
 - [PaidMedia](docs/PaidMedia.md)
 - [PaidMediaInfo](docs/PaidMediaInfo.md)
 - [PaidMediaPhoto](docs/PaidMediaPhoto.md)
 - [PaidMediaPreview](docs/PaidMediaPreview.md)
 - [PaidMediaPurchased](docs/PaidMediaPurchased.md)
 - [PaidMediaVideo](docs/PaidMediaVideo.md)
 - [PaidMessagePriceChanged](docs/PaidMessagePriceChanged.md)
 - [PassportData](docs/PassportData.md)
 - [PassportElementError](docs/PassportElementError.md)
 - [PassportElementErrorDataField](docs/PassportElementErrorDataField.md)
 - [PassportElementErrorFile](docs/PassportElementErrorFile.md)
 - [PassportElementErrorFiles](docs/PassportElementErrorFiles.md)
 - [PassportElementErrorFrontSide](docs/PassportElementErrorFrontSide.md)
 - [PassportElementErrorReverseSide](docs/PassportElementErrorReverseSide.md)
 - [PassportElementErrorSelfie](docs/PassportElementErrorSelfie.md)
 - [PassportElementErrorTranslationFile](docs/PassportElementErrorTranslationFile.md)
 - [PassportElementErrorTranslationFiles](docs/PassportElementErrorTranslationFiles.md)
 - [PassportElementErrorUnspecified](docs/PassportElementErrorUnspecified.md)
 - [PassportFile](docs/PassportFile.md)
 - [PhotoSize](docs/PhotoSize.md)
 - [PinChatMessagePostRequest](docs/PinChatMessagePostRequest.md)
 - [Poll](docs/Poll.md)
 - [PollAnswer](docs/PollAnswer.md)
 - [PollOption](docs/PollOption.md)
 - [PostStoryPost200Response](docs/PostStoryPost200Response.md)
 - [PreCheckoutQuery](docs/PreCheckoutQuery.md)
 - [PreparedInlineMessage](docs/PreparedInlineMessage.md)
 - [PromoteChatMemberPostRequest](docs/PromoteChatMemberPostRequest.md)
 - [ProximityAlertTriggered](docs/ProximityAlertTriggered.md)
 - [ReactionCount](docs/ReactionCount.md)
 - [ReactionType](docs/ReactionType.md)
 - [ReactionTypeCustomEmoji](docs/ReactionTypeCustomEmoji.md)
 - [ReactionTypeEmoji](docs/ReactionTypeEmoji.md)
 - [ReactionTypePaid](docs/ReactionTypePaid.md)
 - [ReadBusinessMessagePostRequest](docs/ReadBusinessMessagePostRequest.md)
 - [RefundStarPaymentPostRequest](docs/RefundStarPaymentPostRequest.md)
 - [RefundedPayment](docs/RefundedPayment.md)
 - [RemoveBusinessAccountProfilePhotoPostRequest](docs/RemoveBusinessAccountProfilePhotoPostRequest.md)
 - [RemoveUserVerificationPostRequest](docs/RemoveUserVerificationPostRequest.md)
 - [ReplyKeyboardMarkup](docs/ReplyKeyboardMarkup.md)
 - [ReplyKeyboardRemove](docs/ReplyKeyboardRemove.md)
 - [ReplyParameters](docs/ReplyParameters.md)
 - [ReplyParametersChatId](docs/ReplyParametersChatId.md)
 - [ResponseParameters](docs/ResponseParameters.md)
 - [RestrictChatMemberPostRequest](docs/RestrictChatMemberPostRequest.md)
 - [RestrictChatMemberPostRequestChatId](docs/RestrictChatMemberPostRequestChatId.md)
 - [RevenueWithdrawalState](docs/RevenueWithdrawalState.md)
 - [RevenueWithdrawalStateFailed](docs/RevenueWithdrawalStateFailed.md)
 - [RevenueWithdrawalStatePending](docs/RevenueWithdrawalStatePending.md)
 - [RevenueWithdrawalStateSucceeded](docs/RevenueWithdrawalStateSucceeded.md)
 - [RevokeChatInviteLinkPostRequest](docs/RevokeChatInviteLinkPostRequest.md)
 - [RevokeChatInviteLinkPostRequestChatId](docs/RevokeChatInviteLinkPostRequestChatId.md)
 - [SavePreparedInlineMessagePost200Response](docs/SavePreparedInlineMessagePost200Response.md)
 - [SavePreparedInlineMessagePostRequest](docs/SavePreparedInlineMessagePostRequest.md)
 - [SendAnimationPostRequestAnimation](docs/SendAnimationPostRequestAnimation.md)
 - [SendAudioPostRequestAudio](docs/SendAudioPostRequestAudio.md)
 - [SendAudioPostRequestThumbnail](docs/SendAudioPostRequestThumbnail.md)
 - [SendChatActionPostRequest](docs/SendChatActionPostRequest.md)
 - [SendContactPostRequest](docs/SendContactPostRequest.md)
 - [SendDicePostRequest](docs/SendDicePostRequest.md)
 - [SendDocumentPostRequestDocument](docs/SendDocumentPostRequestDocument.md)
 - [SendGamePostRequest](docs/SendGamePostRequest.md)
 - [SendGiftPostRequest](docs/SendGiftPostRequest.md)
 - [SendGiftPostRequestChatId](docs/SendGiftPostRequestChatId.md)
 - [SendInvoicePostRequest](docs/SendInvoicePostRequest.md)
 - [SendLocationPostRequest](docs/SendLocationPostRequest.md)
 - [SendMediaGroupPost200Response](docs/SendMediaGroupPost200Response.md)
 - [SendMediaGroupPostRequestMediaInner](docs/SendMediaGroupPostRequestMediaInner.md)
 - [SendMessagePost200Response](docs/SendMessagePost200Response.md)
 - [SendMessagePostRequest](docs/SendMessagePostRequest.md)
 - [SendMessagePostRequestChatId](docs/SendMessagePostRequestChatId.md)
 - [SendMessagePostRequestReplyMarkup](docs/SendMessagePostRequestReplyMarkup.md)
 - [SendPaidMediaPostRequestChatId](docs/SendPaidMediaPostRequestChatId.md)
 - [SendPhotoPostRequestPhoto](docs/SendPhotoPostRequestPhoto.md)
 - [SendPollPostRequest](docs/SendPollPostRequest.md)
 - [SendStickerPostRequestSticker](docs/SendStickerPostRequestSticker.md)
 - [SendVenuePostRequest](docs/SendVenuePostRequest.md)
 - [SendVideoNotePostRequestVideoNote](docs/SendVideoNotePostRequestVideoNote.md)
 - [SendVideoPostRequestCover](docs/SendVideoPostRequestCover.md)
 - [SendVideoPostRequestVideo](docs/SendVideoPostRequestVideo.md)
 - [SendVoicePostRequestVoice](docs/SendVoicePostRequestVoice.md)
 - [SentWebAppMessage](docs/SentWebAppMessage.md)
 - [SetBusinessAccountBioPostRequest](docs/SetBusinessAccountBioPostRequest.md)
 - [SetBusinessAccountGiftSettingsPostRequest](docs/SetBusinessAccountGiftSettingsPostRequest.md)
 - [SetBusinessAccountNamePostRequest](docs/SetBusinessAccountNamePostRequest.md)
 - [SetBusinessAccountUsernamePostRequest](docs/SetBusinessAccountUsernamePostRequest.md)
 - [SetChatAdministratorCustomTitlePostRequest](docs/SetChatAdministratorCustomTitlePostRequest.md)
 - [SetChatDescriptionPostRequest](docs/SetChatDescriptionPostRequest.md)
 - [SetChatMenuButtonPostRequest](docs/SetChatMenuButtonPostRequest.md)
 - [SetChatPermissionsPostRequest](docs/SetChatPermissionsPostRequest.md)
 - [SetChatStickerSetPostRequest](docs/SetChatStickerSetPostRequest.md)
 - [SetChatTitlePostRequest](docs/SetChatTitlePostRequest.md)
 - [SetCustomEmojiStickerSetThumbnailPostRequest](docs/SetCustomEmojiStickerSetThumbnailPostRequest.md)
 - [SetGameScorePostRequest](docs/SetGameScorePostRequest.md)
 - [SetMessageReactionPostRequest](docs/SetMessageReactionPostRequest.md)
 - [SetMyCommandsPostRequest](docs/SetMyCommandsPostRequest.md)
 - [SetMyDefaultAdministratorRightsPostRequest](docs/SetMyDefaultAdministratorRightsPostRequest.md)
 - [SetMyDescriptionPostRequest](docs/SetMyDescriptionPostRequest.md)
 - [SetMyNamePostRequest](docs/SetMyNamePostRequest.md)
 - [SetMyShortDescriptionPostRequest](docs/SetMyShortDescriptionPostRequest.md)
 - [SetPassportDataErrorsPostRequest](docs/SetPassportDataErrorsPostRequest.md)
 - [SetStickerEmojiListPostRequest](docs/SetStickerEmojiListPostRequest.md)
 - [SetStickerKeywordsPostRequest](docs/SetStickerKeywordsPostRequest.md)
 - [SetStickerMaskPositionPostRequest](docs/SetStickerMaskPositionPostRequest.md)
 - [SetStickerPositionInSetPostRequest](docs/SetStickerPositionInSetPostRequest.md)
 - [SetStickerSetThumbnailPostRequestThumbnail](docs/SetStickerSetThumbnailPostRequestThumbnail.md)
 - [SetStickerSetTitlePostRequest](docs/SetStickerSetTitlePostRequest.md)
 - [SetUserEmojiStatusPostRequest](docs/SetUserEmojiStatusPostRequest.md)
 - [SetWebhookPost200Response](docs/SetWebhookPost200Response.md)
 - [SharedUser](docs/SharedUser.md)
 - [ShippingAddress](docs/ShippingAddress.md)
 - [ShippingOption](docs/ShippingOption.md)
 - [ShippingQuery](docs/ShippingQuery.md)
 - [StarAmount](docs/StarAmount.md)
 - [StarTransaction](docs/StarTransaction.md)
 - [StarTransactions](docs/StarTransactions.md)
 - [Sticker](docs/Sticker.md)
 - [StickerSet](docs/StickerSet.md)
 - [StopMessageLiveLocationPostRequest](docs/StopMessageLiveLocationPostRequest.md)
 - [StopPollPost200Response](docs/StopPollPost200Response.md)
 - [StopPollPostRequest](docs/StopPollPostRequest.md)
 - [Story](docs/Story.md)
 - [StoryArea](docs/StoryArea.md)
 - [StoryAreaPosition](docs/StoryAreaPosition.md)
 - [StoryAreaType](docs/StoryAreaType.md)
 - [StoryAreaTypeLink](docs/StoryAreaTypeLink.md)
 - [StoryAreaTypeLocation](docs/StoryAreaTypeLocation.md)
 - [StoryAreaTypeSuggestedReaction](docs/StoryAreaTypeSuggestedReaction.md)
 - [StoryAreaTypeUniqueGift](docs/StoryAreaTypeUniqueGift.md)
 - [StoryAreaTypeWeather](docs/StoryAreaTypeWeather.md)
 - [SuccessfulPayment](docs/SuccessfulPayment.md)
 - [SwitchInlineQueryChosenChat](docs/SwitchInlineQueryChosenChat.md)
 - [TextQuote](docs/TextQuote.md)
 - [TransactionPartner](docs/TransactionPartner.md)
 - [TransactionPartnerAffiliateProgram](docs/TransactionPartnerAffiliateProgram.md)
 - [TransactionPartnerChat](docs/TransactionPartnerChat.md)
 - [TransactionPartnerFragment](docs/TransactionPartnerFragment.md)
 - [TransactionPartnerOther](docs/TransactionPartnerOther.md)
 - [TransactionPartnerTelegramAds](docs/TransactionPartnerTelegramAds.md)
 - [TransactionPartnerTelegramApi](docs/TransactionPartnerTelegramApi.md)
 - [TransactionPartnerUser](docs/TransactionPartnerUser.md)
 - [TransferBusinessAccountStarsPostRequest](docs/TransferBusinessAccountStarsPostRequest.md)
 - [TransferGiftPostRequest](docs/TransferGiftPostRequest.md)
 - [UnbanChatMemberPostRequest](docs/UnbanChatMemberPostRequest.md)
 - [UniqueGift](docs/UniqueGift.md)
 - [UniqueGiftBackdrop](docs/UniqueGiftBackdrop.md)
 - [UniqueGiftBackdropColors](docs/UniqueGiftBackdropColors.md)
 - [UniqueGiftInfo](docs/UniqueGiftInfo.md)
 - [UniqueGiftModel](docs/UniqueGiftModel.md)
 - [UniqueGiftSymbol](docs/UniqueGiftSymbol.md)
 - [UnpinChatMessagePostRequest](docs/UnpinChatMessagePostRequest.md)
 - [Update](docs/Update.md)
 - [UpgradeGiftPostRequest](docs/UpgradeGiftPostRequest.md)
 - [User](docs/User.md)
 - [UserChatBoosts](docs/UserChatBoosts.md)
 - [UserProfilePhotos](docs/UserProfilePhotos.md)
 - [UsersShared](docs/UsersShared.md)
 - [Venue](docs/Venue.md)
 - [VerifyChatPostRequest](docs/VerifyChatPostRequest.md)
 - [VerifyUserPostRequest](docs/VerifyUserPostRequest.md)
 - [Video](docs/Video.md)
 - [VideoChatEnded](docs/VideoChatEnded.md)
 - [VideoChatParticipantsInvited](docs/VideoChatParticipantsInvited.md)
 - [VideoChatScheduled](docs/VideoChatScheduled.md)
 - [VideoNote](docs/VideoNote.md)
 - [Voice](docs/Voice.md)
 - [WebAppData](docs/WebAppData.md)
 - [WebAppInfo](docs/WebAppInfo.md)
 - [WebhookInfo](docs/WebhookInfo.md)
 - [WriteAccessAllowed](docs/WriteAccessAllowed.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization

Endpoints do not require authorization.


## Author




