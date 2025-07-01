# Birthdate

Describes the birthdate of a user.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**day** | **int** | Day of the user&#39;s birth; 1-31 | 
**month** | **int** | Month of the user&#39;s birth; 1-12 | 
**year** | **int** | *Optional*. Year of the user&#39;s birth | [optional] 

## Example

```python
from tele_rest.models.birthdate import Birthdate

# TODO update the JSON string below
json = "{}"
# create an instance of Birthdate from a JSON string
birthdate_instance = Birthdate.from_json(json)
# print the JSON string representation of the object
print(Birthdate.to_json())

# convert the object into a dict
birthdate_dict = birthdate_instance.to_dict()
# create an instance of Birthdate from a dict
birthdate_from_dict = Birthdate.from_dict(birthdate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


