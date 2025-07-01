# BusinessOpeningHoursInterval

Describes an interval of time during which a business is open.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**opening_minute** | **int** | The minute&#39;s sequence number in a week, starting on Monday, marking the start of the time interval during which the business is open; 0 - 7 \\* 24 \\* 60 | 
**closing_minute** | **int** | The minute&#39;s sequence number in a week, starting on Monday, marking the end of the time interval during which the business is open; 0 - 8 \\* 24 \\* 60 | 

## Example

```python
from tele_rest.models.business_opening_hours_interval import BusinessOpeningHoursInterval

# TODO update the JSON string below
json = "{}"
# create an instance of BusinessOpeningHoursInterval from a JSON string
business_opening_hours_interval_instance = BusinessOpeningHoursInterval.from_json(json)
# print the JSON string representation of the object
print(BusinessOpeningHoursInterval.to_json())

# convert the object into a dict
business_opening_hours_interval_dict = business_opening_hours_interval_instance.to_dict()
# create an instance of BusinessOpeningHoursInterval from a dict
business_opening_hours_interval_from_dict = BusinessOpeningHoursInterval.from_dict(business_opening_hours_interval_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


