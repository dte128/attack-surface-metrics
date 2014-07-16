__author__ = 'kevin'


class BaseFormatter(object):

    def __init__(self, call_graph):
        """Constructor for BaseFormatter"""
        self.call_graph = call_graph

    def write_output(self):
        pass

    @property
    def source_dir(self):
        return self.call_graph.source_dir

    @property
    def nodes_count(self):
        return str(len(self.call_graph.nodes))

    @property
    def nodes(self):
        return self.call_graph.nodes

    @property
    def edges_count(self):
        return str(len(self.call_graph.edges))

    @property
    def edges(self):
        return self.call_graph.edges

    @property
    def entry_points_count(self):
        return str(len(self.call_graph.entry_points))

    @property
    def entry_points(self):
        return self.call_graph.entry_points
    
    @property
    def exit_points_count(self):
        return str(len(self.call_graph.exit_points))

    @property
    def exit_points(self):
        return self.call_graph.exit_points

    @property
    def execution_paths_count(self):
        return str(len(self.call_graph.execution_paths))

    @property
    def average_execution_path_length(self):
        return str(self.call_graph.avg_execution_path_length)

    @property
    def median_execution_path_length(self):
        return str(self.call_graph.median_execution_path_length)

    @property
    def execution_paths(self):
        return self.call_graph.execution_paths

    @property
    def entry_points_clustering(self):
        return str(self.call_graph.entry_points_clustering)

    @property
    def exit_points_clustering(self):
        return str(self.call_graph.exit_points_clustering)

    def get_closeness(self, call=None):
        if call:
            return str(self.call_graph.get_closeness(call))
        else:
            return self.call_graph.get_closeness().items()

    def get_betweenness(self, call=None):
        if call:
            return str(self.call_graph.get_betweenness(call))
        else:
            return self.call_graph.get_betweenness().items()

    def get_degree_centrality(self, call=None):
        if call:
            return str(self.call_graph.get_degree_centrality(call))
        else:
            return self.call_graph.get_degree_centrality().items()

    def get_in_degree_centrality(self, call=None):
        if call:
            return str(self.call_graph.get_in_degree_centrality(call))
        else:
            return self.call_graph.get_in_degree_centrality().items()

    def get_out_degree_centrality(self, call=None):
        if call:
            return str(self.call_graph.get_out_degree_centrality(call))
        else:
            return self.call_graph.get_out_degree_centrality().items()

    def get_degree(self, call=None):
        if call:
            return str(self.call_graph.get_degree(call))
        else:
            return self.call_graph.get_degree().items()

    def get_in_degree(self, call=None):
        if call:
            return str(self.call_graph.get_in_degree(call))
        else:
            return self.call_graph.get_in_degree().items()

    def get_out_degree(self, call=None):
        if call:
            return str(self.call_graph.get_out_degree(call))
        else:
            return self.call_graph.get_out_degree().items()

    def get_descendants_entry_point_ratio(self, call):
        return str(self.call_graph.get_descendants_entry_point_ratio(call))

    def get_descendants_exit_point_ratio(self, call):
        return str(self.call_graph.get_descendants_exit_point_ratio(call))

    def get_ancestors_entry_point_ratio(self, call):
        return str(self.call_graph.get_ancestors_entry_point_ratio(call))

    def get_ancestors_exit_point_ratio(self, call):
        return str(self.call_graph.get_ancestors_exit_point_ratio(call))

    def get_descendant_entry_points_count(self, call):
        return str(len(self.call_graph.get_descendant_entry_points(call)))

    def get_descendant_exit_points_count(self, call):
        return str(len(self.call_graph.get_descendant_exit_points(call)))

    def get_ancestor_entry_points_count(self, call):
        return str(len(self.call_graph.get_ancestor_entry_points(call)))

    def get_ancestor_exit_points_count(self, call):
        return str(len(self.call_graph.get_ancestor_exit_points(call)))

    def get_descendant_entry_points(self, call):
        return self.call_graph.get_descendant_entry_points(call)

    def get_descendant_exit_points(self, call):
        return self.call_graph.get_descendant_exit_points(call)

    def get_ancestor_entry_points(self, call):
        return self.call_graph.get_ancestor_entry_points(call)

    def get_ancestor_exit_points(self, call):
        return self.call_graph.get_ancestor_exit_points(call)

