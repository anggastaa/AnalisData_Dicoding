# Proyek Akhir Dicoding Analis Data
## Dataset Characteristic
Both hour.csv and day.csv have the following fields, except hr which is not available in day.csv
	
	- instant: record index
	- dteday : date
	- season : season (1:springer, 2:summer, 3:fall, 4:winter)
	- yr : year (0: 2011, 1:2012)
	- mnth : month ( 1 to 12)
	- hr : hour (0 to 23)
	- holiday : weather day is holiday or not (extracted from http://dchr.dc.gov/page/holiday-schedule)
	- weekday : day of the week
	- workingday : if day is neither weekend nor holiday is 1, otherwise is 0.
	+ weathersit : 
		- 1: Clear, Few clouds, Partly cloudy, Partly cloudy
		- 2: Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist
		- 3: Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds
		- 4: Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog
	- temp : Normalized temperature in Celsius. The values are divided to 41 (max)
	- atemp: Normalized feeling temperature in Celsius. The values are divided to 50 (max)
	- hum: Normalized humidity. The values are divided to 100 (max)
	- windspeed: Normalized wind speed. The values are divided to 67 (max)
	- casual: count of casual users
	- registered: count of registered users
	- cnt: count of total rental bikes including both casual and registered
## Dashboard Link
[Bike Sharing Dashboard](https://cy66nsisuwygvgcyeziann.streamlit.app/)
## Setup Instructions

1. **Clone or Download the Repository**  
   Clone this repository or download the ZIP file and extract it.

   ```bash
   git clone https://github.com/your-repository-url.git
   cd your-repository-folder
2. **Create a Virtual Environment**
    It's recommended to create a virtual environment for the project.

    ```bash
    python -m venv env
    source env/bin/activate  # On macOS/Linux
    env\Scripts\activate     # On Windows
3. **Install Required Libraries**
    Install the libraries specified in [requirement.txt](https://github.com/anggastaa/AnalisData_Dicoding/blob/main/requirements.txt):
    ```bash
    pip install -r requirements.txt
4. **Run the Project**
    Run the dashboard application.
    ```bash
    streamlit run app.py
 
