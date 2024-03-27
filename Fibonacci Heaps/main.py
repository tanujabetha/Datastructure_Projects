import fib 
object = fib.FibHeap()
object.insert(5)
object.insert(7)
object.insert(12)
n = object.insert(14)
object.insert(2)
#object.insert(1)
print('printing roots')
for node in  object.get_roots():
    print(f'Value: {node.val}')
    if node.parent is not None:
        print(f'Parent Value: {node.parent.val}')
    if len(node.children)>0:
        print(f'Children are:')
        for node in node.children:
            print(node.val)

print('Min value now')   
print(object.find_min().val)

print('deleting min')
object.delete_min()



print("Nodes after deletion")
for node in  object.get_roots():
    print(f'Value: {node.val}')
    if node.parent is not None:
        print(f'Parent Value: {node.parent.val}')
    if len(node.children)>0:
        print(f'Children are:')
        for node in node.children:
            print(node.val)
    
print("Min node now")
print(object.find_min().val)
print(n.parent.val)
print('Decrease priority')
object.decrease_priority(n, 1)


#After decreasing priority
print("Nodes after decreasing priority")
for node in  object.get_roots():
    print(f'Value: {node.val}')
    if node.parent is not None:
        print(f'Parent Value: {node.parent.val}')
    if len(node.children)>0:
        print(f'Children are:')
        for node in node.children:
            print(node.val)
    


