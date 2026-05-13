from __future__ import annotations

from collections.abc import Callable
from typing import Any, Concatenate, Generic, ParamSpec, Protocol, TypeAlias, TypeVar, overload

_P = ParamSpec("_P")
_R = TypeVar("_R")
_T = TypeVar("_T")

ClockCallback: TypeAlias = Callable[[float], Any]
ClockEndedCallback: TypeAlias = Callable[[Any], Any]


class ClockNotRunningError(RuntimeError):
    ...


class ClockEvent:
    callback: Callable[..., Any] | None
    clock_ended_callback: Callable[..., Any] | None
    cid: int
    timeout: float
    loop: bool
    free: bool
    weak_callback: Any
    weak_clock_ended_callback: Any
    is_triggered: bool

    def __call__(self, *largs: Any) -> None:
        ...

    def cancel(self) -> None:
        ...

    def release(self) -> None:
        ...

    def tick(self, curtime: float) -> bool:
        ...

    def get_callback(self) -> Callable[..., Any] | None:
        ...

    def get_clock_ended_callback(self) -> Callable[..., Any] | None:
        ...


class FreeClockEvent(ClockEvent):
    ...


class CyClockBase:
    max_iteration: int

    def schedule_once(
        self,
        callback: ClockCallback,
        timeout: float = 0,
    ) -> ClockEvent:
        ...

    def schedule_interval(
        self,
        callback: ClockCallback,
        timeout: float,
    ) -> ClockEvent:
        ...

    def create_trigger(
        self,
        callback: ClockCallback,
        timeout: float = 0,
        interval: bool = False,
        release_ref: bool = True,
    ) -> ClockEvent:
        ...

    def create_lifecycle_aware_trigger(
        self,
        callback: ClockCallback,
        clock_ended_callback: ClockEndedCallback,
        timeout: float = 0,
        interval: bool = False,
        release_ref: bool = True,
    ) -> ClockEvent:
        ...

    def schedule_del_safe(
        self,
        callback: Callable[..., Any],
    ) -> None:
        ...

    def schedule_lifecycle_aware_del_safe(
        self,
        callback: Callable[..., Any],
        clock_ended_callback: Callable[..., Any],
    ) -> None:
        ...

    def unschedule(
        self,
        callback: ClockEvent | Callable[..., Any],
        all: bool = True,
    ) -> None:
        ...

    def get_events(self) -> list[ClockEvent]:
        ...

    def get_before_frame_events(self) -> list[ClockEvent]:
        ...

    def get_min_timeout(self) -> float | None:
        ...

    def _process_events(self) -> None:
        ...

    def _process_events_before_frame(self) -> None:
        ...

    def _release_references(self) -> None:
        ...

    def on_schedule(self, event: ClockEvent) -> None:
        ...

    def get_resolution(self) -> float:
        ...


class CyClockBaseFree(CyClockBase):
    def schedule_once_free(
        self,
        callback: ClockCallback,
        timeout: float = 0,
    ) -> FreeClockEvent:
        ...

    def schedule_interval_free(
        self,
        callback: ClockCallback,
        timeout: float,
    ) -> FreeClockEvent:
        ...

    def create_trigger_free(
        self,
        callback: ClockCallback,
        timeout: float = 0,
        interval: bool = False,
        release_ref: bool = True,
    ) -> FreeClockEvent:
        ...

    def create_lifecycle_aware_trigger_free(
        self,
        callback: ClockCallback,
        clock_ended_callback: ClockEndedCallback,
        timeout: float = 0,
        interval: bool = False,
        release_ref: bool = True,
    ) -> FreeClockEvent:
        ...

    def get_min_free_timeout(self) -> float | None:
        ...

    def _process_free_events(self, current: float) -> None:
        ...


class ClockBaseBehavior:
    MIN_SLEEP: float
    SLEEP_UNDERSHOOT: float

    @property
    def frametime(self) -> float:
        ...

    @property
    def frames(self) -> int:
        ...

    @property
    def frames_displayed(self) -> int:
        ...

    def __init__(self, async_lib: str = "asyncio", **kwargs: Any) -> None:
        ...

    def init_async_lib(self, lib: str) -> None:
        ...

    def usleep(self, microseconds: float) -> None:
        ...

    def idle(self) -> float:
        ...

    async def async_idle(self) -> float:
        ...

    def tick(self) -> None:
        ...

    async def async_tick(self) -> None:
        ...

    def pre_idle(self) -> None:
        ...

    def post_idle(self, ts: float, current: float) -> float:
        ...

    def tick_draw(self) -> None:
        ...

    def get_fps(self) -> float:
        ...

    def get_rfps(self) -> int:
        ...

    def get_time(self) -> float:
        ...

    def get_boottime(self) -> float:
        ...

    def time(self) -> float:
        ...

    def handle_exception(self, e: BaseException) -> None:
        ...


class ClockBaseInterruptBehavior(ClockBaseBehavior):
    interupt_next_only: bool

    def __init__(self, interupt_next_only: bool = False, **kwargs: Any) -> None:
        ...

    def async_usleep(self, microseconds: float) -> Any:
        ...

    def on_schedule(self, event: ClockEvent) -> None:
        ...


class ClockBaseInterruptFreeBehavior(ClockBaseInterruptBehavior):
    ...


class ClockBase(ClockBaseBehavior, CyClockBase):
    ...


class ClockBaseInterrupt(ClockBaseInterruptBehavior, CyClockBase):
    ...


class ClockBaseFreeInterruptAll(ClockBaseInterruptFreeBehavior, CyClockBaseFree):
    ...


class ClockBaseFreeInterruptOnly(ClockBaseInterruptFreeBehavior, CyClockBaseFree):
    ...


def mainthread(
    func: Callable[_P, _R],
) -> Callable[_P, None]:
    ...


class _TriggeredCallable(Protocol[_P]):
    @property
    def is_triggered(self) -> bool:
        ...

    def __call__(self, *args: _P.args, **kwargs: _P.kwargs) -> None:
        ...

    def cancel(self) -> None:
        ...


class _TriggeredDecorator(Protocol):
    def __call__(
        self,
        func: Callable[_P, Any],
    ) -> _TriggeredCallable[_P]:
        ...


@overload
def triggered(
    timeout: Callable[_P, Any],
) -> _TriggeredCallable[_P]:
    ...


@overload
def triggered(
    timeout: float = 0,
    interval: bool = False,
    debounce: bool = False,
) -> _TriggeredDecorator:
    ...


def triggered(
    timeout: float | Callable[..., Any] = 0,
    interval: bool = False,
    debounce: bool = False,
) -> _TriggeredDecorator | _TriggeredCallable[...,]:
    ...


Clock: ClockBase | ClockBaseInterrupt | ClockBaseFreeInterruptAll | ClockBaseFreeInterruptOnly


__all__: tuple[str, ...]
