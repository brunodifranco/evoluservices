venv:
	pip3 install virtualenv
	python3 -m venv .venv_evoluservices
build:
	pip3 install -r requirements.txt
	playwright install --with-deps firefox	
remove:
	pip3 uninstall -r requirements.txt -y 
	playwright uninstall --all
	rm -rf .venv_evoluservices
run:
	streamlit run app.py
