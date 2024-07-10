from pydantic import BaseModel

from shapely.geometry import Point as _Point
from shapely.geometry import MultiPoint as _MultiPoint

from shapely_pydantic import Point
from shapely_pydantic import MultiPoint

#
def test_test():   # :-P

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
