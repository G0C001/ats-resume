from django.shortcuts import render, redirect
from django.http import HttpResponse
from ATS import ats
import io

def index(request):
    if request.method == 'POST':
        new_role = request.POST.get('role')
        new_skills = request.POST.get('skills')
        global file_name
        file_name = f'gokulvasanth_{new_role}.pdf'
        updated_skills = []

        new_skills = new_skills.split(',')
        for skill in new_skills:
            updated_skills.append(skill.strip())

        ats.skills = updated_skills
        ats.Role = new_role
        return redirect('download')

    return render(request, 'index.html')
def download(request):
    buffer = io.BytesIO()
    ats.buffer = buffer
    ats.create_pdf(buffer)
    buffer.seek(0)
    print(file_name)
    response = HttpResponse(buffer, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{file_name}"'
    return response

    
