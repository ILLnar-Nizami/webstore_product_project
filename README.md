# Product Management System

This is a small Django application for product management, consisting of an API and a web interface.

## Functionality

- Create, Read, Update, and Delete products (CRUD operations)
- API for working with products
- Web interface for product management
- Automatic merging of identical products
- Sorting products by various fields
- Displaying the total sum of all products

## Technologies

- Django
- Django REST Framework
- SQLite
- HTML
- JavaScript (Fetch API)

## API Documentation

Interactive API documentation is available at:
- Swagger UI: `/swagger/`
- ReDoc UI: `/redoc/`
- OpenAPI JSON: `/swagger.json`

## Installation and Launch

1. Clone the repository:
   ```
   git clone https://github.com/ILLnar-Nizami/webstore_product_project.git
   cd webstore_product_project
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # For Linux/Mac
   venv\Scripts\activate  # For Windows
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```
   python manage.py migrate
   ```

5. Run the development server:
   ```
   python manage.py runserver
   ```

6. Open a browser and go to http://127.0.0.1:8000/

## Using the API

- GET /api/products/ - get a list of all products
- POST /api/products/ - create a new product
- GET /api/products/{id}/ - get details of a specific product
- PUT /api/products/{id}/ - update a product
- DELETE /api/products/{id}/ - delete a product

## Project Structure
product_project/


├── manage.py

├── product_project/

│ ├── init.py

│ ├── settings.py

│ ├── urls.py

│ └── wsgi.py

├── product_api/

│ ├── init.py

│ ├── admin.py

│ ├── apps.py

│ ├── models.py

│ ├── serializers.py

│ ├── tests.py

│ ├── urls.py

│ └── views.py

├── templates/

│ └── product_api/

│ └── product_page.html

└── requirements.txt

## Testing

To run tests, use the command:
```
python manage.py test
```

## Contributing

If you want to contribute to the project, please create an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
