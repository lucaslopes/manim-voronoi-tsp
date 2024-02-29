# Manim Voronoi TSP
> Manim animation of a heuristic for solving the Traveling Salesman Problem using Voronoi Diagrams as a reduction on search

## How to use

__PREREQUISITE__: [Manim](https://www.manim.community/) must be installed.

Clone the repository, and run the following command inside the directory folder (`manim-voronoi-tsp/`) for see a quick preview in low resolution:

`manim -pql manim_voronoi_tsp/main.py`


### Newly added

I used `from scipy.spatial import Voronoi` to create a Voronoi diagram with:

```
vor = Voronoi(points)
voronoi_diagram = VGroup()
```

Then I add a `Polygon` following all the vertices
