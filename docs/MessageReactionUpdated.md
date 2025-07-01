# MessageReactionUpdated

This object represents a change of a reaction on a message performed by a user.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat** | [**Chat**](Chat.md) |  | 
**message_id** | **int** | Unique identifier of the message inside the chat | 
**user** | [**User**](User.md) |  | [optional] 
**actor_chat** | [**Chat**](Chat.md) |  | [optional] 
**var_date** | **int** | Date of the change in Unix time | 
**old_reaction** | [**List[ReactionType]**](ReactionType.md) | Previous list of reaction types that were set by the user | 
**new_reaction** | [**List[ReactionType]**](ReactionType.md) | New list of reaction types that have been set by the user | 

## Example

```python
from tele_rest.models.message_reaction_updated import MessageReactionUpdated

# TODO update the JSON string below
json = "{}"
# create an instance of MessageReactionUpdated from a JSON string
message_reaction_updated_instance = MessageReactionUpdated.from_json(json)
# print the JSON string representation of the object
print(MessageReactionUpdated.to_json())

# convert the object into a dict
message_reaction_updated_dict = message_reaction_updated_instance.to_dict()
# create an instance of MessageReactionUpdated from a dict
message_reaction_updated_from_dict = MessageReactionUpdated.from_dict(message_reaction_updated_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


