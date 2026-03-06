import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

replacements = {
    '<p>Impossible de charger les données pour le moment. Veuillez réessayer plus tard.</p>': '<p data-i18n="error_msg">Impossible de charger les données pour le moment. Veuillez réessayer plus tard.</p>',
    
    'Télécharger mon CV': '<span data-i18n="cv_btn">Télécharger mon CV</span>',
    'Me contacter\n                </button>': '<span data-i18n="contact_btn">Me contacter</span>\n                </button>',
    
    '<h2 class="section-title">Projets récents</h2>': '<h2 class="section-title" data-i18n="recent_projects">Projets récents</h2>',
    
    '<h2 class="section-title">Loisirs</h2>': '<h2 class="section-title" data-i18n="hobbies">Loisirs</h2>',
    '<h3 class="card-title">⚽ Sports collectifs</h3>': '<h3 class="card-title" data-i18n="sports_title">⚽ Sports collectifs</h3>',
    '<p class="card-desc">J\'aime collaborer en équipe pour aller chercher la victoire, avec une certaine préférence pour le football.</p>': '<p class="card-desc" data-i18n="sports_desc">J\'aime collaborer en équipe pour aller chercher la victoire, avec une certaine préférence pour le football.</p>',
    '<h3 class="card-title">🎮 Jeux vidéo</h3>': '<h3 class="card-title" data-i18n="games_title">🎮 Jeux vidéo</h3>',
    '<p class="card-desc">Je suis un grand fan de jeux compétitifs, notamment de titres comme League of Legends ou Counter-Strike.</p>': '<p class="card-desc" data-i18n="games_desc">Je suis un grand fan de jeux compétitifs, notamment de titres comme League of Legends ou Counter-Strike.</p>',
    '<h3 class="card-title">🎬 Musique & Cinéma</h3>': '<h3 class="card-title" data-i18n="movies_title">🎬 Musique & Cinéma</h3>',
    '<p class="card-desc">J\'aime aussi la musique et le cinéma, en particulier les films assez psychologiques comme <em>Shutter Island</em>.</p>': '<p class="card-desc" data-i18n="movies_desc">J\'aime aussi la musique et le cinéma, en particulier les films assez psychologiques comme <em>Shutter Island</em>.</p>',
    
    '<h2 class="section-title">Parcours</h2>': '<h2 class="section-title" data-i18n="education">Parcours</h2>',
    '<h3 class="timeline-title">Master Informatique (e-Services)</h3>': '<h3 class="timeline-title" data-i18n="master_title">Master Informatique (e-Services)</h3>',
    '<div class="timeline-desc">\n                        Approfondissement en ingénierie logicielle, architecture des services web avancés et gestion de\n                        projet informatique.\n                    </div>': '<div class="timeline-desc" data-i18n="master_desc">\n                        Approfondissement en ingénierie logicielle, architecture des services web avancés et gestion de\n                        projet informatique.\n                    </div>',
    '<h3 class="timeline-title">Licence Informatique</h3>': '<h3 class="timeline-title" data-i18n="licence_title">Licence Informatique</h3>',
    '<div class="timeline-desc">\n                        Acquisition des fondamentaux en développement, algorithmique, base de données et architectures\n                        logicielles.\n                    </div>': '<div class="timeline-desc" data-i18n="licence_desc">\n                        Acquisition des fondamentaux en développement, algorithmique, base de données et architectures\n                        logicielles.\n                    </div>',
    '<h3 class="timeline-title">Baccalauréat Général (Spécialités Maths, Physique-Chimie)</h3>': '<h3 class="timeline-title" data-i18n="bac_title">Baccalauréat Général (Spécialités Maths, Physique-Chimie)</h3>',
    '<div class="timeline-desc">\n                        Obtention du baccalauréat avec la mention Assez Bien.\n                    </div>': '<div class="timeline-desc" data-i18n="bac_desc">\n                        Obtention du baccalauréat avec la mention Assez Bien.\n                    </div>',
    
    '<h2 class="section-title">Langages dominants</h2>': '<h2 class="section-title" data-i18n="languages">Langages dominants</h2>',
    
    '<span>Données synchronisées en temps réel depuis GitHub</span>': '<span data-i18n="footer_sync">Données synchronisées en temps réel depuis GitHub</span>',
    
    '<h2 style="color: white; margin-bottom: 0.5rem; font-size: 1.5rem;">Me contacter</h2>': '<h2 style="color: white; margin-bottom: 0.5rem; font-size: 1.5rem;" data-i18n="modal_title">Me contacter</h2>',
    '<p style="color: var(--text-muted); font-size: 0.9rem;">\n                Envoyez-moi un message via ce formulaire !\n            </p>': '<p style="color: var(--text-muted); font-size: 0.9rem;" data-i18n="modal_desc">\n                Envoyez-moi un message via ce formulaire !\n            </p>',
    '<label for="name" class="form-label">Votre Nom</label>': '<label for="name" class="form-label" data-i18n="label_name">Votre Nom</label>',
    '<label for="email" class="form-label">Votre Email</label>': '<label for="email" class="form-label" data-i18n="label_email">Votre Email</label>',
    '<label for="message" class="form-label">Votre Message</label>': '<label for="message" class="form-label" data-i18n="label_message">Votre Message</label>',
    'Envoyer le message\n                </button>': '<span data-i18n="submit_btn">Envoyer le message</span>\n                </button>'
}

for old, new in replacements.items():
    if old not in content:
        print(f"FAILED TO FIND: {old[:50]}...")
    content = content.replace(old, new)


# Also add placeholders
content = content.replace('placeholder="Jean Dupont"', 'placeholder="Jean Dupont" data-i18n="ph_name"')
content = content.replace('placeholder="jean@exemple.com"', 'placeholder="jean@exemple.com" data-i18n="ph_email"')
content = content.replace('placeholder="Bonjour Mathis, je vous contacte pour..."', 'placeholder="Bonjour Mathis, je vous contacte pour..." data-i18n="ph_message"')


with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("done")
