from __future__ import annotations

from typing import Any


class Texture:
    width: int
    height: int
    size: tuple[int, int]

    @classmethod
    def create(cls, **kwargs: Any) -> Texture: ...

    def blit_buffer(self, *args: Any, **kwargs: Any) -> None: ...
    def flip_vertical(self) -> None: ...
    def ask_update(self) -> None: ...
