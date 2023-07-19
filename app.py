from arkitekt import register
import tifffile
from mikro.api.schema import RepresentationFragment, from_xarray
from pycudadecon import decon
from typing import Optional
import dask.array as da
import numpy as np
import xarray as xr

@register
def deconvolve(
    image: RepresentationFragment,
    psf: RepresentationFragment,
    n_iters: int = 10,
    background: Optional[int] = None,
    shift: int = 0,
    napodize: int = 15,) -> RepresentationFragment:
    """
    Deconvolve

    Deconvolve an image with its psf using
    the richardson lucy deconvolution algorithm

    Args:
        n_iters (int): The number of iterations
        background(int, Optional): The number 
    Returns:
        deconvole (RepresentationFragment): The deconvolved image
    
    """
    psf_data = image.data.sel(c=0, t=0).compute().data



    cs = []
    for c in range(image.data.sizes["c"]):
        ts = []

        for t in range(image.data.sizes["t"]):
        
            image_data = image.data.sel(c=c, t=t).compute().data
            result = decon(image_data, psf_data, n_iters=n_iters, shift=shift, napodize=napodize)

            ts.append(result)

        cs.append(np.stack(ts, axis=0))


    image_array = np.stack(cs, axis=0)
            


    deconvolved = xr.DataArray(image_array, dims=["c","t", "z", "y", "x"])

    return from_xarray(deconvolved, name="Deconvolved " + image.name, origins=[image, psf])


