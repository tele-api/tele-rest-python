# LocationAddress

Describes the physical address of a location.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country_code** | **str** | The two-letter ISO 3166-1 alpha-2 country code of the country where the location is located | 
**state** | **str** | *Optional*. State of the location | [optional] 
**city** | **str** | *Optional*. City of the location | [optional] 
**street** | **str** | *Optional*. Street address of the location | [optional] 

## Example

```python
from tele_rest.models.location_address import LocationAddress

# TODO update the JSON string below
json = "{}"
# create an instance of LocationAddress from a JSON string
location_address_instance = LocationAddress.from_json(json)
# print the JSON string representation of the object
print(LocationAddress.to_json())

# convert the object into a dict
location_address_dict = location_address_instance.to_dict()
# create an instance of LocationAddress from a dict
location_address_from_dict = LocationAddress.from_dict(location_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


