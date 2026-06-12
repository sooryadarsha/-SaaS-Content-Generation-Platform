
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.shortcuts import redirect

from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from content.models import GeneratedContent
from content.gemini_service import generate_ai_content

def home(request):
    return render(
        request,
        'frontend/home.html'
    )



def login_page(request):

    if request.method == "POST":

        username = request.POST.get(
            "username"
        )

        password = request.POST.get(
            "password"
        )

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user:

            login(
                request,
                user
            )

            return redirect(
                "dashboard"
            )

    return render(
        request,
        'frontend/login.html'
    )


from django.contrib.auth.models import User


def register_page(request):

    if request.method == "POST":

        username = request.POST.get(
            "username"
        )

        email = request.POST.get(
            "email"
        )

        password = request.POST.get(
            "password"
        )

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        return redirect(
            "login"
        )

    return render(
        request,
        'frontend/register.html'
    )


from content.models import GeneratedContent

@login_required
def generate_page(request):

    generated_text = None

    if request.method == "POST":

        category = request.POST.get(
            "category"
        )

        topic = request.POST.get(
            "topic"
        )

        prompt = f"""
                Create a {category}
                about {topic}
                """

        generated_text = generate_ai_content(
                    prompt
                )

        GeneratedContent.objects.create(
            user=request.user,
            category=category,
            prompt=topic,
            generated_content=generated_text
        )

    return render(
        request,
        'frontend/generate.html',
        {
            'generated_text':
            generated_text
        }
    )

@login_required
def dashboard_page(request):

    contents = GeneratedContent.objects.filter(
        user=request.user
    )

    context = {

        "total_contents":
        contents.count(),

        "blogs":
        contents.filter(
            category="Blog"
        ).count(),

        "emails":
        contents.filter(
            category="Email"
        ).count(),

        "social_posts":
        contents.filter(
            category="Social"
        ).count(),

        "marketing_contents":
        contents.filter(
            category="Marketing"
        ).count(),
    }

    return render(
        request,
        'frontend/dashboard.html',
        context
    )

@login_required
def history_page(request):

    contents = GeneratedContent.objects.filter(
        user=request.user
    ).order_by('-id')

    return render(
        request,
        'frontend/history.html',
        {
            'contents': contents
        }
    )


def logout_page(request):

    logout(request)

    return redirect('home')