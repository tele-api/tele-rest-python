# coding: utf-8

"""
Telegram Bot API - REST API Client
The Bot API is an HTTP-based interface created for developers keen on building bots for Telegram. To learn how to create and set up a bot, please consult our Introduction to Bots and Bot FAQ.

## Metadata

- **Copyright**: Copyright (c) 2025 Qntx
- **Author**: ΣX <gitctrlx@gmail.com>
- **Version**: 9.2.0
- **Modified**: 2025-08-17T02:10:52.303427632Z[Etc/UTC]
- **Generator Version**: 7.14.0

<details>
<summary><strong>⚠️ Important Disclaimer & Limitation of Liability</strong></summary>
<br>
> **IMPORTANT**: This software is provided "as is" without any warranties, express or implied, including but not limited
> to warranties of merchantability, fitness for a particular purpose, or non-infringement. The developers, contributors,
> and licensors (collectively, "Developers") make no representations regarding the accuracy, completeness, or reliability
> of this software or its outputs.
>
> This client is not intended to provide financial, investment, tax, or legal advice. It facilitates interaction with the
> Telegram Bot API service but does not endorse or recommend any financial actions, including the purchase, sale, or holding of
> financial instruments (e.g., stocks, bonds, derivatives, cryptocurrencies). Users must consult qualified financial or
> legal professionals before making decisions based on this software's outputs.
>
> Financial markets are inherently speculative and carry significant risks. Using this software in trading, analysis, or
> other financial activities may result in substantial losses, including total loss of capital. The Developers are not
> liable for any losses or damages arising from such use. Users assume full responsibility for validating the software's
> outputs and ensuring their suitability for intended purposes.
>
> This client may rely on third-party data or services (e.g., market feeds, APIs). The Developers do not control or verify
> the accuracy of these services and are not liable for any errors, delays, or losses resulting from their use. Users must
> comply with third-party terms and conditions.
>
> Users are solely responsible for ensuring compliance with all applicable financial, tax, and regulatory requirements in
> their jurisdiction. This includes obtaining necessary licenses or approvals for trading or investment activities. The
> Developers disclaim liability for any legal consequences arising from non-compliance.
>
> To the fullest extent permitted by law, the Developers shall not be liable for any direct, indirect, incidental,
> consequential, or punitive damages arising from the use or inability to use this software, including but not limited to
> loss of profits, data, or business opportunities.

</details>
"""  # noqa: E501


import unittest

from tele_rest.models.send_voice_request import SendVoiceRequest

class TestSendVoiceRequest(unittest.TestCase):
    """SendVoiceRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SendVoiceRequest:
        """Test SendVoiceRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SendVoiceRequest`
        """
        model = SendVoiceRequest()
        if include_optional:
            return SendVoiceRequest(
                business_connection_id = '',
                chat_id = None,
                message_thread_id = 56,
                direct_messages_topic_id = 56,
                voice = '',
                caption = '',
                parse_mode = '',
                caption_entities = [
                    tele_rest.models.message_entity.MessageEntity(
                        type = 'mention', 
                        offset = 56, 
                        length = 56, 
                        url = '', 
                        user = tele_rest.models.user.User(
                            id = 56, 
                            is_bot = True, 
                            first_name = '', 
                            last_name = '', 
                            username = '', 
                            language_code = '', 
                            is_premium = True, 
                            added_to_attachment_menu = True, 
                            can_join_groups = True, 
                            can_read_all_group_messages = True, 
                            supports_inline_queries = True, 
                            can_connect_to_business = True, 
                            has_main_web_app = True, ), 
                        language = '', 
                        custom_emoji_id = '', )
                    ],
                duration = 56,
                disable_notification = True,
                protect_content = True,
                allow_paid_broadcast = True,
                message_effect_id = '',
                suggested_post_parameters = tele_rest.models.suggested_post_parameters.SuggestedPostParameters(
                    price = tele_rest.models.suggested_post_price.SuggestedPostPrice(
                        currency = 'XTR', 
                        amount = 56, ), 
                    send_date = 56, ),
                reply_parameters = tele_rest.models.reply_parameters.ReplyParameters(
                    message_id = 56, 
                    chat_id = null, 
                    allow_sending_without_reply = True, 
                    quote = '', 
                    quote_parse_mode = '', 
                    quote_entities = [
                        tele_rest.models.message_entity.MessageEntity(
                            type = 'mention', 
                            offset = 56, 
                            length = 56, 
                            url = '', 
                            user = tele_rest.models.user.User(
                                id = 56, 
                                is_bot = True, 
                                first_name = '', 
                                last_name = '', 
                                username = '', 
                                language_code = '', 
                                is_premium = True, 
                                added_to_attachment_menu = True, 
                                can_join_groups = True, 
                                can_read_all_group_messages = True, 
                                supports_inline_queries = True, 
                                can_connect_to_business = True, 
                                has_main_web_app = True, ), 
                            language = '', 
                            custom_emoji_id = '', )
                        ], 
                    quote_position = 56, 
                    checklist_task_id = 56, ),
                reply_markup = None
            )
        else:
            return SendVoiceRequest(
                chat_id = None,
                voice = '',
        )
        """

    def testSendVoiceRequest(self):
        """Test SendVoiceRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
