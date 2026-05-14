from __future__ import annotations

from typing import Any

from kivy.graphics.instructions import Instruction


class StencilPush(Instruction):
    def __init__(self, **kwargs: Any) -> None: ...


class StencilUse(Instruction):
    def __init__(self, **kwargs: Any) -> None: ...


class StencilUnUse(Instruction):
    def __init__(self, **kwargs: Any) -> None: ...


class StencilPop(Instruction):
    def __init__(self, **kwargs: Any) -> None: ...
