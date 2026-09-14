from fastapi.testclient import TestClient
import sys
import os

# Ensure the server directory is in path so we can import main
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import app

client = TestClient(app)

def test_get_locations():
    response = client.get("/api/locations")
    assert response.status_code == 200
    data = response.json()
    assert "locations" in data
    assert isinstance(data["locations"], list)
    assert len(data["locations"]) > 0

def test_predict_home_price_valid():
    response = client.post(
        "/api/predict",
        json={
            "total_sqft": 1000,
            "location": "1st Phase JP Nagar",
            "bhk": 2,
            "bath": 2
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert "estimated_price" in data
    assert isinstance(data["estimated_price"], float)

def test_predict_home_price_invalid_sqft():
    response = client.post(
        "/api/predict",
        json={
            "total_sqft": -100, # Invalid sqft
            "location": "1st Phase JP Nagar",
            "bhk": 2,
            "bath": 2
        }
    )
    assert response.status_code == 422 # Unprocessable Entity (Validation Error)
