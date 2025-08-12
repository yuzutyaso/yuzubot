import os
import requests
import datetime

# 環境変数からAPIトークンとルームIDを取得
chatwork_api_token = os.environ.get('CHATWORK_API_TOKEN')
chatwork_room_id = os.environ.get('CHATWORK_ROOM_ID')

if not chatwork_api_token or not chatwork_room_id:
    print("APIトークンまたはルームIDが設定されていません。")
    exit()

def post_to_chatwork(api_token, room_id, message):
    """
    Chatworkにメッセージを投稿する関数
    """
    url = f"https://api.chatwork.com/v2/rooms/{room_id}/messages"
    headers = {
        "X-ChatWorkToken": api_token
    }
    payload = {
        "body": message
    }
    response = requests.post(url, headers=headers, params=payload)
    response.raise_for_status()
    print("メッセージを投稿しました:", response.status_code)

def main():
    """
    時報メッセージを生成して投稿するメイン処理
    """
    now = datetime.datetime.now()
    current_hour = now.hour
    message = f"[info][title]時報[/title]今の時刻は{current_hour}時です！[/info]"

    post_to_chatwork(chatwork_api_token, chatwork_room_id, message)

if __name__ == "__main__":
    main()
