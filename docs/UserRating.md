# UserRating

This object describes the rating of a user based on their Telegram Star spendings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**level** | **int** | Current level of the user, indicating their reliability when purchasing digital goods and services. A higher level suggests a more trustworthy customer; a negative level is likely reason for concern. | 
**rating** | **int** | Numerical value of the user&#39;s rating; the higher the rating, the better | 
**current_level_rating** | **int** | The rating value required to get the current level | 
**next_level_rating** | **int** | *Optional*. The rating value required to get to the next level; omitted if the maximum level was reached | [optional] 

## Example

```python
from tele_rest.models.user_rating import UserRating

# TODO update the JSON string below
json = "{}"
# create an instance of UserRating from a JSON string
user_rating_instance = UserRating.from_json(json)
# print the JSON string representation of the object
print(UserRating.to_json())

# convert the object into a dict
user_rating_dict = user_rating_instance.to_dict()
# create an instance of UserRating from a dict
user_rating_from_dict = UserRating.from_dict(user_rating_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


