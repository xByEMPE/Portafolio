import os
import sys
import streamlit as st
from PIL import Image
import requests
from io import BytesIO

# ----- Configuración de la página -----
st.set_page_config(
    page_title='Portafolio - Jesús Enrique García Hernández',
    layout='wide',
    initial_sidebar_state='collapsed'
)

# ----- Meta viewport para responsividad -----
st.markdown('<meta name="viewport" content="width=device-width, initial-scale=1" />', unsafe_allow_html=True)

# ----- CSS personalizado -----
css = '''
<style>
body { background-color: #0a0f29; color: #ffffff; font-family: Arial, sans-serif; margin:0; padding:0; }
.css-18e3th9 { max-width: 1200px; margin: auto; }
.header { text-align: center; padding: 2rem 0; background-color: #101838; transition: background-color .3s ease; }
.header:hover { background-color: #1e2a5c; }
.header h1 { margin: 0; font-size: 3rem; }
.header p { margin: .5rem 0 0; font-size: 1.2rem; color: #c0c6d4; }
.about { padding: 2rem; max-width: 800px; margin: auto; }
.about h2 { margin-bottom: 1rem; }
.about p { line-height: 1.6; }
.projects-container { display: flex; flex-wrap: wrap; justify-content: center; gap: 2rem; padding: 2rem; }
.project-card { background-color: #101838; border-radius: 10px; overflow: hidden; width: 300px; box-shadow: 0 4px 6px rgba(0,0,0,.3); transition: transform .3s ease; }
.project-card:hover { transform: translateY(-10px); }
.project-card img { width: 100%; height: auto; display: block; }
.project-card h3 { margin: 1rem; font-size: 1.5rem; }
.project-card p { margin: 0 1rem 1rem; font-size: 1rem; color: #c0c6d4; }
.project-card a { text-decoration: none; color: inherit; }
footer { text-align: center; padding: 0; background-color: transparent; }
@media (max-width: 1024px) { .project-card { width: 45%; } }
@media (max-width: 768px) { .projects-container { flex-direction: column; align-items: center; } .project-card { width: 90%; } }
</style>
'''
st.markdown(css, unsafe_allow_html=True)

# ----- Desactivar inspección -----
st.markdown(
    '''
    <script>
    document.addEventListener('contextmenu', event => event.preventDefault());
    document.addEventListener('keydown', function(e) {
        if (e.keyCode === 123 || (e.ctrlKey && e.shiftKey && (e.keyCode === 73 || e.keyCode === 67 || e.keyCode === 74)) || (e.ctrlKey && e.keyCode === 85)) {
            e.preventDefault();
        }
    });
    </script>
    ''', unsafe_allow_html=True)

# ----- Header -----
st.markdown(
    '''
    <div class='header'>
        <h1>Jesús Enrique García Hernández</h1>
        <p>Data Scientist & Machine Learning Engineer</p>
    </div>
    ''', unsafe_allow_html=True)

# ----- About Me -----
st.markdown(
    '''
    <section class='about'>
        <h2>About Me</h2>
        <p>Soy un profesional en Ciencia de Datos y Aprendizaje Automático con experiencia en proyectos de inspección de turbinas eólicas utilizando visión computarizada y despliegue en la nube. Me apasiona automatizar flujos de trabajo y optimizar modelos para aplicaciones en tiempo real.</p>
    </section>
    ''', unsafe_allow_html=True)

# ----- Projects -----
st.markdown('<hr>', unsafe_allow_html=True)
st.markdown(
    '''
    <section class='projects'>
        <h2>Projects</h2>
        <div class='projects-container'>
    ''', unsafe_allow_html=True)

projects = [
    {
        'title': 'Modelo de ML para detección automatizada de daños en palas eólicas',
        'description': 'Proyecto de modelo de aprendizaje automático para detección automatizada de daños en palas eólicas.',
        'link': 'https://github.com/xByEMPE/ML-MODEL',
        'image': 'https://via.placeholder.com/300x200'
    },
    {
        'title': 'Modelo de recomendación para restaurantes en EE.UU.',
        'description': 'Sistema de recomendación para restaurantes en Estados Unidos, con filtrado personalizado según preferencias del cliente.',
        'link': 'https://recomendacionrestaurante.streamlit.app/',
        'image': 'https://via.placeholder.com/300x200'
    },
    {
        'title': 'Sistema de recomendación de películas con NLP',
        'description': 'Proyecto académico en Henry: sistema de recomendación de películas usando NLP para sugerencias basadas en títulos, como Star Wars.',
        'link': 'https://github.com/xByEMPE/PI1',
        'image': 'https://via.placeholder.com/300x200'
    }
]

for proj in projects:
    st.markdown(f'''
        <div class='project-card'>
            <a href='{proj['link']}' target='_blank'>
                <img src='{proj['image']}' loading='lazy' alt='{proj['title']}'>
                <h3>{proj['title']}</h3>
                <p>{proj['description']}</p>
            </a>
        </div>
    ''', unsafe_allow_html=True)
st.markdown('</div></section>', unsafe_allow_html=True)

# ----- Footer -----
st.markdown(
    '''
    <footer>
      <div style="display:flex; justify-content:center; gap:1.5rem; align-items:center; padding:1rem 0; background-color:#101838;">
        <a href="https://www.linkedin.com/in/enrique-garciahdz/" target="_blank">
          <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linkedin/linkedin-plain.svg" alt="LinkedIn" width="24" height="24" style="filter: invert(1);" />
        </a>
        <a href="mailto:jeengaher@gmail.com">
          <img src="https://upload.wikimedia.org/wikipedia/commons/4/4e/Gmail_Icon.svg" alt="Gmail" width="24" height="24" style="filter: invert(1);" />
        </a>
        <a href="tel:+529711360870">
          <img src="https://upload.wikimedia.org/wikipedia/commons/6/6a/Phone_font_awesome.svg" alt="Phone" width="24" height="24" style="filter: invert(1);" />
        </a>
        <a href="https://github.com/xByEMPE" target="_blank">
          <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg" alt="GitHub" width="24" height="24" style="filter: invert(1);" />
        </a>
      </div>
      <p style="color:#c0c6d4; font-size:.9rem;">&copy; 2025 Jesús Enrique García Hernández</p>
    </footer>
    ''', unsafe_allow_html=True)

# ----- Entry point para Vercel -----
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8501))
    sys.argv = ['streamlit', 'run', 'app.py', '--server.port', str(port), '--server.address', '0.0.0.0']
    from streamlit.web.cli import main
    main()
