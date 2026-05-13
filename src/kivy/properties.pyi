from __future__ import annotations

from typing import Any, Callable

class Property:
    def __new__(
        cls,
        defaultvalue: Any = None,
        *,
        rebind: bool = False,
        **kwargs: Any,
    ) -> Any: ...

class ObjectProperty(Property):
    def __new__(
        cls,
        defaultvalue: Any = None,
        *,
        rebind: bool = False,
        allownone: bool = False,
        **kwargs: Any,
    ) -> Any: ...

class StringProperty(Property):
    def __new__(
        cls,
        defaultvalue: str | None = "",
        *,
        rebind: bool = False,
        allownone: bool = False,
        **kwargs: Any,
    ) -> Any: ...

class NumericProperty(Property):
    def __new__(
        cls,
        defaultvalue: int | float | None = 0,
        *,
        rebind: bool = False,
        allownone: bool = False,
        **kwargs: Any,
    ) -> Any: ...

class BooleanProperty(Property):
    def __new__(
        cls,
        defaultvalue: bool | None = False,
        *,
        rebind: bool = False,
        allownone: bool = False,
        **kwargs: Any,
    ) -> Any: ...

class ListProperty(Property):
    def __new__(
        cls,
        defaultvalue: list[Any] | tuple[Any, ...] | None = None,
        *,
        rebind: bool = False,
        **kwargs: Any,
    ) -> Any: ...

class DictProperty(Property):
    def __new__(
        cls,
        defaultvalue: dict[Any, Any] | None = None,
        *,
        rebind: bool = False,
        **kwargs: Any,
    ) -> Any: ...

class OptionProperty(Property):
    def __new__(
        cls,
        defaultvalue: Any = None,
        *,
        options: list[Any] | tuple[Any, ...],
        rebind: bool = False,
        **kwargs: Any,
    ) -> Any: ...

class AliasProperty(Property):
    def __new__(
        cls,
        getter: Callable[..., Any],
        setter: Callable[..., Any] | None = None,
        *,
        bind: list[str] | tuple[str, ...] | None = None,
        cache: bool = False,
        rebind: bool = False,
        watch_before_use: bool = True,
        **kwargs: Any,
    ) -> Any: ...

class ReferenceListProperty(Property):
    def __new__(
        cls,
        *properties: Any,
        **kwargs: Any,
    ) -> Any: ...

class VariableListProperty(Property):
    def __new__(
        cls,
        defaultvalue: list[Any] | tuple[Any, ...] | None = None,
        *,
        length: int | None = None,
        options: list[int] | tuple[int, ...] | None = None,
        rebind: bool = False,
        **kwargs: Any,
    ) -> Any: ...

class ColorProperty(Property):
    def __new__(
        cls,
        defaultvalue: list[float] | tuple[float, ...] | str | None = None,
        *,
        rebind: bool = False,
        allownone: bool = False,
        **kwargs: Any,
    ) -> Any: ...

class BoundedNumericProperty(NumericProperty):
    def __new__(
        cls,
        defaultvalue: int | float | None = 0,
        *,
        min: int | float | None = None,
        max: int | float | None = None,
        errorvalue: int | float | None = None,
        errorhandler: Callable[[Any], int | float] | None = None,
        rebind: bool = False,
        allownone: bool = False,
        **kwargs: Any,
    ) -> Any: ...
