# dekon

Dekon is a small arkitekt plugin wrapping the amazing
(pycudadecon)[https://github.com/tlambert03/pycudadecon] library.

## Installation

Please use the arkitekt plugin manager to install this plugin.

## Usage

The plugin provides a single node called `Deconvolve`. It takes an image, and a PSF as input
and returns a deconvolved version of the image. The deconvolution is done using the
Richardson-Lucy algorithm on the GPU.
