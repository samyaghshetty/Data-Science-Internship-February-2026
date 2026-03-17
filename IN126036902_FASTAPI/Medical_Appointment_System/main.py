from fastapi import FastAPI, HTTPException, Query, status
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()

# -------------------------------
# In-Memory Database (Sample Data)
# -------------------------------
patients = [
    {"id": 1, "name": "Sam", "age": 21, "gender": "Male"},
    {"id": 2, "name": "Riya", "age": 25, "gender": "Female"},
    {"id": 3, "name": "Amit", "age": 30, "gender": "Male"}
]

doctors = [
    {"id": 1, "name": "Dr. Sharma", "specialization": "Cardiology"},
    {"id": 2, "name": "Dr. Mehta", "specialization": "Dermatology"},
    {"id": 3, "name": "Dr. Khan", "specialization": "Orthopedics"}
]

appointments = [
    {"id": 1, "patient_id": 1, "doctor_id": 1, "date": "2026-03-20", "status": "scheduled"},
    {"id": 2, "patient_id": 2, "doctor_id": 2, "date": "2026-03-21", "status": "completed"},
    {"id": 3, "patient_id": 3, "doctor_id": 3, "date": "2026-03-22", "status": "cancelled"}
]

history = [
    {"id": 2, "patient_id": 2, "doctor_id": 2, "date": "2026-03-21", "status": "completed"},
    {"id": 3, "patient_id": 3, "doctor_id": 3, "date": "2026-03-22", "status": "cancelled"}
]

# -------------------------------
# Pydantic Models
# -------------------------------
class Patient(BaseModel):
    id: int
    name: str = Field(..., min_length=2)
    age: int = Field(..., gt=0)
    gender: str

class Doctor(BaseModel):
    id: int
    name: str
    specialization: str

class Appointment(BaseModel):
    id: int
    patient_id: int
    doctor_id: int
    date: str
    status: str = "scheduled"

# -------------------------------
# Helper Functions
# -------------------------------
def find_patient(patient_id):
    return next((p for p in patients if p["id"] == patient_id), None)

def find_doctor(doctor_id):
    return next((d for d in doctors if d["id"] == doctor_id), None)

def find_appointment(app_id):
    return next((a for a in appointments if a["id"] == app_id), None)

# -------------------------------
# Day 1 - Basic GET APIs
# -------------------------------
@app.get("/")
def home():
    return {"message": "Medical Appointment System Running"}

@app.get("/patients")
def get_patients():
    return patients

@app.get("/doctors")
def get_doctors():
    return doctors

@app.get("/appointments")
def get_appointments():
    return appointments

@app.get("/appointments/count")
def count_appointments():
    return {"total_appointments": len(appointments)}

# -------------------------------
# Day 2 - POST APIs
# -------------------------------
@app.post("/patients", status_code=status.HTTP_201_CREATED)
def add_patient(patient: Patient):
    if find_patient(patient.id):
        raise HTTPException(status_code=400, detail="Patient already exists")
    patients.append(patient.dict())
    return patient

@app.post("/doctors", status_code=status.HTTP_201_CREATED)
def add_doctor(doctor: Doctor):
    if find_doctor(doctor.id):
        raise HTTPException(status_code=400, detail="Doctor already exists")
    doctors.append(doctor.dict())
    return doctor

@app.post("/appointments", status_code=status.HTTP_201_CREATED)
def book_appointment(appointment: Appointment):
    if find_appointment(appointment.id):
        raise HTTPException(status_code=400, detail="Appointment already exists")

    if not find_patient(appointment.patient_id):
        raise HTTPException(status_code=404, detail="Patient not found")

    if not find_doctor(appointment.doctor_id):
        raise HTTPException(status_code=404, detail="Doctor not found")

    appointments.append(appointment.dict())
    return appointment

# -------------------------------
# Day 3 - GET by ID
# -------------------------------
@app.get("/patients/{id}")
def get_patient(id: int):
    patient = find_patient(id)
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    return patient

@app.get("/doctors/{id}")
def get_doctor(id: int):
    doctor = find_doctor(id)
    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")
    return doctor

@app.get("/appointments/{id}")
def get_appointment(id: int):
    appo = find_appointment(id)
    if not appo:
        raise HTTPException(status_code=404, detail="Appointment not found")
    return appo

# -------------------------------
# Day 4 - CRUD Operations
# -------------------------------
@app.put("/appointments/{id}")
def update_appointment(id: int, updated: Appointment):
    appo = find_appointment(id)
    if not appo:
        raise HTTPException(status_code=404, detail="Appointment not found")

    appo.update(updated.dict())
    return appo

@app.delete("/appointments/{id}")
def delete_appointment(id: int):
    appo = find_appointment(id)
    if not appo:
        raise HTTPException(status_code=404, detail="Appointment not found")

    appointments.remove(appo)
    return {"message": "Appointment deleted"}

# -------------------------------
# Day 5 - Multi-Step Workflow
# -------------------------------
@app.post("/appointments/{id}/complete")
def complete_appointment(id: int):
    appo = find_appointment(id)
    if not appo:
        raise HTTPException(status_code=404, detail="Appointment not found")

    appo["status"] = "completed"
    history.append(appo.copy())
    return {"message": "Appointment completed"}

@app.post("/appointments/{id}/cancel")
def cancel_appointment(id: int):
    appo = find_appointment(id)
    if not appo:
        raise HTTPException(status_code=404, detail="Appointment not found")

    appo["status"] = "cancelled"
    history.append(appo.copy())
    return {"message": "Appointment cancelled"}

@app.get("/appointments/history")
def get_history():
    return history

# -------------------------------
# Day 6 - Advanced APIs
# -------------------------------
@app.get("/appointments/search")
def search_appointments(
    keyword: Optional[str] = Query(None),
    status_filter: Optional[str] = Query(None)
):
    result = appointments

    if keyword:
        result = [a for a in result if keyword.lower() in a["date"].lower()]

    if status_filter:
        result = [a for a in result if a["status"] == status_filter]

    return result

@app.get("/appointments/sort")
def sort_appointments(order: str = Query("asc")):
    return sorted(appointments, key=lambda x: x["date"], reverse=(order == "desc"))

@app.get("/appointments/paginate")
def paginate_appointments(
    limit: int = Query(5),
    skip: int = Query(0)
):
    return appointments[skip: skip + limit]

@app.get("/appointments/browse")
def browse_appointments(
    keyword: Optional[str] = Query(None),
    status_filter: Optional[str] = Query(None),
    order: str = Query("asc"),
    limit: int = Query(5),
    skip: int = Query(0)
):
    result = appointments

    if keyword:
        result = [a for a in result if keyword.lower() in a["date"].lower()]

    if status_filter:
        result = [a for a in result if a["status"] == status_filter]

    result = sorted(result, key=lambda x: x["date"], reverse=(order == "desc"))

    return result[skip: skip + limit]
