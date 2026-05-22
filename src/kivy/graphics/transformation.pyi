# kivy/graphics/transformation.pyi

from __future__ import annotations

from typing import Sequence


class Matrix:
    def __init__(self) -> None: ...

    def __repr__(self) -> str: ...

    def get(self) -> list[float]: ...

    def identity(self) -> Matrix: ...

    def inverse(self) -> Matrix: ...

    def look_at(
        self,
        eyex: float,
        eyey: float,
        eyez: float,
        centerx: float,
        centery: float,
        centerz: float,
        upx: float,
        upy: float,
        upz: float,
    ) -> Matrix: ...

    def multiply(
        self,
        ma: Matrix,
    ) -> Matrix: ...

    def normal_matrix(self) -> Matrix: ...

    def perspective(
        self,
        fovy: float,
        aspect: float,
        zNear: float,
        zFar: float,
    ) -> Matrix: ...

    def project(
        self,
        objx: float,
        objy: float,
        objz: float,
        model: Matrix,
        proj: Matrix,
        vx: float,
        vy: float,
        vw: float,
        vh: float,
    ) -> tuple[float, float, float]: ...

    def rotate(
        self,
        angle: float,
        x: float,
        y: float,
        z: float,
    ) -> Matrix: ...

    def scale(
        self,
        x: float,
        y: float,
        z: float,
    ) -> Matrix: ...

    def set(
        self,
        flat: Sequence[float] | None = None,
        array: Sequence[Sequence[float]] | None = None,
    ) -> None: ...

    def tolist(self) -> list[list[float]]: ...

    def transform_point(
        self,
        x: float,
        y: float,
        z: float,
        t: float | None = None,
    ) -> tuple[float, float, float] | tuple[float, float, float, float]: ...

    def translate(
        self,
        x: float,
        y: float,
        z: float,
    ) -> Matrix: ...

    def transpose(self) -> Matrix: ...

    def view_clip(
        self,
        left: float,
        right: float,
        bottom: float,
        top: float,
        near: float,
        far: float,
        perspective: int,
    ) -> Matrix: ...
