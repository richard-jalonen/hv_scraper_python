from hv_scraper import HvScraper

first = input("Enter keyword:")
second = input("Enter keyword:")
scraper = HvScraper()
first_result = scraper.generate_answer_string(first)
second_result = scraper.generate_answer_string(second)

print(first_result)
print(second_result)
