import matplotlib.pyplot as plt

x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))

dx = x2 - x1
dy = y2 - y1

p = 2 * dy - dx

x, y = x1, y1

points = []

while x <= x2:
    points.append((x, y))
    
    if p < 0:
        p = p + 2 * dy
        
    else:
        y += 1
        p = p + 2 * dy - 2 * dx
        
    x += 1
    
px, py = zip(*points)

plt.plot(px, py, 'ro')
plt.plot(px, py, 'b--', alpha = 0.5)
plt.grid(True)
plt.xlabel("X - axis")
plt.ylabel("Y - axis")
plt.title("Bresenham Line Drawing Algorithm")
plt.show()