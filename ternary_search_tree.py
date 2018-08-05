
class Node:
    lo = None
    hi = None
    eq = None
    endpoint = False
    def __init__(self, char):
        self.char = char


    def insert(self,node, string):
        if len(string) == 0:
            return node

        head = string[0]
        tail = string[1:]
        if node is None:
            node = Node(head)

        if head < node.char:
            node.lo = self.insert(node.lo, string)
        elif head > node.char:
            node.hi = self.insert(node.hi, string)
        else:
            if len(tail) == 0:
                node.endpoint = True
            else:
                node.eq = self.insert(node.eq, tail)

        return node

    def search(self,node, string):
        if node is None or len(string) == 0:
            return False

        head = string[0]
        tail = string[1:]
        if head < node.char:
            return self.search(node.lo, string)
        elif head > node.char:
            return self.search(node.hi, string)
        else:
        # use 'and' for matches on complete words only,
        # versus 'or' for matches on string prefixes
            if len(tail) == 0 or node.endpoint:
                return True
            return self.search(node.eq, tail)


class trie:
    # a simple wrapper

    root = None
    def __init__(self, string):
        self.n=Node(string)
        self.append(string)
    def append(self, string):
        self.root = self.n.insert(self.root,string)
    def contains(self, string):
        return self.n.search(self.root, string)
