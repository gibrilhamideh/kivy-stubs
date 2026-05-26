from __future__ import annotations

from collections.abc import Callable
from typing import Any, TypeAlias

from kivy.graphics.instructions import RenderContext
from kivy.graphics.texture import Texture


ColorRGBA: TypeAlias = tuple[float, float, float, float]
Size: TypeAlias = tuple[int, int]
ReloadCallback: TypeAlias = Callable[["Fbo"], None]


class Fbo(RenderContext):
    texture: Texture
    clear_color: ColorRGBA
    size: Size
    pixels: bytes

    def __init__(
        self,
        *args: Any,
        clear_color: ColorRGBA = (0, 0, 0, 0),
        size: Size = (1024, 1024),
        push_viewport: bool = True,
        with_depthbuffer: bool = False,
        with_stencilbuffer: bool = False,
        texture: Texture | None = None,
        **kwargs: Any,
    ) -> None: ...

    def bind(self) -> None: ...

    def release(self) -> None: ...

    def clear_buffer(self) -> None: ...

    def get_pixel_color(
        self,
        wx: int,
        wy: int,
    ) -> ColorRGBA: ...

    def add_reload_observer(
        self,
        callback: ReloadCallback,
    ) -> None: ...

    def remove_reload_observer(
        self,
        callback: ReloadCallback,
    ) -> None: ...
