# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import time
from typing import Any, cast
from typing_extensions import Literal, overload

import httpx

from ..types import prediction_run_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import required_args, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._constants import DEFAULT_MAX_RETRIES
from .._base_client import make_request_options
from ..types.prediction_run_response import PredictionRunResponse
from ..types.prediction_status_response import Error, PredictionStatusResponse
from ..types.prediction_subscribe_params import (
    EnqueuedCallback,
    QueueUpdateCallback,
)
from ..types.prediction_subscribe_response import PredictionSubscribeResponse

__all__ = ["PredictionsResource", "AsyncPredictionsResource"]


DEFAULT_POLL_INTERVAL_MS = 1000
DEFAULT_TIMEOUT_MS = 5 * 60 * 1000
CREDITS_USED_HEADER = "x-fashn-credits-used"


## Note: use the publicly exported type


class PredictionsResource(SyncAPIResource):
    @overload
    def subscribe(
        self,
        *,
        inputs: prediction_run_params.TryOnRequestInputs,
        model_name: Literal["tryon-v1.6"],
        webhook_url: str | Omit = omit,
        poll_interval: int | None = None,
        timeout: int | None = None,
        max_retries: int | None = None,
        on_enqueued: EnqueuedCallback | None = None,
        on_queue_update: QueueUpdateCallback | None = None,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        request_timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PredictionSubscribeResponse: ...

    @overload
    def subscribe(
        self,
        *,
        inputs: prediction_run_params.ProductToModelRequestInputs,
        model_name: Literal["product-to-model"],
        webhook_url: str | Omit = omit,
        poll_interval: int | None = None,
        timeout: int | None = None,
        max_retries: int | None = None,
        on_enqueued: EnqueuedCallback | None = None,
        on_queue_update: QueueUpdateCallback | None = None,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        request_timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PredictionSubscribeResponse: ...

    @overload
    def subscribe(
        self,
        *,
        inputs: prediction_run_params.FaceToModelRequestInputs,
        model_name: Literal["face-to-model"],
        webhook_url: str | Omit = omit,
        poll_interval: int | None = None,
        timeout: int | None = None,
        max_retries: int | None = None,
        on_enqueued: EnqueuedCallback | None = None,
        on_queue_update: QueueUpdateCallback | None = None,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        request_timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PredictionSubscribeResponse: ...

    @overload
    def subscribe(
        self,
        *,
        inputs: prediction_run_params.ModelCreateRequestInputs,
        model_name: Literal["model-create"],
        webhook_url: str | Omit = omit,
        poll_interval: int | None = None,
        timeout: int | None = None,
        max_retries: int | None = None,
        on_enqueued: EnqueuedCallback | None = None,
        on_queue_update: QueueUpdateCallback | None = None,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        request_timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PredictionSubscribeResponse: ...

    @overload
    def subscribe(
        self,
        *,
        inputs: prediction_run_params.ModelVariationRequestInputs,
        model_name: Literal["model-variation"],
        webhook_url: str | Omit = omit,
        poll_interval: int | None = None,
        timeout: int | None = None,
        max_retries: int | None = None,
        on_enqueued: EnqueuedCallback | None = None,
        on_queue_update: QueueUpdateCallback | None = None,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        request_timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PredictionSubscribeResponse: ...

    @overload
    def subscribe(
        self,
        *,
        inputs: prediction_run_params.ModelSwapRequestInputs,
        model_name: Literal["model-swap"],
        webhook_url: str | Omit = omit,
        poll_interval: int | None = None,
        timeout: int | None = None,
        max_retries: int | None = None,
        on_enqueued: EnqueuedCallback | None = None,
        on_queue_update: QueueUpdateCallback | None = None,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        request_timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PredictionSubscribeResponse: ...

    @overload
    def subscribe(
        self,
        *,
        inputs: prediction_run_params.ReframeRequestInputs,
        model_name: Literal["reframe"],
        webhook_url: str | Omit = omit,
        poll_interval: int | None = None,
        timeout: int | None = None,
        max_retries: int | None = None,
        on_enqueued: EnqueuedCallback | None = None,
        on_queue_update: QueueUpdateCallback | None = None,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        request_timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PredictionSubscribeResponse: ...

    @overload
    def subscribe(
        self,
        *,
        inputs: prediction_run_params.BackgroundChangeRequestInputs,
        model_name: Literal["background-change"],
        webhook_url: str | Omit = omit,
        poll_interval: int | None = None,
        timeout: int | None = None,
        max_retries: int | None = None,
        on_enqueued: EnqueuedCallback | None = None,
        on_queue_update: QueueUpdateCallback | None = None,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        request_timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PredictionSubscribeResponse: ...

    @overload
    def subscribe(
        self,
        *,
        inputs: prediction_run_params.BackgroundRemoveRequestInputs,
        model_name: Literal["background-remove"],
        webhook_url: str | Omit = omit,
        poll_interval: int | None = None,
        timeout: int | None = None,
        max_retries: int | None = None,
        on_enqueued: EnqueuedCallback | None = None,
        on_queue_update: QueueUpdateCallback | None = None,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        request_timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PredictionSubscribeResponse: ...

    def subscribe(
        self,
        *,
        inputs: prediction_run_params.TryOnRequestInputs
        | prediction_run_params.ProductToModelRequestInputs
        | prediction_run_params.FaceToModelRequestInputs
        | prediction_run_params.ModelCreateRequestInputs
        | prediction_run_params.ModelVariationRequestInputs
        | prediction_run_params.ModelSwapRequestInputs
        | prediction_run_params.ReframeRequestInputs
        | prediction_run_params.BackgroundChangeRequestInputs
        | prediction_run_params.BackgroundRemoveRequestInputs,
        model_name: Literal["tryon-v1.6"]
        | Literal["product-to-model"]
        | Literal["face-to-model"]
        | Literal["model-create"]
        | Literal["model-variation"]
        | Literal["model-swap"]
        | Literal["reframe"]
        | Literal["background-change"]
        | Literal["background-remove"],
        webhook_url: str | Omit = omit,
        poll_interval: int | None = None,
        timeout: int | None = None,
        max_retries: int | None = None,
        on_enqueued: EnqueuedCallback | None = None,
        on_queue_update: QueueUpdateCallback | None = None,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        request_timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PredictionSubscribeResponse:
        """Run a prediction and poll until completion with real-time updates.

        Combines `run` and repeated `status` polling into a single call.

        Args:
          inputs: Typed inputs matching the selected `model_name`.
          model_name: One of the supported model names; determines the `inputs` type.
          webhook_url: Optional webhook URL to receive completion notifications.
          poll_interval: Polling interval in milliseconds. Defaults to 1000ms.
          timeout: Overall subscribe timeout in milliseconds. Defaults to 300000ms.
          max_retries: Maximum retry attempts for the status HTTP request. Defaults to client default.
          on_enqueued: Callback invoked once the request ID is available.
          on_queue_update: Callback invoked on every status update.
          request_timeout: Per-request HTTP timeout for run/status calls.
        """
        # Resolve subscribe options from kwargs (TS-style defaults)
        poll_interval_ms = poll_interval if poll_interval is not None else DEFAULT_POLL_INTERVAL_MS
        subscribe_timeout_ms = (
            timeout if (timeout is not None and timeout > 0) else DEFAULT_TIMEOUT_MS
        )
        effective_max_retries = (
            max_retries if (max_retries is not None and max_retries >= 0) else DEFAULT_MAX_RETRIES
        )

        run_result: PredictionRunResponse = self.run(
            inputs=cast(Any, inputs),
            model_name=cast(Any, model_name),
            webhook_url=webhook_url,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=request_timeout,
        )

        prediction_id: str = run_result.id
        if on_enqueued:
            on_enqueued(prediction_id)

        return self._poll_status(
            prediction_id=prediction_id,
            poll_interval_ms=poll_interval_ms,
            subscribe_timeout_ms=subscribe_timeout_ms,
            max_retries=effective_max_retries,
            on_queue_update=on_queue_update,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=request_timeout,
        )

    def _poll_status(
        self,
        *,
        prediction_id: str,
        poll_interval_ms: int,
        subscribe_timeout_ms: int,
        max_retries: int,
        on_queue_update: QueueUpdateCallback | None,
        extra_headers: Headers | None,
        extra_query: Query | None,
        extra_body: Body | None,
        timeout: float | httpx.Timeout | None | NotGiven,
    ) -> PredictionSubscribeResponse:
        poll_interval_ms = poll_interval_ms if poll_interval_ms > 0 else DEFAULT_POLL_INTERVAL_MS
        deadline = time.monotonic() + (subscribe_timeout_ms / 1000) if subscribe_timeout_ms else None

        status_options = make_request_options(
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        status_options["max_retries"] = max_retries

        while True:
            raw_response = self.with_raw_response.status(
                prediction_id,
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            )
            status = raw_response.parse()

            if on_queue_update:
                on_queue_update(status)

            if status.status not in {"starting", "in_queue", "processing"}:
                terminal_status = cast(
                    Literal["completed", "failed", "canceled", "time_out"],
                    status.status,
                )
                credits_used_header = raw_response.headers.get(CREDITS_USED_HEADER)
                credits_used: int | None = None
                try:
                    if credits_used_header is not None:
                        credits_used = int(credits_used_header)
                except Exception:
                    credits_used = None

                return PredictionSubscribeResponse(
                    id=status.id,
                    status=terminal_status,
                    error=status.error,
                    output=status.output,
                    credits_used=credits_used,
                )

            if deadline and time.monotonic() >= deadline:
                timeout_status_for_callback = PredictionStatusResponse(
                    id=prediction_id,
                    status="time_out",
                    error=Error(
                        name="PollingTimeout",
                        message="Prediction polling timed out.",
                    ),
                    output=None,
                )
                if on_queue_update:
                    on_queue_update(timeout_status_for_callback)
                return PredictionSubscribeResponse(
                    id=prediction_id,
                    status="time_out",
                    error=Error(
                        name="PollingTimeout",
                        message="Prediction polling timed out.",
                    ),
                    output=None,
                )

            self._sleep(poll_interval_ms / 1000)

    @cached_property
    def with_raw_response(self) -> PredictionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/fashn-AI/fashn-python-sdk#accessing-raw-response-data-eg-headers
        """
        return PredictionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PredictionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/fashn-AI/fashn-python-sdk#with_streaming_response
        """
        return PredictionsResourceWithStreamingResponse(self)

    @overload
    def run(
        self,
        *,
        inputs: prediction_run_params.TryOnRequestInputs,
        model_name: Literal["tryon-v1.6"],
        webhook_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PredictionRunResponse:
        """Submit a prediction request for AI-powered fashion processing.

        Supports multiple
        model types including:

        - Virtual try-on (tryon-v1.6)
        - Model creation (model-create)
        - Model variation (model-variation)
        - Model swap (model-swap)
        - Product to model (product-to-model)
        - Face to model (face-to-model)
        - Background operations (background-remove, background-change)
        - Image reframing (reframe)
        - Image to video (image-to-video)

        All requests use the versioned format with model_name and inputs structure.

        Args:
          model_name: Virtual Try-On v1.6 enables realistic garment visualization using just a single
              photo of a person and a garment

          webhook_url: Optional webhook URL to receive completion notifications

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def run(
        self,
        *,
        inputs: prediction_run_params.ProductToModelRequestInputs,
        model_name: Literal["product-to-model"],
        webhook_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PredictionRunResponse:
        """Submit a prediction request for AI-powered fashion processing.

        Supports multiple
        model types including:

        - Virtual try-on (tryon-v1.6)
        - Model creation (model-create)
        - Model variation (model-variation)
        - Model swap (model-swap)
        - Product to model (product-to-model)
        - Face to model (face-to-model)
        - Background operations (background-remove, background-change)
        - Image reframing (reframe)
        - Image to video (image-to-video)

        All requests use the versioned format with model_name and inputs structure.

        Args:
          model_name: Product to Model endpoint transforms product images into people wearing those
              products. It supports dual-mode operation: standard product-to-model (generates
              new person) and try-on mode (adds product to existing person)

          webhook_url: Optional webhook URL to receive completion notifications

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def run(
        self,
        *,
        inputs: prediction_run_params.FaceToModelRequestInputs,
        model_name: Literal["face-to-model"],
        webhook_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PredictionRunResponse:
        """Submit a prediction request for AI-powered fashion processing.

        Supports multiple
        model types including:

        - Virtual try-on (tryon-v1.6)
        - Model creation (model-create)
        - Model variation (model-variation)
        - Model swap (model-swap)
        - Product to model (product-to-model)
        - Face to model (face-to-model)
        - Background operations (background-remove, background-change)
        - Image reframing (reframe)
        - Image to video (image-to-video)

        All requests use the versioned format with model_name and inputs structure.

        Args:
          model_name: Face to Model endpoint transforms face images into try-on ready upper-body
              avatars. It converts cropped headshots or selfies into full upper-body
              representations that can be used in virtual try-on applications when full-body
              photos are not available, while preserving facial identity.

          webhook_url: Optional webhook URL to receive completion notifications

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def run(
        self,
        *,
        inputs: prediction_run_params.ModelCreateRequestInputs,
        model_name: Literal["model-create"],
        webhook_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PredictionRunResponse:
        """Submit a prediction request for AI-powered fashion processing.

        Supports multiple
        model types including:

        - Virtual try-on (tryon-v1.6)
        - Model creation (model-create)
        - Model variation (model-variation)
        - Model swap (model-swap)
        - Product to model (product-to-model)
        - Face to model (face-to-model)
        - Background operations (background-remove, background-change)
        - Image reframing (reframe)
        - Image to video (image-to-video)

        All requests use the versioned format with model_name and inputs structure.

        Args:
          model_name: Model creation endpoint

          webhook_url: Optional webhook URL to receive completion notifications

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def run(
        self,
        *,
        inputs: prediction_run_params.ModelVariationRequestInputs,
        model_name: Literal["model-variation"],
        webhook_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PredictionRunResponse:
        """Submit a prediction request for AI-powered fashion processing.

        Supports multiple
        model types including:

        - Virtual try-on (tryon-v1.6)
        - Model creation (model-create)
        - Model variation (model-variation)
        - Model swap (model-swap)
        - Product to model (product-to-model)
        - Face to model (face-to-model)
        - Background operations (background-remove, background-change)
        - Image reframing (reframe)
        - Image to video (image-to-video)

        All requests use the versioned format with model_name and inputs structure.

        Args:
          model_name: Model variation endpoint for creating variations from existing model images

          webhook_url: Optional webhook URL to receive completion notifications

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def run(
        self,
        *,
        inputs: prediction_run_params.ModelSwapRequestInputs,
        model_name: Literal["model-swap"],
        webhook_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PredictionRunResponse:
        """Submit a prediction request for AI-powered fashion processing.

        Supports multiple
        model types including:

        - Virtual try-on (tryon-v1.6)
        - Model creation (model-create)
        - Model variation (model-variation)
        - Model swap (model-swap)
        - Product to model (product-to-model)
        - Face to model (face-to-model)
        - Background operations (background-remove, background-change)
        - Image reframing (reframe)
        - Image to video (image-to-video)

        All requests use the versioned format with model_name and inputs structure.

        Args:
          model_name: Model swap endpoint for transforming model identity while preserving clothing
              and pose

          webhook_url: Optional webhook URL to receive completion notifications

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def run(
        self,
        *,
        inputs: prediction_run_params.ReframeRequestInputs,
        model_name: Literal["reframe"],
        webhook_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PredictionRunResponse:
        """Submit a prediction request for AI-powered fashion processing.

        Supports multiple
        model types including:

        - Virtual try-on (tryon-v1.6)
        - Model creation (model-create)
        - Model variation (model-variation)
        - Model swap (model-swap)
        - Product to model (product-to-model)
        - Face to model (face-to-model)
        - Background operations (background-remove, background-change)
        - Image reframing (reframe)
        - Image to video (image-to-video)

        All requests use the versioned format with model_name and inputs structure.

        Args:
          model_name: Image reframing endpoint

          webhook_url: Optional webhook URL to receive completion notifications

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def run(
        self,
        *,
        inputs: prediction_run_params.BackgroundChangeRequestInputs,
        model_name: Literal["background-change"],
        webhook_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PredictionRunResponse:
        """Submit a prediction request for AI-powered fashion processing.

        Supports multiple
        model types including:

        - Virtual try-on (tryon-v1.6)
        - Model creation (model-create)
        - Model variation (model-variation)
        - Model swap (model-swap)
        - Product to model (product-to-model)
        - Face to model (face-to-model)
        - Background operations (background-remove, background-change)
        - Image reframing (reframe)
        - Image to video (image-to-video)

        All requests use the versioned format with model_name and inputs structure.

        Args:
          model_name: Background change endpoint

          webhook_url: Optional webhook URL to receive completion notifications

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def run(
        self,
        *,
        inputs: prediction_run_params.BackgroundRemoveRequestInputs,
        model_name: Literal["background-remove"],
        webhook_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PredictionRunResponse:
        """Submit a prediction request for AI-powered fashion processing.

        Supports multiple
        model types including:

        - Virtual try-on (tryon-v1.6)
        - Model creation (model-create)
        - Model variation (model-variation)
        - Model swap (model-swap)
        - Product to model (product-to-model)
        - Face to model (face-to-model)
        - Background operations (background-remove, background-change)
        - Image reframing (reframe)
        - Image to video (image-to-video)

        All requests use the versioned format with model_name and inputs structure.

        Args:
          model_name: Background removal endpoint

          webhook_url: Optional webhook URL to receive completion notifications

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def run(
        self,
        *,
        inputs: prediction_run_params.ImageToVideoRequestInputs,
        model_name: Literal["image-to-video"],
        webhook_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PredictionRunResponse:
        """Submit a prediction request for AI-powered fashion processing.

        Supports multiple
        model types including:

        - Virtual try-on (tryon-v1.6)
        - Model creation (model-create)
        - Model variation (model-variation)
        - Model swap (model-swap)
        - Product to model (product-to-model)
        - Face to model (face-to-model)
        - Background operations (background-remove, background-change)
        - Image reframing (reframe)
        - Image to video (image-to-video)

        All requests use the versioned format with model_name and inputs structure.

        Args:
          model_name: Image to Video turns a single image into a short motion clip, with tasteful
              camera work and model movements tailored for fashion.

          webhook_url: Optional webhook URL to receive completion notifications

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["inputs", "model_name"])
    def run(
        self,
        *,
        inputs: prediction_run_params.TryOnRequestInputs
        | prediction_run_params.ProductToModelRequestInputs
        | prediction_run_params.FaceToModelRequestInputs
        | prediction_run_params.ModelCreateRequestInputs
        | prediction_run_params.ModelVariationRequestInputs
        | prediction_run_params.ModelSwapRequestInputs
        | prediction_run_params.ReframeRequestInputs
        | prediction_run_params.BackgroundChangeRequestInputs
        | prediction_run_params.BackgroundRemoveRequestInputs
        | prediction_run_params.ImageToVideoRequestInputs,
        model_name: Literal["tryon-v1.6"]
        | Literal["product-to-model"]
        | Literal["face-to-model"]
        | Literal["model-create"]
        | Literal["model-variation"]
        | Literal["model-swap"]
        | Literal["reframe"]
        | Literal["background-change"]
        | Literal["background-remove"]
        | Literal["image-to-video"],
        webhook_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PredictionRunResponse:
        return self._post(
            "/v1/run",
            body=maybe_transform(
                {
                    "inputs": inputs,
                    "model_name": model_name,
                },
                prediction_run_params.PredictionRunParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"webhook_url": webhook_url}, prediction_run_params.PredictionRunParams),
            ),
            cast_to=PredictionRunResponse,
        )

    def status(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PredictionStatusResponse:
        """Poll for the status of a specific prediction using its ID.

        Use this endpoint to
        track prediction progress and retrieve results.

        **Status States:**

        - `starting` - Prediction is being initialized
        - `in_queue` - Prediction is waiting to be processed
        - `processing` - Model is actively generating your result
        - `completed` - Generation finished successfully, output available
        - `failed` - Generation failed, check error details

        **Output Availability:**

        - **CDN URLs** (default): Available for 72 hours after completion
        - **Base64 outputs** (when `return_base64: true`): Available for 60 minutes
          after completion

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/v1/status/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PredictionStatusResponse,
        )


class AsyncPredictionsResource(AsyncAPIResource):
    @overload
    async def subscribe(
        self,
        *,
        inputs: prediction_run_params.TryOnRequestInputs,
        model_name: Literal["tryon-v1.6"],
        webhook_url: str | Omit = omit,
        poll_interval: int | None = None,
        timeout: int | None = None,
        max_retries: int | None = None,
        on_enqueued: EnqueuedCallback | None = None,
        on_queue_update: QueueUpdateCallback | None = None,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        request_timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PredictionSubscribeResponse: ...

    @overload
    async def subscribe(
        self,
        *,
        inputs: prediction_run_params.ProductToModelRequestInputs,
        model_name: Literal["product-to-model"],
        webhook_url: str | Omit = omit,
        poll_interval: int | None = None,
        timeout: int | None = None,
        max_retries: int | None = None,
        on_enqueued: EnqueuedCallback | None = None,
        on_queue_update: QueueUpdateCallback | None = None,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        request_timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PredictionSubscribeResponse: ...

    @overload
    async def subscribe(
        self,
        *,
        inputs: prediction_run_params.FaceToModelRequestInputs,
        model_name: Literal["face-to-model"],
        webhook_url: str | Omit = omit,
        poll_interval: int | None = None,
        timeout: int | None = None,
        max_retries: int | None = None,
        on_enqueued: EnqueuedCallback | None = None,
        on_queue_update: QueueUpdateCallback | None = None,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        request_timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PredictionSubscribeResponse: ...

    @overload
    async def subscribe(
        self,
        *,
        inputs: prediction_run_params.ModelCreateRequestInputs,
        model_name: Literal["model-create"],
        webhook_url: str | Omit = omit,
        poll_interval: int | None = None,
        timeout: int | None = None,
        max_retries: int | None = None,
        on_enqueued: EnqueuedCallback | None = None,
        on_queue_update: QueueUpdateCallback | None = None,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        request_timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PredictionSubscribeResponse: ...

    @overload
    async def subscribe(
        self,
        *,
        inputs: prediction_run_params.ModelVariationRequestInputs,
        model_name: Literal["model-variation"],
        webhook_url: str | Omit = omit,
        poll_interval: int | None = None,
        timeout: int | None = None,
        max_retries: int | None = None,
        on_enqueued: EnqueuedCallback | None = None,
        on_queue_update: QueueUpdateCallback | None = None,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        request_timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PredictionSubscribeResponse: ...

    @overload
    async def subscribe(
        self,
        *,
        inputs: prediction_run_params.ModelSwapRequestInputs,
        model_name: Literal["model-swap"],
        webhook_url: str | Omit = omit,
        poll_interval: int | None = None,
        timeout: int | None = None,
        max_retries: int | None = None,
        on_enqueued: EnqueuedCallback | None = None,
        on_queue_update: QueueUpdateCallback | None = None,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        request_timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PredictionSubscribeResponse: ...

    @overload
    async def subscribe(
        self,
        *,
        inputs: prediction_run_params.ReframeRequestInputs,
        model_name: Literal["reframe"],
        webhook_url: str | Omit = omit,
        poll_interval: int | None = None,
        timeout: int | None = None,
        max_retries: int | None = None,
        on_enqueued: EnqueuedCallback | None = None,
        on_queue_update: QueueUpdateCallback | None = None,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        request_timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PredictionSubscribeResponse: ...

    @overload
    async def subscribe(
        self,
        *,
        inputs: prediction_run_params.BackgroundChangeRequestInputs,
        model_name: Literal["background-change"],
        webhook_url: str | Omit = omit,
        poll_interval: int | None = None,
        timeout: int | None = None,
        max_retries: int | None = None,
        on_enqueued: EnqueuedCallback | None = None,
        on_queue_update: QueueUpdateCallback | None = None,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        request_timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PredictionSubscribeResponse: ...

    @overload
    async def subscribe(
        self,
        *,
        inputs: prediction_run_params.BackgroundRemoveRequestInputs,
        model_name: Literal["background-remove"],
        webhook_url: str | Omit = omit,
        poll_interval: int | None = None,
        timeout: int | None = None,
        max_retries: int | None = None,
        on_enqueued: EnqueuedCallback | None = None,
        on_queue_update: QueueUpdateCallback | None = None,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        request_timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PredictionSubscribeResponse: ...

    async def subscribe(
        self,
        *,
        inputs: prediction_run_params.TryOnRequestInputs
        | prediction_run_params.ProductToModelRequestInputs
        | prediction_run_params.FaceToModelRequestInputs
        | prediction_run_params.ModelCreateRequestInputs
        | prediction_run_params.ModelVariationRequestInputs
        | prediction_run_params.ModelSwapRequestInputs
        | prediction_run_params.ReframeRequestInputs
        | prediction_run_params.BackgroundChangeRequestInputs
        | prediction_run_params.BackgroundRemoveRequestInputs,
        model_name: Literal["tryon-v1.6"]
        | Literal["product-to-model"]
        | Literal["face-to-model"]
        | Literal["model-create"]
        | Literal["model-variation"]
        | Literal["model-swap"]
        | Literal["reframe"]
        | Literal["background-change"]
        | Literal["background-remove"],
        webhook_url: str | Omit = omit,
        poll_interval: int | None = None,
        timeout: int | None = None,
        max_retries: int | None = None,
        on_enqueued: EnqueuedCallback | None = None,
        on_queue_update: QueueUpdateCallback | None = None,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        request_timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PredictionSubscribeResponse:
        """Run a prediction and poll until completion with real-time updates.

        Async variant combining `run` and repeated `status` polling into a single call.

        Args:
          inputs: Typed inputs matching the selected `model_name`.
          model_name: One of the supported model names; determines the `inputs` type.
          webhook_url: Optional webhook URL to receive completion notifications.
          poll_interval: Polling interval in milliseconds. Defaults to 1000ms.
          timeout: Overall subscribe timeout in milliseconds. Defaults to 300000ms.
          max_retries: Maximum retry attempts for the status HTTP request. Defaults to client default.
          on_enqueued: Callback invoked once the request ID is available.
          on_queue_update: Callback invoked on every status update.
          request_timeout: Per-request HTTP timeout for run/status calls.
        """
        poll_interval_ms = poll_interval if poll_interval is not None else DEFAULT_POLL_INTERVAL_MS
        subscribe_timeout_ms = (
            timeout if (timeout is not None and timeout > 0) else DEFAULT_TIMEOUT_MS
        )
        effective_max_retries = (
            max_retries if (max_retries is not None and max_retries >= 0) else DEFAULT_MAX_RETRIES
        )

        run_result: PredictionRunResponse = await self.run(
            inputs=cast(Any, inputs),
            model_name=cast(Any, model_name),
            webhook_url=webhook_url,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=request_timeout,
        )

        prediction_id: str = run_result.id
        if on_enqueued:
            on_enqueued(prediction_id)

        return await self._poll_status(
            prediction_id=prediction_id,
            poll_interval_ms=poll_interval_ms,
            subscribe_timeout_ms=subscribe_timeout_ms,
            max_retries=effective_max_retries,
            on_queue_update=on_queue_update,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=request_timeout,
        )

    async def _poll_status(
        self,
        *,
        prediction_id: str,
        poll_interval_ms: int,
        subscribe_timeout_ms: int,
        max_retries: int,
        on_queue_update: QueueUpdateCallback | None,
        extra_headers: Headers | None,
        extra_query: Query | None,
        extra_body: Body | None,
        timeout: float | httpx.Timeout | None | NotGiven,
    ) -> PredictionSubscribeResponse:
        poll_interval_ms = poll_interval_ms if poll_interval_ms > 0 else DEFAULT_POLL_INTERVAL_MS
        deadline = time.monotonic() + (subscribe_timeout_ms / 1000) if subscribe_timeout_ms else None

        status_options = make_request_options(
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        status_options["max_retries"] = max_retries

        while True:
            # Use raw response to access headers for credits used
            raw_response = await self.with_raw_response.status(
                prediction_id,
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            )
            status: PredictionStatusResponse = await raw_response.parse()

            if on_queue_update:
                on_queue_update(status)

            if status.status not in {"starting", "in_queue", "processing"}:
                terminal_status = cast(
                    Literal["completed", "failed", "canceled", "time_out"],
                    status.status,
                )
                credits_used_header = raw_response.headers.get(CREDITS_USED_HEADER)
                credits_used: int | None = None
                try:
                    if credits_used_header is not None:
                        credits_used = int(credits_used_header)
                except Exception:
                    credits_used = None

                return PredictionSubscribeResponse(
                    id=status.id,
                    status=terminal_status,
                    error=status.error,
                    output=status.output,
                    credits_used=credits_used,
                )

            if deadline and time.monotonic() >= deadline:
                timeout_status_for_callback = PredictionStatusResponse(
                    id=prediction_id,
                    status="time_out",
                    error=Error(
                        name="PollingTimeout",
                        message="Prediction polling timed out.",
                    ),
                    output=None,
                )
                if on_queue_update:
                    on_queue_update(timeout_status_for_callback)
                return PredictionSubscribeResponse(
                    id=prediction_id,
                    status="time_out",
                    error=Error(
                        name="PollingTimeout",
                        message="Prediction polling timed out.",
                    ),
                    output=None,
                )

            await self._sleep(poll_interval_ms / 1000)
    @cached_property
    def with_raw_response(self) -> AsyncPredictionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/fashn-AI/fashn-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncPredictionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPredictionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/fashn-AI/fashn-python-sdk#with_streaming_response
        """
        return AsyncPredictionsResourceWithStreamingResponse(self)

    @overload
    async def run(
        self,
        *,
        inputs: prediction_run_params.TryOnRequestInputs,
        model_name: Literal["tryon-v1.6"],
        webhook_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PredictionRunResponse:
        """Submit a prediction request for AI-powered fashion processing.

        Supports multiple
        model types including:

        - Virtual try-on (tryon-v1.6)
        - Model creation (model-create)
        - Model variation (model-variation)
        - Model swap (model-swap)
        - Product to model (product-to-model)
        - Face to model (face-to-model)
        - Background operations (background-remove, background-change)
        - Image reframing (reframe)
        - Image to video (image-to-video)

        All requests use the versioned format with model_name and inputs structure.

        Args:
          model_name: Virtual Try-On v1.6 enables realistic garment visualization using just a single
              photo of a person and a garment

          webhook_url: Optional webhook URL to receive completion notifications

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def run(
        self,
        *,
        inputs: prediction_run_params.ProductToModelRequestInputs,
        model_name: Literal["product-to-model"],
        webhook_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PredictionRunResponse:
        """Submit a prediction request for AI-powered fashion processing.

        Supports multiple
        model types including:

        - Virtual try-on (tryon-v1.6)
        - Model creation (model-create)
        - Model variation (model-variation)
        - Model swap (model-swap)
        - Product to model (product-to-model)
        - Face to model (face-to-model)
        - Background operations (background-remove, background-change)
        - Image reframing (reframe)
        - Image to video (image-to-video)

        All requests use the versioned format with model_name and inputs structure.

        Args:
          model_name: Product to Model endpoint transforms product images into people wearing those
              products. It supports dual-mode operation: standard product-to-model (generates
              new person) and try-on mode (adds product to existing person)

          webhook_url: Optional webhook URL to receive completion notifications

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def run(
        self,
        *,
        inputs: prediction_run_params.FaceToModelRequestInputs,
        model_name: Literal["face-to-model"],
        webhook_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PredictionRunResponse:
        """Submit a prediction request for AI-powered fashion processing.

        Supports multiple
        model types including:

        - Virtual try-on (tryon-v1.6)
        - Model creation (model-create)
        - Model variation (model-variation)
        - Model swap (model-swap)
        - Product to model (product-to-model)
        - Face to model (face-to-model)
        - Background operations (background-remove, background-change)
        - Image reframing (reframe)
        - Image to video (image-to-video)

        All requests use the versioned format with model_name and inputs structure.

        Args:
          model_name: Face to Model endpoint transforms face images into try-on ready upper-body
              avatars. It converts cropped headshots or selfies into full upper-body
              representations that can be used in virtual try-on applications when full-body
              photos are not available, while preserving facial identity.

          webhook_url: Optional webhook URL to receive completion notifications

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def run(
        self,
        *,
        inputs: prediction_run_params.ModelCreateRequestInputs,
        model_name: Literal["model-create"],
        webhook_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PredictionRunResponse:
        """Submit a prediction request for AI-powered fashion processing.

        Supports multiple
        model types including:

        - Virtual try-on (tryon-v1.6)
        - Model creation (model-create)
        - Model variation (model-variation)
        - Model swap (model-swap)
        - Product to model (product-to-model)
        - Face to model (face-to-model)
        - Background operations (background-remove, background-change)
        - Image reframing (reframe)
        - Image to video (image-to-video)

        All requests use the versioned format with model_name and inputs structure.

        Args:
          model_name: Model creation endpoint

          webhook_url: Optional webhook URL to receive completion notifications

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def run(
        self,
        *,
        inputs: prediction_run_params.ModelVariationRequestInputs,
        model_name: Literal["model-variation"],
        webhook_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PredictionRunResponse:
        """Submit a prediction request for AI-powered fashion processing.

        Supports multiple
        model types including:

        - Virtual try-on (tryon-v1.6)
        - Model creation (model-create)
        - Model variation (model-variation)
        - Model swap (model-swap)
        - Product to model (product-to-model)
        - Face to model (face-to-model)
        - Background operations (background-remove, background-change)
        - Image reframing (reframe)
        - Image to video (image-to-video)

        All requests use the versioned format with model_name and inputs structure.

        Args:
          model_name: Model variation endpoint for creating variations from existing model images

          webhook_url: Optional webhook URL to receive completion notifications

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def run(
        self,
        *,
        inputs: prediction_run_params.ModelSwapRequestInputs,
        model_name: Literal["model-swap"],
        webhook_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PredictionRunResponse:
        """Submit a prediction request for AI-powered fashion processing.

        Supports multiple
        model types including:

        - Virtual try-on (tryon-v1.6)
        - Model creation (model-create)
        - Model variation (model-variation)
        - Model swap (model-swap)
        - Product to model (product-to-model)
        - Face to model (face-to-model)
        - Background operations (background-remove, background-change)
        - Image reframing (reframe)
        - Image to video (image-to-video)

        All requests use the versioned format with model_name and inputs structure.

        Args:
          model_name: Model swap endpoint for transforming model identity while preserving clothing
              and pose

          webhook_url: Optional webhook URL to receive completion notifications

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def run(
        self,
        *,
        inputs: prediction_run_params.ReframeRequestInputs,
        model_name: Literal["reframe"],
        webhook_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PredictionRunResponse:
        """Submit a prediction request for AI-powered fashion processing.

        Supports multiple
        model types including:

        - Virtual try-on (tryon-v1.6)
        - Model creation (model-create)
        - Model variation (model-variation)
        - Model swap (model-swap)
        - Product to model (product-to-model)
        - Face to model (face-to-model)
        - Background operations (background-remove, background-change)
        - Image reframing (reframe)
        - Image to video (image-to-video)

        All requests use the versioned format with model_name and inputs structure.

        Args:
          model_name: Image reframing endpoint

          webhook_url: Optional webhook URL to receive completion notifications

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def run(
        self,
        *,
        inputs: prediction_run_params.BackgroundChangeRequestInputs,
        model_name: Literal["background-change"],
        webhook_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PredictionRunResponse:
        """Submit a prediction request for AI-powered fashion processing.

        Supports multiple
        model types including:

        - Virtual try-on (tryon-v1.6)
        - Model creation (model-create)
        - Model variation (model-variation)
        - Model swap (model-swap)
        - Product to model (product-to-model)
        - Face to model (face-to-model)
        - Background operations (background-remove, background-change)
        - Image reframing (reframe)
        - Image to video (image-to-video)

        All requests use the versioned format with model_name and inputs structure.

        Args:
          model_name: Background change endpoint

          webhook_url: Optional webhook URL to receive completion notifications

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def run(
        self,
        *,
        inputs: prediction_run_params.BackgroundRemoveRequestInputs,
        model_name: Literal["background-remove"],
        webhook_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PredictionRunResponse:
        """Submit a prediction request for AI-powered fashion processing.

        Supports multiple
        model types including:

        - Virtual try-on (tryon-v1.6)
        - Model creation (model-create)
        - Model variation (model-variation)
        - Model swap (model-swap)
        - Product to model (product-to-model)
        - Face to model (face-to-model)
        - Background operations (background-remove, background-change)
        - Image reframing (reframe)
        - Image to video (image-to-video)

        All requests use the versioned format with model_name and inputs structure.

        Args:
          model_name: Background removal endpoint

          webhook_url: Optional webhook URL to receive completion notifications

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def run(
        self,
        *,
        inputs: prediction_run_params.ImageToVideoRequestInputs,
        model_name: Literal["image-to-video"],
        webhook_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PredictionRunResponse:
        """Submit a prediction request for AI-powered fashion processing.

        Supports multiple
        model types including:

        - Virtual try-on (tryon-v1.6)
        - Model creation (model-create)
        - Model variation (model-variation)
        - Model swap (model-swap)
        - Product to model (product-to-model)
        - Face to model (face-to-model)
        - Background operations (background-remove, background-change)
        - Image reframing (reframe)
        - Image to video (image-to-video)

        All requests use the versioned format with model_name and inputs structure.

        Args:
          model_name: Image to Video turns a single image into a short motion clip, with tasteful
              camera work and model movements tailored for fashion.

          webhook_url: Optional webhook URL to receive completion notifications

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["inputs", "model_name"])
    async def run(
        self,
        *,
        inputs: prediction_run_params.TryOnRequestInputs
        | prediction_run_params.ProductToModelRequestInputs
        | prediction_run_params.FaceToModelRequestInputs
        | prediction_run_params.ModelCreateRequestInputs
        | prediction_run_params.ModelVariationRequestInputs
        | prediction_run_params.ModelSwapRequestInputs
        | prediction_run_params.ReframeRequestInputs
        | prediction_run_params.BackgroundChangeRequestInputs
        | prediction_run_params.BackgroundRemoveRequestInputs
        | prediction_run_params.ImageToVideoRequestInputs,
        model_name: Literal["tryon-v1.6"]
        | Literal["product-to-model"]
        | Literal["face-to-model"]
        | Literal["model-create"]
        | Literal["model-variation"]
        | Literal["model-swap"]
        | Literal["reframe"]
        | Literal["background-change"]
        | Literal["background-remove"]
        | Literal["image-to-video"],
        webhook_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PredictionRunResponse:
        return await self._post(
            "/v1/run",
            body=await async_maybe_transform(
                {
                    "inputs": inputs,
                    "model_name": model_name,
                },
                prediction_run_params.PredictionRunParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"webhook_url": webhook_url}, prediction_run_params.PredictionRunParams
                ),
            ),
            cast_to=PredictionRunResponse,
        )

    async def status(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PredictionStatusResponse:
        """Poll for the status of a specific prediction using its ID.

        Use this endpoint to
        track prediction progress and retrieve results.

        **Status States:**

        - `starting` - Prediction is being initialized
        - `in_queue` - Prediction is waiting to be processed
        - `processing` - Model is actively generating your result
        - `completed` - Generation finished successfully, output available
        - `failed` - Generation failed, check error details

        **Output Availability:**

        - **CDN URLs** (default): Available for 72 hours after completion
        - **Base64 outputs** (when `return_base64: true`): Available for 60 minutes
          after completion

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/v1/status/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PredictionStatusResponse,
        )


class PredictionsResourceWithRawResponse:
    def __init__(self, predictions: PredictionsResource) -> None:
        self._predictions = predictions

        self.run = to_raw_response_wrapper(
            predictions.run,
        )
        self.status = to_raw_response_wrapper(
            predictions.status,
        )


class AsyncPredictionsResourceWithRawResponse:
    def __init__(self, predictions: AsyncPredictionsResource) -> None:
        self._predictions = predictions

        self.run = async_to_raw_response_wrapper(
            predictions.run,
        )
        self.status = async_to_raw_response_wrapper(
            predictions.status,
        )


class PredictionsResourceWithStreamingResponse:
    def __init__(self, predictions: PredictionsResource) -> None:
        self._predictions = predictions

        self.run = to_streamed_response_wrapper(
            predictions.run,
        )
        self.status = to_streamed_response_wrapper(
            predictions.status,
        )


class AsyncPredictionsResourceWithStreamingResponse:
    def __init__(self, predictions: AsyncPredictionsResource) -> None:
        self._predictions = predictions

        self.run = async_to_streamed_response_wrapper(
            predictions.run,
        )
        self.status = async_to_streamed_response_wrapper(
            predictions.status,
        )
