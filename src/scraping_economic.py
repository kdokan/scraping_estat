
#%%
import requests
from bs4 import BeautifulSoup
import urllib.parse
import re

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

    return None


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

    return None

def download_unemployment_rate(output_filename):

    base_url = "https://www.e-stat.go.jp/stat-search/files?page=1&layout=datalist&toukei=00200531&tstat=000000110001&cycle=0&tclass1=000001040276&tclass2=000001011681&tclass3val=0"
    # ダウンロードしたいexcel fileのpathを探す
    response = requests.get(base_url)
    html_code = BeautifulSoup(response.content, "html.parser")
    target_link = html_code.find('a', href='/stat-search/file-download?statInfId=000031831358&fileKind=0')
    target_file_path = target_link.get('href')

    # Excelファイルをダウンロード
    ## Excelファイルへのリンク取得
    excel_absolute_path = urllib.parse.urljoin(base_url, target_file_path)
    ## ダウンロード
    download_excel = requests.get(excel_absolute_path)

    with open(output_filename, "wb") as excel_file:
        excel_file.write(download_excel.content)

    return None


def download_real_income(output_filename):
    base_url = "https://www.stat.go.jp/data/kakei/longtime/index.html"
    target_file_path = "/data/kakei/longtime/zuhyou/season.xls"
    excel_absolute_path = urllib.parse.urljoin(base_url, target_file_path)
    ## ダウンロード
    download_excel = requests.get(excel_absolute_path)

    with open(output_filename, "wb") as excel_file:
        excel_file.write(download_excel.content)

    return None

def download_real_wage(output_filename):
    base_url = "https://www.e-stat.go.jp/stat-search/files?page=1&layout=datalist&toukei=00450071&tstat=000001011791&cycle=0&tclass1=000001035519&tclass2=000001144287&stat_infid=000032189740&tclass3val=0"
    target_file_path = "/themes/custom/estat/favicon.ico"

    excel_absolute_path = urllib.parse.urljoin(base_url, target_file_path)
    ## ダウンロード
    download_excel = requests.get(excel_absolute_path)

    with open(output_filename, "wb") as excel_file:
        excel_file.write(download_excel.content)

    return None

#%%
def download_consumer_price_index(output_filename):
    base_url = "https://www.e-stat.go.jp/stat-search/files?page=1&layout=datalist&toukei=00200573&tstat=000001150147&cycle=0&tclass1=000001150151&tclass2=000001150152&tclass3=000001150153&tclass4=000001150156&tclass5val=0"
    target_file_path = "/stat-search/files?page=1&amp;layout=datalist&amp;cycle=0&amp;toukei=00200573&amp;tstat=000001150147&amp;tclass1=000001150151&amp;tclass2=000001150152&amp;tclass3=000001150153&amp;tclass4=000001150156&amp;tclass5val=0&amp;stat_infid=000032103847"

    excel_absolute_path = urllib.parse.urljoin(base_url, target_file_path)
    ## ダウンロード
    download_excel = requests.get(excel_absolute_path)

    with open(output_filename, "wb") as excel_file:
        excel_file.write(download_excel.content)

    return None