from datetime import datetime
from pathlib import Path

from playwright.sync_api import sync_playwright


SPREADSHEET_URL = (
    "https://docs.google.com/spreadsheets/d/"
    "1_vy216XmrivXZLFosfxT3TLmpHHnyX2lgbhk3f7P-DY/"
    "edit#gid=0"
)

SAVE_DIR = Path("screenshots")

VIEWPORT = {
    "width": 1920,
    "height": 1080,
}


def make_screenshot_path(save_dir: Path = SAVE_DIR) -> Path:
    now_text = datetime.now().strftime("%Y%m%d_%H%M%S")
    return save_dir / f"screenshot_{now_text}.png"


def capture_spreadsheet(
    save_path: str | Path | None = None,
    spreadsheet_url: str = SPREADSHEET_URL,
    save_dir: Path = SAVE_DIR,
    headless: bool = False,
) -> Path:
    save_dir.mkdir(exist_ok=True)

    if save_path is None:
        save_path = make_screenshot_path(save_dir)

    save_path = Path(save_path).resolve()

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=headless)

        try:
            page = browser.new_page(viewport=VIEWPORT)

            page.goto(spreadsheet_url)

            # Google Spreadsheetの読み込み待ち
            page.wait_for_timeout(5000)

            # メニュー非表示/表示切替
            page.keyboard.press("Control+Shift+F")

            # メニュー折りたたみ反映待ち
            page.wait_for_timeout(1000)

            page.screenshot(path=str(save_path))

            print(f"スクリーンショットを保存しました: {save_path}")

            return save_path

        finally:
            browser.close()


if __name__ == "__main__":
    capture_spreadsheet()