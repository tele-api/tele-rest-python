# VerifyChatResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | **bool** |  | [default to True]

## Example

```python
from tele_rest.models.verify_chat_response import VerifyChatResponse

# TODO update the JSON string below
json = "{}"
# create an instance of VerifyChatResponse from a JSON string
verify_chat_response_instance = VerifyChatResponse.from_json(json)
# print the JSON string representation of the object
print(VerifyChatResponse.to_json())

# convert the object into a dict
verify_chat_response_dict = verify_chat_response_instance.to_dict()
# create an instance of VerifyChatResponse from a dict
verify_chat_response_from_dict = VerifyChatResponse.from_dict(verify_chat_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


