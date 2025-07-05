# ExternalReplyInfo

This object contains information about a message that is being replied to, which may come from another chat or forum topic.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**origin** | [**MessageOrigin**](MessageOrigin.md) |  | 
**chat** | [**Chat**](Chat.md) |  | [optional] 
**message_id** | **int** | *Optional*. Unique message identifier inside the original chat. Available only if the original chat is a supergroup or a channel. | [optional] 
**link_preview_options** | [**LinkPreviewOptions**](LinkPreviewOptions.md) |  | [optional] 
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
**has_media_spoiler** | **bool** | *Optional*. *True*, if the message media is covered by a spoiler animation | [optional] [default to True]
**checklist** | [**Checklist**](Checklist.md) |  | [optional] 
**contact** | [**Contact**](Contact.md) |  | [optional] 
**dice** | [**Dice**](Dice.md) |  | [optional] 
**game** | [**Game**](Game.md) |  | [optional] 
**giveaway** | [**Giveaway**](Giveaway.md) |  | [optional] 
**giveaway_winners** | [**GiveawayWinners**](GiveawayWinners.md) |  | [optional] 
**invoice** | [**Invoice**](Invoice.md) |  | [optional] 
**location** | [**Location**](Location.md) |  | [optional] 
**poll** | [**Poll**](Poll.md) |  | [optional] 
**venue** | [**Venue**](Venue.md) |  | [optional] 

## Example

```python
from tele_rest.models.external_reply_info import ExternalReplyInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalReplyInfo from a JSON string
external_reply_info_instance = ExternalReplyInfo.from_json(json)
# print the JSON string representation of the object
print(ExternalReplyInfo.to_json())

# convert the object into a dict
external_reply_info_dict = external_reply_info_instance.to_dict()
# create an instance of ExternalReplyInfo from a dict
external_reply_info_from_dict = ExternalReplyInfo.from_dict(external_reply_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


