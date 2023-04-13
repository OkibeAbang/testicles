'''from linear.CSLL import CSLL
from SLL import *
from SNode import *
from DLL import *
from DNode import *
from StackLL import * 
from QueueLL import *'''



from build.lib.Datastructures.linear.SLL import SLL
from build.lib.Datastructures.linear.CSLL import CSLL
from build.lib.Datastructures.linear.CDLL import CDLL
from build.lib.Datastructures.linear.DLL import DLL
from build.lib.Datastructures.linear.QueueLL import QueueLL
from build.lib.Datastructures.linear.StackLL import StackLL

from build.lib.Datastructures.nodes.SNode import SNode
from build.lib.Datastructures.nodes.DNode import DNode


circle = SLL(SNode(15))
circle.InsertHead(SNode(15))
circle.InsertTail(SNode(15))
circle.InsertHead(SNode(15))
circle.InsertTail(SNode(122))
# circle.Search(SNode(122))
circle.Clear()
circle.SortedInsert(SNode(4))
circle.Insert(SNode(15), 2)
circle.InsertTail(SNode(225))
circle.Delete(SNode(15))
circle.Insert(SNode(53), 5)
circle.Insert(SNode(36), 3)
circle.Insert(SNode(9), 1)
circle.InsertHead(SNode(0))
circle.DeleteTail()
circle.DeleteHead()
print(circle.Print())
