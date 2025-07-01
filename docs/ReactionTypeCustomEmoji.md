# ReactionTypeCustomEmoji

The reaction is based on a custom emoji.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of the reaction, always “custom\\_emoji” | [default to 'custom_emoji']
**custom_emoji_id** | **str** | Custom emoji identifier | 

## Example

```python
from tele_rest.models.reaction_type_custom_emoji import ReactionTypeCustomEmoji

# TODO update the JSON string below
json = "{}"
# create an instance of ReactionTypeCustomEmoji from a JSON string
reaction_type_custom_emoji_instance = ReactionTypeCustomEmoji.from_json(json)
# print the JSON string representation of the object
print(ReactionTypeCustomEmoji.to_json())

# convert the object into a dict
reaction_type_custom_emoji_dict = reaction_type_custom_emoji_instance.to_dict()
# create an instance of ReactionTypeCustomEmoji from a dict
reaction_type_custom_emoji_from_dict = ReactionTypeCustomEmoji.from_dict(reaction_type_custom_emoji_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


