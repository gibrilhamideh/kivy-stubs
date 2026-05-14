from __future__ import annotations

from typing import Any, Callable, Iterator
from weakref import ProxyType

from kivy.event import ObjectWithUid


class Instruction(ObjectWithUid):
    group: str
    proxy_ref: ProxyType[Instruction]

    def __init__(self, **kwargs: Any) -> None: ...
    def flag_update(self, do_parent: int = 1) -> None: ...
    def flag_data_update(self) -> None: ...


class ContextInstruction(Instruction):
    pass


class VertexInstruction(Instruction):
    source: str
    tex_coords: list[float]
    texture: Any

    def __init__(self, **kwargs: Any) -> None: ...


class InstructionGroup(Instruction):
    children: list[Instruction]

    def __init__(self, **kwargs: Any) -> None: ...
    def add(self, c: Instruction) -> None: ...
    def insert(self, index: int, c: Instruction) -> None: ...
    def remove(self, c: Instruction) -> None: ...
    def clear(self) -> None: ...
    def length(self) -> int: ...
    def indexof(self, c: Instruction) -> int: ...
    def get_group(self, groupname: str) -> list[Instruction]: ...
    def remove_group(self, groupname: str) -> None: ...


class CanvasBase(InstructionGroup):
    def __enter__(self) -> CanvasBase: ...
    def __exit__(self, *args: Any) -> None: ...


class Canvas(CanvasBase):
    before: CanvasBase
    after: CanvasBase
    has_before: bool
    has_after: bool
    opacity: float

    def __init__(self, **kwargs: Any) -> None: ...
    def add(self, c: Instruction) -> None: ...
    def remove(self, c: Instruction) -> None: ...
    def clear(self) -> None: ...
    def draw(self) -> None: ...
    def ask_update(self) -> None: ...


class RenderContext(Canvas):
    shader: Any
    use_parent_modelview: bool
    use_parent_projection: bool
    use_parent_frag_modelview: bool

    def __init__(self, *args: Any, **kwargs: Any) -> None: ...


class Callback(Instruction):
    callback: Callable[[Callback], Any] | None
    reset_context: bool

    def __init__(
        self,
        callback: Callable[[Callback], Any] | None = None,
        **kwargs: Any,
    ) -> None: ...

    def ask_update(self) -> None: ...
