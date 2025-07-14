from fdtd.grid import Grid
import numpy as np

class Hy:
    """
    Hy field class for 1D FDTD simulation
    """

    grid: Grid
    field_array: np.ndarray
    
    def __init__(self, grid: Grid) -> None:
        self.grid = grid

    def update(self) -> None:
        pass