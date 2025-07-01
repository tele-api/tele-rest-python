# SetBusinessAccountBioPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business_connection_id** | **str** | Unique identifier of the business connection | 
**bio** | **str** | The new value of the bio for the business account; 0-140 characters | [optional] 

## Example

```python
from tele_rest.models.set_business_account_bio_post_request import SetBusinessAccountBioPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetBusinessAccountBioPostRequest from a JSON string
set_business_account_bio_post_request_instance = SetBusinessAccountBioPostRequest.from_json(json)
# print the JSON string representation of the object
print(SetBusinessAccountBioPostRequest.to_json())

# convert the object into a dict
set_business_account_bio_post_request_dict = set_business_account_bio_post_request_instance.to_dict()
# create an instance of SetBusinessAccountBioPostRequest from a dict
set_business_account_bio_post_request_from_dict = SetBusinessAccountBioPostRequest.from_dict(set_business_account_bio_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


