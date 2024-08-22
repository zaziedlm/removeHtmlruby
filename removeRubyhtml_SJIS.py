import re

def remove_ruby(text):
    """ルビを取り除く関数

    Args:
        text (str): ルビを含むテキスト

    Returns:
        str: ルビを取り除いたテキスト
    """
    text = re.sub(r'(.*?)<ruby><rb>(.*?)</rb><rp>（</rp><rt>.*?</rt><rp>）</rp></ruby>(.*?)', r'\1\2\3', text)
    return text

def main():
    """メイン関数
    ネット上の青空文庫の保存HTMLからルビを取り除いて保存する(グラフDB登録向け)

    Returns:
        None
    """
    base_name = '楠山正雄 桃太郎'
    without_ruby = '_without_ruby'
    extension = '.html'
    with open(f'{base_name}{extension}', 'r', encoding='shift_jis') as f:
        text = f.read()
    
    text = remove_ruby(text)

    with open(f'{base_name}{without_ruby}{extension}', 'w', encoding='shift_jis') as f:
        f.write(text)

if __name__ == "__main__":
    main()