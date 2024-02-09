make venv:
	pip3 install virtualenv
	python3 -m venv .venv_evoluservices
make venvup:
	source .venv_evoluservices/bin/activate
make venvdown:
	deactivate
make build:
	pip3 install -r requirements.txt
	playwright install --with-deps firefox	
make run:
	streamlit run app.py
