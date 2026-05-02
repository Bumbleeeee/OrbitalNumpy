import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from planet import Planet
from initial_conditions import *
# TODO: helper function for leapfrog accel calc

dt = 0.01

fig, ax, earth, sat, moon = earth_center()

ax.view_init(elev=60, azim=45)
ax.grid(False) # etc
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])

sat_plot = ax.plot([sat.pos[0]], [sat.pos[1]], [sat.pos[2]], 'ro', markersize=5)[0]
moon_plot = ax.plot([moon.pos[0]], [moon.pos[1]], [moon.pos[2]], 'go', markersize=5)[0]
earth_plot = ax.plot(earth.pos[0], earth.pos[1], earth.pos[2], 'bo', markersize=5)[0]

sat_trail = ax.plot([], [], [], 'r-')[0]
moon_trail = ax.plot([], [], [], 'g-')[0]
earth_trail = ax.plot([], [], [], 'b-')[0]


def leapfrog(planets: list[Planet]):
    total_accels = []

    # accel for first half step
    for p in planets:
        accel = np.zeros(3)
        for other in planets:
            if p is other:
                continue
            a = p.calc_accel(other)
            accel += p.calc_accel(other)

        total_accels.append(accel)

    # update first half step velocities and full step positions
    for i, p in enumerate(planets):
        p.velo += total_accels[i] * (dt / 2)
        p.pos += p.velo * dt

    # second half step accels
    total_accels.clear()
    for p in planets:
        accel = np.zeros(3)
        for other in planets:
            if p is other:
                continue
            accel += p.calc_accel(other)

        total_accels.append(accel)

    # update second half step velocities
    for i, p in enumerate(planets):
        p.velo += total_accels[i] * (dt / 2)


def update(frame):

    # move planets
    leapfrog([sat, moon, earth])

    # update history
    sat.update_history()
    moon.update_history()
    earth.update_history()

    # update data
    sat_plot.set_data_3d([sat.pos[0]], [sat.pos[1]], [sat.pos[2]])
    moon_plot.set_data_3d([moon.pos[0]], [moon.pos[1]], [moon.pos[2]])
    earth_plot.set_data_3d([earth.pos[0]], [earth.pos[1]], [earth.pos[2]])

    # update trails
    sat_trail.set_data_3d(sat.history[:, 0], sat.history[:, 1], sat.history[:, 2])
    moon_trail.set_data_3d(moon.history[:, 0], moon.history[:, 1], moon.history[:, 2])
    earth_trail.set_data_3d(earth.history[:, 0], earth.history[:, 1], earth.history[:, 2])

    return sat_plot, moon_plot, earth_plot, sat_trail, moon_trail, earth_trail


ani = animation.FuncAnimation(fig=fig, func=update, frames=1000, interval=1, blit=True, repeat=True)
plt.show()
