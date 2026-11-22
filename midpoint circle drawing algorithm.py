import matplotlib.pyplot as plt

xc = int(input("Enter center x: "))
yc = int(input("Enter center y: "))
r = int(input("Enter radius: "))

x = 0
y = r
p = 1 - r

while x <= y:
    plt.scatter(xc + x, yc + y, color='black', s=20, marker='s')
    plt.scatter(xc - x, yc + y, color='black', s=20, marker='s')
    plt.scatter(xc + x, yc - y, color='black', s=20, marker='s')
    plt.scatter(xc - x, yc - y, color='black', s=20, marker='s')
    
    plt.scatter(xc + y, yc + x, color='black', s=20, marker='s')
    plt.scatter(xc - y, yc + x, color='black', s=20, marker='s')
    plt.scatter(xc + y, yc - x, color='black', s=20, marker='s')
    plt.scatter(xc - y, yc - x, color='black', s=20, marker='s')
    
    if p < 0:
        p = p + 2 * x + 3
    else:
        p = p + 2 * (x - y) + 5
        y = y - 1
        
    x = x + 1
    
plt.show()