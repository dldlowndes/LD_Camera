"""
Process the image files output from LD_Camera relies heavily on opencv
"""

import matplotlib.pyplot as plt
import numpy as np
import cv2


class LD_Image:
    """
    Usage: Instantiate, either Load_CSV or Load_Dat, then save/display/
    histogram as desired.
    """
    def __init__(self):
        pass

    def Load_CSV(self, filename, bits_Per_Pixel=10):
        """
        Load an image from a CSV of pixel values. Since the CSV takes care
        of the line endings, this doesn't need the size specified. Only the
        pixel depth (so that scaling works for output to 8 bit)
        """
        self.bits_Per_Pixel = bits_Per_Pixel
        self.pixels = np.loadtxt(filename, delimiter=",", dtype=np.int)

    def Load_DAT(self, filename, width, height, bits_Per_Pixel):
        """
        Load an image from binary data, packed as a list of 16 bit pixel
        values. Need to specify width and height since this data is not
        embedded in the file.
        """
        self.bits_Per_Pixel = bits_Per_Pixel
        img_Data = np.fromfile(filename, dtype=np.uint8).reshape((-1, 2))
        msbs, lsbs = np.hsplit(img_Data, 2)

        self.pixels = ((msbs.astype(np.uint16) << 8) + lsbs.astype(np.uint16))
        self.pixels = self.pixels.reshape((height, width))

    def __Scale_To_8bit(self):
        """
        Scale the pixel values to 8 bit if the image was captured at higher
        than 8 bit pixel depth.
        """
        if self.bits_Per_Pixel > 8:
            self.pixels = self.pixels // (2**(self.bits_Per_Pixel - 8))

        return self.pixels

    def Histogram(self, show_Plot=False):
        """
        Plot a histogram of the pixel values in the image and (optionally)
        display.
        """
        hist, bins = np.histogram(self.pixels,
                                  bins=np.arange(0, 2**(self.bits_Per_Pixel)))
        if show_Plot:
            plt.plot(hist)
        return hist, bins

    def Show_Image(self):
        """
        Display image in a window. Scales to 8 bit since opencv doesn't like
        it otherwise.
        """
        cv2.imshow("image window", self.__Scale_To_8bit().astype(np.uint8))
        cv2.waitKey(1)

    def Save_Image(self, filename):
        """
        Save image to file, opencv determines the format from the filename.
        """
        self.__Scale_To_8bit()
        cv2.imwrite(filename, self.__Scale_To_8bit().astype(np.uint8))


if __name__ == "__main__":
    myImage = LD_Image()
    myImage.Load_DAT("test_image.bin", 1280, 1024, 10)
    myImage.Show_Image()
