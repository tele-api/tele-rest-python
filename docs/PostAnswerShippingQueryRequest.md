# PostAnswerShippingQueryRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shipping_query_id** | **str** | Unique identifier for the query to be answered | 
**ok** | **bool** | Pass *True* if delivery to the specified address is possible and *False* if there are any problems (for example, if delivery to the specified address is not possible) | 
**shipping_options** | [**List[ShippingOption]**](ShippingOption.md) | Required if *ok* is *True*. A JSON-serialized array of available shipping options. | [optional] 
**error_message** | **str** | Required if *ok* is *False*. Error message in human readable form that explains why it is impossible to complete the order (e.g. “Sorry, delivery to your desired address is unavailable”). Telegram will display this message to the user. | [optional] 

## Example

```python
from tele_rest.models.post_answer_shipping_query_request import PostAnswerShippingQueryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostAnswerShippingQueryRequest from a JSON string
post_answer_shipping_query_request_instance = PostAnswerShippingQueryRequest.from_json(json)
# print the JSON string representation of the object
print(PostAnswerShippingQueryRequest.to_json())

# convert the object into a dict
post_answer_shipping_query_request_dict = post_answer_shipping_query_request_instance.to_dict()
# create an instance of PostAnswerShippingQueryRequest from a dict
post_answer_shipping_query_request_from_dict = PostAnswerShippingQueryRequest.from_dict(post_answer_shipping_query_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


