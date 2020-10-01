"""
实现一个大顶堆
    0
  1   2
3 4  5 6

大顶堆中
父节点n 的两个子节点序号为 2*n+1, 2*n+2
子节点n 的父节点序号为 (n-1)//2
"""
class big_heap:
    def __init__(self):
        # 数组存放堆中元素
        self.heap_list = []
        self.heap_size = 0

    def push(self, num):
        self.heap_size += 1
        self.heap_list.append(num)
        # 初始位置直接丢到最后
        num_index = self.heap_size - 1
        # 从下往上调整堆结构
        while num_index != 0:
            if self.heap_list[(num_index - 1) // 2] > self.heap_list[num_index]:
                break
            else:
                tmp = self.heap_list[num_index]
                self.heap_list[num_index] = self.heap_list[(num_index - 1) // 2]
                self.heap_list[(num_index - 1) // 2] = tmp
                num_index = (num_index - 1) // 2

    def pop(self):
        # 空堆，报错
        if self.heap_size == 0:
            print("empty heap !")
            return
        self.heap_size -= 1

        if self.heap_size < 2:
            self.heap_list.pop(0)
            return

        # 堆顶元素用堆尾元素替换，然后从上往下调整堆结构
        self.heap_list[0] = self.heap_list[-1]
        self.heap_list.pop()

        num_index = 0
        while True:
            if num_index * 2 + 1 >= self.heap_size:
                break
            # 选择子节点中较大的进行比较交换
            elif num_index * 2 + 2 >= self.heap_size or \
                self.heap_list[num_index * 2 + 1] > self.heap_list[num_index * 2 + 2]:
                change_index = num_index * 2 + 1
            else:
                change_index = num_index *2 + 2
            # 与子节点比较交换
            if self.heap_list[num_index] > self.heap_list[change_index]:
                break
            else:
                tmp = self.heap_list[num_index]
                self.heap_list[num_index] = self.heap_list[change_index]
                self.heap_list[change_index] = tmp
                # 节点变为子节点，进行迭代
                num_index = change_index


if __name__ == "__main__":
    a = big_heap()
    a.push(12)
    a.push(11)
    a.push(10)
    a.push(9)
    a.push(6)
    a.push(7)
    a.push(8)
    a.push(13)
    for i in range(a.heap_size + 2):
        a.pop()
        print(a.heap_list)
