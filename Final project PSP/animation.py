import pygame
from RRTbaseanimation import RRTGraph
from RRTbaseanimation import RRTMap
import time

def main():
    dimensions =(800,1000)
    start=(50,50)
    goal=(300,300)
    obsdim=70
    obsnum=5
    iteration=0
    t1=0

    pygame.init()
    map=RRTMap(start,goal,dimensions,obsdim,obsnum)
    graph=RRTGraph(start,goal,dimensions,obsdim,obsnum)

    obstacles=graph.makeobs()
    map.drawMap(obstacles)

    t1=time.time()
    while (not graph.path_to_goal()):
        time.sleep(0.005)
        elapsed=time.time()-t1
        t1=time.time()
        #raise exception if timeout
        if elapsed > 10:
            print('timeout re-initiating the calculations')
            raise

        if iteration % 10 == 0:
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
    p = graph.getPathCoords()
    map.drawPath(graph.getPathCoords())
    pygame.display.update()
    pygame.event.clear()
    pygame.event.wait()
    
   
    pygame.init()
    picture = pygame.image.load('car.png')
    count= []
    for opo in sorted(p):
        map.map.fill(map.white)
        count.append(opo)
        if len(count)>=2:
            for i in range(len(count) - 1):
                pygame.draw.circle(map.map, map.grey, count[i], map.nodeRad*2, 0)
                pygame.draw.line(map.map,map.Blue,count[i],count[i+1],map.edgeThickness)
        pygame.draw.circle(map.map, map.Green, start, map.nodeRad + 5, 0)
        pygame.draw.circle(map.map, map.Green, map.goal, map.nodeRad + 20, 1)
        map.drawMap(obstacles)
        time.sleep(0.5)
        
        map.map.blit(picture,opo)
        pygame.display.flip()





main()



























