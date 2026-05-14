from __future__ import annotations

from typing import Any

from kivy.graphics.vertex_instructions import Rectangle


class BoxShadow(Rectangle):
    blur_radius: float
    border_radius: list[float]
    offset: tuple[float, float]
    spread_radius: tuple[float, float]
    inset: bool

    def __init__(
        self,
        *,
        blur_radius: float = 15.0,
        border_radius: list[float] | tuple[float, ...] | None = None,
        offset: tuple[float, float] = (0.0, 0.0),
        spread_radius: tuple[float, float] = (0.0, 0.0),
        inset: bool = False,
        **kwargs: Any,
    ) -> None: ...
