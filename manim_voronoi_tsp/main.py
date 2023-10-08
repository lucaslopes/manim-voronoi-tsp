from manim import Scene
from Scenes import Intro, TSP

class VoronoiTSP(Scene):
    def construct(self):
        Intro.construct(self)
        TSP.construct(self)