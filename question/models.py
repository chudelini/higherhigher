from django.db import models
from django.utils import timezone


class Candidate(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.first_name) + ' ' + str(self.last_name)


class Recruiter(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.first_name) + ' ' + str(self.last_name)


class Task(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class Grade(models.Model):
    value = models.IntegerField()
    created = models.DateTimeField(default=timezone.now)

    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    recruiter = models.ForeignKey(Recruiter, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.candidate) + '-' + str(self.task)

    class Meta:
        unique_together = (('candidate', 'task'))

# Defining function returning dictionary of available candidates/recruiters/tasks
def dict_model():
    # Attributes of candidates keeping in the lists
    C = Candidate.objects
    c_l_first_name = C.values_list('first_name', flat=True)
    c_l_last_name = C.values_list('last_name', flat=True)
    c_l_id = C.values_list('id', flat=True)

    # Attributes of recruiters keeping in the lists
    R = Recruiter.objects
    r_l_first_name = R.values_list('first_name', flat=True)
    r_l_last_name = R.values_list('last_name', flat=True)

    # List of tasks keeping in the list
    T = Task.objects
    t_l_title = T.values_list('title', flat=True)

    # Grades
    G = Grade.objects
    g_l_values = G.values_list('value', flat=True)
    g_l_candidate_id = G.values_list('candidate_id', flat=True)

    c_r_g_dict = {
        'candidates': {
            'c_l_first_name': c_l_first_name,
            'c_l_last_name': c_l_last_name,
            'c_l_id': c_l_id
        },
        'recruiters': {
            'r_l_first_name': r_l_first_name,
            'r_l_last_name': r_l_last_name
        },
        'tasks': {
            't_l_title': t_l_title
        },
        'grades': {
            'g_l_values': g_l_values,
            'g_l_candidate_id': g_l_candidate_id
        }
    }

    return c_r_g_dict