from ninja import Schema
from datetime import datetime
from typing import List, Optional

class ragacaSchema(Schema):
    id: int
    name: str
    last_name: str
    image: Optional[str]  