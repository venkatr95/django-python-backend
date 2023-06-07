import pytest
import logging

logger = logging.getLogger(__name__)

@pytest.mark.django_db
def test_create_notes(api_client) -> None:
    """
    Test the create notes API
    :param api_client:
    :return: None
    """
    payload = {
        "title": "Wash Clothes",
        "content": "Wash clothes in the washing machine",
    }

    # Create a notes
    response_create = api_client.post("/api/notes/", data=payload, format="json")
    notes_id = response_create.data["note"]["id"]
    logger.info(notes_id)
    logger.info(f"Created notes with id: {notes_id}")
    logger.info(f"Response: {response_create.data}")
    assert response_create.status_code == 201
    assert response_create.data["note"]["title"] == payload["title"]

    # Read the notes
    response_read = api_client.get(f"/api/notes/{notes_id}", format="json")
    logger.info(f"Read notes with id: {notes_id}")
    logger.info(f"Response: {response_read.data}")
    assert response_read.status_code == 200
    assert response_read.data["note"]["title"] == payload["title"]
