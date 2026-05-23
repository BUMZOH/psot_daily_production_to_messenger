from messenger_rpa import send_image_to_messenger
from spreadsheet_rpa import capture_spreadsheet


def main() -> None:
    print("スプレッドシートをキャプチャします...")

    image_path = capture_spreadsheet()

    print("Messengerへ画像を投稿します...")

    send_image_to_messenger(image_path)

    print("処理が完了しました")


if __name__ == "__main__":
    main()