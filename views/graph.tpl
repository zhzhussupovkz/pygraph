<html>
<head>
<title>{{title}}</title>
<style type="text/css">
  #container {
    max-width: 400px;
    height: 400px;
    margin: auto;
  }
</style>
</head>
<body>
<div id="graph-container">
</div>
<script src="/static/js/jquery-1.11.2.min.js"></script>
<script src="/static/js/sigma.min.js"></script>
<script src="/static/js/sigma.parsers.json.min.js"></script>
<script type="text/javascript">
    $(document).ready(function() {
        var g = $.parseJSON($('<div/>').html("{{data}}").text())
        var nodes = g.nodes;
        var len = nodes.length;
        for (var i = 0; i < len; i++) {
            nodes[i].x = Math.random();
            nodes[i].y = Math.random();
        }
        g.nodes = nodes
        s = new sigma({
            graph: g,
            container: 'graph-container',
            renderer: {
                container: document.getElementById('graph-container'),
                type: 'canvas'
            },
            settings: {
                defaultNodeColor: '#FF0000'
            }
        });
    });
</script>
</body>
</html>