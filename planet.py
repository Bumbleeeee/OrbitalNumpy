import numpy as np
G = 1

class Planet:
    pos: np.array[np.float64]
    velo: np.array[np.float64]
    mass: int
    history: np.array[np.array[np.float64]]

    def __init__(self, pos: tuple, velo: tuple, mass):
        self.pos = np.array(pos, dtype='float64')
        self.velo = np.array(velo, dtype='float64')
        self.mass = mass
        self.history = np.full((500, 3), self.pos)

    def calc_accel(self, other: Planet):
        dist = np.linalg.norm(self.pos - other.pos)
        accel_scalar = (G * other.mass) / (dist**2)
        accel_vec = (-(self.pos - other.pos) / dist) * accel_scalar
        return accel_vec

    # newest points are last in history
    def update_history(self):
        self.history = np.roll(self.history, -1, axis=0)
        self.history[499] = [self.pos[0], self.pos[1], self.pos[2]]
