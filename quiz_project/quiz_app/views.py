from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Subject, Question

# Login view
def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect("subjects")  # Redirect to the subjects list after successful login
        else:
            return render(request, "login.html", {"error": "Invalid credentials"})
    return render(request, "login.html")

# Subject List view (Shows available subjects)
@login_required
def subject_list(request):
    subjects = Subject.objects.all()  # Fetch all subjects from the database
    return render(request, "subjects.html", {"subjects": subjects})

# Quiz View (Displays questions for the selected subject and handles quiz submission)
@login_required
def quiz_view(request, subject_id):
    subject = Subject.objects.get(id=subject_id)
    questions = Question.objects.filter(subject=subject)

    if request.method == "POST":
        score = 0
        for question in questions:
            selected = request.POST.get(str(question.id))
            if selected and selected == question.correct_answer:
                score += 1

        total = len(questions)
        percentage = (score / total) * 100 if total > 0 else 0

        return render(request, "result.html", {
            "score": score,
            "total": total,
            "percentage": round(percentage, 2)
        })

    return render(request, "quiz.html", {"subject": subject, "questions": questions})
