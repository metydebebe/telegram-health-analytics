select distinct
    cast(sent_at as date) as date_day
from {{ ref('stg_telegram_messages') }}