import random
import numpy as np
from manim import (
    BLUE, Scene, Create, Uncreate, Circle, Text, Dot, VGroup,
    Axes,
)

class TSP(Scene):
    def construct(self, n_cities=100):
        grid = Axes(
            x_range=[0, 1, 0.05],  # step size determines num_decimal_places.
            y_range=[0, 1, 0.05],
            x_length=16,
            y_length=9,
        ).scale(.75)
        graphs = VGroup()
        for _ in range(100):
            graphs += Dot(
                point=grid.c2p(
                    np.random.random(),
                    np.random.random(), 0),
                color=BLUE).scale(.75)
        self.add(grid)
        self.play(Create(graphs))
        self.wait(1)