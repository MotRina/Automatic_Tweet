import openai
import os

openai.api_key = os.environ["OPENAI_API_KEY"]

def make_tweet():
    request = "私は~です。私に代わってTwitterに投稿するツイートを140文字で作成してください。\n\nツイートを作成する際は以下の例文を参考にしてください。\n\n"

    tweet1 = "例文1; ~\n\n"

    tweet2 = "例文2; ~\n\n"

    content = request + tweet1 + tweet2

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": content},
        ],
    )
    return response.choices[0]["message"]["content"]



# OPENAI_API_KEYを設定コマンドは
# echo 'export OPENAI_API_KEY="ここに自身のAPIKEYを入れる"' >> ~/.zshrc
# source ~/.zshrc で可能です
