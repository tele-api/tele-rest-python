# PostGetBusinessConnectionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business_connection_id** | **str** | Unique identifier of the business connection | 

## Example

```python
from tele_rest.models.post_get_business_connection_request import PostGetBusinessConnectionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostGetBusinessConnectionRequest from a JSON string
post_get_business_connection_request_instance = PostGetBusinessConnectionRequest.from_json(json)
# print the JSON string representation of the object
print(PostGetBusinessConnectionRequest.to_json())

# convert the object into a dict
post_get_business_connection_request_dict = post_get_business_connection_request_instance.to_dict()
# create an instance of PostGetBusinessConnectionRequest from a dict
post_get_business_connection_request_from_dict = PostGetBusinessConnectionRequest.from_dict(post_get_business_connection_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


