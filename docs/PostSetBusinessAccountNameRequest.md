# PostSetBusinessAccountNameRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business_connection_id** | **str** | Unique identifier of the business connection | 
**first_name** | **str** | The new value of the first name for the business account; 1-64 characters | 
**last_name** | **str** | The new value of the last name for the business account; 0-64 characters | [optional] 

## Example

```python
from tele_rest.models.post_set_business_account_name_request import PostSetBusinessAccountNameRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostSetBusinessAccountNameRequest from a JSON string
post_set_business_account_name_request_instance = PostSetBusinessAccountNameRequest.from_json(json)
# print the JSON string representation of the object
print(PostSetBusinessAccountNameRequest.to_json())

# convert the object into a dict
post_set_business_account_name_request_dict = post_set_business_account_name_request_instance.to_dict()
# create an instance of PostSetBusinessAccountNameRequest from a dict
post_set_business_account_name_request_from_dict = PostSetBusinessAccountNameRequest.from_dict(post_set_business_account_name_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


