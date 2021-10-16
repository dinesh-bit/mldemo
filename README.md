..bash
requirements file
 
echo >> requirements.txt
pip install -r requirements.txt
....

echo >> README.md

...bash
creating directories and files
echo >>template.py
python template.py
...

mkdir data_given


...bash
initializing git and dvc
git init
dvc init
dvc add data_given/BankNote_Authentication.csv
.....

...bash
To keep track of our code
git add .
git commit -m "first commit"
....

...bash
Adding Origin
git remote add origin http://github.com/dinesh-bit/mldemo.git
git branch  -M main
git push -u origin main
....




