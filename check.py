#!/usr/bin/python

import pep8
import mccabe
import sys
import ast
from ast import iter_child_nodes

fname = sys.argv[1]


def make_mccabe_visitor(fname):
    with open(fname, "rU") as mod:
        code = mod.read()
    tree = compile(code, fname, "exec", ast.PyCF_ONLY_AST)
    visitor = mccabe.PathGraphingAstVisitor()
    visitor.preorder(tree, visitor)
    return visitor


v = make_mccabe_visitor(fname)
for graph in v.graphs.values():
    c = graph.complexity()
    if c > 5:
        text = 'has cc of {}, too complex!'.format(c)
    else:
        text = 'has cc of {}, looks ok'.format(c)
    print(graph.name, text)

p8 = pep8.Checker(fname)
p8.check_all()
