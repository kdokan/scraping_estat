
#%%
import requests
from bs4 import BeautifulSoup
import urllib.parse
import re

#%%

def download_jnto(output_filename):
    """
    function:
        訪日外客数のデータをダウンロード
    args:
        ダウンロードパス
    return:
        rawデータ
    """

    # jntoのurl
    base_url = "https://www.jnto.go.jp/statistics/data/visitors-statistics/"

    # ダウンロードしたいexcel fileのpathを探す
    response = requests.get(base_url)
    html_code = BeautifulSoup(response.content, "html.parser")
    pattern = re.compile(r'/statistics/data/since2003_visitor_arrivals.*\.xlsx')
    matching_html = html_code.find_all('a', href=pattern)
    target_file_path = matching_html[0].get('href')

    # Excelファイルをダウンロード
    ## Excelファイルへのリンク取得
    excel_absolute_path = urllib.parse.urljoin(base_url, target_file_path)
    ## ダウンロード
    download_excel = requests.get(excel_absolute_path)

    with open(output_filename, "wb") as excel_file:
        excel_file.write(download_excel.content)


def download_esri_di(output_filename):
    # 景気動向指数のURL
    base_url = "https://www.esri.cao.go.jp/jp/stat/di/di.html"
    # ダウンロードしたいexcel fileのpathを探す
    response = requests.get(base_url)
    html_code = BeautifulSoup(response.content, "html.parser")
    # a要素の中で href 属性が '0126ci.xlsx' を含むものを検索
    target_link = html_code.find('a', href='0126ci.xlsx')
    target_file_path = target_link.get('href')

    # Excelファイルをダウンロード
    ## Excelファイルへのリンク取得
    excel_absolute_path = urllib.parse.urljoin(base_url, target_file_path)
    ## ダウンロード
    download_excel = requests.get(excel_absolute_path)

    with open(output_filename, "wb") as excel_file:
        excel_file.write(download_excel.content)

