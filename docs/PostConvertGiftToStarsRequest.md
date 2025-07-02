# PostConvertGiftToStarsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business_connection_id** | **str** | Unique identifier of the business connection | 
**owned_gift_id** | **str** | Unique identifier of the regular gift that should be converted to Telegram Stars | 

## Example

```python
from tele_rest.models.post_convert_gift_to_stars_request import PostConvertGiftToStarsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostConvertGiftToStarsRequest from a JSON string
post_convert_gift_to_stars_request_instance = PostConvertGiftToStarsRequest.from_json(json)
# print the JSON string representation of the object
print(PostConvertGiftToStarsRequest.to_json())

# convert the object into a dict
post_convert_gift_to_stars_request_dict = post_convert_gift_to_stars_request_instance.to_dict()
# create an instance of PostConvertGiftToStarsRequest from a dict
post_convert_gift_to_stars_request_from_dict = PostConvertGiftToStarsRequest.from_dict(post_convert_gift_to_stars_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


