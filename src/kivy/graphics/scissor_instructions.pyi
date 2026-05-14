from __future__ import annotations

from typing import Any

from kivy.graphics.instructions import ContextInstruction


class ScissorPush(ContextInstruction):
    x: int
    y: int
    width: int
    height: int

    def __init__(
        self,
        x: int = 0,
        y: int = 0,
        width: int = 0,
        height: int = 0,
        **kwargs: Any,
    ) -> None: ...


class ScissorPop(ContextInstruction):
    def __init__(self, **kwargs: Any) -> None: ...
