import random
import math
import time
import pygame #using the pygame module for visualization of work.
#defining the class RRT map
# contains the methods for drawing the map,obstacles and path
# obstacle = [(42, 879, 30, 30), (491, 171, 30, 30), (356, 237, 30, 30), (204, 395, 30, 30), (225, 121, 30, 30), (546, 687, 30, 30), (401, 507, 30, 30), (131, 801, 30, 30), (106, 289, 30, 30), (404, 672, 30, 30), (66, 730, 30, 30), (487, 578, 30, 30), (397, 271, 30, 30), (99, 371, 30, 30), (202, 351, 30, 30), (130, 95, 30, 30), (19, 147, 30, 30), (510, 106, 30, 30), (100, 319, 30, 30), (567, 393, 30, 30), (203, 115, 30, 30), (45, 26, 30, 30), (390, 7, 30, 30), (8, 821, 30, 30), (561, 457, 30, 30), (392, 676, 30, 30), (155, 818, 30, 30), (569, 961, 30, 30), (264, 211, 30, 30), (521, 266, 30, 30), (345, 804, 30, 30), (433, 20, 30, 30), (285, 533, 30, 30), (543, 62, 30, 30), (169, 619, 30, 30), (96, 243, 30, 30), (187, 273, 30, 30), (241, 706, 30, 30), (349, 684, 30, 30), (324, 944, 30, 30), (48, 180, 30, 30), (416, 1, 30, 30), (282, 838, 30, 30), (115, 905, 30, 30), (89, 105, 30, 30), (87, 256, 30, 30), (522, 606, 30, 30), (380, 948, 30, 30), (110, 812, 30, 30), (371, 502, 30, 30), (107, 709, 30, 30), (339, 332, 30, 30), (292, 741, 30, 30), (372, 114, 30, 30), (227, 3, 30, 30), (6, 200, 30, 30), (132, 562, 30, 30), (412, 578, 30, 30), (200, 708, 30, 30), (431, 701, 30, 30)]
# obstacles = []
# for i in obstacle:
#     obstacles.append(pygame.Rect(i))
obstacles = []
op= [(209, 203), (213, 207), (214, 212), (215, 213), (221, 218), (226, 219), (232, 224), (240, 227), (247, 228), (257, 229), (258, 230), (267, 232), (269, 236), (272, 237), (277, 239), (279, 242), (288, 245), (290, 250), (300, 252), (306, 255)]
class RRTMap:
    
    def __init__(self, start, goal, MapDimensions, obsdim, obsnum): 
        self.start = start
        self.goal = goal
        self.MapDimensions = MapDimensions 
        #defining the height and the width of th window/environment space
        self.Maph, self.Mapw = self.MapDimensions

        #creating a window and defining it settings
        self.MapWindowName = 'PSP project-RRT path planning'
        pygame.display.set_caption(self.MapWindowName)
        self.map = pygame.display.set_mode((self.Mapw, self.Maph))
        self.map.fill((255, 255, 255)) #brackground colour
        self.nodeRad = 2  #defining the node radius and thickness
        self.nodeThickness = 0 
        self.edgeThickness = 1
          #array of the location of the obstacles 
        self.obsdim = obsdim  #dimention of obstacles
        self.obsNumber = obsnum #no of obstcles

        # selecting differnt Colors for various objects
        self.grey = (70, 70, 70)
        self.Blue = (0, 0, 255)
        self.Green = (0, 255, 0)
        self.Red = (255, 0, 0)
        self.white = (255, 255, 255)

 #drawing Start point and the End point   
    def drawMap(self, obstacles): 
        pygame.draw.circle(self.map, self.Green, self.start, self.nodeRad + 5, 0)
        pygame.draw.circle(self.map, self.Green, self.goal, self.nodeRad + 20, 1)
        self.drawObs(obstacles)

    def drawPath(self, path):
        
        
        for node in path:
            time.sleep(0.05)
            pygame.draw.circle(self.map, self.Red, node, 5, 0)
        


#showing the obstacles on the pygame window using function pygame.draw.rect
    def drawObs(self, obstacles): 
     
        obstaclesList = obstacles.copy()
        while (len(obstaclesList) > 0):
            obstacle = obstaclesList.pop(0)
            pygame.draw.rect(self.map, self.grey, obstacle)


#definig RRT grap and passing the same argument as RRT Graph such as Start point,End goal,Map dimentions,dimention and number of obstacles.
class RRTGraph:
    def __init__(self, start, goal, MapDimensions, obsdim, obsnum):
        (x, y) = start
        self.start = start
        self.goal = goal
        self.goalFlag = False #turns true if the object treaches the goal point/End goal.
        self.maph, self.mapw = MapDimensions
        #storing the node location points for parent and children nodes of the RRT in the form of list
        self.x = []
        self.y = []
        self.parent = []
        # initializing the tree 
        self.x.append(x)
        self.y.append(y)
        #starting node is a parent node itself
        self.parent.append(0) 
        # the obstacles
        self.obsDim = obsdim
        self.obsNum = obsnum
        # path
        self.goalstate = None
        self.path = [] 
        self.total = 0
# Randomly generating the rectangular obstacles
    def makeRandomRect(self):
        uppercornerx = int(random.uniform(0, self.mapw - self.obsDim)) #for keeping it inside the window dimention/environment space
        uppercornery = int(random.uniform(0, self.maph - self.obsDim))

        return (uppercornerx, uppercornery)
#Creating and storing obstacles in the list
    def makeobs(self):
        
        for i in range(0, self.obsNum):
            rectang = None    #Creating a temporary variable for storing obstacles untill it gets into list
            startgoalcol = True
            while startgoalcol:
                upper = self.makeRandomRect()
                rectang = pygame.Rect(upper, (self.obsDim, self.obsDim))
                if rectang.collidepoint(self.start) or rectang.collidepoint(self.goal): #for avoiding creating obstacles on start point and end goal.
                    startgoalcol = True
                else:
                    case1 = False
                    for noted in op:
                        if rectang.collidepoint(noted):
                           print("yes")
                           startgoalcol = True
                           break
                    else:
                        startgoalcol = False
                    
            obstacles.append(rectang)
            
        return obstacles

# adding node into the list(n=index,x&y=co-ordinates)
    def add_node(self, n, x, y):
        self.x.insert(n, x)
        self.y.append(y)
#removing the node at the index n using pop method
    def remove_node(self, n):
        self.x.pop(n)
        self.y.pop(n)

## adding parent into parent node using child as index
    def add_edge(self, parent, child):
        self.parent.insert(child, parent)

#removing the edge at the index n using pop method
    def remove_edge(self, n):
        self.parent.pop(n)

    def number_of_nodes(self):
        return len(self.x)

#finding the distance between two nodes using distance formula
    def distance(self, n1, n2):
        (x1, y1) = (self.x[n1], self.y[n1])
        (x2, y2) = (self.x[n2], self.y[n2])
        px = (float(x1) - float(x2)) ** 2
        py = (float(y1) - float(y2)) ** 2
        return (px + py) ** (0.5)

#Randomly generating nodes
    def sample_envir(self):
        x = int(random.uniform(0, self.mapw))
        y = int(random.uniform(0, self.maph))
        return x, y

#Finding the nearest node
    def nearest(self, n):
        dmin = self.distance(0, n)
        nnear = 0 # temperorrily storing the  variable for storing the nearest node
        for i in range(0, n):
            if self.distance(i, n) < dmin:
                dmin = self.distance(i, n)
                nnear = i 
        return nnear

#Geneating the nodes in the free environment were the obstacles are not present
    def isFree(self):
        n = self.number_of_nodes() - 1
        (x, y) = (self.x[n], self.y[n])
        obs = obstacles.copy()
        while len(obs) > 0:
            rectang = obs.pop(0)
            if rectang.collidepoint(x, y):
                self.remove_node(n)
                return False
        return True

#checking if the edge intersects the obstacles and thus removing the intersecting ones.
    def crossObstacle(self, x1, x2, y1, y2):
        obs = obstacles.copy()
       
        while (len(obs) > 0):
            rectang = obs.pop(0)
            for i in range(0, 101):
                u = i / 100
                x = x1 * u + x2 * (1 - u)
                y = y1 * u + y2 * (1 - u)
                if rectang.collidepoint(x, y):
                    self.total+=1
                    return True
        return False


    def connect(self, n1, n2):
        (x1, y1) = (self.x[n1], self.y[n1])
        (x2, y2) = (self.x[n2], self.y[n2])
        if self.crossObstacle(x1, x2, y1, y2):
            
            self.remove_node(n2)
            return False
        else:
            self.add_edge(n1, n2)
            return True

    def step(self, nnear, nrand, dmax=35):
        d = self.distance(nnear, nrand)
        if d > dmax:
            u = dmax / d
            (xnear, ynear) = (self.x[nnear], self.y[nnear])
            (xrand, yrand) = (self.x[nrand], self.y[nrand])
            (px, py) = (xrand - xnear, yrand - ynear)
            theta = math.atan2(py, px)
            (x, y) = (int(xnear + dmax * math.cos(theta)),
                      int(ynear + dmax * math.sin(theta)))
            self.remove_node(nrand)
            if abs(x - self.goal[0]) <= dmax and abs(y - self.goal[1]) <= dmax:
                self.add_node(nrand, self.goal[0], self.goal[1])
                self.goalstate = nrand
                self.goalFlag = True
            else:
                self.add_node(nrand, x, y)

    def bias(self, ngoal):
        n = self.number_of_nodes()
        self.add_node(n, ngoal[0], ngoal[1])
        nnear = self.nearest(n)
        self.step(nnear, n)
        self.connect(nnear, n)
        return self.x, self.y, self.parent

    def expand(self):
        n = self.number_of_nodes()
        x, y = self.sample_envir()
        self.add_node(n, x, y)
        if self.isFree():
            xnearest = self.nearest(n)
            self.step(xnearest, n)
            self.connect(xnearest, n)
        return self.x, self.y, self.parent

    def path_to_goal(self):

        if self.goalFlag:
            self.path = []
            self.path.append(self.goalstate)
            newpos = self.parent[self.goalstate]

            while (newpos != 0):
                self.path.append(newpos)
                newpos = self.parent[newpos]
            self.path.append(0)
        return self.goalFlag

    def getPathCoords(self):
        pathCoords = []
        for node in self.path:
            x, y = (self.x[node], self.y[node])
            pathCoords.append((x, y))
        return pathCoords

    def cost(self, n):
        ninit = 0
        n = n
        parent = self.parent[n]
        c = 0
        while n is not ninit:
            c = c + self.distance(n, parent)
            n = parent
            if n is not ninit:
                parent = self.parent[n]
        return c

    def getTrueObs(self, obs):
        TOBS = []
        for ob in obs:
            TOBS.append(ob.inflate(-50, -50))
        return TOBS

    def waypoints2path(self):
        oldpath = self.getPathCoords()
        path = []
        for i in range(0, len(self.path) - 1):
            print(i)
            if i >= len(self.path):
                break
            x1, y1 = oldpath[i]
            x2, y2 = oldpath[i + 1]
            print('---------')
            print((x1, y1), (x2, y2))
            for i in range(0, 5):
                u = i / 5
                x = int(x2 * u + x1 * (1 - u))
                y = int(y2 * u + y1 * (1 - u)) 
                path.append((x, y))
                print((x, y))

        return path




