var s,
g = {
    nodes: [ {% for node in node_list %}
            {
                id: '{{ node.namespaced_key }}',
                label: '{{ node.title }}',
                x: Math.random(),
                y: Math.random(),
                size: 1,
                color: '#666'
            }, {% endfor %}
    ],
    edges: [ {% for edge in edge_list %}
            {
                id: 'edge{{forloop.counter}}',
                source: "{{ edge.start }}",
                target: "{{ edge.end }}",
                size: 1,
                color: '#ccc'
            } {% endfor %}
    ]
};
s = new sigma({
    graph: g,
    container: 'sigma-container'
});