select
    message_id,
    channel_id,
    sent_at,
    message_text,
    has_image,
    length(message_text) as message_length
from {{ ref('stg_telegram_messages') }}