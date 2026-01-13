from website import create_app
import os

app = create_app()

if __name__ == '__main__':
    port = int(os.evniron.get("PORT",10000))

    app.run(debug=False, port=port, host= "0.0.0.0")


