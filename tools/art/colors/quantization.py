from dataclasses import dataclass
from sklearn.cluster import MiniBatchKMeans
import numpy as np
import cv2

def find_distincts(arr: np.array):
    """
        Find distinct values in numpy array.
    """

    dist_vals = {}
    for i in range(arr.shape[0]):
        
        for j in range(arr.shape[1]):

            # Distinct key signatures for sequences of numbers
            dist_vals[
                arr[i][j].sum() + arr[i][j].prod()
            ] = arr[i][j]

    return dist_vals
class Quantization():

    data: np.array


    def color_quantize(
        self, num_clusters: int
    )-> tuple[np.array, np.array]:
        """
        Returns:
        Tuple:
            HSV version of the image array:np.array, 
            list of distinct colors: np.array
        """
        # load the image and grab its width and height
        (h, w) = self.data.shape[:2]
        # convert the image from the RGB color space to the L*a*b*
        # color space -- since we will be clustering using k-means
        # which is based on the euclidean distance, we'll use the
        # L*a*b* color space where the euclidean distance implies
        # perceptual meaning
        self.data = cv2.cvtColor(self.data, cv2.COLOR_BGR2LAB)
        # reshape the image into a feature vector so that k-means
        # can be applied
        self.data = self.data.reshape((self.data.shape[0] * self.data.shape[1], 3))
        # apply k-means using the specified number of clusters and
        # then create the quantized image based on the predictions
        clt = MiniBatchKMeans(n_clusters = num_clusters)

        labels = clt.fit_predict(self.data)
        quant = clt.cluster_centers_.astype("uint8")[labels]
        # reshape the feature vectors to images
        quant = quant.reshape((h, w, 3))
        self.data = self.data.reshape((h, w, 3))
        # convert from L*a*b* to RGB

        quant = cv2.cvtColor(cv2.cvtColor(quant, cv2.COLOR_LAB2BGR),
            cv2.COLOR_BGR2HSV)
        colors = find_distincts(quant)
        #image = cv2.cvtColor(image, cv2.COLOR_LAB2BGR)

        return quant, colors
