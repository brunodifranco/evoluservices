import time
from pathlib import Path
from playwright.async_api import Playwright
import streamlit as st
from src.actions import (
    enter_credentials,
    go_to_receipts,
    select_period,
    select_receipt_status,
    get_search_results,
    download_file,
)


async def run(
    playwright: Playwright,
    url: str,
    user: str,
    password: str,
    start_date: str,
    end_date: str,
    download_path: Path,
):
    """
    Executa o processo de login, navegação e download de arquivos em uma página web.

    Parameters
    ----------
    playwright : Playwright
        Instância do Playwright usada para lançar o navegador.
    url : str
        URL da página web.
    user : str
        Nome de usuário para login.
    password : str
        Senha para login.
    start_date : str
        Data de início do período de busca no formato "DD/MM/YYYY".
    end_date : str
        Data de término do período de busca no formato "DD/MM/YYYY".
    download_path : Path
        Caminho onde o arquivo será baixado.
    """

    browser = await playwright.firefox.launch(headless=True)
    page = await browser.new_page()
    await page.goto(url)

    login_output = await enter_credentials(page, user, password)

    if not isinstance(login_output, str):

        await go_to_receipts(page)

        await select_period(page, start_date, end_date)

        await select_receipt_status(page)

        total_results = await get_search_results(page)

        if total_results != 0:
            await download_file(page, download_path)
            st.success("Arquivo baixado com sucesso!")
            await browser.close()

        else:
            await browser.close()
            st.error(
                "O período escolhido não retornou nenhum resultado. Favor escolher outro período."
            )

        time.sleep(3)
    else:
        st.error("Usuário ou senha inválidos.")
