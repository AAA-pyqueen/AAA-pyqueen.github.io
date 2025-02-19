from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html')

def certifications(request):
    return render(request, 'main/certifications.html')

def dashboards(request):
    return render(request, 'main/dashboards.html')

def papers(request):
    return render(request, 'main/papers.html')

def coding(request):
    return render(request, 'main/coding.html')

def additional_info(request):
    return render(request, 'main/additional_info.html')
