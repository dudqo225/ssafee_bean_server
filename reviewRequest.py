import json
import datetime

review_list = []

for i in range(1, 31):
    review = {
        'model': 'community.review',
    }
    review['fields'] = {
        'title': f'{i}번째 리뷰.',
        'content': f'{i}번 테스트 리뷰입니다.',
        'user': 1,
        'user_name': 'admin',
        'created_at': f'{datetime.datetime.now()}',
        'updated_at': f'{datetime.datetime.now()}',
        'user_name': 'admin',
    }
    review_list.append(review)

file_path = './community/fixtures/review.json'

with open(file_path, 'w', encoding='UTF8') as outfile:
    json.dump(review_list, outfile, ensure_ascii=False, indent=4)