for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j} x {i} = {j * i}", end="\t")
    print()

# 得到字符串
talbe99 = ""
for i in range(1, 10):
    for j in range(1, i + 1):
        talbe99 += f"{j} x {i} = {j * i}\t"
    talbe99 += "\n"
print(talbe99)


def get_99table():
    talbe99 = ""
    for i in range(1, 10):
        for j in range(1, i + 1):
            talbe99 += f"{j} x {i} = {j * i}\t"
        talbe99 += "\n"
    return talbe99


print(get_99table())
