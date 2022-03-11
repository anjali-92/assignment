'''
Write a code to perform insert and delete operation
in given binary search tree.
'''


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def insert_into_bst(root: Node, val: int):
    if not root:
        return Node(val)
    if val >= root.value:
        root.right = insert_into_bst(root.right, val)
    else:
        root.left = insert_into_bst(root.left, val)
    return root


def maximum_from_subtree(node):
    while node.right:
        node = node.right
    return node


def delete_from_bst(root, val):
    if not root:
        return root

    if val < root.value:
        root.left = delete_from_bst(root.left, val)
    elif val > root.value:
        root.right = delete_from_bst(root.right, val)
    else:
        # if current node has only right child
        if not root.left:
            temp = root.right
            del root
            return temp

        # if current node has only left child
        if not root.right:
            temp = root.left
            del root
            return temp

        # if current node has both children
        temp = maximum_from_subtree(root.left)
        root.value = temp.value
        root.left = delete_from_bst(root.left, temp.value)
    return root


def print_bst_inorder(root, output):
    if root:
        print_bst_inorder(root.left, output)
        output.append(root.value)
        print_bst_inorder(root.right, output)


if __name__ == '__main__':
    root = None

    while True:
        print('''
               Please select one option: \n
               1. Insert value into BST \n
               2. Delete value from BST \n
               3. Press any number to terminate''')
        
        choice = int(input())
        if choice != 1 and choice != 2:
            break

        if choice == 1:            
            value = int(input('Enter value to insert.  '))
            root = insert_into_bst(root, value)
        elif choice == 2:
            value = int(input('Enter value to delete.  '))
            root = delete_from_bst(root, value)

        output = []
        print_bst_inorder(root, output)
        print(output)
