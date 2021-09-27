from autosuggestions.LinkedList import LinkedList
from autosuggestions.Trie import TrieNode

def main():
    sort_by_popularity_test()



def remove_test():
    #remove head
    l = LinkedList(1,2,3,4,5)
    l.remove(0)
    assert l.printAll() == "2 -> 3 -> 4 -> 5", "remove_test -remove head fail, Should be 2 -> 3 -> 4 -> 5 but got " + l.printAll()
    assert str(l.head) == '2', 'head should be 2 but got ' + str(l.head)
    assert str(l.tail) == '5', 'tail should be 5 but got ' + str(l.tail)

    #remove tail
    l = LinkedList(1,2,3,4,5)
    l.remove(4)
    assert l.printAll() == "1 -> 2 -> 3 -> 4", "remove_test -remove tail fail, Should be 1 -> 2 -> 3 -> 4 but got " + l.printAll()
    assert str(l.head) == '1', 'head should be 1 but got ' + str(l.head)
    assert str(l.tail) == '4', 'tail should be 4 but got ' + str(l.tail)

    #remove middle
    l = LinkedList(1,2,3,4,5)
    l.remove(2)
    assert l.printAll() == "1 -> 2 -> 4 -> 5", "remove_test -remove middle fail, Should be 1 -> 2 -> 4 -> 5 but got " + l.printAll()
    assert str(l.head) == '1', 'head should be 1 but got ' + str(l.head)
    assert str(l.tail) == '5', 'tail should be 5 but got ' + str(l.tail)

def sort_by_popularity_test():
    # test 1 / two numbers
    t1 = TrieNode('a')
    t2 = TrieNode('b')

    t1.called_times = 20
    t1.isWord = True

    t2.called_times = 30
    t2.isWord = True

    l = LinkedList(t1,t2)
    l.sort_by_popularity(1,30)

    assert l.printAll() == "b -> a", "sort_by_popularity_test fail, Should be b -> a but got " + l.printAll()
    # print(l.printAll())

    # test 2 / three numbers
    t2 = TrieNode('b')
    t1 = TrieNode('a')
    t3 = TrieNode('c')

    t1.called_times = 20
    t1.isWord = True

    t3.called_times = 50
    t3.isWord = True

    t2.called_times = 30
    t2.isWord = True

    l = LinkedList(t2,t1, t3)
    l.sort_by_popularity(2,50)

    assert l.printAll() == "c -> b -> a", "sort_by_popularity_test fail, Should be c -> b -> a but got " + l.printAll()


def replace_test():
    # testing middle numbers replace
    l = LinkedList(1, 2, 3, 4, 5, 6)
    l.replace(l.head.next, l.head.next.next.next.next, l.head, l.head.next.next.next)
    assert l.printAll() == "1 -> 5 -> 3 -> 4 -> 2 -> 6", "testing middle numbers replace Should be 1 -> 5 -> 3 -> 4 -> 2 -> 6"

    # testing head replace
    l = LinkedList(1, 2, 3, 4, 5, 6)
    l.replace(l.head, l.head.next.next, None, l.head.next)
    assert l.printAll() == "3 -> 2 -> 1 -> 4 -> 5 -> 6", "testing head replace Should be 3 -> 2 -> 1 -> 4 -> 5 -> 6"

    # testing tail replace
    l = LinkedList(1, 2, 3, 4, 5, 6)
    l.replace(l.head.next, l.head.next.next.next.next.next, l.head, l.head.next.next.next.next)
    assert l.printAll() == "1 -> 6 -> 3 -> 4 -> 5 -> 2", "testing tail replace Should be 1 -> 6 -> 3 -> 4 -> 5 -> 2"

    # testing head-tail replace
    l = LinkedList(1, 2, 3, 4, 5, 6)
    l.replace(l.head, l.head.next.next.next.next.next, None, l.head.next.next.next.next)
    assert l.printAll() == "6 -> 2 -> 3 -> 4 -> 5 -> 1", "testing head-tail replace Should be 6 -> 2 -> 3 -> 4 -> 5 -> 1"

    # testing two numbers replace
    l = LinkedList(1, 2)
    l.replace(l.head, l.head.next, None, l.head)
    assert l.printAll() == "2 -> 1", "testing two numbers replace fail, Should be 2 -> 1"

    # testing two three number replace
    l = LinkedList(1, 2, 3)
    l.replace(l.head.next, l.head.next.next, l.head, l.head.next)
    assert l.printAll() == "1 -> 3 -> 2", "testing two three number replace fail, Should be 1 -> 3 -> 2"


if __name__ == '__main__':
    main()

