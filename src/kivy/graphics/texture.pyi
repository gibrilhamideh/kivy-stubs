# texture.pyi

from __future__ import annotations

from typing import Any, Callable, Literal

ColorFormat = Literal[
    "rgb",
    "rgba",
    "bgr",
    "bgra",
    "luminance",
    "luminance_alpha",
    "red",
    "rg",
]

InternalColorFormat = Literal[
    "rgb",
    "rgba",
    "luminance",
    "luminance_alpha",
    "r8",
    "rg8",
    "rgba8",
]

BufferFormat = Literal[
    "ubyte",
    "ushort",
    "uint",
    "byte",
    "short",
    "int",
    "float",
]

MinFilter = Literal[
    "linear",
    "nearest",
    "linear_mipmap_linear",
    "linear_mipmap_nearest",
    "nearest_mipmap_nearest",
    "nearest_mipmap_linear",
]

MagFilter = Literal[
    "linear",
    "nearest",
]

WrapMode = Literal[
    "repeat",
    "mirrored_repeat",
    "clamp_to_edge",
]


class Texture:
    width: int
    height: int
    size: tuple[int, int]

    target: int
    id: int

    mipmap: bool

    colorfmt: str
    bufferfmt: str

    tex_coords: list[float]

    uvpos: tuple[float, float]
    uvsize: tuple[float, float]

    pixels: bytes

    min_filter: MinFilter
    mag_filter: MagFilter

    wrap: WrapMode

    @staticmethod
    def create(
        size: tuple[int, int] | None = ...,
        colorfmt: ColorFormat | None = ...,
        bufferfmt: BufferFormat | None = ...,
        mipmap: bool = ...,
        callback: Callable[..., Any] | None = ...,
        icolorfmt: InternalColorFormat | None = ...,
    ) -> Texture: ...

    @staticmethod
    def create_from_data(
        im: Any,
        mipmap: bool = ...,
    ) -> Texture: ...

    def bind(self) -> None: ...

    def ask_update(
        self,
        callback: Callable[..., Any],
    ) -> None: ...

    def add_reload_observer(
        self,
        callback: Callable[..., Any],
    ) -> None: ...

    def remove_reload_observer(
        self,
        callback: Callable[..., Any],
    ) -> None: ...

    def blit_buffer(
        self,
        pbuffer: bytes | memoryview | Any,
        size: tuple[int, int] | None = ...,
        colorfmt: ColorFormat | None = ...,
        pos: tuple[int, int] | None = ...,
        bufferfmt: BufferFormat | None = ...,
        mipmap_level: int = ...,
        mipmap_generation: bool = ...,
        rowlength: int = ...,
    ) -> None: ...

    def blit_data(
        self,
        im: Any,
        pos: tuple[int, int] | None = ...,
    ) -> None: ...

    def flip_horizontal(self) -> None: ...

    def flip_vertical(self) -> None: ...

    def get_region(
        self,
        x: int,
        y: int,
        width: int,
        height: int,
    ) -> TextureRegion: ...

    def save(
        self,
        filename: str | Any,
        flipped: bool = ...,
        fmt: str | None = ...,
    ) -> bool: ...


class TextureRegion(Texture):
    pass
