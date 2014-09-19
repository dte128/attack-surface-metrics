__author__ = 'kevin'

import unittest
import os

from attacksurfacemeter import CallGraph
from loaders import CflowLoader

from tests.test_call_graph import CallGraphTestCase


class CallGraphReverseFileTestCase(CallGraphTestCase):
    def setUp(self):
        self.call_graph = CallGraph.from_loader(
            CflowLoader(
                os.path.join(os.path.dirname(os.path.realpath(__file__)), "helloworld/callgraph.r.txt"), True))

if __name__ == '__main__':
    unittest.main()