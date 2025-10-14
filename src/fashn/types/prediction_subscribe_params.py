# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Protocol

from .prediction_status_response import PredictionStatusResponse

__all__ = ["QueueUpdateCallback", "EnqueuedCallback"]


class QueueUpdateCallback(Protocol):
    def __call__(self, status: PredictionStatusResponse, /) -> None: ...


class EnqueuedCallback(Protocol):
    def __call__(self, prediction_id: str, /) -> None: ...



