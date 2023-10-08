from manim import Scene, Create, Uncreate, Circle, Text, DOWN

class Intro(Scene):
    def construct(self, n_cities=100):
        title = Text("Voronoi TSP").scale(2)
        subtitle = Text(
            "A Voronoi-based solution to the Travelling Salesman Problem"
        ).scale(0.75). next_to(title, DOWN)
        num_cities = Text(f"{n_cities} cities").scale(1)
        self.play(Create(title))
        self.play(Create(subtitle))
        self.wait(1)
        self.play(
            Uncreate(subtitle),
            title.animate.become(num_cities).scale(1.5),
        )
        self.wait(1)
        self.play(Uncreate(title))
        self.wait(.1)