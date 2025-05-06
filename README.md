# yaml-to-resume
yaml-to-resume is a Python script to convert resume data in a yaml format and convert it into a pdf.
## Installation
Choose a directory to clone the project into using
```bash
git clone https://github.com/EvanLongmuir/yaml-to-resume.git
```
and install the requirements using `pip install -r requirements.txt`
## Usage
run the script with python
```bash
python app.py
```
```
usage: app.py [-h] [-y YAML] [-o OUTPUT] [-t TEMPLATE] [-l]

convert structured yaml data into a pdf resume

options:
  -h, --help            show this help message and exit
  -y, --yaml YAML       Choose yaml file (Default = data.yaml)
  -o, --output OUTPUT   Choose a name used for the outputed files (Default =
                        output)
  -t, --template TEMPLATE
                        Choose a template for the resume (Default =
                        template.tex)
  -l, --latex           When enabled script will output the filled in LaTeX
                        template
```
