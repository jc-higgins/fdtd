import numpy as np

class Grid:
    """
    Grid class for FDTD simulation
    """

    canvas: np.ndarray

    def __init__(self, Nx, Ny, Nz, dx, dy, dz) -> None:
        self.Nx = Nx
        self.Ny = Ny
        self.Nz = Nz
        self.dx = dx
        self.dy = dy
        self.dz = dz
        