from bs4 import *
from msedge.selenium_tools import *
from tqdm import tqdm
import db_connection as db

PATH = "edgedriver_win64/msedgedriver.exe"

options = EdgeOptions()
options.use_chromium = True
options.add_argument("headless")
options.add_argument("disable-gpu")


def arr(string):
    arr = []
    temp_str = ""
    i = 0
    while (i < len(string)):
        if string[i] == '[':
            arr.append(temp_str.strip())
            i = i+2
            temp_str = ""
        else:
            temp_str += string[i]
        i += 1
    arr.append(temp_str)
    return arr[1:]


def get_data(url):
    composite_arr = []
    driver = Edge(PATH, options=options)
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    for i in soup.find_all('div', {'class': 'sques_quiz'}):
        question = None

        question = i.find('div', 'wp_quiz_question testclass').text
        question = " ".join(question.split()[1:])
        answer_option = i.find('div', 'wp_quiz_question_options').text
        ans_arr = arr(answer_option)
        answer = i.find('div', 'ques_answer').text.split('[')[-1][:-1]

        obj = db.create_payload(question, ans_arr, answer)
        composite_arr.append(obj)
    driver.close()
    return composite_arr


def run(link):
    composite_arr = get_data(link)
    db.add_data(composite_arr)
