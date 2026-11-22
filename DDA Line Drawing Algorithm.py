import matplotlib.pyplot as plt

x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))

dx = x2 - x1
dy = y2 - y1

steps = max(abs(dx), abs(dy))

if steps == 0:
    x_points = [x1]
    y_points = [y1]
    
else:
    xinc = dx/steps
    yinc = dy/steps
    
    x = x1
    y = y1
    
    x_points = []
    y_points = []
    
    for i in range(steps + 1):
        x_points.append(round(x))
        y_points.append(round(y))
        
        x += xinc
        y += yinc
        
plt.plot(x_points, y_points, marker = 's', color = 'blue')
plt.title("DDA Line Drawing Alogorithm")
plt.xlabel("X - axis")
plt.ylabel("Y - axis")
plt.grid(True)
plt.axis("equal")
plt.show()