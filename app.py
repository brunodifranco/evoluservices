import streamlit as st
from main import run
from playwright.sync_api import sync_playwright
import streamlit as st
from datetime import datetime, timedelta, date
from utils import select_folder

import os


def login_form():

    # Login
    st.sidebar.markdown("#### Entre suas credenciais")
    user = st.sidebar.text_input("Usuário")
    password = st.sidebar.text_input("Senha", type="password")

    return user, password


def date_form(date_format: str = "DD/MM/YYYY"):
    with st.form("Date"):

        start_date = st.date_input(
            "Data inicial", datetime.today() - timedelta(days=3), format=date_format
        )
        end_date = st.date_input("Data final",datetime.today() + timedelta(days=7), format=date_format)

        if not end_date >= start_date:
            st.error("Error: A data final deve ser maior ou igual a inicial.")

        st.form_submit_button("Selecione o período desejado")

        start_date_str = start_date.strftime("%d/%m/%Y")
        end_date_str = end_date.strftime("%d/%m/%Y")
        
        return start_date_str, end_date_str

# ARRUMAR ISSO DAQUI - COLOCAR PRA BAIXAR NA PASTA "downloads" QUE ESTA NO DIRETORIO (VER COMO PEGA ISSO, OCM OS.PWD POR EXEMPLO)
def path_form():

    with st.form("Path"):

        selected_folder_path = st.session_state.get("folder_path", None)

        folder_select_button = st.form_submit_button("Selecione o destino do arquivo")
        if folder_select_button:
            selected_folder_path = select_folder()
            st.session_state.folder_path = selected_folder_path

        if selected_folder_path:
            st.write("O arquivo será baixado para o destino:", selected_folder_path)

        return selected_folder_path

if __name__ == "__main__":
    # Title
    st.markdown(
        "<h1 style='text-align: center;'>Evoluservices Download App</h1>",
        unsafe_allow_html=True,
    )

    user, password = login_form()
    start_date, end_date = date_form()
    download_path = path_form()
    # download_path = "/home/bruno/evoluservices/"


    with st.form("Download"):

        submitted = st.form_submit_button(
            "Fazer Download do arquivo", use_container_width=True
        )

        if submitted and start_date and end_date and user and password and download_path:

            with sync_playwright() as playwright:
                run(
                    playwright=playwright,
                    url="https://signin.evoluservices.com/",
                    user=user,
                    password=password,
                    start_date=start_date,
                    end_date=end_date,
                    download_path=download_path,
                )
            
        elif submitted:
            st.error("Favor preencher todos os campos antes de baixar o arquivo!")
