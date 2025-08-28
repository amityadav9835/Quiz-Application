from django.db import models
from django.contrib.auth.models import User

# Main Quiz model
class Quiz(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='quizzes')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    time_limit = models.IntegerField(help_text="Time limit in minutes", default=10)  # Add this line

    def __str__(self):
        return self.title

# Question model linked to a Quiz
class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    text = models.TextField()
    
    option_a = models.CharField(max_length=255)
    option_b = models.CharField(max_length=255)
    option_c = models.CharField(max_length=255)
    option_d = models.CharField(max_length=255)

    correct_option = models.CharField(
        max_length=1,
        choices=[
            ('A', 'Option A'),
            ('B', 'Option B'),
            ('C', 'Option C'),
            ('D', 'Option D'),
        ]
    )

    def __str__(self):
        return self.text
    

class QuizResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='results')
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='results')
    score = models.IntegerField()
    total = models.IntegerField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def percentage(self):
        return (self.score / self.total) * 100 if self.total > 0 else 0

    def __str__(self):
        return f"{self.user.username} - {self.quiz.title} ({self.score}/{self.total})"

class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_option = models.CharField(
        max_length=1,
        choices=[
            ('A', 'Option A'),
            ('B', 'Option B'),
            ('C', 'Option C'),
            ('D', 'Option D'),
        ]
    )
    submitted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'quiz', 'question')  # Prevent duplicate answers

    def is_correct(self):
        return self.selected_option == self.question.correct_option

    def __str__(self):
        return f"{self.user.username} - {self.question.text[:40]}... - Selected: {self.selected_option}"