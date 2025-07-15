select *
from {{ ref('fct_messages') }}
where message_text is null
