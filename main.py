import medical_data_visualizer
from unittest import main

# Generate charts
medical_data_visualizer.draw_cat_plot()
medical_data_visualizer.draw_heat_map()

# Run tests
main(module='test_module', exit=False, verbosity=2)
