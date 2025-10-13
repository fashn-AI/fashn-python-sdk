# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Protocol
from typing_extensions import Literal, TypedDict

from .prediction_status_response import PredictionStatusResponse

__all__ = ["QueueUpdateCallback", "EnqueuedCallback", "PredictionSubscribeParams"]


class QueueUpdateCallback(Protocol):
    def __call__(self, status: PredictionStatusResponse, /) -> None: ...


class EnqueuedCallback(Protocol):
    def __call__(self, prediction_id: str, /) -> None: ...


class PredictionSubscribeParams(TypedDict, total=False):
    # Core run parameters
    inputs: dict[str, Any]
    model_name: Literal[
        "tryon-v1.6",
        "product-to-model",
        "face-to-model",
        "model-create",
        "model-variation",
        "model-swap",
        "reframe",
        "background-change",
        "background-remove",
    ]
    webhook_url: str

    # Subscribe-only options
    poll_interval: int
    timeout: int
    max_retries: int
    on_enqueued: EnqueuedCallback
    on_queue_update: QueueUpdateCallback

