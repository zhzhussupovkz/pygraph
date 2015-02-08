<html>
<head>
<title>{{title}}</title>
<style type="text/css">
  #container {
    max-width: 800;
    height: 600px;
    margin: auto;
  }
</style>
</head>
<body>
<div id="graph-container">
</div>
<script src="/static/js/jquery-1.11.2.min.js"></script>
<script src="/static/js/vis.min.js"></script>

<script type="text/javascript">
    $(document).ready(function() {
        $.ajax({
            url: "/rgraph",
            type: "GET",
            success: function(data) {
                var g = $.parseJSON(data)
                var nodes = g.nodes;
                var edges = g.edges;

                var container = document.getElementById('graph-container');
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
    });
</script>
</body>
</html>