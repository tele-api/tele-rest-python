# DeclineSuggestedPostResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | **bool** |  | [default to True]

## Example

```python
from tele_rest.models.decline_suggested_post_response import DeclineSuggestedPostResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeclineSuggestedPostResponse from a JSON string
decline_suggested_post_response_instance = DeclineSuggestedPostResponse.from_json(json)
# print the JSON string representation of the object
print(DeclineSuggestedPostResponse.to_json())

# convert the object into a dict
decline_suggested_post_response_dict = decline_suggested_post_response_instance.to_dict()
# create an instance of DeclineSuggestedPostResponse from a dict
decline_suggested_post_response_from_dict = DeclineSuggestedPostResponse.from_dict(decline_suggested_post_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


