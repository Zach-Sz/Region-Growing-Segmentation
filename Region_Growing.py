import numpy as np
import matplotlib.pyplot as plt

def region_grow(orimg, seed, threshold):
    [A,B] = np.shape(orimg)
    segimg = np.zeros((A,B))
    segimg[seed[0],seed[1]] = 255
    pixelxy = []
    pixelxy.append([seed[0],seed[1]])
    used = []
    used.append([seed[0],seed[1]])
    
    
    while len(pixelxy) > 0:
        #print(used)
        if pixelxy[0][1]+1 < B and pixelxy[0][1]-1 >= 0 and pixelxy[0][0]-1 >= 0 and pixelxy[0][0]+1 < A:
            if abs(orimg[pixelxy[0][0],pixelxy[0][1]] - orimg[pixelxy[0][0],pixelxy[0][1]+1]) <= threshold:
                segimg[pixelxy[0][0],pixelxy[0][1]+1] = 255
                plist = np.array([pixelxy[0][0],pixelxy[0][1]+1])
                if not any((plist == x).all() for x in used) and not any((plist == x).all() for x in pixelxy):
                    pixelxy.append(([pixelxy[0][0],pixelxy[0][1]+1]))
                    
        #if pixelxy[0][1]-1 >= 0: 
            if abs(orimg[pixelxy[0][0],pixelxy[0][1]] - orimg[pixelxy[0][0],pixelxy[0][1]-1]) <= threshold:
                segimg[pixelxy[0][0],pixelxy[0][1]-1] = 255
                plist = np.array([pixelxy[0][0],pixelxy[0][1]-1])
                if not any((plist == x).all() for x in used) and not any((plist == x).all() for x in pixelxy):
                    pixelxy.append(([pixelxy[0][0],pixelxy[0][1]-1]))
            
        #if pixelxy[0][0]-1 >= 0:
            if abs(orimg[pixelxy[0][0],pixelxy[0][1]] - orimg[pixelxy[0][0]-1,pixelxy[0][1]]) <= threshold:
                segimg[pixelxy[0][0]-1,pixelxy[0][1]] = 255
                plist = np.array([pixelxy[0][0]-1,pixelxy[0][1]])
                if not any((plist == x).all() for x in used) and not any((plist == x).all() for x in pixelxy):
                    pixelxy.append(([pixelxy[0][0]-1,pixelxy[0][1]]))
        
        #if pixelxy[0][0]+1 <= A:
            if abs(orimg[pixelxy[0][0],pixelxy[0][1]] - orimg[pixelxy[0][0]+1,pixelxy[0][1]]) <= threshold:
                segimg[pixelxy[0][0]+1,pixelxy[0][1]] = 255
                plist = np.array([pixelxy[0][0]+1,pixelxy[0][1]])
                if not any((plist == x).all() for x in used) and not any((plist == x).all() for x in pixelxy):
                    pixelxy.append(([pixelxy[0][0]+1,pixelxy[0][1]]))
  
                
    
    
    
        #if pixelxy[0][1]+1 <= B and pixelxy[0][0]+1 <= A:
            if abs(orimg[pixelxy[0][0],pixelxy[0][1]] - orimg[pixelxy[0][0]+1,pixelxy[0][1]+1]) <= threshold:
                segimg[pixelxy[0][0]+1,pixelxy[0][1]+1] = 255
                plist = np.array([pixelxy[0][0]+1,pixelxy[0][1]+1])
                if not any((plist == x).all() for x in used) and not any((plist == x).all() for x in pixelxy):
                    pixelxy.append(([pixelxy[0][0]+1,pixelxy[0][1]+1]))
                
        #if pixelxy[0][0]+1 <= A and pixelxy[0][1]-1 >= 0:
            if abs(orimg[pixelxy[0][0],pixelxy[0][1]] - orimg[pixelxy[0][0]+1,pixelxy[0][1]-1]) <= threshold:
                segimg[pixelxy[0][0]+1,pixelxy[0][1]-1] = 255
                plist = np.array([pixelxy[0][0]+1,pixelxy[0][1]-1])
                if not any((plist == x).all() for x in used) and not any((plist == x).all() for x in pixelxy):
                    pixelxy.append(([pixelxy[0][0]+1,pixelxy[0][1]-1]))
                
        #if pixelxy[0][0]-1 >= 0 and pixelxy[0][1]+1 <= B:
            if abs(orimg[pixelxy[0][0],pixelxy[0][1]] - orimg[pixelxy[0][0]-1,pixelxy[0][1]+1]) <= threshold:
                segimg[pixelxy[0][0]-1,pixelxy[0][1]+1] = 255
                plist = np.array([pixelxy[0][0]-1,pixelxy[0][1]+1])
                if not any((plist == x).all() for x in used) and not any((plist == x).all() for x in pixelxy):
                    pixelxy.append(([pixelxy[0][0]-1,pixelxy[0][1]+1]))
                
        #if pixelxy[0][0]+1 <= A and pixelxy[0][1]-1 >= 0:
            if abs(orimg[pixelxy[0][0],pixelxy[0][1]] - orimg[pixelxy[0][0]-1,pixelxy[0][1]-1]) <= threshold:
                segimg[pixelxy[0][0]-1,pixelxy[0][1]-1] = 255
                plist = np.array([pixelxy[0][0]-1,pixelxy[0][1]-1])
                if not any((plist == x).all() for x in used) and not any((plist == x).all() for x in pixelxy):
                    pixelxy.append(([pixelxy[0][0]-1,pixelxy[0][1]-1]))
                      
        used.append(([pixelxy[0][0],pixelxy[0][1]])) 
        pixelxy.pop(0)
    return(segimg)












