class Record:
    def __init__(self, record_id, parent_id):
        self.record_id = record_id
        self.parent_id = parent_id

class Node:
    def __init__(self, node_id):
        self.node_id = node_id
        self.children = []

def BuildTree(records):
    if not records:
        return 
    records.sort(key=lambda x: x.record_id)
    for record in range(len(records)):
        if records[record].record_id!=record:
            raise ValueError("Record id is invalid or out of order.")
        if records[record].parent_id>records[record].record_id:
            raise ValueError("Node parent_id should be smaller than it's record_id.")
        if record!=0 and records[record].parent_id==records[record].record_id:
            raise ValueError("Only root should have equal record and parent id.")      
      
    nodes=[Node(record.record_id) for record in records]
    root=[node for node in nodes if node.node_id in {record.parent_id for record in records}]
    for node in root:
        node.children=[nodes[nd] for nd in range(1,len(records)) if records[nd].parent_id==node.node_id]
    
    return nodes[0]
            
               
            