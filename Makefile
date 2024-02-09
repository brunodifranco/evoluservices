build:
	sudo docker build -t evoluservices_app .
run:
	sudo docker run -d -p 8501:8501 --name evoluservices_container evoluservices_app
down:
	sudo docker stop evoluservices_container
	sudo docker rm -f evoluservices_container
streamlit: 
	streamlit run app.py
