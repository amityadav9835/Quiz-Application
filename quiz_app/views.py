from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
@login_required
def base(request):
    return render(request, 'quiz_app/base.html')

def signup_view(request):  
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # redirect to login after signup
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


@login_required
def base(request):
    return render(request, 'quiz_app/base.html')

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Quiz, Question , Answer
from .forms import QuizForm, QuestionForm

@login_required
def create_quiz(request):
    if request.method == 'POST':
        form = QuizForm(request.POST)
        if form.is_valid():
            quiz = form.save(commit=False)
            quiz.creator = request.user
            quiz.save()
            return redirect('add_question', quiz_id=quiz.id)
    else:
        form = QuizForm()
    return render(request, 'quiz_app/create_quiz.html', {'form': form})

@login_required
def add_question(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id, creator=request.user)

    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.quiz = quiz
            question.save()

            # Check which button was clicked
            if request.POST.get('action') == 'add_next':
                return redirect('add_question', quiz_id=quiz.id)
            elif request.POST.get('action') == 'finish':
                return redirect('create_quiz')  # or 'dashboard' if preferred

    else:
        form = QuestionForm()

    return render(request, 'quiz_app/add_question.html', {'form': form, 'quiz': quiz})


@login_required
def dashboard(request):
    quizzes = Quiz.objects.all()
    return render(request, 'quiz_app/dashboard.html', {'quizzes': quizzes})
@login_required
def quiz_detail(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    questions = Question.objects.filter(quiz=quiz)
    return render(request, 'quiz_app/quiz_detail.html', {'quiz': quiz, 'questions': questions})

from .models import Answer, QuizResult

@login_required
def submit_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    questions = Question.objects.filter(quiz=quiz)
    score = 0
    total = questions.count()

    if request.method == 'POST':
        for question in questions:
            selected = request.POST.get(f'question_{question.id}')

            if selected in ['A', 'B', 'C', 'D']:
                # Save or update the user's answer
                Answer.objects.update_or_create(
                    user=request.user,
                    quiz=quiz,
                    question=question,
                    defaults={'selected_option': selected}
                )

                if selected == question.correct_option:
                    score += 1

        # Save the result
        QuizResult.objects.create(
            user=request.user,
            quiz=quiz,
            score=score,
            total=total
        )

        return render(request, 'quiz_app/quiz_result.html', {
            'quiz': quiz,
            'score': score,
            'total': total,
            'percentage': (score / total) * 100 if total > 0 else 0,
        })

    return redirect('quiz_detail', quiz_id=quiz.id)

from .models import QuizResult

@login_required
def quiz_summary(request):
    results = QuizResult.objects.filter(user=request.user).select_related('quiz')

    summary = [
        {
            'quiz': r.quiz,
            'score': r.score,
            'total': r.total,
            'percentage': (r.score / r.total) * 100 if r.total > 0 else 0,
            'submitted_at': r.submitted_at,
        }
        for r in results
    ]

    return render(request, 'quiz_app/quiz_summary.html', {
        'results': summary,
        'user': request.user,  # pass current user to template
    })
@login_required
def view_result_detail(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    questions = quiz.questions.all()
    answers = Answer.objects.filter(user=request.user, quiz=quiz)

    question_data = []

    for question in questions:
        answer = answers.filter(question=question).first()
        selected_option = answer.selected_option if answer else None
        is_correct = (selected_option == question.correct_option) if selected_option else False

        question_data.append({
            'question': question,
            'selected': selected_option,
            'is_correct': is_correct,
        })

    return render(request, 'quiz_app/result_detail.html', {
        'quiz': quiz,
        'question_data': question_data
    })

