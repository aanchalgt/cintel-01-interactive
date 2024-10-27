
# Import the required dependencies
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from shiny.express import ui, input, render
from palmerpenguins import load_penguins

# Add page options for the overall app.
ui.page_opts(title="Palmer Penguins Plot", fillable=True)

# Create a sidebar with a slider input and input selector.
with ui.sidebar():
    # Slider for specifying the number of bins in the histogram.
    ui.input_slider("selected_number_of_bins", "Number of Bins", 5, 50, 25)

    # Selector for specifying which penguin species to be observed.
    ui.input_select("Species", "Species of Choice", ["Adelie", "Chinstrap", "Gentoo"])

@render.plot(alt="A histogram on Palmer Penguins")

def draw_histogram():
    # Define the number of points to generate. Use optional type hinting to indicate this is an integer.
    count_of_points: int = 437
    
    # Set a random seed to ensure reproducibility.
    np.random.seed(5)
    
    # Generate random data:
    random_data_array = 100 + 10 * np.random.randn(count_of_points)
    
    # Create a histogram for the randomly generated dataset.
    
    plt.hist(random_data_array, input.selected_number_of_bins(), density=True)

    plt.title("Histogram of Penguins Data")

    plt.xlabel("Value")

    plt.ylabel("Density")

    plt.grid(True)




