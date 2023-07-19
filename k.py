from arkitekt import easy
from mikro.api.schema import from_xarray
import tifffile
import xarray as xr

with easy("dekon_data", url="lok:8000"):
    tif = tifffile.imread("psf.tif")
    image = tifffile.imread("im_raw.tif")

    print(image.shape)

    
    t = from_xarray(xr.DataArray(tif, dims=["z","y","x"]), name="PSF")
    t = from_xarray(xr.DataArray(image, dims=["z","y","x"]), name="Raw image")


