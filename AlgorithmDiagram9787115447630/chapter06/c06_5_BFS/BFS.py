""" 广度搜索算法 """
from collections import deque

""" 从你的社交关系网中找到芒果销售商:
 01 你的社交关系：
 
      /-ALICE -----> PEGGY
     /                |
    /                 |-->
 You --------------------> BOB -----> ANUJ
    \
     \-----> CLAIRE -----> THOM
                   \
                    \
                     \-----> JONNY
 
 02 目标芒果销售商：名字以M结尾
 """


# 判断一个人是否是芒果销售商
def person_is_seller(name):
    return name[-1] == 'm'


# 查找芒果销售商的方法
def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []  # 这个数组用于记录检查过的人
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:  # 仅当这个人没检查过时才检查
            if person_is_seller(person):
                print(person + " is a mango seller!")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)  # 将这个人标记为检查过
    return False


# 初始化你的社交关系网
graph = {
    "you": ["alice", "bob", "claire"],
    "bob": ["anuj", "peggy"],
    "alice": ["peggy"],
    "claire": ["thom", "jonny"],
    "anuj": [],
    "peggy": [],
    "thom": [],
    "jonny": []
}

search("you")
