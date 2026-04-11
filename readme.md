### Use Bash!
Setup script.
```shell
git clone https://github.com/shaspire/serd-rpo5-24r-p2.git &&
cd ./serd-rpo5-24r-p2 &&
python -m venv venv &&
source ./venv/bin/activate &&
pip install -r ./src/req.txt
```

Collect Static, Migrations and Superuser.
Assuming execution from root of repository.
```shell
python src/manage.py collectstatic &&
python src/manage.py makemigrations &&
python src/manage.py migrate &&
python src/manage.py createsuperuser
```
