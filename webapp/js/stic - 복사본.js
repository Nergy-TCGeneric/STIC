function draw() {
	
	var container = document.getElementById('testMap');
	
	var Nodes = [
		{id:1, label:"시작"},
		{id:2, label:"불의 발견"},
		{id:3, label:"수렵채집"},
		{id:4, label:"테스트4"}
	];
	
	var Edges = [
		{from:1, to:2, label:"어떻게 이걸 사용하지?"},
		{from:1, to:3},
		{from:1, to:4}
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