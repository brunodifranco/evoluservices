import streamlit as st
from main import run
from playwright.sync_api import sync_playwright
from playwright.async_api import async_playwright
import streamlit as st
from datetime import datetime, timedelta
from utils import select_folder
from pathlib import Path
import asyncio

import sys
import os


def login_form():
    st.sidebar.markdown("#### Login")
    user = st.sidebar.text_input("Usuário")
    password = st.sidebar.text_input("Senha", type="password")

    return user, password


def date_form(date_format: str = "DD/MM/YYYY"):
    with st.form("Date"):

        start_date = st.date_input(
            "Data inicial", datetime.today() - timedelta(days=3), format=date_format
        )
        end_date = st.date_input(
            "Data final", datetime.today() + timedelta(days=7), format=date_format
        )

        if not end_date >= start_date:
            st.error("Erro: A data final deve ser maior ou igual a inicial.")

        st.form_submit_button("Selecione o período desejado")

        start_date_str = start_date.strftime("%d/%m/%Y")
        end_date_str = end_date.strftime("%d/%m/%Y")

        return start_date_str, end_date_str
    
async def main():

    st.markdown(
        "<h1 style='text-align: center;'>Evoluservices Download App</h1>",
        unsafe_allow_html=True,
    )

    user, password = login_form()
    start_date, end_date = date_form()
    download_path = Path(os.path.join(os.getcwd() + "/downloads"))

    with st.form("Download"):

        submitted = st.form_submit_button(
            "Fazer Download do arquivo", use_container_width=True
        )

        if (
            submitted
            and start_date
            and end_date
            and user
            and password
            and download_path
        ):

            for _ in range(3):
                try:
                    async with async_playwright() as playwright:
                        await run(
                            playwright=playwright,
                            url="https://signin.evoluservices.com/",
                            user=user,
                            password=password,
                            start_date=start_date,
                            end_date=end_date,
                            download_path=download_path,
                        )
                    break
                except TimeoutError:
                    st.warning("Tempo limite excedido. Tentando novamente...")
                    continue


        elif submitted:
            st.error("Favor preencher todos os campos antes de baixar o arquivo!")

if __name__ == "__main__":
    if sys.platform == "win32":
        loop = asyncio.ProactorEventLoop()
    else:
        loop = asyncio.SelectorEventLoop()

    asyncio.set_event_loop(loop)
    loop.run_until_complete(main())
