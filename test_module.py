import unittest
import pandas as pd
import numpy as np
import medical_data_visualizer
from medical_data_visualizer import df


class CatPlotTestCase(unittest.TestCase):

    def setUp(self):
        self.fig = medical_data_visualizer.draw_cat_plot()
        self.ax = self.fig.axes[0]

    def test_line_colors(self):
        """Both panels must contain bars."""
        for ax in self.fig.axes:
            self.assertGreater(len(ax.patches), 0)

    def test_bar_chart_number_of_bars(self):
        """Each panel should have 12 bars (6 variables × 2 values)."""
        for ax in self.fig.axes:
            self.assertEqual(len(ax.patches), 12)

    def test_bar_chart_x_tick_labels(self):
        expected = sorted(['active', 'alco', 'cholesterol', 'gluc',
                           'overweight', 'smoke'])
        for ax in self.fig.axes:
            labels = [t.get_text() for t in ax.get_xticklabels()]
            self.assertEqual(labels, expected)

    def test_number_of_axes(self):
        self.assertEqual(len(self.fig.axes), 2)


class HeatMapTestCase(unittest.TestCase):

    def setUp(self):
        self.fig = medical_data_visualizer.draw_heat_map()
        self.ax = self.fig.axes[0]

    def test_heat_map_shape(self):
        """Data used for the heat map should have 14 columns."""
        self.assertEqual(df.shape[1], 14)

    def test_heat_map_labels(self):
        expected_labels = sorted([
            'id', 'age', 'sex', 'height', 'weight', 'ap_hi', 'ap_lo',
            'cholesterol', 'gluc', 'smoke', 'alco', 'active', 'cardio',
            'overweight'
        ])
        labels = sorted([t.get_text() for t in self.ax.get_xticklabels()])
        self.assertEqual(labels, expected_labels)

    def test_heat_map_has_values(self):
        """Heatmap cells should contain annotation text."""
        self.assertGreater(len(self.ax.texts), 0)


if __name__ == '__main__':
    unittest.main()
