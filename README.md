# Paper-Recommender-2025

<pre>
Paper-Recommender-2025/
├─── app/      # Flask app files
│   ├─── static/      # Static assets
|   |   ├───ALIS-logo.png      # Logo
│   │   └─── favicon.ico       # Favicon
│   ├─── templates/      # HTML files
|   |   ├─── partials/      # Reusable HTML fragments
|   |   |   └─── _results.html    # partial template for rendering search results dynamically via AJAX
│   |   ├─── base.html      # Main layout template
|   |   └─── index.html      # Homepage template with the search form and dynamic result display
|   ├─── __init__.py      # Initializes the Flask app and sets up routing
|   ├─── interface_connector.py      # Bridges the frontend with the backend recommendation logic
|   └─── routes.py      # Defines the main web routes and handles request/response logic
├─── src/      # Backend / Recommender system
|   ├─── __init__.py      # Marks src as a Python module
|   ├─── config.py      # Central configuration of model paths, metadata, and global constants
|   ├─── encoder.py      # Handles model loading and text embedding generation
|   ├─── recommender.py      # The recommender system
|   └─── utils.py      # Provides utility functions for text normalization and metadata preprocessing
├─── .gitignore      # Excludes virtual environments, model files, etc.
├─── LICENSE      # Open-source license governing usage and distribution of the project  
├─── README.md      # This file
├─── run.py      # Entry point for launching the Flask app with Gunicorn  
└─── test_backend.py      # Script for testing backend recommender logic and model outputs
</pre>
