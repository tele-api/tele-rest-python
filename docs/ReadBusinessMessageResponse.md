# ReadBusinessMessageResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | **bool** |  | [default to True]

## Example

```python
from tele_rest.models.read_business_message_response import ReadBusinessMessageResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReadBusinessMessageResponse from a JSON string
read_business_message_response_instance = ReadBusinessMessageResponse.from_json(json)
# print the JSON string representation of the object
print(ReadBusinessMessageResponse.to_json())

# convert the object into a dict
read_business_message_response_dict = read_business_message_response_instance.to_dict()
# create an instance of ReadBusinessMessageResponse from a dict
read_business_message_response_from_dict = ReadBusinessMessageResponse.from_dict(read_business_message_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


