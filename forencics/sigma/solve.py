res = [-64,-80,-62,-84,-64,-81,-67,-88,-14,-60,-81,-69,-13,-82,-68,-69,-20,-60,-14,-60,-84,-17,-18,-60,-80,-14,-68,-74,-17,-90]


flag = ''
for i in res:
    flag += chr(-(i - 35))
print(flag)

# csawctf{1_th0ugh7_1_w45_s1gm4}
