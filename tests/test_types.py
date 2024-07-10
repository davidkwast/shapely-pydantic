from pydantic import BaseModel

from shapely.geometry import Point as _Point
from shapely.geometry import MultiPoint as _MultiPoint

from shapely_pydantic import Point
from shapely_pydantic import MultiPoint
from shapely_pydantic import LineString
from shapely_pydantic import MultiLineString
from shapely_pydantic import Polygon
from shapely_pydantic import Multipolygon
from shapely_pydantic import LinearRing
from shapely_pydantic import GeometryCollection

#
def test_types():   # :-P

    #

    class Model(BaseModel):
        point: Point
        multipoint: MultiPoint
        linestring: LineString
        multilinestring: MultiLineString
        polygon: Polygon
        multipolygon: Multipolygon
        linearring: LinearRing
        geometrycollection: GeometryCollection

    #
    class PointModel(BaseModel):
        geom: Point

    assert PointModel(geom=_Point([0, 0])).geom == _Point([0, 0])

    #
    class MultiPointModel(BaseModel):
        geom: MultiPoint

    assert MultiPointModel(geom=_MultiPoint([[0, 0]])).geom == _MultiPoint(
        [[0, 0]]
    )

    # assert type(Model(poi='POINT (0,0)').poi) == _Point([0, 0])
