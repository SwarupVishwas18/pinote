from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login, logout
from .models import Note
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from textwrap import wrap
from pyperclip import copy
# Create your views here.


def index(request):
    return render(request, 'notes/index.html')


def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        print("Hello")
        if form.is_valid():
            user = form.save()
            login(request, user)

            messages.success(request, 'Account Created')
            return redirect('notes:home')
    cxt = {'form': form}
    return render(request, 'notes/register.html', cxt)


def about(request):
    return render(request, 'notes/about.html')


def home(request):
    user = request.user

    if request.user.is_authenticated:
        if request.method == 'POST':
            if request.POST.get('note_title') and request.POST.get('note_body'):

                note = Note()
                note.title = request.POST.get('note_title')
                note.description = request.POST.get('note_body')
                note.author = user

                note.save()

                notes_data = Note.objects.filter(author=user)
                return render(request, 'notes/main.html', context={'notes_data': notes_data})
        else:
            print("Hello")
            notes_data = Note.objects.filter(author=user)
            return render(request, 'notes/main.html', context={'notes_data': notes_data})

    else:
        print("Hello")
        notes_data = Note.objects.filter(author=user)
        return render(request, 'notes/main.html', context={'notes_data': notes_data})


def delete_record(request, note_id):
    note = Note.objects.get(pk=note_id)
    note.delete()
    return redirect('../home')


def download_note(request, note_id):
    note = Note.objects.get(pk=note_id)
    buf = io.BytesIO()
    # create canvas
    can = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    can.setTitle(note.title)
    textobj = can.beginText()
    textobj.setTextOrigin(inch, inch)
    textobj.setFont('Helvetica', 18)

    # Add text
    textobj.textLine(note.title)
    textobj.setFont('Helvetica', 14)
    wrap_lines = wrap(note.description, 80)
    for line in wrap_lines:
        textobj.textLine(line)
    print(line)

    can.drawText(textobj)
    can.showPage()
    can.save()
    buf.seek(0)

    return FileResponse(buf, as_attachment=True, filename=note.title+'.pdf')


def copy_note(request, note_id):
    note = Note.objects.get(pk=note_id)
    title = note.title
    body = note.description

    copy_text = f"*{title}*\n{body}"
    messages.success(request, 'Message has been copied.')
    copy(copy_text)
    return redirect('../home')


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('../')
