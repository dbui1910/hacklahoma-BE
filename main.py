from flask import Flask, jsonify, request
import os

app = Flask(__name__)


def helloWorld():
    return "Hello World"
@app.route('/')
def home():
    return render_template('home.html')


@app.route('/')
def index():
    return jsonify({"Choo Choo": helloWorld()})


@app.route('/twillio')
def Send_Text():
    return "Messaging User"


@app.route('/process_location', methods=['POST'])
def Capture_Location():
    data = request.get_json()
    lat = data['latitude']
    lng = data['longitude']
    return "Current Location... Lat:", lat, "\tLong:", lng
user_latitude = 0.0
user_longitude = 0.0
@app.route('/test', methods=['POST'])
def test():
    output = request.get_json()
    result = json.loads(output) #this converts the json output to a python dictionary
    user_latitude = result['latitude']
    user_longitude = result['longitude']
    return result

# Load the JSON file
with open('response.json') as f:
    data = json.load(f)

# Get the longitude and latitude values
latitude_target = data['latitude']
longitude_target = data['longitude']

print("Longitude:", longitude_target)
print("Latitude:", latitude_target)

def is_within_radius(user_latitude, user_longitude, target_lat, target_lng):
    R = 3963.1676  # Earth's radius in miles
    lat1 = math.radians(user_latitude)
    lat2 = math.radians(float(latitude_target))
    lat_diff = math.radians(float(latitude_target) - user_latitude)
    lng_diff = math.radians(float(longitude_target) - user_longitude)
  
    a = (
        math.sin(lat_diff / 2) ** 2 +
        math.cos(lat1) * math.cos(lat2) * math.sin(lng_diff / 2) ** 2
    )
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c
  
    if distance <= 5:
        print('You are within 5 miles of the target location!')
    else:
        print('You are more than 5 miles away from the target location.')
  
    return distance <= 5  # Return True if distance is less than or equal to 5 miles


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
