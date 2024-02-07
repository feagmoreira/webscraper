# Web Scraper App Exercise

Web Scraper project was created using Falcon Web Framework and is hosted using the recomended WSGI web server for Waitress, for Windows enviroment. If application will be used in a non-Windows enrivonrment please use Gunicorn WSGI web server

## Usage Instructions
- Create directory where the project structure will be created.

Example:
```bash
mkdir webscrapper
```

- Extract zip file in the created directory.

<u>Windows Enviroment</u> <br>

Example:<br>

```cmd
expand source destination
expand 'C:\Users\user\downloads' 'C:\Users\user\Desktop\webscrapper'
```

<u>Non-Windows Enviroment</u> <br>
Example:<br>

```bash
unzip -d /dest/directory/ {file.zip} 
unzip -d /projects/webscraper/ webscraper.zip
```

- Create and activate Virtual Enviroment inside the created directory

<u>Windows Enviroment</u> <br>

Example:<br>

```cmd
cd webscraper
python -m venv .venv
.venv\Scripts\activate.bat
```

<u>Non-Windows Enviroment</u> <br>

Example:<br>

```bash
cd webscraper
python -m venv .venv
source .venv/bin/activate
```

- Install required libraries using requirements.txt file

<u>Windows Enviroment</u> <br>
Example:<br>

```cmd
pip install -r requirements.txt
```

<u>Non-Windows Enviroment</u> <br>
For non windows enviroments, the waitress library can be removed and Gunicorn must be installed. <br>

Example:<br>

```bash
pip install -r requirements.txt
pip install gunicorn
```

The list of libraries that will be installed in the virtual enviroment are: <br>
-falcon <br>
-waitress(windows) /gunicorn(non-windows) <br>
-mypy <br>
-pytest <br>

- Start Web Server (port 8000) that will host webscrapper app (virtual environment must be active)

<u>Windows Enviroment</u> <br>

```cmd
waitress-serve --port=8000 webscraper.app:app
```
<u>Non-Windows Enviroment</u> <br>

```bash
gunicorn webscraper.app
```

- Open index.html file located in the view folder, paste the desired Aptoide app link and click on submit request button to load app´s information. Error messages will be displayed as alerts for the user.

