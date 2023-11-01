import matplotlib.pyplot as plt
import numpy as np

################# WYKRES Z DWIEMA KROPKAMI ###############
# plt.plot([5],[7],'ro')
# plt.plot([4],[12],'b^')

# plt.axis((0,10, 0, 13))
# plt.xticks(np.arange(0, 15+1, 1))
# plt.yticks(np.arange(0, 10+1, 1))


################ WYKRES Z LINIĄ #########

# x = [1,2,3,4,5,6,7,8,9,10,11,12]

# y1 = [-2, -5,-7, -8, -3, 0, 2, 5, 4, 7, 11, 15]
# y2 = [2, 5, 6, 4, 9, 11, 7, 8 ,9 , 12, 14, 16]
# y3 = [-7, -5, 2, 0, 3, 6, 3, 1, 5, 3, 2, 2]

# plt.plot(x, y1, 'bo-')
# plt.plot(x, y2, 'g^--')
# plt.plot(x, y3, 'r*-.')

# plt.xticks(np.arange(0, 15, 1))
# plt.title('Wykres pomarow temperatur ze stacji S1, S2 S3')
# plt.xlabel('Czas poiaru [h]')
# plt.ylabel('Temeraura [°C]')
# plt.legend(['S1' , 'S2', 'S3'], loc='best', fontsize='15')


########### WYKRES Z PARABOLĄ ############
# x = np.linspace(-20, 20, 1000)
# y1 = x - 2
# y2 = x ** 2 - 4


# plt.plot(x, y1)
# plt.plot(x, y2)

# plt.axhline(0, color= 'black', linewidth= 0.5)
# plt.axvline(0, color= 'black', linewidth= 0.5)

# plt.axis((-10, 10, -10, 10))
# plt.xticks(np.arange(-10, 10+1, 1))
# plt.yticks(np.arange(-10, 10+1, 1))
# plt.plot([2, -1], [0, -3], 'ro')


# plt.title('Wykres funkcji liniowej i kwadratowej')

########### WYKRES PODWOJNY A W NIM RWNIEZ WYKRES SLUPKOWY  ########

# x = np.linspace(-10, 10, 1000)

# def my_func(x):
#   return x ** 3 + 2 * x - 6  
  
# plt.subplot(211)
# plt.plot(x, my_func(x), 'g-')
# plt.subplot(212)
# parties = ['Ludzie', 'Elfy', 'Krasnoludy', 'Enty']
# results = [21.56, 30.10, 19.22, 28.12]
# plt.bar(parties, results)


           
# """ OBOK LUB WIECEJ
# plt.subplot(121), plt.subplot(122)

# plt.subplot(211),(222), (223), (224)
# """

############### WYKRES KOŁOWY #############



costs = ['jedzenie', 'rozrywka', 'czynsz', 'odziez']
pln = [1356, 545, 1067,220]

explode = [0, 0.1, 0, 0]

plt.pie(pln, labels= costs, shadow= True, startangle= 90, explode= explode)






plt.show()