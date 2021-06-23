# pretend B-tree
from math import ceil

M = 5
max_child = M
max_keys = max_child -1
min_keys = int(ceil(M/2))-1


class BTreeNode:
    def __init__(self):
        self.leaf = False
        self.key = []
        self.cnt_key = 0
        self.child = []
        self.cnt_child = 0


root = None


def search_node(node, val):
    if not node:
        print("Empty tree")
        return 0
    level = node
    while 1:
        i = 0
        while i < level.cnt_key:
            if level.key[i] == val:
                print("key %d exists!" % val)
                return 1
            elif level.key[i] > val:
                break
            i += 1
        if level.leaf:
            break
        level = level.child[i]
    print("key %d dose not exist" % val)
    return 0


# 값을 넣어서 노드를 만듬.
def create_node(val):
    new_node = BTreeNode()
    new_node.leaf = False
    new_node.key[0] = val
    new_node.cnt_key = 1
    new_node.cnt_child = 0
    return new_node


# 노드 값을 분리해서 다른 노드에 분배하는 함수
def split_node(pos: int, node: BTreeNode, p_node: BTreeNode):
    median = node.cnt_key//2
    right_node = BTreeNode()
    right_node.leaf = node.leaf
    right_node.cnt_key = 0
    right_node.cnt_child = 0
    num_iter = node.cnt_key
    # 분리할 노드에 키 담기
    for i in range(median+1, num_iter):
        right_node.key[i-(median+1)] = node.key[i]
        right_node.cnt_key += 1
        node.cnt_key -= 1
    # 현재 노드가 리프가 아니면 자식노드도 분리
    if not node.leaf:
        num_iter = node.cnt_child
        for j in range(median+1, num_iter):
            right_node.child[j-median+1] = node.child[j]
            right_node.cnt_child += 1
            node.cnt_child -= 1
    if node == root:
        new_p_node = create_node(node.key[median])
        node.cnt_key -= 1
        new_p_node.child[0] = node
        new_p_node.child[1] = right_node
    else:
        for i in range(p_node.cnt_key, pos, -1):
            p_node.key[i] = p_node.key[i-1]
            p_node.child[i+1] = p_node.child[i]
        p_node.key[pos] = node.key[median]
        p_node.cnt_key += 1
        node.cnt_key -= 1
        p_node.child[pos+1] = right_node
        p_node.cnt_child += 1
    return node


def insert_node(p_pos: int, val: int, node: BTreeNode, p_node: BTreeNode) -> BTreeNode:
    pos = 0
    while pos < node.cnt_key:
        if node.key[pos] == val:
            print("Duplicates are not permitted!")
            return node
        elif node.key[pos] > val:
            break
        pos += 1
    if not node.leaf:
        node.child[pos] = insert_node(pos, val, node.child[pos], node)
        if node.cnt_key == max_keys + 1:
            node = split_node(p_pos, node, p_node)
    else:
        for i in range(node.cnt_key, pos, -1):
            node.key[i] = node.key[i-1]
            node.child[i+1] = node.child[i]
        node.key[pos] = val
        node.cnt_key += 1
        if node.cnt_key == max_keys + 1:
            node = split_node(p_pos, node, p_node)
    return node


def insert(val):
    global root
    if not root:
        root = create_node(val)
        root.left = 1
        return
    else:
        root = insert_node(0, val, root, root)


# 못 빌릴 때 합치는 함수
def merge_node(p_node, node_pos, mer_node_pos):
    merge_idx = p_node.child[mer_node_pos].cnt_key
    p_node.child[mer_node_pos].key[merge_idx] = p_node.key[mer_node_pos]
    p_node.child[mer_node_pos].cnt_key += 1
    for i in range(p_node.child[node_pos].cnt_key):
        p_node.child[mer_node_pos].key[merge_idx+1+i] = p_node.child[node_pos].key[i]
        p_node.child[mer_node_pos].cnt_key += 1
    merge_child_idx = p_node.child[mer_node_pos].cnt_child
    for i in range(p_node.child[mer_node_pos].cnt_child):
        p_node.child[mer_node_pos].child[merge_child_idx+i] = p_node.child[node_pos].child[i]
        p_node.child[mer_node_pos].cnt_child += 1
    del p_node.child[node_pos]
    for i in range(p_node.cnt_key-1):
        p_node.key[i] = p_node.key[i+1]
    p_node.cnt_child -= 1


# 왼쪽에서 빌리는 함수
def borrow_from_left(p_node: BTreeNode, cur_node_pos: int):
    tenant_idx = 0
    for i in range(p_node.child[cur_node_pos]):
        p_node.child[cur_node_pos].key[i+1] = p_node.child[cur_node_pos].key[i]
    p_node.child[cur_node_pos].key[tenant_idx] = p_node.key[cur_node_pos-1]
    p_node.child[cur_node_pos].cnt_key += 1

    idx_from_sib_to_par = p_node.child[cur_node_pos - 1].cnt_key - 1
    p_node.key[cur_node_pos - 1] = p_node.child[cur_node_pos - 1].key[idx_from_sib_to_par]
    p_node.child[cur_node_pos - 1].cnt_key -= 1

    if p_node.child[cur_node_pos-1].cnt_child > 0:
        tenant_child_idx = p_node.child[cur_node_pos - 1].cnt_child - 1
        for i in range(p_node.child[cur_node_pos].cnt_child):
            p_node.child[cur_node_pos].child[i] = p_node.child[cur_node_pos].child[i - 1]
        p_node.child[cur_node_pos].child[0] = p_node.child[cur_node_pos].child[tenant_child_idx]
        p_node.child[cur_node_pos].cnt_child += 1
        p_node.child[cur_node_pos-1].cnt_child -= 1


# 오른쪽에서 빌리는 함수
def borrow_from_right(p_node, cur_node_pos):
    tenant_idx = p_node.child[cur_node_pos].cnt_key
    p_node.child[cur_node_pos].key[tenant_idx] = p_node.key[cur_node_pos]
    p_node.child[cur_node_pos].cnt_key += 1
    idx_from_sib_to_par = 0
    p_node.key[cur_node_pos] = p_node.child[cur_node_pos + 1].key[idx_from_sib_to_par]
    for i in range(p_node.child[cur_node_pos+1].cnt_key - 1):
        p_node.child[cur_node_pos + 1].key[i] = p_node.child[cur_node_pos + 1].key[i + 1]
    p_node.child[cur_node_pos + 1].cnt_key -= 1
    idx_from_sib = 0
    # 자식 노드 정리
    if p_node.child[cur_node_pos + 1].cnt_child > 0:
        tenant_child_idx = p_node.child[cur_node_pos].cnt_child
        p_node.child[cur_node_pos].child[tenant_child_idx] = p_node.child[cur_node_pos + 1].child[idx_from_sib]
        p_node.child[cur_node_pos].cnt_child += 1
        for i in range(p_node.child[cur_node_pos+1].cnt_child - 1):
            p_node.child[cur_node_pos + 1].child[i] = p_node.child[cur_node_pos + 1].child[i + 1]
        p_node.child[cur_node_pos + 1].cnt_child -= 1


def balance_node(node, child_pos):
    # 제일 왼쪽
    if not child_pos:
        if node.child[child_pos + 1].cnt_key > min_keys:
            borrow_from_right(node, child_pos)
        else:
            merge_node(node, child_pos+1, child_pos)
        return
    # 제일 오른쪽
    elif child_pos == node.cnt_key:
        if node.child[child_pos - 1].cnt_key > min_keys:
            borrow_from_left(node, child_pos)
        else:
            merge_node(node, child_pos, child_pos - 1)
        return
    # 나머지의 경우
    else:
        if node.child[child_pos - 1].cnt_key > min_keys:
            borrow_from_left(node, child_pos)
        elif node.child[child_pos + 1].cnt_key.min_keys:
            borrow_from_right(node, child_pos)
        else:
            merge_node(node, child_pos, child_pos - 1)
        return


# 내부노드 기준으로 자식들을 erge해야 하는 케이스
def merge_child_node(p_node, cur_node_pos):
    merge_idx = p_node.child[cur_node_pos].cnt_key
    val_p_node = p_node.key[cur_node_pos]
    p_node.child[cur_node_pos].key[merge_idx] = p_node.key[cur_node_pos]
    p_node.child[cur_node_pos].cnt_key += 1

    # 합치려는 노드에 형제 노드 값을 가지고 옴
    for i in range(p_node.child[cur_node_pos+1].cnt_key):
        p_node.child[cur_node_pos].key[merge_idx+1+i] = p_node.child[cur_node_pos+1].key[i]
        p_node.child[cur_node_pos].cnt_key += 1

    # 형제노드 자식도 들고와야 함
    for i in range(p_node.child[cur_node_pos+1].cnt_child):
        p_node.child[cur_node_pos].child[merge_idx+1+i] = p_node.child[cur_node_pos+1].child[i]
        p_node.child[cur_node_pos].cnt_child += 1

    # 부모노드(내부노드)의 키를 줬으니까 재배열 & 자식도 재배열
    for i in range(cur_node_pos, p_node.cnt_key):
        p_node.key[i] = p_node.key[i+1]
        p_node.cnt_key -= 1
    for i in range(cur_node_pos+1, p_node.cnt_child):
        p_node.child[i] = p_node.child[i+1]
        p_node.cnt_child -= 1
    return val_p_node


# predecessor 찾는 함수
def find_predecessor(cur_node):
    if cur_node.leaf:
        return cur_node.key[cur_node.cnt_key-1]
    find_predecessor(cur_node.child[cur_node.cnt_child - 1])


# predecessor 찾아서 내부노드에 덮어 씌우는 함수
def override_with_predecessor(p_node: BTreeNode, pos_std_search: int):
    predecessor = find_predecessor(p_node.child[pos_std_search])
    predecessor.key[pos_std_search] =predecessor
    return predecessor


# successor 찾는 함수
def find_successor(cur_node):
    if cur_node.leaf:
        return cur_node.key[0]
    return find_successor(cur_node.child[0])


# successor를 찾아 내부 노드에 덮어 씌우는 함수
def override_with_successor(p_node, pos_std_search):
    successor = find_successor(p_node.child[pos_std_search + 1])
    p_node.key[pos_std_search] = successor
    return successor


# 내부 노드에서 값을 지우는 함수
def delete_inner_node(cur_node: BTreeNode, cur_node_pos: int) -> None:
    if cur_node.child[cur_node_pos].cnt_key >= cur_node.child[cur_node_pos+1].cnt_key:
        if cur_node.child[cur_node_pos].cnt_key > min_keys:
            cessor = override_with_predecessor(cur_node, cur_node_pos)
            delete_val_from_node(cessor, cur_node.child[cur_node_pos])
        else:
            deletion_for_merge = merge_child_node(cur_node, cur_node_pos)
            delete_val_from_node(deletion_for_merge, cur_node.child[cur_node_pos])
    else:
        if cur_node.child[cur_node_pos+1].cnt_key > min_keys:
            cessor = override_with_successor(cur_node, cur_node_pos)
            delete_val_from_node(cessor, cur_node.child[cur_node_pos + 1])
        else:
            deletion_for_merge = merge_child_node(cur_node, cur_node_pos)
            delete_val_from_node(deletion_for_merge, cur_node.child[cur_node_pos])


# 노드랑 지우는 값을 넣어주면 지우는 함수
def delete_val_from_node(val: int, node: BTreeNode):
    flag = False
    pos = 0
    while pos < node.cnt_key:
        if node.key[pos] == val:
            flag = True
            break
        elif node.key[pos] > val:
            break
        pos += 1
    if flag:
        if node.leaf:
            for i in range(pos, node.cnt_key):
                node.key[i] = node.key[i+1]
            node.cnt_key -= 1
        else:
            delete_inner_node(node, pos)
        return flag
    else:
        if node.leaf:
            return flag
        else:
            flag = delete_val_from_node(val, node.child[pos])
    if node.child[pos].cnt_key < min_keys:
        balance_node(node, pos)
    return flag


def delete(node: BTreeNode, val: int):
    global root
    if not node:
        print("Empty tree")
        return
    flag = delete_val_from_node(val, node)
    if not flag:
        print("%d does not exist in this tree" % val)
        return
    if not node.cnt_key:
        node = node.child[0]
    root = node


def print_tree(node, level):
    if not node:
        print("Empty tree!")
        return
    print("Level %d :   " % level, end="")
    for i in range(level-1):
        print("\t\t", end="")
    for i in range(node.cnt_key):
        print("%d " % node.key[i], end="")
    print()
    level += 1
    for i in range(node.cnt_child):
        print(node.child[i], level)


def main():
    insert(10)
    insert(20)
    insert(30)
    insert(40)
    insert(50)
    insert(60)
    insert(70)
    print_tree(root, 1)
    print("*"*20)
    delete(root, 103)
    delete(root, 70)
    delete(root, 130)
    print_tree(root, 1)
    search_node(root, 30)
    return 0


if __name__ == "__main__":
    main()
