# shapely-pydantic


```python

from shapely_pydantic import Point
from shapely_pydantic import MultiPoint
from shapely_pydantic import LineString
from shapely_pydantic import MultiLineString
from shapely_pydantic import Polygon
from shapely_pydantic import Multipolygon
from shapely_pydantic import LinearRing
from shapely_pydantic import GeometryCollection


class Shapely_Model_Demo(BaseModel):
    point: Point
    multipoint: MultiPoint
    linestring: LineString
    multilinestring: MultiLineString
    polygon: polygon
    multipolygon: Multipolygon
    linearring: LinearRing
    geometrycollection: GeometryCollection

```