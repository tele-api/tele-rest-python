# ReactionCount

Represents a reaction added to a message along with the number of times it was added.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**ReactionType**](ReactionType.md) |  | 
**total_count** | **int** | Number of times the reaction was added | 

## Example

```python
from tele_rest.models.reaction_count import ReactionCount

# TODO update the JSON string below
json = "{}"
# create an instance of ReactionCount from a JSON string
reaction_count_instance = ReactionCount.from_json(json)
# print the JSON string representation of the object
print(ReactionCount.to_json())

# convert the object into a dict
reaction_count_dict = reaction_count_instance.to_dict()
# create an instance of ReactionCount from a dict
reaction_count_from_dict = ReactionCount.from_dict(reaction_count_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


