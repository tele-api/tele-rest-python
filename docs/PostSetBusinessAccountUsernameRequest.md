# PostSetBusinessAccountUsernameRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business_connection_id** | **str** | Unique identifier of the business connection | 
**username** | **str** | The new value of the username for the business account; 0-32 characters | [optional] 

## Example

```python
from tele_rest.models.post_set_business_account_username_request import PostSetBusinessAccountUsernameRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostSetBusinessAccountUsernameRequest from a JSON string
post_set_business_account_username_request_instance = PostSetBusinessAccountUsernameRequest.from_json(json)
# print the JSON string representation of the object
print(PostSetBusinessAccountUsernameRequest.to_json())

# convert the object into a dict
post_set_business_account_username_request_dict = post_set_business_account_username_request_instance.to_dict()
# create an instance of PostSetBusinessAccountUsernameRequest from a dict
post_set_business_account_username_request_from_dict = PostSetBusinessAccountUsernameRequest.from_dict(post_set_business_account_username_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


