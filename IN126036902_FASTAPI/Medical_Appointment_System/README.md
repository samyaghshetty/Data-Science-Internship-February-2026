# 🏥 FastAPI Medical Appointment System

## 🚀 Project Overview
This project is a backend system built using FastAPI for managing medical appointments.

It includes patient management, doctor management, appointment booking, and advanced API functionalities.

---

## ⚙️ Features Implemented

### ✅ GET APIs
- Home route
- Get all patients, doctors, appointments
- Get record by ID
- Count total appointments

### ✅ POST APIs with Validation
- Add patient
- Add doctor
- Book appointment
- Pydantic validation with constraints

### ✅ Helper Functions
- find_patient()
- find_doctor()
- find_appointment()

### ✅ CRUD Operations
- Create appointment
- Update appointment
- Delete appointment

### ✅ Multi-Step Workflow
- Appointment → Complete → Cancel → History

### ✅ Advanced APIs
- Search appointments
- Sort appointments
- Pagination
- Combined browsing endpoint

---

## ▶️ Run the Project

```bash
pip install -r requirements.txt
uvicorn main:app --reload
