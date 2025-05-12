# Birth Chart API

A RESTful API service that calculates astrological birth charts based on birth date, time, and location coordinates.

## API Endpoint

```
POST https://birthchart-api.onrender.com/calculate_chart
```

### Request Body

```json
{
  "date": "YYYY/MM/DD",
  "time": "HH:MM",
  "latitude": number,
  "longitude": number,
  "timezone": "+HH:MM"  // Optional, defaults to "+03:00"
}
```

### Example Request

```bash
curl -X POST https://birthchart-api.onrender.com/calculate_chart \
-H "Content-Type: application/json" \
-d '{
  "date": "1990/01/01",
  "time": "12:00",
  "latitude": 41.0082,
  "longitude": 28.9784,
  "timezone": "+03:00"
}'
```

### Response

The API returns a JSON response containing planetary positions and other astrological data.

## Local Development

### Prerequisites

- Python 3.9 or higher
- pip (Python package manager)

### Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/birthchart-api.git
cd birthchart-api
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the development server:

```bash
python app.py
```

The server will start on `http://localhost:5001`

## Dependencies

- Flask - Web framework
- flatlib - Astrological calculations
- gunicorn - Production WSGI server

## Deployment

This API is deployed on Render using the configuration in `.render.yaml`.
