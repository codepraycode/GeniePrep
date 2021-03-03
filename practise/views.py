from django.http.response import Http404, HttpResponse, JsonResponse
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from pathlib import Path
import os
import json
from urllib.parse import unquote
from ast import literal_eval
from random import sample

BASE_DIR = Path(__file__).resolve().parent.parent
static_path = os.path.join(BASE_DIR, 'static')

filepath = static_path + r'\answers.json'
# print("path =>",filepath)

with open(filepath) as file:
    data = json.loads(file.read())
    # print(data.keys())

    # Extract and store all subjects from file into list
    subjects = [] # list(data.keys())
    start = stop = 0
    
  

# Fucntion to get question_answer range
def get_quest_range(sub, _from=4, _to=10):
    # sub for subject
    quest = list(sub.keys())[2:] # excluded 'short' and 'code'

    quest = list(map(int, quest)) # convert all quest element to integer
    
    quest_range = quest[_from-1: _to] # range requested

    return quest_range

'''
def setup(request):
    return render(request, 'setup.html', {})

def instruction(request):

    return render(request, 'instructions.html', {})
'''

def index(request):
    return HttpResponseNotFound("Start Page still in Development")



def test(request):
    # This Functions sends the test sheet.
    # Requires Start, stop
    # requires subjects
    # requires duration

    # Process the duration
    # receives a number string from url
    duration = request.GET.get('dur', '30') #mins
    # print(duration)
    # convert to float
    

    

    # global start, stop
    #start, stop = (10, 20)  # Query from cookie
    subjects = [] # Query from cookie
    # %2c m-> ,

    test_data = request.COOKIES['testData'] # Get testData from cookie
    # print(test_data)
    
    test_data = unquote(test_data) # Decode the URL encoding in UTF-8
    # print(test_data ,'=>', type(test_data))
    test_data = test_data.strip('][').split(' ') # Convert string list to actual list
    # print(test_data)
    test_data = list(literal_eval(test_data[0])) # Convert string dict to actual dict
    # print(test_data)
    
    # test_data ->
    ## [
    #   {'name': 'English', 'start': '1', 'stop': '10'},
    #   {'name': 'Chemistry', 'start': '1', 'stop': '10'}
    #  ]

    c = 1 # index for the dictionary
    quest_ans = {}# {}
    for each_data in test_data:
        # each_data is a dictionary
        #subjects.append(each_data['name'])
        
        name = each_data['name']
        subjects.append(name)
        sub = data[name]
        rep_ans = get_quest_range(sub, _from=int(each_data['start']), _to=int(each_data['stop']))

        temp = {'sub': name, 'code': sub['code'], 'data': rep_ans}

        quest_ans[c] = temp
        c += 1

        temp = None
        
    print(quest_ans)
    
    # print(type(quest_range[0]))
    return render(request, 'practise/test.html',
        {
            'quest_range':quest_ans.values(),
            'subjects':subjects,
            'duration': float(duration),
        })
    


# Create your views here.
def practise(request):
    
    
    subjects = [
        {'code': 'ENG', 'name': 'English'},
        {'code': 'MTH', 'name': 'Mathematics'},
        {'code': 'PHY', 'name': 'Physics'},
        {'code': 'CHM', 'name': 'Chemistry'}
    ]
    
    """
    if request.method == 'POST':
        # print("Yes!!")
        script_data = request.POST #.keys()

        # print(script_data)

        # MarkeWork
        # Response Format:
        # {subject_code: { question_indexNo: {'choose':str,'correct':bool, 'correction':str} }}
        # global marked_work

        marked_work = marker(script_data)
        print(marked_work)
        response = {}

        

        # quest_ans = {}
        for i,k in enumerate(subjects):
            sub = data[subjects[i]]
            temp = {'sub':k, 'code':sub['code'],'data':marked_work}

            response[i] = temp

            temp = None

        
        return render(request, 'check_test.html',
                      {
                          'reply': response.values(),
                          'subjects': subjects
                      })
    """

    
    mode = request.GET.get('m',None)

    print(mode)
    if mode == 'setup':
        # An API Call for the questions_data which is
        
        # All Keys
        keys = list(request.GET.keys())

        
        # print(keys[1:])
        # Subject Keys
        subjects_set = [s for s in keys if s.startswith('subject')]
        # print(subjects_set)
        data = {'good': bool(subjects_set), 'subjects':[]}

        
        
        
        
        for i in subjects_set: 
            # print(f"{i} > {request.GET[i]}")
            name = request.GET[i]
            
            code = None
            for s in subjects:
                if s['name'].lower() == name.lower():
                    code = s['code']
                    break
            # [from, to] -> default, except changed in the DOM
            start_from, to_stop = [e for e in keys if e.startswith(code)]
            
            start_from = request.GET[start_from]
            to_stop = request.GET[to_stop]

            start_from_to_range = len(list(range(int(start_from),int(to_stop)+1)))
            # print("start from {} to {}".format(start_from, to_stop))
            
            

            data['subjects'].append({'name':name, 'start':start_from, 'stop':to_stop, 'quest_range':start_from_to_range})
        
        
        
        # As for the time
        timepicked = request.GET['timeset'].replace('%3a', ':')
        time_split = timepicked.split(sep=':') # [min, sec]
        time_split = list(map(int,time_split))
        # Duration in minutes, so min + (secs/min) -> rounded to 2 decimal places
        duration = round((time_split[0]) + (time_split[1]/60),2)
        # print(duration)
        data['duration'] = duration # in minutes

        # print(data)
        return JsonResponse(data)
        
    if mode == 'instruction':
        return render(request, 'practise/instructions.html', {})
    
        
    # print(mode)
    # if mode=='setup':
    return render(request, 'practise/practiseMain.html', {'subjects':subjects})
    





def dashview(request):
    return render(request, 'dashboard/dashmain.html', {})


def profile(request):
    return render(request, "dashboard/profile.html")


def leaderBoard(request):
    return render(request, "dashboard/leaderboard.html")


def records(request):
    return render(request, "dashboard/records.html")




## Function for Correction
def correction(request):
    subjects = {'ENG':'English', 'MTH':'Mathematics', 'PHY':'Physics', 'CHM':'Chemistry'}
    response = {}

    script = {
        'ENG':
            {
                '10': {'selected': 'A', 'correct': False, 'correction': 'C'}, 
                '11': {'selected': 'B', 'correct': False, 'correction': 'C'}, 
                '12': {'selected': 'C', 'correct': True, 'correction': 'C'}, 
                '13': {'selected': 'D', 'correct': False, 'correction': 'C'}, 
                '14': {'selected': None, 'correct': False, 'correction': 'B'}
            },
        'MTH':
            {
                '10': {'selected': 'A', 'correct': True, 'correction': 'A'},
                '11': {'selected': 'B', 'correct': False, 'correction': 'A'},
                '12': {'selected': 'C', 'correct': False, 'correction': 'D'},
                '13': {'selected': None, 'correct': False, 'correction': 'D'},
                '14': {'selected': None, 'correct': False, 'correction': 'B'},
            },
        'CHM':
            {
                '10': {'selected': None, 'correct': None, 'correction': None},
                '11': {'selected': 'B', 'correct': False, 'correction': 'D'},
                '12': {'selected': None, 'correct': False, 'correction': 'A'},
                '13': {'selected': 'C', 'correct': False, 'correction': 'B'},
                '14': {'selected': 'A', 'correct': False, 'correction': 'C'}
            },

        'PHY':
            {
                '10': {'selected': None, 'correct': False, 'correction': 'A'},
                '11': {'selected': 'C', 'correct': False, 'correction': 'D'},
                '12': {'selected': 'A', 'correct': True, 'correction': 'A'},
                '13': {'selected': 'B', 'correct': False, 'correction': 'C'},
                '14': {'selected': 'D', 'correct': True, 'correction': 'D'}
            }

        
    }

   
    # Response => {code: {sub:str,code:str,data:{}}}
    count = 1
    for c,v in script.items():
        # v is a dictionary
        answers = {}
        for i,rem in v.items():
            prep_answers = {int(i):{'index':i}}
            prep_answers[int(i)].update(rem)
            answers.update(prep_answers)
            # print(answers)
        
        # print(answers)
        # Subject data element example
        # subject_data': {10: {'index': '10', 'selected': 'A', 'correct': False, 'correction': 'C'}
        temp = {'sub': subjects[c], 'code': c, 'subject_data': answers}
        response[count] = (temp)
        count += 1
    
    # print(response)
    subject_list = list(subjects.values())

    context = {'subjects': subject_list, 'data': response}
    # print()
    # print(context['data'])
    


    return render(request, 'check_test.html', context)#,'reply': response.values()})



## Function that Does the Marking
def marker(practise_data):
    subject_codes = ['ENG', 'MTH', 'CHM', 'PHY'] # Query this subject's codes from session

    # Get the subject name and map to subject code
    # data is a global variable, defined when opening the answer file
    # Data is the Marking Guide
    subject_names = {data[s]['code']:s for s in subjects if data[s]['code'] in subject_codes} # subject code:Subject Name
    
    # Create Dictionary that should contain subject code:list of answers
    # Iterate throught the subject codes
    # Get the subjects key name in the file
    # get the list of all questions attempted
    # update result dictionary with subject code: question list

    # Create Dictionary => result
    # Create with suject codes as keys
    # Result dictionary holds the marked data

    # Make Result a dictionary of this format
    # {subject_code: { question_indexNo: {'choose':str,'correct':bool, 'correction':str} }}

    result = {}

    for scode in subject_codes:
        sname = subject_names[scode]
        quest_list = get_quest_range(data[sname], _from=start, _to=stop)
        
        quest_list = list(map(str, quest_list))

        result[scode] = {indexNo:None for indexNo in quest_list}
    

    

    #print(result)
    
    for code,value in result.items():
        # Return the subject's data using subject code
        subj = data[subject_names[code]] # Marking Guide
        
        # Value is a dictionary also
        # Seperate the code from index number
        # e.g ENG11 -> 11
        ans = [n.replace(code, '')
               for n in practise_data if n.startswith(code)]
        # print(code, "=>", ans)

        for each in ans:
            # each answer is assumed to be present within the range
            # So each is assumed

            if each in value.keys():
                
                correct_one = subj[each] # Get correct answer from Guide
                option_gotten = practise_data[code+each] # Get answer from practise_data
                # Check if correct, incorrect or Bonus.
                # Bonus is when correct_one is None
                isCorrect = option_gotten == correct_one if correct_one is not None else correct_one

                # Keep this line for future marking debug
                # print("For {}) Choose => {}, correct => {}, {}".format(code+each, option_gotten, correct_one, (isCorrect, 'Bonus')[isCorrect is None]))
                # print()
            

                # Replace the Old None with dictionary value
                value[each] = {'selected': option_gotten,'correct': isCorrect, 'correction': correct_one}
        
        # As for the untouched values.
        # if there be any option that was not answered, which should be None
        # set option to None, which could evaluate to Bonus if correct_option is None also
        untouched = [v for v in value.keys() if value[v] is None]
        for unt in untouched:
            correct_one = subj[unt]
            option_gotten = None
            isCorrect = option_gotten == correct_one if correct_one is not None else correct_one

            # Keep this line for future marking debug
            # print("For {}) Choose => {}, correct => {}, {}".format(code+each, option_gotten, correct_one, (isCorrect, 'Bonus')[isCorrect is None]))
            # print()

            value[unt] = {'selected': option_gotten,
                           'correct': isCorrect, 'correction': correct_one}
    
    # Format-> { subject_code: { question_indexNo: 
    #                                  { 'choose':str,'correct':bool, 'correction':str} }
    #           }
    return result # Marked :)
    
    
    
    


    


