# ApproveSuggestedPostRequest

Request parameters for approveSuggestedPost

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat_id** | **int** | Unique identifier for the target direct messages chat | 
**message_id** | **int** | Identifier of a suggested post message to approve | 
**send_date** | **int** | Point in time (Unix timestamp) when the post is expected to be published; omit if the date has already been specified when the suggested post was created. If specified, then the date must be not more than 2678400 seconds (30 days) in the future | [optional] 

## Example

```python
from tele_rest.models.approve_suggested_post_request import ApproveSuggestedPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApproveSuggestedPostRequest from a JSON string
approve_suggested_post_request_instance = ApproveSuggestedPostRequest.from_json(json)
# print the JSON string representation of the object
print(ApproveSuggestedPostRequest.to_json())

# convert the object into a dict
approve_suggested_post_request_dict = approve_suggested_post_request_instance.to_dict()
# create an instance of ApproveSuggestedPostRequest from a dict
approve_suggested_post_request_from_dict = ApproveSuggestedPostRequest.from_dict(approve_suggested_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


