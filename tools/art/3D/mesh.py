import numpy as np
from stl import mesh
from featuredetection import FeatureField


IMAGE_SCALE = 10

class Mesh:

    vertices = []
    edges = []
    faces = []

    def __init__(self, fn="py3.jpg"):
        self.fn = fn
        pass

    def generate(self):
        #todo: generate shapes with faces
        self.generate_verts()
        self.generate_mesh()

    def generate_mesh(self):
        # Create the mesh
        m = mesh.Mesh(
            np.zeros(
                len(self.vertices), dtype=mesh.Mesh.dtype
            ))
        for i in range(len(self.vertices)):
                    m.vectors[i] = self.vertices[i]
        print("Saving a mesh ")
        # Write the mesh to file "cube.stl"
        m.save('meme.stl')

    def generate_verts(self):
        # H = img.shape[1]
	    # W = img.shape[0]
        kp = FeatureField().sift_keypoints(self.fn)

        verts = np.zeros(( len(kp), 3), np.uint16)
        # get keypoints
        
        for i, k in enumerate(kp):
            verts[i] = [
                k.pt[0] / IMAGE_SCALE ,
                k.pt[1] / IMAGE_SCALE,
                i / IMAGE_SCALE
            ]

        self.vertices = verts 

    def generate_faces(self, verts=[]):
        #
        for v in range(0, self.vertices.shape[0], 3):
            self.faces.append(
                [v, v+1, v+2] # Next 3 vertices into face
            )



me = Mesh("py4.jpg")
me.generate()
