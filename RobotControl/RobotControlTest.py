import pybullet as p
import time
import pybullet_data

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath()) 
p.setPhysicsEngineParameter(numSolverIterations=10)
p.setTimeStep(1. / 120.)
RobotID=p.loadURDF("r2d2.urdf", useMaximalCoordinates=True)
p.configureDebugVisualizer(p.COV_ENABLE_RENDERING, 0)
p.configureDebugVisualizer(p.COV_ENABLE_GUI, 0)
p.configureDebugVisualizer(p.COV_ENABLE_TINY_RENDERER, 0)

print(p.getNumJoints(RobotID))

## Base Link(-1) --- link0 -- link1 -- link 2
## indices =  [0 .. getNumJoints()] 
<<<<<<< HEAD
=======
## 
>>>>>>> bb41a3fc45ac7d55fc19fb45737b16eec38a25cd

