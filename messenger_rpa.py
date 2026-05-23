import os
import subprocess
import time
from pathlib import Path

import pyautogui
import pyperclip


CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

MESSENGER_URL = (
    "https://www.facebook.com/messages/t/"
    "8513540385329633/"
)

ATTACH_BUTTON_IMAGE = "attach_button.png"


def send_image_to_messenger(image_path: str | Path) -> None:
    image_path = Path(image_path).resolve()

    if not image_path.exists():
        raise FileNotFoundError(f"画像ファイルが見つかりません: {image_path}")

    print("既存Chromeを終了します...")
    os.system("taskkill /f /im chrome.exe")
    time.sleep(2)
    print("Chrome終了完了")

    print("Messengerを起動します...")
    subprocess.Popen([
        CHROME_PATH,
        "--new-window",
        "--window-position=100,100",
        "--window-size=1280,900",
        MESSENGER_URL,
    ])

    time.sleep(5)

    print("Chromeを最大化します...")
    pyautogui.hotkey("win", "up")
    time.sleep(1)

    print("添付ボタンを検索します...")
    button_position = pyautogui.locateCenterOnScreen(
        ATTACH_BUTTON_IMAGE,
        confidence=0.8
    )

    if button_position is None:
        raise RuntimeError("添付ボタンが見つかりませんでした")

    print(f"添付ボタン発見: {button_position}")

    pyautogui.click(button_position)
    time.sleep(3)

    print("画像パスを入力します...")
    pyperclip.copy(str(image_path))
    pyautogui.hotkey("ctrl", "v")
    pyautogui.press("enter")    # ファイル選択ダイアログ[開く]実行


    time.sleep(2)
    pyautogui.press("enter")    # 送信


    print("画像を添付しました")
    time.sleep(2)



if __name__ == "__main__":
    send_image_to_messenger(
        "screenshot_20260523_133255.png"
    )