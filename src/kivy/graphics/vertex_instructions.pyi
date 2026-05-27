from __future__ import annotations

from typing import Any, Sequence
from numpy.typing import NDArray
import numpy as np

from kivy.graphics.instructions import VertexInstruction



class GraphicException(Exception):
    pass


class Rectangle(VertexInstruction):
    pos: tuple[float, float]
    size: tuple[float, float]
    texture: Any
    source: str

    def __init__(
        self,
        *,
        pos: tuple[float, float] = (0.0, 0.0),
        size: tuple[float, float] = (100.0, 100.0),
        source: str = "",
        texture: Any = None,
        **kwargs: Any,
    ) -> None: ...


class RoundedRectangle(Rectangle):
    radius: Sequence[float]


class BorderImage(Rectangle):
    border: Sequence[float]


class Ellipse(Rectangle):
    angle_start: float
    angle_end: float
    segments: int


class Line(VertexInstruction):
    points: list[float]
    width: float
    close: bool
    dash_length: float
    dash_offset: float
    cap: str
    joint: str

    def __init__(
        self,
        *,
        points: Sequence[float] | None = None,
        width: float = 1.0,
        close: bool = False,
        **kwargs: Any,
    ) -> None: ...


class SmoothLine(Line):
    pass


class Bezier(Line):
    segments: int
    loop: bool


class Mesh(VertexInstruction):
    vertices: Sequence[float] | NDArray[np.float32]
    indices: Sequence[int] | NDArray[np.uint16]
    mode: str
    fmt: Any

    def __init__(
        self,
        *,
        vertices: Sequence[float] | NDArray[np.float32],
        indices: Sequence[int] | NDArray[np.uint16],
        mode: str = "triangles",
        **kwargs: Any,
    ) -> None: ...


class Point(VertexInstruction):
    points: list[float]
    pointsize: float

    def __init__(
        self,
        *,
        points: Sequence[float] | None = None,
        pointsize: float = 1.0,
        **kwargs: Any,
    ) -> None: ...


class Quad(VertexInstruction):
    points: Sequence[float]

    def __init__(
        self,
        *,
        points: Sequence[float],
        **kwargs: Any,
    ) -> None: ...


class Triangle(VertexInstruction):
    points: Sequence[float]

    def __init__(
        self,
        *,
        points: Sequence[float],
        **kwargs: Any,
    ) -> None: ...


class SmoothRectangle(Rectangle):
    pass


class SmoothEllipse(Ellipse):
    pass


class SmoothRoundedRectangle(RoundedRectangle):
    pass


class SmoothQuad(Quad):
    pass


class SmoothTriangle(Triangle):
    pass
