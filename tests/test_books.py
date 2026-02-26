# Checking Root
def test_root(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["message"] == "Books Information API"

# Create Book
def test_create_book(client, create_user):
    login = client.post(
        "/login",
        data={"username": "testuser", "password": "password"}
    )

    token = login.json()["access_token"]

    response = client.post(
        "/books",
        json={
            "title": "Test Book",
            "author": "Test Author",
            "year": 2024
        },
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 200
    assert response.json()["title"] == "Test Book"

# Get All Books
def test_get_books(client):
    response = client.get("/books")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

# Get Book by ID
def test_get_book_not_found(client):
    response = client.get("/books/999")
    assert response.status_code == 404

# Delete book
def test_delete_book(client, create_user):
    login = client.post(
        "/login",
        data={"username": "testuser", "password": "password"}
    )

    token = login.json()["access_token"]

    # Create book
    create = client.post(
        "/books",
        json={"title": "Delete Me", "author": "Author", "year": 2023},
        headers={"Authorization": f"Bearer {token}"}
    )

    book_id = create.json()["id"]

    # Delete book
    response = client.delete(
        f"/books/{book_id}",
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 200