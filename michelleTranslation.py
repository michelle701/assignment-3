import matplotlib.pyplot as plt


class CoordinatePlotter:
    def __init__(self, file_path):
        self.file_path = file_path
        self.x_coordinates = []
        self.y_coordinates = []

    def load_data(self):
        """ coordinates from the specified file."""
        with open(self.file_path, 'r') as my_file:
            my_file.readline()  # Skip the header line
            for line in my_file.readlines():
                x, y = map(float, line.split(', '))
                self.x_coordinates.append(x)
                self.y_coordinates.append(y)

    def translate_coordinates(self, translation_vector):
        """Translate the coordinates by the given vector."""
        translated_x = [x + translation_vector[0] for x in self.x_coordinates]
        translated_y = [y + translation_vector[1] for y in self.y_coordinates]
        return translated_x, translated_y

    def plot_data(self):
        """Plot the original and translated coordinates."""
        # Plotting the original coordinates
        plt.scatter(self.x_coordinates, self.y_coordinates, color='blue', label='Original Points')

        # Translate the points
        translation_vector = (1, 2)  # translation vector
        translated_x, translated_y = self.translate_coordinates(translation_vector)

        # Plotting the translated coordinates in a different color
        plt.scatter(translated_x, translated_y, color='green', label='Translated Points')

        # Adding labels and title to the graph
        plt.ylabel('Y Coordinates')
        plt.xlabel('X Coordinates')
        plt.title('Scatter Plot of Coordinates')
        plt.grid(True)
        plt.legend()  # Showing legend to differentiate the points
        plt.show()


# Usage
if __name__ == "__main__":
    file_path = 'C:/Users/USER/Documents/Captures/x_y_coordinates.txt'
    plotter = CoordinatePlotter(file_path)
    plotter.load_data()
    plotter.plot_data()