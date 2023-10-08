from manim import Scene, Create, Circle, Text

class Intro(Scene):
    def construct(self):
        title = Text("Voronoi TSP").scale(2)
        self.add(title)
        self.wait(2)