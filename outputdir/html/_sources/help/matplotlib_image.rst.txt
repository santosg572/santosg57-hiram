matplotlib.image
================

['Affine2D', 'AxesImage', 'BESSEL', 'BICUBIC', 'BILINEAR', 'BLACKMAN', 'Bbox', 'BboxBase', 'BboxImage', 'BboxTransform', 
'BboxTransformTo', 'CATROM', 'FigureCanvasBase', 'FigureImage', 'GAUSSIAN', 'HAMMING', 'HANNING', 'HERMITE', 
'IdentityTransform', 'KAISER', 'LANCZOS', 'MITCHELL', 'NEAREST', 'NonUniformImage', 'PIL', 'Path', 'PcolorImage', 
'QUADRIC', 'SINC', 'SPLINE16', 'SPLINE36', 'TransformedBbox', '_ImageBase', '__builtins__', '__cached__', '__doc__', 
'__file__', '__loader__', '__name__', '__package__', '__spec__', '_api', '_draw_list_compositing_images', '_image', 
'_interpd_', '_log', '_pil_png_to_float_array', '_resample', '_rgb_to_rgba', 'cbook', 'cm', 'composite_images', 'imread', 
'imsave', 'interpolations_names', 'logging', 'martist', 'math', 'mcolors', 'mpl', 'np', 'os', 'pil_to_array', 'resample', 
'thumbnail', 'warnings']


** &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&& **
Help on function imread in module matplotlib.image:

imread(fname, format=None)
    Read an image from a file into an array.
    
    .. note::
    
        This function exists for historical reasons.  It is recommended to
        use `PIL.Image.open` instead for loading images.
    
    Parameters
    ----------
    fname : str or file-like
        The image file to read: a filename, a URL or a file-like object opened
        in read-binary mode.
    
        Passing a URL is deprecated.  Please open the URL
        for reading and pass the result to Pillow, e.g. with
        ``np.array(PIL.Image.open(urllib.request.urlopen(url)))``.
    format : str, optional
        The image file format assumed for reading the data.  The image is
        loaded as a PNG file if *format* is set to "png", if *fname* is a path
        or opened file with a ".png" extension, or if it is a URL.  In all
        other cases, *format* is ignored and the format is auto-detected by
        `PIL.Image.open`.
    
    Returns
    -------
    `numpy.array`
        The image data. The returned array has shape
    
        - (M, N) for grayscale images.
        - (M, N, 3) for RGB images.
        - (M, N, 4) for RGBA images.
    
        PNG images are returned as float arrays (0-1).  All other formats are
        returned as int arrays, with a bit depth determined by the file's
        contents.

None
** &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&& **
Help on function imsave in module matplotlib.image:

imsave(fname, arr, vmin=None, vmax=None, cmap=None, format=None, origin=None, dpi=100, *, metadata=None, pil_kwargs=None)
    Colormap and save an array as an image file.
    
    RGB(A) images are passed through.  Single channel images will be
    colormapped according to *cmap* and *norm*.
    
    .. note::
    
       If you want to save a single channel image as gray scale please use an
       image I/O library (such as pillow, tifffile, or imageio) directly.
    
    Parameters
    ----------
    fname : str or path-like or file-like
        A path or a file-like object to store the image in.
        If *format* is not set, then the output format is inferred from the
        extension of *fname*, if any, and from :rc:`savefig.format` otherwise.
        If *format* is set, it determines the output format.
    arr : array-like
        The image data. The shape can be one of
        MxN (luminance), MxNx3 (RGB) or MxNx4 (RGBA).
    vmin, vmax : float, optional
        *vmin* and *vmax* set the color scaling for the image by fixing the
        values that map to the colormap color limits. If either *vmin*
        or *vmax* is None, that limit is determined from the *arr*
        min/max value.
    cmap : str or `~matplotlib.colors.Colormap`, default: :rc:`image.cmap`
        A Colormap instance or registered colormap name. The colormap
        maps scalar data to colors. It is ignored for RGB(A) data.
    format : str, optional
        The file format, e.g. 'png', 'pdf', 'svg', ...  The behavior when this
        is unset is documented under *fname*.
    origin : {'upper', 'lower'}, default: :rc:`image.origin`
        Indicates whether the ``(0, 0)`` index of the array is in the upper
        left or lower left corner of the Axes.
    dpi : float
        The DPI to store in the metadata of the file.  This does not affect the
        resolution of the output image.  Depending on file format, this may be
        rounded to the nearest integer.
    metadata : dict, optional
        Metadata in the image file.  The supported keys depend on the output
        format, see the documentation of the respective backends for more
        information.
        Currently only supported for "png", "pdf", "ps", "eps", and "svg".
    pil_kwargs : dict, optional
        Keyword arguments passed to `PIL.Image.Image.save`.  If the 'pnginfo'
        key is present, it completely overrides *metadata*, including the
        default 'Software' key.

None
