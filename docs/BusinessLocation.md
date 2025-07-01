# BusinessLocation

Contains information about the location of a Telegram Business account.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | Address of the business | 
**location** | [**Location**](Location.md) |  | [optional] 

## Example

```python
from tele_rest.models.business_location import BusinessLocation

# TODO update the JSON string below
json = "{}"
# create an instance of BusinessLocation from a JSON string
business_location_instance = BusinessLocation.from_json(json)
# print the JSON string representation of the object
print(BusinessLocation.to_json())

# convert the object into a dict
business_location_dict = business_location_instance.to_dict()
# create an instance of BusinessLocation from a dict
business_location_from_dict = BusinessLocation.from_dict(business_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


