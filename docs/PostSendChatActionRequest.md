# PostSendChatActionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business_connection_id** | **str** | Unique identifier of the business connection on behalf of which the action will be sent | [optional] 
**chat_id** | [**PostSendMessageRequestChatId**](PostSendMessageRequestChatId.md) |  | 
**message_thread_id** | **int** | Unique identifier for the target message thread; for supergroups only | [optional] 
**action** | **str** | Type of action to broadcast. Choose one, depending on what the user is about to receive: *typing* for [text messages](https://core.telegram.org/bots/api/#sendmessage), *upload\\_photo* for [photos](https://core.telegram.org/bots/api/#sendphoto), *record\\_video* or *upload\\_video* for [videos](https://core.telegram.org/bots/api/#sendvideo), *record\\_voice* or *upload\\_voice* for [voice notes](https://core.telegram.org/bots/api/#sendvoice), *upload\\_document* for [general files](https://core.telegram.org/bots/api/#senddocument), *choose\\_sticker* for [stickers](https://core.telegram.org/bots/api/#sendsticker), *find\\_location* for [location data](https://core.telegram.org/bots/api/#sendlocation), *record\\_video\\_note* or *upload\\_video\\_note* for [video notes](https://core.telegram.org/bots/api/#sendvideonote). | 

## Example

```python
from tele_rest.models.post_send_chat_action_request import PostSendChatActionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostSendChatActionRequest from a JSON string
post_send_chat_action_request_instance = PostSendChatActionRequest.from_json(json)
# print the JSON string representation of the object
print(PostSendChatActionRequest.to_json())

# convert the object into a dict
post_send_chat_action_request_dict = post_send_chat_action_request_instance.to_dict()
# create an instance of PostSendChatActionRequest from a dict
post_send_chat_action_request_from_dict = PostSendChatActionRequest.from_dict(post_send_chat_action_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


