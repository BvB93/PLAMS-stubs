import sys

from types import TracebackType
from typing import (
    TypeVar,
    Mapping,
    Dict,
    Generic,
    Type,
    Any,
    Iterable,
    Sequence,
    Tuple,
    Callable,
    Optional,
)

if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

class SupportsMissing(Protocol):
    def __missing__(self, __key: Any) -> Any: ...

KT = TypeVar("KT")
VT = TypeVar("VT")
T = TypeVar("T", bound=SupportsMissing)
ST = TypeVar("ST", bound=Settings)

class Settings(Dict[KT, VT]):
    def copy(self) -> Settings[KT, VT]: ...
    def soft_update(self: ST, other: Mapping[KT, VT]) -> ST: ...
    def update(self, other: Mapping[KT, VT]) -> None: ...  # type: ignore[override]
    def merge(self: ST, other: Mapping[KT, VT]) -> ST: ...
    def find_case(self, key: KT) -> KT: ...
    def as_dict(self) -> Dict[KT, VT]: ...
    @classmethod
    def suppress_missing(cls: Type[T]) -> SuppressMissing[T]: ...
    def get_nested(
        self, key_tuple: Iterable[Any], suppress_missing: bool = False
    ) -> Any: ...
    def set_nested(
        self, key_tuple: Sequence[Any], value: Any, suppress_missing: bool = False
    ) -> None: ...
    def flatten(self, flatten_list: bool = ...) -> Settings[Tuple[Any, ...], Any]: ...
    def unflatten(self, unflatten_list: bool = ...) -> Settings[Any, Any]: ...
    def __missing__(self, name: KT) -> Settings[Any, Any]: ...
    def __getattr__(self, name: KT) -> VT: ...  # type: ignore[misc]
    def __setattr__(self, name: KT, value: VT) -> None: ...  # type: ignore[misc,override]
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __add__(self: ST, other: Mapping[KT, VT]) -> ST: ...
    def __iadd__(self: ST, other: Mapping[KT, VT]) -> ST: ...
    def __copy__(self) -> Settings[KT, VT]: ...

class SuppressMissing(Generic[T]):
    obj: T
    missing: Callable[[T, Any], Any]
    def __init__(self, obj: Type[T]) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_value: Optional[BaseException],
        traceback: Optional[TracebackType],
    ) -> None: ...
