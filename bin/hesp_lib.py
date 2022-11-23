#!/usr/bin/python
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib.colors import LogNorm
import numpy, time
import numpy as np
import peakutils
from astropy.io import fits
from scipy.ndimage import morphology as morph
from scipy.ndimage import filters
import os
import progressbar
from time import sleep 
def biascombine(files, output='BIAS.fit', trim=False, silent=False):
    # assume biaslist is a simple text file with image names
    # e.g. ls flat.00*b.fits > bflat.lis    
    if silent is False:
        print('biascombine: combining ' + str(len(files)) + ' files')

    for i in range(0,len(files)):
        hdu_i = fits.open(files[i][:-5]+'_pp.fit',do_not_scale_image_data=True)

        if trim is False:
            im_i = hdu_i[0].data
        if trim is True:
            datasec = hdu_i[0].header['DATASEC'][1:-1].replace(':',',').split(',')
            d = map(float, datasec)
            im_i = hdu_i[0].data[d[2]-1:d[3],d[0]-1:d[1]]

        # create image stack
        if (i==0):
            all_data = np.array(im_i)
        elif (i>0):
            all_data = np.dstack( (all_data, im_i) )
        hdu_i.close(closed=True)

    # do median across whole stack
    #print all_data
    try:
        bias = np.median(all_data, axis=2)
    except:
        bias= np.array(all_data)        
    #print bias.shape
    # write output to disk for later use
    hduOut = fits.PrimaryHDU(bias)
    hduOut.writeto(output, overwrite=True)
     
def overscanbias(img, cols1=(1,), cols2=(1,)):
    '''
    Generate a bias frame based on overscan region.
    Can work with rows or columns, pass either kwarg the limits:
    >>> bias = overscanbias(imagedata, cols=(1024,1050))
    '''
    bias = np.zeros_like(img)
    if len(cols1) > 1:
        bcol = np.mean(img[:,cols1[0]:cols1[1]], axis=1)
        for j in range(img.shape[1]):
            img[:,j] = bcol

    if len(cols2) > 1:
        brow = np.mean(img[:,cols2[0]:cols2[1]], axis=1)
        for j in range(img.shape[1]):
              bias[:,j] = brow
              img[:,j]=(img[:,j]+bias[:,j])/2
          
    if len(cols1)==1:
        print('OVERSCANBIAS ERROR: need to pass either cols=(a,b) or rows=(a,b),')
        print('setting bias = zero as result!')

    return img
        

