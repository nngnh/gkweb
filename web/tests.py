from django.test import TestCase

# Create your tests here.
data = [{"id": 1, "name": '名称1', "bid": 0},
        {"id": 2, "name": '名称2', "bid": 0},
        {"id": 3, "name": '名称3', "bid": 1},
        {"id": 4, "name": '名称4', "bid": 1},
        {"id": 5, "name": '名称5', "bid": 3},
        {"id": 6, "name": '名称6', "bid": 5}]

new_data = []  # 定义一个与 data 一模一样的新列表
d_data = []  # 定义一个最终需要的列表

for d in data:
    d["son"] = []
    new_data.append(d)
# 先为每一个元素，也就是每一个字典增加一个 key="son"

son_id = []  # 定义一个元素为所有子元素的 id 的列表

for d in data:
    for nd in new_data:  # 双层循环，寻求用笛卡尔积的模式来实现子节点嵌套
        if d["id"] == nd["bid"]:  # 如果一个元素的 bid 与另一个元素的 id 相同
            d["son"].append(nd)  # 就将另一个元素设为该元素的 “son” 键的值
            son_id.append(nd["id"])  # 将子元素的 id 记录到 son_id 列表
    if d["id"] not in son_id:  # 在外层循环中判断该元素的 id 是否在 son_id 列表中
        d_data.append(d)  # 如果不是，则将该元素添加到最终目标的 d_data 列表中
print(d_data)