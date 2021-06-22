from manimlib import*
import numpy as np

class Icosahedron(ThreeDScene):

    def f(t=0):
        phi = (-1 + np.sqrt(5)) / 2

        verts = [
            np.array([0, 1, -phi]),
            np.array([1, phi, 0]),
            np.array([phi, 0, -1]),
            np.array([-phi, 0, -1]),
            np.array([-1, phi, 0]),
            np.array([0, 1, phi]),

            np.array([0, -1, phi]),
            np.array([-phi, 0, 1]),
            np.array([-1, -phi, 0]),
            np.array([0, -1, -phi]),
            np.array([1, -phi, 0]),
            np.array([phi, 0, 1])
        ]

        surf = SGroup()
        
        face_indices=[
                        [0, 1, 2],
                        [1, 0, 5],
                        [0, 2, 3],
                        [0, 3, 4],
                        [0, 4, 5],

                        [2, 1, 10],
                        [1, 5, 11],
                        [10, 1, 11],
                        [3, 2, 9],
                        [9, 2, 10],

                        [4, 3, 8],
                        [8, 3, 9],
                        [5, 4, 7],
                        [7, 4, 8],
                        [5, 7, 11],

                        [6, 7, 8],
                        [7, 6, 11],
                        [6, 8, 9],
                        [6, 9, 10],
                        [6, 10, 11]
            ]

        for x in face_indices:
            current_face=SGroup()

            i=x[0]
            j=x[1]
            k=x[2]

            normal = np.cross(verts[j]-verts[i],verts[k]-verts[i])
            vertices = [verts[i], verts[j], verts[k]]
            centroid = (verts[i]+verts[j]+verts[k])/3

            if np.dot(centroid,normal) < 0:
                print(x)

            third = centroid

            for s in range(0,3):
                first=vertices[s]
                second = (vertices[(s+1)%3] + vertices[s])/2
                surf.add(Triangle3D(vertices=[first,second,third], color=WHITE))

                second = (vertices[(s-1)%3] + vertices[s])/2
                surf.add(Triangle3D(vertices=[first,second,third], color=BLACK))

        return surf

    surf = f()

    surf.scale(3)
    self.play(Rotating(surf,axis=[1,1,1], angle=TAU, rate_func = smooth, run_time=6))
