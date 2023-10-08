from manim import Scene, Create, Uncreate, Circle, Text

class Intro(Scene):
    def construct(self, n_cities=10):
        title = Text("Voronoi TSP").scale(2)
        subtitle = Text("A Voronoi-based solution to the Travelling Salesman Problem").scale(0.75)
        num_cities = Text(f"{n_cities} cities").scale(0.75)
        self.play(Create(title))
        self.play(Create(subtitle))
        self.wait(1)
        self.play(
            Uncreate(title),
            Uncreate(subtitle),
            Create(num_cities),
        )
        self.wait(1)
        self.play(Uncreate(num_cities))
        self.wait(1)