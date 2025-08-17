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

from tele_rest.models.send_message_response import SendMessageResponse

class TestSendMessageResponse(unittest.TestCase):
    """SendMessageResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SendMessageResponse:
        """Test SendMessageResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SendMessageResponse`
        """
        model = SendMessageResponse()
        if include_optional:
            return SendMessageResponse(
                ok = True,
                result = tele_rest.models.message.Message(
                    message_id = 56, 
                    message_thread_id = 56, 
                    direct_messages_topic = tele_rest.models.direct_messages_topic.DirectMessagesTopic(
                        topic_id = 56, 
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
                            has_main_web_app = True, ), ), 
                    from = tele_rest.models.user.User(
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
                    sender_chat = tele_rest.models.chat.Chat(
                        id = 56, 
                        type = 'private', 
                        title = '', 
                        username = '', 
                        first_name = '', 
                        last_name = '', 
                        is_forum = True, 
                        is_direct_messages = True, ), 
                    sender_boost_count = 56, 
                    sender_business_bot = , 
                    date = 56, 
                    business_connection_id = '', 
                    chat = tele_rest.models.chat.Chat(
                        id = 56, 
                        type = 'private', 
                        title = '', 
                        username = '', 
                        first_name = '', 
                        last_name = '', 
                        is_forum = True, 
                        is_direct_messages = True, ), 
                    forward_origin = null, 
                    is_topic_message = True, 
                    is_automatic_forward = True, 
                    reply_to_message = tele_rest.models.message.Message(
                        message_id = 56, 
                        message_thread_id = 56, 
                        sender_boost_count = 56, 
                        date = 56, 
                        business_connection_id = '', 
                        chat = , 
                        is_topic_message = True, 
                        is_automatic_forward = True, 
                        external_reply = tele_rest.models.external_reply_info.ExternalReplyInfo(
                            origin = null, 
                            message_id = 56, 
                            link_preview_options = tele_rest.models.link_preview_options.LinkPreviewOptions(
                                is_disabled = True, 
                                url = '', 
                                prefer_small_media = True, 
                                prefer_large_media = True, 
                                show_above_text = True, ), 
                            animation = tele_rest.models.animation.Animation(
                                file_id = '', 
                                file_unique_id = '', 
                                width = 56, 
                                height = 56, 
                                duration = 56, 
                                thumbnail = tele_rest.models.photo_size.PhotoSize(
                                    file_id = '', 
                                    file_unique_id = '', 
                                    width = 56, 
                                    height = 56, 
                                    file_size = 56, ), 
                                file_name = '', 
                                mime_type = '', 
                                file_size = 56, ), 
                            audio = tele_rest.models.audio.Audio(
                                file_id = '', 
                                file_unique_id = '', 
                                duration = 56, 
                                performer = '', 
                                title = '', 
                                file_name = '', 
                                mime_type = '', 
                                file_size = 56, ), 
                            document = tele_rest.models.document.Document(
                                file_id = '', 
                                file_unique_id = '', 
                                file_name = '', 
                                mime_type = '', 
                                file_size = 56, ), 
                            paid_media = tele_rest.models.paid_media_info.PaidMediaInfo(
                                star_count = 56, 
                                paid_media = [
                                    null
                                    ], ), 
                            photo = [
                                tele_rest.models.photo_size.PhotoSize(
                                    file_id = '', 
                                    file_unique_id = '', 
                                    width = 56, 
                                    height = 56, 
                                    file_size = 56, )
                                ], 
                            sticker = tele_rest.models.sticker.Sticker(
                                file_id = '', 
                                file_unique_id = '', 
                                type = 'regular', 
                                width = 56, 
                                height = 56, 
                                is_animated = True, 
                                is_video = True, 
                                emoji = '', 
                                set_name = '', 
                                premium_animation = tele_rest.models.file.File(
                                    file_id = '', 
                                    file_unique_id = '', 
                                    file_size = 56, 
                                    file_path = '', ), 
                                mask_position = tele_rest.models.mask_position.MaskPosition(
                                    point = 'forehead', 
                                    x_shift = 1.337, 
                                    y_shift = 1.337, 
                                    scale = 1.337, ), 
                                custom_emoji_id = '', 
                                needs_repainting = True, 
                                file_size = 56, ), 
                            story = tele_rest.models.story.Story(
                                chat = , 
                                id = 56, ), 
                            video = tele_rest.models.video.Video(
                                file_id = '', 
                                file_unique_id = '', 
                                width = 56, 
                                height = 56, 
                                duration = 56, 
                                cover = [
                                    
                                    ], 
                                start_timestamp = 56, 
                                file_name = '', 
                                mime_type = '', 
                                file_size = 56, ), 
                            video_note = tele_rest.models.video_note.VideoNote(
                                file_id = '', 
                                file_unique_id = '', 
                                length = 56, 
                                duration = 56, 
                                file_size = 56, ), 
                            voice = tele_rest.models.voice.Voice(
                                file_id = '', 
                                file_unique_id = '', 
                                duration = 56, 
                                mime_type = '', 
                                file_size = 56, ), 
                            has_media_spoiler = True, 
                            checklist = tele_rest.models.checklist.Checklist(
                                title = '', 
                                title_entities = [
                                    tele_rest.models.message_entity.MessageEntity(
                                        type = 'mention', 
                                        offset = 56, 
                                        length = 56, 
                                        url = '', 
                                        language = '', 
                                        custom_emoji_id = '', )
                                    ], 
                                tasks = [
                                    tele_rest.models.checklist_task.ChecklistTask(
                                        id = 56, 
                                        text = '', 
                                        text_entities = [
                                            tele_rest.models.message_entity.MessageEntity(
                                                type = 'mention', 
                                                offset = 56, 
                                                length = 56, 
                                                url = '', 
                                                language = '', 
                                                custom_emoji_id = '', )
                                            ], 
                                        completed_by_user = , 
                                        completion_date = 56, )
                                    ], 
                                others_can_add_tasks = True, 
                                others_can_mark_tasks_as_done = True, ), 
                            contact = tele_rest.models.contact.Contact(
                                phone_number = '', 
                                first_name = '', 
                                last_name = '', 
                                user_id = 56, 
                                vcard = '', ), 
                            dice = tele_rest.models.dice.Dice(
                                emoji = '', 
                                value = 56, ), 
                            game = tele_rest.models.game.Game(
                                title = '', 
                                description = '', 
                                photo = [
                                    
                                    ], 
                                text = '', ), 
                            giveaway = tele_rest.models.giveaway.Giveaway(
                                chats = [
                                    
                                    ], 
                                winners_selection_date = 56, 
                                winner_count = 56, 
                                only_new_members = True, 
                                has_public_winners = True, 
                                prize_description = '', 
                                country_codes = [
                                    ''
                                    ], 
                                prize_star_count = 56, 
                                premium_subscription_month_count = 56, ), 
                            giveaway_winners = tele_rest.models.giveaway_winners.GiveawayWinners(
                                chat = , 
                                giveaway_message_id = 56, 
                                winners_selection_date = 56, 
                                winner_count = 56, 
                                winners = [
                                    
                                    ], 
                                additional_chat_count = 56, 
                                prize_star_count = 56, 
                                premium_subscription_month_count = 56, 
                                unclaimed_prize_count = 56, 
                                only_new_members = True, 
                                was_refunded = True, 
                                prize_description = '', ), 
                            invoice = tele_rest.models.invoice.Invoice(
                                title = '', 
                                description = '', 
                                start_parameter = '', 
                                currency = '', 
                                total_amount = 56, ), 
                            location = tele_rest.models.location.Location(
                                latitude = 1.337, 
                                longitude = 1.337, 
                                horizontal_accuracy = 1.337, 
                                live_period = 56, 
                                heading = 56, 
                                proximity_alert_radius = 56, ), 
                            poll = tele_rest.models.poll.Poll(
                                id = '', 
                                question = '0', 
                                question_entities = [
                                    
                                    ], 
                                options = [
                                    tele_rest.models.poll_option.PollOption(
                                        text = '0', 
                                        voter_count = 56, )
                                    ], 
                                total_voter_count = 56, 
                                is_closed = True, 
                                is_anonymous = True, 
                                type = 'regular', 
                                allows_multiple_answers = True, 
                                correct_option_id = 56, 
                                explanation = '', 
                                explanation_entities = [
                                    
                                    ], 
                                open_period = 56, 
                                close_date = 56, ), 
                            venue = tele_rest.models.venue.Venue(
                                location = tele_rest.models.location.Location(
                                    latitude = 1.337, 
                                    longitude = 1.337, 
                                    horizontal_accuracy = 1.337, 
                                    live_period = 56, 
                                    heading = 56, 
                                    proximity_alert_radius = 56, ), 
                                title = '', 
                                address = '', 
                                foursquare_id = '', 
                                foursquare_type = '', 
                                google_place_id = '', 
                                google_place_type = '', ), ), 
                        quote = tele_rest.models.text_quote.TextQuote(
                            text = '', 
                            entities = [
                                
                                ], 
                            position = 56, 
                            is_manual = True, ), 
                        reply_to_story = tele_rest.models.story.Story(
                            chat = , 
                            id = 56, ), 
                        reply_to_checklist_task_id = 56, 
                        via_bot = , 
                        edit_date = 56, 
                        has_protected_content = True, 
                        is_from_offline = True, 
                        is_paid_post = True, 
                        media_group_id = '', 
                        author_signature = '', 
                        paid_star_count = 56, 
                        text = '', 
                        entities = [
                            
                            ], 
                        link_preview_options = tele_rest.models.link_preview_options.LinkPreviewOptions(
                            is_disabled = True, 
                            url = '', 
                            prefer_small_media = True, 
                            prefer_large_media = True, 
                            show_above_text = True, ), 
                        suggested_post_info = tele_rest.models.suggested_post_info.SuggestedPostInfo(
                            state = 'pending', 
                            price = tele_rest.models.suggested_post_price.SuggestedPostPrice(
                                currency = 'XTR', 
                                amount = 56, ), 
                            send_date = 56, ), 
                        effect_id = '', 
                        animation = tele_rest.models.animation.Animation(
                            file_id = '', 
                            file_unique_id = '', 
                            width = 56, 
                            height = 56, 
                            duration = 56, 
                            file_name = '', 
                            mime_type = '', 
                            file_size = 56, ), 
                        audio = tele_rest.models.audio.Audio(
                            file_id = '', 
                            file_unique_id = '', 
                            duration = 56, 
                            performer = '', 
                            title = '', 
                            file_name = '', 
                            mime_type = '', 
                            file_size = 56, ), 
                        document = tele_rest.models.document.Document(
                            file_id = '', 
                            file_unique_id = '', 
                            file_name = '', 
                            mime_type = '', 
                            file_size = 56, ), 
                        paid_media = tele_rest.models.paid_media_info.PaidMediaInfo(
                            star_count = 56, 
                            paid_media = [
                                null
                                ], ), 
                        photo = [
                            
                            ], 
                        sticker = tele_rest.models.sticker.Sticker(
                            file_id = '', 
                            file_unique_id = '', 
                            type = 'regular', 
                            width = 56, 
                            height = 56, 
                            is_animated = True, 
                            is_video = True, 
                            emoji = '', 
                            set_name = '', 
                            custom_emoji_id = '', 
                            needs_repainting = True, 
                            file_size = 56, ), 
                        story = , 
                        video = tele_rest.models.video.Video(
                            file_id = '', 
                            file_unique_id = '', 
                            width = 56, 
                            height = 56, 
                            duration = 56, 
                            start_timestamp = 56, 
                            file_name = '', 
                            mime_type = '', 
                            file_size = 56, ), 
                        video_note = tele_rest.models.video_note.VideoNote(
                            file_id = '', 
                            file_unique_id = '', 
                            length = 56, 
                            duration = 56, 
                            file_size = 56, ), 
                        voice = tele_rest.models.voice.Voice(
                            file_id = '', 
                            file_unique_id = '', 
                            duration = 56, 
                            mime_type = '', 
                            file_size = 56, ), 
                        caption = '', 
                        caption_entities = [
                            
                            ], 
                        show_caption_above_media = True, 
                        has_media_spoiler = True, 
                        checklist = tele_rest.models.checklist.Checklist(
                            title = '', 
                            tasks = [
                                tele_rest.models.checklist_task.ChecklistTask(
                                    id = 56, 
                                    text = '', 
                                    completion_date = 56, )
                                ], 
                            others_can_add_tasks = True, 
                            others_can_mark_tasks_as_done = True, ), 
                        contact = tele_rest.models.contact.Contact(
                            phone_number = '', 
                            first_name = '', 
                            last_name = '', 
                            user_id = 56, 
                            vcard = '', ), 
                        dice = tele_rest.models.dice.Dice(
                            emoji = '', 
                            value = 56, ), 
                        game = tele_rest.models.game.Game(
                            title = '', 
                            description = '', 
                            photo = [
                                
                                ], 
                            text = '', ), 
                        poll = tele_rest.models.poll.Poll(
                            id = '', 
                            question = '0', 
                            options = [
                                tele_rest.models.poll_option.PollOption(
                                    text = '0', 
                                    voter_count = 56, )
                                ], 
                            total_voter_count = 56, 
                            is_closed = True, 
                            is_anonymous = True, 
                            type = 'regular', 
                            allows_multiple_answers = True, 
                            correct_option_id = 56, 
                            explanation = '', 
                            open_period = 56, 
                            close_date = 56, ), 
                        venue = tele_rest.models.venue.Venue(
                            location = , 
                            title = '', 
                            address = '', 
                            foursquare_id = '', 
                            foursquare_type = '', 
                            google_place_id = '', 
                            google_place_type = '', ), 
                        location = , 
                        new_chat_members = [
                            
                            ], 
                        left_chat_member = , 
                        new_chat_title = '', 
                        new_chat_photo = [
                            
                            ], 
                        delete_chat_photo = True, 
                        group_chat_created = True, 
                        supergroup_chat_created = True, 
                        channel_chat_created = True, 
                        message_auto_delete_timer_changed = tele_rest.models.message_auto_delete_timer_changed.MessageAutoDeleteTimerChanged(
                            message_auto_delete_time = 56, ), 
                        migrate_to_chat_id = 56, 
                        migrate_from_chat_id = 56, 
                        pinned_message = null, 
                        invoice = tele_rest.models.invoice.Invoice(
                            title = '', 
                            description = '', 
                            start_parameter = '', 
                            currency = '', 
                            total_amount = 56, ), 
                        successful_payment = tele_rest.models.successful_payment.SuccessfulPayment(
                            currency = '', 
                            total_amount = 56, 
                            invoice_payload = '', 
                            subscription_expiration_date = 56, 
                            is_recurring = True, 
                            is_first_recurring = True, 
                            shipping_option_id = '', 
                            order_info = tele_rest.models.order_info.OrderInfo(
                                name = '', 
                                phone_number = '', 
                                email = '', 
                                shipping_address = tele_rest.models.shipping_address.ShippingAddress(
                                    country_code = '', 
                                    state = '', 
                                    city = '', 
                                    street_line1 = '', 
                                    street_line2 = '', 
                                    post_code = '', ), ), 
                            telegram_payment_charge_id = '', 
                            provider_payment_charge_id = '', ), 
                        refunded_payment = tele_rest.models.refunded_payment.RefundedPayment(
                            currency = 'XTR', 
                            total_amount = 56, 
                            invoice_payload = '', 
                            telegram_payment_charge_id = '', 
                            provider_payment_charge_id = '', ), 
                        users_shared = tele_rest.models.users_shared.UsersShared(
                            request_id = 56, 
                            users = [
                                tele_rest.models.shared_user.SharedUser(
                                    user_id = 56, 
                                    first_name = '', 
                                    last_name = '', 
                                    username = '', )
                                ], ), 
                        chat_shared = tele_rest.models.chat_shared.ChatShared(
                            request_id = 56, 
                            chat_id = 56, 
                            title = '', 
                            username = '', ), 
                        gift = tele_rest.models.gift_info.GiftInfo(
                            gift = tele_rest.models.gift.Gift(
                                id = '', 
                                sticker = , 
                                star_count = 56, 
                                upgrade_star_count = 56, 
                                total_count = 56, 
                                remaining_count = 56, 
                                publisher_chat = , ), 
                            owned_gift_id = '', 
                            convert_star_count = 56, 
                            prepaid_upgrade_star_count = 56, 
                            can_be_upgraded = True, 
                            text = '', 
                            is_private = True, ), 
                        unique_gift = tele_rest.models.unique_gift_info.UniqueGiftInfo(
                            gift = tele_rest.models.unique_gift.UniqueGift(
                                base_name = '', 
                                name = '', 
                                number = 56, 
                                model = tele_rest.models.unique_gift_model.UniqueGiftModel(
                                    name = '', 
                                    sticker = , 
                                    rarity_per_mille = 56, ), 
                                symbol = tele_rest.models.unique_gift_symbol.UniqueGiftSymbol(
                                    name = '', 
                                    sticker = , 
                                    rarity_per_mille = 56, ), 
                                backdrop = tele_rest.models.unique_gift_backdrop.UniqueGiftBackdrop(
                                    name = '', 
                                    colors = tele_rest.models.unique_gift_backdrop_colors.UniqueGiftBackdropColors(
                                        center_color = 56, 
                                        edge_color = 56, 
                                        symbol_color = 56, 
                                        text_color = 56, ), 
                                    rarity_per_mille = 56, ), ), 
                            origin = 'upgrade', 
                            last_resale_star_count = 56, 
                            owned_gift_id = '', 
                            transfer_star_count = 56, 
                            next_transfer_date = 56, ), 
                        connected_website = '', 
                        write_access_allowed = tele_rest.models.write_access_allowed.WriteAccessAllowed(
                            from_request = True, 
                            web_app_name = '', 
                            from_attachment_menu = True, ), 
                        passport_data = tele_rest.models.passport_data.PassportData(
                            data = [
                                tele_rest.models.encrypted_passport_element.EncryptedPassportElement(
                                    type = 'personal_details', 
                                    phone_number = '', 
                                    email = '', 
                                    files = [
                                        tele_rest.models.passport_file.PassportFile(
                                            file_id = '', 
                                            file_unique_id = '', 
                                            file_size = 56, 
                                            file_date = 56, )
                                        ], 
                                    front_side = tele_rest.models.passport_file.PassportFile(
                                        file_id = '', 
                                        file_unique_id = '', 
                                        file_size = 56, 
                                        file_date = 56, ), 
                                    reverse_side = , 
                                    selfie = , 
                                    translation = [
                                        
                                        ], 
                                    hash = '', )
                                ], 
                            credentials = tele_rest.models.encrypted_credentials.EncryptedCredentials(
                                data = '', 
                                hash = '', 
                                secret = '', ), ), 
                        proximity_alert_triggered = tele_rest.models.proximity_alert_triggered.ProximityAlertTriggered(
                            traveler = , 
                            watcher = , 
                            distance = 56, ), 
                        boost_added = tele_rest.models.chat_boost_added.ChatBoostAdded(
                            boost_count = 56, ), 
                        chat_background_set = tele_rest.models.chat_background.ChatBackground(
                            type = null, ), 
                        checklist_tasks_done = tele_rest.models.checklist_tasks_done.ChecklistTasksDone(
                            checklist_message = , 
                            marked_as_done_task_ids = [
                                56
                                ], 
                            marked_as_not_done_task_ids = [
                                56
                                ], ), 
                        checklist_tasks_added = tele_rest.models.checklist_tasks_added.ChecklistTasksAdded(
                            tasks = [
                                
                                ], ), 
                        direct_message_price_changed = tele_rest.models.direct_message_price_changed.DirectMessagePriceChanged(
                            are_direct_messages_enabled = True, 
                            direct_message_star_count = 56, ), 
                        forum_topic_created = tele_rest.models.forum_topic_created.ForumTopicCreated(
                            name = '', 
                            icon_color = 56, 
                            icon_custom_emoji_id = '', ), 
                        forum_topic_edited = tele_rest.models.forum_topic_edited.ForumTopicEdited(
                            name = '', 
                            icon_custom_emoji_id = '', ), 
                        forum_topic_closed = null, 
                        forum_topic_reopened = null, 
                        general_forum_topic_hidden = null, 
                        general_forum_topic_unhidden = null, 
                        giveaway_created = tele_rest.models.giveaway_created.GiveawayCreated(
                            prize_star_count = 56, ), 
                        giveaway = tele_rest.models.giveaway.Giveaway(
                            chats = [
                                
                                ], 
                            winners_selection_date = 56, 
                            winner_count = 56, 
                            only_new_members = True, 
                            has_public_winners = True, 
                            prize_description = '', 
                            prize_star_count = 56, 
                            premium_subscription_month_count = 56, ), 
                        giveaway_winners = tele_rest.models.giveaway_winners.GiveawayWinners(
                            chat = , 
                            giveaway_message_id = 56, 
                            winners_selection_date = 56, 
                            winner_count = 56, 
                            winners = [
                                
                                ], 
                            additional_chat_count = 56, 
                            prize_star_count = 56, 
                            premium_subscription_month_count = 56, 
                            unclaimed_prize_count = 56, 
                            only_new_members = True, 
                            was_refunded = True, 
                            prize_description = '', ), 
                        giveaway_completed = tele_rest.models.giveaway_completed.GiveawayCompleted(
                            winner_count = 56, 
                            unclaimed_prize_count = 56, 
                            giveaway_message = , 
                            is_star_giveaway = True, ), 
                        paid_message_price_changed = tele_rest.models.paid_message_price_changed.PaidMessagePriceChanged(
                            paid_message_star_count = 56, ), 
                        suggested_post_approved = tele_rest.models.suggested_post_approved.SuggestedPostApproved(
                            suggested_post_message = , 
                            send_date = 56, ), 
                        suggested_post_approval_failed = tele_rest.models.suggested_post_approval_failed.SuggestedPostApprovalFailed(
                            price = tele_rest.models.suggested_post_price.SuggestedPostPrice(
                                currency = 'XTR', 
                                amount = 56, ), ), 
                        suggested_post_declined = tele_rest.models.suggested_post_declined.SuggestedPostDeclined(
                            comment = '', ), 
                        suggested_post_paid = tele_rest.models.suggested_post_paid.SuggestedPostPaid(
                            currency = 'XTR', 
                            amount = 56, 
                            star_amount = tele_rest.models.star_amount.StarAmount(
                                amount = 56, 
                                nanostar_amount = 56, ), ), 
                        suggested_post_refunded = tele_rest.models.suggested_post_refunded.SuggestedPostRefunded(
                            reason = 'post_deleted', ), 
                        video_chat_scheduled = tele_rest.models.video_chat_scheduled.VideoChatScheduled(
                            start_date = 56, ), 
                        video_chat_started = null, 
                        video_chat_ended = tele_rest.models.video_chat_ended.VideoChatEnded(
                            duration = 56, ), 
                        video_chat_participants_invited = tele_rest.models.video_chat_participants_invited.VideoChatParticipantsInvited(
                            users = [
                                
                                ], ), 
                        web_app_data = tele_rest.models.web_app_data.WebAppData(
                            data = '', 
                            button_text = '', ), 
                        reply_markup = tele_rest.models.inline_keyboard_markup.InlineKeyboardMarkup(
                            inline_keyboard = [
                                [
                                    tele_rest.models.inline_keyboard_button.InlineKeyboardButton(
                                        text = '', 
                                        url = '', 
                                        callback_data = '', 
                                        web_app = tele_rest.models.web_app_info.WebAppInfo(
                                            url = '', ), 
                                        login_url = tele_rest.models.login_url.LoginUrl(
                                            url = '', 
                                            forward_text = '', 
                                            bot_username = '', 
                                            request_write_access = True, ), 
                                        switch_inline_query = '', 
                                        switch_inline_query_current_chat = '', 
                                        switch_inline_query_chosen_chat = tele_rest.models.switch_inline_query_chosen_chat.SwitchInlineQueryChosenChat(
                                            query = '', 
                                            allow_user_chats = True, 
                                            allow_bot_chats = True, 
                                            allow_group_chats = True, 
                                            allow_channel_chats = True, ), 
                                        copy_text = tele_rest.models.copy_text_button.CopyTextButton(
                                            text = '0', ), 
                                        callback_game = null, 
                                        pay = True, )
                                    ]
                                ], ), ), 
                    external_reply = tele_rest.models.external_reply_info.ExternalReplyInfo(
                        origin = null, 
                        message_id = 56, 
                        has_media_spoiler = True, ), 
                    quote = tele_rest.models.text_quote.TextQuote(
                        text = '', 
                        position = 56, 
                        is_manual = True, ), 
                    reply_to_story = , 
                    reply_to_checklist_task_id = 56, 
                    via_bot = , 
                    edit_date = 56, 
                    has_protected_content = True, 
                    is_from_offline = True, 
                    is_paid_post = True, 
                    media_group_id = '', 
                    author_signature = '', 
                    paid_star_count = 56, 
                    text = '', 
                    entities = [
                        
                        ], 
                    link_preview_options = , 
                    suggested_post_info = tele_rest.models.suggested_post_info.SuggestedPostInfo(
                        state = 'pending', 
                        send_date = 56, ), 
                    effect_id = '', 
                    animation = , 
                    audio = , 
                    document = , 
                    paid_media = , 
                    photo = , 
                    sticker = , 
                    story = , 
                    video = , 
                    video_note = , 
                    voice = , 
                    caption = '', 
                    caption_entities = [
                        
                        ], 
                    show_caption_above_media = True, 
                    has_media_spoiler = True, 
                    checklist = , 
                    contact = , 
                    dice = , 
                    game = , 
                    poll = , 
                    venue = , 
                    location = , 
                    new_chat_members = [
                        
                        ], 
                    left_chat_member = , 
                    new_chat_title = '', 
                    new_chat_photo = [
                        
                        ], 
                    delete_chat_photo = True, 
                    group_chat_created = True, 
                    supergroup_chat_created = True, 
                    channel_chat_created = True, 
                    message_auto_delete_timer_changed = tele_rest.models.message_auto_delete_timer_changed.MessageAutoDeleteTimerChanged(
                        message_auto_delete_time = 56, ), 
                    migrate_to_chat_id = 56, 
                    migrate_from_chat_id = 56, 
                    pinned_message = null, 
                    invoice = , 
                    successful_payment = tele_rest.models.successful_payment.SuccessfulPayment(
                        currency = '', 
                        total_amount = 56, 
                        invoice_payload = '', 
                        subscription_expiration_date = 56, 
                        is_recurring = True, 
                        is_first_recurring = True, 
                        shipping_option_id = '', 
                        telegram_payment_charge_id = '', 
                        provider_payment_charge_id = '', ), 
                    refunded_payment = tele_rest.models.refunded_payment.RefundedPayment(
                        currency = 'XTR', 
                        total_amount = 56, 
                        invoice_payload = '', 
                        telegram_payment_charge_id = '', 
                        provider_payment_charge_id = '', ), 
                    users_shared = tele_rest.models.users_shared.UsersShared(
                        request_id = 56, 
                        users = [
                            tele_rest.models.shared_user.SharedUser(
                                user_id = 56, 
                                first_name = '', 
                                last_name = '', 
                                username = '', )
                            ], ), 
                    chat_shared = tele_rest.models.chat_shared.ChatShared(
                        request_id = 56, 
                        chat_id = 56, 
                        title = '', 
                        username = '', ), 
                    gift = tele_rest.models.gift_info.GiftInfo(
                        gift = tele_rest.models.gift.Gift(
                            id = '', 
                            sticker = , 
                            star_count = 56, 
                            upgrade_star_count = 56, 
                            total_count = 56, 
                            remaining_count = 56, ), 
                        owned_gift_id = '', 
                        convert_star_count = 56, 
                        prepaid_upgrade_star_count = 56, 
                        can_be_upgraded = True, 
                        text = '', 
                        is_private = True, ), 
                    unique_gift = tele_rest.models.unique_gift_info.UniqueGiftInfo(
                        gift = tele_rest.models.unique_gift.UniqueGift(
                            base_name = '', 
                            name = '', 
                            number = 56, 
                            model = tele_rest.models.unique_gift_model.UniqueGiftModel(
                                name = '', 
                                sticker = , 
                                rarity_per_mille = 56, ), 
                            symbol = tele_rest.models.unique_gift_symbol.UniqueGiftSymbol(
                                name = '', 
                                sticker = , 
                                rarity_per_mille = 56, ), 
                            backdrop = tele_rest.models.unique_gift_backdrop.UniqueGiftBackdrop(
                                name = '', 
                                colors = tele_rest.models.unique_gift_backdrop_colors.UniqueGiftBackdropColors(
                                    center_color = 56, 
                                    edge_color = 56, 
                                    symbol_color = 56, 
                                    text_color = 56, ), 
                                rarity_per_mille = 56, ), ), 
                        origin = 'upgrade', 
                        last_resale_star_count = 56, 
                        owned_gift_id = '', 
                        transfer_star_count = 56, 
                        next_transfer_date = 56, ), 
                    connected_website = '', 
                    write_access_allowed = tele_rest.models.write_access_allowed.WriteAccessAllowed(
                        from_request = True, 
                        web_app_name = '', 
                        from_attachment_menu = True, ), 
                    passport_data = tele_rest.models.passport_data.PassportData(
                        data = [
                            tele_rest.models.encrypted_passport_element.EncryptedPassportElement(
                                type = 'personal_details', 
                                phone_number = '', 
                                email = '', 
                                hash = '', )
                            ], 
                        credentials = tele_rest.models.encrypted_credentials.EncryptedCredentials(
                            data = '', 
                            hash = '', 
                            secret = '', ), ), 
                    proximity_alert_triggered = tele_rest.models.proximity_alert_triggered.ProximityAlertTriggered(
                        traveler = , 
                        watcher = , 
                        distance = 56, ), 
                    boost_added = tele_rest.models.chat_boost_added.ChatBoostAdded(
                        boost_count = 56, ), 
                    chat_background_set = tele_rest.models.chat_background.ChatBackground(
                        type = null, ), 
                    checklist_tasks_done = tele_rest.models.checklist_tasks_done.ChecklistTasksDone(), 
                    checklist_tasks_added = tele_rest.models.checklist_tasks_added.ChecklistTasksAdded(
                        tasks = [
                            
                            ], ), 
                    direct_message_price_changed = tele_rest.models.direct_message_price_changed.DirectMessagePriceChanged(
                        are_direct_messages_enabled = True, 
                        direct_message_star_count = 56, ), 
                    forum_topic_created = tele_rest.models.forum_topic_created.ForumTopicCreated(
                        name = '', 
                        icon_color = 56, 
                        icon_custom_emoji_id = '', ), 
                    forum_topic_edited = tele_rest.models.forum_topic_edited.ForumTopicEdited(
                        name = '', 
                        icon_custom_emoji_id = '', ), 
                    forum_topic_closed = null, 
                    forum_topic_reopened = null, 
                    general_forum_topic_hidden = null, 
                    general_forum_topic_unhidden = null, 
                    giveaway_created = tele_rest.models.giveaway_created.GiveawayCreated(
                        prize_star_count = 56, ), 
                    giveaway = , 
                    giveaway_winners = , 
                    giveaway_completed = tele_rest.models.giveaway_completed.GiveawayCompleted(
                        winner_count = 56, 
                        unclaimed_prize_count = 56, 
                        is_star_giveaway = True, ), 
                    paid_message_price_changed = tele_rest.models.paid_message_price_changed.PaidMessagePriceChanged(
                        paid_message_star_count = 56, ), 
                    suggested_post_approved = tele_rest.models.suggested_post_approved.SuggestedPostApproved(
                        send_date = 56, ), 
                    suggested_post_approval_failed = tele_rest.models.suggested_post_approval_failed.SuggestedPostApprovalFailed(
                        price = , ), 
                    suggested_post_declined = tele_rest.models.suggested_post_declined.SuggestedPostDeclined(
                        comment = '', ), 
                    suggested_post_paid = tele_rest.models.suggested_post_paid.SuggestedPostPaid(
                        currency = 'XTR', 
                        amount = 56, ), 
                    suggested_post_refunded = tele_rest.models.suggested_post_refunded.SuggestedPostRefunded(
                        reason = 'post_deleted', ), 
                    video_chat_scheduled = tele_rest.models.video_chat_scheduled.VideoChatScheduled(
                        start_date = 56, ), 
                    video_chat_started = null, 
                    video_chat_ended = tele_rest.models.video_chat_ended.VideoChatEnded(
                        duration = 56, ), 
                    video_chat_participants_invited = tele_rest.models.video_chat_participants_invited.VideoChatParticipantsInvited(
                        users = [
                            
                            ], ), 
                    web_app_data = tele_rest.models.web_app_data.WebAppData(
                        data = '', 
                        button_text = '', ), 
                    reply_markup = tele_rest.models.inline_keyboard_markup.InlineKeyboardMarkup(
                        inline_keyboard = [
                            [
                                tele_rest.models.inline_keyboard_button.InlineKeyboardButton(
                                    text = '', 
                                    url = '', 
                                    callback_data = '', 
                                    switch_inline_query = '', 
                                    switch_inline_query_current_chat = '', 
                                    callback_game = null, 
                                    pay = True, )
                                ]
                            ], ), )
            )
        else:
            return SendMessageResponse(
                ok = True,
                result = tele_rest.models.message.Message(
                    message_id = 56, 
                    message_thread_id = 56, 
                    direct_messages_topic = tele_rest.models.direct_messages_topic.DirectMessagesTopic(
                        topic_id = 56, 
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
                            has_main_web_app = True, ), ), 
                    from = tele_rest.models.user.User(
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
                    sender_chat = tele_rest.models.chat.Chat(
                        id = 56, 
                        type = 'private', 
                        title = '', 
                        username = '', 
                        first_name = '', 
                        last_name = '', 
                        is_forum = True, 
                        is_direct_messages = True, ), 
                    sender_boost_count = 56, 
                    sender_business_bot = , 
                    date = 56, 
                    business_connection_id = '', 
                    chat = tele_rest.models.chat.Chat(
                        id = 56, 
                        type = 'private', 
                        title = '', 
                        username = '', 
                        first_name = '', 
                        last_name = '', 
                        is_forum = True, 
                        is_direct_messages = True, ), 
                    forward_origin = null, 
                    is_topic_message = True, 
                    is_automatic_forward = True, 
                    reply_to_message = tele_rest.models.message.Message(
                        message_id = 56, 
                        message_thread_id = 56, 
                        sender_boost_count = 56, 
                        date = 56, 
                        business_connection_id = '', 
                        chat = , 
                        is_topic_message = True, 
                        is_automatic_forward = True, 
                        external_reply = tele_rest.models.external_reply_info.ExternalReplyInfo(
                            origin = null, 
                            message_id = 56, 
                            link_preview_options = tele_rest.models.link_preview_options.LinkPreviewOptions(
                                is_disabled = True, 
                                url = '', 
                                prefer_small_media = True, 
                                prefer_large_media = True, 
                                show_above_text = True, ), 
                            animation = tele_rest.models.animation.Animation(
                                file_id = '', 
                                file_unique_id = '', 
                                width = 56, 
                                height = 56, 
                                duration = 56, 
                                thumbnail = tele_rest.models.photo_size.PhotoSize(
                                    file_id = '', 
                                    file_unique_id = '', 
                                    width = 56, 
                                    height = 56, 
                                    file_size = 56, ), 
                                file_name = '', 
                                mime_type = '', 
                                file_size = 56, ), 
                            audio = tele_rest.models.audio.Audio(
                                file_id = '', 
                                file_unique_id = '', 
                                duration = 56, 
                                performer = '', 
                                title = '', 
                                file_name = '', 
                                mime_type = '', 
                                file_size = 56, ), 
                            document = tele_rest.models.document.Document(
                                file_id = '', 
                                file_unique_id = '', 
                                file_name = '', 
                                mime_type = '', 
                                file_size = 56, ), 
                            paid_media = tele_rest.models.paid_media_info.PaidMediaInfo(
                                star_count = 56, 
                                paid_media = [
                                    null
                                    ], ), 
                            photo = [
                                tele_rest.models.photo_size.PhotoSize(
                                    file_id = '', 
                                    file_unique_id = '', 
                                    width = 56, 
                                    height = 56, 
                                    file_size = 56, )
                                ], 
                            sticker = tele_rest.models.sticker.Sticker(
                                file_id = '', 
                                file_unique_id = '', 
                                type = 'regular', 
                                width = 56, 
                                height = 56, 
                                is_animated = True, 
                                is_video = True, 
                                emoji = '', 
                                set_name = '', 
                                premium_animation = tele_rest.models.file.File(
                                    file_id = '', 
                                    file_unique_id = '', 
                                    file_size = 56, 
                                    file_path = '', ), 
                                mask_position = tele_rest.models.mask_position.MaskPosition(
                                    point = 'forehead', 
                                    x_shift = 1.337, 
                                    y_shift = 1.337, 
                                    scale = 1.337, ), 
                                custom_emoji_id = '', 
                                needs_repainting = True, 
                                file_size = 56, ), 
                            story = tele_rest.models.story.Story(
                                chat = , 
                                id = 56, ), 
                            video = tele_rest.models.video.Video(
                                file_id = '', 
                                file_unique_id = '', 
                                width = 56, 
                                height = 56, 
                                duration = 56, 
                                cover = [
                                    
                                    ], 
                                start_timestamp = 56, 
                                file_name = '', 
                                mime_type = '', 
                                file_size = 56, ), 
                            video_note = tele_rest.models.video_note.VideoNote(
                                file_id = '', 
                                file_unique_id = '', 
                                length = 56, 
                                duration = 56, 
                                file_size = 56, ), 
                            voice = tele_rest.models.voice.Voice(
                                file_id = '', 
                                file_unique_id = '', 
                                duration = 56, 
                                mime_type = '', 
                                file_size = 56, ), 
                            has_media_spoiler = True, 
                            checklist = tele_rest.models.checklist.Checklist(
                                title = '', 
                                title_entities = [
                                    tele_rest.models.message_entity.MessageEntity(
                                        type = 'mention', 
                                        offset = 56, 
                                        length = 56, 
                                        url = '', 
                                        language = '', 
                                        custom_emoji_id = '', )
                                    ], 
                                tasks = [
                                    tele_rest.models.checklist_task.ChecklistTask(
                                        id = 56, 
                                        text = '', 
                                        text_entities = [
                                            tele_rest.models.message_entity.MessageEntity(
                                                type = 'mention', 
                                                offset = 56, 
                                                length = 56, 
                                                url = '', 
                                                language = '', 
                                                custom_emoji_id = '', )
                                            ], 
                                        completed_by_user = , 
                                        completion_date = 56, )
                                    ], 
                                others_can_add_tasks = True, 
                                others_can_mark_tasks_as_done = True, ), 
                            contact = tele_rest.models.contact.Contact(
                                phone_number = '', 
                                first_name = '', 
                                last_name = '', 
                                user_id = 56, 
                                vcard = '', ), 
                            dice = tele_rest.models.dice.Dice(
                                emoji = '', 
                                value = 56, ), 
                            game = tele_rest.models.game.Game(
                                title = '', 
                                description = '', 
                                photo = [
                                    
                                    ], 
                                text = '', ), 
                            giveaway = tele_rest.models.giveaway.Giveaway(
                                chats = [
                                    
                                    ], 
                                winners_selection_date = 56, 
                                winner_count = 56, 
                                only_new_members = True, 
                                has_public_winners = True, 
                                prize_description = '', 
                                country_codes = [
                                    ''
                                    ], 
                                prize_star_count = 56, 
                                premium_subscription_month_count = 56, ), 
                            giveaway_winners = tele_rest.models.giveaway_winners.GiveawayWinners(
                                chat = , 
                                giveaway_message_id = 56, 
                                winners_selection_date = 56, 
                                winner_count = 56, 
                                winners = [
                                    
                                    ], 
                                additional_chat_count = 56, 
                                prize_star_count = 56, 
                                premium_subscription_month_count = 56, 
                                unclaimed_prize_count = 56, 
                                only_new_members = True, 
                                was_refunded = True, 
                                prize_description = '', ), 
                            invoice = tele_rest.models.invoice.Invoice(
                                title = '', 
                                description = '', 
                                start_parameter = '', 
                                currency = '', 
                                total_amount = 56, ), 
                            location = tele_rest.models.location.Location(
                                latitude = 1.337, 
                                longitude = 1.337, 
                                horizontal_accuracy = 1.337, 
                                live_period = 56, 
                                heading = 56, 
                                proximity_alert_radius = 56, ), 
                            poll = tele_rest.models.poll.Poll(
                                id = '', 
                                question = '0', 
                                question_entities = [
                                    
                                    ], 
                                options = [
                                    tele_rest.models.poll_option.PollOption(
                                        text = '0', 
                                        voter_count = 56, )
                                    ], 
                                total_voter_count = 56, 
                                is_closed = True, 
                                is_anonymous = True, 
                                type = 'regular', 
                                allows_multiple_answers = True, 
                                correct_option_id = 56, 
                                explanation = '', 
                                explanation_entities = [
                                    
                                    ], 
                                open_period = 56, 
                                close_date = 56, ), 
                            venue = tele_rest.models.venue.Venue(
                                location = tele_rest.models.location.Location(
                                    latitude = 1.337, 
                                    longitude = 1.337, 
                                    horizontal_accuracy = 1.337, 
                                    live_period = 56, 
                                    heading = 56, 
                                    proximity_alert_radius = 56, ), 
                                title = '', 
                                address = '', 
                                foursquare_id = '', 
                                foursquare_type = '', 
                                google_place_id = '', 
                                google_place_type = '', ), ), 
                        quote = tele_rest.models.text_quote.TextQuote(
                            text = '', 
                            entities = [
                                
                                ], 
                            position = 56, 
                            is_manual = True, ), 
                        reply_to_story = tele_rest.models.story.Story(
                            chat = , 
                            id = 56, ), 
                        reply_to_checklist_task_id = 56, 
                        via_bot = , 
                        edit_date = 56, 
                        has_protected_content = True, 
                        is_from_offline = True, 
                        is_paid_post = True, 
                        media_group_id = '', 
                        author_signature = '', 
                        paid_star_count = 56, 
                        text = '', 
                        entities = [
                            
                            ], 
                        link_preview_options = tele_rest.models.link_preview_options.LinkPreviewOptions(
                            is_disabled = True, 
                            url = '', 
                            prefer_small_media = True, 
                            prefer_large_media = True, 
                            show_above_text = True, ), 
                        suggested_post_info = tele_rest.models.suggested_post_info.SuggestedPostInfo(
                            state = 'pending', 
                            price = tele_rest.models.suggested_post_price.SuggestedPostPrice(
                                currency = 'XTR', 
                                amount = 56, ), 
                            send_date = 56, ), 
                        effect_id = '', 
                        animation = tele_rest.models.animation.Animation(
                            file_id = '', 
                            file_unique_id = '', 
                            width = 56, 
                            height = 56, 
                            duration = 56, 
                            file_name = '', 
                            mime_type = '', 
                            file_size = 56, ), 
                        audio = tele_rest.models.audio.Audio(
                            file_id = '', 
                            file_unique_id = '', 
                            duration = 56, 
                            performer = '', 
                            title = '', 
                            file_name = '', 
                            mime_type = '', 
                            file_size = 56, ), 
                        document = tele_rest.models.document.Document(
                            file_id = '', 
                            file_unique_id = '', 
                            file_name = '', 
                            mime_type = '', 
                            file_size = 56, ), 
                        paid_media = tele_rest.models.paid_media_info.PaidMediaInfo(
                            star_count = 56, 
                            paid_media = [
                                null
                                ], ), 
                        photo = [
                            
                            ], 
                        sticker = tele_rest.models.sticker.Sticker(
                            file_id = '', 
                            file_unique_id = '', 
                            type = 'regular', 
                            width = 56, 
                            height = 56, 
                            is_animated = True, 
                            is_video = True, 
                            emoji = '', 
                            set_name = '', 
                            custom_emoji_id = '', 
                            needs_repainting = True, 
                            file_size = 56, ), 
                        story = , 
                        video = tele_rest.models.video.Video(
                            file_id = '', 
                            file_unique_id = '', 
                            width = 56, 
                            height = 56, 
                            duration = 56, 
                            start_timestamp = 56, 
                            file_name = '', 
                            mime_type = '', 
                            file_size = 56, ), 
                        video_note = tele_rest.models.video_note.VideoNote(
                            file_id = '', 
                            file_unique_id = '', 
                            length = 56, 
                            duration = 56, 
                            file_size = 56, ), 
                        voice = tele_rest.models.voice.Voice(
                            file_id = '', 
                            file_unique_id = '', 
                            duration = 56, 
                            mime_type = '', 
                            file_size = 56, ), 
                        caption = '', 
                        caption_entities = [
                            
                            ], 
                        show_caption_above_media = True, 
                        has_media_spoiler = True, 
                        checklist = tele_rest.models.checklist.Checklist(
                            title = '', 
                            tasks = [
                                tele_rest.models.checklist_task.ChecklistTask(
                                    id = 56, 
                                    text = '', 
                                    completion_date = 56, )
                                ], 
                            others_can_add_tasks = True, 
                            others_can_mark_tasks_as_done = True, ), 
                        contact = tele_rest.models.contact.Contact(
                            phone_number = '', 
                            first_name = '', 
                            last_name = '', 
                            user_id = 56, 
                            vcard = '', ), 
                        dice = tele_rest.models.dice.Dice(
                            emoji = '', 
                            value = 56, ), 
                        game = tele_rest.models.game.Game(
                            title = '', 
                            description = '', 
                            photo = [
                                
                                ], 
                            text = '', ), 
                        poll = tele_rest.models.poll.Poll(
                            id = '', 
                            question = '0', 
                            options = [
                                tele_rest.models.poll_option.PollOption(
                                    text = '0', 
                                    voter_count = 56, )
                                ], 
                            total_voter_count = 56, 
                            is_closed = True, 
                            is_anonymous = True, 
                            type = 'regular', 
                            allows_multiple_answers = True, 
                            correct_option_id = 56, 
                            explanation = '', 
                            open_period = 56, 
                            close_date = 56, ), 
                        venue = tele_rest.models.venue.Venue(
                            location = , 
                            title = '', 
                            address = '', 
                            foursquare_id = '', 
                            foursquare_type = '', 
                            google_place_id = '', 
                            google_place_type = '', ), 
                        location = , 
                        new_chat_members = [
                            
                            ], 
                        left_chat_member = , 
                        new_chat_title = '', 
                        new_chat_photo = [
                            
                            ], 
                        delete_chat_photo = True, 
                        group_chat_created = True, 
                        supergroup_chat_created = True, 
                        channel_chat_created = True, 
                        message_auto_delete_timer_changed = tele_rest.models.message_auto_delete_timer_changed.MessageAutoDeleteTimerChanged(
                            message_auto_delete_time = 56, ), 
                        migrate_to_chat_id = 56, 
                        migrate_from_chat_id = 56, 
                        pinned_message = null, 
                        invoice = tele_rest.models.invoice.Invoice(
                            title = '', 
                            description = '', 
                            start_parameter = '', 
                            currency = '', 
                            total_amount = 56, ), 
                        successful_payment = tele_rest.models.successful_payment.SuccessfulPayment(
                            currency = '', 
                            total_amount = 56, 
                            invoice_payload = '', 
                            subscription_expiration_date = 56, 
                            is_recurring = True, 
                            is_first_recurring = True, 
                            shipping_option_id = '', 
                            order_info = tele_rest.models.order_info.OrderInfo(
                                name = '', 
                                phone_number = '', 
                                email = '', 
                                shipping_address = tele_rest.models.shipping_address.ShippingAddress(
                                    country_code = '', 
                                    state = '', 
                                    city = '', 
                                    street_line1 = '', 
                                    street_line2 = '', 
                                    post_code = '', ), ), 
                            telegram_payment_charge_id = '', 
                            provider_payment_charge_id = '', ), 
                        refunded_payment = tele_rest.models.refunded_payment.RefundedPayment(
                            currency = 'XTR', 
                            total_amount = 56, 
                            invoice_payload = '', 
                            telegram_payment_charge_id = '', 
                            provider_payment_charge_id = '', ), 
                        users_shared = tele_rest.models.users_shared.UsersShared(
                            request_id = 56, 
                            users = [
                                tele_rest.models.shared_user.SharedUser(
                                    user_id = 56, 
                                    first_name = '', 
                                    last_name = '', 
                                    username = '', )
                                ], ), 
                        chat_shared = tele_rest.models.chat_shared.ChatShared(
                            request_id = 56, 
                            chat_id = 56, 
                            title = '', 
                            username = '', ), 
                        gift = tele_rest.models.gift_info.GiftInfo(
                            gift = tele_rest.models.gift.Gift(
                                id = '', 
                                sticker = , 
                                star_count = 56, 
                                upgrade_star_count = 56, 
                                total_count = 56, 
                                remaining_count = 56, 
                                publisher_chat = , ), 
                            owned_gift_id = '', 
                            convert_star_count = 56, 
                            prepaid_upgrade_star_count = 56, 
                            can_be_upgraded = True, 
                            text = '', 
                            is_private = True, ), 
                        unique_gift = tele_rest.models.unique_gift_info.UniqueGiftInfo(
                            gift = tele_rest.models.unique_gift.UniqueGift(
                                base_name = '', 
                                name = '', 
                                number = 56, 
                                model = tele_rest.models.unique_gift_model.UniqueGiftModel(
                                    name = '', 
                                    sticker = , 
                                    rarity_per_mille = 56, ), 
                                symbol = tele_rest.models.unique_gift_symbol.UniqueGiftSymbol(
                                    name = '', 
                                    sticker = , 
                                    rarity_per_mille = 56, ), 
                                backdrop = tele_rest.models.unique_gift_backdrop.UniqueGiftBackdrop(
                                    name = '', 
                                    colors = tele_rest.models.unique_gift_backdrop_colors.UniqueGiftBackdropColors(
                                        center_color = 56, 
                                        edge_color = 56, 
                                        symbol_color = 56, 
                                        text_color = 56, ), 
                                    rarity_per_mille = 56, ), ), 
                            origin = 'upgrade', 
                            last_resale_star_count = 56, 
                            owned_gift_id = '', 
                            transfer_star_count = 56, 
                            next_transfer_date = 56, ), 
                        connected_website = '', 
                        write_access_allowed = tele_rest.models.write_access_allowed.WriteAccessAllowed(
                            from_request = True, 
                            web_app_name = '', 
                            from_attachment_menu = True, ), 
                        passport_data = tele_rest.models.passport_data.PassportData(
                            data = [
                                tele_rest.models.encrypted_passport_element.EncryptedPassportElement(
                                    type = 'personal_details', 
                                    phone_number = '', 
                                    email = '', 
                                    files = [
                                        tele_rest.models.passport_file.PassportFile(
                                            file_id = '', 
                                            file_unique_id = '', 
                                            file_size = 56, 
                                            file_date = 56, )
                                        ], 
                                    front_side = tele_rest.models.passport_file.PassportFile(
                                        file_id = '', 
                                        file_unique_id = '', 
                                        file_size = 56, 
                                        file_date = 56, ), 
                                    reverse_side = , 
                                    selfie = , 
                                    translation = [
                                        
                                        ], 
                                    hash = '', )
                                ], 
                            credentials = tele_rest.models.encrypted_credentials.EncryptedCredentials(
                                data = '', 
                                hash = '', 
                                secret = '', ), ), 
                        proximity_alert_triggered = tele_rest.models.proximity_alert_triggered.ProximityAlertTriggered(
                            traveler = , 
                            watcher = , 
                            distance = 56, ), 
                        boost_added = tele_rest.models.chat_boost_added.ChatBoostAdded(
                            boost_count = 56, ), 
                        chat_background_set = tele_rest.models.chat_background.ChatBackground(
                            type = null, ), 
                        checklist_tasks_done = tele_rest.models.checklist_tasks_done.ChecklistTasksDone(
                            checklist_message = , 
                            marked_as_done_task_ids = [
                                56
                                ], 
                            marked_as_not_done_task_ids = [
                                56
                                ], ), 
                        checklist_tasks_added = tele_rest.models.checklist_tasks_added.ChecklistTasksAdded(
                            tasks = [
                                
                                ], ), 
                        direct_message_price_changed = tele_rest.models.direct_message_price_changed.DirectMessagePriceChanged(
                            are_direct_messages_enabled = True, 
                            direct_message_star_count = 56, ), 
                        forum_topic_created = tele_rest.models.forum_topic_created.ForumTopicCreated(
                            name = '', 
                            icon_color = 56, 
                            icon_custom_emoji_id = '', ), 
                        forum_topic_edited = tele_rest.models.forum_topic_edited.ForumTopicEdited(
                            name = '', 
                            icon_custom_emoji_id = '', ), 
                        forum_topic_closed = null, 
                        forum_topic_reopened = null, 
                        general_forum_topic_hidden = null, 
                        general_forum_topic_unhidden = null, 
                        giveaway_created = tele_rest.models.giveaway_created.GiveawayCreated(
                            prize_star_count = 56, ), 
                        giveaway = tele_rest.models.giveaway.Giveaway(
                            chats = [
                                
                                ], 
                            winners_selection_date = 56, 
                            winner_count = 56, 
                            only_new_members = True, 
                            has_public_winners = True, 
                            prize_description = '', 
                            prize_star_count = 56, 
                            premium_subscription_month_count = 56, ), 
                        giveaway_winners = tele_rest.models.giveaway_winners.GiveawayWinners(
                            chat = , 
                            giveaway_message_id = 56, 
                            winners_selection_date = 56, 
                            winner_count = 56, 
                            winners = [
                                
                                ], 
                            additional_chat_count = 56, 
                            prize_star_count = 56, 
                            premium_subscription_month_count = 56, 
                            unclaimed_prize_count = 56, 
                            only_new_members = True, 
                            was_refunded = True, 
                            prize_description = '', ), 
                        giveaway_completed = tele_rest.models.giveaway_completed.GiveawayCompleted(
                            winner_count = 56, 
                            unclaimed_prize_count = 56, 
                            giveaway_message = , 
                            is_star_giveaway = True, ), 
                        paid_message_price_changed = tele_rest.models.paid_message_price_changed.PaidMessagePriceChanged(
                            paid_message_star_count = 56, ), 
                        suggested_post_approved = tele_rest.models.suggested_post_approved.SuggestedPostApproved(
                            suggested_post_message = , 
                            send_date = 56, ), 
                        suggested_post_approval_failed = tele_rest.models.suggested_post_approval_failed.SuggestedPostApprovalFailed(
                            price = tele_rest.models.suggested_post_price.SuggestedPostPrice(
                                currency = 'XTR', 
                                amount = 56, ), ), 
                        suggested_post_declined = tele_rest.models.suggested_post_declined.SuggestedPostDeclined(
                            comment = '', ), 
                        suggested_post_paid = tele_rest.models.suggested_post_paid.SuggestedPostPaid(
                            currency = 'XTR', 
                            amount = 56, 
                            star_amount = tele_rest.models.star_amount.StarAmount(
                                amount = 56, 
                                nanostar_amount = 56, ), ), 
                        suggested_post_refunded = tele_rest.models.suggested_post_refunded.SuggestedPostRefunded(
                            reason = 'post_deleted', ), 
                        video_chat_scheduled = tele_rest.models.video_chat_scheduled.VideoChatScheduled(
                            start_date = 56, ), 
                        video_chat_started = null, 
                        video_chat_ended = tele_rest.models.video_chat_ended.VideoChatEnded(
                            duration = 56, ), 
                        video_chat_participants_invited = tele_rest.models.video_chat_participants_invited.VideoChatParticipantsInvited(
                            users = [
                                
                                ], ), 
                        web_app_data = tele_rest.models.web_app_data.WebAppData(
                            data = '', 
                            button_text = '', ), 
                        reply_markup = tele_rest.models.inline_keyboard_markup.InlineKeyboardMarkup(
                            inline_keyboard = [
                                [
                                    tele_rest.models.inline_keyboard_button.InlineKeyboardButton(
                                        text = '', 
                                        url = '', 
                                        callback_data = '', 
                                        web_app = tele_rest.models.web_app_info.WebAppInfo(
                                            url = '', ), 
                                        login_url = tele_rest.models.login_url.LoginUrl(
                                            url = '', 
                                            forward_text = '', 
                                            bot_username = '', 
                                            request_write_access = True, ), 
                                        switch_inline_query = '', 
                                        switch_inline_query_current_chat = '', 
                                        switch_inline_query_chosen_chat = tele_rest.models.switch_inline_query_chosen_chat.SwitchInlineQueryChosenChat(
                                            query = '', 
                                            allow_user_chats = True, 
                                            allow_bot_chats = True, 
                                            allow_group_chats = True, 
                                            allow_channel_chats = True, ), 
                                        copy_text = tele_rest.models.copy_text_button.CopyTextButton(
                                            text = '0', ), 
                                        callback_game = null, 
                                        pay = True, )
                                    ]
                                ], ), ), 
                    external_reply = tele_rest.models.external_reply_info.ExternalReplyInfo(
                        origin = null, 
                        message_id = 56, 
                        has_media_spoiler = True, ), 
                    quote = tele_rest.models.text_quote.TextQuote(
                        text = '', 
                        position = 56, 
                        is_manual = True, ), 
                    reply_to_story = , 
                    reply_to_checklist_task_id = 56, 
                    via_bot = , 
                    edit_date = 56, 
                    has_protected_content = True, 
                    is_from_offline = True, 
                    is_paid_post = True, 
                    media_group_id = '', 
                    author_signature = '', 
                    paid_star_count = 56, 
                    text = '', 
                    entities = [
                        
                        ], 
                    link_preview_options = , 
                    suggested_post_info = tele_rest.models.suggested_post_info.SuggestedPostInfo(
                        state = 'pending', 
                        send_date = 56, ), 
                    effect_id = '', 
                    animation = , 
                    audio = , 
                    document = , 
                    paid_media = , 
                    photo = , 
                    sticker = , 
                    story = , 
                    video = , 
                    video_note = , 
                    voice = , 
                    caption = '', 
                    caption_entities = [
                        
                        ], 
                    show_caption_above_media = True, 
                    has_media_spoiler = True, 
                    checklist = , 
                    contact = , 
                    dice = , 
                    game = , 
                    poll = , 
                    venue = , 
                    location = , 
                    new_chat_members = [
                        
                        ], 
                    left_chat_member = , 
                    new_chat_title = '', 
                    new_chat_photo = [
                        
                        ], 
                    delete_chat_photo = True, 
                    group_chat_created = True, 
                    supergroup_chat_created = True, 
                    channel_chat_created = True, 
                    message_auto_delete_timer_changed = tele_rest.models.message_auto_delete_timer_changed.MessageAutoDeleteTimerChanged(
                        message_auto_delete_time = 56, ), 
                    migrate_to_chat_id = 56, 
                    migrate_from_chat_id = 56, 
                    pinned_message = null, 
                    invoice = , 
                    successful_payment = tele_rest.models.successful_payment.SuccessfulPayment(
                        currency = '', 
                        total_amount = 56, 
                        invoice_payload = '', 
                        subscription_expiration_date = 56, 
                        is_recurring = True, 
                        is_first_recurring = True, 
                        shipping_option_id = '', 
                        telegram_payment_charge_id = '', 
                        provider_payment_charge_id = '', ), 
                    refunded_payment = tele_rest.models.refunded_payment.RefundedPayment(
                        currency = 'XTR', 
                        total_amount = 56, 
                        invoice_payload = '', 
                        telegram_payment_charge_id = '', 
                        provider_payment_charge_id = '', ), 
                    users_shared = tele_rest.models.users_shared.UsersShared(
                        request_id = 56, 
                        users = [
                            tele_rest.models.shared_user.SharedUser(
                                user_id = 56, 
                                first_name = '', 
                                last_name = '', 
                                username = '', )
                            ], ), 
                    chat_shared = tele_rest.models.chat_shared.ChatShared(
                        request_id = 56, 
                        chat_id = 56, 
                        title = '', 
                        username = '', ), 
                    gift = tele_rest.models.gift_info.GiftInfo(
                        gift = tele_rest.models.gift.Gift(
                            id = '', 
                            sticker = , 
                            star_count = 56, 
                            upgrade_star_count = 56, 
                            total_count = 56, 
                            remaining_count = 56, ), 
                        owned_gift_id = '', 
                        convert_star_count = 56, 
                        prepaid_upgrade_star_count = 56, 
                        can_be_upgraded = True, 
                        text = '', 
                        is_private = True, ), 
                    unique_gift = tele_rest.models.unique_gift_info.UniqueGiftInfo(
                        gift = tele_rest.models.unique_gift.UniqueGift(
                            base_name = '', 
                            name = '', 
                            number = 56, 
                            model = tele_rest.models.unique_gift_model.UniqueGiftModel(
                                name = '', 
                                sticker = , 
                                rarity_per_mille = 56, ), 
                            symbol = tele_rest.models.unique_gift_symbol.UniqueGiftSymbol(
                                name = '', 
                                sticker = , 
                                rarity_per_mille = 56, ), 
                            backdrop = tele_rest.models.unique_gift_backdrop.UniqueGiftBackdrop(
                                name = '', 
                                colors = tele_rest.models.unique_gift_backdrop_colors.UniqueGiftBackdropColors(
                                    center_color = 56, 
                                    edge_color = 56, 
                                    symbol_color = 56, 
                                    text_color = 56, ), 
                                rarity_per_mille = 56, ), ), 
                        origin = 'upgrade', 
                        last_resale_star_count = 56, 
                        owned_gift_id = '', 
                        transfer_star_count = 56, 
                        next_transfer_date = 56, ), 
                    connected_website = '', 
                    write_access_allowed = tele_rest.models.write_access_allowed.WriteAccessAllowed(
                        from_request = True, 
                        web_app_name = '', 
                        from_attachment_menu = True, ), 
                    passport_data = tele_rest.models.passport_data.PassportData(
                        data = [
                            tele_rest.models.encrypted_passport_element.EncryptedPassportElement(
                                type = 'personal_details', 
                                phone_number = '', 
                                email = '', 
                                hash = '', )
                            ], 
                        credentials = tele_rest.models.encrypted_credentials.EncryptedCredentials(
                            data = '', 
                            hash = '', 
                            secret = '', ), ), 
                    proximity_alert_triggered = tele_rest.models.proximity_alert_triggered.ProximityAlertTriggered(
                        traveler = , 
                        watcher = , 
                        distance = 56, ), 
                    boost_added = tele_rest.models.chat_boost_added.ChatBoostAdded(
                        boost_count = 56, ), 
                    chat_background_set = tele_rest.models.chat_background.ChatBackground(
                        type = null, ), 
                    checklist_tasks_done = tele_rest.models.checklist_tasks_done.ChecklistTasksDone(), 
                    checklist_tasks_added = tele_rest.models.checklist_tasks_added.ChecklistTasksAdded(
                        tasks = [
                            
                            ], ), 
                    direct_message_price_changed = tele_rest.models.direct_message_price_changed.DirectMessagePriceChanged(
                        are_direct_messages_enabled = True, 
                        direct_message_star_count = 56, ), 
                    forum_topic_created = tele_rest.models.forum_topic_created.ForumTopicCreated(
                        name = '', 
                        icon_color = 56, 
                        icon_custom_emoji_id = '', ), 
                    forum_topic_edited = tele_rest.models.forum_topic_edited.ForumTopicEdited(
                        name = '', 
                        icon_custom_emoji_id = '', ), 
                    forum_topic_closed = null, 
                    forum_topic_reopened = null, 
                    general_forum_topic_hidden = null, 
                    general_forum_topic_unhidden = null, 
                    giveaway_created = tele_rest.models.giveaway_created.GiveawayCreated(
                        prize_star_count = 56, ), 
                    giveaway = , 
                    giveaway_winners = , 
                    giveaway_completed = tele_rest.models.giveaway_completed.GiveawayCompleted(
                        winner_count = 56, 
                        unclaimed_prize_count = 56, 
                        is_star_giveaway = True, ), 
                    paid_message_price_changed = tele_rest.models.paid_message_price_changed.PaidMessagePriceChanged(
                        paid_message_star_count = 56, ), 
                    suggested_post_approved = tele_rest.models.suggested_post_approved.SuggestedPostApproved(
                        send_date = 56, ), 
                    suggested_post_approval_failed = tele_rest.models.suggested_post_approval_failed.SuggestedPostApprovalFailed(
                        price = , ), 
                    suggested_post_declined = tele_rest.models.suggested_post_declined.SuggestedPostDeclined(
                        comment = '', ), 
                    suggested_post_paid = tele_rest.models.suggested_post_paid.SuggestedPostPaid(
                        currency = 'XTR', 
                        amount = 56, ), 
                    suggested_post_refunded = tele_rest.models.suggested_post_refunded.SuggestedPostRefunded(
                        reason = 'post_deleted', ), 
                    video_chat_scheduled = tele_rest.models.video_chat_scheduled.VideoChatScheduled(
                        start_date = 56, ), 
                    video_chat_started = null, 
                    video_chat_ended = tele_rest.models.video_chat_ended.VideoChatEnded(
                        duration = 56, ), 
                    video_chat_participants_invited = tele_rest.models.video_chat_participants_invited.VideoChatParticipantsInvited(
                        users = [
                            
                            ], ), 
                    web_app_data = tele_rest.models.web_app_data.WebAppData(
                        data = '', 
                        button_text = '', ), 
                    reply_markup = tele_rest.models.inline_keyboard_markup.InlineKeyboardMarkup(
                        inline_keyboard = [
                            [
                                tele_rest.models.inline_keyboard_button.InlineKeyboardButton(
                                    text = '', 
                                    url = '', 
                                    callback_data = '', 
                                    switch_inline_query = '', 
                                    switch_inline_query_current_chat = '', 
                                    callback_game = null, 
                                    pay = True, )
                                ]
                            ], ), ),
        )
        """

    def testSendMessageResponse(self):
        """Test SendMessageResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
