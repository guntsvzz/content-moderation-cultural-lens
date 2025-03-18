from enum import Enum
from typing import Optional
from pydantic import BaseModel, ValidationError

class AdContent(BaseModel):
    Title: str
    # Scenario: str
    # Country: str
    Storyboard: str
    Ad_Description: str
    # social_bias: Optional[str] = None
    # hate_speech: Optional[str] = None
    # culture: Optional[str] = None