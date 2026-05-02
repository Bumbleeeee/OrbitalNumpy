from planet import Planet
import matplotlib.pyplot as plt

def create_fig(xlims: tuple, ylims: tuple, zlims: tuple):
    fig = plt.figure()
    ax = fig.add_subplot(projection="3d")
    ax.set(xlim3d=xlims, xlabel='X')
    ax.set(ylim3d=ylims, ylabel='Y')
    ax.set(zlim3d=zlims, zlabel='Z')

    return fig, ax

def figure_eight():
    earth = Planet(pos=(-0.97, 0.24, 0), velo=(0.465, 0.43, 0), mass=1)
    sat = Planet(pos=(0.97, -0.24, 0.0), velo=(0.465, 0.43, 0.0), mass=1)
    moon = Planet(pos=(0, 0.0, 0.0), velo=(-0.93, -0.86, 0.0), mass=1)
    fig, ax = create_fig((-2, 2), (-2, 2), (-1, 1))

    return fig, ax, earth, sat, moon


def earth_center():
    earth = Planet(pos=(0, 0, 0), velo=(0, -0.0707, 0), mass=1000)
    sat = Planet(pos=(20.0, 0.0, 0.0), velo=(0.0, 7.07, 0.0), mass=10)
    moon = Planet(pos=(21.0, 0.0, 0.0), velo=(0.0, 10.23, 0.0), mass=0)
    fig, ax = create_fig((-30, 30), (-30, 30), (-10, 10))

    return fig, ax, earth, sat, moon


def lagrange_equilateral():
    # NOTE: unstable, probably due to limited precision. Better if dt is smaller but much slower
    earth = Planet(pos=(1, 0, 0), velo=(0, 1, 0), mass=1)
    sat = Planet(pos=(-0.5, 0.86602540378, 0), velo=(-0.86602540378, -0.5, 0), mass=1)
    moon = Planet(pos=(-0.5, -0.86602540378, 0), velo=(0.86602540378, -0.5, 0), mass=1)
    fig, ax = create_fig((-5, 5), (-5, 5), (-1, 1))

    return fig, ax, earth, sat, moon


