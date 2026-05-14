# src/kivy/event.pyi

from typing import Any, Callable

class ObjectWithUid:
    uid: int

    def __init__(self, **kwargs: Any) -> None: ...

class EventDispatcher:
    def __init__(self, **kwargs: Any) -> None: ...
    def bind(self, **kwargs: Callable[..., Any]) -> None: ...
    def fbind(
        self,
        name: str,
        func: Callable[..., Any],
        *args: Any,
        **kwargs: Any,
    ) -> int: ...
    def unbind(self, **kwargs: Callable[..., Any]) -> None: ...
    def funbind(
        self,
        name: str,
        func: Callable[..., Any],
        *args: Any,
        **kwargs: Any,
    ) -> None: ...
    def dispatch(
        self,
        event_type: str,
        *args: Any,
        **kwargs: Any,
    ) -> Any: ...
    def property(self, name: str, quiet: bool = False) -> Any: ...
    def setter(self, name: str) -> Callable[[Any, Any], None]: ...
    def getter(self, name: str) -> Callable[[Any], Any]: ...
