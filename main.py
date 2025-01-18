import sys
import requests
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
# from ui_login import Ui_MainWindow  # Import the login UI
from ui_login1 import Ui_MainWindow
from patient_form import PatientForm  # Import the patient form UI

class LoginApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.handle_login)  # Login button click

    def handle_login(self):
        username = self.textEdit_3.toPlainText()
        password = self.textEdit_4.toPlainText()

        try:
            response = requests.post(
                'http://127.0.0.1:8000/auth/login/',  # Update with your backend login URL
                json={'username': username, 'password': password}
            )
            if response.status_code == 200:
                data = response.json()
                role_redirect = data.get('redirect')
                QMessageBox.information(self, "Login Successful", f"Redirecting to: {role_redirect}")

                # Redirect to the appropriate window based on the role
                if role_redirect == 'patient_registration':
                    self.open_patient_form()
                elif role_redirect == 'admin_dashboard':
                    # You can implement admin functionality here
                    QMessageBox.information(self, "Redirect", "Admin Dashboard is under construction!")
                elif role_redirect == 'inventory_management':
                    # Implement inventory management window
                    QMessageBox.information(self, "Redirect", "Inventory Management is under construction!")
                else:
                    QMessageBox.information(self, "Redirect", "Patient Home is under construction!")
            else:
                QMessageBox.warning(self, "Login Failed", "Invalid username or password.")
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Error", f"Server error: {e}")

    def open_patient_form(self):
        self.patient_form = PatientForm()  # Create instance of the PatientForm class
        self.patient_form.show()
        self.close()  # Close login window

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginApp()
    window.show()
    sys.exit(app.exec())
