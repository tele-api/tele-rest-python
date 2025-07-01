# PreparedInlineMessage

Describes an inline message to be sent by a user of a Mini App.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the prepared message | 
**expiration_date** | **int** | Expiration date of the prepared message, in Unix time. Expired prepared messages can no longer be used | 

## Example

```python
from tele_rest.models.prepared_inline_message import PreparedInlineMessage

# TODO update the JSON string below
json = "{}"
# create an instance of PreparedInlineMessage from a JSON string
prepared_inline_message_instance = PreparedInlineMessage.from_json(json)
# print the JSON string representation of the object
print(PreparedInlineMessage.to_json())

# convert the object into a dict
prepared_inline_message_dict = prepared_inline_message_instance.to_dict()
# create an instance of PreparedInlineMessage from a dict
prepared_inline_message_from_dict = PreparedInlineMessage.from_dict(prepared_inline_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


