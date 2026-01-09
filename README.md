# 📝 FastAPI Blog API

A beginner-friendly **Blog REST API** built using **FastAPI**, designed to demonstrate core backend development concepts such as CRUD operations, RESTful API design, and request/response validation using **Pydantic**.

This project is ideal for students and backend beginners who want hands-on experience with FastAPI and API development.

---

## 🚀 Features

* Create new blog posts
* Read all blog posts
* Read a single blog post by ID
* Update existing blog posts
* Delete blog posts
* Fast and lightweight API using FastAPI
* Automatic interactive API documentation (Swagger UI)

---

## 🛠️ Tech Stack

* **Backend Framework:** FastAPI
* **Language:** Python
* **Data Validation:** Pydantic
* **Server:** Uvicorn

---

## 📂 Project Structure

```
blog-api/
│── main.py
│── schemas.py
│── models.py
│── routers/
│   └── blog.py
│── requirements.txt
```

---

## ⚙️ Installation & Setup

1. Clone the repository

   ```bash
   git clone https://github.com/your-username/fastapi-blog-api.git
   cd fastapi-blog-api
   ```

2. Create and activate a virtual environment

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\\Scripts\\activate
   ```

3. Install dependencies

   ```bash
   pip install -r requirements.txt
   ```

4. Run the application

   ```bash
   uvicorn main:app --reload
   ```

---

## 📌 API Documentation

Once the server is running, access:

* **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* **ReDoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 📬 Sample Endpoints

* `GET /blogs` – Get all blog posts
* `GET /blogs/{id}` – Get a specific blog post
* `POST /blogs` – Create a new blog post
* `PUT /blogs/{id}` – Update a blog post
* `DELETE /blogs/{id}` – Delete a blog post

---

## 🎯 Learning Outcomes

* Understanding RESTful API principles
* Hands-on experience with FastAPI
* Using Pydantic for schema validation
* Structuring backend projects

---

## 🔮 Future Improvements

* Database integration (SQLite / PostgreSQL)
* JWT-based authentication
* User roles (Admin / Author)
* Pagination and filtering
* Deployment (Docker / Cloud)

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork the repository and submit a pull request.

---

## 📄 License

This project is open-source and available under the MIT License.

---

### ⭐ If you like this project, give it a star on GitHub!
