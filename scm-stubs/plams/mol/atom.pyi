from typing import (
    Any,
    Optional,
    List,
    Generic,
    Iterable,
    Tuple,
    Mapping,
    Iterator,
    Sequence,
)
from scm.plams import Bond, Molecule, Settings, Any

class Atom:
    atnum: int
    mol: Molecule
    bonds: List[Bond]
    properties: Settings[Any, Any]
    coords: Tuple[float, float, float]
    def __init__(
        self,
        atnum: int = ...,
        symbol: Optional[str] = ...,
        coords: Optional[Tuple[float, float, float]] = ...,
        unit: str = ...,
        bonds: Optional[List[Bond]] = ...,
        mol: Optional[Molecule] = ...,
        **other: Any
    ) -> None: ...
    def __iter__(self) -> Iterator[float]: ...
    @property
    def symbol(self) -> str: ...
    @symbol.setter
    def symbol(self, symbol: str) -> None: ...
    @property
    def x(self) -> float: ...
    @x.setter
    def x(self, value: float) -> None: ...
    @property
    def y(self) -> float: ...
    @y.setter
    def y(self, value: float) -> None: ...
    @property
    def z(self) -> float: ...
    @z.setter
    def z(self, value: float) -> None: ...
    @property
    def mass(self) -> float: ...
    @property
    def radius(self) -> float: ...
    @property
    def connectors(self) -> float: ...
    @property
    def is_metallic(self) -> int: ...
    @property
    def is_electronegative(self) -> int: ...
    def translate(self, vector: Iterable[float], unit: str = ...) -> None: ...
    def move_to(self, point: Iterable[float], unit: str = ...) -> None: ...
    def distance_to(
        self, point: Iterable[float], unit: str = ..., result_unit: str = ...
    ) -> Tuple[float, float, float]: ...
    def vector_to(
        self, point: Iterable[float], unit: str = ..., result_unit: str = ...
    ) -> float: ...
    def angle(
        self,
        point1: Iterable[float],
        point2: Iterable[float],
        point1unit: str = ...,
        point2unit: str = ...,
        result_unit: str = ...,
    ): ...
    def rotate(self, matrix: Union[np.ndarray, Sequence[Sequence[float]]]) -> None: ...
    def neighbors(self) -> List[Atom]: ...
