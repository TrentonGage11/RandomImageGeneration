from pylab import imshow, show, get_cmap
from numpy import random
def generateArray(w: int=100, h: int=100)
    array = random.random((w,h))

def makeFigureFromArray(color_map: str="Spectral", interpolation_type: str="nearest"):
    """Color Maps: ['viridis', 'plasma', 'inferno', 'magma', 'cividis', 'Greys', 'Purples', 'Blues', 'Greens', 'Oranges', 'Reds', 'YlOrBr', 'YlOrRd', 'OrRd', 'PuRd', 'RdPu', 'BuPu', 'GnBu', 'PuBu', 'YlGnBu', 
    'PuBuGn', 'BuGn', 'YlGn', 'binary', 'gist_yarg', 'gist_gray', 'gray', 'bone', 'pink', 'spring', 'summer', 'autumn', 'winter', 'cool', 'Wistia', 'hot', 'afmhot', 'gist_heat', 'copper', 'PiYG', 'PRGn', 'BrBG', 
    'PuOr', 'RdGy', 'RdBu', 'RdYlBu', 'RdYlGn', 'Spectral', 'coolwarm', 'bwr', 'seismic', 'twilight', 'twilight_shifted', 'hsv', 'Pastel1', 'Pastel2', 'Paired', 'Accent', 'Dark2', 'Set1', 'Set2', 'Set3', 'tab10', 
    'tab20', 'tab20b', 'tab20c', 'flag', 'prism', 'ocean', 'gist_earth', 'terrain', 'gist_stern', 'gnuplot', 'gnuplot2', 'CMRmap', 'cubehelix', 'brg', 'gist_rainbow', 'rainbow', 'jet', 'nipy_spectral', 'gist_ncar']
    Interpolation: [None, 'none', 'nearest', 'bilinear', 'bicubic', 'spline16', 'spline36', 'hanning', 'hamming', 'hermite', 'kaiser', 'quadric', 'catrom', 'gaussian', 'bessel', 'mitchell', 'sinc', 'lanczos']
    """
    imshow(array, cmap=get_cmap(color_map), interpolation=interpolation_type)

def showFigure():
    show()

def getDesktop():
    if os.environ["ONEDRIVE"]:
        fp = f"{os.environ['ONEDRIVE']}\\Desktop"
    elif os.environ["USERPROFILE"]:
        fp = f"{os.environ['USERPROFILE']}\\Desktop"
    return fp

def saveFigure(name=f"{getDesktop()}\\{''.join(choice("abcdefABCDEF012345") for i in range(8))}" ,resolution=300, face_color='w', edge_color='w' ,layout='portrait', filetype=None, transparen=False, metadatainfo=None):
    savefig(fname=name, dpi=resolution, facecolor=face_color, edgecolor=edge_color, orientation=layout, papertype=None, format=filetype, transparent=transparent, metadata=None)
