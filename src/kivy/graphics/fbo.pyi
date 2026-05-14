from __future__ import annotations

from typing import Any

from kivy.graphics.instructions import Canvas
from kivy.graphics.texture import Texture


class Fbo(Canvas):
    texture: Texture
    clear_color: tuple[float, float, float, float]
    size: tuple[float, float]
    pixels: bytes

    def __init__(
        self,
        size: tuple[float, float] = (1024, 1024),
        with_stencilbuffer: bool = False,
        texture: Texture | None = None,
        **kwargs: Any,
    ) -> None: ...

    def bind(self) -> None: ...
    def release(self) -> None: ...
    def clear_buffer(self) -> None: ...
    def draw(self) -> None: ...
    def ask_update(self) -> None: ...
    def get_pixel_color(self, wx: int, wy: int) -> Any: ...
