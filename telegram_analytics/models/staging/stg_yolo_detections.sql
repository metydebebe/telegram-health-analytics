select
  image_path,
  class_id,
  confidence
from {{ source('raw', 'raw_yolo_detections') }}
