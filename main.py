import tiktoken

# モデルに対応したエンコーディングを取得
encoding = tiktoken.encoding_for_model("gpt-4o")

# テキストをトークン化してカウント
text = "情報を見つけるのに役立つ AI アシスタントです。"
tokens = encoding.encode(text)
token_count = len(tokens)

print(f"テキスト: {text}")
print(f"トークン数: {token_count}")
print(f"トークン: {tokens}")

# トークンをデコードしてテキストに戻す
decoded_text = encoding.decode(tokens)
print(f"デコード結果: {decoded_text}")

# トークンをひとつづつデコード
for token in tokens:
    print(f"トークン: {token}, デコード結果: {encoding.decode([token])}")
