# Shato Sports Bar

A small, mobile-first Django site for Shato Sports Bar (Mvurwi) — a local
pub joint with pool tables, cold drinks, and no big screens.

- 2 public pages: **Home** and **About**, both extending one mobile-first
  `base.html`.
- Plain CSS + JS (no Tailwind/build step). Dark theme is the default, with
  a toggle that remembers the visitor's choice.
- A **Notice** model, editable from a Shato-branded Django admin, for
  posting things like "Weekly Pool Tournament" without touching code.
- HTMX polls a small endpoint every 60 seconds so the notice on the Home
  page can update itself without a full page reload.

## Project layout

```
shato-bar/
├── manage.py
├── requirements.txt
├── shato/              # project settings, urls, wsgi/asgi
├── core/                # the app: models, views, admin, urls
│   └── migrations/
├── templates/
│   ├── base.html
│   ├── admin/base_site.html   # branded admin header/colours
│   └── core/
│       ├── home.html
│       ├── about.html
│       └── partials/notice.html   # swapped in by HTMX
└── static/
    ├── css/style.css
    ├── js/app.js
    └── img/                # drop logo.png / pub.jpg here
```

## Setup

```bash
# 1. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Apply migrations
python manage.py migrate

# 4. Create an admin user
python manage.py createsuperuser

# 5. Run the dev server
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` for the site and
`http://127.0.0.1:8000/admin/` to post notices.

## Posting a notice

1. Log in at `/admin/`.
2. Open **Notices → Add Notice**.
3. Fill in a title and body (e.g. "Weekly Pool Tournament" /
   "K50 entry, winner takes the pot, Fridays from 6PM"), optionally
   attach a flyer image, and tick **Is active**.
4. It appears on the Home page immediately and refreshes there via
   HTMX every 60 seconds, so it'll update on visitors' screens without
   them reloading.

## Before going live

- Set a real `DJANGO_SECRET_KEY` and `DJANGO_DEBUG=False` via
  environment variables (see `shato/settings.py`).
- Set `DJANGO_ALLOWED_HOSTS` to the real domain.
- Add real photos to `static/img/` (`logo.png`, `pub.jpg`).
- Fill in the real opening hours / contact details on the Home page
  (`templates/core/home.html`) — placeholders are marked `TODO`.
- Run `python manage.py collectstatic`.
- Swap SQLite for Postgres if you expect meaningful traffic.

## Notes

- `static/` and `templates/` live at the project root (next to
  `manage.py`), matching `STATICFILES_DIRS` and `TEMPLATES[0]['DIRS']`
  in `shato/settings.py` — this is what makes `{% static %}` resolve
  correctly in development.
- Uploaded notice flyers are stored under `media/notices/` and served
  by Django only while `DEBUG=True`; use a real file/object storage
  backend in production.
