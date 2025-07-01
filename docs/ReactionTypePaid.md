# ReactionTypePaid

The reaction is paid.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of the reaction, always “paid” | [default to 'paid']

## Example

```python
from tele_rest.models.reaction_type_paid import ReactionTypePaid

# TODO update the JSON string below
json = "{}"
# create an instance of ReactionTypePaid from a JSON string
reaction_type_paid_instance = ReactionTypePaid.from_json(json)
# print the JSON string representation of the object
print(ReactionTypePaid.to_json())

# convert the object into a dict
reaction_type_paid_dict = reaction_type_paid_instance.to_dict()
# create an instance of ReactionTypePaid from a dict
reaction_type_paid_from_dict = ReactionTypePaid.from_dict(reaction_type_paid_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


