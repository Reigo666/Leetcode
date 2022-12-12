
import collections
from typing import  List,Optional
import copy

import random
class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.x_center=x_center
        self.y_center=y_center
        self.radius=radius

    def randPoint(self) -> List[float]:
        radius=self.radius
        while True:
            randx=random.uniform(-radius,radius)
            randy=random.uniform(-radius,radius)
            if randx*randx+randy*randy<=radius*radius:
                break

        return [self.x_center+randx,self.y_center+randy]

# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()