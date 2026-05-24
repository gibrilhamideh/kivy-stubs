from __future__ import annotations

from io import BytesIO
from typing import Any, ClassVar, Iterable, overload

from kivy.event import EventDispatcher
from kivy.graphics.texture import Texture, TextureRegion


class ImageData:
    fmt: str
    mipmaps: dict[int, list[Any]]
    source: str | None
    flip_vertical: bool
    source_image: Any

    _supported_fmts: ClassVar[tuple[str, ...]]

    def __init__(
        self,
        width: int,
        height: int,
        fmt: str,
        data: Any,
        source: str | None = ...,
        flip_vertical: bool = ...,
        source_image: Any = ...,
        rowlength: int = ...,
    ) -> None: ...

    @property
    def width(self) -> int: ...

    @property
    def height(self) -> int: ...

    @property
    def data(self) -> Any: ...

    @property
    def rowlength(self) -> int: ...

    @property
    def size(self) -> tuple[int, int]: ...

    @property
    def have_mipmap(self) -> bool: ...

    def release_data(self) -> None: ...

    def add_mipmap(
        self,
        level: int,
        width: int,
        height: int,
        data: Any,
        rowlength: int,
    ) -> None: ...

    def get_mipmap(self, level: int) -> list[Any] | tuple[int, int, Any, int]: ...

    def iterate_mipmaps(self) -> Iterable[tuple[int, int, int, Any, int]]: ...


class ImageLoaderBase:
    _provider_name: ClassVar[str | None]

    filename: str
    keep_data: bool

    def __init__(self, filename: str, **kwargs: Any) -> None: ...

    def load(self, filename: str) -> list[ImageData] | None: ...

    @staticmethod
    def can_save(fmt: str | None, is_bytesio_like: bool = ...) -> bool: ...

    @staticmethod
    def can_load_memory() -> bool: ...

    @staticmethod
    def save(*largs: Any, **kwargs: Any) -> Any: ...

    def populate(self) -> None: ...

    @property
    def width(self) -> int: ...

    @property
    def height(self) -> int: ...

    @property
    def size(self) -> tuple[int, int]: ...

    @property
    def texture(self) -> Texture | None: ...

    @property
    def textures(self) -> list[Texture]: ...

    @property
    def nocache(self) -> bool: ...


class ImageLoader:
    loaders: ClassVar[list[type[ImageLoaderBase]]]
    loaders_by_name: ClassVar[dict[str, type[ImageLoaderBase]]]

    @staticmethod
    def zip_loader(filename: str, **kwargs: Any) -> ImageLoaderBase: ...

    @staticmethod
    def register(defcls: type[ImageLoaderBase]) -> None: ...

    @staticmethod
    def load(filename: str, **kwargs: Any) -> ImageLoaderBase | Image | Texture | None: ...


class Image(EventDispatcher):
    copy_attributes: ClassVar[tuple[str, ...]]
    data_uri_re: ClassVar[Any]

    anim_delay: float

    @overload
    def __init__(self, arg: str, **kwargs: Any) -> None: ...

    @overload
    def __init__(self, arg: BytesIO, **kwargs: Any) -> None: ...

    @overload
    def __init__(self, arg: Image, **kwargs: Any) -> None: ...

    @overload
    def __init__(self, arg: ImageLoaderBase, **kwargs: Any) -> None: ...

    @overload
    def __init__(self, arg: Texture | TextureRegion, **kwargs: Any) -> None: ...

    def remove_from_cache(self) -> None: ...

    def anim_reset(self, allow_anim: bool) -> None: ...

    @property
    def anim_available(self) -> bool: ...

    @property
    def anim_index(self) -> int: ...

    def on_texture(self, *largs: Any) -> None: ...

    @staticmethod
    def load(filename: str, **kwargs: Any) -> Image: ...

    @staticmethod
    def available_providers() -> list[str]: ...

    @property
    def image(self) -> ImageLoaderBase | Image | None: ...

    @image.setter
    def image(self, image: ImageLoaderBase | Image | None) -> None: ...

    @property
    def filename(self) -> str | None: ...

    @filename.setter
    def filename(self, value: str | None) -> None: ...

    def load_memory(
        self,
        data: BytesIO,
        ext: str,
        filename: str = ...,
    ) -> None: ...

    @property
    def size(self) -> tuple[int, int]: ...

    @property
    def width(self) -> int: ...

    @property
    def height(self) -> int: ...

    @property
    def texture(self) -> Texture | None: ...

    @property
    def nocache(self) -> bool: ...

    def save(
        self,
        filename: str | BytesIO,
        flipped: bool = ...,
        fmt: str | None = ...,
    ) -> bool: ...

    def read_pixel(self, x: int, y: int) -> list[float]: ...


def load(filename: str) -> Image: ...
