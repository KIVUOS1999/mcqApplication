import function as f
from tqdm import tqdm

links = [
    # "https://www.gktoday.in/quizbase/current-affairs-quiz-january-2023",
    # "https://www.gktoday.in/quizbase/current-affairs-quiz-december-2022",
    # "https://www.gktoday.in/quizbase/current-affairs-quiz-november-2022",
    # "https://www.gktoday.in/quizbase/current-affairs-quiz-october-2022",
    # "https://www.gktoday.in/quizbase/current-affairs-quiz-september-2022",
    # "https://www.gktoday.in/quizbase/current-affairs-quiz-august-2022",
    # "https://www.gktoday.in/quizbase/current-affairs-quiz-july-2022",
    # "https://www.gktoday.in/quizbase/current-affairs-quiz-june-2022",
    # "https://www.gktoday.in/quizbase/current-affairs-quiz-may-2022",
    # "https://www.gktoday.in/quizbase/current-affairs-quiz-april-2022",
    # "https://www.gktoday.in/quizbase/current-affairs-quiz-march-2022",
    # "https://www.gktoday.in/quizbase/current-affairs-quiz-february-2022"
]

for link in links:
    print(link)
    for i in tqdm(range(2, 6)):
        full_link = f"{link}?pageno={i}"
        f.run(full_link)
