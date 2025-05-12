from flask import Flask, request, jsonify
from chartCalculator import get_planetary_positions
app = Flask(__name__)

@app.route('/calculate_chart', methods=['POST'])
def calculate_chart_endpoint():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Request must be JSON"}), 400

    birth_date = data.get('date')
    birth_time = data.get('time')
    latitude = data.get('latitude')
    longitude = data.get('longitude')
    timezone = data.get('timezone', '+03:00') # Default if not provided


    if not all([birth_date, birth_time, latitude is not None, longitude is not None]):
        return jsonify({"error": f"Missing required birth data: {birth_date}, {birth_time}, {latitude}, {longitude}"}), 400

    try:
        # Ensure latitude and longitude can be converted to float
        lat_float = float(latitude)
        lon_float = float(longitude)
    except ValueError:
        return jsonify({"error": "Invalid latitude or longitude format. Must be numbers."}), 400

    chart_result = get_planetary_positions(birth_date, birth_time, lat_float, lon_float, 3)
    
    if "error" in chart_result:
        # You might want to distinguish between client errors (4xx) and server errors (5xx)
        # For example, if the error is due to bad input from flatlib (e.g., invalid date format it couldn't catch)
        return jsonify(chart_result), 400 # Or 500 if it's an unexpected internal error
        
    return jsonify(chart_result)

if __name__ == '__main__':
    # This will run the Flask development server
    # For production, you'd use a proper WSGI server like Gunicorn or uWSGI
    app.run(debug=True, host='0.0.0.0', port=5001) # Changed port to 5001 to avoid conflict if you run script directly too