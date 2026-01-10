# Kerstmenu 2025 - Publicatie

Deze folder bevat de gepubliceerde HTML versies van het kerstmenu, toegankelijk voor iedereen via GitHub Pages.

## 📁 Bestanden

- `index.html` - Hoofdpagina met overzicht van alle gangen
- `voorgerecht-libanees.html` - Libanese Mezze recepten
- `voorgerecht-spitskool.html` - Wasabi-Spitskool recept
- `hoofdgerecht.html` - Mahshi met Saffraan recepten
- `dessert.html` - Baklava & Sorbet recepten
- `style.css` - Stylesheet voor alle receptpagina's

## 🌐 GitHub Pages Setup

### Stap 1: Activeer GitHub Pages

1. Ga naar je repository op GitHub
2. Klik op **Settings** (Instellingen)
3. Scroll naar **Pages** in het linkermenu
4. Bij **Source** selecteer: **Deploy from a branch**
5. Bij **Branch** selecteer: **main** en folder **/publish**
6. Klik op **Save**

### Stap 2: Wacht op deployment

GitHub Pages heeft 1-5 minuten nodig om de site te bouwen. Je ziet een groene checkmark wanneer het klaar is.

### Stap 3: Bezoek je site

Je kerstmenu is nu toegankelijk via:
```
https://<jouw-github-username>.github.io/kerstmenu-2025/
```

Vervang `<jouw-github-username>` met je GitHub gebruikersnaam.

## 📱 Toegankelijkheid

✅ **Geen GitHub account nodig** - Iedereen kan de menu pagina's bekijken  
✅ **Mobiel vriendelijk** - Responsive design voor telefoons en tablets  
✅ **Direct delen** - Stuur de URL naar familie en vrienden  
✅ **Print vriendelijk** - Alle recepten zijn printbaar

## 🔄 Updates

Wanneer je markdown bestanden in de `menu/` folder update:

1. Converteer opnieuw met Pandoc:
   ```powershell
   pandoc menu/<bestand>.md -o publish/<bestand>.html --standalone --css=style.css --metadata title="Titel"
   ```

2. Commit en push naar GitHub:
   ```powershell
   git add publish/
   git commit -m "Update menu pagina's"
   git push
   ```

3. GitHub Pages update automatisch binnen enkele minuten

## 🎨 Styling Aanpassen

Pas `style.css` aan om kleuren, fonts of layout te wijzigen. Alle HTML pagina's gebruiken deze stylesheet.

---

**Versie**: 1.0  
**Laatst bijgewerkt**: 10 januari 2026
