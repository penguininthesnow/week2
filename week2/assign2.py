# 作業一:位置座標判斷

positions = {
    "悟空":(0, 0),
    "丁滿":(-1, 4),
    "辛巴":(-3, 3),
    "貝吉塔":(-4, -1),
    "弗利沙":(4, -1),
    "特南克斯":(1, -2),

}

# 斜線 假設 y=-x+2
LINE_A, LINE_B, LINE_C = 1.0, 1.0, -2.0

# # 設定邊界
# X_MIN, X_MAX = -4, 4
# Y_MIN, Y_MAX = -2, 4

def same_side(p1, p2, a, b, c):
    v1=a+p1[0]+b*p1[1]+c
    v2=a+p2[0]+b*p2[1]+c
    if v1==0 or v2==0:
        return True
    return v1*v2>0 #同號表示在同一側

def cross_line(p1, p2, a, b, c, cheat=2):
    dx= abs(p1[0] - p2[0])
    dy= abs(p2[0] - p2[0])
    cor = dx + dy # 同側則回傳 cor
    if same_side:
        return cor
    else:
        return cor + cheat # 不同側代表有跨越 要+2(cheat)


def func1(name):
    if name not in positions:
        print("角色不存在")
        return
    

    target = positions[name]
    dists = {}

    for other, pos in positions.items():
        if other == name:
            continue
        d = cross_line(target, pos, LINE_A, LINE_B, LINE_C , cheat=2)
        dists[ other ] = d

    min_d = min(dists.values())
    max_d = max(dists.values())

    nearest = sorted([n for n, d in dists.items() if d == min_d])
    farthest = sorted([n for n, d in dists.items() if d == max_d])

    print(f"最遠{'、 '.join(farthest)} ; 最近{'、 '.join(nearest)} ")

func1("辛巴")
func1("悟空")
func1("弗利沙")
func1("特南克斯")


# 作業二:一對一服務設置

def func2( ss, start, end, criteria ):
    if not hasattr(func2, "schedule"):
        func2.schedule = {s["name"]:[] for s in ss}

    field, op, value = None, None, None
    for o in ["<=", ">=", "="]:
        if o in criteria:
            field, value = criteria.split(o)
            op = o
            field, value = field.strip(), value.strip()
            break

    available = []

    for s in ss:
        conflict = any(not(end <= st or start >= et) for st, et in func2.schedule[s["name"]])
        if conflict:
            continue

        if field == "name":
            if op == "=" and s["name"] == value:
                available.append(s)
            # match = (op == "=" and s["name"] == value)
        else:
            val = float(value)
            if op == ">=" and s[field] >= val:
                available.append(s)
            elif op == "<=" and s[field] <= val:
                available.append(s)
            elif op =="=" and s[field] == val:
                available.append(s)

    if not available:
        print("Sorry")
        return
        
    if field != "name":
        val = float(value)
        chosen = min(available, key=lambda x: abs(x[field] - val))
    else:
        chosen = available[0]

    func2.schedule[chosen["name"]].append((start, end))
    print(chosen["name"])



services=[
    {"name": "S1", "r": 4.5, "c": 1000},
    {"name": "S2", "r": 3, "c": 1200},
    {"name": "S3", "r": 3.8, "c": 800}
]


func2(services, 15, 17, "c>=800" )
func2(services, 11, 13, "r<=4" )
func2(services, 10, 12, "name=S3" )
func2(services, 15, 18, "r>=4.5" )
func2(services, 16, 18, "r>=4" )
func2(services, 13, 17, "name=S1" )
func2(services, 8, 9, "c<=1500" )


# 作業三:規則數列

def func3(index):
    y=[ -2, -3, +1, +2] # y=[0]=-2, y=[2]=+1 以此類推
    n = 25 # 從 25 開始
    for x in range(1, index+1): # index 代表迴圈走的次數 第1次 ~ 第index次
        z = y[( x - 1 ) % 4] # 4 個一循還 # 除以4之後取餘數
        n= n + z # n=25，z=y[0]=-2，n=25-2
    print(n)

func3(1)
func3(5)
func3(10)
func3(30)


# 作業四:列車問題

def func4(sp, stat, n):
    candidates=[]

    for i, (s, st) in enumerate(zip(sp, stat)):
         if st == '0': # 只看可服務的車廂
            candidates.append((i, s))  
    if not candidates:
        return None

    # 能完全容納乘客的車廂
    enough=[(i, s) for i, s in candidates if s>= n]
    if enough:
        #   選座位數最小的那一個
        idx= min(enough, key=lambda x: x[1])[0]
    else:
        #  選座位數最小的那一個(剛好夠)
        idx = max(candidates, key=lambda x:x[1])[0]

    return idx
    

print (func4([3, 1, 5, 4, 3, 2], "101000", 2))
print (func4([1, 0, 5, 1, 3], "10100", 2))
print (func4([4, 6, 5, 8], "1000", 4))