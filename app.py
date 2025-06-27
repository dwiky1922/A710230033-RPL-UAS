from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def main():
    return render_template_string("""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Halo dari Flask!</title>
            <style>
                body { font-family: Arial, sans-serif; text-align: center; padding: 50px; background-color: #f4f4f4; }
                h1 { color: #333; }
                button {
                    padding: 10px 20px;
                    font-size: 16px;
                    background-color: #007bff;
                    color: white;
                    border: none;
                    border-radius: 5px;
                    cursor: pointer;
                }
                button:hover {
                    background-color: #0056b3;
                }
                #response {
                    margin-top: 20px;
                    font-size: 18px;
                    color: #444;
                }
            </style>
        </head>
        <body>
            <h1>Halo, saya Dwiky Abyantara Murdianto</h1>
            <p>NIM: A710230033</p>
            <button onclick="showResponse()">Tanya Kabar</button>
            <div id="response"></div>

            <script>
                function showResponse() {
                    document.getElementById('response').innerHTML = "Saya baik, bagaimana dengan kamu?";
                }
            </script>
        </body>
        </html>
    """)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
