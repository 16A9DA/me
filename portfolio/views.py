from django.shortcuts import render

def index(request):
    context = {
        'projects': [
            {
                'name': 'Predictive Maintenance',
                'tech': 'Python · scikit-learn · Streamlit',
                'desc': 'End-to-end ML pipeline for industrial failure prediction on 10,000 sensor records. F1 score 0.68.',
                'url': 'https://github.com/16A9DA/predictive-maintenance-failure-detection',
                'color': 'card-cyan',
            },
            {
                'name': 'Prompt2Exploit',
                'tech': 'Python · Flask · OWASP ZAP',
                'desc': 'Security study comparing AI-generated vs human-written code across 18 systems.',
                'url': 'https://github.com/16A9DA/Prompt2Exploit',
                'color': 'card-yellow',
            },
            {
                'name': 'Job Finder API',
                'tech': 'FastAPI · Llama 3 · scikit-learn',
                'desc': 'REST API parsing PDF resumes into structured profiles. MLP classifier at 90% accuracy.',
                'url': 'https://github.com/16A9DA/Job-Finder',
                'color': 'card-pink',
            },
            {
                'name': 'Movie Sentiment',
                'tech': 'NLTK · SVM · TF-IDF · Streamlit',
                'desc': 'NLP classifier on 50,000 IMDB reviews. SVM achieved 85% accuracy.',
                'url': 'https://github.com/16A9DA/Movie-Sentiment',
                'color': 'card-cyan',
            },
            {
                'name': 'StudyBuddy',
                'tech': 'Django · DRF · SQLite',
                'desc': 'Multi-user study platform with room-based threading and role-based auth.',
                'url': 'https://github.com/16A9DA/StuddyBuddy',
                'color': 'card-yellow',
            },
        ],
        'skills': [
            'Machine Learning', 'Python Backend Dev', 'NLP',
            'REST APIs', 'Data Analysis', 'Security Research',
        ],
        'tools': [
            {'name': 'Python', 'icon': '🐍'},
            {'name': 'Django', 'icon': '🟢'},
            {'name': 'scikit-learn', 'icon': '🤖'},
            {'name': 'FastAPI', 'icon': '⚡'},
            {'name': 'Pandas', 'icon': '🐼'},
            {'name': 'Git', 'icon': '🔀'},
        ],
    }
    return render(request, 'portfolio/index.html', context)
