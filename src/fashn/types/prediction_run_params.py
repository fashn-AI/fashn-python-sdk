# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "PredictionRunParams",
    "TryOnRequest",
    "TryOnRequestInputs",
    "ProductToModelRequest",
    "ProductToModelRequestInputs",
    "FaceToModelRequest",
    "FaceToModelRequestInputs",
    "ModelCreateRequest",
    "ModelCreateRequestInputs",
    "ModelVariationRequest",
    "ModelVariationRequestInputs",
    "ModelSwapRequest",
    "ModelSwapRequestInputs",
    "ReframeRequest",
    "ReframeRequestInputs",
    "BackgroundChangeRequest",
    "BackgroundChangeRequestInputs",
    "BackgroundRemoveRequest",
    "BackgroundRemoveRequestInputs",
    "ImageToVideoRequest",
    "ImageToVideoRequestInputs",
    "EditRequest",
    "EditRequestInputs",
]


class TryOnRequest(TypedDict, total=False):
    inputs: Required[TryOnRequestInputs]

    model_name: Required[Literal["tryon-v1.6"]]
    """
    Virtual Try-On v1.6 enables realistic garment visualization using just a single
    photo of a person and a garment
    """

    webhook_url: str
    """Optional webhook URL to receive completion notifications"""


class TryOnRequestInputs(TypedDict, total=False):
    garment_image: Required[str]
    """Reference image of the clothing item to be tried on the `model_image`.

    Base64 images must include the proper prefix (e.g.,
    `data:image/jpg;base64,<YOUR_BASE64>`)
    """

    model_image: Required[str]
    """Primary image of the person on whom the virtual try-on will be performed.

    Models Studio users can use their saved models by passing `saved:<model_name>`.
    Base64 images must include the proper prefix (e.g.,
    `data:image/jpg;base64,<YOUR_BASE64>`)
    """

    category: Literal["auto", "tops", "bottoms", "one-pieces"]
    """Use `auto` to enable automatic classification of the garment type.

    For flat-lay or ghost mannequin images, the system detects the garment type
    automatically. For on-model images, full-body shots default to a full outfit
    swap. For focused shots (upper or lower body), the system selects the most
    likely garment type (tops or bottoms).
    """

    garment_photo_type: Literal["auto", "flat-lay", "model"]
    """
    Specifies the type of garment photo to optimize internal parameters for better
    performance. `model` is for photos of garments on a model, `flat-lay` is for
    flat-lay or ghost mannequin images, and `auto` attempts to automatically detect
    the photo type.
    """

    mode: Literal["performance", "balanced", "quality"]
    """Specifies the mode of operation.

    - `performance` mode is faster but may compromise quality (5 seconds).
    - `balanced` mode is a perfect middle ground between speed and quality (8
      seconds).
    - `quality` mode is slower, but delivers the highest quality results (12–17
      seconds).
    """

    moderation_level: Literal["conservative", "permissive", "none"]
    """Sets the content moderation level for garment images.

    - `conservative` enforces stricter modesty standards suitable for culturally
      sensitive contexts. Blocks underwear, swimwear, and revealing outfits.
    - `permissive` allows swimwear, underwear, and revealing garments, while still
      blocking explicit nudity.
    - `none` disables all content moderation.

    **This technology is designed for ethical virtual try-on applications.
    Misuse—such as generating inappropriate imagery without consent—violates our
    Terms of Service. Setting moderation_level: none does not remove your
    responsibility for ethical and lawful use. Violations may result in service
    denial.**
    """

    num_samples: int
    """Number of images to generate in a single run.

    Image generation has a random element in it, so trying multiple images at once
    increases the chances of getting a good result.
    """

    output_format: Literal["png", "jpeg"]
    """Specifies the desired output image format.

    - `png`: Delivers the highest quality image, ideal for use cases such as content
      creation where quality is paramount.
    - `jpeg`: Provides a faster response with a slightly compressed image, more
      suitable for real-time applications like consumer virtual try-on experiences.
    """

    return_base64: bool
    """
    When set to `true`, the API will return the generated image as a base64-encoded
    string instead of a CDN URL. The base64 string will be prefixed according to the
    `output_format` (e.g., `data:image/png;base64,...` or
    `data:image/jpeg;base64,...`). This option offers enhanced privacy as
    user-generated outputs are not stored on our servers when `return_base64` is
    enabled.
    """

    seed: int
    """Sets random operations to a fixed state.

    Use the same seed to reproduce results with the same inputs, or different seed
    to force different results.
    """

    segmentation_free: bool
    """
    Direct garment fitting without clothing segmentation, enabling bulkier garment
    try-ons with improved preservation of body shape and skin texture. Set to
    `false` if original garments are not removed properly.
    """


class ProductToModelRequest(TypedDict, total=False):
    inputs: Required[ProductToModelRequestInputs]

    model_name: Required[Literal["product-to-model"]]
    """
    Product to Model endpoint transforms product images into people wearing those
    products. It supports dual-mode operation: standard product-to-model (generates
    new person) and try-on mode (adds product to existing person)
    """

    webhook_url: str
    """Optional webhook URL to receive completion notifications"""


class ProductToModelRequestInputs(TypedDict, total=False):
    product_image: Required[str]
    """URL or base64 encoded image of the product to be worn.

    Supports clothing, accessories, shoes, and other wearable fashion items. Base64
    images must include the proper prefix (e.g.,
    data:image/jpg;base64,<YOUR_BASE64>)
    """

    aspect_ratio: Literal["1:1", "2:3", "3:4", "4:5", "5:4", "4:3", "3:2", "16:9", "9:16"]
    """Desired aspect ratio for the output image.

    Only applies when `model_image` is not provided (standard product-to-model
    mode).

    When `model_image` is provided (try-on mode), this parameter is ignored and the
    output will match the `model_image`'s aspect ratio.

    **Default:** product_image's aspect ratio (standard mode only)
    """

    image_prompt: str
    """
    Optional URL or base64 of an inspiration image to guide pose, environment, and
    lighting while keeping the final edit product-centric.
    """

    model_image: str
    """URL or base64 encoded image of the person to wear the product.

    When provided, enables try-on mode. When omitted, generates a new person wearing
    the product. Base64 images must include the proper prefix (e.g.,
    data:image/jpg;base64,<YOUR_BASE64>)
    """

    output_format: Literal["png", "jpeg"]
    """Specifies the desired output image format.

    - `png`: Delivers the highest quality image, ideal for use cases such as content
      creation where quality is paramount.
    - `jpeg`: Provides a faster response with a slightly compressed image, more
      suitable for real-time applications.
    """

    prompt: str
    """
    Additional instructions for person appearance (when `model_image` is not
    provided), styling preferences, or background.

    **Examples:** "man with tattoos", "tucked-in", "open jacket", "rolled-up
    sleeves", "studio background", "professional office setting"

    **Default:** None
    """

    resolution: Literal["1k", "4k"]
    """Resolution setting for the output image."""

    return_base64: bool
    """
    When set to `true`, the API will return the generated image as a base64-encoded
    string instead of a CDN URL. The base64 string will be prefixed
    `data:image/png;base64,....`

    This option offers enhanced privacy as user-generated outputs are not stored on
    our servers when `return_base64` is enabled.
    """

    seed: int
    """Seed for reproducible results.

    Use the same seed to reproduce results with the same inputs, or different seed
    to force different results. Must be between 0 and 2^32-1.
    """


class FaceToModelRequest(TypedDict, total=False):
    inputs: Required[FaceToModelRequestInputs]

    model_name: Required[Literal["face-to-model"]]
    """
    Face to Model endpoint transforms face images into try-on ready upper-body
    avatars. It converts cropped headshots or selfies into full upper-body
    representations that can be used in virtual try-on applications when full-body
    photos are not available, while preserving facial identity.
    """

    webhook_url: str
    """Optional webhook URL to receive completion notifications"""


class FaceToModelRequestInputs(TypedDict, total=False):
    face_image: Required[str]
    """URL or base64 encoded image of the face to transform into an upper-body avatar.

    The AI will analyze facial features, hair, and skin tone to create a
    representation suitable for virtual try-on applications.

    Base64 images must include the proper prefix (e.g.,
    data:image/jpg;base64,<YOUR_BASE64>)
    """

    aspect_ratio: Literal["1:1", "4:5", "3:4", "2:3", "9:16"]
    """Desired aspect ratio for the output image.

    Only vertical ratios are supported. Images will always be extended downward to
    fit the aspect ratio.

    **Default:** `2:3`
    """

    output_format: Literal["png", "jpeg"]
    """Specifies the output image format.

    - `png` - PNG format, original quality
    - `jpeg` - JPEG format, smaller file size

    **Default:** `"jpeg"`
    """

    prompt: str
    """Optional styling or body shape guidance for the avatar representation.

    Examples: "athletic build", "curvy figure", "slender frame".

    If you don't provide a prompt, the body shape will be inferred from the face
    image.

    **Default:** Empty string
    """

    return_base64: bool
    """
    When set to `true`, the API will return the generated image as a base64-encoded
    string instead of a CDN URL. The base64 string will be prefixed
    `data:image/png;base64,...`.

    This option offers enhanced privacy as user-generated outputs are not stored on
    our servers when `return_base64` is enabled.

    **Default:** `false`
    """

    seed: int
    """Sets random operations to a fixed state.

    Use the same seed to reproduce results with the same inputs, or different seed
    to force different results.
    """


class ModelCreateRequest(TypedDict, total=False):
    inputs: Required[ModelCreateRequestInputs]

    model_name: Required[Literal["model-create"]]
    """Model creation endpoint"""

    webhook_url: str
    """Optional webhook URL to receive completion notifications"""


class ModelCreateRequestInputs(TypedDict, total=False):
    prompt: Required[str]
    """Prompt for the model image generation.

    Describes the desired fashion model, clothing, pose, and scene.
    """

    aspect_ratio: Literal["1:1", "2:3", "3:4", "4:5", "5:4", "4:3", "3:2", "16:9", "9:16"]
    """Defines the width-to-height ratio of the generated image.

    This parameter controls the canvas dimensions for text-only generation. When
    image_reference is provided, the output inherits the reference image's aspect
    ratio and this parameter is ignored.

    **Supported Resolutions**

    Each aspect ratio corresponds to a specific resolution optimized for ~1MP
    output:

    | Aspect Ratio | Resolution  | Use Case                      |
    | ------------ | ----------- | ----------------------------- |
    | 1:1          | 1024 × 1024 | Square format, social media   |
    | 2:3          | 832 × 1248  | Portrait, fashion photography |
    | 3:4          | 880 × 1176  | Standard portrait             |
    | 4:5          | 912 × 1144  | Instagram portrait            |
    | 5:4          | 1144 × 912  | Landscape portrait            |
    | 4:3          | 1176 × 880  | Traditional landscape         |
    | 3:2          | 1176 × 784  | Wide landscape                |
    | 16:9         | 1360 × 768  | Widescreen, banners           |
    | 9:16         | 760 × 1360  | Vertical video format         |
    """

    disable_prompt_enhancement: bool
    """Disable prompt enhancement.

    When true, the prompt will be used as is, or a default prompt will be used if no
    prompt is provided.
    """

    image_reference: str
    """Optional reference image that guides the generation process.

    The model extracts structural information from this image to control the output
    composition.

    Processing Behavior:

    - Aspect Ratio: Output automatically matches the reference image's dimensions.
    - Guidance Type: Controlled by the reference_type parameter (pose or silhouette)
    - Image Processing: Automatically resized while preserving aspect ratio

    Base64 images must include the proper prefix (e.g.,
    data:image/jpg;base64,<YOUR_BASE64>)
    """

    lora_url: str
    """
    URL to a FLUX-based LoRA weights file (.safetensors) for custom identity
    generation. When provided, the LoRA will be loaded and applied during generation
    to maintain consistent character appearance across generations. Must be
    FLUX-compatible LoRA weights in .safetensors format, under 256MB.
    """

    output_format: Literal["png", "jpeg"]
    """Specifies the desired output image format.

    - `png`: Delivers the highest quality image, ideal for use cases such as content
      creation where quality is paramount.
    - `jpeg`: Provides a faster response with a slightly compressed image, more
      suitable for real-time applications.
    """

    reference_type: Literal["pose", "silhouette"]
    """Type of reference to use when image_reference is provided.

    - `pose` matches the body position and stance from the reference image.
    - `silhouette` matches the outline and shape from the reference image.

    **Default is applied only if image_reference is provided**
    """

    return_base64: bool
    """
    When set to `true`, the API will return the generated image as a base64-encoded
    string instead of a CDN URL. The base64 string will be prefixed according to the
    `output_format` (e.g., `data:image/png;base64,...` or
    `data:image/jpeg;base64,...`). This option offers enhanced privacy as
    user-generated outputs are not stored on our servers when `return_base64` is
    enabled.
    """

    seed: int
    """Random seed for reproducible results"""


class ModelVariationRequest(TypedDict, total=False):
    inputs: Required[ModelVariationRequestInputs]

    model_name: Required[Literal["model-variation"]]
    """Model variation endpoint for creating variations from existing model images"""

    webhook_url: str
    """Optional webhook URL to receive completion notifications"""


class ModelVariationRequestInputs(TypedDict, total=False):
    model_image: Required[str]
    """Source fashion model image to create variations from.

    The variation will maintain the core composition while introducing controlled
    modifications. Base64 images must include the proper prefix (e.g.,
    data:image/jpg;base64,<YOUR_BASE64>)
    """

    lora_url: str
    """
    URL to a FLUX-based LoRA weights file (.safetensors) for custom identity
    generation. When provided, the LoRA will be loaded and applied during generation
    to maintain consistent character appearance across generations. Must be
    FLUX-compatible LoRA weights in .safetensors format, under 256MB.
    """

    output_format: Literal["png", "jpeg"]
    """Specifies the desired output image format.

    - `png`: Delivers the highest quality image, ideal for use cases such as content
      creation where quality is paramount.
    - `jpeg`: Provides a faster response with a slightly compressed image, more
      suitable for real-time applications.
    """

    return_base64: bool
    """
    When set to `true`, the API will return the generated image as a base64-encoded
    string instead of a CDN URL. The base64 string will be prefixed according to the
    `output_format` (e.g., `data:image/png;base64,...` or
    `data:image/jpeg;base64,...`). This option offers enhanced privacy as
    user-generated outputs are not stored on our servers when `return_base64` is
    enabled.
    """

    seed: int
    """Sets random operations to a fixed state.

    Use the same seed to reproduce results with the same inputs, or different seed
    to force different results.
    """

    variation_strength: Literal["subtle", "strong"]
    """Controls the intensity of variations applied to the source image.

    - `subtle` - Minor adjustments that preserve most of the original
      characteristics while introducing small variations.
    - `strong` - More significant modifications that create noticeable differences
      while maintaining the core composition.
    """


class ModelSwapRequest(TypedDict, total=False):
    inputs: Required[ModelSwapRequestInputs]

    model_name: Required[Literal["model-swap"]]
    """
    Model swap endpoint for transforming model identity while preserving clothing
    and pose
    """

    webhook_url: str
    """Optional webhook URL to receive completion notifications"""


class ModelSwapRequestInputs(TypedDict, total=False):
    model_image: Required[str]
    """Source fashion model image containing the clothing and pose to preserve.

    The model's identity (face, skin tone, hair) will be transformed while keeping
    the outfit exactly as shown. Base64 images must include the proper prefix (e.g.,
    data:image/jpg;base64,<YOUR_BASE64>)
    """

    background_change: bool
    """
    Controls whether the background should be modified according to the prompt or
    preserved from the original image. When enabled, include background descriptions
    in your prompt.

    - `true` - Background will be changed according to the prompt description.
    - `false` - Original background will be preserved exactly as in the source
      image.
    """

    disable_prompt_enhancement: bool
    """Disable prompt enhancement.

    When true, the prompt will be used exactly as provided, or a default prompt will
    be used if no prompt is provided.
    """

    lora_url: str
    """
    URL to a FLUX-based LoRA weights file (.safetensors) for custom identity
    generation. When provided, the LoRA will be loaded and applied during generation
    to maintain consistent character appearance across generations. Must be
    FLUX-compatible LoRA weights in .safetensors format, under 256MB.
    """

    output_format: Literal["png", "jpeg"]
    """Specifies the desired output image format.

    - `png`: Delivers the highest quality image, ideal for use cases such as content
      creation where quality is paramount.
    - `jpeg`: Provides a faster response with a slightly compressed image, more
      suitable for real-time applications.
    """

    prompt: str
    """Description of the desired model identity transformation.

    Specify ethnicity, facial features, hair color, and other physical
    characteristics.

    **Default: Empty string (Random identity change)**
    """

    return_base64: bool
    """
    When set to `true`, the API will return the generated image as a base64-encoded
    string instead of a CDN URL. The base64 string will be prefixed according to the
    `output_format` (e.g., `data:image/png;base64,...` or
    `data:image/jpeg;base64,...`). This option offers enhanced privacy as
    user-generated outputs are not stored on our servers when `return_base64` is
    enabled.
    """

    seed: int
    """Sets random operations to a fixed state.

    Use the same seed to reproduce results with the same inputs, or different seed
    to force different results.
    """


class ReframeRequest(TypedDict, total=False):
    inputs: Required[ReframeRequestInputs]

    model_name: Required[Literal["reframe"]]
    """Image reframing endpoint"""

    webhook_url: str
    """Optional webhook URL to receive completion notifications"""


class ReframeRequestInputs(TypedDict, total=False):
    aspect_ratio: Required[Literal["21:9", "1:1", "4:3", "3:2", "2:3", "5:4", "4:5", "3:4", "16:9", "9:16"]]
    """Target aspect ratio for the reframed image.

    The AI determines whether expansion or cropping is more appropriate based on the
    current image content and dimensions.

    **Behavior:**

    - If target is wider than source → may expand horizontally or crop vertically
    - If target is taller than source → may expand vertically or crop horizontally
    - If source already matches target (within 2% tolerance) → returns an error

    **Supported Aspect Ratios**

    Each aspect ratio corresponds to a specific resolution optimized for ~1MP
    output:

    | Aspect Ratio | Resolution  | Use Case                      |
    | ------------ | ----------- | ----------------------------- |
    | 21:9         | 1568 × 672  | Ultra-wide cinematic          |
    | 1:1          | 1024 × 1024 | Square format, social media   |
    | 4:3          | 1176 × 880  | Traditional landscape         |
    | 3:2          | 1248 × 832  | Standard landscape            |
    | 2:3          | 832 × 1248  | Portrait, fashion photography |
    | 5:4          | 1144 × 912  | Instagram landscape           |
    | 4:5          | 912 × 1144  | Instagram portrait            |
    | 3:4          | 880 × 1176  | Standard portrait             |
    | 16:9         | 1360 × 760  | Horizontal video format       |
    | 9:16         | 760 × 1360  | Vertical video format         |
    """

    image: Required[str]
    """Source image to reframe to a new aspect ratio.

    The AI will intelligently analyze the image content and decide whether to expand
    (outpainting/zoom-out) or crop (zoom-in) based on subject position, content
    density, and edge details.

    Resolution Handling: Output resolution is limited to ~1MP. If your image is
    already at or above this size, it will be downsampled so that, after reframing,
    the final result fits within the 1MP limit.

    Base64 Format: Base64 images must include the proper prefix (e.g.,
    data:image/jpg;base64,<YOUR_BASE64>)
    """

    num_images: int
    """Number of images to generate in a single run.

    Image generation has a random element in it, so trying multiple images at once
    increases the chances of getting a good result.
    """

    output_format: Literal["png", "jpeg"]
    """Specifies the desired output image format.

    - `png`: Delivers the highest quality image, ideal for use cases such as content
      creation where quality is paramount.
    - `jpeg`: Provides a faster response with a slightly compressed image, more
      suitable for real-time applications.
    """

    return_base64: bool
    """
    When set to `true`, the API will return the generated image as a base64-encoded
    string instead of a CDN URL. The base64 string will be prefixed according to the
    `output_format` (e.g., `data:image/png;base64,...` or
    `data:image/jpeg;base64,...`). This option offers enhanced privacy as
    user-generated outputs are not stored on our servers when `return_base64` is
    enabled.
    """

    seed: int
    """Sets random operations to a fixed state.

    Use the same seed to reproduce results with the same inputs, or different seed
    to force different results.
    """


class BackgroundChangeRequest(TypedDict, total=False):
    inputs: Required[BackgroundChangeRequestInputs]

    model_name: Required[Literal["background-change"]]
    """Background change endpoint"""

    webhook_url: str
    """Optional webhook URL to receive completion notifications"""


class BackgroundChangeRequestInputs(TypedDict, total=False):
    image: Required[str]
    """Source image containing the subject to preserve.

    The AI will automatically detect and separate the foreground subject from the
    background. Base64 images must include the proper prefix (e.g.,
    data:image/jpg;base64,<YOUR_BASE64>)
    """

    prompt: Required[str]
    """
    Description of the desired new background (e.g., 'beach sunset', 'modern
    office', 'forest clearing'). The AI generates a new background based on this
    description and harmonizes it with the preserved foreground subject.
    """

    disable_prompt_enhancement: bool
    """Disable prompt enhancement for the background description.

    When `true`, the background prompt will be used exactly as provided.
    """

    output_format: Literal["png", "jpeg"]
    """Specifies the output image format.

    - `png`: Delivers the highest quality image, ideal for use cases such as content
      creation where quality is paramount.
    - `jpeg`: Provides a faster response with a slightly compressed image, more
      suitable for real-time applications.
    """

    return_base64: bool
    """
    When set to `true`, the API will return the generated image as a base64-encoded
    string instead of a CDN URL. The base64 string will be prefixed according to the
    `output_format` (e.g., `data:image/png;base64,...` or
    `data:image/jpeg;base64,...`). This option offers enhanced privacy as
    user-generated outputs are not stored on our servers when `return_base64` is
    enabled.
    """

    seed: int
    """Sets random operations to a fixed state.

    Use the same seed to reproduce results with the same inputs, or different seed
    to force different results.
    """


class BackgroundRemoveRequest(TypedDict, total=False):
    inputs: Required[BackgroundRemoveRequestInputs]

    model_name: Required[Literal["background-remove"]]
    """Background removal endpoint"""

    webhook_url: str
    """Optional webhook URL to receive completion notifications"""


class BackgroundRemoveRequestInputs(TypedDict, total=False):
    image: Required[str]
    """Source image to remove the background from.

    The AI will automatically detect the main subject and create a clean cutout with
    transparent background. Base64 images must include the proper prefix (e.g.,
    data:image/jpg;base64,<YOUR_BASE64>)
    """

    return_base64: bool
    """
    When set to `true`, the API will return the generated image as a base64-encoded
    string instead of a CDN URL. The base64 string will be prefixed
    `data:image/png;base64,...`. This option offers enhanced privacy as
    user-generated outputs are not stored on our servers when `return_base64` is
    enabled.
    """


class ImageToVideoRequest(TypedDict, total=False):
    inputs: Required[ImageToVideoRequestInputs]

    model_name: Required[Literal["image-to-video"]]
    """
    Image to Video turns a single image into a short motion clip, with tasteful
    camera work and model movements tailored for fashion.
    """

    webhook_url: str
    """Optional webhook URL to receive completion notifications"""


class ImageToVideoRequestInputs(TypedDict, total=False):
    image: Required[str]
    """Source image to animate into a short video.

    Base64 images must include the proper prefix (e.g.,
    `data:image/jpg;base64,<YOUR_BASE64>`)
    """

    duration: Literal[5, 10]
    """Duration of the generated video in seconds."""

    negative_prompt: str
    """Optional cues to avoid undesirable motion or framing."""

    prompt: str
    """Optional motion guidance.

    Detailed prompting is not recommended because motion is difficult to control
    precisely. For the best results, leave this field empty and allow the system to
    plan motion automatically. If you include guidance, keep it short and concrete
    (e.g., "raising hand to touch face").
    """

    resolution: Literal["480p", "720p", "1080p"]
    """Target video resolution used by the internal video engine."""


class EditRequest(TypedDict, total=False):
    inputs: Required[EditRequestInputs]

    model_name: Required[Literal["edit"]]
    """
    Versatile post-processing to restyle shots, adjust views, and fix details while
    preserving identity and product fidelity.
    """

    webhook_url: str
    """Optional webhook URL to receive completion notifications"""


class EditRequestInputs(TypedDict, total=False):
    image: Required[str]
    """Source image to edit.

    The AI will apply the requested modifications based on your prompt while
    preserving the overall composition and identity of the image.

    Base64 images must include the proper prefix (e.g.,
    `data:image/jpg;base64,<YOUR_BASE64>`)
    """

    prompt: Required[str]
    """Natural language description of the edit to apply.

    Be specific about what you want to change.

    **Examples:** "change the dress to red", "add sunglasses", "make the background
    a beach sunset", "change the shirt to a floral pattern"
    """

    image_context: str
    """Optional URL or base64 of a context image to guide the edit.

    This image provides additional visual context that influences how the edit is
    applied.

    Base64 images must include the proper prefix (e.g.,
    `data:image/jpg;base64,<YOUR_BASE64>`)
    """

    mask: str
    """
    Optional mask image where white (255) marks regions to edit and black (0) areas
    remain unchanged. When provided, the edit will only affect the masked regions,
    enabling precise local edits.

    Base64 images must include the proper prefix (e.g.,
    `data:image/png;base64,<YOUR_BASE64>`)
    """

    num_images: int
    """Number of images to generate in a single run.

    Image generation has a random element in it, so trying multiple images at once
    increases the chances of getting a good result.
    """

    output_format: Literal["png", "jpeg"]
    """Specifies the desired output image format.

    - `png`: Delivers the highest quality image, ideal for use cases such as content
      creation where quality is paramount.
    - `jpeg`: Provides a faster response with a slightly compressed image, more
      suitable for real-time applications.
    """

    resolution: Literal["1k", "4k"]
    """Resolution setting for the output image."""

    return_base64: bool
    """
    When set to `true`, the API will return the generated image as a base64-encoded
    string instead of a CDN URL. The base64 string will be prefixed according to the
    `output_format` (e.g., `data:image/png;base64,...` or
    `data:image/jpeg;base64,...`). This option offers enhanced privacy as
    user-generated outputs are not stored on our servers when `return_base64` is
    enabled.
    """

    seed: int
    """Sets random operations to a fixed state.

    Use the same seed to reproduce results with the same inputs, or different seed
    to force different results.
    """


PredictionRunParams: TypeAlias = Union[
    TryOnRequest,
    ProductToModelRequest,
    FaceToModelRequest,
    ModelCreateRequest,
    ModelVariationRequest,
    ModelSwapRequest,
    ReframeRequest,
    BackgroundChangeRequest,
    BackgroundRemoveRequest,
    ImageToVideoRequest,
    EditRequest,
]
