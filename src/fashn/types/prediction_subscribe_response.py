# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .prediction_status_response import Error

__all__ = ["PredictionSubscribeResponse"]


class PredictionSubscribeResponse(BaseModel):
    id: str
    error: Optional[Error] = None
    status: Literal["completed", "failed", "canceled", "time_out"]
    output: Union[List[str], List[str], None] = None
    credits_used: Optional[int] = None

