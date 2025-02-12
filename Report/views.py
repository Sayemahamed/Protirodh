from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from Report.forms import CrimeReportForm, CommentForm
from .models import CrimeReport, Comment, Vote

# Create your views here.

def home(request):
    return render(request, 'base.html')

def index(request, *args, **kwargs):
    return render(request, 'dummy_feed.html', {})

def detail(request, post_id):
    return render(request, 'dummy_post_detail.html', {'post_id': post_id})

def search(request):
    return render(request, 'dummy_search.html')



# # Dummy function to simulate AI-generated description
# def generate_ai_description(image):
#     # In a real implementation, you would call an AI API (e.g., OpenAI, Google Vision)
#     return "AI generated description for the uploaded image."

@login_required
def create_crime_report(request):
    if request.method == 'POST':
        form = CrimeReportForm(request.POST, request.FILES)
        if form.is_valid():
            crime_report = form.save(commit=False)
            crime_report.reported_by = request.user
            crime_report.save()
            messages.success(request, "Crime report created successfully!")
            return redirect('crime_feed')
    else:
        form = CrimeReportForm()
    return render(request, 'crime_reports/create_crime_report.html', {'form': form})

@login_required
def crime_feed(request):
    crime_reports = CrimeReport.objects.all().order_by('-post_time')
    return render(request, 'crime_reports/crime_feed.html', {'crime_reports': crime_reports})

@login_required
def crime_detail(request, report_id):
    crime_report = get_object_or_404(CrimeReport, id=report_id)
    comments = crime_report.comments.filter(parent_comment__isnull=True).order_by('-created_at')  # Fetch only parent comments
    vote_score = crime_report.vote_score

    if request.method == 'POST':
        if request.user.banned:
            messages.error(request, "You are banned from commenting.")
            return redirect('crime_detail', report_id=report_id)
        
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.crime_report = crime_report
            comment.user = request.user
            parent_comment_id = request.POST.get("parent_comment_id")  # Handle replies
            if parent_comment_id:
                comment.parent_comment = get_object_or_404(Comment, id=parent_comment_id)
                comment.save()

            #     # Notify the original commenter
            #     Notification.objects.create(
            #         recipient=comment.parent_comment.user,
            #         sender=request.user,
            #         comment=comment,
            #         message=f"{request.user.username} replied to your comment."
            #     )
            # else:
            #     comment.save()
            #     Notification.objects.create(
            #         recipient=crime_report.reported_by,
            #         sender=request.user,
            #         comment=comment,
            #         message=f"{request.user.username} commented on your post."
            #     )
            
            messages.success(request, "Comment added successfully!")
            return redirect('crime_detail', report_id=report_id)

    else:
        form = CommentForm()

    return render(request, 'crime_reports/crime_detail.html', {
        'crime_report': crime_report,
        'comments': comments,
        'form': form,
        'vote_score': vote_score,
        'share_link': request.build_absolute_uri(crime_report.get_share_link()),
    })

@login_required
def vote_report(request, report_id, vote_value):
    crime_report = get_object_or_404(CrimeReport, id=report_id)
    
    if request.user.banned:
        messages.error(request, "You are banned from voting.")
        return redirect('crime_detail', report_id=report_id)

    vote, created = Vote.objects.get_or_create(
        crime_report=crime_report,
        user=request.user,
        defaults={'vote': vote_value}
    )

    if not created:
        if vote.vote == vote_value:
            vote.delete()
            messages.success(request, "Your vote has been removed.")
        else:
            vote.vote = vote_value
            vote.save()
            messages.success(request, "Your vote has been updated.")
    else:
        messages.success(request, "Your vote has been recorded.")

    # # Notify post owner
    # Notification.objects.create(
    #     recipient=crime_report.reported_by,
    #     sender=request.user,
    #     vote=vote,
    #     message=f"{request.user.username} {'upvoted' if vote_value == 1 else 'downvoted'} your post."
    # )

    return redirect('crime_detail', report_id=report_id)

# @login_required
# def notifications(request):
#     """View for displaying notifications."""
#     user_notifications = request.user.notifications.filter(is_read=False).order_by('-created_at')
#     for notification in user_notifications:
#         notification.is_read = True
#         notification.save()
#     return render(request, 'crime_reports/notifications.html', {'notifications': user_notifications})