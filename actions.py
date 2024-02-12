from playwright.sync_api import Page
import time
from pathlib import Path
from typing import Union


async def enter_credentials(page: Page, user: str, password: str) -> Union[str, None]:
    await page.wait_for_load_state("load")

    await page.locator('//*[@id="j_username"]').fill(user)
    await page.locator('//*[@id="j_password"]').fill(password)
    await page.click("#btn-login button")
 
    await page.wait_for_load_state("load")
    time.sleep(1)

    if await page.locator('//*[@id="invalid-login-or-password"]').is_visible():
        return "Usuário ou senha inválidos."

async def go_to_receipts(page: Page):

    await page.locator('//*[@id="receipts"]').click()
    await page.wait_for_load_state("load")
    time.sleep(2)


async def select_period(page: Page, start_date: str, end_date: str):
    await page.get_by_label("Data Prevista de Recebimento:").click()
    await page.wait_for_selector(".x-combo-list")

    for _ in range(4):
        await page.keyboard.press("ArrowDown")
    await page.keyboard.press("Enter")

    # Data de ínicio
    await page.keyboard.press("Tab")
    await page.locator(
        ".x-form-field-wrap.x-form-field-trigger-wrap.evc-periodfield-inicio.x-trigger-wrap-focus input"
    ).fill(start_date)

    # Data final
    await page.keyboard.press("Tab")
    await page.locator(
        ".x-form-field-wrap.x-form-field-trigger-wrap.evc-periodfield-termino.x-trigger-wrap-focus input"
    ).fill(end_date)


async def select_receipt_status(page: Page):
    await page.get_by_label("Status do Recebimento:").click()
    await page.locator('.x-combo-list-item span:has-text("A Receber")').click()

    await page.locator('//div[contains(text(), "Valor selecionado:")]').click()


async def get_search_results(page: Page):

    await page.get_by_role("button", name="Buscar").click()
    await page.wait_for_load_state("load")

    time.sleep(4)

    total_results = await page.query_selector(
        "td.x-toolbar-cell:nth-child(2) > div.x-form-display-field"
    )

    total_results = await total_results.inner_text()
    
    

    return int(total_results)


async def download_file(page: Page, download_path: Path):

    await page.keyboard.press("PageDown")
    await page.wait_for_load_state("load")
    await page.get_by_role("button", name="Exportar").click()

    time.sleep(1.5)

    async with page.expect_download() as download_info:
        await page.locator(
            '//div[@class="x-window-footer x-window-footer-noborder x-panel-btns"]//button[text()="Exportar"]'
        ).click()

    download = await download_info.value
    output_path = Path(str(download_path) + "/" + download.suggested_filename)
    await download.save_as(output_path)


