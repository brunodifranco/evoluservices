import sys
import asyncio
import streamlit as st
from playwright.async_api import async_playwright, TimeoutError
from src.main import run
from src.utils import all_filled, login_input, date_input, path_input


async def main():
    """
    Roda o app do Streamlit com Playwright.
    """

    st.markdown(
        "<h1 style='text-align: center;'>Evoluservices Download App</h1>",
        unsafe_allow_html=True,
    )

    # Inputs
    user, password = login_input()
    start_date, end_date = date_input()
    download_path = path_input()

    with st.form("Download"):

        submitted = st.form_submit_button(
            "Fazer Download do arquivo", use_container_width=True
        )
        # Verifica se está tudo preenchido
        if all_filled(submitted, start_date, end_date, user, password, download_path):

            for _ in range(3):  # Tenta 3 vezes fazer o download
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
            else:
                st.error(
                    "Algum erro inesperado ocorreu. Todas as tentativas de download falharam."
                )

        elif submitted:
            st.error("Favor preencher todos os campos antes de baixar o arquivo!")


if __name__ == "__main__":

    # Verifica se está rodando no Linux ou Windows
    if sys.platform == "win32":
        loop = asyncio.ProactorEventLoop()
    else:
        loop = asyncio.SelectorEventLoop()

    asyncio.set_event_loop(loop)
    loop.run_until_complete(main())
