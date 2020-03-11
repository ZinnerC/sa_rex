#!/usr/bin/env python

import py_trees

if __name__ == '__main__':

    root = py_trees.composites.Selector("Selector")
    high = py_trees.behaviours.Success(name="High Priority")
    med = py_trees.behaviours.Success(name="Med Priority")
    low = py_trees.behaviours.Success(name="Low Priority")
    root.add_children([high, med, low])

    behaviour_tree = py_trees.trees.BehaviourTree(root)
    behaviour_tree.setup(15)
    i = 0
    try:
        behaviour_tree.tick_tock(
            sleep_ms=500,
            #number_of_iterations=py_trees.trees.CONTINUOUS_TICK_TOCK,
            number_of_iterations=10,
            pre_tick_handler=None,
            post_tick_handler=None
        )
        print(10-i)
        i=+1
    except KeyboardInterrupt:
        behaviour_tree.interrupt()

py_trees.display.render_dot_tree(root) # this line work, the code only needs to be canceled since the upper if statement stays true