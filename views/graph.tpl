<html>
<head>
<title>{{title}}</title>
<style type="text/css">
  #container {
    max-width: 800px;
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
<script src="/static/js/draw.js"></script>

<script type="text/javascript">
    $(document).ready(function() {
        draw('/graph', 'graph-container');
    });
</script>
</body>
</html>