# PostSetMessageReactionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat_id** | [**PostSendMessageRequestChatId**](PostSendMessageRequestChatId.md) |  | 
**message_id** | **int** | Identifier of the target message. If the message belongs to a media group, the reaction is set to the first non-deleted message in the group instead. | 
**reaction** | [**List[ReactionType]**](ReactionType.md) | A JSON-serialized list of reaction types to set on the message. Currently, as non-premium users, bots can set up to one reaction per message. A custom emoji reaction can be used if it is either already present on the message or explicitly allowed by chat administrators. Paid reactions can&#39;t be used by bots. | [optional] 
**is_big** | **bool** | Pass *True* to set the reaction with a big animation | [optional] 

## Example

```python
from tele_rest.models.post_set_message_reaction_request import PostSetMessageReactionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostSetMessageReactionRequest from a JSON string
post_set_message_reaction_request_instance = PostSetMessageReactionRequest.from_json(json)
# print the JSON string representation of the object
print(PostSetMessageReactionRequest.to_json())

# convert the object into a dict
post_set_message_reaction_request_dict = post_set_message_reaction_request_instance.to_dict()
# create an instance of PostSetMessageReactionRequest from a dict
post_set_message_reaction_request_from_dict = PostSetMessageReactionRequest.from_dict(post_set_message_reaction_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


