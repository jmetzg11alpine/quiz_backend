from fastapi import FastAPI 
from supabase import create_client, Client 
from .config import settings 
import time
from . import schemas
from . import functions

app = FastAPI()

while True:
    try:
        supabase: Client = create_client(settings.url, settings.key)
        print('database connection was successful!!')
        break
    except Exception as error:
        print('failed to connect')
        print('error', error)
        time.sleep(2)

################## quiz 1 #########################
@app.get('/q1')
def q1_get():
    scores = functions.get_quiz_scores(supabase, 'q1')
    return scores

@app.post('/q1')
def q1_post(quiz: schemas.Quiz):
    quiz = quiz.dict()
    try:
        supabase.table('q1').insert(quiz).execute()
        return {'score': quiz['score']}
    except:
        return {'message': 'keeping original score'}
 
################## quiz 2 #########################
@app.get('/q2')
def q2_get():
    scores = functions.get_quiz_scores(supabase, 'q2')
    return scores

@app.post('/q2')
def q2_post(quiz: schemas.Quiz):
    quiz = quiz.dict()
    try:
        supabase.table('q2').insert(quiz).execute()
        return {'score': quiz['score']}
    except:
        return {'message': 'keeping original score'}

################## quiz 3 #########################
@app.get('/q3')
def q3_get():
    scores = functions.get_quiz_scores(supabase, 'q3')
    return scores

@app.post('/q3')
def q3_post(quiz: schemas.Quiz):
    quiz = quiz.dict()
    try:
        supabase.table('q3').insert(quiz).execute()
        return {'score': quiz['score']}
    except:
        return {'message': 'keeping original score'}


################## quiz 4 #########################
@app.get('/q4')
def q4_get():
    scores = functions.get_quiz_scores(supabase, 'q4')
    return scores

@app.post('/q4')
def q4_post(quiz: schemas.Quiz):
    quiz = quiz.dict()
    try:
        supabase.table('q4').insert(quiz).execute()
        return {'score': quiz['score']}
    except:
        return {'message': 'keeping original score'}


################## user average #########################
@app.get('/all_scores_average')
def all_scores_average():
    scores = functions.get_scores(supabase)
    return scores

