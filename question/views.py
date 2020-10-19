from django.http import JsonResponse
from django.shortcuts import render
from .models import dict_model
import numpy as np
from .forms import GradeForm
from django.shortcuts import redirect


# Defining function returning JSON with the list of candidates, their grades and average of grades
def index(request):
    c_g_target_list = []
    m = dict_model()

    c_l_id = m['candidates']['c_l_id']

    for c_id in c_l_id:
        # Appending dictionary with data per candidate to the target list
        g_l_value = list(m['grades']['g_l_values'].filter(candidate_id=c_id))

        c_g_target_list.append(
            {
                'pk': str(c_id),
                'full_name': str(list(m['candidates']['c_l_first_name'].filter(id=c_id))[0]) + ' ' +
                             str(list(m['candidates']['c_l_last_name'].filter(id=c_id))[0]),
                'grades': g_l_value,
                'avg_grades': np.mean(g_l_value)
            }
        )

    return JsonResponse({'data': c_g_target_list}, safe=False)


# Function grading task done by candidate
def add_mark(request):
    if request.method == "POST":
        form = GradeForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('/')
    else:
        form = GradeForm()
    return render(request, 'question/post_edit.html', {'form': form})
