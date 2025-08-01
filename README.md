# 🚫 Hate Speech Detection API

[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A robust FastAPI-based Hate Speech Detection system that classifies text into different categories of offensive content. This project provides a complete machine learning pipeline from data processing to model serving with a user-friendly API.

## ✨ Features

- **Real-time Prediction**: Instant hate speech classification
- **RESTful API**: Built with FastAPI for high performance
- **Interactive Documentation**: Auto-generated API docs with Swagger UI
- **Complete ML Pipeline**: End-to-end solution from data processing to serving
- **Local-First**: No cloud dependencies required
- **Scalable**: Designed for easy deployment in production environments

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/hate-speech-detection.git
   cd hate-speech-detection
   ```

2. **Set up a virtual environment (recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: .\venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Prepare the dataset**
   - Place your `dataset.zip` file in the `data/` directory
   - The system will automatically extract and process it on first run

5. **Start the API server**
   ```bash
   python main.py
   ```

6. **Access the API**
   - Interactive API docs: http://127.0.0.1:8000/docs
   - Alternative API docs: http://127.0.0.1:8000/redoc

## 🛠️ API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/health` | GET | Check API status |
| `/train` | GET | Train or retrain the model |
| `/predict` | POST | Make predictions on input text |
| `/info` | GET | Get API and model information |
| `/docs` | GET | Interactive API documentation |

## 📂 Project Structure

```
hate-speech-detection/
├── main.py                 # Main FastAPI application
├── setup.py                 # Package configuration and distribution setup
├── requirements.txt        # Python dependencies
├── README.md              # Project documentation
├── data/                  # Dataset directory
│   └── dataset.zip        # Dataset file (not included in repo)
├── hate/                  # Core ML components
│   ├── components/        # ML pipeline components
│   ├── configuration/     # Configuration management
│   ├── constants/         # Project constants
│   ├── entity/           # Data structures and models
│   ├── exception/        # Custom exceptions
│   ├── ml/              # Model architecture
│   └── pipeline/         # Training and prediction pipelines
└── tokenizer.pickle      # Pre-trained tokenizer
```

## 🧪 Example Usage

### Using Python

```python
import requests

# Example prediction
response = requests.post(
    "http://127.0.0.1:8000/predict",
    json={"text": "Sample text to classify"}
)
print(response.json())
```

### Using cURL

```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/predict' \
  -H 'Content-Type: application/json' \
  -d '{"text": "Sample text to classify"}'
```

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 🙏 Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/) for the awesome web framework
- [scikit-learn](https://scikit-learn.org/) for machine learning tools


