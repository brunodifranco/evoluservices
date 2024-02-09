venv:
	pip3 install virtualenv
	python3 -m venv .venv_evoluservices
up:
	( 
	source .venv_evoluservices/bin/activate; \
	)
	
down:
	deactivate		
build:
	pip3 install -r requirements.txt
	playwright install --with-deps firefox	
run:
	streamlit run app.py
