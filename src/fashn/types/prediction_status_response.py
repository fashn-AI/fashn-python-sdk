# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["PredictionStatusResponse", "Error"]


class Error(BaseModel):
    message: str
    """Detailed error message explaining the specific failure"""

    name: Literal[
        "ImageLoadError",
        "ContentModerationError",
        "PoseError",
        "LoRALoadError",
        "InputValidationError",
        "PipelineError",
        "ThirdPartyError",
        "3rdPartyProviderError",
        "InternalServerError",
    ]
    """Error type/category with troubleshooting guidance:

    **ImageLoadError** - Unable to load image from provided inputs

    - _Cause_: Pipeline cannot load product image, model image, garment image, or
      reference image
    - _Solution_: For URLs - ensure public accessibility and correct Content-Type
      headers. For Base64 - include proper data:image/format;base64 prefix

    **ContentModerationError** - Prohibited content detected

    - _Cause_: Content moderation flagged product, garment, or model image. More
      sensitive when model_image contains an actual person (virtual try-on mode)
    - _Solution_: For try-on models - adjust moderation_level to 'permissive' or
      'none' if appropriate. For product-to-model - explicit or inappropriate
      imagery is prohibited, particularly with real people. For intimate apparel
      (lingerie/swimwear), use FASHN Virtual Try-On endpoint with full moderation
      control. Product generation without model_image operates under more permissive
      policies. Contact support@fashn.ai with prediction ID if content was
      incorrectly flagged

    **PoseError** - Unable to detect body pose (try-on models only)

    - _Cause_: Body pose not detectable in model or garment image
    - _Solution_: Improve image quality following model photo guidelines

    **LoRALoadError** - Failed to load LoRA weights (model-create, model-variation,
    model-swap only)

    - _Cause_: Cannot download or load LoRA file
    - _Solution_: Ensure URL is public, file is valid .safetensors under 256MB,
      compatible with FLUX.1-dev

    **InputValidationError** - Invalid parameter combination (reframe only)

    - _Cause_: Missing required parameters or invalid values for selected mode
    - _Solution_: Ensure target_aspect_ratio is provided when mode is
      'aspect_ratio'. Check aspect ratio values are from supported list

    **PipelineError** - Unexpected pipeline execution error

    - _Cause_: Internal processing failure
    - _Solution_: Retry request (no charge for failures). Contact support@fashn.ai
      with prediction ID if persists

    **ThirdPartyError** - Third-party processor failure

    - _Cause_: External service restrictions (content/prompt limitations)
    - _Model-specific solutions_:
      - _Try-on_: Modify image inputs for captioning restrictions
      - _Product-to-model_: Try modifying image inputs, most likely caused by
        content restrictions in image captioning
      - _Model-swap_: Try different inputs or disable prompt enhancement
      - _Background-change_: Modify image inputs or background prompt
      - _Reframe_: Try different image inputs for captioning restrictions
    - Contact support@fashn.ai with prediction ID if persists

    **3rdPartyProviderError** - Third-party provider failure (fallback error type)

    - _Cause_: External provider error without specific classification
    - _Solution_: Retry request. Contact support@fashn.ai with prediction ID if
      persists

    **InternalServerError** - General server error (fallback error type)

    - _Cause_: Unexpected server-side failure
    - _Solution_: Retry request. Contact support@fashn.ai with prediction ID if
      persists
    """


class PredictionStatusResponse(BaseModel):
    id: str
    """The unique prediction ID"""

    error: Optional[Error] = None
    """Structured error object with name and message fields"""

    status: Literal["starting", "in_queue", "processing", "completed", "failed", "canceled", "time_out"]
    """Current status of the prediction"""

    output: Union[List[str], List[str], None] = None
    """Generated images - format depends on original request's return_base64 setting"""
