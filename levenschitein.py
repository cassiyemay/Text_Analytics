
from nltk.metrics import distance
from pprint import pprint

t1 = "@Ofordwords my next video lesson will be available on YouTube"
t2 = "do not count your chickens before they are hatched"
t3 = "every human being has an impact on another"
t4 = "you know you must be doing something right if old people like you"
t5 = "96 out of the 100 most common English words have germanic roots"
array1 = [t1,t2,t3,t4,t5]

t6 = "@Sunflower354 my next video lesson will be available on YouTube"
t7 = "@Keinthen12 my next video lesson will be available on YouTube#NoSecrets"
t8 = "@HadNoRight my next video lesson will be available on YouTube http://bit.ly/54vw8o "
t9 = "#WordsWorld my next video lesson will be available on YouTube http://bit.ly/54vw8o/  #LetTheVedioIn"
t10 = "@Dublintime12 my next video lesson will be available on YouTube http://bit.ly/54vw8o  #LetTheVedioIn #TheVideo #FreeLessonIn"
t11 = "my next video lesson will be available on YouTube #freelaptoplink"
t12 = "@TextAnalysis11 my next video lesson will be available on YouTube #picture1.png http://freelaptop.ie/ "
t13 = "@ComputerScience345 my next video lesson will be available on YouTube"
t14 = "#googleanswers #applicationformobile my next video lesson will be available on YouTube"
t15 = "my next video lesson will be available on YouTube http://www.marketing.ly #Youtubevideo"
t16 = "@hehhthheiih456777 my next video lesson will be available on YouTube"
t17 = "my next video lesson will be available on YouTube @uytohyeh123 #lessonfreee"
t18 = "my next video lesson will be available on YouTube @opityeytn555"
t19 = "my next video lesson will be available on YouTube @12_hghetfhtte345"
t20 = "@ty_worldwide1 my next video lesson will be available on YouTube #discount80%"
t21 = "my next video lesson will be available on YouTube @ mmm_dheith #picture2.png"
t22 = "#workday #studyingfree my next video lesson will be available on YouTube"
t23 = "@JohnMark #Mylesson my next video lesson will be available on YouTube"
t24 = "my next video lesson will be available on YouTube @FaceBook_11 #photograph111.png"
t25 = "#goodlife.png @IrishTime my next video lesson will be available on YouTube"
array = [t6,t7,t8,t9,t10,t11,t12,t13,t14,t15,t16,t17,t18,t19,t20,t21,t22,t23,t24,t25]
list = []
matrix = [[0]*20 for i in range(5)]
#pprint(matrix)
for i in range(len(array1)):
    for j in range(len(array)):
        matrix[i][j] =distance.edit_distance(array1[i],array[j])


print(matrix[4])


ans = distance.edit_distance(t1,t2)
ans1 = distance.edit_distance(t1,t3)
ans2 = distance.edit_distance(t1,t4)
ans3 = distance.edit_distance(t1,t5)

print(ans,ans1,ans2,ans3)