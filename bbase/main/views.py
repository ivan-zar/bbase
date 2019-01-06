from django.shortcuts import render, redirect
from django.http import Http404
from .models import Patient, PatientsTest, BloodCountTest, TestType


def index(request, p_id=0):
    if p_id == 0:
        patient_chosen = False
    else:
        patient_chosen = True
    context = {'patient': Patient.objects.get(pk=request.session['p_id']),
               'patient_chosen': patient_chosen}

    return render(request, 'index.html', context)


def patient_choice(request):
    patient_list = Patient.objects.all()

    context = {'patient_list': patient_list}

    return render(request, 'patient_choice.html', context)


def patient(request, patient_id):
    try:
        patient = Patient.objects.get(pk=patient_id)
        tests = PatientsTest.objects.all().filter(patient=patient_id)

    except Patient.DoesNotExist:
        raise Http404("Question doesn't exist")

    return render(request, 'patient.html', {'patient': patient, 'tests': tests})


def new_patient(request):
    return render(request, 'new_patient.html')


def new_patient_submit(request):
    # The view returns the template with a form if the form is not filled yet. If the form filled (default 'action'
    # attribute of 'form' tag redirect it to the same html), and request.method == POST returns True, than
    # a record in the database is updated and user is redirected to the page customer_choice.

    if request.method == 'POST':
        b = Patient(name=request.POST['name'], birthdate=request.POST['birth_date'])
        b.save()

        return redirect('patient_choice')

    return render(request, 'new_patient.html')


def new_test(request, patient_id):

    if request.method == 'POST':
        patient = Patient.objects.get(id=patient_id)
        testType = TestType.objects.get(id=request.POST['testType'])
        i = PatientsTest(date=request.POST['date'], patient=patient, testType=testType)
        i.save()
        patientTest=PatientsTest.objects.get(id=i.id)
        n = BloodCountTest(hb=request.POST['hb'], rbc=request.POST['rbc'], hct=request.POST['hct'],
                           wbc=request.POST['wbc'], patientsTest=patientTest)
        n.save()

        return redirect('patient', patient_id)

    return render(request, 'new_test.html', {'patient_id':patient_id})

def test(request, patient_id, test_id):

    test = BloodCountTest.objects.get(patientsTest=test_id)

    return render(request, 'test.html', {'test': test, 'patient_id': patient_id, 'test_id': test_id})

def delete_test(request, patient_id, test_id):

    PatientsTest.objects.get(id=test_id).delete()

    return redirect('patient', patient_id)
