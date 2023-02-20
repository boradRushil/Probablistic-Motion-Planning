import pygame
from RRTbasePy import RRTGraph
from RRTbasePy import RRTMap
import time
dict1 = {}
def main(i):
    dimensions =(512,512)
    start=(50,50)
    goal=(300,300)
    obsdim=30
    obsnum=50
    iteration=0
    t1=0

    pygame.init()
    map=RRTMap(start,goal,dimensions,obsdim,obsnum)
    graph=RRTGraph(start,goal,dimensions,obsdim,obsnum)

    map.drawMap()

    t1=time.time()
    while (not graph.path_to_goal()):
        time.sleep(0.005)
        elapsed=time.time()-t1
        t1=time.time()
        #raise exception if timeout
        if elapsed > 10:
            print('timeout re-initiating the calculations')
            raise

        if iteration % i == 0:
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
    map.drawPath(graph.getPathCoords())
    dict1[i] = len(graph.getPathCoords())
    pygame.display.update()
    pygame.event.clear()
    pygame.event.wait()
    time.sleep(0.5)
    pygame.display.quit()
    pygame.quit()


x = int(input("ENTER THE VALUE FROM WHICH YOU WANT TO FIND ASPECT RATIO : "))
for i in range(x,1,-1):
    time.sleep(0.05)
    main(i)
for i in sorted(dict1):
    print(dict1[i],i)
    break
    



























