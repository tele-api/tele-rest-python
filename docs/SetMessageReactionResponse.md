# SetMessageReactionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | **bool** |  | [default to True]

## Example

```python
from tele_rest.models.set_message_reaction_response import SetMessageReactionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SetMessageReactionResponse from a JSON string
set_message_reaction_response_instance = SetMessageReactionResponse.from_json(json)
# print the JSON string representation of the object
print(SetMessageReactionResponse.to_json())

# convert the object into a dict
set_message_reaction_response_dict = set_message_reaction_response_instance.to_dict()
# create an instance of SetMessageReactionResponse from a dict
set_message_reaction_response_from_dict = SetMessageReactionResponse.from_dict(set_message_reaction_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


