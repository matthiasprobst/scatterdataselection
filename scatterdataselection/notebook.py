import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.graph_objs as go
from ipywidgets import widgets


class ScatterSelection():
    selected_points = None

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def scatter_selector(self, print_selection=False):

        df = pd.DataFrame({'x': self.x, 'y': self.y})
        f = go.FigureWidget([go.Scatter(x=df['x'], y=df['y'], mode='markers')])
        scatter = f.data[0]

        out = widgets.Output()

        def selection_fn(trace, points, selector):
            with out:
                self.selected_points = points.point_inds
                out.clear_output()
                if print_selection:
                    if len(points.point_inds) == 0:
                        display(df)
                    else:
                        display(df[df['x'].isin(points.xs)])
                print(self.selected_points)

        def selection_fn2(trace, points):
            with out:
                out.clear_output()
                self.selected_points = points.point_inds
                if print_selection:
                    if len(points.point_inds) == 0:
                        display(df)
                    else:
                        display(df[df['x'].isin(points.xs)])

        scatter.on_selection(selection_fn)
        scatter.on_deselect(selection_fn2)

        #         f.layout.dragmode = 'select'
        f.layout.dragmode = 'lasso'
        w = widgets.VBox([f, out])
        display(w)