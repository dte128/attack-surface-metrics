import os
import subprocess

import networkx as nx

from attacksurfacemeter import utilities
from attacksurfacemeter.call import Call
from attacksurfacemeter.granularity import Granularity
from attacksurfacemeter.loaders.base_loader import BaseLoader
from attacksurfacemeter.loaders.stack import Stack


class CflowLoader(BaseLoader):
    """"""
    def __init__(self, source, reverse=False, defenses=None,
                 vulnerabilities=None):
        """Constructor for CflowParser.

        Parameters
        ----------
        source : str
            The absolute path to a text file containing the call graph
            generated using cflow or the absolute path to a directory
            containing the source files for which a call graph must be
            generated using cflow.
        reverse : bool
            If true, the call graph is assumed to have been created using the
            cflow's -r option.
        defenses : list, optional
            A list of Call objects, each representing a designed defense in the
            system.
        vulnerabilities : list, optional
            A list of Call objects, each representing a vulnerable function in
            the system.
        """
        super(CflowLoader, self).__init__(
            source, reverse, defenses, vulnerabilities
        )

    def load_call_graph(self, granularity=Granularity.FUNC):
        """Load a call graph generated by cflow.

        If necessary, the static call graph generation utility (cflow) is
        invoked to generate the call graph before attempting to load it.

        Parameters
        ----------
        granularity : str
            The granularity at which the call graph must be loaded. See
            attacksurfacemeter.granularity.Granularity for available choices.

        Returns
        -------
        call_graph : networkx.DiGraph
            An object representing the call graph.
        """
        call_graph = nx.DiGraph()
        parent = Stack()

        raw_call_graph = None
        if os.path.isfile(self.source):
            raw_call_graph = open(self.source)
        elif os.path.isdir(self.source):
            raw_call_graph = self._exec_cflow()

        try:
            previous = Call.from_cflow(raw_call_graph.readline(), granularity)
            for line in raw_call_graph:
                current = Call.from_cflow(line, granularity)

                if current.level > previous.level:
                    parent.push(previous)
                elif current.level < previous.level:
                    for t in range(previous.level - current.level):
                        parent.pop()

                if parent.top:
                    caller = callee = None
                    entry = exit = dangerous = defense = False
                    if self.is_reverse:
                        caller = current
                        callee = parent.top
                    else:
                        caller = parent.top
                        callee = current

                    (caller_attrs, callee_attrs) = utilities.get_node_attrs(
                        'cflow', caller, callee, self.defenses,
                        self.vulnerabilities
                    )

                    call_graph.add_node(caller, caller_attrs)

                    if callee_attrs is not None:
                        call_graph.add_node(callee, callee_attrs)

                        # Adding the edge caller --  callee
                        attrs = {'cflow': None, 'call': None}
                        call_graph.add_edge(caller, callee, attrs)

                        # Adding the edge callee -- caller with the assumption
                        #   that every call must return
                        attrs = {'cflow': None, 'return': None}
                        call_graph.add_edge(callee, caller, attrs)

                previous = current
        finally:
            if raw_call_graph:
                raw_call_graph.close()

        return call_graph

    def _exec_cflow(self):
        """Execute cflow as a subprocess and return its output.

        Parameters
        ----------
        None

        Returns
        -------
        stdout : file
            An instance of a file object representing the output from cflow.
        """
        cflow_exe = 'run_cflow.sh'
        if self.is_reverse:
            cflow_exe = 'run_cflow_r.sh'

        dirname = os.path.dirname(os.path.realpath(__file__))
        proc = subprocess.Popen(
            '{0} {1}'.format(os.path.join(dirname, cflow_exe), self.source),
            stdout=subprocess.PIPE,
            shell=True,
            universal_newlines=True
        )

        return proc.stdout
