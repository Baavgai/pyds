# Python Data Structures

Just an implementation of basic data structures in python.

This is not really for use in any real project.
Any functionality found in custom rolled ADTs will doubtless be found in more battle hardened libraries.
If you're a python programmer, just use `list` or `dict` until you can't.

If you're a student and want to know how some random programmer might implement a
[linked list](https://en.wikipedia.org/wiki/Linked_list) or a [binary tree](https://en.wikipedia.org/wiki/Binary_search_tree), you're in the right place.

## Linked List

You might do a simple list node like so:

```python
class Node:
    def __init__(self, value, next=None):
        self.value, self.next  = value, next
```

What methods would you add?  In reality, a node in a list shouldn't really have any brains.  It's just data.
With this in mind, I'd approach this more functionally:

```python
def create_node(value, next=None):
    return (value, next)
```

While we loose the names value and next, a simple tuple buys us immutability and a lack of ambiguity.

Building a list is as simple as:

```python
def insert_value(container, value):
    return create_node(value, container)
```

## Immutability

The value of immutability is debatable for some of these dynamic structures.  The above code is basically a LISP style
[cons](https://en.wikipedia.org/wiki/Cons) list.  Changing such a list involves making another copy.  Sort of.
Because Python does garbage collection, you can actually leverage a lot of that old school functional programming goodness.
e.g. a copy can keep a lot of what already been allocated without throwing it away.  Well, in theory.

If immutability is not a concern, then more imperative implementations will make other standard operations faster and easier, if not safer.

## Binary Tree

A tree node can be:

```python
def create_node(value, left=None, right=None):
    return (value, left, right)
```

Or, if mutable:

```python
def create_node(value, left=None, right=None):
    return [value, left, right]
```
