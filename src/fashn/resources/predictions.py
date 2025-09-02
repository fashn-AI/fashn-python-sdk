# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, overload

import httpx

from ..types import prediction_run_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import required_args, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.prediction_run_response import PredictionRunResponse
from ..types.prediction_status_response import PredictionStatusResponse

__all__ = ["PredictionsResource", "AsyncPredictionsResource"]


class PredictionsResource(SyncAPIResource):
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
        webhook_url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PredictionRunResponse:
        """Submit a prediction request for AI-powered fashion processing.

        Supports multiple
        model types including:

        - Virtual try-on (tryon-v1.6)
        - Model creation (model-create)
        - Model variation (model-variation)
        - Model swap (model-swap)
        - Product to model (product-to-model)
        - Background operations (background-remove, background-change)
        - Image reframing (reframe)

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
        webhook_url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PredictionRunResponse:
        """Submit a prediction request for AI-powered fashion processing.

        Supports multiple
        model types including:

        - Virtual try-on (tryon-v1.6)
        - Model creation (model-create)
        - Model variation (model-variation)
        - Model swap (model-swap)
        - Product to model (product-to-model)
        - Background operations (background-remove, background-change)
        - Image reframing (reframe)

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
        inputs: prediction_run_params.ModelCreateRequestInputs,
        model_name: Literal["model-create"],
        webhook_url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PredictionRunResponse:
        """Submit a prediction request for AI-powered fashion processing.

        Supports multiple
        model types including:

        - Virtual try-on (tryon-v1.6)
        - Model creation (model-create)
        - Model variation (model-variation)
        - Model swap (model-swap)
        - Product to model (product-to-model)
        - Background operations (background-remove, background-change)
        - Image reframing (reframe)

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
        webhook_url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PredictionRunResponse:
        """Submit a prediction request for AI-powered fashion processing.

        Supports multiple
        model types including:

        - Virtual try-on (tryon-v1.6)
        - Model creation (model-create)
        - Model variation (model-variation)
        - Model swap (model-swap)
        - Product to model (product-to-model)
        - Background operations (background-remove, background-change)
        - Image reframing (reframe)

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
        webhook_url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PredictionRunResponse:
        """Submit a prediction request for AI-powered fashion processing.

        Supports multiple
        model types including:

        - Virtual try-on (tryon-v1.6)
        - Model creation (model-create)
        - Model variation (model-variation)
        - Model swap (model-swap)
        - Product to model (product-to-model)
        - Background operations (background-remove, background-change)
        - Image reframing (reframe)

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
        webhook_url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PredictionRunResponse:
        """Submit a prediction request for AI-powered fashion processing.

        Supports multiple
        model types including:

        - Virtual try-on (tryon-v1.6)
        - Model creation (model-create)
        - Model variation (model-variation)
        - Model swap (model-swap)
        - Product to model (product-to-model)
        - Background operations (background-remove, background-change)
        - Image reframing (reframe)

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
        webhook_url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PredictionRunResponse:
        """Submit a prediction request for AI-powered fashion processing.

        Supports multiple
        model types including:

        - Virtual try-on (tryon-v1.6)
        - Model creation (model-create)
        - Model variation (model-variation)
        - Model swap (model-swap)
        - Product to model (product-to-model)
        - Background operations (background-remove, background-change)
        - Image reframing (reframe)

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
        webhook_url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PredictionRunResponse:
        """Submit a prediction request for AI-powered fashion processing.

        Supports multiple
        model types including:

        - Virtual try-on (tryon-v1.6)
        - Model creation (model-create)
        - Model variation (model-variation)
        - Model swap (model-swap)
        - Product to model (product-to-model)
        - Background operations (background-remove, background-change)
        - Image reframing (reframe)

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

    @required_args(["inputs", "model_name"])
    def run(
        self,
        *,
        inputs: prediction_run_params.TryOnRequestInputs
        | prediction_run_params.ProductToModelRequestInputs
        | prediction_run_params.ModelCreateRequestInputs
        | prediction_run_params.ModelVariationRequestInputs
        | prediction_run_params.ModelSwapRequestInputs
        | prediction_run_params.ReframeRequestInputs
        | prediction_run_params.BackgroundChangeRequestInputs
        | prediction_run_params.BackgroundRemoveRequestInputs,
        model_name: Literal["tryon-v1.6"]
        | Literal["product-to-model"]
        | Literal["model-create"]
        | Literal["model-variation"]
        | Literal["model-swap"]
        | Literal["reframe"]
        | Literal["background-change"]
        | Literal["background-remove"],
        webhook_url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
        webhook_url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PredictionRunResponse:
        """Submit a prediction request for AI-powered fashion processing.

        Supports multiple
        model types including:

        - Virtual try-on (tryon-v1.6)
        - Model creation (model-create)
        - Model variation (model-variation)
        - Model swap (model-swap)
        - Product to model (product-to-model)
        - Background operations (background-remove, background-change)
        - Image reframing (reframe)

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
        webhook_url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PredictionRunResponse:
        """Submit a prediction request for AI-powered fashion processing.

        Supports multiple
        model types including:

        - Virtual try-on (tryon-v1.6)
        - Model creation (model-create)
        - Model variation (model-variation)
        - Model swap (model-swap)
        - Product to model (product-to-model)
        - Background operations (background-remove, background-change)
        - Image reframing (reframe)

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
        inputs: prediction_run_params.ModelCreateRequestInputs,
        model_name: Literal["model-create"],
        webhook_url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PredictionRunResponse:
        """Submit a prediction request for AI-powered fashion processing.

        Supports multiple
        model types including:

        - Virtual try-on (tryon-v1.6)
        - Model creation (model-create)
        - Model variation (model-variation)
        - Model swap (model-swap)
        - Product to model (product-to-model)
        - Background operations (background-remove, background-change)
        - Image reframing (reframe)

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
        webhook_url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PredictionRunResponse:
        """Submit a prediction request for AI-powered fashion processing.

        Supports multiple
        model types including:

        - Virtual try-on (tryon-v1.6)
        - Model creation (model-create)
        - Model variation (model-variation)
        - Model swap (model-swap)
        - Product to model (product-to-model)
        - Background operations (background-remove, background-change)
        - Image reframing (reframe)

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
        webhook_url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PredictionRunResponse:
        """Submit a prediction request for AI-powered fashion processing.

        Supports multiple
        model types including:

        - Virtual try-on (tryon-v1.6)
        - Model creation (model-create)
        - Model variation (model-variation)
        - Model swap (model-swap)
        - Product to model (product-to-model)
        - Background operations (background-remove, background-change)
        - Image reframing (reframe)

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
        webhook_url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PredictionRunResponse:
        """Submit a prediction request for AI-powered fashion processing.

        Supports multiple
        model types including:

        - Virtual try-on (tryon-v1.6)
        - Model creation (model-create)
        - Model variation (model-variation)
        - Model swap (model-swap)
        - Product to model (product-to-model)
        - Background operations (background-remove, background-change)
        - Image reframing (reframe)

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
        webhook_url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PredictionRunResponse:
        """Submit a prediction request for AI-powered fashion processing.

        Supports multiple
        model types including:

        - Virtual try-on (tryon-v1.6)
        - Model creation (model-create)
        - Model variation (model-variation)
        - Model swap (model-swap)
        - Product to model (product-to-model)
        - Background operations (background-remove, background-change)
        - Image reframing (reframe)

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
        webhook_url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PredictionRunResponse:
        """Submit a prediction request for AI-powered fashion processing.

        Supports multiple
        model types including:

        - Virtual try-on (tryon-v1.6)
        - Model creation (model-create)
        - Model variation (model-variation)
        - Model swap (model-swap)
        - Product to model (product-to-model)
        - Background operations (background-remove, background-change)
        - Image reframing (reframe)

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

    @required_args(["inputs", "model_name"])
    async def run(
        self,
        *,
        inputs: prediction_run_params.TryOnRequestInputs
        | prediction_run_params.ProductToModelRequestInputs
        | prediction_run_params.ModelCreateRequestInputs
        | prediction_run_params.ModelVariationRequestInputs
        | prediction_run_params.ModelSwapRequestInputs
        | prediction_run_params.ReframeRequestInputs
        | prediction_run_params.BackgroundChangeRequestInputs
        | prediction_run_params.BackgroundRemoveRequestInputs,
        model_name: Literal["tryon-v1.6"]
        | Literal["product-to-model"]
        | Literal["model-create"]
        | Literal["model-variation"]
        | Literal["model-swap"]
        | Literal["reframe"]
        | Literal["background-change"]
        | Literal["background-remove"],
        webhook_url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
