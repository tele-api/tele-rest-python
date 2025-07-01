# StarAmount

Describes an amount of Telegram Stars.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **int** | Integer amount of Telegram Stars, rounded to 0; can be negative | 
**nanostar_amount** | **int** | *Optional*. The number of 1/1000000000 shares of Telegram Stars; from -999999999 to 999999999; can be negative if and only if *amount* is non-positive | [optional] 

## Example

```python
from tele_rest.models.star_amount import StarAmount

# TODO update the JSON string below
json = "{}"
# create an instance of StarAmount from a JSON string
star_amount_instance = StarAmount.from_json(json)
# print the JSON string representation of the object
print(StarAmount.to_json())

# convert the object into a dict
star_amount_dict = star_amount_instance.to_dict()
# create an instance of StarAmount from a dict
star_amount_from_dict = StarAmount.from_dict(star_amount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


