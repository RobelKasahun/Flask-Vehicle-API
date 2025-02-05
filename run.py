from app import routes
import os
from app.routes import app
from flask_cors import CORS

if __name__ == "__main__":
    CORS(app)
    port = int(os.environ.get("PORT", 8000))
    app.run(debug=True, host="0.0.0.0", port=port)
