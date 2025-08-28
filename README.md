# Data_Scientist_In_Python


#### how to run the python file
```bash
# 0. Create a virtual environment (if not already created)
python3 -m venv venv    

# 1. From source directory. Activate the virtual environment
source venv/bin/activate   

# 2. Install dependencies
pip3 install requests pandas numpy openpyxl xlrd

#  or
echo "requests
pandas
numpy
openpyxl
xlrd" > requirements.txt
pip3 install -r requirements.txt # to install all dependencies
pip3 list # to verify the installations

# 3. Run the Python script
python3 importing_data_in_python/fetch_data.py
python3 importing_data_in_python/scrape_web.py
python3 importing_data_in_python/api_json.py
```
