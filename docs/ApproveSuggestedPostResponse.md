# ApproveSuggestedPostResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | **bool** |  | [default to True]

## Example

```python
from tele_rest.models.approve_suggested_post_response import ApproveSuggestedPostResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApproveSuggestedPostResponse from a JSON string
approve_suggested_post_response_instance = ApproveSuggestedPostResponse.from_json(json)
# print the JSON string representation of the object
print(ApproveSuggestedPostResponse.to_json())

# convert the object into a dict
approve_suggested_post_response_dict = approve_suggested_post_response_instance.to_dict()
# create an instance of ApproveSuggestedPostResponse from a dict
approve_suggested_post_response_from_dict = ApproveSuggestedPostResponse.from_dict(approve_suggested_post_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


