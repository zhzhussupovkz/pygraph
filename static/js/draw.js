function draw(graphUrl, graphContainer) {
    $.ajax({
        url: graphUrl,
        type: "GET",
        success: function(data) {
            var g = $.parseJSON(data)
            var nodes = g.nodes;
            var edges = g.edges;

            var container = document.getElementById(graphContainer);
            var data= {
                nodes: nodes,
                edges: edges,
            };
            var options = {
                width: '800px',
                height: '600px',
                edges: {
                    style: 'arrow',
                    arrowScaleFactor: 0.5,
                }
            };
            var network = new vis.Network(container, data, options);
        }
    });
}