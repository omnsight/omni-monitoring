from unittest.mock import patch

import jwt
from fastapi.testclient import TestClient
from omni_python_library import init_omni_library
from omni_python_library.utils.config import UserRole

from omni_monitoring.main import app


class TestMonitoringSource:
    client: TestClient
    no_roles_client: TestClient
    guest_client: TestClient

    @classmethod
    def setup_class(cls):
        init_omni_library()
        # Client with admin roles
        payload = {"sub": "test-user-id-123", "roles": [UserRole.ADMIN]}
        token = jwt.encode(payload, key=None, algorithm="none")
        cls.client = TestClient(app)
        cls.client.headers = {"Authorization": f"Bearer {token}"}

        # Client with no roles
        no_roles_payload = {"sub": "test-user-id-456", "roles": []}
        no_roles_token = jwt.encode(no_roles_payload, key=None, algorithm="none")
        cls.no_roles_client = TestClient(app)
        cls.no_roles_client.headers = {"Authorization": f"Bearer {no_roles_token}"}

        cls.guest_client = TestClient(app)

    def teardown_method(self, method):
        # This method is called after each test.
        # It's a good place to clean up resources created during the test.
        response = self.client.get("/monitoring-sources")
        for item in response.json():
            self.client.delete(f"/monitoring-sources/{item['_id']}")

    def test_create_monitoring_source_success(self):
        # Arrange
        payload = {"name": "test-source", "source_type": "test-type"}

        # Act
        response = self.client.post("/monitoring-sources", json=payload)

        # Assert
        assert response.status_code == 200
        assert response.json()["name"] == "test-source"
        assert response.json()["owner"] == "test-user-id-123"

    def test_create_monitoring_source_permission_denied(self):
        # Arrange
        payload = {"name": "test-source", "source_type": "test-type"}

        # Act
        response = self.no_roles_client.post("/monitoring-sources", json=payload)
        guest_response = self.guest_client.post("/monitoring-sources", json=payload)

        # Assert
        assert response.status_code == 403
        assert response.json()["detail"] == "Only the owner can create this resource"
        assert guest_response.status_code == 401

    @patch("omni_monitoring.routers.monitoring_source.dal.create_monitoring_source")
    def test_create_monitoring_source_internal_error(self, mock_create):
        # Arrange
        mock_create.side_effect = Exception("Internal error")
        payload = {"name": "test-source", "source_type": "test-type"}

        # Act
        response = self.client.post("/monitoring-sources", json=payload)

        # Assert
        assert response.status_code == 500
        assert response.json()["detail"] == "Internal Server Error"

    def test_delete_monitoring_source_success(self):
        # Arrange
        payload = {"name": "test-source", "source_type": "test-type"}
        create_response = self.client.post("/monitoring-sources", json=payload)
        source_id = create_response.json()["_id"]

        # Act
        delete_response = self.client.delete(f"/monitoring-sources/{source_id}")

        # Assert
        assert delete_response.status_code == 204
        get_response = self.client.get(f"/monitoring-sources/{source_id}")
        assert get_response.status_code == 404

    def test_get_bad_monitoring_source(self):
        get_response = self.client.get("/monitoring-sources/bad_collection/1234")
        assert get_response.status_code == 404

    def test_delete_monitoring_source_not_found(self):
        # Act
        response = self.client.delete("/monitoring-sources/non-existent/id")

        # Assert
        assert response.status_code == 404
        assert response.json()["detail"] == "Resource not found"

    def test_delete_monitoring_source_permission_denied(self):
        # Arrange
        payload = {"name": "test-source", "source_type": "test-type"}
        create_response = self.client.post("/monitoring-sources", json=payload)
        source_id = create_response.json()["_id"]

        # Act
        response = self.no_roles_client.delete(f"/monitoring-sources/{source_id}")
        guest_response = self.guest_client.delete(f"/monitoring-sources/{source_id}")

        # Assert
        assert response.status_code == 403
        assert response.json()["detail"] == "Insufficient permissions to access this resource"
        assert guest_response.status_code == 401

    @patch("omni_monitoring.routers.monitoring_source.dal.delete_monitoring_source")
    def test_delete_monitoring_source_internal_error(self, mock_delete):
        # Arrange
        mock_delete.side_effect = Exception("Internal error")

        # Act
        response = self.client.delete("/monitoring-sources/some/id")

        # Assert
        assert response.status_code == 500
        assert response.json()["detail"] == "Internal Server Error"

    def test_get_monitoring_source_success(self):
        # Arrange
        payload = {"name": "test-source", "source_type": "test-type"}
        create_response = self.client.post("/monitoring-sources", json=payload)
        source_id = create_response.json()["_id"]

        # Act
        response = self.client.get(f"/monitoring-sources/{source_id}")

        # Assert
        assert response.status_code == 200
        assert response.json()["_id"] == source_id

    def test_get_monitoring_source_not_found(self):
        # Act
        response = self.client.get("/monitoring-sources/non-existent/id")

        # Assert
        assert response.status_code == 404
        assert response.json()["detail"] == "Resource not found"

    def test_get_monitoring_source_permission_denied(self):
        # Arrange
        payload = {"name": "test-source", "source_type": "test-type"}
        create_response = self.client.post("/monitoring-sources", json=payload)
        source_id = create_response.json()["_id"]

        # Act
        response = self.no_roles_client.get(f"/monitoring-sources/{source_id}")
        guest_response = self.guest_client.get(f"/monitoring-sources/{source_id}")

        # Assert
        assert response.status_code == 403
        assert response.json()["detail"] == "Insufficient permissions to access this resource"
        assert guest_response.status_code == 401

    @patch("omni_monitoring.routers.monitoring_source.dal.get_monitoring_source")
    def test_get_monitoring_source_internal_error(self, mock_get):
        # Arrange
        mock_get.side_effect = Exception("Internal error")

        # Act
        response = self.client.get("/monitoring-sources/some/id")

        # Assert
        assert response.status_code == 500
        assert response.json()["detail"] == "Internal Server Error"

    def test_get_monitoring_sources_by_user_success(self):
        # Arrange
        payload1 = {"name": "test-source-1", "source_type": "test-type"}
        self.client.post("/monitoring-sources", json=payload1)
        payload2 = {"name": "test-source-2", "source_type": "test-type"}
        self.client.post("/monitoring-sources", json=payload2)

        # Act
        response = self.client.get("/monitoring-sources")

        # Assert
        assert response.status_code == 200
        assert len(response.json()) == 2

    @patch("omni_monitoring.routers.monitoring_source.dal.get_monitoring_sources_by_user")
    def test_get_monitoring_sources_by_user_internal_error(self, mock_get_all):
        # Arrange
        mock_get_all.side_effect = Exception("Internal error")

        # Act
        response = self.client.get("/monitoring-sources")

        # Assert
        assert response.status_code == 500
        assert response.json()["detail"] == "Internal Server Error"

    def test_update_monitoring_source_success(self):
        # Arrange
        payload = {"name": "test-source", "source_type": "test-type"}
        create_response = self.client.post("/monitoring-sources", json=payload)
        source_id = create_response.json()["_id"]
        update_payload = {"name": "updated-source", "source_type": "updated-type"}

        # Act
        response = self.client.put(f"/monitoring-sources/{source_id}", json=update_payload)

        # Assert
        assert response.status_code == 200
        assert response.json()["name"] == "updated-source"

    def test_update_monitoring_source_not_found(self):
        # Arrange
        update_payload = {"name": "updated-source", "source_type": "updated-type"}

        # Act
        response = self.client.put("/monitoring-sources/non-existent/id", json=update_payload)

        # Assert
        assert response.status_code == 404
        assert response.json()["detail"] == "Resource not found"

    def test_update_monitoring_source_permission_denied(self):
        # Arrange
        payload = {"name": "test-source", "source_type": "test-type"}
        create_response = self.client.post("/monitoring-sources", json=payload)
        source_id = create_response.json()["_id"]
        update_payload = {"name": "updated-source", "source_type": "updated-type"}

        # Act
        response = self.no_roles_client.put(f"/monitoring-sources/{source_id}", json=update_payload)
        guest_response = self.guest_client.put(f"/monitoring-sources/{source_id}", json=update_payload)

        # Assert
        assert response.status_code == 403
        assert response.json()["detail"] == "Insufficient permissions to access this resource"
        assert guest_response.status_code == 401

    @patch("omni_monitoring.routers.monitoring_source.dal.update_monitoring_source")
    def test_update_monitoring_source_internal_error(self, mock_update):
        # Arrange
        mock_update.side_effect = Exception("Internal error")
        update_payload = {"name": "updated-source", "source_type": "updated-type"}

        # Act
        response = self.client.put("/monitoring-sources/some/id", json=update_payload)

        # Assert
        assert response.status_code == 500
        assert response.json()["detail"] == "Internal Server Error"

    def test_get_monitoring_source_views_success(self):
        # Arrange
        payload = {"name": "test-source", "source_type": "test-type"}
        create_response = self.client.post("/monitoring-sources", json=payload)
        source_id = create_response.json()["_id"]

        # Act
        response = self.client.get(f"/monitoring-sources/{source_id}/views")

        # Assert
        assert response.status_code == 200, f"{response}"
