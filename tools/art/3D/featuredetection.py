import numpy as np
import cv2 as cv
from datetime import datetime
from stl import mesh

def timed_(f):
    def wrapper(*args):
        e1 = cv.getTickCount()
        res = f(*args)
        e2 = cv.getTickCount()
        t = (e2 - 
            e1
        ) / cv.getTickFrequency()
        print("\n{} elapsed in {} seconds.".format(f, t))
        return res
    return wrapper


class FeatureField():

    def __init__(self) -> None:
        pass


    def generate(self, fn: str):
        #todo: generate shapes with faces
        vertices = self.sift_verts(fn)
        new_mesh = self.generate_mesh(vertices)
        print("Saving a mesh ")
        # Write the mesh to file "cube.stl"
        new_mesh.save(fn + '.stl')

    def generate_mesh(self, verts)-> np.array:
        # Create the mesh vectors as single verts
        m = mesh.Mesh(
            np.zeros(
                len(self.vertices), dtype=mesh.Mesh.dtype
            ))
        for i in range(len(verts)):
            m.vectors[i] = verts[i]
        return m


    def sift_verts(self, fn) -> np.array:

        kp = FeatureField().sift_keypoints(fn)
        SCALE = 10
        verts = np.zeros(( len(kp), 3), np.uint16)
        # add keypoints as vertices
        for i, k in enumerate(kp):
            verts[i] = [
                k.pt[0] / SCALE ,
                k.pt[1] / SCALE,
                i / SCALE]
        return verts

    def generate_faces(self, verts=[]):
        #
        faces = []
        for v in range(0, self.vertices.shape[0], 3):
            faces.append(
                [v, v+1, v+2] # Next 3 vertices into face
            )
        return faces

    @timed_
    def sift_keypoints(self, fname) -> cv.KeyPoint:
        img = cv.imread(fname)

        gray= cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        sift = cv.SIFT_create(1231)
        
        kp, des = sift.detectAndCompute(gray,None)
        img = cv.drawKeypoints(gray, kp, img)
        cv.imwrite(
            str(
                datetime.now().timestamp()
            ) + '.jpg',
            img)
        return kp

class DepthField:

    @staticmethod
    def generate(fname):
        pass

#features = FeatureField()
#keypoints = features.sift_keypoints('m.jpg')