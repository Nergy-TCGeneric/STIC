function draw() {
	
	var container = document.getElementById('testMap');
	
	var Nodes = [
		{id:1, label:"ㅜ_ㅜ"},
		{id:2, label:"자료가 부족합니다 -_-"},
		{id:3, label:"검증된 자료여야 합니다."},
		{id:4, label:"Vis.js에 의한 로드 지연은 없어야 합니다."},
		{id:5, label:"군대 가기 전까지 빨리 만드쇼 -.-"}
	];
	
	var Edges = [
		{from:1, to:2},
		{from:1, to:3},
		{from:1, to:4},
		{from:1, to:5}
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