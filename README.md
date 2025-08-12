# Infectious Diseases Hotspot Prediction

This Django project predicts infectious disease hotspots using a machine learning model and association rules. Users can input demographic and disease data to receive predictions and related disease insights.

## Features
- Web form for user input (county, year, sex, population, disease count)
  
- Predicts if a location is a disease hotspot using a Keras autoencoder model
  
- Displays associated diseases using mined association rules
  
- Admin interface for managing disease data

## Project Structure
```
myproject/
    settings.py
    urls.py
    wsgi.py
    asgi.py
    unsupervised_autoencoder_model.h5
    association_rules.csv
myapp/
    models.py
    views.py
    forms.py
    urls.py
    templates/
        predict.html
        result.html
    static/
        style.css
        style1.css
        img1.webp
manage.py
db.sqlite3
```

## Setup Instructions
1. **Clone the repository**
2. **Install dependencies**
   - Python 3.x
   - Django
   - TensorFlow
   - pandas, numpy
   - (Optional) Any other requirements
3. **Apply migrations**
   ```bash
   python manage.py migrate
   ```
4. **Run the development server**
   ```bash
   python manage.py runserver
   ```
5. **Access the app**
   - Go to `http://127.0.0.1:8000/` in your browser

## Usage
- Fill out the prediction form with the required details
- Submit to see if the location is a hotspot and view associated diseases

## Files
- `unsupervised_autoencoder_model.h5`: Pre-trained Keras model for prediction
- `association_rules.csv`: CSV file with association rules for related diseases

## Admin
- Access the admin at `/admin/` (create a superuser with `python manage.py createsuperuser`)

## License
This project is for educational and research purposes.
