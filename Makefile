build:
	pip install -r requirements.txt
	playwright install --with-deps firefox
run: 
	streamlit run app.py
