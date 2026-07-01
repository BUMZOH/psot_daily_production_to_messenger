from messenger_rpa import send_image_to_messenger
from spreadsheet_rpa import capture_spreadsheet


def main() -> None:
    print("スプレッドシートをキャプチャします...")
    image_path = capture_spreadsheet()

    # 夜遅くのMessenger投稿は社員に対して迷惑となるため廃止
    if False:
        print("Messengerへ画像を投稿します...")
        send_image_to_messenger(image_path)

    print("処理が完了しました")


if __name__ == "__main__":
    main()