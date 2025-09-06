# DeclineSuggestedPostRequest

Request parameters for declineSuggestedPost

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat_id** | **int** | Unique identifier for the target direct messages chat | 
**message_id** | **int** | Identifier of a suggested post message to decline | 
**comment** | **str** | Comment for the creator of the suggested post; 0-128 characters | [optional] 

## Example

```python
from tele_rest.models.decline_suggested_post_request import DeclineSuggestedPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeclineSuggestedPostRequest from a JSON string
decline_suggested_post_request_instance = DeclineSuggestedPostRequest.from_json(json)
# print the JSON string representation of the object
print(DeclineSuggestedPostRequest.to_json())

# convert the object into a dict
decline_suggested_post_request_dict = decline_suggested_post_request_instance.to_dict()
# create an instance of DeclineSuggestedPostRequest from a dict
decline_suggested_post_request_from_dict = DeclineSuggestedPostRequest.from_dict(decline_suggested_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


