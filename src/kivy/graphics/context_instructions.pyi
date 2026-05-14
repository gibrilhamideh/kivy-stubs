from __future__ import annotations

from typing import Any

from kivy.graphics.instructions import ContextInstruction


def gl_init_resources() -> None: ...


class Color(ContextInstruction):
    r: float
    g: float
    b: float
    a: float
    rgba: tuple[float, float, float, float]
    hsv: tuple[float, float, float]

    def __init__(
        self,
        r: float = 1.0,
        g: float = 1.0,
        b: float = 1.0,
        a: float = 1.0,
        **kwargs: Any,
    ) -> None: ...


class BindTexture(ContextInstruction):
    texture: Any
    index: int
    source: str

    def __init__(
        self,
        texture: Any = None,
        index: int = 0,
        source: str = "",
        **kwargs: Any,
    ) -> None: ...


class PushState(ContextInstruction):
    states: tuple[str, ...]

    def __init__(self, *states: str, **kwargs: Any) -> None: ...


class ChangeState(ContextInstruction):
    def __init__(self, **kwargs: Any) -> None: ...


class PopState(ContextInstruction):
    states: tuple[str, ...]

    def __init__(self, *states: str, **kwargs: Any) -> None: ...


class MatrixInstruction(ContextInstruction):
    matrix: Any

    def __init__(self, **kwargs: Any) -> None: ...


class PushMatrix(ContextInstruction):
    stack: str

    def __init__(
        self,
        stack: str = "modelview_mat",
        **kwargs: Any,
    ) -> None: ...


class PopMatrix(ContextInstruction):
    stack: str

    def __init__(
        self,
        stack: str = "modelview_mat",
        **kwargs: Any,
    ) -> None: ...


class Rotate(MatrixInstruction):
    angle: float
    axis: tuple[float, float, float]
    origin: tuple[float, float]

    def __init__(
        self,
        angle: float = 0.0,
        axis: tuple[float, float, float] = (0.0, 0.0, 1.0),
        origin: tuple[float, float] = (0.0, 0.0),
        **kwargs: Any,
    ) -> None: ...


class Scale(MatrixInstruction):
    x: float
    y: float
    z: float
    origin: tuple[float, float, float]

    def __init__(
        self,
        x: float = 1.0,
        y: float = 1.0,
        z: float = 1.0,
        origin: tuple[float, float, float] = (0.0, 0.0, 0.0),
        **kwargs: Any,
    ) -> None: ...


class Translate(MatrixInstruction):
    x: float
    y: float
    z: float

    def __init__(
        self,
        x: float = 0.0,
        y: float = 0.0,
        z: float = 0.0,
        **kwargs: Any,
    ) -> None: ...


class LoadIdentity(ContextInstruction):
    stack: str

    def __init__(
        self,
        stack: str = "modelview_mat",
        **kwargs: Any,
    ) -> None: ...


class ApplyContextMatrix(ContextInstruction):
    target_stack: str
    source_stack: str

    def __init__(
        self,
        target_stack: str = "modelview_mat",
        source_stack: str = "frag_modelview_mat",
        **kwargs: Any,
    ) -> None: ...


class UpdateNormalMatrix(ContextInstruction):
    def __init__(self, **kwargs: Any) -> None: ...
