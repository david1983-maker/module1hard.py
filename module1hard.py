grades = [[5,3,3,5,4],[2,2,2,3],[4,5,5,2],[4,4,3],[5,5,5,4,5]]
students = {'Johny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

students=list(students)
students.sort()

grades0=(sum(grades [0])/5)
grades1=(sum(grades [1])/4)
grades2=(sum(grades [2])/4)
grades3=(sum(grades [3])/3)
grades4=(sum(grades [4])/5)

score={students [0]:grades0, students [1]:grades1,
       students [2]:grades2, students[3]:grades3,
       students[4]:grades4}

print(score)