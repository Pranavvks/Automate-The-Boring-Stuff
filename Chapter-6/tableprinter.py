tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
for a, b, c in zip(tableData[0], tableData[1], tableData[2]):
#for a ,b ,c in range (len(max(tableData[0],tableData[1],tableData[2]))):
    print(a.rjust(5),b.rjust(5),c.rjust(5))
#max_length1 = len(max(tableData[0] , key = len))
#max_length2 = len(max(tableData[1] , key = len))
#max_length3 = len(max(tableData[2] , key = len))




