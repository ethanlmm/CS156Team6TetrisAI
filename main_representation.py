import kb


request_rule1 = ["add_shape", "L"]
request_rule2 = ["add_shape", "I"]
request_rule3 = ["add_shape", "O"]
request_rule4 = ["add_shape", "S"]
request_rule5 = ["add_shape", "Z"]
request_rule6 = ["add_shape", "J"]
request_rule7 = ["add_shape", "T"]

request_fact1 = ["update_board",("I",(1,0))]
request_fact2 = ["update_board", ("I",(2,0))]
request_fact3 = ["update_board",("I",(4,0))]
request_fact4 = ["update_board",("I",(5,0))]

request_rule_update = ["remove_shape","L"]
request_board_display = ["display_board",""]
request_board_remove = ["remove_row", 2]


# a. create a KB
knowledge_base = kb.kb()

# b. Insert at least four representation into the KB
knowledge_base.kb_ask(request_rule1)
knowledge_base.kb_ask(request_rule2)
knowledge_base.kb_ask(request_rule3)
knowledge_base.kb_ask(request_rule4)
knowledge_base.kb_ask(request_rule5)
knowledge_base.kb_ask(request_rule6)
knowledge_base.kb_ask(request_rule7)

# c. Insert at least four facts into the KB
knowledge_base.kb_ask(request_fact1)
knowledge_base.kb_ask(request_fact2)
knowledge_base.kb_ask(request_fact3)
knowledge_base.kb_ask(request_fact4)

# d. Updating and removing rules in the KB
knowledge_base.kb_ask(request_rule_update)

# e. Updating and removing facts in the KB
# Pieces(facts) in Tetris is not modify individually,
# instead they become part of the board and will be 
# updated as a whole. 
knowledge_base.kb_ask(request_board_remove)

# f. Display contents of a KB
# all the previous steps display the content using print
knowledge_base.kb_ask(request_board_display)

# g. Delets a KB
knowledge_base.__init__()




