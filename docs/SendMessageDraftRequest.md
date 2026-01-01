# SendMessageDraftRequest

Request parameters for sendMessageDraft

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat_id** | **int** | Unique identifier for the target private chat | 
**message_thread_id** | **int** | Unique identifier for the target message thread | [optional] 
**draft_id** | **int** | Unique identifier of the message draft; must be non-zero. Changes of drafts with the same identifier are animated | 
**text** | **str** | Text of the message to be sent, 1-4096 characters after entities parsing | 
**parse_mode** | **str** | Mode for parsing entities in the message text. See [formatting options](https://core.telegram.org/bots/api/#formatting-options) for more details. | [optional] 
**entities** | [**List[MessageEntity]**](MessageEntity.md) | A JSON-serialized list of special entities that appear in message text, which can be specified instead of *parse\\_mode* | [optional] 

## Example

```python
from tele_rest.models.send_message_draft_request import SendMessageDraftRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SendMessageDraftRequest from a JSON string
send_message_draft_request_instance = SendMessageDraftRequest.from_json(json)
# print the JSON string representation of the object
print(SendMessageDraftRequest.to_json())

# convert the object into a dict
send_message_draft_request_dict = send_message_draft_request_instance.to_dict()
# create an instance of SendMessageDraftRequest from a dict
send_message_draft_request_from_dict = SendMessageDraftRequest.from_dict(send_message_draft_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


