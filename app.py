from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Event-Driven Architecture | Flask on Kubernetes</title>
        <style>
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                margin: 0;
                padding: 0;
                background: linear-gradient(to right, #141e30, #243b55);
                color: white;
                text-align: center;
                overflow-x: hidden;
            }
            h1 {
                font-size: 2.5em;
                margin-top: 40px;
                color: #00d4ff;
                text-shadow: 0px 0px 15px rgba(0, 212, 255, 0.7);
                animation: glow 2s infinite alternate;
            }
            @keyframes glow {
                from { text-shadow: 0px 0px 10px #00d4ff; }
                to { text-shadow: 0px 0px 20px #00ffff; }
            }
            .container {
                width: 85%;
                margin: 0 auto;
                padding: 20px;
                line-height: 1.6;
                background: rgba(255, 255, 255, 0.08);
                border-radius: 12px;
                box-shadow: 0 0 20px rgba(0, 0, 0, 0.3);
                margin-top: 40px;
            }
            h2 {
                color: #00ffff;
                margin-top: 30px;
            }
            .architecture {
                display: flex;
                justify-content: space-around;
                align-items: center;
                flex-wrap: wrap;
                margin: 30px 0;
            }
            .box {
                width: 250px;
                padding: 15px;
                margin: 10px;
                background: rgba(0, 212, 255, 0.1);
                border: 1px solid #00d4ff;
                border-radius: 8px;
                transition: 0.3s;
            }
            .box:hover {
                transform: scale(1.05);
                background: rgba(0, 212, 255, 0.2);
            }
            footer {
                margin-top: 50px;
                font-size: 0.9em;
                color: #aaa;
            }
            a {
                color: #00ffff;
                text-decoration: none;
            }
            a:hover {
                text-decoration: underline;
            }
        </style>
    </head>
    <body>
        <h1>🚀 Event-Driven Architecture</h1>
        <div class="container">
            <p>
                Event-driven architecture (EDA) is a software design pattern that enables applications 
                to communicate through the production, detection, and reaction to events.
                It decouples services, allowing systems to be more scalable, flexible, and real-time.
            </p>

            <h2>💡 Architecture Overview</h2>
            <div class="architecture">
                <div class="box">
                    <h3>Producer</h3>
                    <p>Generates events — e.g., user action, sensor reading, or transaction.</p>
                </div>
                <div class="box">
                    <h3>Event Broker</h3>
                    <p>Acts as a central hub (Kafka, RabbitMQ, AWS SNS/SQS) that routes events to consumers.</p>
                </div>
                <div class="box">
                    <h3>Consumer</h3>
                    <p>Listens for specific events and performs a corresponding action.</p>
                </div>
            </div>

            <h2>⚙️ Benefits of Event-Driven Systems</h2>
            <ul style="text-align:left; display:inline-block; text-align:left; font-size:1.1em;">
                <li>🔁 <b>Loose Coupling</b> — Producers and consumers evolve independently.</li>
                <li>⚡ <b>Scalability</b> — Easily handle massive workloads through parallel processing.</li>
                <li>🧩 <b>Flexibility</b> — New event consumers can be added without changing existing logic.</li>
                <li>⏱️ <b>Real-Time Processing</b> — Immediate reaction to business events as they occur.</li>
                <li>🧠 <b>Resilience</b> — System remains operational even if one component fails.</li>
            </ul>

            <h2>📈 Example: E-commerce Checkout Flow</h2>
            <p>
                <b>Producer:</b> The checkout service emits an “OrderPlaced” event.<br>
                <b>Broker:</b> Kafka routes this event to multiple consumers.<br>
                <b>Consumers:</b> 
                - Inventory service updates stock, 
                - Email service sends confirmation, 
                - Analytics service logs order metrics.<br><br>
                Each consumer acts asynchronously and independently, improving speed and reliability.
            </p>
        </div>

        <footer>
            <p>Powered by Flask ⚙️ | Deployed with Kubernetes + ArgoCD 🚀 | Built by <a href="https://github.com/monis121hassan" target="_blank">Monis Hassan</a></p>
        </footer>
    </body>
    </html>
    """
    return render_template_string(html)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
