import pygame
from firstfile_final import RRTGraph
from firstfile_final import RRTMap
import time
import random
import matplotlib.pyplot as plt

dict1 = {}
length1  =[]
block = []

#defining the various dimentions reated to the environment
def main(goal,map,dimensions,start,obsdim,obsnum,graph,obstacles,i):
    iteration = 0
    pygame.init()
    map.drawMap(obstacles)
    t1=time.time()
    
    while (not graph.path_to_goal()):
        time.sleep(0.005)
        elapsed=time.time()-t1
        t1=time.time()
        if dict1.get(i)==None:
            dict1[i] = 1
        else:
            dict1[i]+=1
        #raise exception if timeout
        if elapsed > 10:
            print('timeout re-initiat1ing the calculations')
            raise
        if iteration % 50 == 0:
            X, Y, Parent = graph.bias(goal)
            pygame.draw.circle(map.map, map.grey, (X[-1], Y[-1]), map.nodeRad*2, 0)
            pygame.draw.line(map.map, map.Blue, (X[-1], Y[-1]), (X[Parent[-1]], Y[Parent[-1]]),
                             map.edgeThickness)

        else: 
            X, Y, Parent = graph.expand()
            pygame.draw.circle(map.map, map.grey, (X[-1], Y[-1]), map.nodeRad*2, 0)
            pygame.draw.line(map.map, map.Blue, (X[-1], Y[-1]), (X[Parent[-1]], Y[Parent[-1]]),
                            map.edgeThickness)
        if iteration % 5 == 0:
       
            pygame.display.update()
        iteration += 1

    length1.append(len(graph.getPathCoords()))
    block.append(graph.total)

    map.drawPath(graph.getPathCoords())
    pygame.display.update()
    pygame.event.clear()
    pygame.event.wait()
    time.sleep(0.05)
   

       
op = []
if __name__ == '__main__':
    x = 200
    y = 200
    obstacles =[]
    n = 0
    for i in range(20):
        result=False
        n = n+1
        dimensions =(600,1000)
        start=(1,1)
        if obstacles!=[]:
            case1 = True
            while case1 :
                x = x + random.randint(1,10);y = y+ random.randint(1,10)
                goal=(x,y)
                for rectang in obstacles: 
                    if rectang.collidepoint(goal):
                       break
                else:
                    case1 = False
        else:
            goal = start
                        

                   
       
        obsdim=30
        obsnum=70
        map=RRTMap(start,goal,dimensions,obsdim,obsnum)
        graph=RRTGraph(start,goal,dimensions,obsdim,obsnum)
        if obstacles==[]:
            obstacles=graph.makeobs()   
        while not result:
            try:
                main(goal,map,dimensions,start,obsdim,obsnum,graph,obstacles,n)
                result=True
            except:
                result=False
    
    # fig = plt.figure()
    # ax = fig.add_axes([0,0,1,1])
    length1.sort()
    block.sort()
    print(length1)
    plt.scatter(length1, block)
    plt.plot(length1,block)
    
   
    # ax.line(length1,block)
    plt.show()
   