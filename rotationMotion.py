import numpy as np
import matplotlib.pyplot as plt


def circular_path(radius, initial_position, num_steps, centerPoint, num_rotations=1):
    
    # Generate the angles for each step in the circular path
    angles = np.linspace(0, num_rotations*2*np.pi, num_steps)
    
    # Calculate the positions for each step in the circular path
    positions = []
    for angle in angles:
        x = centerPoint[0] + radius*np.cos(angle)
        y = centerPoint[1] + radius*np.sin(angle)
        z = initial_position[2]
        positions.append([x, y, z])
    
    Pos_arr=np.array(positions)
    # to force the path such that the intial point is the current postion of the drone
    shift = np.array([Pos_arr[0,0], Pos_arr[0,1], Pos_arr[0,2] ])
    arr_shifted = Pos_arr - shift + initial_position

    # shift = np.array([Pos_arr[0,0]+initial_position[0], Pos_arr[0,1]+initial_position[1], Pos_arr[0,2]+initial_position[2] ])


    return arr_shifted


def store_teamPaths(initial_positions, radius, num_steps,num_drones,centerPoint,rotatNum):
    circular_paths = []
    for i in range(num_drones):
        circular_paths.append(circular_path(radius[i], initial_positions[i], num_steps,centerPoint,num_rotations=rotatNum))
    
    return circular_paths


num_drones = 5
num_steps = 50 
centerPoint=[0,0,0]
rotatNum=2  # number of rotations

# # scenario (1)
initial_positions = np.array([[ 0  ,  0, 1],
                              [0.25,  0, 1.25],
                              [0.5 ,  0, 1.5],
                              [0.75,  0, 1.75],
                              [1.0 ,  0, 2.0]])
radius = [0.5, 0.75, 1.0, 1.25, 1.5] # radius of the circle of each drone



# scenario (2)
# initial_positions = np.array([[ 0  ,  0,   1],
#                               [1.0,   0,   1],
#                               [1.0 ,  1.0, 1],
#                               [0.0,   1.0, 1],
#                               [0.5 ,  0.5, 2]])

# radius = [1.0, 1.0, 1.0, 1.0, 1.0] # radius of the circle of each drone


circular_paths=store_teamPaths(initial_positions, radius, num_steps,num_drones,centerPoint,rotatNum)

# plot
# Create 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot circular paths
for i in range(num_drones):
    ax.plot(circular_paths[i][:, 0], circular_paths[i][:, 1], circular_paths[i][:, 2], c='b')

# Plot initial positions
for i in range(len(initial_positions)):
    ax.scatter(initial_positions[i][0], initial_positions[i][1], initial_positions[i][2], c='r')

# Animate drones' motion
for i in range(num_steps):
    for j in range(num_drones):
        ax.scatter(circular_paths[j][i, 0], circular_paths[j][i, 1], circular_paths[j][i, 2], c='b')
    plt.draw()
    plt.pause(0.05)
    ax.clear()
    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 3)
    ax.set_zlim(-3, 3)
    ax.view_init(elev=30., azim=i*2)

    # Plot circular paths
    for j in range(num_drones):
        ax.plot(circular_paths[j][:, 0], circular_paths[j][:, 1], circular_paths[j][:, 2], c='b')

    # Plot initial positions
    for j in range(len(initial_positions)):
        ax.scatter(initial_positions[j][0], initial_positions[j][1], initial_positions[j][2], c='r')

plt.show()
