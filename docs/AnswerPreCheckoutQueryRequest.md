# AnswerPreCheckoutQueryRequest

Request parameters for answerPreCheckoutQuery

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pre_checkout_query_id** | **str** | Unique identifier for the query to be answered | 
**ok** | **bool** | Specify *True* if everything is alright (goods are available, etc.) and the bot is ready to proceed with the order. Use *False* if there are any problems. | 
**error_message** | **str** | Required if *ok* is *False*. Error message in human readable form that explains the reason for failure to proceed with the checkout (e.g. \&quot;Sorry, somebody just bought the last of our amazing black T-shirts while you were busy filling out your payment details. Please choose a different color or garment!\&quot;). Telegram will display this message to the user. | [optional] 

## Example

```python
from tele_rest.models.answer_pre_checkout_query_request import AnswerPreCheckoutQueryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AnswerPreCheckoutQueryRequest from a JSON string
answer_pre_checkout_query_request_instance = AnswerPreCheckoutQueryRequest.from_json(json)
# print the JSON string representation of the object
print(AnswerPreCheckoutQueryRequest.to_json())

# convert the object into a dict
answer_pre_checkout_query_request_dict = answer_pre_checkout_query_request_instance.to_dict()
# create an instance of AnswerPreCheckoutQueryRequest from a dict
answer_pre_checkout_query_request_from_dict = AnswerPreCheckoutQueryRequest.from_dict(answer_pre_checkout_query_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


