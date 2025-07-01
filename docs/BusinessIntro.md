# BusinessIntro

Contains information about the start page settings of a Telegram Business account.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | *Optional*. Title text of the business intro | [optional] 
**message** | **str** | *Optional*. Message text of the business intro | [optional] 
**sticker** | [**Sticker**](Sticker.md) |  | [optional] 

## Example

```python
from tele_rest.models.business_intro import BusinessIntro

# TODO update the JSON string below
json = "{}"
# create an instance of BusinessIntro from a JSON string
business_intro_instance = BusinessIntro.from_json(json)
# print the JSON string representation of the object
print(BusinessIntro.to_json())

# convert the object into a dict
business_intro_dict = business_intro_instance.to_dict()
# create an instance of BusinessIntro from a dict
business_intro_from_dict = BusinessIntro.from_dict(business_intro_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


