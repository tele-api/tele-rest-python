# SetMessageReactionPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat_id** | [**SendMessagePostRequestChatId**](SendMessagePostRequestChatId.md) |  | 
**message_id** | **int** | Identifier of the target message. If the message belongs to a media group, the reaction is set to the first non-deleted message in the group instead. | 
**reaction** | [**List[ReactionType]**](ReactionType.md) | A JSON-serialized list of reaction types to set on the message. Currently, as non-premium users, bots can set up to one reaction per message. A custom emoji reaction can be used if it is either already present on the message or explicitly allowed by chat administrators. Paid reactions can&#39;t be used by bots. | [optional] 
**is_big** | **bool** | Pass *True* to set the reaction with a big animation | [optional] 

## Example

```python
from tele_rest.models.set_message_reaction_post_request import SetMessageReactionPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetMessageReactionPostRequest from a JSON string
set_message_reaction_post_request_instance = SetMessageReactionPostRequest.from_json(json)
# print the JSON string representation of the object
print(SetMessageReactionPostRequest.to_json())

# convert the object into a dict
set_message_reaction_post_request_dict = set_message_reaction_post_request_instance.to_dict()
# create an instance of SetMessageReactionPostRequest from a dict
set_message_reaction_post_request_from_dict = SetMessageReactionPostRequest.from_dict(set_message_reaction_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


