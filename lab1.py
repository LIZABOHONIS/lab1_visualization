import random #підключаємо необхідні нам бібліотеки
import matplotlib.pyplot as plt
import statistics as s1

import random

class Rand:
    def random (self,n=1000):
        data = []
        return [random.random() for i in range(n)]

if __name__ == '__main__':
    a = Rand()
    data = a.random()
    print('data=', data)
    
plt.plot(data,'yo')


m = s1.mean(data) #середнє значення
print("mean=",m)
plt.plot(m, 'ro')

c = s1.median(data) #медіана
print("median=",c)
plt.plot(c, 'ko')


k = s1.variance(data) #дисперсія
print("dispersia=",k)
plt.plot(k, 'r+')


l = s1.pstdev(data) #стандартне відхилення
print("standart_vidhilennya=",l)
plt.plot(l, 'go')
plt.show()






