from playwright.sync_api import sync_playwright, Playwright
from pathlib import Path
import streamlit as st

import time


from actions import (
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

    browser = await playwright.firefox.launch(headless=True)
    # page = await browser.new_context(viewport={"width": 1920, "height": 1040}).new_page()
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
            browser.close()

        else:
            await browser.close()
            st.error(
                "O período escolhido não retornou nenhum resultado. Favor escolher outro período."
            )

        time.sleep(3)
    else:
        st.error(
            "Usuário ou senha inválidos."

        )


# if __name__ == "__main__":

#     with sync_playwright() as playwright:
#         run(
#             playwright=playwright,
#             url="https://signin.evoluservices.com/",
#             start_date="04/09/23",
#             end_date="27/02/24",
#             download_path="/home/bruno/Downloads/",
#         )
