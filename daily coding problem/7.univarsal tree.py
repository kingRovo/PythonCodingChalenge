def is_unival(root):
    return unival_helper(root, root.value)

def unival_helper(root, value):
    if root is None:
        return True
    if root.value == value:
        return unival_helper(root.left, value) and unival_helper(root.right, value)
    return False
