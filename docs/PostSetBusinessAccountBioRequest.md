# PostSetBusinessAccountBioRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business_connection_id** | **str** | Unique identifier of the business connection | 
**bio** | **str** | The new value of the bio for the business account; 0-140 characters | [optional] 

## Example

```python
from tele_rest.models.post_set_business_account_bio_request import PostSetBusinessAccountBioRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostSetBusinessAccountBioRequest from a JSON string
post_set_business_account_bio_request_instance = PostSetBusinessAccountBioRequest.from_json(json)
# print the JSON string representation of the object
print(PostSetBusinessAccountBioRequest.to_json())

# convert the object into a dict
post_set_business_account_bio_request_dict = post_set_business_account_bio_request_instance.to_dict()
# create an instance of PostSetBusinessAccountBioRequest from a dict
post_set_business_account_bio_request_from_dict = PostSetBusinessAccountBioRequest.from_dict(post_set_business_account_bio_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


