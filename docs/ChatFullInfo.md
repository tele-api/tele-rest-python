# ChatFullInfo

This object contains full information about a chat.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for this chat. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this identifier. | 
**type** | **str** | Type of the chat, can be either “private”, “group”, “supergroup” or “channel” | 
**title** | **str** | *Optional*. Title, for supergroups, channels and group chats | [optional] 
**username** | **str** | *Optional*. Username, for private chats, supergroups and channels if available | [optional] 
**first_name** | **str** | *Optional*. First name of the other party in a private chat | [optional] 
**last_name** | **str** | *Optional*. Last name of the other party in a private chat | [optional] 
**is_forum** | **bool** | *Optional*. *True*, if the supergroup chat is a forum (has [topics](https://telegram.org/blog/topics-in-groups-collectible-usernames#topics-in-groups) enabled) | [optional] [default to True]
**accent_color_id** | **int** | Identifier of the accent color for the chat name and backgrounds of the chat photo, reply header, and link preview. See [accent colors](https://core.telegram.org/bots/api/#accent-colors) for more details. | 
**max_reaction_count** | **int** | The maximum number of reactions that can be set on a message in the chat | 
**photo** | [**ChatPhoto**](ChatPhoto.md) |  | [optional] 
**active_usernames** | **List[str]** | *Optional*. If non-empty, the list of all [active chat usernames](https://telegram.org/blog/topics-in-groups-collectible-usernames#collectible-usernames); for private chats, supergroups and channels | [optional] 
**birthdate** | [**Birthdate**](Birthdate.md) |  | [optional] 
**business_intro** | [**BusinessIntro**](BusinessIntro.md) |  | [optional] 
**business_location** | [**BusinessLocation**](BusinessLocation.md) |  | [optional] 
**business_opening_hours** | [**BusinessOpeningHours**](BusinessOpeningHours.md) |  | [optional] 
**personal_chat** | [**Chat**](Chat.md) |  | [optional] 
**available_reactions** | [**List[ReactionType]**](ReactionType.md) | *Optional*. List of available reactions allowed in the chat. If omitted, then all [emoji reactions](https://core.telegram.org/bots/api/#reactiontypeemoji) are allowed. | [optional] 
**background_custom_emoji_id** | **str** | *Optional*. Custom emoji identifier of the emoji chosen by the chat for the reply header and link preview background | [optional] 
**profile_accent_color_id** | **int** | *Optional*. Identifier of the accent color for the chat&#39;s profile background. See [profile accent colors](https://core.telegram.org/bots/api/#profile-accent-colors) for more details. | [optional] 
**profile_background_custom_emoji_id** | **str** | *Optional*. Custom emoji identifier of the emoji chosen by the chat for its profile background | [optional] 
**emoji_status_custom_emoji_id** | **str** | *Optional*. Custom emoji identifier of the emoji status of the chat or the other party in a private chat | [optional] 
**emoji_status_expiration_date** | **int** | *Optional*. Expiration date of the emoji status of the chat or the other party in a private chat, in Unix time, if any | [optional] 
**bio** | **str** | *Optional*. Bio of the other party in a private chat | [optional] 
**has_private_forwards** | **bool** | *Optional*. *True*, if privacy settings of the other party in the private chat allows to use &#x60;tg://user?id&#x3D;&lt;user_id&gt;&#x60; links only in chats with the user | [optional] [default to True]
**has_restricted_voice_and_video_messages** | **bool** | *Optional*. *True*, if the privacy settings of the other party restrict sending voice and video note messages in the private chat | [optional] [default to True]
**join_to_send_messages** | **bool** | *Optional*. *True*, if users need to join the supergroup before they can send messages | [optional] [default to True]
**join_by_request** | **bool** | *Optional*. *True*, if all users directly joining the supergroup without using an invite link need to be approved by supergroup administrators | [optional] [default to True]
**description** | **str** | *Optional*. Description, for groups, supergroups and channel chats | [optional] 
**invite_link** | **str** | *Optional*. Primary invite link, for groups, supergroups and channel chats | [optional] 
**pinned_message** | [**Message**](Message.md) |  | [optional] 
**permissions** | [**ChatPermissions**](ChatPermissions.md) |  | [optional] 
**accepted_gift_types** | [**AcceptedGiftTypes**](AcceptedGiftTypes.md) |  | 
**can_send_paid_media** | **bool** | *Optional*. *True*, if paid media messages can be sent or forwarded to the channel chat. The field is available only for channel chats. | [optional] [default to True]
**slow_mode_delay** | **int** | *Optional*. For supergroups, the minimum allowed delay between consecutive messages sent by each unprivileged user; in seconds | [optional] 
**unrestrict_boost_count** | **int** | *Optional*. For supergroups, the minimum number of boosts that a non-administrator user needs to add in order to ignore slow mode and chat permissions | [optional] 
**message_auto_delete_time** | **int** | *Optional*. The time after which all messages sent to the chat will be automatically deleted; in seconds | [optional] 
**has_aggressive_anti_spam_enabled** | **bool** | *Optional*. *True*, if aggressive anti-spam checks are enabled in the supergroup. The field is only available to chat administrators. | [optional] [default to True]
**has_hidden_members** | **bool** | *Optional*. *True*, if non-administrators can only get the list of bots and administrators in the chat | [optional] [default to True]
**has_protected_content** | **bool** | *Optional*. *True*, if messages from the chat can&#39;t be forwarded to other chats | [optional] [default to True]
**has_visible_history** | **bool** | *Optional*. *True*, if new chat members will have access to old messages; available only to chat administrators | [optional] [default to True]
**sticker_set_name** | **str** | *Optional*. For supergroups, name of the group sticker set | [optional] 
**can_set_sticker_set** | **bool** | *Optional*. *True*, if the bot can change the group sticker set | [optional] [default to True]
**custom_emoji_sticker_set_name** | **str** | *Optional*. For supergroups, the name of the group&#39;s custom emoji sticker set. Custom emoji from this set can be used by all users and bots in the group. | [optional] 
**linked_chat_id** | **int** | *Optional*. Unique identifier for the linked chat, i.e. the discussion group identifier for a channel and vice versa; for supergroups and channel chats. This identifier may be greater than 32 bits and some programming languages may have difficulty/silent defects in interpreting it. But it is smaller than 52 bits, so a signed 64 bit integer or double-precision float type are safe for storing this identifier. | [optional] 
**location** | [**ChatLocation**](ChatLocation.md) |  | [optional] 

## Example

```python
from tele_rest.models.chat_full_info import ChatFullInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ChatFullInfo from a JSON string
chat_full_info_instance = ChatFullInfo.from_json(json)
# print the JSON string representation of the object
print(ChatFullInfo.to_json())

# convert the object into a dict
chat_full_info_dict = chat_full_info_instance.to_dict()
# create an instance of ChatFullInfo from a dict
chat_full_info_from_dict = ChatFullInfo.from_dict(chat_full_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


