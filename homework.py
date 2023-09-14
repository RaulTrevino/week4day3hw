#
#
#    linked list are made up of nodes that contain 2 parts the data 'what u want to store' and a pointer that points to the next node
#    they do not have indexes but they know where to position themselves based ont the value of the previous nodes.
#   
#   to add a new node in the beginning of a linked list you create a new node and set its pointer to the head of a list and then it 
#   will become the new head of the linked list. to add to the middle of a list ex: 1-2-3-4 and i want to add 5 between 2 and 3 i 
#   would have to create a node 5 then point it to node 3 and would also make node 2 point to 5 making 1-2-5-3-4.
#
#   to remove node from the middle of a list ex: 3 from 1-2-3-4-5 you would have to make node 2 point to node 4 and that would remove
#   node 3 from linked list and the output would become 1-2-4-5