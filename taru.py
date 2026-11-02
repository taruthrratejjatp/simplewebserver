from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<html>
    <head>
        <title>Computer Specification</title>
    </head>
    <header>
        <h1>Taruthrra Tejja TP (26010324)</h1>
    </header>
    <table border="1" cellpadding="5">
        <tr>
            <th>Device name</th>
            <th>Processor</th>
            <th>Installed RAM</th>
            <th>Graphics Card</th>
            <th>Storage</th>
            <th>Device ID</th>
            <Th>Product ID</Th>
            <th>System type</th>
            <th>Pen and Torch</th>
        </tr>
        <tr>
            <td>TL15-53M-G2</td>
            <td>Intel(R) Core(TM) 5 210H (2.20 GHz)</td>
            <td>16.0 GB (15.7 GB usable)</td>
            <td>Intel(R) Graphics (128 MB)</td>
            <td>132 GB of 477 GB used</td>
            <td>4D85838C-9BB5-4159-9C5C-5431C3C5EA4D</td>
            <td>00342-42954-08785-AAOEM</td>
            <td>64-bit operating system, x64-based processor</td>
            <td>No pen or touch input is available for this display</td>
        </tr>

    </table>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Client request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my own webserver is running successfully...")
httpd.serve_forever()