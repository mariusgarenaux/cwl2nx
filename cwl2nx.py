import yaml
import networkx as nx
import matplotlib.pyplot as plt
from cwl_utils.parser import load_document_by_uri, Workflow
from cwl_utils.parser.cwl_v1_0 import LoadingOptions
import os


class CWLToNetworkx:
    def __init__(self, cwl_path: str):
        """
        Initialize the connector.
        Parse and validate the cwl file, with cwl_utils library.

        Parameters :
        ---

        - cwl_path: path to the cwl file
        """
        self.cwl_path = cwl_path
        self.verbose_node_names = True
        self.cwl_utils_graph: Workflow = self.parse_and_validate_cwl()
        self.nx_graph: nx.DiGraph = nx.DiGraph()

    def parse_and_validate_cwl(self) -> Workflow:
        """
        Parse the cwl in an Workflow object from cwl_utils
        parser submodule.
        """
        try:
            loading_options = LoadingOptions(no_link_check=True)
            parsed_cwl = load_document_by_uri(
                self.cwl_path, loadingOptions=loading_options
            )
            # add a proper label for each step TODO : add custom labels
            for each_step in parsed_cwl.steps:
                if self.verbose_node_names:
                    each_step.label = each_step.id
                else:
                    each_step.label = each_step.id.split("/")[-1]

        except Exception:
            raise Exception(f"Could not parse and validate the cwl file.")
        else:
            return parsed_cwl

    def convert_to_networkx(self):
        """
        Convert the cwl_utils.parser.Workflow in a networkx graph.
        """
        color_step = "blue"
        shape_step = "o"
        size_step = 500

        color_input = "green"
        shape_input = "s"
        size_input = 150

        for each_step in self.cwl_utils_graph.steps:
            self.nx_graph.add_node(each_step.id)
            self.nx_graph.nodes[each_step.id]["color"] = color_step
            self.nx_graph.nodes[each_step.id]["shape"] = shape_step
            self.nx_graph.nodes[each_step.id]["size"] = size_step
            self.nx_graph.nodes[each_step.id]["label"] = each_step.id.split("/")[-1]
            self.nx_graph.nodes[each_step.id]["cwl"] = {
                "source_object": each_step,
                "node_type": "step",
            }

            for each_input in each_step.in_:
                self.nx_graph.add_node(each_input.source)
                self.nx_graph.nodes[each_input.source]["color"] = color_input
                self.nx_graph.nodes[each_input.source]["shape"] = shape_input
                self.nx_graph.nodes[each_input.source]["size"] = size_input
                self.nx_graph.nodes[each_input.source]["label"] = (
                    each_input.source.split("/")[-1]
                )
                self.nx_graph.nodes[each_input.source]["cwl"] = {
                    "source_object": each_input,
                    "node_type": "input",
                }
                self.nx_graph.add_edge(each_input.source, each_step.id)

            for each_output in each_step.out:
                self.nx_graph.add_node(each_output)
                self.nx_graph.nodes[each_output]["color"] = color_input
                self.nx_graph.nodes[each_output]["shape"] = shape_input
                self.nx_graph.nodes[each_output]["size"] = size_input
                self.nx_graph.nodes[each_output]["label"] = each_output.split("/")[-1]
                self.nx_graph.nodes[each_output]["cwl"] = {
                    "source_object": each_output,
                    "node_type": "output",
                }
                self.nx_graph.add_edge(each_step.id, each_output)

        if not nx.is_directed_acyclic_graph(self.nx_graph):
            raise Exception(f"The parsed graph is not a DAG (Directed Acyclic Graph).")

        return self.nx_graph

    def plot(self):
        nx.display(G=self.nx_graph)
        plt.show()


if __name__ == "__main__":
    dir = "workflow.yaml"
    dag = CWLToNetworkx(dir).convert_to_networkx()
    nx.display(dag)
    plt.show()
