<html>
    <head>
        <title>{{title}}</title>
        <meta http-equiv="content-type" content="text/html; charset=utf-8">
        <link rel="stylesheet" type="text/css" href="/static/css/main.css">
    </head>

    <body>
        <div id="container">

            <div id="header">
                <h1>{{header}}</h1>
            </div>

            <div id="wrapper">
                <div id="content">
                <p>
                    <div id='graph-container'></div>
                </p>
                </div>
            </div>

            <div id="navigation">
                <p>
                    <ul>
                        <li><a href="https://github.com/zhzhussupovkz/pygraph">Github</a></li>
                        <li><a href="https://python.org">Python</a></li>
                        <li><a href="http://visjs.org/">vis.js</a></li>
                    </ul>
                </p>
            </div>

            <div id="extra">
                <p><strong>{{header}}</strong></p>
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur venenatis nunc viverra sapien gravida, at lobortis ante malesuada. Duis a aliquet ipsum. Fusce dictum neque molestie felis euismod porttitor. In hac habitasse platea dictumst. Etiam non ultricies sem. Quisque auctor consequat nunc. Aenean vitae vestibulum lacus. Cras bibendum orci ut elit egestas sollicitudin.</p>
                <p>Nunc et tempor arcu, nec consequat justo. Nullam fringilla dignissim aliquam. Maecenas lacinia blandit mauris sit amet aliquet. Etiam venenatis consequat metus at tincidunt. Nulla egestas sapien sit amet vestibulum efficitur. Nulla justo leo, placerat vitae egestas vitae, mollis ac eros. Suspendisse vitae ante ut dolor porttitor scelerisque. Curabitur et dignissim orci. Duis sed sem sit amet neque euismod blandit sed ut nisl. Sed vel lorem nec quam vestibulum eleifend vel ut est. Sed justo ante, dignissim nec velit ultricies, pulvinar finibus dolor.</p>
            </div>

            <div id="footer">
                <p>Pygraph 2015</p>
                <script src="/static/js/jquery-1.11.2.min.js"></script>
                <script src="/static/js/vis.min.js"></script>
                <script src="/static/js/draw.js"></script>

                <script type="text/javascript">
                    $(document).ready(function() {
                        draw('/rgraph', 'graph-container');
                    });
                </script>
            </div>

        </div>
    </body>
</html>