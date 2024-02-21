import random
import numpy as np
from scipy.spatial import Voronoi

from manim import (
    BLUE, Scene, Create, Uncreate, Circle, Text, Dot, VGroup,
    Axes, Polygon, GRAY
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

        dots = VGroup()
        for i in range(100):
            graphs += Dot(
                point=grid.c2p(
                    np.random.random(),
                    np.random.random(), 0),
                color=BLUE).scale(.75)
            dots.add(graphs[i])
        self.add(grid)
        self.play(Create(graphs))
        self.wait(1)

        points = [dot.get_center()[:2] for dot in dots]
        print("Points:", points)  # Debugging statement

        try:
            vor = Voronoi(points)
            voronoi_diagram = VGroup()
            for region_index in vor.regions:
                if -1 in region_index or len(region_index) == 0:
                    continue  # Skip invalid or infinite regions
                vertices = [vor.vertices[i] for i in region_index]
                vertices = [(vertex[0], vertex[1], 0) for vertex in vertices]  # Ensure vertices are in (x, y, z) format
                voronoi_diagram.add(Polygon(*vertices, color=GRAY, stroke_width=1))

            self.play(Create(voronoi_diagram))
            self.wait(1)
        except Exception as e:
            print("Error:", e)  # Print any error messages for debugging

        self.wait(1)
