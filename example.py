from cwl2nx import cwl_to_str, CWLToNetworkxConnector

dir = "workflow_example.cwl.yaml"

print(cwl_to_str(dir, verbose=False, display_colors="md"))
print(cwl_to_str(dir, verbose=False, display_colors="ANSI"))
# dag = CWLToNetworkxConnector(dir).convert_to_networkx()

# for each_node in dag.nodes:
#     print(dag.nodes[each_node])
