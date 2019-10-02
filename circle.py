import math
import logging
logger = logging.getLogger(__name__)


class Circle:
    def __init__(self, radius=1):
        self._radius = radius
        self._diameter = radius * 2
        self._area = radius ** 2 * math.pi

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        try:
            n = int(value)
            if n <= 0:
                raise ValueError("Radius can not be negative")
        except ValueError as e:
            raise
        self._radius = value
        self._diameter = 2 * value
        self._area = value ** 2 * math.pi

    @property
    def diameter(self):
        return self._diameter

    @diameter.setter
    def diameter(self, value):
        self._diameter = value
        self._radius = value / 2
        self._area = self._radius ** 2 * math.pi

    @property
    def area(self):
        return self._area

    @area.setter
    def area(self, value):
        self._area = value
        self._radius = math.sqrt(value / math.pi)
        self._diameter = self.radius * 2


c = Circle(5)
print(c.radius)
print(c.diameter)
print(c.area)

c.radius = 1
print(c.radius)
print(c.diameter)
print(c.area)

c.diameter = 4
print(c.radius)
print(c.diameter)
print(c.area)

c.radius = -2
print(c.radius)
print(c.diameter)
print(c.area)
