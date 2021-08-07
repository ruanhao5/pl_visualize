import mayavi.mlab
import torch
import numpy as np

mypointcloud=np.fromfile("data/000001.bin",dtype=np.float32,count=-1).reshape([-1,4])
mypointcloud=torch.from_numpy(mypointcloud)
print(mypointcloud.size())
print(mypointcloud.type())

def viz_mayavi(points,vals="distance"):
    x=points[:,0]
    y=points[:,1]
    z=points[:,2]
    r=points[:,3]
    d=torch.sqrt(x**2+y**2)

    if vals=="height":
        col=z
    else:
        col=d

    fig=mayavi.mlab.figure(bgcolor=(0,0,0),size=(1280,720))
    mayavi.mlab.points3d(x,y,z,
                         col,
                         mode="point",
                         colormap='spectral',
                         figure=fig,
                         )

    mayavi.mlab.show()

if __name__=="__main__":
    viz_mayavi(mypointcloud,vals="height")
