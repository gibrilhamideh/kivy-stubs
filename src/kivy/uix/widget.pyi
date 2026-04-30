# src/kivy/uix/widget.pyi

from __future__ import annotations

from collections.abc import Generator
from typing import Any, ClassVar, Literal

from kivy.event import EventDispatcher

__all__: tuple[str, str]

CanvasMode = Literal["before", "after"] | None
Coordinate = tuple[float, float]
SizeHint = tuple[float | None, float | None]
PosHint = dict[str, float]
MotionFilter = dict[str, list[Widget]]

class WidgetException(Exception):
    pass

class WidgetMetaclass(type):
    def __init__(
        cls,
        name: str,
        bases: tuple[type, ...],
        attrs: dict[str, Any],
    ) -> None: ...

class Widget(EventDispatcher):
    __events__: ClassVar[
        tuple[
            Literal["on_motion"],
            Literal["on_touch_down"],
            Literal["on_touch_move"],
            Literal["on_touch_up"],
            Literal["on_kv_post"],
        ]
    ]

    # ------------------------------------------------------------
    # Basic geometry
    # ------------------------------------------------------------

    x: float
    y: float
    width: float
    height: float

    pos: Coordinate
    size: Coordinate

    right: float
    top: float

    center_x: float
    center_y: float
    center: Coordinate

    # ------------------------------------------------------------
    # Tree / layout
    # ------------------------------------------------------------

    cls: list[str]
    children: list[Widget]
    parent: Widget | None

    size_hint_x: float | None
    size_hint_y: float | None
    size_hint: SizeHint

    pos_hint: PosHint

    size_hint_min_x: float | None
    size_hint_min_y: float | None
    size_hint_min: SizeHint

    size_hint_max_x: float | None
    size_hint_max_y: float | None
    size_hint_max: SizeHint

    ids: dict[str, Any]

    # ------------------------------------------------------------
    # Graphics / state
    # ------------------------------------------------------------

    opacity: float
    canvas: Any
    disabled: bool

    # Kivy stores motion type id -> widgets registered for that motion type.
    motion_filter: MotionFilter

    # Weak proxy to self.
    proxy_ref: Any

    def __init__(self, **kwargs: Any) -> None: ...
    def __hash__(self) -> int: ...

    # ------------------------------------------------------------
    # KV / class rules
    # ------------------------------------------------------------

    def apply_class_lang_rules(
        self,
        root: Widget | None = None,
        ignored_consts: set[Any] = ...,
        rule_children: list[Widget] | None = None,
    ) -> None: ...

    # ------------------------------------------------------------
    # Collision
    # ------------------------------------------------------------

    def collide_point(self, x: float, y: float) -> bool: ...
    def collide_widget(self, wid: Widget) -> bool: ...

    # ------------------------------------------------------------
    # Motion / touch events
    # ------------------------------------------------------------

    def on_motion(self, etype: str, me: Any) -> bool | None: ...
    def on_touch_down(self, touch: Any) -> bool | None: ...
    def on_touch_move(self, touch: Any) -> bool | None: ...
    def on_touch_up(self, touch: Any) -> bool | None: ...
    def on_kv_post(self, base_widget: Widget) -> None: ...

    # ------------------------------------------------------------
    # Tree management
    # ------------------------------------------------------------

    def add_widget(
        self,
        widget: Widget,
        index: int = 0,
        canvas: CanvasMode = None,
    ) -> None: ...
    def remove_widget(self, widget: Widget) -> None: ...
    def clear_widgets(
        self,
        children: list[Widget] | None = None,
    ) -> None: ...

    # ------------------------------------------------------------
    # Motion event registration
    # ------------------------------------------------------------

    def register_for_motion_event(
        self,
        type_id: str,
        widget: Widget | None = None,
    ) -> None: ...
    def unregister_for_motion_event(
        self,
        type_id: str,
        widget: Widget | None = None,
    ) -> None: ...

    # Internal but useful for subclasses overriding behavior.
    def _update_motion_filter(
        self,
        child_widget: Widget,
        child_motion_filter: MotionFilter,
    ) -> None: ...
    def _find_index_in_motion_filter(
        self,
        type_id: str,
        widget: Widget,
    ) -> int: ...

    # ------------------------------------------------------------
    # Export / rendering helpers
    # ------------------------------------------------------------

    def export_to_png(
        self,
        filename: str,
        *args: Any,
        **kwargs: Any,
    ) -> None: ...
    def export_as_image(
        self,
        *args: Any,
        **kwargs: Any,
    ) -> Any: ...

    # ------------------------------------------------------------
    # Window helpers
    # ------------------------------------------------------------

    def get_root_window(self) -> Any: ...
    def get_parent_window(self) -> Any: ...

    # ------------------------------------------------------------
    # Tree walking
    # ------------------------------------------------------------

    def _walk(
        self,
        restrict: bool = False,
        loopback: bool = False,
        index: int | None = None,
    ) -> Generator[Widget, None, None]: ...
    def walk(
        self,
        restrict: bool = False,
        loopback: bool = False,
    ) -> Generator[Widget, None, None]: ...
    def _walk_reverse(
        self,
        loopback: bool = False,
        go_up: bool = False,
    ) -> Generator[Widget, None, None]: ...
    def walk_reverse(
        self,
        loopback: bool = False,
    ) -> Generator[Widget, None, None]: ...

    # ------------------------------------------------------------
    # Coordinate transforms
    # ------------------------------------------------------------

    def to_widget(
        self,
        x: float,
        y: float,
        relative: bool = False,
    ) -> Coordinate: ...
    def to_window(
        self,
        x: float,
        y: float,
        initial: bool = True,
        relative: bool = False,
    ) -> Coordinate: ...
    def to_parent(
        self,
        x: float,
        y: float,
        relative: bool = False,
    ) -> Coordinate: ...
    def to_local(
        self,
        x: float,
        y: float,
        relative: bool = False,
    ) -> Coordinate: ...
    def _apply_transform(
        self,
        m: Any,
        pos: Coordinate | None = None,
    ) -> Any: ...
    def get_window_matrix(
        self,
        x: float = 0,
        y: float = 0,
    ) -> Any: ...

    # ------------------------------------------------------------
    # AliasProperty backing methods
    # ------------------------------------------------------------

    def get_right(self) -> float: ...
    def set_right(self, value: float) -> None: ...
    def get_top(self) -> float: ...
    def set_top(self, value: float) -> None: ...
    def get_center_x(self) -> float: ...
    def set_center_x(self, value: float) -> None: ...
    def get_center_y(self) -> float: ...
    def set_center_y(self, value: float) -> None: ...
    def get_disabled(self) -> bool: ...
    def set_disabled(self, value: bool) -> None: ...
    def inc_disabled(self, count: int = 1) -> None: ...
    def dec_disabled(self, count: int = 1) -> None: ...
    def on_opacity(self, instance: Widget, value: float) -> None: ...
