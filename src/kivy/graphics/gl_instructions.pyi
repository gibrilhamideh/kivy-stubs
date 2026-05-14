from __future__ import annotations

from typing import Any

from kivy.graphics.instructions import Instruction


class ClearColor(Instruction):
    r: float
    g: float
    b: float
    a: float
    rgba: tuple[float, float, float, float]

    def __init__(
        self,
        r: float = 0.0,
        g: float = 0.0,
        b: float = 0.0,
        a: float = 0.0,
        **kwargs: Any,
    ) -> None: ...


class ClearBuffers(Instruction):
    clear_color: bool
    clear_depth: bool
    clear_stencil: bool

    def __init__(
        self,
        clear_color: bool = True,
        clear_depth: bool = False,
        clear_stencil: bool = False,
        **kwargs: Any,
    ) -> None: ...
