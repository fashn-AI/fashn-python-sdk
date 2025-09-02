# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from fashn import Fashn, AsyncFashn
from fashn.types import PredictionRunResponse, PredictionStatusResponse
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPredictions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_run_overload_1(self, client: Fashn) -> None:
        prediction = client.predictions.run(
            inputs={
                "garment_image": "https://example.com/garment.jpg",
                "model_image": "https://example.com/model.jpg",
            },
            model_name="tryon-v1.6",
        )
        assert_matches_type(PredictionRunResponse, prediction, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_run_with_all_params_overload_1(self, client: Fashn) -> None:
        prediction = client.predictions.run(
            inputs={
                "garment_image": "https://example.com/garment.jpg",
                "model_image": "https://example.com/model.jpg",
                "category": "auto",
                "garment_photo_type": "auto",
                "mode": "performance",
                "moderation_level": "conservative",
                "num_samples": 1,
                "output_format": "png",
                "return_base64": True,
                "seed": 0,
                "segmentation_free": True,
            },
            model_name="tryon-v1.6",
            webhook_url="https://example.com/webhook",
        )
        assert_matches_type(PredictionRunResponse, prediction, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_run_overload_1(self, client: Fashn) -> None:
        response = client.predictions.with_raw_response.run(
            inputs={
                "garment_image": "https://example.com/garment.jpg",
                "model_image": "https://example.com/model.jpg",
            },
            model_name="tryon-v1.6",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prediction = response.parse()
        assert_matches_type(PredictionRunResponse, prediction, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_run_overload_1(self, client: Fashn) -> None:
        with client.predictions.with_streaming_response.run(
            inputs={
                "garment_image": "https://example.com/garment.jpg",
                "model_image": "https://example.com/model.jpg",
            },
            model_name="tryon-v1.6",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prediction = response.parse()
            assert_matches_type(PredictionRunResponse, prediction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_run_overload_2(self, client: Fashn) -> None:
        prediction = client.predictions.run(
            inputs={"product_image": "https://example.com/product.jpg"},
            model_name="product-to-model",
        )
        assert_matches_type(PredictionRunResponse, prediction, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_run_with_all_params_overload_2(self, client: Fashn) -> None:
        prediction = client.predictions.run(
            inputs={
                "product_image": "https://example.com/product.jpg",
                "aspect_ratio": "1:1",
                "model_image": "https://example.com/person.jpg",
                "output_format": "png",
                "prompt": "professional office setting",
                "return_base64": True,
                "seed": 0,
            },
            model_name="product-to-model",
            webhook_url="https://example.com/webhook",
        )
        assert_matches_type(PredictionRunResponse, prediction, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_run_overload_2(self, client: Fashn) -> None:
        response = client.predictions.with_raw_response.run(
            inputs={"product_image": "https://example.com/product.jpg"},
            model_name="product-to-model",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prediction = response.parse()
        assert_matches_type(PredictionRunResponse, prediction, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_run_overload_2(self, client: Fashn) -> None:
        with client.predictions.with_streaming_response.run(
            inputs={"product_image": "https://example.com/product.jpg"},
            model_name="product-to-model",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prediction = response.parse()
            assert_matches_type(PredictionRunResponse, prediction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_run_overload_3(self, client: Fashn) -> None:
        prediction = client.predictions.run(
            inputs={"prompt": "A professional model wearing casual clothes"},
            model_name="model-create",
        )
        assert_matches_type(PredictionRunResponse, prediction, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_run_with_all_params_overload_3(self, client: Fashn) -> None:
        prediction = client.predictions.run(
            inputs={
                "prompt": "A professional model wearing casual clothes",
                "aspect_ratio": "1:1",
                "disable_prompt_enhancement": True,
                "image_reference": "https://example.com/reference.jpg",
                "lora_url": "https://example.com/custom_identity.safetensors",
                "output_format": "png",
                "reference_type": "pose",
                "return_base64": True,
                "seed": 0,
            },
            model_name="model-create",
            webhook_url="https://example.com/webhook",
        )
        assert_matches_type(PredictionRunResponse, prediction, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_run_overload_3(self, client: Fashn) -> None:
        response = client.predictions.with_raw_response.run(
            inputs={"prompt": "A professional model wearing casual clothes"},
            model_name="model-create",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prediction = response.parse()
        assert_matches_type(PredictionRunResponse, prediction, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_run_overload_3(self, client: Fashn) -> None:
        with client.predictions.with_streaming_response.run(
            inputs={"prompt": "A professional model wearing casual clothes"},
            model_name="model-create",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prediction = response.parse()
            assert_matches_type(PredictionRunResponse, prediction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_run_overload_4(self, client: Fashn) -> None:
        prediction = client.predictions.run(
            inputs={"model_image": "https://example.com/model.jpg"},
            model_name="model-variation",
        )
        assert_matches_type(PredictionRunResponse, prediction, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_run_with_all_params_overload_4(self, client: Fashn) -> None:
        prediction = client.predictions.run(
            inputs={
                "model_image": "https://example.com/model.jpg",
                "lora_url": "https://example.com/custom_identity.safetensors",
                "output_format": "png",
                "return_base64": True,
                "seed": 0,
                "variation_strength": "subtle",
            },
            model_name="model-variation",
            webhook_url="https://example.com/webhook",
        )
        assert_matches_type(PredictionRunResponse, prediction, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_run_overload_4(self, client: Fashn) -> None:
        response = client.predictions.with_raw_response.run(
            inputs={"model_image": "https://example.com/model.jpg"},
            model_name="model-variation",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prediction = response.parse()
        assert_matches_type(PredictionRunResponse, prediction, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_run_overload_4(self, client: Fashn) -> None:
        with client.predictions.with_streaming_response.run(
            inputs={"model_image": "https://example.com/model.jpg"},
            model_name="model-variation",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prediction = response.parse()
            assert_matches_type(PredictionRunResponse, prediction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_run_overload_5(self, client: Fashn) -> None:
        prediction = client.predictions.run(
            inputs={"model_image": "https://example.com/model.jpg"},
            model_name="model-swap",
        )
        assert_matches_type(PredictionRunResponse, prediction, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_run_with_all_params_overload_5(self, client: Fashn) -> None:
        prediction = client.predictions.run(
            inputs={
                "model_image": "https://example.com/model.jpg",
                "background_change": True,
                "disable_prompt_enhancement": True,
                "lora_url": "https://example.com/custom_identity.safetensors",
                "output_format": "png",
                "prompt": "Asian woman with long black hair and brown eyes",
                "return_base64": True,
                "seed": 0,
            },
            model_name="model-swap",
            webhook_url="https://example.com/webhook",
        )
        assert_matches_type(PredictionRunResponse, prediction, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_run_overload_5(self, client: Fashn) -> None:
        response = client.predictions.with_raw_response.run(
            inputs={"model_image": "https://example.com/model.jpg"},
            model_name="model-swap",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prediction = response.parse()
        assert_matches_type(PredictionRunResponse, prediction, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_run_overload_5(self, client: Fashn) -> None:
        with client.predictions.with_streaming_response.run(
            inputs={"model_image": "https://example.com/model.jpg"},
            model_name="model-swap",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prediction = response.parse()
            assert_matches_type(PredictionRunResponse, prediction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_run_overload_6(self, client: Fashn) -> None:
        prediction = client.predictions.run(
            inputs={"image": "https://example.com/image.jpg"},
            model_name="reframe",
        )
        assert_matches_type(PredictionRunResponse, prediction, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_run_with_all_params_overload_6(self, client: Fashn) -> None:
        prediction = client.predictions.run(
            inputs={
                "image": "https://example.com/image.jpg",
                "mode": "direction",
                "output_format": "png",
                "return_base64": True,
                "seed": 0,
                "target_aspect_ratio": "1:1",
                "target_direction": "both",
            },
            model_name="reframe",
            webhook_url="https://example.com/webhook",
        )
        assert_matches_type(PredictionRunResponse, prediction, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_run_overload_6(self, client: Fashn) -> None:
        response = client.predictions.with_raw_response.run(
            inputs={"image": "https://example.com/image.jpg"},
            model_name="reframe",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prediction = response.parse()
        assert_matches_type(PredictionRunResponse, prediction, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_run_overload_6(self, client: Fashn) -> None:
        with client.predictions.with_streaming_response.run(
            inputs={"image": "https://example.com/image.jpg"},
            model_name="reframe",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prediction = response.parse()
            assert_matches_type(PredictionRunResponse, prediction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_run_overload_7(self, client: Fashn) -> None:
        prediction = client.predictions.run(
            inputs={"image": "https://example.com/image.jpg"},
            model_name="background-change",
        )
        assert_matches_type(PredictionRunResponse, prediction, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_run_with_all_params_overload_7(self, client: Fashn) -> None:
        prediction = client.predictions.run(
            inputs={
                "image": "https://example.com/image.jpg",
                "background_prompt": "A beautiful sunset beach scene",
                "disable_prompt_enhancement": True,
                "output_format": "png",
                "return_base64": True,
                "seed": 0,
            },
            model_name="background-change",
            webhook_url="https://example.com/webhook",
        )
        assert_matches_type(PredictionRunResponse, prediction, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_run_overload_7(self, client: Fashn) -> None:
        response = client.predictions.with_raw_response.run(
            inputs={"image": "https://example.com/image.jpg"},
            model_name="background-change",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prediction = response.parse()
        assert_matches_type(PredictionRunResponse, prediction, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_run_overload_7(self, client: Fashn) -> None:
        with client.predictions.with_streaming_response.run(
            inputs={"image": "https://example.com/image.jpg"},
            model_name="background-change",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prediction = response.parse()
            assert_matches_type(PredictionRunResponse, prediction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_run_overload_8(self, client: Fashn) -> None:
        prediction = client.predictions.run(
            inputs={"image": "https://example.com/image.jpg"},
            model_name="background-remove",
        )
        assert_matches_type(PredictionRunResponse, prediction, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_run_with_all_params_overload_8(self, client: Fashn) -> None:
        prediction = client.predictions.run(
            inputs={
                "image": "https://example.com/image.jpg",
                "return_base64": True,
            },
            model_name="background-remove",
            webhook_url="https://example.com/webhook",
        )
        assert_matches_type(PredictionRunResponse, prediction, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_run_overload_8(self, client: Fashn) -> None:
        response = client.predictions.with_raw_response.run(
            inputs={"image": "https://example.com/image.jpg"},
            model_name="background-remove",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prediction = response.parse()
        assert_matches_type(PredictionRunResponse, prediction, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_run_overload_8(self, client: Fashn) -> None:
        with client.predictions.with_streaming_response.run(
            inputs={"image": "https://example.com/image.jpg"},
            model_name="background-remove",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prediction = response.parse()
            assert_matches_type(PredictionRunResponse, prediction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_status(self, client: Fashn) -> None:
        prediction = client.predictions.status(
            "123a87r9-4129-4bb3-be18-9c9fb5bd7fc1-u1",
        )
        assert_matches_type(PredictionStatusResponse, prediction, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_status(self, client: Fashn) -> None:
        response = client.predictions.with_raw_response.status(
            "123a87r9-4129-4bb3-be18-9c9fb5bd7fc1-u1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prediction = response.parse()
        assert_matches_type(PredictionStatusResponse, prediction, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_status(self, client: Fashn) -> None:
        with client.predictions.with_streaming_response.status(
            "123a87r9-4129-4bb3-be18-9c9fb5bd7fc1-u1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prediction = response.parse()
            assert_matches_type(PredictionStatusResponse, prediction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_status(self, client: Fashn) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.predictions.with_raw_response.status(
                "",
            )


class TestAsyncPredictions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_run_overload_1(self, async_client: AsyncFashn) -> None:
        prediction = await async_client.predictions.run(
            inputs={
                "garment_image": "https://example.com/garment.jpg",
                "model_image": "https://example.com/model.jpg",
            },
            model_name="tryon-v1.6",
        )
        assert_matches_type(PredictionRunResponse, prediction, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_run_with_all_params_overload_1(self, async_client: AsyncFashn) -> None:
        prediction = await async_client.predictions.run(
            inputs={
                "garment_image": "https://example.com/garment.jpg",
                "model_image": "https://example.com/model.jpg",
                "category": "auto",
                "garment_photo_type": "auto",
                "mode": "performance",
                "moderation_level": "conservative",
                "num_samples": 1,
                "output_format": "png",
                "return_base64": True,
                "seed": 0,
                "segmentation_free": True,
            },
            model_name="tryon-v1.6",
            webhook_url="https://example.com/webhook",
        )
        assert_matches_type(PredictionRunResponse, prediction, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_run_overload_1(self, async_client: AsyncFashn) -> None:
        response = await async_client.predictions.with_raw_response.run(
            inputs={
                "garment_image": "https://example.com/garment.jpg",
                "model_image": "https://example.com/model.jpg",
            },
            model_name="tryon-v1.6",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prediction = await response.parse()
        assert_matches_type(PredictionRunResponse, prediction, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_run_overload_1(self, async_client: AsyncFashn) -> None:
        async with async_client.predictions.with_streaming_response.run(
            inputs={
                "garment_image": "https://example.com/garment.jpg",
                "model_image": "https://example.com/model.jpg",
            },
            model_name="tryon-v1.6",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prediction = await response.parse()
            assert_matches_type(PredictionRunResponse, prediction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_run_overload_2(self, async_client: AsyncFashn) -> None:
        prediction = await async_client.predictions.run(
            inputs={"product_image": "https://example.com/product.jpg"},
            model_name="product-to-model",
        )
        assert_matches_type(PredictionRunResponse, prediction, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_run_with_all_params_overload_2(self, async_client: AsyncFashn) -> None:
        prediction = await async_client.predictions.run(
            inputs={
                "product_image": "https://example.com/product.jpg",
                "aspect_ratio": "1:1",
                "model_image": "https://example.com/person.jpg",
                "output_format": "png",
                "prompt": "professional office setting",
                "return_base64": True,
                "seed": 0,
            },
            model_name="product-to-model",
            webhook_url="https://example.com/webhook",
        )
        assert_matches_type(PredictionRunResponse, prediction, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_run_overload_2(self, async_client: AsyncFashn) -> None:
        response = await async_client.predictions.with_raw_response.run(
            inputs={"product_image": "https://example.com/product.jpg"},
            model_name="product-to-model",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prediction = await response.parse()
        assert_matches_type(PredictionRunResponse, prediction, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_run_overload_2(self, async_client: AsyncFashn) -> None:
        async with async_client.predictions.with_streaming_response.run(
            inputs={"product_image": "https://example.com/product.jpg"},
            model_name="product-to-model",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prediction = await response.parse()
            assert_matches_type(PredictionRunResponse, prediction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_run_overload_3(self, async_client: AsyncFashn) -> None:
        prediction = await async_client.predictions.run(
            inputs={"prompt": "A professional model wearing casual clothes"},
            model_name="model-create",
        )
        assert_matches_type(PredictionRunResponse, prediction, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_run_with_all_params_overload_3(self, async_client: AsyncFashn) -> None:
        prediction = await async_client.predictions.run(
            inputs={
                "prompt": "A professional model wearing casual clothes",
                "aspect_ratio": "1:1",
                "disable_prompt_enhancement": True,
                "image_reference": "https://example.com/reference.jpg",
                "lora_url": "https://example.com/custom_identity.safetensors",
                "output_format": "png",
                "reference_type": "pose",
                "return_base64": True,
                "seed": 0,
            },
            model_name="model-create",
            webhook_url="https://example.com/webhook",
        )
        assert_matches_type(PredictionRunResponse, prediction, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_run_overload_3(self, async_client: AsyncFashn) -> None:
        response = await async_client.predictions.with_raw_response.run(
            inputs={"prompt": "A professional model wearing casual clothes"},
            model_name="model-create",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prediction = await response.parse()
        assert_matches_type(PredictionRunResponse, prediction, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_run_overload_3(self, async_client: AsyncFashn) -> None:
        async with async_client.predictions.with_streaming_response.run(
            inputs={"prompt": "A professional model wearing casual clothes"},
            model_name="model-create",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prediction = await response.parse()
            assert_matches_type(PredictionRunResponse, prediction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_run_overload_4(self, async_client: AsyncFashn) -> None:
        prediction = await async_client.predictions.run(
            inputs={"model_image": "https://example.com/model.jpg"},
            model_name="model-variation",
        )
        assert_matches_type(PredictionRunResponse, prediction, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_run_with_all_params_overload_4(self, async_client: AsyncFashn) -> None:
        prediction = await async_client.predictions.run(
            inputs={
                "model_image": "https://example.com/model.jpg",
                "lora_url": "https://example.com/custom_identity.safetensors",
                "output_format": "png",
                "return_base64": True,
                "seed": 0,
                "variation_strength": "subtle",
            },
            model_name="model-variation",
            webhook_url="https://example.com/webhook",
        )
        assert_matches_type(PredictionRunResponse, prediction, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_run_overload_4(self, async_client: AsyncFashn) -> None:
        response = await async_client.predictions.with_raw_response.run(
            inputs={"model_image": "https://example.com/model.jpg"},
            model_name="model-variation",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prediction = await response.parse()
        assert_matches_type(PredictionRunResponse, prediction, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_run_overload_4(self, async_client: AsyncFashn) -> None:
        async with async_client.predictions.with_streaming_response.run(
            inputs={"model_image": "https://example.com/model.jpg"},
            model_name="model-variation",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prediction = await response.parse()
            assert_matches_type(PredictionRunResponse, prediction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_run_overload_5(self, async_client: AsyncFashn) -> None:
        prediction = await async_client.predictions.run(
            inputs={"model_image": "https://example.com/model.jpg"},
            model_name="model-swap",
        )
        assert_matches_type(PredictionRunResponse, prediction, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_run_with_all_params_overload_5(self, async_client: AsyncFashn) -> None:
        prediction = await async_client.predictions.run(
            inputs={
                "model_image": "https://example.com/model.jpg",
                "background_change": True,
                "disable_prompt_enhancement": True,
                "lora_url": "https://example.com/custom_identity.safetensors",
                "output_format": "png",
                "prompt": "Asian woman with long black hair and brown eyes",
                "return_base64": True,
                "seed": 0,
            },
            model_name="model-swap",
            webhook_url="https://example.com/webhook",
        )
        assert_matches_type(PredictionRunResponse, prediction, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_run_overload_5(self, async_client: AsyncFashn) -> None:
        response = await async_client.predictions.with_raw_response.run(
            inputs={"model_image": "https://example.com/model.jpg"},
            model_name="model-swap",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prediction = await response.parse()
        assert_matches_type(PredictionRunResponse, prediction, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_run_overload_5(self, async_client: AsyncFashn) -> None:
        async with async_client.predictions.with_streaming_response.run(
            inputs={"model_image": "https://example.com/model.jpg"},
            model_name="model-swap",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prediction = await response.parse()
            assert_matches_type(PredictionRunResponse, prediction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_run_overload_6(self, async_client: AsyncFashn) -> None:
        prediction = await async_client.predictions.run(
            inputs={"image": "https://example.com/image.jpg"},
            model_name="reframe",
        )
        assert_matches_type(PredictionRunResponse, prediction, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_run_with_all_params_overload_6(self, async_client: AsyncFashn) -> None:
        prediction = await async_client.predictions.run(
            inputs={
                "image": "https://example.com/image.jpg",
                "mode": "direction",
                "output_format": "png",
                "return_base64": True,
                "seed": 0,
                "target_aspect_ratio": "1:1",
                "target_direction": "both",
            },
            model_name="reframe",
            webhook_url="https://example.com/webhook",
        )
        assert_matches_type(PredictionRunResponse, prediction, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_run_overload_6(self, async_client: AsyncFashn) -> None:
        response = await async_client.predictions.with_raw_response.run(
            inputs={"image": "https://example.com/image.jpg"},
            model_name="reframe",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prediction = await response.parse()
        assert_matches_type(PredictionRunResponse, prediction, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_run_overload_6(self, async_client: AsyncFashn) -> None:
        async with async_client.predictions.with_streaming_response.run(
            inputs={"image": "https://example.com/image.jpg"},
            model_name="reframe",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prediction = await response.parse()
            assert_matches_type(PredictionRunResponse, prediction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_run_overload_7(self, async_client: AsyncFashn) -> None:
        prediction = await async_client.predictions.run(
            inputs={"image": "https://example.com/image.jpg"},
            model_name="background-change",
        )
        assert_matches_type(PredictionRunResponse, prediction, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_run_with_all_params_overload_7(self, async_client: AsyncFashn) -> None:
        prediction = await async_client.predictions.run(
            inputs={
                "image": "https://example.com/image.jpg",
                "background_prompt": "A beautiful sunset beach scene",
                "disable_prompt_enhancement": True,
                "output_format": "png",
                "return_base64": True,
                "seed": 0,
            },
            model_name="background-change",
            webhook_url="https://example.com/webhook",
        )
        assert_matches_type(PredictionRunResponse, prediction, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_run_overload_7(self, async_client: AsyncFashn) -> None:
        response = await async_client.predictions.with_raw_response.run(
            inputs={"image": "https://example.com/image.jpg"},
            model_name="background-change",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prediction = await response.parse()
        assert_matches_type(PredictionRunResponse, prediction, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_run_overload_7(self, async_client: AsyncFashn) -> None:
        async with async_client.predictions.with_streaming_response.run(
            inputs={"image": "https://example.com/image.jpg"},
            model_name="background-change",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prediction = await response.parse()
            assert_matches_type(PredictionRunResponse, prediction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_run_overload_8(self, async_client: AsyncFashn) -> None:
        prediction = await async_client.predictions.run(
            inputs={"image": "https://example.com/image.jpg"},
            model_name="background-remove",
        )
        assert_matches_type(PredictionRunResponse, prediction, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_run_with_all_params_overload_8(self, async_client: AsyncFashn) -> None:
        prediction = await async_client.predictions.run(
            inputs={
                "image": "https://example.com/image.jpg",
                "return_base64": True,
            },
            model_name="background-remove",
            webhook_url="https://example.com/webhook",
        )
        assert_matches_type(PredictionRunResponse, prediction, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_run_overload_8(self, async_client: AsyncFashn) -> None:
        response = await async_client.predictions.with_raw_response.run(
            inputs={"image": "https://example.com/image.jpg"},
            model_name="background-remove",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prediction = await response.parse()
        assert_matches_type(PredictionRunResponse, prediction, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_run_overload_8(self, async_client: AsyncFashn) -> None:
        async with async_client.predictions.with_streaming_response.run(
            inputs={"image": "https://example.com/image.jpg"},
            model_name="background-remove",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prediction = await response.parse()
            assert_matches_type(PredictionRunResponse, prediction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_status(self, async_client: AsyncFashn) -> None:
        prediction = await async_client.predictions.status(
            "123a87r9-4129-4bb3-be18-9c9fb5bd7fc1-u1",
        )
        assert_matches_type(PredictionStatusResponse, prediction, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_status(self, async_client: AsyncFashn) -> None:
        response = await async_client.predictions.with_raw_response.status(
            "123a87r9-4129-4bb3-be18-9c9fb5bd7fc1-u1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prediction = await response.parse()
        assert_matches_type(PredictionStatusResponse, prediction, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_status(self, async_client: AsyncFashn) -> None:
        async with async_client.predictions.with_streaming_response.status(
            "123a87r9-4129-4bb3-be18-9c9fb5bd7fc1-u1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prediction = await response.parse()
            assert_matches_type(PredictionStatusResponse, prediction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_status(self, async_client: AsyncFashn) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.predictions.with_raw_response.status(
                "",
            )
