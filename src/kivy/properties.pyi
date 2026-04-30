from typing import Any, Generic, TypeVar

T = TypeVar("T")

class Property(Generic[T]):
    def __init__(
        self,
        defaultvalue: T | None = None,
        *,
        rebind: bool = False,
        **kwargs: Any,
    ) -> None: ...

class ObjectProperty(Property[T], Generic[T]):
    def __init__(
        self,
        defaultvalue: T | None = None,
        *,
        rebind: bool = False,
        allownone: bool = False,
        **kwargs: Any,
    ) -> None: ...

class StringProperty(Property[str]):
    def __init__(
        self,
        defaultvalue: str = "",
        *,
        rebind: bool = False,
        allownone: bool = False,
        **kwargs: Any,
    ) -> None: ...

class NumericProperty(Property[float]):
    def __init__(
        self,
        defaultvalue: float = 0,
        *,
        rebind: bool = False,
        allownone: bool = False,
        **kwargs: Any,
    ) -> None: ...

class BooleanProperty(Property[bool]):
    def __init__(
        self,
        defaultvalue: bool = False,
        *,
        rebind: bool = False,
        allownone: bool = False,
        **kwargs: Any,
    ) -> None: ...

class ListProperty(Property[list[Any]]):
    def __init__(
        self,
        defaultvalue: list[Any] | None = None,
        *,
        rebind: bool = False,
        **kwargs: Any,
    ) -> None: ...

class DictProperty(Property[dict[Any, Any]]):
    def __init__(
        self,
        defaultvalue: dict[Any, Any] | None = None,
        *,
        rebind: bool = False,
        **kwargs: Any,
    ) -> None: ...

class OptionProperty(Property[str]):
    def __init__(
        self,
        defaultvalue: str | None = None,
        *,
        options: list[str] | tuple[str, ...],
        rebind: bool = False,
        **kwargs: Any,
    ) -> None: ...

class AliasProperty(Property[T], Generic[T]):
    def __init__(
        self,
        getter: Any,
        setter: Any | None = None,
        *,
        bind: list[str] | tuple[str, ...] | None = None,
        cache: bool = False,
        rebind: bool = False,
        **kwargs: Any,
    ) -> None: ...

class ReferenceListProperty(Property[tuple[Any, ...]]):
    def __init__(
        self,
        *properties: Property[Any],
        **kwargs: Any,
    ) -> None: ...

class ColorProperty(Property[list[float]]):
    def __init__(
        self,
        defaultvalue: list[float] | tuple[float, ...] | str | None = None,
        *,
        rebind: bool = False,
        allownone: bool = False,
        **kwargs: Any,
    ) -> None: ...

class VariableListProperty(Property[list[float]]):
    def __init__(
        self,
        defaultvalue: list[float] | tuple[float, ...] | None = None,
        *,
        length: int | None = None,
        options: list[int] | tuple[int, ...] | None = None,
        rebind: bool = False,
        **kwargs: Any,
    ) -> None: ...
