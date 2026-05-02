import matplotlib.pyplot as plt

def create_fig(xlims: tuple, ylims: tuple, zlims: tuple):
    fig = plt.figure()
    ax = fig.add_subplot(projection="3d")
    ax.set(xlim3d=xlims, xlabel='X')
    ax.set(ylim3d=ylims, ylabel='Y')
    ax.set(zlim3d=zlims, zlabel='Z')

    return fig, ax