function draw() {
	
	var container = document.getElementById('testMap');
	
	var Nodes = [
		{id:1, label:"테스트"},
		{id:2, label:"test2"}
	];
	
	var Edges = [
		{from:1, to:2}
	];
	
	var data = {
		nodes: Nodes,
		edges: Edges
	};
	
	var options = {
		nodes : {
			shape: 'dot',
			size: 30,
			font: {
				color: '#ffffff'
			}
		}
	};
	
	var network = new vis.Network(container, data, options);
}

window.onload = draw();