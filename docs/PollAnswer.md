# PollAnswer

This object represents an answer of a user in a non-anonymous poll.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**poll_id** | **str** | Unique poll identifier | 
**voter_chat** | [**Chat**](Chat.md) |  | [optional] 
**user** | [**User**](User.md) |  | [optional] 
**option_ids** | **List[int]** | 0-based identifiers of chosen answer options. May be empty if the vote was retracted. | 

## Example

```python
from tele_rest.models.poll_answer import PollAnswer

# TODO update the JSON string below
json = "{}"
# create an instance of PollAnswer from a JSON string
poll_answer_instance = PollAnswer.from_json(json)
# print the JSON string representation of the object
print(PollAnswer.to_json())

# convert the object into a dict
poll_answer_dict = poll_answer_instance.to_dict()
# create an instance of PollAnswer from a dict
poll_answer_from_dict = PollAnswer.from_dict(poll_answer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


