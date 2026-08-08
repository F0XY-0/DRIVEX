# DriveX (CarDealer)

A Django-based car marketplace/dealership showcase site. Built as a portfolio project — it's not a real payment/checkout system, but acts as a middleman/showcase for a company's car inventory (browse cars, view details, contact about them).

## Tech Stack
- Python / Django
- HTML / CSS / JS (vanilla)
- SQLite (default Django dev DB, unless changed)

## Project Structure
```
CarDealer/
├── manage.py
├── core/              # Project settings (settings.py, urls.py, wsgi.py)
├── cars/              # Main app — models, views, urls, admin
├── media/
│   └── cars/          # Uploaded car images
├── static/
│   ├── css/
│   ├── js/
│   └── img/
└── templates/
    ├── home.html       # Landing page — hero slideshow, feature grid,
    │                   # car listing grid, testimonials, CTA, footer
    ├── Main.html
    └── contact.html
```

## Features
- Hero slideshow of featured cars
- Car listing grid pulled from the `cars` app
- Contact page/view (`{% url 'contact' %}`)
- Toast/popup notification linking to the contact view (in progress)

## Setup
```bash
# clone / unzip the project, then:
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install django
python manage.py migrate
python manage.py runserver
```

## Status / TODO
- [X] Finish toast/popup notification on `home.html`
- [ ] Flesh out car detail pages
- [ ] Polish contact form handling
- [X] Add car filtering/search
- [ ] Deploy

## Notes
First project of this kind — going on the portfolio. Purpose is to showcase inventory, not process real transactions.
