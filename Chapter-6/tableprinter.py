tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
for a, b, c in zip(tableData[0], tableData[1], tableData[2]):
    print(a.rjust(5),b.rjust(5),c.rjust(5))




