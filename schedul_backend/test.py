import datetime
import json
column = "[asd]"

aa = [{"aa":"123","as":"1"},{"aa":"12","as":"2"},{"aa":"234","as":"2"},{"aa":"12","as":"3"},{"aa":"123","as":"3"},{"aa":"234","as":"4"}]
bb = []
for a in aa:
    flag = 0
    for b in bb:
        if a.get("aa")== b.get("aa"):
            flag = 1
            b["as"] = int(a.get("as"))+int(b.get("as"))
    if flag == 0:
        bb.append(a)

print(bb)

# f = [{"aa":"123"},{"aa":"234"},{"aa":"23"}]
# g = [{"aa":"123"},{"aa":"345"}]
# hh = []
# for i in f:
#     hh.append(i)
# for i in g:
#     if i not in hh:
#
#         hh.append(i)
# print(hh)
# asdas = ""
# aa = json.loads(asdas)
print("ss")

aa = datetime.datetime.strftime(datetime.datetime.now(),'%Y-%m-%d %H:%M:%S')
if isinstance(datetime.datetime.now(), datetime.datetime) == True:
    print("sas")