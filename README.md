# Probablistic-Motion-Planning
Simulation of an automated path planning mechanism with obstacle detection having particular patterns using Python(PyGame)

# Steps/Approach for Code modelling:

### Step 1:
 > First step includes the formation of the obstacles in the Environment and we are considering the obstacles as static throughout the process

![Step-1](https://user-images.githubusercontent.com/73428876/223770030-e41cf89e-ba86-4515-874d-b73d4f21b164.png)

### Step2:
> The second step includes the process of generating random nodes in the environment in such a what that it does not assimilate with the obstacles formed. Further we are forming a process by which nodes are connected to their nearest neighbor keeping the end goal into consideration and also deleting or dumping the edges which passes through the obstacles.

![Step-2](https://user-images.githubusercontent.com/73428876/223770763-265dedd7-65f6-4a38-98eb-fb36dcd7d51e.png)

### Step3:
> The third step is a step in which the RRT is exploring around the complete environment forming a chain of parent and their succeeding child nodes around the environment/free space.

![Step-3](https://user-images.githubusercontent.com/73428876/223770793-1f29cef3-8823-4448-9147-c01a687ee8b1.png)

### Final step:
>It is the step in which after exploring around the environment we are trying to find the optimal path for the object to reach to its destination/End goal.

![Step-4](https://user-images.githubusercontent.com/73428876/223770818-dbcc19ac-6b2a-499b-9622-35295d5b8285.png)

# Block Diagram:
![BM23-MAT202(Probability) - Block Diagram](https://user-images.githubusercontent.com/73428876/223772825-b133df6e-02ec-41f5-a93c-dbb9813829a5.jpg)

# Concept Map:
![BM23-MAT202(Probability) - Concept Map](https://user-images.githubusercontent.com/73428876/223773421-0702d6fb-13f6-42d8-bcfa-70b17f0fe63b.jpg)

# Probablistic Uncertainity Model:

![BM23-MAT202(Probability) - Probabilistic Model](https://user-images.githubusercontent.com/73428876/223773371-1c5f03ff-baea-4858-a3c8-67cc381cac3f.jpg)
