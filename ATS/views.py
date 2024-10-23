from django.shortcuts import render, redirect
from django.http import HttpResponse
from ATS import ats
from ATS import rename
from django.http import HttpResponse, FileResponse
import os

def index(request):
    if request.method == 'POST':
        new_role = request.POST.get('role')
        new_skills = request.POST.get('skills')
        global file_name
        file_name = f'gokulvasanth_{new_role}.pdf'
        updated_skills = [
            "Ajax", "Anaconda", "Linux", "API", "Bootstrap", "CSS", "Django", "AI/ML",
            "Github", "HTML", "Javascript", "Jupyter", "MySQL", "Python",
            "Visual Studio", "Visual Studio Code", "Windows"
        ]

        new_skills = new_skills.split(',')
        for skill in new_skills:
            updated_skills.append(skill.strip())

        ats.skills = updated_skills
        ats.Role = new_role
        rename.collect_and_rename_pdfs(file_name)
        ats.create_pdf(f'./templates/{file_name}')
        return redirect('download')

    return render(request, 'index.html')

def download(request):
    file_path = os.path.join('./templates', file_name)
    print(file_path)

    try:
        if os.path.exists(file_path):
            return FileResponse(open(file_path, 'rb'), content_type='application/pdf', as_attachment=True, filename=file_name)
        else:
            return HttpResponse("File not found.", status=404)
    except Exception as e:
        return HttpResponse(f"An error occurred: {e}", status=500)


    
