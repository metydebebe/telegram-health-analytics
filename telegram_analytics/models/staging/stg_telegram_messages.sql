with raw as (
  select
    data as msg
  from raw.telegram_messages_raw
)

select 
  msg ->> 'id' as message_id,
  msg ->> 'message' as message_text,
  msg ->> 'date' as sent_at,
  msg -> 'peer_id' ->> 'channel_id' as channel_id,
  (msg -> 'media') is not null as has_image
from raw