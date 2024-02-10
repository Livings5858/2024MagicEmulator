import os

def copyList(numList):
    return numList.copy() + numList.copy()

def rotateList(numList, nameLength):
    for i in range(nameLength):
        num = numList.pop(0)
        numList.append(num)
    return numList

def insertList(numList, numLength, index):
    resList = numList[numLength:]
    top3List = numList[:numLength]
    resList[index:index] = top3List
    return resList

def popRootNum(numList):
    return numList.pop(0)

def popAndDelete(numList, numLength):
    for i in range(numLength):
        num = numList.pop(0)
        # print("delete: ", num)
    return numList

def rotateAndDelete(numList):
    while len(numList) > 1:
        numList = rotateList(numList, 1)
        print("好运留下来：拿一张放下面", numList[-1])
        print("烦恼丢出去：拿一张丢出去", numList[0])
        numList = popAndDelete(numList, 1)
        print("现在剩余的牌", numList)
    return numList

def main():
    # 准备四张牌
    numList = [1, 2, 3, 4]
    print("准备四张牌", numList)
    # 撕成2半，叠在一起
    numList = copyList(numList)
    print("撕成2半，叠在一起", numList)
    # 名字几个字，就拿几张牌放在底下
    numList = rotateList(numList, 2)
    print("名字几个字，就拿几张牌放在底下，以2个字为例: ", numList)
    # 拿起最上面三张，插在中间位置
    numList = insertList(numList, 3, 3)
    print("拿起最上面三张，插在中间位置", numList)
    # 拿起最上面的一张，等待一会验证
    checkNum = popRootNum(numList)
    print('拿起最上面的一张，等待一会验证: ', checkNum)
    print('剩余的牌：', numList)
    # 南方人拿起1张，北方2张，不知道南北3张，放中间
    numList = insertList(numList, 2, 3)
    print("南方人拿起1张，北方2张（以它为例），不知道南北3张，放中间",numList)
    # 男生1张，女生2张，扔到天上
    numList = popAndDelete(numList, 1)
    print("男生1张(以它为例)，女生2张，扔到天上",numList)
    # 见证奇迹的时刻，把上面的牌放在下面，循环7次
    numList = rotateList(numList, 7)
    print("见证奇迹的时刻，把上面的牌放在下面，循环7次:", numList)
    # 好运留下来：拿一张放下面
    # 烦恼丢出去：拿一张丢出去
    numList = rotateAndDelete(numList)
    # 最后剩一张牌
    if numList[0]==checkNum:
        checkMsg = "验证成功"
    else:
        checkMsg = "验证失败"
    print('最后剩一张牌', numList[0], '对比之前的牌', checkNum, checkMsg)


if __name__ == "__main__":
    main()

