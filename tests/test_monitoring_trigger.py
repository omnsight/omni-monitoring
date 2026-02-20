from unittest.mock import patch

import jwt
from fastapi.testclient import TestClient
from omni_python_library import init_omni_library
from omni_python_library.models import MonitorTriggerMainData
from omni_python_library.utils.user import UserRole

from omni_monitoring.main import app


class TestMonitorTrigger:
    client: TestClient

    @classmethod
    def setup_class(cls):
        init_omni_library()
        # Client with admin roles
        payload = {"sub": "test-user-id-123", "roles": [UserRole.ADMIN]}
        token = jwt.encode(payload, key=None, algorithm="none")
        cls.client = TestClient(app)
        cls.client.headers = {"Authorization": f"Bearer {token}"}

    def teardown_method(self, method):
        self.client.delete("/monitor-triggers")

    def test_create_monitor_trigger_success(self):
        # Arrange
        payload = MonitorTriggerMainData(
            language="en",
        )

        # Act
        response = self.client.post("/monitor-triggers", json=payload.model_dump(exclude_unset=True))

        # Assert
        assert response.status_code == 200, f"{response.json()}"
        assert response.json()["language"] == "en"

    @patch("omni_monitoring.routers.monitor_trigger.dal.create_monitor_trigger")
    def test_create_monitor_trigger_internal_error(self, mock_create):
        # Arrange
        mock_create.side_effect = Exception("Internal error")
        payload = MonitorTriggerMainData(
            language="en",
        )

        # Act
        response = self.client.post("/monitor-triggers", json=payload.model_dump(exclude_unset=True))

        # Assert
        assert response.status_code == 500
        assert response.json()["detail"] == "Internal Server Error"

    def test_get_monitor_trigger_success(self):
        # Arrange
        payload = MonitorTriggerMainData(
            language="en",
        )
        self.client.post("/monitor-triggers", json=payload.model_dump(exclude_unset=True))

        # Act
        response = self.client.get("/monitor-triggers")

        # Assert
        assert response.status_code == 200
        assert response.json()["language"] == "en"

    def test_get_monitor_trigger_not_found(self):
        # Act
        response = self.client.get("/monitor-triggers")

        # Assert
        assert response.status_code == 404
        assert response.json()["detail"] == "Monitor trigger not found"

    @patch("omni_monitoring.routers.monitor_trigger.dal.get_monitor_trigger")
    def test_get_monitor_trigger_internal_error(self, mock_get):
        # Arrange
        mock_get.side_effect = Exception("Internal error")

        # Act
        response = self.client.get("/monitor-triggers")

        # Assert
        assert response.status_code == 500
        assert response.json()["detail"] == "Internal Server Error"

    def test_delete_monitor_trigger_success(self):
        # Arrange
        payload = MonitorTriggerMainData(
            language="en",
        )
        create_response = self.client.post("/monitor-triggers", json=payload.model_dump(exclude_unset=True))
        assert create_response.status_code == 200

        # Act
        delete_response = self.client.delete("/monitor-triggers")

        # Assert
        assert delete_response.status_code == 204
        get_response = self.client.get("/monitor-triggers")
        assert get_response.status_code == 404

    def test_delete_monitor_trigger_not_found(self):
        # Act
        response = self.client.delete("/monitor-triggers")

        # Assert
        assert response.status_code == 404
        assert response.json()["detail"] == "Monitor trigger not found"

    @patch("omni_monitoring.routers.monitor_trigger.dal.delete_monitor_trigger")
    def test_delete_monitor_trigger_internal_error(self, mock_delete):
        # Arrange
        # To trigger the internal error, we need to ensure a trigger exists first.
        payload = MonitorTriggerMainData(
            language="en",
        )
        self.client.post("/monitor-triggers", json=payload.model_dump(exclude_unset=True))
        mock_delete.side_effect = Exception("Internal error")

        # Act
        response = self.client.delete("/monitor-triggers")

        # Assert
        assert response.status_code == 500
        assert response.json()["detail"] == "Internal Server Error"
