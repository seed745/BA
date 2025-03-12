#script for writing different sizes sources for a soucre comparison

r = [2,4,6,8,9,9.5,10,12,14]
for i in range(0,9):
    print("/gps/pos/shape Circle")
    print("/gps/pos/centre 0 0 10 mm")
    print(f"/gps/pos/radius {r[i]} mm" )
    print()
