# coding: utf-8

"""
Telegram Bot API - REST API Client
The Bot API is an HTTP-based interface created for developers keen on building bots for Telegram. To learn how to create and set up a bot, please consult our Introduction to Bots and Bot FAQ.

## Metadata

- **Copyright**: Copyright (c) 2025 Qntx
- **Author**: ΣX <gitctrlx@gmail.com>
- **Version**: 9.0.0
- **Modified**: 2025-07-01T14:36:24.755929598Z[Etc/UTC]
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

from tele_rest.models.create_chat_invite_link_post200_response import CreateChatInviteLinkPost200Response

class TestCreateChatInviteLinkPost200Response(unittest.TestCase):
    """CreateChatInviteLinkPost200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateChatInviteLinkPost200Response:
        """Test CreateChatInviteLinkPost200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateChatInviteLinkPost200Response`
        """
        model = CreateChatInviteLinkPost200Response()
        if include_optional:
            return CreateChatInviteLinkPost200Response(
                ok = True,
                result = tele_rest.models.chat_invite_link.ChatInviteLink(
                    invite_link = '', 
                    creator = tele_rest.models.user.User(
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
                    creates_join_request = True, 
                    is_primary = True, 
                    is_revoked = True, 
                    name = '', 
                    expire_date = 56, 
                    member_limit = 56, 
                    pending_join_request_count = 56, 
                    subscription_period = 56, 
                    subscription_price = 56, )
            )
        else:
            return CreateChatInviteLinkPost200Response(
                ok = True,
                result = tele_rest.models.chat_invite_link.ChatInviteLink(
                    invite_link = '', 
                    creator = tele_rest.models.user.User(
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
                    creates_join_request = True, 
                    is_primary = True, 
                    is_revoked = True, 
                    name = '', 
                    expire_date = 56, 
                    member_limit = 56, 
                    pending_join_request_count = 56, 
                    subscription_period = 56, 
                    subscription_price = 56, ),
        )
        """

    def testCreateChatInviteLinkPost200Response(self):
        """Test CreateChatInviteLinkPost200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
