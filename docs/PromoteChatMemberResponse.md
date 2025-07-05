# PromoteChatMemberResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | **bool** |  | [default to True]

## Example

```python
from tele_rest.models.promote_chat_member_response import PromoteChatMemberResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PromoteChatMemberResponse from a JSON string
promote_chat_member_response_instance = PromoteChatMemberResponse.from_json(json)
# print the JSON string representation of the object
print(PromoteChatMemberResponse.to_json())

# convert the object into a dict
promote_chat_member_response_dict = promote_chat_member_response_instance.to_dict()
# create an instance of PromoteChatMemberResponse from a dict
promote_chat_member_response_from_dict = PromoteChatMemberResponse.from_dict(promote_chat_member_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


