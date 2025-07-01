# MessageReactionCountUpdated

This object represents reaction changes on a message with anonymous reactions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat** | [**Chat**](Chat.md) |  | 
**message_id** | **int** | Unique message identifier inside the chat | 
**var_date** | **int** | Date of the change in Unix time | 
**reactions** | [**List[ReactionCount]**](ReactionCount.md) | List of reactions that are present on the message | 

## Example

```python
from tele_rest.models.message_reaction_count_updated import MessageReactionCountUpdated

# TODO update the JSON string below
json = "{}"
# create an instance of MessageReactionCountUpdated from a JSON string
message_reaction_count_updated_instance = MessageReactionCountUpdated.from_json(json)
# print the JSON string representation of the object
print(MessageReactionCountUpdated.to_json())

# convert the object into a dict
message_reaction_count_updated_dict = message_reaction_count_updated_instance.to_dict()
# create an instance of MessageReactionCountUpdated from a dict
message_reaction_count_updated_from_dict = MessageReactionCountUpdated.from_dict(message_reaction_count_updated_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


