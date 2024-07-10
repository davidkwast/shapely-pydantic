"""shapely-pydantic."""


#
import sys
from typing import Any, ClassVar, Tuple, Type

from pydantic import GetCoreSchemaHandler, ValidationError, field_validator
from pydantic_core.core_schema import SerSchema, _dict_not_none
from pydantic_core import ArgsKwargs, PydanticCustomError, core_schema

from shapely import Geometry as _Geometry
from shapely.geometry import Point as _Point
from shapely import from_wkt as shapely_from_wkt


#
if sys.version_info < (3, 12):
    from typing_extensions import TypedDict
else:
    from typing import TypedDict

if sys.version_info < (3, 11):
    from typing_extensions import Protocol, Required, TypeAlias
else:
    from typing import Protocol, Required, TypeAlias

if sys.version_info < (3, 9):
    from typing_extensions import Literal
else:
    from typing import Literal


#
class GeometrySchema(TypedDict, total=False):
    type: _Geometry   # Required[Literal['geometry']]
    serialization: SerSchema


def geometry_schema(
    *, strict: bool = None, serialization: SerSchema = None
) -> GeometrySchema:

    return _dict_not_none(
        type='any',
        strict=strict,
        serialization=serialization,
    )


class Geometry(_Geometry):

    #
    @classmethod
    def __get_pydantic_core_schema__(
        cls, source: Type[Any], handler: GetCoreSchemaHandler
    ) -> core_schema.CoreSchema:
        return geometry_schema()


#


class Point(Geometry):
    pass


class MultiPoint(Geometry):
    pass


#


class LinearRing(Geometry):
    pass


#


class LineString(Geometry):
    pass


class MultiLineString(Geometry):
    pass


#


class Polygon(Geometry):
    pass


class MultiPolygon(Geometry):
    pass


#


class GeometryCollection(Geometry):
    pass
