# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "PredictionRunParams",
    "TryOnMaxRequest",
    "TryOnMaxRequestInputs",
    "TryOnRequest",
    "TryOnRequestInputs",
    "ProductToModelRequest",
    "ProductToModelRequestInputs",
    "FaceToModelRequest",
    "FaceToModelRequestInputs",
    "ModelCreateRequest",
    "ModelCreateRequestInputs",
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
    "PackshotRequest",
    "PackshotRequestInputs",
]


class TryOnMaxRequest(TypedDict, total=False):
    inputs: Required[TryOnMaxRequestInputs]

    model_name: Required[Literal["tryon-max"]]
    """
    Premium virtual try-on built for AI fashion photoshoots and publishable
    e-commerce content. Places products onto model images with enhanced fidelity,
    producing images suitable for PDPs, catalogs, and marketing assets.
    """

    webhook_url: str
    """Optional webhook URL to receive completion notifications"""


class TryOnMaxRequestInputs(TypedDict, total=False):
    model_image: Required[str]
    """URL or base64 encoded image of the person to wear the product.

    The try-on process preserves the model's identity, pose, and styling while
    seamlessly integrating the product. Base64 images must include the proper prefix
    (e.g., data:image/jpg;base64,<YOUR_BASE64>)
    """

    product_image: Required[str]
    """
    URL or base64 encoded image of the product (garment, accessory, etc.) to place
    on the model. Base64 images must include the proper prefix (e.g.,
    data:image/jpg;base64,<YOUR_BASE64>)
    """

    aspect_ratio: Literal["21:9", "1:1", "4:3", "3:2", "2:3", "5:4", "4:5", "3:4", "16:9", "9:16"]
    """Optional aspect ratio for the output image."""

    generation_mode: Literal["fast", "balanced", "quality"]
    """Sets the generation quality level.

    'quality' produces the most detailed and realistic output but takes longer to
    process and costs more credits. 'fast' prioritizes speed and lower cost.
    """

    num_images: int
    """Number of images to generate per request (1-4)."""

    output_format: Literal["png", "jpeg"]
    """Specifies the desired output image format.

    - `png`: Delivers the highest quality image, ideal for use cases such as content
      creation where quality is paramount.
    - `jpeg`: Provides a faster response with a slightly compressed image, more
      suitable for real-time applications.
    """

    prompt: str
    """Optional instructions to customize the try-on result.

    Use this to adjust how the product is worn or make minor styling changes.

    **Examples:** "remove scarf", "tuck in shirt", "roll up sleeves", "open jacket"
    """

    resolution: Literal["1k", "2k", "4k"]
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
    """Controls generation randomness on a best-effort basis.

    Exact reproducibility is not guaranteed.
    """


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
    """Number of images to generate per request (1-4)."""

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
    """Controls generation randomness on a best-effort basis.

    Exact reproducibility is not guaranteed.
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

    aspect_ratio: Literal["21:9", "1:1", "4:3", "3:2", "2:3", "5:4", "4:5", "3:4", "16:9", "9:16"]
    """Desired aspect ratio for the output image.

    Only applies when `model_image` is not provided (standard product-to-model
    mode).

    When `model_image` is provided (try-on mode), this parameter is ignored and the
    output will match the `model_image`'s aspect ratio.

    **Default:** product_image's aspect ratio (standard mode only)
    """

    generation_mode: Literal["fast", "balanced", "quality"]
    """Sets the generation quality level.

    'quality' produces the most detailed and realistic output but takes longer to
    process and costs more credits. 'fast' prioritizes speed and lower cost.
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

    resolution: Literal["1k", "2k", "4k"]
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
    """Controls generation randomness on a best-effort basis.

    Must be between 0 and 2^32-1; exact reproducibility is not guaranteed.
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

    aspect_ratio: Literal["21:9", "1:1", "4:3", "3:2", "2:3", "5:4", "4:5", "3:4", "16:9", "9:16"]
    """Desired aspect ratio for the output image.

    Vertical ratios (e.g. `2:3`, `3:4`, `9:16`) produce the most natural upper-body
    portraits.

    **Default:** `2:3`
    """

    generation_mode: Literal["fast", "balanced", "quality"]
    """Sets the generation quality level.

    'quality' produces the most detailed and realistic output but takes longer to
    process and costs more credits. 'fast' prioritizes speed and lower cost.
    """

    num_images: int
    """Number of images to generate in a single run."""

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

    resolution: Literal["1k", "2k", "4k"]
    """Resolution setting for the output image."""

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
    """Controls generation randomness on a best-effort basis.

    Exact reproducibility is not guaranteed.
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

    aspect_ratio: Literal["21:9", "1:1", "4:3", "3:2", "2:3", "5:4", "4:5", "3:4", "16:9", "9:16"]
    """Defines the width-to-height ratio of the generated image.

    This parameter controls the canvas dimensions for text-only generation. When
    image_reference is provided, the output inherits the reference image's aspect
    ratio and this parameter is ignored.

    **Supported Resolutions**

    Each aspect ratio corresponds to a specific resolution optimized for ~1MP
    output:

    | Aspect Ratio | Resolution  | Use Case                      |
    | ------------ | ----------- | ----------------------------- |
    | 21:9         | 1568 × 672  | Ultra-wide cinematic          |
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

    face_reference: str
    """Optional face reference image to guide facial features in the generated model.

    When provided, the generated person will resemble the face in this image.

    Base64 images must include the proper prefix (e.g.,
    data:image/jpg;base64,<YOUR_BASE64>)
    """

    face_reference_mode: Literal["match_base", "match_reference"]
    """Controls how the face reference is applied.

    - `match_base` adapts the reference face to match the base image's style and
      lighting.
    - `match_reference` preserves the reference face as closely as possible.
    """

    generation_mode: Literal["fast", "balanced", "quality"]
    """Sets the generation quality level.

    'quality' produces the most detailed and realistic output but takes longer to
    process and costs more credits. 'fast' prioritizes speed and lower cost.
    """

    image_reference: str
    """Optional reference image that guides the generation process.

    The model extracts structural information from this image to control the output
    composition.

    Processing Behavior:

    - Aspect Ratio: When image_reference is provided and aspect_ratio is omitted,
      the output matches the reference image's dimensions. If aspect_ratio is
      explicitly set, it overrides the reference image's proportions.
    - Image Processing: Automatically resized while preserving aspect ratio.

    Base64 images must include the proper prefix (e.g.,
    data:image/jpg;base64,<YOUR_BASE64>)
    """

    num_images: int
    """Number of images to generate."""

    output_format: Literal["png", "jpeg"]
    """Specifies the desired output image format.

    - `png`: Delivers the highest quality image, ideal for use cases such as content
      creation where quality is paramount.
    - `jpeg`: Provides a faster response with a slightly compressed image, more
      suitable for real-time applications.
    """

    resolution: Literal["1k", "2k", "4k"]
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
    """Controls generation randomness on a best-effort basis.

    Exact reproducibility is not guaranteed.
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

    aspect_ratio: Literal["21:9", "1:1", "4:3", "3:2", "2:3", "5:4", "4:5", "3:4", "16:9", "9:16"]
    """Optional aspect ratio for the output image."""

    face_reference: str
    """Optional face reference image to guide facial features of the replacement
    person.

    When provided, the new person will resemble the face in this image.

    Base64 images must include the proper prefix (e.g.,
    data:image/jpg;base64,<YOUR_BASE64>)
    """

    face_reference_mode: Literal["match_base", "match_reference"]
    """Controls how the face reference is applied.

    - `match_base` adapts the reference face to match the base image's style and
      lighting.
    - `match_reference` preserves the reference face as closely as possible.
    """

    generation_mode: Literal["fast", "balanced", "quality"]
    """Sets the generation quality level.

    'quality' produces the most detailed and realistic output but takes longer to
    process and costs more credits. 'fast' prioritizes speed and lower cost.
    """

    num_images: int
    """Number of images to generate."""

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

    resolution: Literal["1k", "2k", "4k"]
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
    """Controls generation randomness on a best-effort basis.

    Exact reproducibility is not guaranteed.
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

    generation_mode: Literal["fast", "balanced", "quality"]
    """Sets the generation quality level.

    'quality' produces the most detailed and realistic output but takes longer to
    process and costs more credits. 'fast' prioritizes speed and lower cost.
    """

    num_images: int
    """Number of images to generate per request (1-4)."""

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
    """Controls generation randomness on a best-effort basis.

    Exact reproducibility is not guaranteed.
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

    generation_mode: Literal["fast", "balanced", "quality"]
    """Sets the generation quality level.

    'quality' produces the most detailed and realistic output but takes longer to
    process and costs more credits. 'fast' prioritizes speed and lower cost.
    """

    num_images: int
    """Number of images to generate in a single run."""

    output_format: Literal["png", "jpeg"]
    """Specifies the output image format.

    - `png`: Delivers the highest quality image, ideal for use cases such as content
      creation where quality is paramount.
    - `jpeg`: Provides a faster response with a slightly compressed image, more
      suitable for real-time applications.
    """

    resolution: Literal["1k", "2k", "4k"]
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
    """Controls generation randomness on a best-effort basis.

    Exact reproducibility is not guaranteed.
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

    end_image: str
    """Optional image to use as the final frame of the generated video.

    When provided, the video smoothly transitions from the `image` (start frame) to
    `end_image` (end frame) over the clip duration.

    Supported with `resolution: "480p"`, `"720p"`, and `"1080p"`.

    Base64 images must include the proper prefix (e.g.,
    `data:image/jpg;base64,<YOUR_BASE64>`).
    """

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
    """Target video resolution used by the video engine."""

    seed: int
    """Controls generation randomness on a best-effort basis.

    Exact reproducibility is not guaranteed.
    """


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

    aspect_ratio: Literal["21:9", "1:1", "4:3", "3:2", "2:3", "5:4", "4:5", "3:4", "16:9", "9:16"]
    """Optional aspect ratio for the output image."""

    generation_mode: Literal["fast", "balanced", "quality"]
    """Sets the generation quality level.

    'quality' produces the most detailed and realistic output but takes longer to
    process and costs more credits. 'fast' prioritizes speed and lower cost.
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
    """Number of images to generate per request (1-4)."""

    output_format: Literal["png", "jpeg"]
    """Specifies the desired output image format.

    - `png`: Delivers the highest quality image, ideal for use cases such as content
      creation where quality is paramount.
    - `jpeg`: Provides a faster response with a slightly compressed image, more
      suitable for real-time applications.
    """

    resolution: Literal["1k", "2k", "4k"]
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
    """Controls generation randomness on a best-effort basis.

    Exact reproducibility is not guaranteed.
    """


class PackshotRequest(TypedDict, total=False):
    inputs: Required[PackshotRequestInputs]

    model_name: Required[Literal["packshot"]]
    """Turns a product photo into a clean commercial packshot.

    Optionally accepts a style reference image to guide staging, background, and
    lighting.
    """

    webhook_url: str
    """Optional webhook URL to receive completion notifications"""


class PackshotRequestInputs(TypedDict, total=False):
    product_image: Required[str]
    """Source product image to convert into a commercial packshot.

    The AI generates a clean studio-style presentation while preserving product
    identity and detail.

    Base64 images must include the proper prefix (e.g.,
    `data:image/jpg;base64,<YOUR_BASE64>`)
    """

    aspect_ratio: Literal["21:9", "1:1", "4:3", "3:2", "2:3", "5:4", "4:5", "3:4", "16:9", "9:16"]
    """Optional aspect ratio for the output image."""

    generation_mode: Literal["fast", "balanced", "quality"]
    """Sets the generation quality level.

    'quality' produces the most detailed and realistic output but takes longer to
    process and costs more credits. 'fast' prioritizes speed and lower cost.
    """

    image_context: str
    """
    Optional URL or base64 of a style reference image guiding the packshot
    presentation (staging, background, lighting). The reference influences styling
    without overriding the product itself.

    Base64 images must include the proper prefix (e.g.,
    `data:image/jpg;base64,<YOUR_BASE64>`)
    """

    num_images: int
    """Number of images to generate per request (1-4)."""

    output_format: Literal["png", "jpeg"]
    """Specifies the desired output image format.

    - `png`: Delivers the highest quality image, ideal for use cases such as content
      creation where quality is paramount.
    - `jpeg`: Provides a faster response with a slightly compressed image, more
      suitable for real-time applications.
    """

    prompt: str
    """Optional natural-language description of the desired packshot styling.

    If empty, the model picks a sensible commercial default for the detected
    product.

    **Examples:** "clean white background flat-lay", "soft studio lighting on a
    beige pedestal", "isolated on a marble surface"
    """

    resolution: Literal["1k", "2k", "4k"]
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
    """Controls generation randomness on a best-effort basis.

    Exact reproducibility is not guaranteed.
    """


PredictionRunParams: TypeAlias = Union[
    TryOnMaxRequest,
    TryOnRequest,
    ProductToModelRequest,
    FaceToModelRequest,
    ModelCreateRequest,
    ModelSwapRequest,
    ReframeRequest,
    BackgroundChangeRequest,
    BackgroundRemoveRequest,
    ImageToVideoRequest,
    EditRequest,
    PackshotRequest,
]
