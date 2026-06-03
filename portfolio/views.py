from django.shortcuts import render

def index(request):
    context = {
        'projects': [
            
            {
                "name": "WidgetAI",
                "tech": "PySide6 · Docker",
                "desc": f"Currently working on.\n Brings ChatGPT, Claude, and Perplexity into a single floating desktop widget to eliminate browser friction.",
                "url": 'https://github.com/16A9DA/WidgetAI',
                "color": 'card-cyan'
            },

            {
                'name': 'Predictive Maintenance',
                'tech': 'Python · scikit-learn · Streamlit',
                'desc': 'End-to-end ML pipeline for industrial failure prediction on 10,000 sensor records. F1 score 0.68.',
                'url': 'https://github.com/16A9DA/predictive-maintenance-failure-detection',
                'color': 'card-pink',
            },
            {
                'name': 'Prompt2Exploit',
                'tech': 'Python · Flask · OWASP ZAP',
                'desc': 'Security study comparing AI-generated vs human-written code across 18 systems.',
                'url': 'https://github.com/16A9DA/Prompt2Exploit',
                'color': 'card-orange',
            },
            {
                'name': 'Job Finder API',
                'tech': 'FastAPI · Llama 3 · scikit-learn ',
                'desc': 'NLP REST API parsing PDF resumes into structured profiles. MLP classifier at 90% accuracy.',
                'url': 'https://github.com/16A9DA/Job-Finder',
                'color': 'card-pink',
            },

            {
                'name': 'StuddyBuddy',
                'tech': 'Django · SQLite · Docker' ,
                'desc': 'Multi-user study platform with room-based threading and role-based auth.Containerized with Docker for consistent deployment',
                'url': 'https://github.com/16A9DA/StuddyBuddy',
                'color': 'card-yellow',
            },
        ]
    }
    return render(request, 'portfolio/index.html', context)
