from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html>
    <head>
        <title>
            Tabular column
        </title>
    </head>
    <body>
        <table border="2" cellpadding="2">
            <tr>
                <th>S.No</th>
                <th>Specifications</th>
                <th>Type</th>
            </tr>
            <tr>
                <td>1</td>
                <td>Device name</td>
                <td>TMP215-75-G2</td>
            </tr>
            <tr>
                <td>2</td>
                <td>Processor</td>
                <td>Intel(R) Core(TM) Ultra 5 125H (1.20 Ghz)</td>
            </tr>
            <tr>
                <td>3</td>
                <td>Installed RAM</td>
                <td>16.0 GB (15.5 GB usable)</td>
            </tr>
            <tr>
                <td>4</td>
                <td>Device ID</td>
                <td>72ACA473-F6AC-40A8-A41A-EEA4D6DA7C85</td>
            </tr>
            <tr>
                <td>5</td>
                <td>Product ID</td>
                <td>00342-42784-48514-AAOEM</td>
            </tr>
        </table>
    </body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()