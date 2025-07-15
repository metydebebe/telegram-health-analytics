select
  detections.image_path,
  detections.class_id,
  detections.confidence,
  messages.message_id
from {{ ref('stg_yolo_detections') }} as detections
left join {{ ref('fct_messages') }} as messages
  on detections.image_path like '%' || messages.message_id || '%'
