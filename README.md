# Hate Speech Detection 

## 🚀 Quick Start

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Add dataset**: Place `dataset.zip` in the `data/` directory

3. **Start the API**:
   ```bash
   python main.py
   ```

4. **Access the API**: Visit `http://127.0.0.1:8000/docs`

## 📁 Project Structure

```
Hate-Speech-Detection/
├── main.py                 # Main FastAPI application
├── demo.py                 # Demo script for testing
├── test_imports.py         # Import verification script
├── requirements.txt        # Python dependencies
├── README.md              # This file
├── data/                  # Dataset directory
│   └── dataset.zip        # Dataset file (you need to provide this)
├── hate/                  # Core ML components
│   ├── components/        # ML pipeline components
│   ├── configuration/     # Local data management
│   ├── constants/         # Configuration constants
│   ├── entity/           # Data structures
│   ├── exception/        # Error handling
│   ├── ml/              # Model architecture
│   └── pipeline/         # Training and prediction pipelines
└── tokenizer.pickle      # Pre-trained tokenizer
```

## 🔧 API Endpoints

- `GET /health` - Health check
- `GET /train` - Train the model
- `POST /predict` - Predict hate speech in text
- `GET /info` - API information
- `GET /docs` - Interactive API documentation


## 📊 Features

- **Local Data Management**: No cloud dependencies
- **FastAPI Web API**: RESTful API with auto-generated docs
- **Complete ML Pipeline**: Data ingestion, transformation, training, evaluation
- **Real-time Prediction**: Instant hate speech detection
- **Simple Setup**: Easy local deployment

## 🔒 Local Deployment

- ✅ No cloud setup required
- ✅ Faster data access
- ✅ No cloud costs
- ✅ Works offline
- ✅ Full control over environment
- ✅ Easy debugging and testing

## 📝 Usage Example

```python
import requests

# Predict hate speech
response = requests.post(
    "http://127.0.0.1:8000/predict",
    json={"text": "I hate you and hope you die"}
)
result = response.json()
print(f"Prediction: {result['prediction']}")
```

