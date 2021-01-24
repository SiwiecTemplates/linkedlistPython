# Testing my linked lists DDL
from pip._vendor.distlib.compat import raw_input

from sentinel_DLL import Sentinel_DLL

l = Sentinel_DLL()

def test_sentinel_DLL():
    # Prompt a user to input States

    l.append("Maine")
    l.append("Idaho")
    l.append("Utah")

    # Add Ohio after Idaho
    node = l.find("Idaho")
    if node is not None:
        print(node.get_data())
        l.insert_after(node, "Ohio")

    # Delete Idaho
    if node != None:
        l.delete(node)

    print("Hello, welcome to the linked list test. Here are some states:\n")
    print(l)

    state = raw_input("Please enter a state and press enter to add it to the list: ")
    while state != '-1':
        state = raw_input("Please enter a state or -1 to exit: ")
        if state != '-1':
            l.append(state)

    printList = raw_input("Would you like to print the list? Y/N").lower()
    if printList == 'y':
        print(l)
    if printList == 'n':
        exit(0)

    insertAnother = input("Would you like to insert a element between two states? Y/N").lower()
    if insertAnother == 'y':
        insertAfter = input("Enter the state which you would like to add an element after: ")
        insert = input("Enter the state you would like to add:")
        test_insert_after(insertAfter, insert)
    if insertAnother == 'n':
        exit(0)


    print("Here is the updated list: \n")
    print(l)


def test_insert_after(insAfter, ins):
    node = l.find(insAfter)
    if node is not None:
        l.insert_after(node, ins)
    else:
        print("The state selected to insert an element after does not exist. Please try again.")
        print("**press -1 to escape**")
        insAfter = input("Enter the state which you would like to add an element after: ")
        if insAfter != "-1":
            test_insert_after(insAfter, ins) # Recursion


test_sentinel_DLL()