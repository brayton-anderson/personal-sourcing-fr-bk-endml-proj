from website import create_app
from website import db

if __name__ == "__main__":
    app = create_app()
    # app.run(debug=True)
    app.run(host="0.0.0.0", port=5000)
    # app.run(debug=True)
