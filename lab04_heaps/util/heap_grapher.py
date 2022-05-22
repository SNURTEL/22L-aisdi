import plotly.graph_objects as go
from typing import Tuple, List, Union
from lab04_heaps.src import AbstractHeap
from math import log


class HeapGrapher:
    """
    Class used for graphing binary trees
    """

    def __init__(self):
        """
        Inits class TreeGrapher
        """
        self._fig = None
        self._node_coords = []
        self._line_coords = []
        self._num_children = 0
        self._source_heap = None

    def graph_tree(self, heap: AbstractHeap) -> None:
        """
        Graphs a binary tree
        """
        self._set_source_heap(heap)
        self._get_all_node_coords()
        self._get_line_coords()
        self._make_graph()
        self._show_graph()

    def _set_source_heap(self, heap: AbstractHeap):
        self._fig = None
        self._node_coords = []
        self._num_children = heap.num_children
        self._source_heap = heap

    def _get_all_node_coords(self) -> None:
        """
        Builds (x, y) tuples for all nodes (where x is the node key and y is the level at which the node appears)
        and saves them to self._node_coords
        """
        height = int(log(len(self._source_heap.get_raw_data()), self._source_heap.num_children)) + 1

        self._node_coords = [(50 - 50 * (self._num_children ** h / y_idx), h) for h in range(height) for y_idx in range(1, self._num_children ** h)]

    #
    # def _get_node_and_children_coords(self, node: Node, parent_y: int) -> Tuple[Tuple[int]]:
    #     """
    #     Recursively builds (x, y) tuples for all nodes in a subtree rooted at a given node
    #     :param node: Subtree's root node
    #     :param parent_y: Parent node's y coordinate
    #     :return: A tuple of (x, y) tuples
    #     """
    #     l_coords = self._get_node_and_children_coords(
    #         node.l_child, parent_y + 1) if node.l_child else ()
    #     r_coords = self._get_node_and_children_coords(
    #         node.r_child, parent_y + 1) if node.r_child else ()
    #
    #     return (node.key, parent_y + 1), *l_coords, *r_coords  # pycharm u ok?

    def _get_line_coords(self):
        """
        Using a node coordinate list from self._node_coords a list containing start and end points of every line
        representing a parent-child relationship in a binary tree. Each set of coordinates is separated
        by a ((None, None)) tuple, preparing the data to be drawn with .add_trace(go.Scatter())
        :return: An example returned structure would look like this:
        [((x1, y1), (x2, y2)), ((None, None)), ((x1, y1), (x2, y2)), ((None, None))]
        """
        line_coords = []

        # last_y_occurrences = {0: 0}
        #
        # for i in range(1, len(self._node_coords)):
        #     end_coords = self._node_coords[i]
        #     last_y_occurrences[end_coords[1]] = i
        #     line_coords.append(
        #         (self._node_coords[last_y_occurrences[end_coords[1] - 1]], end_coords))

        # TODO implement


        for i in range(len(line_coords), 0, -1):
            line_coords.insert(i, ((None, None),))

        self._line_coords = line_coords

    def _make_graph(self) -> None:
        """
        Generates the tree graph using data from self._node_coords and self._get_line_coords()
        """
        self._fig = go.Figure()

        # converts to ((x1, x2, x3, ...), (y1, y2, y3, ...))
        nodes_x_y = tuple(zip(*self._node_coords))

        # converts to ((x11, x12, None, x21, x22, None, ...) (y11, y12, None, y21, y22, None, ...))
        flattened_lines_x_y = [
            pos for pair in self._line_coords for pos in pair]
        lines_x_y = tuple(zip(*flattened_lines_x_y))

        # lines
        self._fig.add_trace(go.Scatter(x=lines_x_y[0],
                                       y=lines_x_y[1],
                                       mode='lines',
                                       line={'color': 'rgb(210, 210, 210)',
                                             'width': 2},
                                       hoverinfo=None))

        # markers
        self._fig.add_trace(go.Scatter(x=nodes_x_y[0],
                                       y=nodes_x_y[1],
                                       mode='markers',
                                       name='nodes',
                                       marker=dict(symbol='circle-dot',
                                                   size=30,
                                                   color='#6175c1',
                                                   line=dict(color='rgb(50, 50, 50)',
                                                             width=2))))

        # self._fig['layout']['yaxis']['autorange'] = "reversed"

        xaxis = dict(showline=False, zeroline=False,
                     showgrid=False, showticklabels=False)
        yaxis = dict(showline=False, zeroline=False, showgrid=False,
                     showticklabels=False, autorange='reversed')

        self._fig.update_layout(annotations=self._get_annotations(),
                                font_size=18,
                                showlegend=False,
                                xaxis=xaxis,
                                yaxis=yaxis,
                                margin=dict(l=40, r=40, b=85, t=100),
                                hovermode='closest',
                                plot_bgcolor='rgb(248,248,248)')


    def _get_annotations(self, font_size: int = 10, font_color: str = 'rgb(250,250,250)') -> List[dict]:
        """
        Constructs an annotation dict for every node in a tree
        :param font_size: Font size
        :param font_color: Font
        :return: A list of plotly-style annotations for each node in the tree (same order as in self._node_coords)
        """
        return [dict(text=coords[0],
                     x=coords[0], y=coords[1],
                     font=dict(color=font_color, size=font_size),
                     showarrow=False, )
                for coords in self._node_coords]

    def _show_graph(self) -> None:
        """
        Renders the fig using a default renderer
        """
        self._fig.show()
