# Message

This object represents a message.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message_id** | **int** | Unique message identifier inside this chat. In specific instances (e.g., message containing a video sent to a big chat), the server might automatically schedule a message instead of sending it immediately. In such cases, this field will be 0 and the relevant message will be unusable until it is actually sent | 
**message_thread_id** | **int** | *Optional*. Unique identifier of a message thread to which the message belongs; for supergroups only | [optional] 
**var_from** | [**User**](User.md) |  | [optional] 
**sender_chat** | [**Chat**](Chat.md) |  | [optional] 
**sender_boost_count** | **int** | *Optional*. If the sender of the message boosted the chat, the number of boosts added by the user | [optional] 
**sender_business_bot** | [**User**](User.md) |  | [optional] 
**var_date** | **int** | Date the message was sent in Unix time. It is always a positive number, representing a valid date. | 
**business_connection_id** | **str** | *Optional*. Unique identifier of the business connection from which the message was received. If non-empty, the message belongs to a chat of the corresponding business account that is independent from any potential bot chat which might share the same identifier. | [optional] 
**chat** | [**Chat**](Chat.md) |  | 
**forward_origin** | [**MessageOrigin**](MessageOrigin.md) |  | [optional] 
**is_topic_message** | **bool** | *Optional*. *True*, if the message is sent to a forum topic | [optional] [default to True]
**is_automatic_forward** | **bool** | *Optional*. *True*, if the message is a channel post that was automatically forwarded to the connected discussion group | [optional] [default to True]
**reply_to_message** | [**Message**](Message.md) |  | [optional] 
**external_reply** | [**ExternalReplyInfo**](ExternalReplyInfo.md) |  | [optional] 
**quote** | [**TextQuote**](TextQuote.md) |  | [optional] 
**reply_to_story** | [**Story**](Story.md) |  | [optional] 
**via_bot** | [**User**](User.md) |  | [optional] 
**edit_date** | **int** | *Optional*. Date the message was last edited in Unix time | [optional] 
**has_protected_content** | **bool** | *Optional*. *True*, if the message can&#39;t be forwarded | [optional] [default to True]
**is_from_offline** | **bool** | *Optional*. *True*, if the message was sent by an implicit action, for example, as an away or a greeting business message, or as a scheduled message | [optional] [default to True]
**media_group_id** | **str** | *Optional*. The unique identifier of a media message group this message belongs to | [optional] 
**author_signature** | **str** | *Optional*. Signature of the post author for messages in channels, or the custom title of an anonymous group administrator | [optional] 
**paid_star_count** | **int** | *Optional*. The number of Telegram Stars that were paid by the sender of the message to send it | [optional] 
**text** | **str** | *Optional*. For text messages, the actual UTF-8 text of the message | [optional] 
**entities** | [**List[MessageEntity]**](MessageEntity.md) | *Optional*. For text messages, special entities like usernames, URLs, bot commands, etc. that appear in the text | [optional] 
**link_preview_options** | [**LinkPreviewOptions**](LinkPreviewOptions.md) |  | [optional] 
**effect_id** | **str** | *Optional*. Unique identifier of the message effect added to the message | [optional] 
**animation** | [**Animation**](Animation.md) |  | [optional] 
**audio** | [**Audio**](Audio.md) |  | [optional] 
**document** | [**Document**](Document.md) |  | [optional] 
**paid_media** | [**PaidMediaInfo**](PaidMediaInfo.md) |  | [optional] 
**photo** | [**List[PhotoSize]**](PhotoSize.md) | *Optional*. Message is a photo, available sizes of the photo | [optional] 
**sticker** | [**Sticker**](Sticker.md) |  | [optional] 
**story** | [**Story**](Story.md) |  | [optional] 
**video** | [**Video**](Video.md) |  | [optional] 
**video_note** | [**VideoNote**](VideoNote.md) |  | [optional] 
**voice** | [**Voice**](Voice.md) |  | [optional] 
**caption** | **str** | *Optional*. Caption for the animation, audio, document, paid media, photo, video or voice | [optional] 
**caption_entities** | [**List[MessageEntity]**](MessageEntity.md) | *Optional*. For messages with a caption, special entities like usernames, URLs, bot commands, etc. that appear in the caption | [optional] 
**show_caption_above_media** | **bool** | *Optional*. *True*, if the caption must be shown above the message media | [optional] [default to True]
**has_media_spoiler** | **bool** | *Optional*. *True*, if the message media is covered by a spoiler animation | [optional] [default to True]
**checklist** | [**Checklist**](Checklist.md) |  | [optional] 
**contact** | [**Contact**](Contact.md) |  | [optional] 
**dice** | [**Dice**](Dice.md) |  | [optional] 
**game** | [**Game**](Game.md) |  | [optional] 
**poll** | [**Poll**](Poll.md) |  | [optional] 
**venue** | [**Venue**](Venue.md) |  | [optional] 
**location** | [**Location**](Location.md) |  | [optional] 
**new_chat_members** | [**List[User]**](User.md) | *Optional*. New members that were added to the group or supergroup and information about them (the bot itself may be one of these members) | [optional] 
**left_chat_member** | [**User**](User.md) |  | [optional] 
**new_chat_title** | **str** | *Optional*. A chat title was changed to this value | [optional] 
**new_chat_photo** | [**List[PhotoSize]**](PhotoSize.md) | *Optional*. A chat photo was change to this value | [optional] 
**delete_chat_photo** | **bool** | *Optional*. Service message: the chat photo was deleted | [optional] [default to True]
**group_chat_created** | **bool** | *Optional*. Service message: the group has been created | [optional] [default to True]
**supergroup_chat_created** | **bool** | *Optional*. Service message: the supergroup has been created. This field can&#39;t be received in a message coming through updates, because bot can&#39;t be a member of a supergroup when it is created. It can only be found in reply\\_to\\_message if someone replies to a very first message in a directly created supergroup. | [optional] [default to True]
**channel_chat_created** | **bool** | *Optional*. Service message: the channel has been created. This field can&#39;t be received in a message coming through updates, because bot can&#39;t be a member of a channel when it is created. It can only be found in reply\\_to\\_message if someone replies to a very first message in a channel. | [optional] [default to True]
**message_auto_delete_timer_changed** | [**MessageAutoDeleteTimerChanged**](MessageAutoDeleteTimerChanged.md) |  | [optional] 
**migrate_to_chat_id** | **int** | *Optional*. The group has been migrated to a supergroup with the specified identifier. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this identifier. | [optional] 
**migrate_from_chat_id** | **int** | *Optional*. The supergroup has been migrated from a group with the specified identifier. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this identifier. | [optional] 
**pinned_message** | [**MaybeInaccessibleMessage**](MaybeInaccessibleMessage.md) |  | [optional] 
**invoice** | [**Invoice**](Invoice.md) |  | [optional] 
**successful_payment** | [**SuccessfulPayment**](SuccessfulPayment.md) |  | [optional] 
**refunded_payment** | [**RefundedPayment**](RefundedPayment.md) |  | [optional] 
**users_shared** | [**UsersShared**](UsersShared.md) |  | [optional] 
**chat_shared** | [**ChatShared**](ChatShared.md) |  | [optional] 
**gift** | [**GiftInfo**](GiftInfo.md) |  | [optional] 
**unique_gift** | [**UniqueGiftInfo**](UniqueGiftInfo.md) |  | [optional] 
**connected_website** | **str** | *Optional*. The domain name of the website on which the user has logged in. [More about Telegram Login »](https://core.telegram.org/widgets/login) | [optional] 
**write_access_allowed** | [**WriteAccessAllowed**](WriteAccessAllowed.md) |  | [optional] 
**passport_data** | [**PassportData**](PassportData.md) |  | [optional] 
**proximity_alert_triggered** | [**ProximityAlertTriggered**](ProximityAlertTriggered.md) |  | [optional] 
**boost_added** | [**ChatBoostAdded**](ChatBoostAdded.md) |  | [optional] 
**chat_background_set** | [**ChatBackground**](ChatBackground.md) |  | [optional] 
**checklist_tasks_done** | [**ChecklistTasksDone**](ChecklistTasksDone.md) |  | [optional] 
**checklist_tasks_added** | [**ChecklistTasksAdded**](ChecklistTasksAdded.md) |  | [optional] 
**direct_message_price_changed** | [**DirectMessagePriceChanged**](DirectMessagePriceChanged.md) |  | [optional] 
**forum_topic_created** | [**ForumTopicCreated**](ForumTopicCreated.md) |  | [optional] 
**forum_topic_edited** | [**ForumTopicEdited**](ForumTopicEdited.md) |  | [optional] 
**forum_topic_closed** | **object** |  | [optional] 
**forum_topic_reopened** | **object** |  | [optional] 
**general_forum_topic_hidden** | **object** |  | [optional] 
**general_forum_topic_unhidden** | **object** |  | [optional] 
**giveaway_created** | [**GiveawayCreated**](GiveawayCreated.md) |  | [optional] 
**giveaway** | [**Giveaway**](Giveaway.md) |  | [optional] 
**giveaway_winners** | [**GiveawayWinners**](GiveawayWinners.md) |  | [optional] 
**giveaway_completed** | [**GiveawayCompleted**](GiveawayCompleted.md) |  | [optional] 
**paid_message_price_changed** | [**PaidMessagePriceChanged**](PaidMessagePriceChanged.md) |  | [optional] 
**video_chat_scheduled** | [**VideoChatScheduled**](VideoChatScheduled.md) |  | [optional] 
**video_chat_started** | **object** |  | [optional] 
**video_chat_ended** | [**VideoChatEnded**](VideoChatEnded.md) |  | [optional] 
**video_chat_participants_invited** | [**VideoChatParticipantsInvited**](VideoChatParticipantsInvited.md) |  | [optional] 
**web_app_data** | [**WebAppData**](WebAppData.md) |  | [optional] 
**reply_markup** | [**InlineKeyboardMarkup**](InlineKeyboardMarkup.md) |  | [optional] 

## Example

```python
from tele_rest.models.message import Message

# TODO update the JSON string below
json = "{}"
# create an instance of Message from a JSON string
message_instance = Message.from_json(json)
# print the JSON string representation of the object
print(Message.to_json())

# convert the object into a dict
message_dict = message_instance.to_dict()
# create an instance of Message from a dict
message_from_dict = Message.from_dict(message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


