import streamlit as st
from src.main import run
from playwright.sync_api import sync_playwright
import streamlit as st
from datetime import datetime

# from utils import upload_file_to_s3


if __name__ == "__main__":
    # Title
    st.markdown(
        "<h1 style='text-align: center;'>Teste</h1>",
        unsafe_allow_html=True,
    )

    # Sidebar
    with st.form("Período"):
        start_date = st.sidebar.date_input("Start date")
        end_date = st.sidebar.date_input("End date")
        if start_date < end_date:
            st.success("Start date: `%s`\n\nEnd date:`%s`" % (start_date, end_date))
        else:
            st.error("Error: End date must fall after start date.")

    ## CONTINUAR A PARTIR DAQUI (mas antes testar o docker com streamlit (ver link))
        submitted = st.form_submit_button(
            "Fazer o Download do arquivo", use_container_width=True
        )

        if submitted and start_date and end_date:
            with sync_playwright() as playwright:
                run(
                    playwright=playwright,
                    url="https://signin.evoluservices.com/",
                    start_date="04/09/23",
                    end_date="27/02/24",
                    download_path="/home/bruno/Downloads/",
                )
            st.success("Arquivo baixado com sucesso!")
